#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>


void outputArr(int arr[], int n)
{
    pid_t pid;
    pid = fork();
    if (pid == 0)
    {
        int total = 0;
        for (int i = 0; i != n; i++)
        {
            if (arr[i] % 3 == 0) 
            total++;
        }
        printf("Child: %d\n", total);
    }
    if (pid > 0)
    {
        int total = 0;
        for (int i = 0; i != n; i++)
        {
            if (arr[i] % 2 == 0) 
            total++;
        }
        printf("Parent: %d\n", total);
    }
}
int main(int argc, char *argv[])
{
    FILE *fp = fopen("numbers.txt", "r");
    if (!fp) 
    {
        printf("FILE NOT FOUND!");
        return -1;
    }

    int numbers[100];
    char word[255];
    int count = 0;
    while(fgets(word, sizeof(word), fp))
    {
        numbers[count] = atoi(word);
        count++;
    } 
    outputArr(numbers, count);
    fclose(fp);
    return 0;
}