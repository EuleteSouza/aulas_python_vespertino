altura = 20
espacamento = 0 
asterisco = 1
simbolo = '*'

for i in range(altura):
    espacamento = altura - i - 1

    for j in range(espacamento):
        print(' ', end='')

    for k in range(asterisco):
        print(simbolo, end='')

    print()
    asterisco +=2