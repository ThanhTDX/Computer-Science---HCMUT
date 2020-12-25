	.data
msg1: .asciiz "Input Fahrenheit: "
warning: .asciiz "Warning"
safe: .asciiz "Safe"
fp1: .float 32
fp2: .float 5
fp3: .float 9
fp4: .float 99.5
	.globl main
	.text
main:
	l.s	$f4, fp4	
	l.s	$f1, fp1
	l.s	$f2, fp2
	l.s	$f3, fp3
	
	# 	since C = (F - 32)*5/9, we set immediates as the formula
	#	and 99.5 as the comparison
	
	li	$v0, 4
	la	$a0, msg1
	syscall
	li	$v0, 6		#ask input, saved in f0 (note: since we use float, code 6)
	syscall
	
	sub.s	$f0, $f0, $f1	#calculation
	mul.s	$f0, $f0, $f2
	div.s	$f0, $f0, $f3
	
	c.le.s	$f4, $f0	#compare to 99.5
	bc1t	warningPath
	bc1f	safePath
warningPath:			#bigger path
	li	$v0, 4
	la	$a0, warning
	syscall
	li	$v0, 10
	syscall
safePath:			#smaller path
	li	$v0, 4
	la	$a0, safe
	syscall
	li	$v0, 10
	syscall
	
