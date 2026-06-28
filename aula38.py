"""
    Repetições
    while(enquanto)
    Executa uma ação enquanto uma condição for verdadeira
"""

quant_linhas = 5
quant_colunas = 5


linha = 1
while linha <= quant_linhas:
    coluna = 1
    print(linha)

    while coluna <= quant_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1

    linha += 1

print('Acabou')