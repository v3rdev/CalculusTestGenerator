import sqlite3


def verificarBancoDados(NomeBancoDados):
    import os
    NomeArquivo = NomeBancoDados + '.db'
    # Verificar se o arquivo do banco de dados já existe
    return os.path.exists(NomeArquivo)


def criarBancoDados(NomeBancoDados='SemNome', retornarNome=False):
    if NomeBancoDados == 'SemNome':
        NomeBancoDados = input('Digite o nome do banco de dados que deseja criar: ')
    
    # Verificar se o arquivo do banco de dados já existe
    if verificarBancoDados(NomeBancoDados):
        if retornarNome:
            return NomeBancoDados
        else:
            return print(f'O banco de dados "{NomeBancoDados}" já existe.')

    # Conectar-se ao banco de dados
    conn = sqlite3.connect(NomeBancoDados + '.db')
    conn.close()

    print(f'Banco de dados "{NomeBancoDados}" criado com sucesso.')

    if retornarNome:   
        return NomeBancoDados
    else:
        return print(f'O banco de dados "{NomeBancoDados}" já existe.')
           

def imprimirNomesBancoDados():
    import os
    print("Bancos de dados existentes:")
    # Listar todos os arquivos no diretório atual
    arquivos = os.listdir('.')
    # Filtrar os arquivos que terminam com a extensão '.db'
    bancos_dados = [arquivo[:-3] for arquivo in arquivos if arquivo.endswith('.db')]
    # Imprimir os nomes dos bancos de dados
    for banco_dados in bancos_dados:
        print(banco_dados)


def verificarTabela(NomeBancoDados, NomeTabela):
    if verificarBancoDados(NomeBancoDados):
        conn = sqlite3.connect(NomeBancoDados + '.db')
        cur = conn.cursor()
        cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{NomeTabela}'")
        return cur.fetchone()
    else:
        return False


def criarTabela(NomeBancoDados, NomeTabela='SemNome', retornarNome=False):
    if not verificarBancoDados(NomeBancoDados):
        return print(f'O banco de dados com nome {NomeBancoDados} não existe, programa finalizado!')
    if NomeTabela == 'SemNome':
        # Caso o nome da tabela não seja dado, solicitar o nome ao usuário
        NomeTabela = input('Digite o nome da tabela que deseja criar: ')

    conn = sqlite3.connect(NomeBancoDados + '.db')
    cur = conn.cursor()

    # Criar a tabela se ela não existir
    if verificarTabela(NomeTabela):
        if retornarNome:
            return NomeTabela
        else:
            return print(f'A tabela "{NomeTabela}" já existe.')
    else:
        cur.execute(f'''CREATE TABLE {NomeTabela} (enunciado TEXT, idTopico TEXT)''')
        # Cometer as alterações e fechar a conexão
        conn.commit()
        conn.close()
        if retornarNome:
            return NomeTabela
        else:
            return print(f'Tabela "{NomeTabela}" criada com sucesso!')
        

def imprimirNomesTabelas(NomeBancoDados = 'SemNome'):
    if NomeBancoDados ==  'SemNome':
        NomeBancoDados = input('Digite o nome do bando de dados: ')
    if not verificarBancoDados(NomeBancoDados):
        return print(f'O banco de dados com nome {NomeBancoDados} não existe, programa finalizado!')
        
    # Conectar ao banco de dados
    conn = sqlite3.connect(NomeBancoDados + '.db')
    cursor = conn.cursor()

    # Executar a consulta SQL para recuperar os nomes das tabelas
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")

    # Recuperar os nomes das tabelas do cursor
    NomesTabelas = cursor.fetchall()

    if len(NomesTabelas) == 0:
        print('A tabela está vazia!')
        #print(NomesTabelas)
    else:
        # Imprimir os nomes das tabelas
        print("Nomes das tabelas:")
        for tabela in NomesTabelas:
            print(tabela[0])

    # Fechar a conexão com o banco de dados
    conn.close()


def inserirDados(NomeBancoDados = 'SemNome', NomeTabela = 'SemNome'):
    if NomeBancoDados == 'SemNome':
        NomeBancoDados = input('Digite o nome da base de dados: ')
    if not verificarBancoDados(NomeBancoDados):
        return print(f'O banco de dados com nome {NomeBancoDados} não existe, programa finalizado!')
    if NomeTabela == 'SemNome':
        NomeTabela = input('Digite o nome da tabela: ')
    if not verificarTabela(NomeBancoDados, NomeTabela):
        return print(f'A tabela com nome {NomeTabela} não existe, programa finalizado!')

    conn = sqlite3.connect(NomeBancoDados + '.db')
    cur = conn.cursor()

#    # Coletar enunciado e tópico da questão
#    inicio = r'''
#    \documentclass{article}
#    \begin{document}
#    '''
#    final = r'''
#    \end{document}
#    '''

    enunciado = input('Questão: ')
    idTopico = input('Informe o tópico da questão: ')

    # Inserir dados na tabela
    cur.execute(f'INSERT INTO {NomeTabela} (enunciado, idTopico) VALUES (?, ?)', (enunciado, idTopico))

    # Cometer as alterações e fechar a conexão
    conn.commit()
    conn.close()

    print('Dados inseridos com sucesso.')


def imprimirDados(NomeBancoDados='SemNome', NomeTabela='SemNome'):
    if NomeBancoDados == 'SemNome':
        NomeBancoDados = input('Digite o nome da base de dados: ')
    if not verificarBancoDados(NomeBancoDados):
        return print(f'O banco de dados com nome {NomeBancoDados} não existe, programa finalizado!')
    if NomeTabela == 'SemNome':
        NomeTabela = input('Digite o nome da tabela: ')
    if not verificarTabela(NomeBancoDados, NomeTabela):
        return print(f'A tabela com nome {NomeTabela} não existe, programa finalizado!')

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








# Programa Principal

"""nomeBanco = input('Digite o nome do banco de dados que deseja criar: ')
criarBancoDados(nomeBanco)
imprimirNomesBancoDados()

nomeTabela = input('Digite o nome da tabela que deseja criar: ')
criarTabela(nomeBanco, nomeTabela)
imprimirNomesTabelas(nomeBanco)
#Calculo2 = criarTabela(BancoVer2, 'Calculo2')
"""


#imprimirNomesBancoDados()
#inserirDados('MMB1_2005', 'Notas_P2')
imprimirDados('MMB1_2005', 'Notas_P2')
#imprimirDados()

#criarTabela('')


#imprimirNomesTabelas()








#criarBancoDados('BancoTeste3')
#inserirDados('BancoTeste3')
#imprimirDados('BancoTeste3')
#imprimirNomesTabelas('BancoTeste3')


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
    pass
