	.text
	.globl main
	
main:
	li 	$v0, 4		#Just a warning
	la	$a0, warning	
	syscall
	
	li	$v0, 4		#Input 1st number
	la	$a0, msg1
	syscall
	li	$v0, 5
	syscall
	move	$s0, $v0
	
	li	$v0, 4		#Input 2nd number
	la	$a0, msg1
	syscall
	li	$v0, 5
	syscall
	move	$s1, $v0
	
	li	$v0, 4		#Input 3rd number
	la	$a0, msg1
	syscall
	li	$v0, 5
	syscall
	move	$s2, $v0
	
	li	$v0, 4		#Input 4th number
	la	$a0, msg1
	syscall
	li	$v0, 5
	syscall
	move	$s3, $v0
	
	li	$v0, 4		#Input 5th number
	la	$a0, msg1
	syscall
	li	$v0, 5
	syscall
	move	$s4, $v0
	
	#Printing numbers in reversed order
	li	$v0, 4
	la	$a0, msg2	#Message
	syscall
	move	$a0, $s4
	li	$v0, 1
	syscall
	li	$v0, 4
	la	$a0, spacebar
	syscall
	move	$a0, $s3
	li	$v0, 1
	syscall
	li	$v0, 4
	la	$a0, spacebar
	syscall
	move	$a0, $s2
	li	$v0, 1
	syscall
	li	$v0, 4
	la	$a0, spacebar
	syscall
	move	$a0, $s1
	li	$v0, 1
	syscall
	li	$v0, 4
	la	$a0, spacebar
	syscall
	move	$a0, $s0
	li	$v0, 1
	syscall
	li	$v0, 4
	la	$a0, spacebar
	syscall
	li	$v0, 10
	syscall
	.data
warning: .asciiz "You'll input 5 numbers\n"
msg1: .asciiz "Enter a number:"
msg2: .asciiz "The number in reversed order is :"
spacebar: .asciiz " "	
