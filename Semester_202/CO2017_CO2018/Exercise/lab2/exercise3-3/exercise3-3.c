#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>
#include <sys/types.h>

int main(int argc, char **argv)
{
    pid_t pid1, pid2, pid3;
    printf("A\n");
    pid1 = fork();
    if (pid1 < 0) return 1;
    if (pid1 == 0)
    {
        pid2 = fork();
        if (pid2 < 0) return 1;
        if (pid2 == 0)
        {
            pid3 = fork();
            if (pid3 < 0) return 1;
            if (pid3 == 0) printf("|--B--E--I\n");
            else wait(NULL);
        }
        else
        {
            wait(NULL);
            pid3 = fork();
            {
                if (pid3 < 0) return 1;
                if (pid3 == 0) printf("|--B--F\n");
                else wait(NULL);
            }
        }
    }
    else
    {
        wait(NULL);
        pid2 = fork();
        if (pid2 < 0) return 1;
        if (pid2 == 0)
        {
            pid3 = fork();
            if (pid3 < 0) return 1;
            if (pid3 == 0) printf("|--C--G\n");
            else wait(NULL);
        }
        else
        {
            wait(NULL);
            pid3 = fork();
            if (pid3 < 0) return 1;
            if (pid3 == 0) printf("|--D\n");
            else wait(NULL);
        }
    }
    return 0;
}