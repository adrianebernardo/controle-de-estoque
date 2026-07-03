# Sistema de Controle de Estoque
É um programa de terminal para gerenciar os produtos de uma loja. Você pode cadastrar produtos com nome, quantidade e preço, listar tudo que está guardado, calcular estatísticas de valor (total parado no estoque, produto mais caro e mais barato) e salvar os dados manualmente quando quiser. Todos os dados são salvos em JSON, então nada é perdido entre sessões.
## Como rodar
```bash
python estoque.py
```
## Funcionalidades
- **Cadastrar Produto** — pede nome, quantidade e preço unitário; valida as entradas com try/except para não quebrar se o usuário digitar texto no lugar de número
- **Listar Produtos** — exibe todos os produtos cadastrados com nome, quantidade e preço formatados
- **Ver Estatísticas** — calcula e mostra o valor total parado no estoque (quantidade × preço de todos os itens), o produto mais caro e o produto mais barato
- **Salvar Dados** — grava a lista de produtos no arquivo `estoque.json`
- **Sair** — salva os dados automaticamente antes de encerrar o programa; nenhuma informação é perdida
## Funções implementadas
| Função | Responsabilidade |
|--------|-----------------|
| `carregar_dados()` | Lê o arquivo `estoque.json` do disco e retorna a lista de produtos; retorna lista vazia se o arquivo não existir ou estiver corrompido |
| `salvar_dados()` | Grava a lista de produtos atualizada no arquivo `estoque.json` com indentação e encoding UTF-8 |
| `pedir_quantidade()` | Pede a quantidade ao usuário com validação, repetindo até receber um número inteiro válido |
| `pedir_preco()` | Pede o preço unitário ao usuário com validação, repetindo até receber um número decimal válido |
| `cadastrar_produto()` | Coleta nome, quantidade e preço do usuário e monta o dicionário do produto usando `return` |
| `listar_produtos()` | Percorre todos os produtos e imprime cada um formatado com nome, quantidade e preço |
| `estatisticas()` | Soma quantidade × preço de todos os itens e encontra o produto mais caro e o mais barato, retornando os três valores em uma tupla |
| `exibir_estatisticas()` | Usa `estatisticas()` e imprime o resultado formatado no terminal |
## Estrutura do repositório
```
controle-de-estoque/
├── estoque.py       # programa principal
├── estoque.json     # dados gerados pelo programa
└── README.md        # documentação do projeto
```
## Tecnologias usadas
Python 3 · json · os
## O que aprendi
Eu tive a oportunidade de fazer pela segunda vez o mesmo estilo de trabalho e, antes minha maior dificuldade no trabalho tinha sido o uso do fluxograma, porque não entendia tão bem a ideia de formalizar minha ideia antes de começar a codar. Agora eu entendo a importância, e pretendo usar - mas sem papel! O JSON é muito importante, mas usando ele ainda mais agora já brilhou mais ideias na minha cabeça para projetos futuros. <3