
# T = numero de casos de teste

# print("Digite a quantidade de casos")
T = int(input())

#N e K (1 ≤ K, N ≤ 10000),  respectivamente o número de refrigerantes comprados e o número de garrafas vazias
# K = Quantidade de garrafas compradas no primeiro dia
# N = Quantidade de garrafas vazia que precisa para ganhar 1 cheia

for cont in range(T):
    K = int(input())
    N = int(input())
    if K >= 1 and N <= 10000:
        garrafasRetornadas = K/N
        saldo = K-N
        total = garrafasRetornadas + saldo
        #Comando para desconsidera as casas decimais após a virgula
        totalSVirgula = round(total,0)
        print(totalSVirgula)
        
    cont = cont+1


