notas = []  

while True:
    entrada = input("Digite uma nota por vez, e depois digite 'sair' para calcular a média: ")
    
    if entrada.lower() == 'sair':
        break

    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida! Digite uma nota entre 0 e 10.")
    except ValueError:
        print("Entrada inválida! Digite um número ou 'sair'.")


if notas:
    media = sum(notas) / len(notas)
    print(f"A média das {len(notas)} notas é: {media:.2f}")
else:
    print("Nenhuma nota válida foi inserida.")