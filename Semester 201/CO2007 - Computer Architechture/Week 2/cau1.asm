	.text
	.globl main
	
main:
	li 	$v0, 4
	la	$a0, msg1
	syscall

	li	$v0, 5
	syscall
	
	addi 	$s0,$v0,1
	li	$v0, 4
	la	$a0, msg2
	syscall
	
	li	$v0, 1
	move	$a0, $s0
	syscall
	li	$v0, 10
	syscall
	
	.data
msg1: .asciiz "Enter number:"
msg2: .asciiz "The +1 equals:"
