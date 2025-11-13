import sqlite3
banco = sqlite3.connect('escola.db')
cursor = banco.cursor()

cursor.execute("CREATE TABLE escola (id INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT, idade INTEGER, email TEXT)")

cursor.execute("INSERT INTO escola Values(1,'Samira', 16 , 'Samirinha237@gmail.com')")
cursor.execute("INSERT INTO escola Values(2,'Daniella', 15 , 'Daniella596859@gmail.com' )")
cursor.execute("INSERT INTO escola Values(3,'Manuela', 16 , 'manuzinha800@gmail.com')")
cursor.execute("INSERT INTO escola Values(4,'Caio' , 14, 'caio2510@gmail.com')")
cursor.execute("INSERT INTO escola Values(5,'Pedro', 15, 'pedrinxx17@gmail.com')")

# 3 - UPDATE: Atualizar 
# 👉 COMPLETE:
cursor.execute("UPDATE escola SET idade  = 15 WHERE idade = 16 ")

# 5 - DELETE: Remover 
# 👉 COMPLETE:
cursor.execute("DELETE FROM escola WHERE idade = 14")

cursor.execute("SELECT * FROM escola")
print(cursor.fetchall())


banco.commit()

