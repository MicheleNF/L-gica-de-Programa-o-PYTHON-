programa {
  funcao inicio() {
  inteiro numero


   escreva("Digite um número para saber se é positivo ou negativo: ")
   leia(numero)

  
   se (numero > 0)`{`
      escreva("O número ", numero, " é positivo.")
   }
   senao {
      se (numero < 0)
         escreva("O número ", numero, " é negativo.")
   
      senao 
         escreva("O número ", numero, " é igual a zero.")
   }  
  }
}
