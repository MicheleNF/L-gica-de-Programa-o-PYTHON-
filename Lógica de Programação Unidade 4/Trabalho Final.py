import os

# Banco de dados e estoque minimo 
estoque = {}
ESTOQUE_MINIMO = 5

# Funções
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def cadastrar_produto():
    try:
        id_produto = input("ID do produto: ").strip()
        if id_produto in estoque:
            print("Produto já cadastrado.")
            return
        nome = input("Nome: ").strip()
        categoria = input("Categoria: ").strip()
        quantidade = int(input("Quantidade em estoque: "))
        preco = float(input("Preço: R$ "))
        estoque[id_produto] = {
            'nome': nome,
            'categoria': categoria,
            'quantidade': quantidade,
            'preco': preco
        }
        print("Produto cadastrado com sucesso.")
    except ValueError:
        print("Erro: Digite valores numéricos válidos para quantidade e preço.")

def editar_produto():
    id_produto = input("ID do produto a editar: ").strip()
    if id_produto not in estoque:
        print("Produto não encontrado.")
        return
    try:
        nome = input("Alterar nome: ").strip()
        categoria = input("Alterar categoria: ").strip()
        quantidade = int(input("Alterar quantidade: "))
        preco = float(input("Alterar preço: R$ "))
        estoque[id_produto].update({
            'nome': nome,
            'categoria': categoria,
            'quantidade': quantidade,
            'preco': preco
        })
        print("Produto atualizado com sucesso.")
    except ValueError:
        print("Erro: Quantidade e preço devem ser válidos.")

def deletar_produto():
    id_produto = input("ID do produto a apagar: ").strip()
    if estoque.pop(id_produto, None):
        print("Produto removido.")
    else:
        print("Produto não encontrado.")

def movimentar_estoque():
    id_produto = input("ID do produto: ").strip()
    if id_produto not in estoque:
        print("Produto não encontrado.")
        return
    operacao = input("Entrada (E) ou Saída (S): ").strip().upper()
    try:
        quantidade = int(input("Quantidade: "))
        if operacao == 'E':
            estoque[id_produto]['quantidade'] += quantidade
            print("Entrada registrada.")
        elif operacao == 'S':
            if quantidade <= estoque[id_produto]['quantidade']:
                estoque[id_produto]['quantidade'] -= quantidade
                print("Saída registrada.")
            else:
                print("Erro: Estoque insuficiente.")
        else:
            print("Operação inválida.")
    except ValueError:
        print("Erro: Digite uma quantidade válida.")

def consultar_produto():
    criterio = input("Buscar por ID (I), Nome (N) ou Categoria (C): ").strip().upper()
    chave = input("Digite o valor da busca: ").strip().lower()
    encontrados = []
    for id, dados in estoque.items():
        if (criterio == 'I' and id.lower() == chave) or \
           (criterio == 'N' and dados['nome'].lower() == chave) or \
           (criterio == 'C' and dados['categoria'].lower() == chave):
            encontrados.append((id, dados))
    if encontrados:
        for id, dados in encontrados:
            print(f"ID: {id} | Nome: {dados['nome']} | Categoria: {dados['categoria']} | Quantidade: {dados['quantidade']} | Preço: R$ {dados['preco']:.2f}")
    else:
        print("Nenhum produto encontrado.")

def relatorio_estoque():
    if not estoque:
        print("Estoque vazio.")
    for id, dados in estoque.items():
        print(f"ID: {id} | Nome: {dados['nome']} | Categoria: {dados['categoria']} | Quantidade: {dados['quantidade']} | Preço: R$ {dados['preco']:.2f}")

def relatorio_baixo_estoque():
    alerta = False
    for id, dados in estoque.items():
        if dados['quantidade'] < ESTOQUE_MINIMO:
            print(f"ALERTA - ID: {id} | Nome: {dados['nome']} | Quantidade: {dados['quantidade']}")
            alerta = True
    if not alerta:
        print("Nenhum dos produto está com baixo estoque.")

# Menu principal
def menu():
    while True:
        print("\n=== SISTEMA DE ESTOQUE ===")
        print("1. Cadastrar Produto")
        print("2. Alterar Produto")
        print("3. Deletar Produto")
        print("4. Entrada/Saída de Produto")
        print("5. Consultar Produto")
        print("6. Relatório de Estoque")
        print("7. Relatório de Baixo Estoque")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_produto()
        elif opcao == '2':
            editar_produto()
        elif opcao == '3':
            deletar_produto()
        elif opcao == '4':
            movimentar_estoque()
        elif opcao == '5':
            consultar_produto()
        elif opcao == '6':
            relatorio_estoque()
        elif opcao == '7':
            relatorio_baixo_estoque()
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

        input("\nPressione Enter para continuar...")
        limpar_tela()

# Iniciar o sistema
menu()
