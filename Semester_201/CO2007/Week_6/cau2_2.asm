	.data
d_a: .double 1.50
d_b: .double 2.25
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
	
	#This section is for question 2.4 only