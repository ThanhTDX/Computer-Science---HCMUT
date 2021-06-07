#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE (1 << 30)

int main() {
	while (1) {
		void * data = malloc(SIZE);
		memset(data, 0, SIZE);
		//printf("Allocated %d MBs\n", SIZE >> 20);
	}
}

