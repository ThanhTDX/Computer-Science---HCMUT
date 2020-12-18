	.globl main
	
main:
	li	$s0, 0		#final results
	li	$t1, 0		#holder
	jal	loop
	
	li	$v0, 4
	la	$a0, msg4
	syscall
	li	$v0, 1		#output
	move	$a0, $s0
	syscall
	li	$v0, 10
	syscall
	
loop:				
	li	$v0, 4
	la	$a0, msg1
	syscall
	li	$v0, 5
	syscall
	move 	$t1, $v0
	
	blt	$t1, 0, exit	#condidtion if <0
	add	$s0, $s0, $t1
	
	li	$v0, 4
	la	$a0, msg2
	syscall
	j 	loop
exit:
	li	$v0, 4
	la	$a0, msg3
	syscall
	jr	$ra
	
	.text
	.data
msg1: .asciiz "Enter a number: "
msg2: .asciiz "Number positive, repeat.\n"
msg3: .asciiz "Dectect negative number, out loop.\n"
msg4: .asciiz "Sum of all positive numbers: "
