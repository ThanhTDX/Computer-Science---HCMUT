	.text
	.globl main
	
main:
	li	$t0, 0		#counter
	la	$t1, array	#address of array
	li	$t2, 10		#limiter
loop:				
	beq	$t0, $t2, exit	#t0 used as the counter
	addi	$t0, $t0, 1
	addi	$t1, $t1, 4
	
	li	$v0, 4		#printng msg1
	la	$a0, msg1
	syscall
	
	li	$v0, 5		#getting number and put into array as well as += into $s0
	syscall
	
	sw	$v0, 0($t1)
	add	$s0, $s0, $v0
	j loop
	
exit:	
	li	$v0, 4		#printing msg2
	la	$a0, msg2
	syscall
	li	$v0, 1		#printing number
	move	$a0, $s0
	syscall
	li	$v0, 10		#termination
	syscall
	
	
	.data
array:	.space	40
msg1: .asciiz "Enter number: "
msg2: .asciiz "Result is:"		
newline: .asciiz "\n"	