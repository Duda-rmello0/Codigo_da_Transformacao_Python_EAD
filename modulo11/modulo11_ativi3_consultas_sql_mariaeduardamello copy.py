
import sqlite3

conn = sqlite3.connect("banco.db")
cursor = conn.cursor()


cursor.execute("INSERT INTO Clientes (nome, email) VALUES (?, ?)", ("Ana Silva", "ana.silva@email.com"))
cursor.execute("INSERT INTO Clientes (nome, email) VALUES (?, ?)", ("Beatriz Souza", "beatriz.souza@email.com"))
cursor.execute("INSERT INTO Clientes (nome, email) VALUES (?, ?)", ("Antonio Santos", "antonio.santos@email.com"))
conn.commit()
print("✅ Dados inseridos!")

print("--- Clientes com nome começando em 'A' ---")
cursor.execute("SELECT * FROM Clientes WHERE nome LIKE 'A%'")

clientes_com_a = cursor.fetchall()
for cliente in clientes_com_a:
    print(f"ID: {cliente[0]} | Nome: {cliente[1]} | Email: {cliente[2]}")

conn.close()