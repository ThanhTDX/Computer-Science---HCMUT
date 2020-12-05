	.text
	.globl 	main
main:
	la	$t0, array	#address of 1st element of array
	li	$t1, 0		#counter
	li	$s0, 0		#sum - results
	li	$t2, 0		#value of elements
	jal 	loop
	
	li	$v0, 1		#output results
	move	$a0, $s0
	syscall
	
	li	$v0, 10		#termination
	syscall
	
loop:
	beq	$t1, 10, exit
	
	lw	$t2, 0($t0)	#load value of elements
	add	$s0, $s0, $t2
	
	addi	$t1, $t1, 1	#counter up
	addi	$t0, $t0, 4	#readdress pointer up for output
	j	loop
exit:
	li	$t1, 0
	li	$t2, 0
				#$t1,$t2: set value to original value aka 0 for future purposes
	jr	$ra
	
	.data 	
array:	.word	1, 2, 67, 4, 12, 6, 33, 8, 9, 10