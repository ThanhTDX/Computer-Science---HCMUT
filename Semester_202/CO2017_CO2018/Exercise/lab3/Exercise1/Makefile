
all:  pi_multi-thread.c		pi_serial.c	
	gcc -pthread -o pi_multi-thread pi_multi-thread.c	
	gcc -pthread -o pi_serial pi_serial.c	
	gcc -pthread -o pi_multi-thread.exe pi_multi-thread.c	
	gcc -pthread -o pi_serial.exe pi_serial.c	
clean:
	rm -f *.o pi_multi-thread	pi_multi-thread.exe
	rm -f *.o pi_serial 		pi_serial.exe