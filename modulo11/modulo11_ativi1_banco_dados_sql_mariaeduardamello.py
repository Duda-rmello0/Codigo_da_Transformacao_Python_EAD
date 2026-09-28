import sqlite3

conn = sqlite3.connect("banco.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS Clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT
)
""")

conn.commit()
conn.close()
print("Tabela 'Clientes' criada com sucesso!")