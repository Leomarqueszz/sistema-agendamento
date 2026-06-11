import sqlite3

conexao = sqlite3.connect("agendamento.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS agendamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente TEXT NOT NULL,
    data TEXT NOT NULL,
    horario TEXT NOT NULL
)
""")

conexao.commit()