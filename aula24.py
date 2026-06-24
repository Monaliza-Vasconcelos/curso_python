#operadores in e not in

nome = 'Monaliza'
print(nome[2])

#in checa letra por letra
print('M' in nome)

#not in - checa se não está dentro
print('M' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que você deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')