// bubble sort
#include <stdio.h>
int main()
{
    int arr[20],num,x,y,temp; 
    printf("..Enter the Number of Elements : ");
    scanf("%d",&num);    
    printf("..Enter the Elements : ");
    for(x=0;x<num;x++)
        scanf("%d",&arr[x]);
    for(x=0;x<num-1;x++)
	{       
        for(y=0;y<num-x-1;y++)
		{          
            if(arr[y]>arr[y+1])
			{               
                temp=arr[y];
                arr[y]=arr[y+1];
                arr[y+1]=temp;
            }
        }
    }
    printf("Array after bubble sort is : ");
    for(x=0;x<num;x++)
	{
        printf("%d  ",arr[x]);
    }
    return 0;
}

