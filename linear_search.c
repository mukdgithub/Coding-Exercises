// linear search
#include<stdio.h>
int main()
{
    {
        int i,n,c=0;
        double s;
        printf("\n..ENTER THE NUMBER OF ELEMENTS..");
        scanf("%i",&n);
        double arr[n];
        printf("\n..ENTER THE ELEMENTS..");
        for(i=0;i<n;i++)
        {
            scanf("%d",&arr[i]);
        }
        printf("\n..ENTER THE ELEMENT TO BE SEARCHED..");
        scanf("%d",&s);
        for(i=0;i<n;i++)
        {
            if(s==arr[i])
                c=1;
        }
        if(c==1)
            printf("\n..THE ELEMENT IS PRESENT..");
        else
            printf("\n..THE ELEMENT IS NOT PRESENT..");
    }
}
