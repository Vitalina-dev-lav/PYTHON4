import random
import sqlite3

connection = sqlite3.connect('scratch.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Ussers(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Ussers (email)")

cursor.execute("INSERT INTO Ussers(username, email, age) VALUES (?,?,?)", ("newuser", "ex@gmail.com", "28"))
# for i in range(30):
#     cursor.execute("INSERT INTO Ussers(username, email, age)VALUES(?,?,?)",(f"newuser{i}", f"{i}ex@gmail.com",str(random.randint(20,60))))

# cursor.execute("UPDATE Ussers SET age=? WHERE username=?", (29, "newuser"))
# cursor.execute("DELETE FROM Ussers WHERE username=?",("newuser0",))


connection.commit()
connection.close()