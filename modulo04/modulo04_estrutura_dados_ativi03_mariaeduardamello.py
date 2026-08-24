numeros = [12, 7, 5, 18, 22, 9, 3, 14, 21, 40]

pares = []
impares = []

# Percorrendo o conjunto de números
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

# Exibindo cada categoria separadamente
print(f"Números Pares: {pares}")
print(f"Números Ímpares: {impares}")