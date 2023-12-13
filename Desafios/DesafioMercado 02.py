def calcular_garrafas(n, k):
    garrafas_cheias = n // k
    garrafas_sobrando = n % k
    total_garrafas = garrafas_cheias + garrafas_sobrando

    return total_garrafas

# Entrada de dados
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    resultado = calcular_garrafas(n, k)
    print(resultado)
