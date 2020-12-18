	.globl main
	
main:
#-----------Multiplication------------
	lui	$t0, 0x5000
	li	$t1, 4
	mult	$t0, $t1
	mflo	$s0
	mfhi	$s1
#-----------Divsion-------------------
	li	$t0, 10
	li	$t1, 7
	div	$t0, $t1
	mflo	$s0
	mfhi	$s1
#-----------Exit-------------------
	li	$v0, 10
	syscall
	
	#1.1	mfhi $s0
	#	mflo $s1
	#1.2	$s0: 0x40000000
	#	$s1: 0x00000001
	#1.3	$s0: 0x00000001
	#	$s1: 0x00000003
	#1.4	$s0: save upper 64-bit of answer 
	#	$s1: save lower 64-bit of answer
	#1.5	$s0: save quotient of answer
	#	$s1: save remainder of answer
	#1.6	No
