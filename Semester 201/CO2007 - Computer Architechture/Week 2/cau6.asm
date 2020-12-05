	.globl main

main:
	li	$a1, 0
	li 	$s7, 0
	li	$t0, 0	
	#setting up, t0 will be used as counters, $s7 as the final results and $a1 as temporary parameter.
# ---------------------INPUT PURPOSE ONLY-----------------------------------------------------------
	#Asking user to input x
	li	$v0, 4
	la 	$a0, msg
	syscall
	li 	$v0, 5
	syscall
	move	$s0, $v0
	
	#Asking to input a,b,c,d
	li	$v0, 4
	la 	$a0, msg1
	syscall
	li 	$v0, 5
	syscall
	move	$s1, $v0	#this is a
	
	li	$v0, 4
	la 	$a0, msg2
	syscall
	li 	$v0, 5
	syscall
	move	$s2, $v0	#this is b
	
	li	$v0, 4
	la 	$a0, msg3
	syscall
	li 	$v0, 5
	syscall
	move	$s3, $v0	#this is c
	
	li	$v0, 4
	la 	$a0, msg4
	syscall
	li 	$v0, 5
	syscall
	move	$s4, $v0	#this is d
#-------------------------MAKING LOOP----------------------------------
	move	$a1, $s1
	jal 	loop		
	add 	$s7, $s7, $a1	#s7 += a*x^3
	move	$a1, $s2
	li	$t0, 1
	jal 	loop
	add 	$s7, $s7, $a1	#s7 += b*x^2
	move	$a1, $s3
	li	$t0, 2
	jal 	loop
	add 	$s7, $s7, $a1	#s7 += c*x
	add 	$s7, $s7, $s4	#s7 += d
	
#NOTE: 	This can be shortened/utilized via recursions, but since I'm bad, I have not found the solution.
#	I will come back, however, and redo the problem again
#------------------------Outputing the results-------------------------
	li	$v0, 4
	la 	$a0, answer
	syscall
	li 	$v0, 1
	move	$a0, $s7
	syscall
	li	$v0, 10
	syscall
#-------------------------LOOP--------------------------------------------------
loop:
	beq 	$t0, 3, exit
	mul	$a1, $a1, $s0
	addi	$t0, $t0, 1
	j loop
exit:	jr	$ra



	.data
msg: .asciiz "Enter x:"
msg1: .asciiz "Enter a:"		
msg2: .asciiz "Enter b:"
msg3: .asciiz "Enter c:"
msg4: .asciiz "Enter d:"
answer: .asciiz "Answer is:"


