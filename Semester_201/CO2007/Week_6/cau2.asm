	.data
d_a: .double 1.1
d_b: .double 2.2
	.globl main
	.text
main:
	la 	$t0, d_a
	ldc1	$f0, 0($t0)
	la	$t0, d_b
	ldc1	$f2, 0($t0)
	add.d	$f4, $f2, $f0
	
	li	$v0, 10
	syscall
	#	WARNING!!!! 
	#	THE E-LEARNING CODE SNIPSET WON'T COMPILE
	#	BECAUSE VALUE OF D_A AND D_B REQUIRES 2 REGISTERS TO SAVE THE VALUE
	#EG:    la 	$t0, d_a
	#	ldc1	$f0, 0($t0) => $f0, and $f1 will be used to save $t0
	#	la	$t0, d_b
	#	ldc1	$f1, 0($t0) => WON'T WORK since f1 has been used to save d_a
	#	SOLUTION: Instead of $f1 and $f2, save d_b on $f2, and result on $f4
	#	The Copreprocessor will have more space to save all doubles
	
	#1.1	1: Type of d_a and d_b is double, which is more precise than 
	#	float but takes more memory
	#	2: ldc1 (q1: lwc1): save content of value of doubles to a 64-bit 
	#	Copreprocessor1 register
	#	3: add.d (q1: add.s): add 2 doubles and save value in 64-bit register
	#1.2	result is 3.3000000000000003. Although doubles are more precise than
	#	float, it can only extent to 15-digit precision. After that, 
	#	inaccuracies can occur
	#1.3	$f0: 0x3ff199999999999a
	#	$f1: 0x400199999999999a
	#	$f2: 0x400a666666666667
