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

