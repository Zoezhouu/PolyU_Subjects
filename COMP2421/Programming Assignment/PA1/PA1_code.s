#################################################################
# File: PA1.s (Programming Assignment 1)                        #
#                                                               #
# This program is to perform convertions from decimal number to #
# the binary (32-bits) number, the quanternary (16-bits) number,#
# the octal (11-bits). It first asks to input 1 integer through #
# console and then does the digit conversion. Then print out 3  #
# results on the console. Then ask if continue: if continue,    #
# restart with calling main; if does not continue, then break.  #
#################################################################

####################
# The data segment #
####################
	
     .data
# Create some null terminated strings which are to be used in the program
strPrompt:       .asciiz "Enter a number: "
strDec:          .asciiz "Input number is: "
strResultBin:    .asciiz "Binary: "
strResultQua:    .asciiz "Quaternary:"
strResultOct:    .asciiz "Octal: "
strContinue:     .asciiz "Continue? (1=Yes/0=No)"
strBye:          .asciiz "Bye!"
strNew:          .asciiz "\n"
# binary_number    .space 33 # reserve space for binary number(32 bits + null terminator)
# quanternary_number .space 17
# octal_number  .space 12

# example: input decimal: 23
# binary: 0000 0000 0000 0000 0000 0000 0001 0111 (32 bits)
# Quanternary: 0000 0000 0000 0113 (16 bits)
# Octal: 0000 0000 027 (11 bits)

###############################################
# The text segment -- instructions start here #
###############################################

    .text
    .globl main

main:
    # STEP 1 -- get input, read & save decimal input
    # print the prompt (strPrompt)
    li $v0, 4                   # syscall number 4 prints string whose address is in $a0
    la $a0, strPrompt           # load address of the string
    syscall                     # actually print the string

    # read decimal input
    li $v0, 5                   # system call for read integer 
    syscall

    move $s0, $v0               # move input to $s0
    # $s0, saved value: decimal number

    #---------------------------------------------------------------#

    # STEP 2 - print out input decimal number
    # print output message to console
    li $v0, 4                   # system call for print string
    la $a0, strDec              # string
    syscall

    # print input decimal number to console
    li $v0, 1                   
    move $a0, $s0               
    syscall                     # print decimal number

    #---------------------------------------------------------------#
    
    # STEP 3 - convert decimal to binary number
    # print newline
    li $v0, 4
    la $a0, strNew
    syscall

    li $v0, 4 
    la $a0, strResultBin
    syscall                     # print binary string

    # print binary number here
    li $t0, 32                  # set $t0 to 32(32*1 = 32)
Binfor:
    sub $t0, $t0, 1             # $t0 -=1 (2 = 2^1)
    move $t1, $s0               # $t1 = $s0, saved decimal
    srl $t2, $t1, $t0           # $t1 shift right $t0 bits, saved in $t2
    rem $t2, $t2, 2             # remainder of $t2/2, saved in $t2
    move $a0, $t2               
    li $v0, 1
    syscall                     # print remainder($t2)
    bnez $t0, Binfor            # if shift bit != 0, loop


    #---------------------------------------------------------------#
    
    # STEP 4 - convert decimal to quanternary number, print quanternary number
    # print newline
    li $v0, 4
    la $a0, strNew
    syscall

    li $v0, 4
    la $a0, strResultQua
    syscall                     # print quanternary string

    # print quanternary number here
    li $t0, 32                  # set $t0 to 32(16*2 = 32)
Quanfor:
    sub $t0, $t0, 2             # $t0 -= 2(4 = 2^2  32/2=16)
    move $t1, $s0               # $t1 = $s0, saved decimal
    srl $t2, $t1, $t0           # $t1 shift right $t0 bits saved in $t2
    rem $t2, $t2, 4             # remainder of $t2/4, saved in $t2
    move $a0, $t2
    li $v0, 1
    syscall                     # print remainder($t2)
    bnez $t0, Quanfor           # if shift bit != 0, loop

    #---------------------------------------------------------------#
    
    # STEP 5 - convert decimal to octal number, print octal number
    # print newline
    li $v0, 4
    la $a0, strNew
    syscall

    li $v0, 4
    la $a0, strResultOct
    syscall                     # print octal part

    li $t0, 33                  # set $t0 to 3(11*3=33)
Octfor:
    sub $t0, $t0, 3             # $t0 -= 3(8 = 2^3   33/3=11)
    move $t1, $s0               # $t1 = $s0, saved decimal
    srl $t2, $t1, $t0           # $t1 shift right $t0 bits saved in $t2
    rem $t2, $t2, 8             # remainder of $t2/4, saved in $t2
    move $a0, $t2
    li $v0, 1
    syscall                     # print remainder($t2)
    bnez $t0, Octfor            # if shift bit != 0, loop
    
    #---------------------------------------------------------------#

    # STEP 6 - check if user wants to continue
    # print newline
    li $v0, 4
    la $a0, strNew
    syscall

    # print continue string
    li $v0, 4
    la $a0, strContinue
    syscall

    li $v0, 12                  # system callfor read characters
    syscall
    beq $v0, 49, main           # 49 is ASCII code for '1', if $v0 = '1', then run main

    #---------------------------------------------------------------#

    # STEP 7 - bye string
    li $v0, 4
    la $a0, strBye
    syscall

    li $v0, 10                  # exit program
    syscall                     # system call for exit

##################
# End of Program #
##################
