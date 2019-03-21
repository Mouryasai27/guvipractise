#include<stdio.h>
int main()
{
	int n,r,d=0,original;
	scanf("%d",&n);
	original=n;
	while(n!=0)
	{
		r = n%10;
		d = d*10+r;
		n = n/10;
	}
	if(original == d){
                printf("yes");
	}
	else{
                printf("no");
	}
	return 0;
}
