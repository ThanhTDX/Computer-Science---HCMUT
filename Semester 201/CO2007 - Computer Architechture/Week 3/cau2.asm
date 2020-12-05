	.text
	.globl 	main
main:
	la	$t0, array	#address of 1st element of array
	li	$t1, 0		#counter
	li	$s0, 0		#sum - results of even elements
	li	$s1, 0		#sum - results of odd elements
	li	$t2, 0		#value of elements
	jal 	loop
	
	li	$v0, 1		#output results of even elements
	move	$a0, $s0
	syscall
	
	li	$v0, 4		#spacebar
	la	$a0, spacebar
	syscall
	
	li	$v0, 1		#output results of odd elements
	move	$a0, $s1
	syscall
	
	li	$v0, 10		#termination
	syscall
	
loop:
	#LOOP EVEN ELEMENTS
	beq	$t1, 10, exit	
	
	lw	$t2, 0($t0)	#load value of elements
	add	$s0, $s0, $t2
	
	addi	$t1, $t1, 1	#counter up
	addi	$t0, $t0, 4	#readdress pointer up for output
	#END OF LOOP EVEN ELEMENTS
	
	#LOOP ODD ELEMENTS
	beq	$t1, 10, exit
	
	lw	$t2, 0($t0)	#load value of elements
	add	$s1, $s1, $t2
	
	addi	$t1, $t1, 1	#counter up
	addi	$t0, $t0, 4	#readdress pointer up for output
	#END OF ODD ELEMENTS
	j	loop
exit:
	li	$t1, 0
	li	$t2, 0
				#$t1,$t2: set value to original value aka 0 for future purposes
	jr	$ra
	
	.data 	
array:	.word	1, 2, 3, 4, 5, 6, 7, 8, 9, 10
spacebar: .asciiz " "