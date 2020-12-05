	.data
# ARRAY
array:  .space	40	#40: number of bytes 
	la	$t0, array
	li	$s0, 0
	sw	$s0, 0($t1)
#END ARRAY

	.globl main
	
main:

# FOR LOOP
loop:					
	beq 	$t0, 10, exit
	addi 	$s0, $s0, 30
	addi	$t0, $t0, 1
	j loop
exit:
# END FOR LOOP

# FOR LOOP WITH FUNCTION
loop:					
	beq 	$t0, 10, exit
	addi 	$s0, $s0, 30
	addi	$t0, $t0, 1
	j loop
exit:	jr 	$ra		#Jump to the address saved before (only have 1 - $ra)
	j	*name*		#Jump to another function
	jal	*name*		#Jump to a function, BUT saving the address of the line on $ra (for jr)
# END FOR LOOP WITH FUNCTION

	.text
msg1: .asciiz ""
msg2: .asciiz ""
