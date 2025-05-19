import pymysql

def conectar():
    try:
        conexao = pymysql.connect(
            host='localhost',
            user='root',
            password='240301',
            database='cadastro',
        )
        print('Conectado ao banco de dados!')
        return conexao
    except pymysql.MySQLError as e:
        print(f'Erro ao conectar ao banco de dados: {e}')
        return None

# Inserir aluno
def inserir_aluno(id_aluno, nome_aluno, email, telefone, cpf, sexo, data_nascimento):
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("INSERT INTO alunos (id_aluno, nome_aluno, email, telefone, cpf, sexo, data_nascimento) VALUES (%s, %s,%s,%s, %s,%s, %s)",
        (id_aluno, nome_aluno, email, telefone, cpf, sexo, data_nascimento))

        conexao.commit()
        print(f"Usuário {nome_aluno} inserido com sucesso!")
    except pymysql.MySQLError as e:
        print(f'Erro ao inserir aluno: {e}')
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
# Listar alunos
def listar_alunos():
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM alunos")
        resultado = cursor.fetchall()
        for alunos in resultado:
            print(f"[ID: {alunos[0]}], [ Nome: {alunos[1]}], [ Email: {alunos[2]}], [ Telefone: {alunos[3]}], [ CPF: {alunos[4]}], [ Sexo: {alunos[5]}], [ Data de Nascimento: {alunos[6]}]")
        return resultado
    except pymysql.MySQLError as e:
        print(f'Erro ao listar alunos: {e}')
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

# Atualizar aluno
def atualizar_alunos(id, nome_aluno = None, novo_email = None, telefone = None, cpf = None, sexo = None, data_nascimento = None):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT nome_aluno, email, telefone, cpf, sexo, data_nascimento FROM alunos WHERE id_aluno = %s",(id,))
    resultado = cursor.fetchone()
    if nome is None:
        nome = resultado[0]
    if novo_email is None:
        novo_email = resultado[1]
    if telefone is None:
        telefone = resultado[2]
    if cpf is None:
        cpf = resultado[3]
    if sexo is None:
        sexo = resultado[4]
    if data_nascimento is None:
        data_nascimento = resultado[5]

    cursor.execute("UPDATE alunos SET nome_aluno = %s, email = %s, telefone = %s, cpf = %s, sexo = %s, data_nascimento = %s WHERE id_aluno = %s",
    (nome, novo_email, telefone, cpf, sexo, data_nascimento, id))
    conexao.commit()
    cursor.close()
    conexao.close()
    print(f"Usuário com ID {id} atualizado com sucesso!")

# Deletar aluno
def deletar_aluno(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM alunos WHERE id_aluno = %s", (id,))

    conexao.commit()
    cursor.close()  
    conexao.close()
    print(f"Usuário com ID {id} deletado com sucesso!")

# Inserir curso
def inserir_curso(id_curso, nome_curso, carga_horaria, preco):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO cursos (id_curso, nome_curso, carga_horaria, preco) VALUES (%s, %s, %s, %s)",    (id_curso, nome_curso, carga_horaria, preco))

    conexao.commit()
    cursor.close()
    conexao.close()
    print(f"Curso {nome_curso} inserido com sucesso!")

# Listar cursos
def listar_cursos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM cursos")
    resultado = cursor.fetchall()
    for cursos in resultado:
        print(f"[ID: {cursos[0]}], [ Nome: {cursos[1]}], [ Carga Horária: {cursos[2]}], [ Preço: {cursos[3]}]")
    cursor.close()
    conexao.close()
    return resultado

# Atualizar curso
def atualizar_curso(id, nome = None, carga_horaria = None, preco = None):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT nome_curso, carga_horaria, preco FROM cursos WHERE id_curso = %s",(id,))
    resultado = cursor.fetchone()
    if nome is None:
        nome = resultado[0]
    if carga_horaria is None:
        carga_horaria = resultado[1]
    if preco is None:
        preco = resultado[2]

    cursor.execute("UPDATE cursos SET nome_curso = %s, carga_horaria = %s, preco = %s WHERE id_curso = %s", (nome , carga_horaria, preco, id))
    conexao.commit()
    cursor.close()
    conexao.close()
    print(f"Curso com ID {id} atualizado com sucesso!")

# Deletar curso
def deletar_curso(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM cursos WHERE id_curso = %s", (id,))

    conexao.commit()
    cursor.close()  
    conexao.close()
    print(f"Curso com ID {id} deletado com sucesso!")

#Inserir turma
def inserir_turma(id_turma, nome_turma, turno, data_inicio):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO turmas(id_turma, nome_turma, turno, data_inicio) VALUES (%s, %s, %s, %s)", (id_turma, nome_turma, turno, data_inicio))
    conexao.commit()
    cursor.close()
    conexao.close()
    print(f"Turma {nome_turma} inserida com sucesso!")

inserir_turma(9, 'A', 'noite', '2025-08-01')

# listar turmas
def listar_turmas():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM turmas")
    resultado = cursor.fetchall()
    for turmas in resultado:
        print(f"ID: {turmas[0]}, Nome:{turmas[1]}, Turno:{turmas[2]}, Data de Inicio:{turmas[3]}")
    cursor.close()
    conexao.close()
    return resultado


# atualizar turma
def atualizar_turma(id, nome = None, turno = None, data_inicio = None):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT nome_turma, turno, data_inicio FROM turmas WHERE id_turma = %s",(id,))
    resultado = cursor.fetchone()
    if nome is None:
        nome = resultado[0]
    if turno is None:
        turno = resultado[1]
    if data_inicio is None:
        data_inicio = resultado[2]

    cursor.execute("UPDATE turmas SET nome_turma = %s, turno = %s, data_inicio = %s WHERE id_turma = %s", (nome , turno, data_inicio, id))
    conexao.commit()
    cursor.close()
    conexao.close()
    print(f"Turma com ID {id} atualizada com sucesso!")

# deletar turma
def deletar_turma(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM turmas WHERE id_turma = %s", (id,))

    conexao.commit()
    cursor.close()  
    conexao.close()
    print(f"Turma com ID {id} deletada com sucesso!")