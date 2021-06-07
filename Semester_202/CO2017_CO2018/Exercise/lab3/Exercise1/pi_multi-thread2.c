#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
int num = 4;
float circle_points=0.0f;
float square_points=0.0f;

struct point
{
	float x;
	float y;
};
float RandomGenerator()
{
	float n;
	n=((float)rand()/RAND_MAX)*(float)(2.0);
	printf("%f | \n",n);
	return n;
}
void GetPoints(struct point p)
{
	int d=p.x*p.x+p.y*p.y;
	if(d<=1){
		circle_points+=1;
	}
	square_points+=1;
	
}
void* GeneratePoint(void* argc)
{
	struct point tempt;
	tempt.x=RandomGenerator();	
	tempt.y=RandomGenerator();
	GetPoints(tempt);
	pthread_exit(0);
}
int main()
{
	pthread_t threads[num];
	for(int i=0;i<num;i++)
	{
		pthread_create(&threads[i],NULL,GeneratePoint,NULL);
	}
	pthread_join(threads[0],NULL);
	float pi=4*(circle_points/square_points);
	printf("Pi: %f",pi);
	printf("\n");
	
	return 0;
}
