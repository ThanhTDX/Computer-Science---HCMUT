	.text
	.globl main
	
main:
	li	$t0, 0		#counter
	la	$t1, array	#address of 1st element array
	li	$t2, 10		#limit
	
	jal 	loop		#input elements into array 
	
	li	$v0, 4
	la	$a0, msg2
	syscall

	addi	$t1, $t1, -4	#readdress pointer to array[i]
	jal	reverseLoop
	
	li	$v0, 10
	syscall
loop:				
	beq	$t0, $t2, exit

	
	li	$v0, 4		#print msg1
	la	$a0, msg1
	syscall
	
	li	$v0, 5		#get number
	syscall
	
	sw	$v0, 0($t1)	#saving element of array
	
	addi	$t0, $t0, 1
	addi	$t1, $t1, 4	#readdress pointer up for input
	j loop
	
reverseLoop:				
	beq	$t0, 0, exit	
	
	li	$v0, 1		#output element of array
	lw	$a0, 0($t1)
	syscall	
	
	li	$v0, 4		#spacebar
	la	$a0, spacebar
	syscall
	
	addi	$t0, $t0, -1
	addi	$t1, $t1, -4	#readdress pointer down for output
	j 	reverseLoop
exit:	jr	$ra

	.data
array:	.space	40
msg1: .asciiz "Enter number: "
msg2: .asciiz "Result is:"		
newline: .asciiz "\n"	
spacebar: .asciiz " "
