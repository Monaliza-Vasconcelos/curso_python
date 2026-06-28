"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
primeiro_nome = input('Digite seu primeiro nome: ')

if primeiro_nome.isalpha():
    quantidade_letras = len(primeiro_nome)
    if quantidade_letras <= 4:
        print('Seu nome é curto!')
    elif quantidade_letras >= 5 and quantidade_letras <= 6:
        print('Seu nome é normal!')
    elif quantidade_letras > 6:
        print('Seu nome é grande!')
    else:
        print('Erro, valor digitado, errado.')
else:
    print('Erro, digite apenas strings.')