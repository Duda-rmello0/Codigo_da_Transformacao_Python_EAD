def maior_menor(lista):
  maior = max(lista)
  menor = min(lista)
  return maior, menor


# Criando uma lista vazia para receber os números
numeros = []

print("Digite 5 números:")
for i in range(5):
  # Usamos float(input) para aceitar tanto números inteiros quanto com vírgula/ponto
  num = float(input(f"Digite o {i+1}º número: "))
  numeros.append(num)

maior_val, menor_val = maior_menor(numeros)
print(f"O maior valor é: {maior_val}")
print(f"O menor valor é: {menor_val}")