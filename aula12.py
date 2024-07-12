import os
import time

lista_cpf = ['12345678', '98765412', '15975364', '33333333']
lista_usuarios = ['gomes', 'oliveira', 'lucas', 'karython']

os.system('cls')
while True:
    print(30*'=','BEM-VINDO AO SISTEMA PYTHON CADASTROS', 30*'=')
    print('1. Cadastrar Usuário')
    print('2. Consultar Usuário')
    print('3. Acessar o Sistema')
    print('4. Remover um Usuário')
    print('5. Sair')

    opcao = input('Digite a opção desejada:')

# Opção para cadastrar novo usuário
    if opcao == '1':
        os.system('cls')
        novo_nome = input ('Digite o nome que será cadastrado: ')
        novo_cpf = input('Digite um novo cpf: ')


        if novo_cpf in lista_cpf:
            print('O cpf digitado já existe')
        else:
            lista_cpf.append(novo_cpf)
            lista_usuarios.append(novo_nome)
            print('Senha cadastrada com sucesso!')

#Opção de Consultar usuario
    elif opcao == '2':
        os.system('cls')

        for i in lista_usuarios:
            print(f'Usuário: {i}')

#Opção de Acessar
    elif opcao == '3':
        os.system('cls')

        cpf_login = input('Digite um cpf: ')

        if cpf_login in lista_cpf:
            print('Acesso realizado com Sucesso!')
        else:
            print('Usuário não possui cadastro!')

# Remover 
    elif opcao == '4':
        os.system('cls')
        
        cpf_remove = input('Digite o cpf a ser excluido: ')

        if cpf_remove in lista_cpf:
            indice = lista_cpf.index(cpf_remove)
            nome = lista_usuarios.pop(indice)
            lista_cpf.pop(indice)

            print(f'Usuario: {nome} com cpf {cpf_remove} foi removido com sucesso!')

    elif opcao == '5':
        os.system('cls')
        print('Saindo do sistema')
        time.sleep(3)
        break

    else:
        print('Opção inválida!!!')

print('Você saiu do Sistema!!!')