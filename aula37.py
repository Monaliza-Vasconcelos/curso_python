"""
    Repetições
    while(enquanto)
    Executa uma ação enquanto uma condição for verdadeira
"""

contador = 0


while contador < 100:
    contador += 1

    #Continue pula o laço
    if contador == 6:
        continue

    print(contador)

    if contador == 40:
        break



print('Acabou')