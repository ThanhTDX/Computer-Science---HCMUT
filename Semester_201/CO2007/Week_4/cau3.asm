#------------------------------------NOTE---------------------------------------
#	This problem utilize the power of branches j
#	But in hindsight, jr and jal produces a better - shorter answer
#0-------------------------------END NOTE---------------------------------------
	
	.globl main
	
main:
	la	$t0, array		#save address of array
	li	$t1, 0			#limit input	
	li	$t2, 0			#counter
	
	li	$v0, 4			#asking for input
	la	$a0, msg1
	syscall
	li	$v0, 5
	syscall
	
	bgt	$v0, 10, invalidIndex	#checking if input is >10
	blt	$v0, 1, invalidIndex	#checking if input is <0
	j 	loop			#and jump to loop
	
loop:
	move	$t1, $v0
	addi	$t2, $t2, 1
	beq	$t2, $t1, validIndex
	addi	$t0, $t0, 4
	j 	loop
	
validIndex:				#YES path
	lw	$s0, 0($t0)
	li	$v0, 4
	la	$a0, msg2
	syscall
	li	$v0, 1
	move	$a0, $t1
	syscall
	li	$v0, 4
	la	$a0, msg3
	syscall
	li	$v0, 1
	move	$a0, $s0
	syscall
	li	$v0, 10
	syscall

invalidIndex:				#NO path
	li	$v0, 4
	la	$a0, msg4
	syscall
	li	$v0, 10
	syscall
	

	.text
	.data
array:  .word	2, 12, 22, 34, 45, 53, 63, 77, 82, 95	#array with 10 elements
msg1: .asciiz "Choose a number (preferrably from 1 to 10): "
msg2: .asciiz "Position at index "
msg3: .asciiz " is: "
msg4: .asciiz "Index invalid, system terminates."