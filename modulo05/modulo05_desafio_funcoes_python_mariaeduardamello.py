from faker import Faker

fake = Faker('pt_BR')

usuarios_cadastrados = {}
for _ in range(3):
    usuarios_cadastrados[fake.user_name()] = fake.password(length=8)

def validar_login(usuario, senha, base_dados):
  if usuario in base_dados and base_dados[usuario] == senha:
    return True
  return False

print("--- Usuários e Senhas Gerados ---")
print(usuarios_cadastrados)
print("-" * 33)

usuario_input = input("Digite o usuário: ")
senha_input = input("Digite a senha: ")

if validar_login(usuario_input, senha_input, usuarios_cadastrados):
  print("Login realizado com sucesso! Acesso concedido.")
else:
  print("Usuário ou senha incorretos. Acesso negado.")