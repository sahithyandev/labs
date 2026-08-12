.data
N: .word 4
A: .word 23,12,5,9,2,14,16,44,21,42,9,8

.bss
B: .word 0,0,0,0

.text
.global main

li t6, -1
li t5, 12 # 3 * N

jal main
li a0,0
li a7,93
ecall


res_triplet:
    # prologue
	addi sp, sp, -32
	sw s0, 0(sp)
	sw s1, 4(sp) 
	sw s2, 8(sp)
	sw s3, 12(sp)
    sw s4, 16(sp)
		
	mv s0, a0 # pointer to A
	mv s1, a1 # j
	mv s2, zero # i
	mv s3, zero # sum
    
    # body
	loop2:
	    beq s2, t5, end_loop2
         # if i == M, exit loop
		
	    add t0, s0, s1
        add t0, t0, s2
	    lw t1, 0(t0) # A[j+i]
	    add s3, s3, t1 # sum += A[i]

		bgez s3, 8
		mul s3, s3, t6 # if sum < 0, multiply by -1

		addi s2, s2, 4 # increment i
		j loop2

    # epilogue
	end_loop2:
		mv t0, zero
		mv t1, zero
		mv a0, s3 # return the sum
		lw s0, 0(sp)
		lw s1, 4(sp) 
		lw s2, 8(sp)
		lw s3, 12(sp)
        lw s4, 16(sp)
		addi sp, sp, 32
    ret

main:
    # prologue
    addi sp, sp, -16
    sw ra, 0(sp)
    
    # body
    la s0, A # pointer to A
	li s1, 0 # j
	la s2, B
    li s3, 0 # i
    # maximum value of i
    lw s4, N
    slli s4, s4, 2

    loop:
		beq s3, s4, end_loop # if i == N, exit loop
        mv a0, s0
        mv a1, s1
		jal res_triplet
		mv t3, a0 # returned value from res_triplet
		
		add t4, s2, s3 # address of B[i]
		sw t3, 0(t4) # store the result in B[i]

		addi s1, s1, 12
		addi s3, s3, 4 # increment i
		j loop

    # epilogue
	end_loop:
		lw ra, 0(sp)
		addi sp, sp, 16
    ret