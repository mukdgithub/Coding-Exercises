#include<stdio.h>
#include<stdlib.h>

struct myArray
{
	int total_size;
	int used_size;
	int *ptr;
	
};

void createArray(struct myArray *a, int tsize, int usize)
{
	(*a).total_size=tsize;
	(*a).used_size=usize;
	(*a).ptr = (int *)malloc(tsize *sizeof(int));
	
	a->total_size=tsize;
	a->used_size=usize;
	a->ptr = (int *)malloc(tsize *sizeof(int));
}

int main()
{
	struct myArray marks;
	createArray(&marks,100,20);
	
	return 0;
}
