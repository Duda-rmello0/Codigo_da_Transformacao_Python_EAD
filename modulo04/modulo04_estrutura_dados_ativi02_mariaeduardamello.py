aluno = {
    "nome": "Maria Eduarda",
    "idade": 16,
    "notas": [8.5, 9.0, 9.5]
}

print("--- Dados do Aluno ---")
print(f"Nome: {aluno['nome']}")
print(f"Idade: {aluno['idade']} anos")
print(f"Notas: {aluno['notas']}")

media = sum(aluno['notas']) / len(aluno['notas'])
print(f"Média do Aluno: {media:.2f}")