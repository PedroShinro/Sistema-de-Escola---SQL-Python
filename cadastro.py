from conexao import *

# Inserir aluno
def inserir_aluno(nome_aluno, email, telefone, cpf, sexo, data_nascimento, turma):
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("INSERT INTO alunos (nome_aluno, email, telefone, cpf, sexo, data_nascimento, turma) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (nome_aluno, email, telefone, cpf, sexo, data_nascimento, turma))
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
            print(f"[ID: {alunos[0]}], [ Nome: {alunos[1]}], [ Email: {alunos[2]}], [ Telefone: {alunos[3]}], [ CPF: {alunos[4]}], [ Sexo: {alunos[5]}], [ Data de Nascimento: {alunos[6]}], [ Turma: {alunos[7]}]")
        return resultado
    except pymysql.MySQLError as e:
        print(f'Erro ao listar alunos: {e}')
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

# alunos por id
def alunos_por_id(id): 
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM alunos WHERE id_aluno = %s", (id,))
        resultado = cursor.fetchall()
        for alunos in resultado:
            print(f"[ID: {alunos[0]}], [ Nome: {alunos[1]}], [ Email: {alunos[2]}], [ Telefone: {alunos[3]}], [ CPF: {alunos[4]}], [ Sexo: {alunos[5]}], [ Data de Nascimento: {alunos[6]}], [ Turma: {alunos[7]}]")
        return resultado
    except pymysql.MySQLError as e:
        print(f"Erro ao listar aluno por ID: {e}")
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

def alunos_por_cpf(cpf):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        
        # Remove formatação do CPF para busca mais flexível
        cpf_limpo = cpf.replace('.', '').replace('-', '')
        
        # Busca por CPF exato ou CPF sem formatação
        cursor.execute("""
            SELECT * FROM alunos 
            WHERE cpf = %s OR REPLACE(REPLACE(cpf, '.', ''), '-', '') = %s
        """, (cpf, cpf_limpo))
        
        resultado = cursor.fetchall()
        for alunos in resultado:
            print(f"[ID: {alunos[0]}], [ Nome: {alunos[1]}], [ Email: {alunos[2]}], [ Telefone: {alunos[3]}], [ CPF: {alunos[4]}], [ Sexo: {alunos[5]}], [ Data de Nascimento: {alunos[6]}], [ Turma: {alunos[7]}]")
        return resultado
    except pymysql.MySQLError as e:
        print(f"Erro ao listar aluno por CPF: {e}")
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()


# Atualizar aluno
def atualizar_alunos(id, nome_aluno = None, email = None, telefone = None, cpf = None, sexo = None, data_nascimento = None, turma = None):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT nome_aluno, email, telefone, cpf, sexo, data_nascimento, turma FROM alunos WHERE id_aluno = %s", (id,))
        resultado = cursor.fetchone()
        if nome_aluno is None:
            nome_aluno = resultado[0]
        if email is None:
            email = resultado[1]
        if telefone is None:
            telefone = resultado[2]
        if cpf is None:
            cpf = resultado[3]
        if sexo is None:
            sexo = resultado[4]
        if data_nascimento is None:
            data_nascimento = resultado[5]
        if turma is None:
            turma = resultado[6]

        cursor.execute("UPDATE alunos SET nome_aluno = %s, email = %s, telefone = %s, cpf = %s, sexo = %s, data_nascimento = %s, turma = %s WHERE id_aluno = %s",
        (nome_aluno, email, telefone, cpf, sexo, data_nascimento, turma, id))
        conexao.commit()
        print(f"Usuário com ID {id} atualizado com sucesso!")
    except pymysql.MySQLError as e:
        print(f'Erro ao atualizar aluno: {e}')
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()


# Deletar aluno
def deletar_aluno(id):
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("DELETE FROM alunos WHERE id_aluno = %s", (id,))

        conexao.commit()
        print(f"Usuário com ID {id} deletado com sucesso!")
    except pymysql.MySQLError as e:
        print(f'Erro ao deletar aluno: {e}')
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

# Inserir curso
def inserir_curso(nome_curso, carga_horaria, preco):
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("INSERT INTO cursos (nome_curso, carga_horaria, preco) VALUES (%s, %s, %s)",    (nome_curso, carga_horaria, preco))

        conexao.commit()
        print(f"Curso {nome_curso} inserido com sucesso!")
    except pymysql.MySQLError as e:
        print(f'Erro ao inserir curso: {e}')
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

# Listar cursos
def listar_cursos():
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM cursos")
        resultado = cursor.fetchall()
        for cursos in resultado:
            print(f"[ID: {cursos[0]}], [ Nome: {cursos[1]}], [ Carga Horária: {cursos[2]}], [ Preço: {cursos[3]}]")  
        return resultado
    except pymysql.MySQLError as e:
        print(f'Erro ao listar cursos: {e}')
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()


# Atualizar curso
def atualizar_curso(id, nome = None, carga_horaria = None, preco = None):
    try:
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
        print(f"Curso com ID {id} atualizado com sucesso!")
    except pymysql.MySQLError as e:
        print(f'Erro ao atualizar curso: {e}')
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

# Deletar curso
def deletar_curso(id):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM cursos WHERE id_curso = %s", (id,))
        conexao.commit()
        print(f"Curso com ID {id} deletado com sucesso!")
    except pymysql.MySQLError as e:
        print(f'Erro ao deletar curso: {e}')   
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()


#Inserir turma
def inserir_turma(nome_turma, cursos, data_inicio):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO turmas(nome_turma, cursos, data_inicio) VALUES (%s, %s, %s)", (nome_turma, cursos, data_inicio))
        conexao.commit()

        print(f"{nome_turma} inserida com sucesso!")
    except pymysql.MySQLError as e:
        print(f'Erro ao inserir turma: {e}')
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()


# listar turmas
def listar_turmas():
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM turmas")
        resultado = cursor.fetchall()
        for turmas in resultado:
            print(f"[ID: {turmas[0]}], [ Nome: {turmas[1]}], [ cursos: {turmas[2]}], [ Data de Início: {turmas[3]}]")
        return resultado
    except pymysql.MySQLError as e:
        print(f'Erro ao listar turmas: {e}')
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

listar_turmas()

# atualizar turma
def atualizar_turma(id, nome = None, cursos = None, data_inicio = None,):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT nome_turma, cursos, data_inicio FROM turmas WHERE id_turma = %s",(id,))
        resultado = cursor.fetchone()
        if nome is None:
            nome = resultado[0]
        if cursos is None:
            cursos = resultado[1]
        if data_inicio is None:
            data_inicio = resultado[2]

        cursor.execute("UPDATE turmas SET nome_turma = %s, cursos = %s, data_inicio = %s WHERE id_turma = %s", (nome , cursos, data_inicio, id))
        conexao.commit()

        print(f"Turma com ID {id} atualizada com sucesso!")
    except pymysql.MySQLError as e:
        print(f'Erro ao atualizar turma: {e}')
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

# Deletar turma
def deletar_turma(id):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM turmas WHERE id_turma = %s", (id,))
        conexao.commit()
        print(f"Turma com ID {id} deletada com sucesso!")
    except pymysql.MySQLError as e:
        print(f'Erro ao deletar turma: {e}')
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

#listar notas
def listar_notas():
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM notas")
        resultado = cursor.fetchall()
        for notas in resultado:
            print(f"[ID: {notas[0]}], [NOTA_1: {notas[1]}], [NOTA_2: {notas[2]}], [MEDIA: {notas[3]}], [SITUAÇÃO: {notas[4]}]")
        return resultado
    except pymysql.MySQLError as e:
        print(f"Erro ao listar notas: {e}")
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

#Inserir notas
def inserir_notas(nome_aluno, nota1, nota2):
    try:
        # Buscar ID do aluno pelo nome
        id_aluno = buscar_aluno_por_nome(nome_aluno)
        if not id_aluno:
            print(f"Aluno {nome_aluno} não encontrado!")
            return False
            
        # Calcular média e situação
        n1, n2 = float(nota1), float(nota2)
        media = (n1 + n2) / 2
        situacao = "Aprovado" if media >= 6 else "Reprovado"
        
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO notas (id_aluno, nota1, nota2, media, situacao) VALUES (%s, %s, %s, %s, %s)",
        (id_aluno, nota1, nota2, media, situacao))
        conexao.commit()
        print("Notas inseridas com sucesso!")
        return True
    except pymysql.MySQLError as e:
        print(f"Erro ao inserir as notas: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()


#atualizar notas
def atualizar_notas(nome_aluno, nota1, nota2):
    try:
        # Buscar ID do aluno pelo nome
        id_aluno = buscar_aluno_por_nome(nome_aluno)
        if not id_aluno:
            print(f"Aluno {nome_aluno} não encontrado!")
            return False
            
        # Calcular média e situação
        n1, n2 = float(nota1), float(nota2)
        media = (n1 + n2) / 2
        situacao = "Aprovado" if media >= 6 else "Reprovado"
        
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("UPDATE notas SET nota1 = %s, nota2 = %s, media = %s, situacao = %s WHERE id_aluno = %s",
                       (nota1, nota2, media, situacao, id_aluno))
        conexao.commit()
        print(f"Notas do aluno {nome_aluno} foram atualizadas!")
        return True
    except pymysql.MySQLError as e:
        print(f"Erro ao atualizar as notas: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

def buscar_aluno_por_nome(nome_aluno):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT id_aluno FROM alunos WHERE nome_aluno = %s", (nome_aluno,))
        resultado = cursor.fetchone()
        return resultado[0] if resultado else None
    except pymysql.MySQLError as e:
        print(f"Erro ao buscar aluno: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

def deletar_notas(nome_aluno):
    try:
        # Buscar ID do aluno pelo nome
        id_aluno = buscar_aluno_por_nome(nome_aluno)
        if not id_aluno:
            print(f"Aluno {nome_aluno} não encontrado!")
            return False
            
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM notas WHERE id_aluno = %s", (id_aluno,))
        conexao.commit()
        print(f"Notas do aluno {nome_aluno} deletadas com sucesso!")
        return True
    except pymysql.MySQLError as e:
        print(f"Erro ao deletar as notas: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
            
# operações de filtragem no banco de dados

def alunos_aprovados():
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT a.nome_aluno, n.media, n.situacao FROM alunos as a JOIN notas as n ON a.id_aluno = n.id_aluno WHERE n.situacao = 'Aprovado'")
        resultado = cursor.fetchall()
        for alunos in resultado:
            print(f"[Nome: {alunos[0]}], [Média: {alunos[1]}], [Situação: {alunos[2]}]")
        return resultado
    except pymysql.MySQLError as e:
        print(f"Erro ao listar alunos aprovados: {e}")
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

# Listar alunos reprovados           
def alunos_reprovados():
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT a.nome_aluno, n.media, n.situacao FROM alunos as a JOIN notas as n ON a.id_aluno = n.id_aluno WHERE n.situacao = 'Reprovado'")
        resultado = cursor.fetchall()
        for alunos in resultado:
            print(f"[Nome: {alunos[0]}], [Média: {alunos[1]}], [Situação: {alunos[2]}]")
        return resultado
    except pymysql.MySQLError as e:
        print(f"Erro ao listar alunos reprovados: {e}")
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()


# Listar alunos por curso
def alunos_por_curso(nome_curso):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT a.nome_aluno, c.nome_curso FROM alunos as a JOIN cursos as c ON a.cursoaluno = c.id_curso WHERE c.nome_curso = %s", (nome_curso,))
        resultado = cursor.fetchall()
        for alunos in resultado:
            print(f"[Nome: {alunos[0]}], [Curso: {alunos[1]}]")
        return resultado
    except pymysql.MySQLError as e:
        print(f"Erro ao listar alunos por curso: {e}")
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()


# Listar alunos por turma
def alunos_por_turma(nome_turma):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT a.nome_aluno, t.nome_turma FROM alunos as a JOIN turmas as t ON a.turmaaluno = t.id_turma WHERE t.nome_turma = %s", (nome_turma,))
        resultado = cursor.fetchall()
        for alunos in resultado:
            print(f"[Nome: {alunos[0]}], [Turma: {alunos[1]}]")
        return resultado
    except pymysql.MySQLError as e:
        print(f"Erro ao listar alunos por turma: {e}")
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

          
# alunos por data de início
def alunos_data_inicio(data_inicio):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT a.nome_aluno, t.data_inicio, t.nome_turma FROM alunos as a JOIN turmas as t ON a.turmaaluno = t.id_turma WHERE t.data_inicio = %s", (data_inicio,))
        resultado = cursor.fetchall()
        for alunos in resultado:
            print(f"[Nome: {alunos[0]}], [Data de Início: {alunos[1]}], [Turma: {alunos[2]}]")
        return resultado
    except pymysql.MySQLError as e:
        print(f"Erro ao listar alunos por data de início: {e}")
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

def alunos_por_notas():
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        # Modificado para incluir o ID do aluno
        cursor.execute("SELECT a.id_aluno, a.nome_aluno, n.nota1, n.nota2, n.media, n.situacao FROM alunos as a JOIN notas as n ON a.id_aluno = n.id_aluno")
        resultado = cursor.fetchall()
        for alunos in resultado:
            print(f"[ID: {alunos[0]}], [Nome: {alunos[1]}], [Nota 1: {alunos[2]}], [Nota 2: {alunos[3]}], [Média: {alunos[4]}], [Situação: {alunos[5]}]")
        return resultado
    except pymysql.MySQLError as e:
        print(f"Erro ao listar alunos por notas: {e}")
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()