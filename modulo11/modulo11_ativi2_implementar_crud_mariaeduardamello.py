
import sqlite3

conn = sqlite3.connect("banco.db")
cursor = conn.cursor()


cursor.execute("INSERT INTO Clientes (nome, email) VALUES (?, ?)", ("Carlos Silva", "carlos@email.com"))
cursor.execute("INSERT INTO Clientes (nome, email) VALUES (?, ?)", ("Beatriz Souza", "beatriz@email.com"))
conn.commit()
print("✅ Dados inseridos!")

print("\n--- Todos os Clientes ---")
cursor.execute("SELECT * FROM Clientes")
for cliente in cursor.fetchall():
    print(cliente)


cursor.execute("UPDATE Clientes SET email = ? WHERE id = ?", ("carlos.novo@email.com", 1))
conn.commit()
print("\n✅ Cliente ID 1 atualizado!")


cursor.execute("DELETE FROM Clientes WHERE id = ?", (2,))
conn.commit()
print("✅ Cliente ID 2 deletado!")

conn.close()