	.data
	.text
	.globl main

main:
	addiu  	$s0, $s0, 66000
loop:					#for loop for +30
	beq 	$t0, 10, exit
	addi 	$s0, $s0, 30
	addi	$t0, $t0, 1
	j loop
exit: 	move 	$t0, $0
	subi	$s0, $s0, 6000
	addi	$s0, $s0, 25
	move	$a0, $s0
	li	$v0, 1
	syscall
	li	$v0, 10
	syscall

