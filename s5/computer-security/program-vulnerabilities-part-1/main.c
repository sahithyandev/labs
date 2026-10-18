// Use
//
// clang -fno-stack-protector -D_FORTIFY_SOURCE=0 -o main main.c -Wno-deprecated-declarations
// 
// to compile this file. Otherwise the security hardening features of
// these compilers would crash the program


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 1. Stack smashing
// NOTE: on macOS (ASLR + pointer auth on arm64), a long input here crashes
// with SIGBUS instead of returning to attacker-chosen code. This proves that
// the return address was overwritten. a real hijack needs a
// fixed load address, e.g. ASLR disabled.
void stack_smashing() {
    char canary[4] = "OK"; // sits next to buffer; if this changes, buffer overran it
    char buffer[10];
    printf("buffer is at %p, size 10. canary starts as \"%s\"\n", (void*)buffer, canary);
    // VULN: when the attacker inputs a longer string
    gets(buffer);
    printf("Data inside the buffer is: %s\n", buffer);
    printf("%s: canary is now \"%s\"\n",
           strcmp(canary, "OK") ? "VULNERABLE (canary overwritten)" : "safe this run", canary);
}


// 2. No range checking
void no_range_checking() {
    int values[5] = {1,2,3,4,5};
    printf("values array is at %p, length 5\n", (void*)values);
    printf("Enter an index: ");
    int index;
    // VULN: when the attacker inputs an index value that is higher than 4 (LENGTH-1)
    scanf("%d", &index);
    printf("%s: reading values[%d] (valid range is 0-4)\n",
           (index < 0 || index > 4) ? "VULNERABLE (index out of bounds)" : "safe", index);
    printf("Value at index: %d\n", values[index]);
}

// 3. Overflow and exploit adjacent variables
void buffer_overflow_variables() {
    char a[6] = "SECRET";
    char buffer[10];
    printf("a is at %p, buffer is at %p\n", (void*)a, (void*)buffer);
    // VULN: when the attacker inputs a longer string, causing it to overflow into a
    gets(buffer);
    printf("%s: a is now \"%s\"\n",
           strcmp(a, "SECRET") ? "VULNERABLE (a overwritten)" : "safe this run", a);
}

// 4. Code execution with pointer exploitation
// NOTE: same macOS ASLR issue as #1 - normal/hijacked's addresses change on
// every run, so a payload built from one run's printed address won't line
// up with the next run's fn_ptr slot; it crashes (SIGBUS) instead of
// jumping to hijacked(). Works as a real redirect on Linux with ASLR off.
void normal() { printf("Normal function called\n"); }
void hijacked() { printf("Hijacked function called\n"); }

void pointer_exploitation() {
    // struct keeps buffer and fn_ptr adjacent in memory
    struct {
        char buffer[10];
        void (*fn_ptr)(void);
    } s = { "", normal };
    printf("normal is at %p, hijacked is at %p, fn_ptr slot is at %p\n",
           (void*)normal, (void*)hijacked, (void*)&s.fn_ptr);
    // VULN: a longer string overflows buffer and overwrites fn_ptr
    gets(s.buffer);
    if (s.fn_ptr == hijacked) {
        printf("VULNERABLE (fn_ptr redirected to hijacked): ");
        s.fn_ptr();
    } else if (s.fn_ptr == normal) {
        printf("safe this run: fn_ptr still points to normal: ");
        s.fn_ptr();
    } else {
        printf("VULNERABLE (fn_ptr overwritten to garbage %p) - not calling it, would crash\n",
               (void*)s.fn_ptr);
    }
}

int main(int argc, char *argv[]) {
    // run one demo at a time so an early crash doesn't block the rest
    int which = argc > 1 ? atoi(argv[1]) : 0;
    switch (which) {
        case 1: stack_smashing(); break;
        case 2: no_range_checking(); break;
        case 3: buffer_overflow_variables(); break;
        case 4: pointer_exploitation(); break;
        default:
            printf("Usage: %s <1-4>\n"
                   "  1 stack_smashing  2 no_range_checking\n"
                   "  3 buffer_overflow_variables  4 pointer_exploitation\n", argv[0]);
    }
    return 0;
}
