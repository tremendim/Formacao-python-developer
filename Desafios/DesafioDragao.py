

# C = Numeros de casos de teste
#print("Digite a quantidade de oponentes")
C = int(input()) 
cont=0

for cont in range (C):
    #print("Digite o valor de energia do ser vivo")
    energia = int(input())
    if energia <= 8000:
        print("Inseto!")
    else:
        print("Maior que 8000!")
    cont=cont+1
        




