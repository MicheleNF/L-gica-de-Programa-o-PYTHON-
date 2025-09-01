programa
{
	funcao inicio()
	{
		inteiro n, i, contador = 0

		escreva("Digite um número inteiro positivo: ")
		leia(n)

		se (n < 0) {
			escreva("Por favor, digite um número inteiro positivo.")
			retorne
		}

		para (i = 0; i <= n; i++) {
			se (i % 2 == 0) {
				escreva(i, " ")
				contador++
			}
		}
		escreva("\n")
    escreva("Quantidade de números pares: ", contador)
	}
}
