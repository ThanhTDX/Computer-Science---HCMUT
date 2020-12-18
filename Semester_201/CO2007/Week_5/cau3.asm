	.globl main
	
main:
	li	$s0, 0		#store a of mflo
	li	$s1, 0		#store a of mfhi
	li	$s2, 10		#b
	li	$s3, 7		#c
	li	$t0, 0		#input
	li	$t1, 0		#counter
	
	li	$v0, 4		#input
	la	$a0, msg1
	syscall
	li	$v0, 5		#end input
	syscall
	move	$t0, $v0	#store input into t0
	
	
	blt	$t0, 0, invalid	#condition for 0->4
	bgt	$t0, 4, invalid	
	
	jal	switchCase
	
	li	$v0, 4		#output
	la	$a0, msg3
	syscall
	li	$v0, 1
	move	$a0, $s0
	syscall
	li	$v0, 4
	la	$a0, spacebar
	syscall
	li	$v0, 1
	move	$a0, $s1	#end output
	syscall
	
	li	$v0, 10
	syscall
switchCase:		
	
	beq	$t0, $t1, case0
	addi	$t1, $t1, 1
	beq	$t0, $t1, case1	
	addi	$t1, $t1, 1
	beq	$t0, $t1, case2
	addi	$t1, $t1, 1
	beq	$t0, $t1, case3
	addi	$t1, $t1, 1
	beq	$t0, $t1, case4
case0:
	add	$s0, $s2, $s3	#case 0
	jr	$ra
case1:	
	sub	$s0, $s2, $s3
	jr	$ra
	
case2:	
	mult	$s2, $s3
	mflo	$s0
	mfhi	$s1
	jr	$ra
	
case3:	
	div	$s2, $s3
	mflo	$s0
	jr	$ra
case4:	
	div	$s2, $s3
	mfhi	$s0
	jr	$ra
	
#-This is me being very lazy, the right solution requires only 1 calculation
invalid:
	li	$v0, 4
	la	$a0, msg2
	syscall
	li	$v0, 10
	syscall
	
	.text
	.data
msg1: .asciiz "Choose a number from 0 to 4: "
msg2: .asciiz "Your choice is invalid."
msg3: .asciiz "Result is: "
spacebar: .asciiz " "