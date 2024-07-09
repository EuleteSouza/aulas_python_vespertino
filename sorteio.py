'''import random

nome1 = input('Digite um nome: ')
nome2 = input('Digite um nome: ')
nome3 = input('Digite um nome: ')
nome4 = input('Digite um nome: ')
nome5 = input('Digite um nome: ')

lista = [nome1, nome2, nome3, nome4, nome5]

premiado = random.choice(lista)
print(f'O premiado da mega da virada é o {premiado}')'''


'''import random

lista = []

while True:
    nome = input('Digite os nomes que serão sorteados: ')

    if nome != '':
        lista.append(nome)
    else:
        break

premiado = random.choice(lista)
print(f'O vencedor é: {premiado}')'''

import random
import os

lista = []
lista_sorteados = []

while True:
    nome = input('Digite os nomes que serão sorteados: ')

    if nome != '':
        lista.append(nome)
    else:
        break
    

while True:
    if lista:
        os.system('cls')
        premiado = random.choice(lista)
        lista_sorteados.append(premiado)
        #lista.remove(premiado) # Remove a primeira ocorrência
        lista.pop(premiado) # Remove o elemento no indice específico

        print(f'O vencedor é: {premiado}')

        opcao = input('Deseja realizar um novo sorteio? (s/n)').lower()
        os.system('cls')

       


        if opcao != 's':
            break
    else:
        print('Não existe nomes para serem sorteados!')

print('Sistema finalizado!')
print(lista)
print(lista_sorteados)


