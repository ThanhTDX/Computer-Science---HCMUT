	.text
	.globl 	main
main:
	la	$t0, array	#address of 1st element of array
	li	$t1, 1		#counter
	li	$s0, 0		#saved when user input value
	li	$t2, 0		#value of elements
	
	jal	askInput
	jal 	loop
	
	lw	$t2, 0($t0)	#load value of elements
	move	$s1, $t2
	
	li	$v0, 4		#output results
	la	$a0, msg1
	syscall	
	li	$v0, 1		
	move	$a0, $t2
	syscall
	
	li	$t1, 1		#set value back to orignial value - 0 for future purposes
	li	$t2, 0
	li	$v0, 10		#termination
	syscall

askInput:
	li	$v0, 4		#ask input
	la	$a0, msg
	syscall
	li	$v0, 5
	syscall
	move	$s0, $v0
	
	ble 	$s0, 0, invalid		#condition
	bgt	$s0, 10, invalid	
	j	exit
loop:
	beq	$t1, $s0, exit
	addi	$t1, $t1, 1	#counter up
	addi	$t0, $t0, 4	#readdress pointer up for output
	j	loop
exit:	
	jr	$ra
invalid:
	li	$v0, 4
	la	$a0, msg2
	syscall
	j 	askInput
	
	.data 	
array:	.word	6, 27, 67, 95, 12, 61, 33, 39, 55, 53
msg:	.asciiz	"Choose a number between 1 to 10: "
msg1:	.asciiz "Value at index you choose is: "
msg2: 	.asciiz "Invalid, choose again.\n"