#include <stdio.h>
#include <locale.h>

int main()
{
	setlocale(LC_ALL,"Portuguese");
	float nota1, nota2, media;
	printf("Digite sua primeira nota: ");
	scanf("%f", &nota1);
	printf("Digite sua segunda nota: ");
	scanf("%f", &nota2);
	media=(nota1+nota2)/2;
	if(media >= 7) {
		printf("Voc� foi aprovado! Com m�dia: %f", media);
	} else {
		printf("Voc� foi reprovado! Com m�dia: %f", media);
	}
	return 0;
}

