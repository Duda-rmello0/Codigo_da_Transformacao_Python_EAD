def calcular_media():
    n1 = float(input("Digite a primeira nota:"))
    n2 = float(input("Digite a segunda nota:"))
    n3 = float(input("Digite a terceira nota:"))
    
    media = (n1 + n2 + n3) / 2

    if media >= 7:
        return media, "Aprovado"
    else:
        return media, "Reprovado"

 
resultado, status = calcular_media()
print(f"Média: {resultado}, Status: {status}")