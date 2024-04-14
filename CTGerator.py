import sqlite3


def verificarBancoDados(NomeBancoDados):
    """
    Verifica se um banco de dados SQLite com o nome especificado já existe no sistema de arquivos.

    Args:
        NomeBancoDados (str): O nome do banco de dados a ser verificado.

    Returns:
        bool: True se o arquivo do banco de dados existe, False caso contrário.
    """
    import os
    NomeArquivo = NomeBancoDados + '.db'
    # Verificar se o arquivo do banco de dados já existe
    return os.path.exists(NomeArquivo)


def criarBancoDados(NomeBancoDados='SemNome', retornarNome=False):
    """
    Cria um novo banco de dados SQLite com o nome especificado, se ele ainda não existir.

    Args:
        NomeBancoDados (str, opcional): O nome do banco de dados a ser criado. Se não fornecido, será solicitado ao usuário.
        retornarNome (bool, opcional): Se True, a função retorna o nome do banco de dados criado. Caso contrário, apenas imprime uma mensagem.

    Returns:
        str: O nome do banco de dados criado, se retornarNome for True.
    """
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
    """
    Imprime os nomes dos bancos de dados existentes no diretório atual.

    A função lista todos os arquivos no diretório atual com a extensão '.db'
    e imprime seus nomes sem a extensão.

    """
    import os
    print("Bancos de dados existentes:")
    # Listar todos os arquivos no diretório atual
    arquivos = os.listdir('.')
    # Filtrar os arquivos que terminam com a extensão '.db'
    bancos_dados = [arquivo[:-3] for arquivo in arquivos if arquivo.endswith('.db')]

    # Imprimir os nomes dos bancos de dados
    for banco_dados in bancos_dados:
        print(banco_dados)


def editarListaNomesBancoDados():
    """
    Permite editar a lista de bancos de dados.

    O usuário pode optar por remover ou renomear um banco de dados existente.

    Returns:
        None
    """
    import os
    opcao = int(input('''
                      Editar lista de Banco de Dados
                      [1] Remover
                      [2] Renomear
                      [3] Sair
                      
                      Escolha uma opção: '''))
    if opcao == 3:
        return print('Programa finalizado!')
    imprimirNomesBancoDados()
    operacao = 'remover' if opcao == 1 else 'renomear'
    NomeBancoDados = input(f'Digite o nome do arquivo que deseja {operacao}: ')
    if os.path.exists(NomeBancoDados + '.db'):
        if opcao == 1:
            os.remove(NomeBancoDados + '.db')
            print(f'O arquivo "{NomeBancoDados}" foi removido com sucesso.')
        elif opcao == 2:
            NomeBancoDadosNovo = input('Digite o novo nome do arquivo que deseja renomear: ')
            os.rename(NomeBancoDados + '.db', NomeBancoDadosNovo + '.db')
            print(f'O arquivo foi renomeado com sucesso.')
    else:
        print(f'O arquivo "{NomeBancoDados}" não existe.')



def verificarTabela(NomeBancoDados, NomeTabela):
    """
    Verifica se uma tabela específica existe em um banco de dados SQLite.

    Args:
        NomeBancoDados (str): O nome do banco de dados SQLite, sem a extensão .db.
        NomeTabela (str): O nome da tabela a ser verificada.

    Returns:
        bool: True se a tabela existir, False caso contrário.
    """
    if verificarBancoDados(NomeBancoDados):
        conn = sqlite3.connect(NomeBancoDados + '.db')
        cur = conn.cursor()
        cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{NomeTabela}'")
        tabela_existente = cur.fetchone()
        conn.close()
        return tabela_existente is not None
    else:
        return False


def criarTabela(NomeBancoDados, NomeTabela='SemNome', retornarNome=False):
    """
    Cria uma tabela em um banco de dados SQLite.

    Args:
        NomeBancoDados (str): O nome do banco de dados SQLite, sem a extensão .db.
        NomeTabela (str, optional): O nome da tabela a ser criada. Se não fornecido, será solicitado ao usuário.
        retornarNome (bool, optional): Indica se o nome da tabela deve ser retornado. O padrão é False.

    Returns:
        str or None: O nome da tabela criada, se retornarNome for True, caso contrário, None.
    """
    if not verificarBancoDados(NomeBancoDados):
        return print(f'O banco de dados com nome {NomeBancoDados} não existe, programa finalizado!')
    if NomeTabela == 'SemNome':
        # Caso o nome da tabela não seja dado, solicitar o nome ao usuário
        NomeTabela = input('Digite o nome da tabela que deseja criar: ')

    conn = sqlite3.connect(NomeBancoDados + '.db')
    cur = conn.cursor()

    # Criar a tabela se ela não existir
    if verificarTabela(NomeBancoDados, NomeTabela):
        if retornarNome:
            return NomeTabela
        else:
            return print(f'A tabela "{NomeTabela}" já existe.')
    else:
        cur.execute(f'''CREATE TABLE {NomeTabela} (IdQuestao TEXT, enunciado TEXT, IdTopico TEXT, Peso FLOAT)''')
        # Cometer as alterações e fechar a conexão
        conn.commit()
        conn.close()
        if retornarNome:
            return NomeTabela
        else:
            return print(f'Tabela "{NomeTabela}" criada com sucesso!')
        

def imprimirNomesTabelas(NomeBancoDados = 'SemNome'):
    """
    Imprime os nomes das tabelas em um banco de dados SQLite.

    Parameters:
    - NomeBancoDados (str): O nome do banco de dados SQLite. Se não for fornecido, será solicitado ao usuário.

    Returns:
    - None
    """
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


