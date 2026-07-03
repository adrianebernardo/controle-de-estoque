import json  # serve para carregar e salvar os arquivos json
import os    # serve para o código verificar se o arquivo existe antes de tentar abrir

# a variável guarda o endereço de onde os dados estão salvos
ARQUIVO = "estoque.json"

# commit 1:
def carregar_dados():
    if not os.path.exists(ARQUIVO): # se o arquivo ainda não existe (primeira vez rodando o
        # programa), não tem o que carregar
        return []
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f: # "r" = ler | "utf-8" = é uma forma
            # de codificação para o Python não retornar com palavras estranhas!
            return json.load(f) # transforma o texto do arquivo em dados que o Python entende
        # como listas e dicionários
    except Exception:
        print("Não consegui ler o arquivo salvo. Vou começar com o estoque vazio.")
        return [] # protege contra o arquivo corrompido

def salvar_dados(lista_produtos): # "lista_produtos" é a lista inteira de produtos cadastrados
    try:
        with open(ARQUIVO, "w", encoding="utf-8") as f: # "w" = escrever
            json.dump(lista_produtos, f, indent=4, ensure_ascii=False) # "json.dump" = little
            # bro do "json.load" e faz o caminho inverso ao dele: pega a lista/dicionário do
            # Python e escreve ela no arquivo já formatada como texto JSON | "indent=4" =
            # formata bonito; ensure_ascii=False = preserva os acentos
        print("Dados salvos com sucesso em estoque.json! <3")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")

# commit 2:
def pedir_quantidade(): # fica repetindo até receber um número inteiro válido (a "dica" do
    # enunciado é exatamente essa: se a pessoa digitar "dez", não pode quebrar!)
    while True:
        try:
            qtd = int(input("Quantidade: "))
            if qtd < 0:
                print("A quantidade não pode ser negativa! >:(")
                continue # para tudo! e volta para o começo do while
            return qtd
        except ValueError: # para o Python não mostrar esse erro feio e crashar tudo,
            # ele mostra o print bonitinho!
            print("Entrada inválida! Digite um número inteiro (ex: 10), não texto (ex: 'dez').")

def pedir_preco(): # mesma lógica da quantidade, só que aceitando número decimal (float)
    while True:
        try:
            preco = float(input("Preço unitário (ex: 19.90): "))
            if preco < 0:
                print("O preço não pode ser negativo! >:(")
                continue
            return preco
        except ValueError:
            print("Entrada inválida! Digite um número (ex: 19.90), não texto.")

def cadastrar_produto(): # pede os 3 dados do produto e devolve um dicionário pronto
    print("\n--- CADASTRAR PRODUTO ---")
    nome = input("Nome do produto: ").strip() # strip = remove espaços extras no começo/fim
    if not nome: # confere se o nome foi digitado
        print("O nome do produto não pode ser vazio!")
        return None # devolve None pra avisar quem chamou que não rolou o cadastro

    quantidade = pedir_quantidade()
    preco = pedir_preco()

    produto = { # o tal do dicionário
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }
    return produto # quem chamou (o menu) que decide o que fazer com esse dicionário

# commit 3:
def listar_produtos(lista_produtos):
    print("\n--- LISTA DE PRODUTOS ---")
    if not lista_produtos: # lista vazia = nenhum produto foi cadastrado ainda
        print("Nenhum produto cadastrado até o momento, loser.")
        return
    # decorações omagaaa
    print(f"{'Produto':<20} | {'Quantidade':<10} | {'Preço unitário':<15}")
    print("-" * 50) # linha separadora só pra ficar bonitinho
    for item in lista_produtos: # percorre cada produto e imprime formatado igual o cabeçalho
        print(f"{item['nome']:<20} | {item['quantidade']:<10} | R$ {item['preco']:<12.2f}")

# commit 4:
def estatisticas(lista_produtos): # calcula tudo que o enunciado pede: total, mais caro
    # e mais barato — sem imprimir nada aqui, só calcula e devolve (é a função quem faz
    # as contas usando return, o menu que decide como mostrar)
    if not lista_produtos: # se não tem produto, não dá pra calcular estatística nenhuma
        return None

    total = sum(item["quantidade"] * item["preco"] for item in lista_produtos) # soma de
    # qtd * preço de cada item, tudo numa linha só (list comprehension com sum)

    mais_caro = max(lista_produtos, key=lambda item: item["preco"]) # "key" diz pro Python
    # comparar os dicionários pelo valor do preço, não pelo dicionário inteiro
    mais_barato = min(lista_produtos, key=lambda item: item["preco"])

    return total, mais_caro, mais_barato # devolve os 3 valores de uma vez (tupla)


def exibir_estatisticas(lista_produtos): # essa aqui só chama a de cima e imprime bonitinho
    print("\n--- ESTATÍSTICAS DO ESTOQUE ---")
    resultado = estatisticas(lista_produtos)

    if resultado is None: # se não veio nada, é porque a lista tava vazia
        print("Nenhum produto cadastrado para calcular estatísticas.")
        return

    total, mais_caro, mais_barato = resultado # desempacota a tupla nas 3 variáveis
    print(f"Valor total parado no estoque: R$ {total:.2f}")
    print(f"Produto mais caro: {mais_caro['nome']} (R$ {mais_caro['preco']:.2f})")
    print(f"Produto mais barato: {mais_barato['nome']} (R$ {mais_barato['preco']:.2f})")
    
# commit 5:
def menu(): # função principal, é ela que fica rodando enquanto o programa estiver aberto
    estoque = carregar_dados() # carrega o que já tinha salvo assim que o programa começa
    if estoque is None: # proteção extra, caso carregar_dados devolva None por algum motivo
        estoque = []

    while True: # loop infinito, só para quando o usuário escolhe sair (opção 5)
        print("\n=============================")
        print("  CONTROLE DE ESTOQUE")
        print("=============================")
        print("1 -> Cadastrar Produto")
        print("2 -> Listar Produtos")
        print("3 -> Ver Estatísticas")
        print("4 -> Salvar Dados")
        print("5 -> Sair")
        print("=============================")

        opcao = input("Escolha uma opção: ").strip() # strip pra não dar erro se a pessoa
        # digitar espaço sem querer antes/depois do número

        if opcao == "1":
            novo_produto = cadastrar_produto() # chama a função de cadastro
            if novo_produto is not None: # só adiciona na lista se o cadastro deu certo
                estoque.append(novo_produto)
                print(f"Produto '{novo_produto['nome']}' cadastrado com sucesso!")
        elif opcao == "2":
            listar_produtos(estoque)
        elif opcao == "3":
            exibir_estatisticas(estoque)
        elif opcao == "4":
            salvar_dados(estoque) # opção separada pra salvar quando o usuário quiser
        elif opcao == "5":
            print("\nSalvando dados e encerrando o sistema. Até mais!")
            salvar_dados(estoque) # salva automaticamente antes de sair, pra garantir
            break # quebra o while True e o programa termina
        else:
            print("\nOpção inválida! Por favor, escolha um número de 1 a 5.")


if __name__ == "__main__": # só roda o menu() se o arquivo for executado diretamente,
    # e não se ele for importado dentro de outro arquivo
    menu()


