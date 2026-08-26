import shutil
import os

arquivo_origem = "clientes.json" 
pasta_backup = "backup_destino"


if not os.path.exists(pasta_backup):
    os.makedirs(pasta_backup)

caminho_destino = os.path.join(pasta_backup, arquivo_origem)

try:
    shutil.copy2(arquivo_origem, caminho_destino)
    print(f"Backup realizado com sucesso! Arquivo copiado para: '{caminho_destino}'")
except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo_origem}' não foi encontrado para fazer o backup. Execute a atividade 1 primeiro!")
    
   