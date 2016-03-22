#include <stdio.h>
#include <locale.h>

int main()
{
	setlocale(LC_ALL,"Portuguese");
	float C, F;
	printf("Digite a temperatura em Fahrenheit: ");
	scanf("%f", &F);
	C=(5*(F-32))/9;
	printf("A temperatura em Celsius é: %.2f", C);
	return 0;
}

