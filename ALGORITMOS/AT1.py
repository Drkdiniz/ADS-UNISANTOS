# Criando as listas para armazenar as compras e vendas
compras = []
vendas = []

while True:
    print("Menu:")
    print("1. Registrar uma compra")
    print("2. Registrar uma venda")
    print("3. Verificar o saldo total das vendas")
    print("4. Sair do programa")
    
    while True:
        opcao = input("Escolha uma opção: ")
        if opcao in ['1', '2', '3', '4']:
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
    
    if opcao == '1':
        nome_produto = input("Insira o nome do produto: ")
        while True:
            try:
                quantidade = int(input("Insira a quantidade: "))
                break
            except ValueError:
                print("Erro: Você deve inserir um número inteiro para a quantidade.")
        while True:
            try:
                valor_unitario = float(input("Insira o valor unitário: "))
                break
            except ValueError:
                print("Erro: Você deve inserir um número para o valor unitário.")
        compras.append((nome_produto, quantidade, valor_unitario))
        print(f"=====Compra do produto {nome_produto} registrada com sucesso!=====")
        
    elif opcao == '2':
        while True:
            nome_produto = input("Insira o nome do produto: ")
            if nome_produto not in [produto[0] for produto in compras]:
                print("Erro: Este produto não foi cadastrado.")
                continue
            while True:
                try:
                    quantidade = int(input("Insira a quantidade: "))
                    total_comprado = sum([qtd for prod, qtd, val in compras if prod == nome_produto])
                    total_vendido = sum([qtd for prod, qtd, val in vendas if prod == nome_produto])
                    if quantidade > (total_comprado - total_vendido):
                        print(f"Erro: A quantidade vendida não pode exceder a quantidade comprada de {nome_produto}.")
                        continue
                    break
                except ValueError:
                    print("Erro: Você deve inserir um número inteiro para a quantidade.")
            while True:
                try:
                    valor_unitario = float(input("Insira o valor unitário: "))
                    break
                except ValueError:
                    print("Erro: Você deve inserir um número para o valor unitário.")
            vendas.append((nome_produto, quantidade, valor_unitario))
            print(f"Venda do produto {nome_produto} registrada com sucesso!")
            break
        
    elif opcao == '3':
        total_compras = sum([quantidade * valor_unitario for nome_produto, quantidade, valor_unitario in compras])
        total_vendas = sum([quantidade * valor_unitario for nome_produto, quantidade, valor_unitario in vendas])
        
        try:
            lucro = total_vendas - total_compras
            print(f"O lucro total é de {lucro:.2f}")
        except ZeroDivisionError:
            print("Erro: Não há lucro!")
        
    elif opcao == '4':
    
        break