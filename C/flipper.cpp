#include <stdio.h>
#include <locale.h>

int main()
{
	setlocale(LC_ALL,"Portuguese");
	int P, R;
	printf("Digite P e R: ");
	scanf("%d %d", &P, &R);
	if(P == 0) {
		printf("C");
	} else if(R == 1) {
		printf("A");
	} else {
		printf("B");
	}
	return 0;
}

