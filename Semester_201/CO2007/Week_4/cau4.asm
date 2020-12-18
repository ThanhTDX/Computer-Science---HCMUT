	.globl main
	
main:
	la	$a0, array		#save address of array
	li	$a1, 0			#save register k	
	li	$t0, 0			#counter
	li	$t1, 0			#temporary for swapping
	
	jal	askInput
	jal	loop
	li	$v0, 10
	syscall
	
askInput:
	li	$v0, 5
	syscall
	bgt	$v0, 9, error	
	blt	$v0, 1, error
	jr	$ra
loop:
	move	$a1, $v0
	beq	$t0, $a1, swapValue
	addi	$t0, $t0, 1
	addi	$a0, $a0, 4
	j	loop
swapValue:
	lw	$t1, 0($a0)
	addi	$a0, $a0, 4
	lw	$t2, 0($a0)
	sw	$t1, -4($a0)
	sw	$t2, 0($a0)
	jr	$ra
error:				
	li	$v0, 10
	syscall
	
	.text
	.data
array:  .word	2, 12, 22, 34, 45, 53, 63, 77, 82, 95	#array with 10 elements