import sqlite3

def criarBancoDados(NomeBancoDados):
    # Conectar-se ao banco de dados
    conn = sqlite3.connect(NomeBancoDados + '.db')
    cur = conn.cursor()

    # Criar a tabela se ela não existir
    cur.execute('''CREATE TABLE IF NOT EXISTS NomeBancoDados (enunciado TEXT, idTopico TEXT)''')

    # Cometer as alterações e fechar a conexão
    conn.commit()
    conn.close()


def inserirLista(NomeBancoDados, lista):
    # Conectar-se ao banco de dados
    conn = sqlite3.connect(NomeBancoDados + '.db')
    cur = conn.cursor()

    # Inserir a lista na tabela
    cur.executemany(f'INSERT INTO {NomeBancoDados} (enunciado, idTopico) VALUES (?, ?)', lista)

    # Cometer as alterações e fechar a conexão
    conn.commit()
    conn.close()
    pass

def inserirDados(NomeBancoDados, lista):
    # Conectar-se ao banco de dados correto
    conn = sqlite3.connect(NomeBancoDados + '.db')
    cur = conn.cursor()

    # Coletar enunciado e tópico da questão
    inicio = r'''
    \documentclass{article}
    \begin{document}
    '''
    final = r'''
    \end{document}
    '''
    enunciado = input('Quesão: ')
    idTopico = input('Informe o tópico da questão: ')
    lista = [(enunciado, idTopico)]

    # Inserir dados na tabela
    cur.execute('INSERT INTO NomeBancoDados (enunciado, idTopico) VALUES (?, ?)', lista)

    # Cometer as alterações e fechar a conexão
    conn.commit()
    conn.close()

    print('Dados inseridos com sucesso.')

def inserirDados2(NomeBancoDados):
    conn = sqlite3.connect('NomeBancoDados.db')
    cur = conn.cursor()

    print(r"""
    \documentclass{article}
    \begin{document}""")
    enunciado = str(input(r"""
    Questão: """))
    print(r"""
    \end{document}
          """)
    idTopico = str(input('''Informe o tópico da questão: '''))

    dados = [(enunciado, idTopico)]

    cur.executemany('INSERT INTO NomeBancoDados (enunciado, idTopico) VALUES (?, ?)', dados)
    conn.commit()
    print('Dados inseridos com sucesso.')
    conn.close()
    pass

def imprimirDados(NomeBancoDados):
    # Conectar-se ao banco de dados
    conn = sqlite3.connect(NomeBancoDados + '.db')
    cur = conn.cursor()

    # Selecionar todos os dados da tabela
    cur.execute('SELECT * FROM NomeBancoDados')

    # Iterar sobre os resultados e imprimir cada linha
    for linha in cur.fetchall():
        print(linha)

    # Fechar a conexão
    conn.close()

def imprimirNomesTabelas(NomeBancoDados):
    # Conectar ao banco de dados
    conn = sqlite3.connect(NomeBancoDados)
    cursor = conn.cursor()

    # Executar a consulta SQL para recuperar os nomes das tabelas
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")

    # Recuperar os nomes das tabelas do cursor
    NomesTabelas = cursor.fetchall()

    # Imprimir os nomes das tabelas
    print("Nomes das tabelas:")
    for tabela in NomesTabelas:
        print(tabela[0])

    # Fechar a conexão com o banco de dados
    conn.close()



#criarBancoDados('BancoTeste3')
#inserirDados('BancoTeste3')
#imprimirDados('BancoTeste3')
imprimirNomesTabelas('BancoTeste3')


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
    pass
