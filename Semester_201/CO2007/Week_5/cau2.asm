	.globl main
	
main:
	#setup
	li	$s0, 0		#counter
	li	$t0, 0		#input
	li	$s1, 2		#used as divisor
	
	jal	loopmsg		#inputting
	
	li	$v0, 4
	la	$a0, msg3
	syscall
	move	$a0, $s0
	li	$v0, 1
	syscall
	li	$v0, 10		#output
	syscall
loopmsg:
	li	$v0, 4
	la	$a0, msg1
	syscall
	li	$v0, 5 		#input number
	syscall
	move	$t0, $v0	#store in t0
	j 	log_2
log_2:
	div	$t0, $t0, $s1
	mfhi	$t1
	beq	$t1, 1, alarm
	addi	$s0, $s0, 1
	j	log_2
alarm:
	beq	$t0, 0, exitLog
	li	$v0, 4
	la	$a0, msg2
	syscall
	j 	loopmsg	
exitLog:
	jr	$ra

	.text
	.data
msg1: .asciiz "Enter exponent of 2: "
msg2: .asciiz "Invalid, try again.\n"
msg3: .asciiz "Result is: "