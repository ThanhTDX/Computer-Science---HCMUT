	.text
	.globl main
	
main:
	li $v0, 4
	la $a0, msg1
	syscall
	
	li $v0, 5
	syscall
	move $s0, $v0
	
	li $v0, 4
	la $a0, msg2
	syscall	
	
	li $v0, 5
	syscall
	move $s1, $v0
	
	add $s0, $s0, $s1
	
	li $v0, 4
	la $a0, sum
	syscall	
	
	li $v0, 1
	move $a0, $s0
	syscall
	li	$v0, 10
	syscall
	.data
msg1: .asciiz "Enter number A:"
msg2: .asciiz "Enter number B:"
sum: .asciiz "A + B = "	
