	.data
s_a: .float 1.1
s_b: .float 2.2
	.globl main
	.text
main:
	la 	$t0, s_a
	lwc1	$f0, 0($t0)
	la	$t0, s_b
	lwc1	$f1, 0($t0)
	add.s	$f2, $f1, $f0
	
	li	$v0, 10
	syscall
	
	#1.1	lwc1: load content of value to Coprocessor1
	#	add.s: add 2 float singles and save value in 32-bit register
	#1.2	can't, since $f0 can be interacted in Coprocessor1, main processor
	#	doesn't have float numbers ($f0) as a type
	#1.3	result is 3.3000002. Because we're using float numbers, in which
	#	can only extent to 6-digits precision, after that, innaccuracies
	#	can occur.$f0	
	#1.4	$f0: 0x3f8ccccd	
	#	$f1: 0x400ccccd
	#	$f2: 0x40533334
