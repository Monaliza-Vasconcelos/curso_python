"""
    iterando strings com while
"""


# 0123456789

nome = "Monaliza Vasconcelos"

tamanho_nome = len(nome)
contador = 0

while contador < tamanho_nome:

    print(f'{nome[contador]}', end="*")
    contador += 1

print()
    

