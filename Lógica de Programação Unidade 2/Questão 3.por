programa {
  funcao inicio() {
  real nota1, nota2, nota3, total

  escreva("Digite sua primeira nota: ")
  leia (nota1)
  escreva("Digite sua segunda nota: ")
  leia (nota2)  
  escreva("Digite sua terceira nota: ")
  leia (nota3)

  total = (nota1 + nota2 + nota3) / 3

  se (total >= 70){
    escreva("Você obteve a nota ", total, " parabéns foi aprovado.")
  }
    senao {
      escreva("Você obteve a nota ", total, " foi reprovado.")
  }
  }
}
