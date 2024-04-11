import sqlite3

conn = sqlite3.connect('database_calculus.db')

cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS alunos (nome TEXT, nota INTEGER)''')

dados_alunos = [('Carlogit push s', 8)]

cur.executemany('INSERT INTO alunos (nome, nota) VALUES (?, ?)', dados_alunos)

conn.commit()

print('Dados inseridos com sucesso.')

conn.close()



class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
    pass
