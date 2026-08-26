def fazer_login(usuario, senha, base):
    if usuario in base and base[usuario] == senha:
        print("Login bem-sucedido!")
        return True
    print("Erro de login.")
    return False