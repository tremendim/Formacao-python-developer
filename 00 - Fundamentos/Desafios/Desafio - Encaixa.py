N = int(input())
cont = 0

while cont != N:
    A = input()
    B = input()
    tamB = len(B)
    tamAFormatado = (A[-tamB:])
    if tamAFormatado == B:
        print('encaixa')
    else:
        print('nao encaixa')
    cont=cont+1

