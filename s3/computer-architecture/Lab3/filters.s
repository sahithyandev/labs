.data
N: .word 6
A: .word 48,64,56,80,96,48

.bss
B: .word 0

.text
.global main

jal main
li a0, 0
li a7, 93
ecall
ret


my_filter:
    # prologue
    addi sp, sp, -32
    
    sw ra, 0(sp)
    sw s0, 4(sp)
    sw s1, 8(sp)
    sw s2, 12(sp)
    sw s3, 16(sp)
    sw s4, 20(sp)
    
    # body
    li t6, 0
    bgt a0, a1, skip_setting_one
    andi a0, a0, 15
    bnez a0, skip_setting_one
    li t6, 1
    
    skip_setting_one:
    mv a0, t6
    # epilogue
    lw ra, 0(sp)
    lw s0, 4(sp)
    lw s1, 8(sp)
    lw s2, 12(sp)
    lw s3, 16(sp)
    lw s4, 20(sp)  
    addi sp, sp, 32
    ret

main:
    addi sp, sp, -16
    sw ra, 0(sp)
    
    la s0, A
    la s1, B
    li s2, 0 # i
    li s3, 0 # j
    lw s4, N # bound for lopp
    addi s4, s4, -1
    slli s4, s4, 2
    
    loop:
        beq s2, s4, end_loop
        add t0, s0, s2
        lw a0, 0(t0)
        lw a1, 4(t0)
        jal my_filter
        addi s2, s2, 4 
        beqz a0, loop
        
        add t1, s1, s3
        lw a0, 0(t0)
        lw a1, 4(t0)
        add a0, a0, a1
        addi a0, a0, 2
        sw a0, 0(t1)
        addi s3, s3, 4
        j loop
        
    end_loop:
        lw ra, 0(sp)
        addi sp, sp, 16
    ret