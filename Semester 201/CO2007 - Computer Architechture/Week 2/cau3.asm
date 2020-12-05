	.text
	.globl main
	
main:
	li 	$v0, 4
	la 	$a0, msg1
	syscall
	
	li 	$v0, 5	
	syscall
	move 	$s1, $v0	#save new number as a
	
	li 	$v0, 4
	la 	$a0, msg2
	syscall
	
	li 	$v0, 5
	syscall
	move 	$s2, $v0	#save new number as b

	li 	$v0, 4
	la 	$a0, msg3
	syscall
	
	li 	$v0, 5
	syscall
	move 	$s3, $v0	#save new number as c
	
	li 	$v0, 4
	la 	$a0, msg4
	syscall
	
	li 	$v0, 5
	syscall
	move 	$s4, $v0	#save new number as d
	
	#calculating  and printing f
	add 	$t0, $s1, $s2
	sub 	$t1, $s3, $s4
	subi 	$t1, $t1, 2
	sub 	$t0, $t0, $t1	#result of f = (a+b) - (c-d-2)
	
	li 	$v0, 4		#printing f
	la	$a0, sumf
	syscall
	move 	$a0, $t0	
	li 	$v0, 1
	syscall
	
	#calculating  and printing g
	add	$t2, $s1, $s2
	add	$t4, $t2, $t2
	add	$t2, $t2, $t4
	add	$t3, $s3, $s4
	add 	$t3, $t3, $t3
	sub	$t2, $t2, $t3	#result of g = (a+b)*3 - (c+d)*2
	
	li 	$v0, 4		#printing g
	la	$a0, sumg
	syscall
	move 	$a0, $t2	
	li 	$v0, 1
	syscall
	li	$v0, 10
	syscall
	#Comment: g can be calculated using "multi $t2, $t2, 3" but it is introduced in chapter 3, so multi not allowed.
	.data
msg1: .asciiz "Enter number a:"
msg2: .asciiz "Enter number b:"
msg3: .asciiz "Enter number c:"
msg4: .asciiz "Enter number d:"	
sumf: .asciiz "Value of f:"
sumg: .asciiz "\nValue of g:"
