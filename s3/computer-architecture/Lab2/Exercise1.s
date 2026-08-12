.data
    N: .word 12
    A: .word 0, 1, 2, 7, -8, 4, 5, 12, 11, -2, 6, 3
    sizeOfB: .word 0
.bss
    B: .word 0
    
.global main
.text
main:
    li a1, 0 # loop variable
    
    # a2 is the upper limit
    # calculated by multiplying numOfElements by 4
    lw a2, N
    slli a2, a2, 2
    
    # a3 - pointer to the array
    la a3, A
    la a5, B
    
    # a4 - current item's memory position
    add a4, a3, a1
    lw a0, 0(a4)
    
    blt a0, zero, 20
    andi t0, a0, 1
    bnez t0, 12
    
    sw a0, 0(a5)
    addi a5, a5, 4  
    
    # go to next iteration
    addi a1, a1, 4
    blt a1, a2, -32
    
    li a0, 0
    li a7, 93
    ecall
    
    ret
    