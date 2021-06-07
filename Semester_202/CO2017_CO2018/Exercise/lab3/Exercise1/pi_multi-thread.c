#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>
#include <time.h>


void* calc_num(void *param)
{
    srand((unsigned int)time(NULL));
    int* result = malloc(sizeof(int));

    int value = 0;
    int point_total = atoi(param);
    for (int i = 0; i < point_total/4; i++)
    {
        float x = -1 + rand() / (float) RAND_MAX *2;
        float y = -1 + rand() / (float) RAND_MAX *2;
        if (x*x + y*y <= 1) value++;
    }
    *result = value;
    return (void*) result;
}

int main(int argc, char *argv[])
{
    int point_circle = 0;

    pthread_t p[4];
    for (int i = 0; i < 4; i++)
    {
        pthread_create(&p[i], NULL, &calc_num, argv[1]);  
    }
    for (int i = 0; i < 4; i++)
    {
        int *tmp = NULL;
        pthread_join(p[i], (void**) &tmp); 
        point_circle += *tmp;
        free(tmp);
    }
    printf("%f\n", (float)4*point_circle/atoi(argv[1]));
    return 0;
}
