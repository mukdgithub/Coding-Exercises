#include<stdio.h>

int binary_search(int arr[], int size, int element)
{
	int low,mid,high;
	low=0; high=size-1;
	
	while(low<=high)
	{
		mid=(low+high)/2;
		if(arr[mid]==element)
			return mid;
		
		if(arr[mid]<element)
			low=mid+1;
		else
			high=mid-1;
	}
	return -1;
	
}

int main()
{
	int arr[]={1,23,45,56,67,74,87};
	int size=sizeof(arr)/sizeof(int);
	int element=74;
	int search_index=binary_search(arr,size,element);
	printf(" the element %d was found at index %d ",element,search_index);
}







