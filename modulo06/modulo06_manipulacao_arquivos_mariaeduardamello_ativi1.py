conteudo_para_salvar = "Olá! Este é um texto de teste armazenado em um arquivo TXT usando Python."


# O with open serve para criar e salvar o arquivo "dados.txt". Ele utiliza o "w" para escrever o arquivo.
with open("dados.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(conteudo_para_salvar)
print("Arquivo TXT criado e salvo com sucesso!")


# O with open abre o arquivo "dados.txt" e utiliza o "r" para ler.
with open("dados.txt", "r", encoding="utf-8") as arquivo:
    conteudo_lido = arquivo.read()

print("\n--- Conteúdo lido do arquivo TXT ---")
print(conteudo_lido)