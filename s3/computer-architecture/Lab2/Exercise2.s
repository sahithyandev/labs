.data
    N: .word 12
    A: .word 5,7,6,2,3,7,6,5,1,2,3,4
    B: .word 1,2,3,4,5,6,7,8,9,1,2,3
.bss
    C: .word 0

.global main
.text
main:
    li a1, 0 # iteration variable
    # array pointers
    la a2, A
    la a3, B
    la a7, C
    li t3,-1
    
    # iteration bound
    lw a4, N
    slli a4, a4, 2

loop:
    # load A[i] to t0
    add a5, a2, a1
    lw t0, 0(a5)
    
    # load B[N-i-1] to t1
    add a6,a3,a4
    addi a6,a6,-4
    sub a6,a6,a1
    lw t1,0(a6)
    
    # calculate absolute sum of t0,t1
    add t2,t0,t1
    bgtz t2, 8
    mul t2,t2,t3
    
    # t4 is the target address
    add t4,a7,a1
    sw t2, 0(t4)
    
    # go to next iteration
    addi a1, a1, 4
    blt a1, a4, loop
    
    li a0,0
    li a7,93
    ecall
    ret