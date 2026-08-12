.data
    N: .word 12
    V: .word 0,1 # initialized with first 2 elements

.global main
.text
main:
    li a1, 8 # to account for the first 2 elements
    lw a2,N
    slli a2,a2,2
    
    # last 2 values
    li t0, 0
    li t1, 1

loop:
    # calculate next value
    add t2, t0, t1
        
    # update last 2 values
    mv t0,t1
    mv t1,t2
    
    # store latest value in the array
    la a3, V
    add a4,a3,a1 
    sw t2, 0(a4)

    # go to next iteration
    addi a1,a1,4
    blt a1,a2,loop
    
    li a0, 0
    li a7, 93
    ecall
    ret

    