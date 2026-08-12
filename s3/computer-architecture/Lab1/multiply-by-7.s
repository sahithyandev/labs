.globl main
main:
    # Load the value into a0 register
    li a1, 11
    slli a0,a1,3
    sub a0,a0,a1
    ret