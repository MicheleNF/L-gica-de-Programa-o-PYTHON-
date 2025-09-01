n = int(input("Digite um número inteiro N para calcular o fatorial: "))

if n < 0:
    print("Não é possível calcular o fatorial de número negativo.")
else:
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    print(f"O fatorial de {n} é: {fatorial}")
    