n = int (input("Digite um número natural: "))

if n < 1:
    print("Por favor, digite um número natural (maior ou igual a 1).")
else:
    soma = n * (n + 1) // 2
    print(f"A soma dos {n} primeiros números naturais é: {soma}")