def editarListaNomesTabelas(NomeBancoDados):
    if not verificarBancoDados(NomeBancoDados):
        return print(f'O banco de dados com nome {NomeBancoDados} não existe!')
    opcao = int(input('''
                      Editar lista de tabelas
                      [1] Remover
                      [2] Renomear
                      [3] Sair
                      
                      Escolha uma opção: '''))
    if opcao == 3:
        return print('Programa finalizado!')
    imprimirNomesTabelas(NomeBancoDados)
    operacao = 'remover' if opcao == 1 else 'renomear'
    NomeTabela = input(f'Digite o nome do arquivo que deseja {operacao}: ')
    conn = sqlite3.connect(NomeBancoDados + '.db')
    cur = conn.cursor()
    if verificarTabela(NomeBancoDados, NomeTabela):
        if opcao == 1:
            cur.execute(f"DROP TABLE IF EXISTS {NomeTabela}")
            print(f'O arquivo foi removido com sucesso.')
        elif opcao == 2:
            cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
            NomesTabelas = cur.fetchall()
            NomesTabelas = [NomesTabelas[i][0] for i in range(len(NomesTabelas))]
            while True:
                NomeTabelaNovo = input('Digite o novo nome do arquivo que deseja renomear: ')
                if NomeTabelaNovo in NomesTabelas:
                    print('Já existe um arquivo com esse nome, tente de novo!')
                else:
                    break            
            cur.execute(f"ALTER TABLE {NomeTabela} RENAME TO {NomeTabelaNovo}")
            #os.rename(NomeBancoDados + '.db', NomeBancoDadosNovo + '.db')
            print('O arquivo foi renomeado com sucesso.')
    else:
        print(f'O arquivo "{NomeTabela}" não existe.')
    conn.commit()
    conn.close()



def inserirDados(NomeBancoDados = 'SemNome', NomeTabela = 'SemNome'):
    """
    Insere dados em uma tabela de um banco de dados SQLite.

    Args:
        NomeBancoDados (str, optional): O nome do banco de dados onde os dados serão inseridos. Se não fornecido,
        o usuário será solicitado a inserir o nome do banco de dados. O padrão é 'SemNome'.
        NomeTabela (str, optional): O nome da tabela onde os dados serão inseridos. Se não fornecido, o usuário será
        solicitado a inserir o nome da tabela. O padrão é 'SemNome'.

    Returns:
        None
    """
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

    IdQuestao = input('IdQuestao: ')
    Enunciado = input('Questão: ')
    IdTopico = input('Informe o tópico da questão: ')
    Peso = float(input('Peso: '))

    # Inserir dados na tabela
    cur.execute(f'INSERT INTO {NomeTabela} (IdQuestao, Enunciado, IdTopico, Peso) VALUES (?, ?, ?, ?)', (IdQuestao, Enunciado, IdTopico, Peso))

    # Cometer as alterações e fechar a conexão
    conn.commit()
    conn.close()

    print('Dados inseridos com sucesso.')


def imprimirDados(NomeBancoDados='SemNome', NomeTabela='SemNome'):
    """
    Imprime todos os dados de uma tabela de um banco de dados SQLite.

    Args:
        NomeBancoDados (str, optional): O nome do banco de dados onde os dados serão impressos. Se não fornecido,
        o usuário será solicitado a inserir o nome do banco de dados. O padrão é 'SemNome'.
        NomeTabela (str, optional): O nome da tabela onde os dados serão impressos. Se não fornecido, o usuário será
        solicitado a inserir o nome da tabela. O padrão é 'SemNome'.

    Returns:
        None
    """
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


def editarListaDados(NomeBancoDados, NomeTabela):
    if verificarBancoDados(NomeBancoDados) == False or verificarTabela(NomeBancoDados, NomeTabela) == False:
        print('Verifique se a informação fornecida é válida!')
    imprimirDados(NomeBancoDados, NomeTabela)
    conn = sqlite3.connect(NomeBancoDados + '.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM " + NomeTabela)
    linhas = cur.fetchall()
 #   print(linhas)
    EntradasIdQuestao = [linhas[i][0] for i in range(len(linhas))]
 #   print(EntradasIdQuestao)
    while True:
        IdQuestao = input('Digite o ID da questão que deseja remover [ou C para cancelar a edição]: ') # IdQuestao
        if IdQuestao in EntradasIdQuestao:
            cur.execute(f"DELETE FROM {NomeTabela} WHERE IdQuestao=?", (IdQuestao,))
            print(f'A entrada com ID {IdQuestao} foi removido com sucesso.')
            break
        elif IdQuestao.strip().upper() == 'C':
            print('Edição cancelada!')
            break
        else:
            print('Não existe uma entrada com esse IdQuestão, tente de novo!')
    conn.commit()
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
#imprimirDados('MMB1_2005', 'Notas_P2')
#imprimirDados()

#criarTabela('MMB1_2005')

#editarListaNomesBancoDados()

#imprimirNomesBancoDados()



#NomeBancoDados = criarBancoDados('BD_Calculo_1', True)
#imprimirNomesBancoDados()
#NomeTabela = criarTabela(NomeBancoDados, 'Tabela_Questoes', True)
#imprimirNomesTabelas(NomeBancoDados)
#inserirDados()
editarListaDados('BD_Calculo_1', 'Tabela_Questoes')
imprimirDados('BD_Calculo_1', 'Tabela_Questoes')


#editarListaDados('MMB1_2005', 'Notas_P2')
#imprimirDados('MMB1_2005', 'Notas_P2')








#criarBancoDados('BancoTeste3')
#inserirDados('BancoTeste3')
#imprimirDados('BancoTeste3')
#imprimirNomesTabelas('BancoTeste3')


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
    pass
