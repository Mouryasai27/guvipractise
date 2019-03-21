#include<stdio.h>
int main()
{
	int n,r,d=0;
	scanf("%d",&n);
	while(n!=0)
	{
		r = n%10;
		d = d*10+r;
		n = n/10;
	}
	if(n == d){
                printf("yes");
	}
	else{
                printf("no");
	}
	return 0;
}
