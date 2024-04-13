import sqlite3

def criarBancoDados():
    # Conectar-se ao banco de dados
    NomeBancoDados = input('Digite o nome do banco de dados que deseja criar: ')
    conn = sqlite3.connect(NomeBancoDados + '.db')
    cur = conn.cursor()

    while True:
        opcao = input('Deseja criar uma tabela [Sim/Não]? ').strip().upper()
        if opcao == 'NÃO':
            break
        elif opcao == 'SIM':
            # Criar a tabela se ela não existir com um nome escolhido
            NomeTabela = input('Digite o nome da tabela: ')
            cur.execute(f'''CREATE TABLE IF NOT EXISTS {NomeTabela} (enunciado TEXT, idTopico TEXT)''')
            print(f'Tabela "{NomeTabela}" criada com sucesso!')
        else:
            print('Opção inválida. Por favor, responda com "Sim" ou "Não".')

    # Cometer as alterações e fechar a conexão
    conn.commit()
    conn.close()
    pass

def criarBancoDados(retornarNome = False):
    # Conectar-se ao banco de dados
    NomeBancoDados = input('Digite o nome do banco de dados que deseja criar: ')
    conn = sqlite3.connect(NomeBancoDados + '.db')
    cur = conn.cursor()

    # Fechar a conexão
    conn.close()

    print(f'Banco de dados "{NomeBancoDados}" criado com sucesso.')

    if retornarNome == True:
        return NomeBancoDados
    pass


def criarBancoDados(retornarNome=False):
    import os
    # Conectar-se ao banco de dados
    NomeBancoDados = input('Digite o nome do banco de dados que deseja criar: ')
    NomeArquivo = NomeBancoDados + '.db'
    
    # Verificar se o arquivo do banco de dados já existe
    if os.path.exists(NomeArquivo):
        print(f'O banco de dados "{NomeBancoDados}" já existe.')
        if retornarNome:
            return NomeBancoDados
        else:
            return
    
    conn = sqlite3.connect(NomeArquivo)
    conn.close()

    print(f'Banco de dados "{NomeBancoDados}" criado com sucesso.')

    if retornarNome:
        return NomeBancoDados
    

def criarTabela():
    while True:
        opcao = input('Deseja criar a tabela em um banco de dados existente [Sim/Não/Sair]? ').strip().upper()
        if opcao == 'SIM' or opcao == 'NÃO' or 'SAIR':
            break
        else:
            print('Opção inválida, tente de novo!')

    if opcao == 'SIM' or opcao == 'NÃO':
        # Conectar-se ao banco de dados correto
        if opcao == 'SIM':
            NomeBancoDados = input('Digite o nome do banco de dados onde deseja criar a tabela: ')
        else:
            NomeBancoDados = criarBancoDados(True)
        conn = sqlite3.connect(NomeBancoDados + '.db')
        cur = conn.cursor()

        # Solicitar o nome da tabela ao usuário
        NomeTabela = input('Digite o nome da tabela que deseja criar: ')

        # Verificar se a tabela já existe
        cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{NomeTabela}'")
        tabela_existente = cur.fetchone()

        # Criar a tabela se ela não existir
        if tabela_existente:
            print(f'A tabela "{NomeTabela}" já existe.')
        else:
            cur.execute(f'''CREATE TABLE {NomeTabela} (enunciado TEXT, idTopico TEXT)''')
            print(f'Tabela "{NomeTabela}" criada com sucesso!')

        # Fechar a conexão
        conn.close()


def inserirDados():
    NomeBancoDados = input('Digite o nome da Base de dados: ')
    NomeTabela = input('Digite o nome da Tabela:')

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

    # Inserir dados na tabela
    cur.execute(f'INSERT INTO {NomeTabela} (enunciado, idTopico) VALUES (?, ?)', (enunciado, idTopico))

    # Cometer as alterações e fechar a conexão
    conn.commit()
    conn.close()

    print('Dados inseridos com sucesso.')


def imprimirDados():
    NomeBancoDados = input('Digite o nome da Base de dados: ')
    NomeTabela = input('Digite o nome da Tabela:')
    
    # Conectar-se ao banco de dados
    conn = sqlite3.connect(NomeBancoDados + '.db')
    cur = conn.cursor()

    # Selecionar todos os dados da tabela
    cur.execute('SELECT * FROM ' + NomeTabela)

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
