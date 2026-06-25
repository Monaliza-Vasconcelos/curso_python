"""
Formatação básica de strings

s - string
d - int
f - float
.<número de dígitos>f
x ou X - hexadecimal
(caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - Centro
Sinal - + ou -
Ex: 0>-100,.1f
conversion flags - !r !s !a


"""

variavel = 'ABC'
print(f'{variavel: >10}.')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}')
print(f'{1000.12312312312312:.1f}')
