#include "mem.h"
#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <time.h>

void proc_test(){
	int i;
	int index = 0;
	char * mem[5];
	int arr_alloc[5] = {115, 500, 358, 200, 375};
	for (i = 0; i < 5; i++) {
		/* Allocate memory */
		mem[index] = mem_alloc(arr_alloc[i]);
		if (mem[index] != NULL) {
			index++;
		}
	}
}


int main() {
	
	srand(time(NULL));
	
	mem_init(2325);
	
	proc_test();
	
	mem_finish();
	
}