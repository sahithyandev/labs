.equ N 8

.data
A: .word 7,3,25,4,75,2,1,1
newline: .string "\n"

.bss
B: .word 0, 0, 0, 0, 0, 0, 0, 0

.text
.globl main

jal main
li a0,0
li a7,93
ecall

MaxVector:
    addi sp, sp, -16
    sw s1, 0(sp)

    mv s1, zero
    mv t2, zero
    loop2:
        beq s1, a1, endloop2
        lw t1, 0(a0)
        ble t1, t2, else2
        mv t2, t1
        mv t3, a0
        else2:
        addi a0, a0, 4
        addi s1, s1, 1
        j loop2
        
    endloop2:
    sw zero, 0(t3)
    mv a0, t2
    lw s1, 0(sp)
    addi sp, sp, 16
    ret

SortVector:
    addi sp, sp, -32
    sw s1, 0(sp)
    sw s2, 4(sp)
    sw s3, 8(sp)
    sw ra, 12(sp)
    mv s1, a0 # Address of vector A
    mv s2, a1 # Address of vector B
    mv s3, a2 # Size of vectors A and B
    mv t1, zero

    loop1:
        beq t1, s3, endloop1
        mv a0, s1
        mv a1, s3
        sw t1, 16(sp)
        jal MaxVector
        lw t1, 16(sp)
        sw a0, 0(s2)
        
        li a7, 1
        ecall
        la a0, newline
        li a7, 4
        ecall
        
        addi s2, s2, 4
        addi t1, t1, 1
        j loop1
        
    endloop1:
    li a0 0
    lw s1, 0(sp)
    lw s2, 4(sp)
    lw s3, 8(sp)
    lw ra, 12(sp)
    addi sp, sp, 32
    ret
    
main:
    addi sp, sp, -16
    sw ra, 0(sp)

    la a0, A
    la a1, B
    addi a2, zero, N
    jal SortVector

    li a0 0
    lw ra, 0(sp)
    addi sp, sp, 16
    ret
    