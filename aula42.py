frase = 'aaaaaaaaaaaaaaaaaaaaoooooooooooo'.lower()


i = 0 
aparece_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    quantas_vezes_letra_apareceu_atual = frase.count(letra_atual)

    if aparece_mais_vezes <= quantas_vezes_letra_apareceu_atual:
        aparece_mais_vezes = quantas_vezes_letra_apareceu_atual
        letra_apareceu_mais_vezes =  letra_atual

    i += 1

print(f'A letra que apareceu mais vezes foi,"{letra_apareceu_mais_vezes}" com {aparece_mais_vezes}x')