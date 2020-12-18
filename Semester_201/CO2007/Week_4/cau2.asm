	.globl main
	
main:
	li	$s0, 0		#a, also final results
	li	$s1, 10		#b
	li	$s2, 5		#c
	li	$t0, 99		#input for user	
	
	jal	loop
	
	li	$v0, 4
	la	$a0, msg2
	syscall
	li	$v0, 1		#output results aka a
	move	$a0, $s0
	syscall
	
	li	$v0, 10		#termination
	syscall
	
loop:
	li	$v0, 4
	la	$a0, msg1
	syscall
	li	$v0, 5 		#input number
	syscall
	move	$t0, $v0	#store in t0
	
	beq	$t0, 0, do0	#if t0=0
	beq	$t0, 1, do1	#=1
	beq	$t0, 2, do2	#=2
	j 	loop
do0:
	add	$s0, $s1, $s2	#a = b + c
	jr	$ra
do1:
	sub	$s0, $s1, $s2	#a = b - c
	jr	$ra
do2:
	sub	$s0, $s2, $s1	#a = c - b
	jr	$ra

	.text
	.data
	
msg1: .asciiz "Please input an integer between 0,1,2: "
msg2: .asciiz "Final result is: "
