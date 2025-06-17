# Importando dependências do Tkinter
import tkinter as tk
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

# Importando pillow
from PIL import ImageTk, Image

# tk calendar
from tkcalendar import Calendar, DateEntry
from datetime import *

# import pattern de celular
import re

# Ligação com o bd
from cadastro import *

# Instalações:---
# pip install pymysql
# pip install tkcalendar

# Cores
co0 = '#2e2d2b' # Preto
co1 = '#feffff' # Branco
co2 = '#e5e5e5' # Gray
co3 = '#00a095' # Verde
co4 = '#403d3d' # Letra
co5 = '#003480' # Azul
co6 = '#038cfc' # Azul
co7 = '#ef5350' # Vermelho
co8 = '#263238' # cinza escuro
co9 = '#e9edf5' # cinza claro
co10 = '#a1a1a1' # Campo de entrada
co11 = '#d3af37'


# Criando a Janela
janela = Tk()
janela.title('Colégio Golden Ball') # Nome do programa
janela.geometry('850x620') # Tamanho da janela
janela.configure(background= co8) # Cor da janela
janela.resizable(width= FALSE, height= FALSE) # Tamanho fixo da janela

# Estilo da janela
style = Style(janela)
style.theme_use('clam')


# Frames--------------------------------------------------------------------------

# FRAME - logo ----------
frame_logo = Frame(janela, width= 850, height= 52, bg= co5)
frame_logo.grid(row= 0, column= 0, pady= 0, sticky= NSEW)

# Conteúdo
app_lg1 = Image.open('img-estudante-96.png')
app_lg2 = app_lg1.resize((50, 50))
app_lg3 = ImageTk.PhotoImage(app_lg2)
app_logo = Label(frame_logo, image= app_lg3, text= 'Cadastro de Alunos', width= 850, compound= LEFT, relief= RAISED, anchor= NW, font= ('Ivy 15 bold'), bg= co5, fg= co1)
app_logo.place(x= 0, y= 0)
# ----------

# Linha divisória ----------
ttk.Separator(janela, orient= HORIZONTAL).grid(row= 1, columnspan= 1, ipadx= 680)
# ----------

# FRAME - cadastro, add e salvar (Superior) ----------
frame_dados = Frame(janela, width= 850, height= 65, bg= co8)
frame_dados.grid(row= 2, column= 0, pady= 0, padx= 0, sticky= NSEW)

# Botão "CADASTRO"
app_img_cadastro = Image.open('img-add-30.png')
app_img_cadastro = app_img_cadastro.resize((18, 18))
app_img_cadastro = ImageTk.PhotoImage(app_img_cadastro)
app_cadastro = Button(frame_dados, command= lambda:control('cadastro'), image= app_img_cadastro, text= ' Cadastro', width= 100, compound= LEFT, overrelief= RIDGE, font= ('Ivy 11'), bg= co8, fg= co1)
app_cadastro.place(x= 10, y= 30)

# Botão "ADICIONAR"
app_img_adicionar = Image.open('img-add-30.png')
app_img_adicionar = app_img_adicionar.resize((18, 18))
app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)
app_adicionar = Button(frame_dados, command= lambda:control('adicionar'), image= app_img_adicionar, text= ' Adicionar', width= 100, compound= LEFT, overrelief= RIDGE, font= ('Ivy 11'), bg= co8, fg= co1)
app_adicionar.place(x= 123, y= 30)

# Botão "SALVAR"
app_img_salvar = Image.open('img-salvar-30.png')
app_img_salvar = app_img_salvar.resize((18, 18))
app_img_salvar = ImageTk.PhotoImage(app_img_salvar)
app_salvar = Button(frame_dados, command= lambda:control('note'), image= app_img_salvar, text= ' Notas', width= 100, compound= LEFT, overrelief= RIDGE, font= ('Ivy 11'), bg= co8, fg= co1)
app_salvar.place(x= 236, y= 30)
# Linha divisória ----------
ttk.Separator(janela, orient= HORIZONTAL).grid(row= 3, columnspan= 1, ipadx= 680)
# ----------

# FRAME - inserir dados do aluno (meio) ----------
frame_detalhes = Frame(janela, width= 850, height= 200, bg= co8)
frame_detalhes.grid(row= 4, column= 0, pady= 0, padx= 10, sticky= NSEW)
# ----------

# FRAME - tabela dos cadastros (Inferior) ----------
frame_tabela = Frame(janela, width= 850, height= 200, bg= co8)
frame_tabela.grid(row= 5, column= 0, pady= 0, padx= 10, sticky= NSEW)
# ----------                            

# --------------------------------------------------------------------------






# Função para cadastrar alunos----------------------------------------------------
def alunos():
    # BOTÃO - Função Novo Aluno
    def novo_aluno():
        nome = e_nome.get()
        email = e_email.get()
        telefone = e_tel.get()
        sexo = c_sexo.get()
        data = data_nascimento.get()
        cpf = e_cpf.get()
        tur = c_turma.get()

        lista = [nome, email, telefone, sexo, data, cpf, tur]

        # Verifica campos vazios
        for i in lista:
            if i == '':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return
        
        # Inserir no BD 
        inserir_aluno(nome, email, telefone, cpf, sexo, data, tur)

        # Mostrar mensagem de sucesso
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

        # limpar campos de entrada
        e_nome.delete(0, END)
        e_email.delete(0, END)
        e_tel.delete(0, END)
        e_cpf.delete(0, END)
        c_sexo.delete(0, END)
        data_nascimento.delete(0, END)
        c_turma.delete(0, END)

        # Apresemta os valores na tabela
        listar_alunos()
        alunos()

    def limpar_tabela():
            for item in tree_aluno.get_children():
                tree_aluno.delete(item)
    
        

    def procurar_aluno():
        # Campo de busca
        termo = e_nome_procurar.get().strip()

        # Retorna mensagem caso o campo esteja vazio
        if not termo:
            messagebox.showinfo("Aviso", "Digite um ID ou CPF.")
            return

        # Limpa a tabela antes de exibir o resultado
        limpar_tabela()

        # Verifica se é ID (apenas números e até 10 dígitos)
        if termo.isdigit() and len(termo) <= 10:
            # Se for ID
            resultado = alunos_por_id(int(termo))
        else:
            # Assume que é CPF (com ou sem formatação)
            resultado = alunos_por_cpf(termo)

        if resultado:
            # Exibe os resultados na tabela
            for aluno in resultado:
                tree_aluno.insert('', 'end', values=aluno)
        else:
            messagebox.showinfo("Aviso", "Aluno não encontrado.")

    # Função para Atualizar Alunos----------------------------------------------------
    def update_aluno():
        # limpar campos de entrada
        e_nome.delete(0, END)
        e_email.delete(0, END)
        e_tel.delete(0, END)
        e_cpf.delete(0, END)
        c_sexo.delete(0, END)
        data_nascimento.delete(0, END)
        c_turma.delete(0, END)

        try:
            tree_itens = tree_aluno.focus()
            tree_dicionario = tree_aluno.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            # Alualizar valores da tabela
            e_nome.insert(0, tree_lista[1])
            e_email.insert(0, tree_lista[2])
            e_tel.insert(0, tree_lista[3])
            e_cpf.insert(0, tree_lista[4])
            c_sexo.insert(0, tree_lista[5])
            data_nascimento.insert(0, tree_lista[6])
            c_turma.insert(0, tree_lista[7])

            def update():
                nome = e_nome.get()
                email = e_email.get()
                telefone = e_tel.get()
                sexo = c_sexo.get()
                data = data_nascimento.get()
                cpf = e_cpf.get()
                tur = c_turma.get()

                lista = [valor_id, nome, email, telefone, sexo, data, cpf, tur]

                # Verifica campos vazios
                for i in lista:
                    if i == '':
                        messagebox.showerror('Erro', 'Preencha todos os campos')
                        return
                
                # Inserir no BD 
                atualizar_alunos(valor_id, nome, email, telefone, cpf, sexo, data, tur)

                # Mostrar mensagem de sucesso
                messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')

                # limpar campos de entrada
                e_nome.delete(0, END)
                e_email.delete(0, END)
                e_tel.delete(0, END)
                e_cpf.delete(0, END)
                c_sexo.delete(0, END)
                data_nascimento.delete(0, END)
                c_turma.delete(0, END)

                # Apresemta os valores na tabela
                listar_alunos()
                alunos()

                # Destruir botão Salvar (Sumir depois que atualiza os dados)
                botao_salvar.destroy()

            # Botão SALVAR
            botao_salvar = Button(frame_detalhes, command= update, anchor= CENTER, text= 'Salvar Atualização'.upper(), overrelief= RIDGE, font=('Ivy 7 bold'), bg= co3, fg= co1)
            botao_salvar.place(x= 716, y= 130)
        
        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos cursos da tabela')

    # BOTÃO - Função Deletar Curso
    def delete_aluno():
        try:
            tree_itens = tree_aluno.focus()
            tree_dicionario = tree_aluno.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            # Botão deletar
            deletar_aluno([valor_id])

            # Mostrar mensagem de sucesso
            messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')

            listar_alunos()


        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos cursos da tabela')

    
        
    








    # Campos de entrada
    l_nome = Label(frame_detalhes, text= 'Nome: *', height= 1, anchor= NW, font= ('Ivy 10'), bg= co8, fg= co1)
    l_nome.place(x= 4, y= 10)
    e_nome = Entry(frame_detalhes, width= 45, justify= 'left', relief= 'solid', bg= co10, fg= co0)
    e_nome.place(x= 7, y= 40)

    l_email = Label(frame_detalhes, text= 'Email: *', height= 1, anchor= NW, font= ('Ivy 10'), bg= co8, fg= co1)
    l_email.place(x= 4, y= 70)
    e_email = Entry(frame_detalhes, width= 45, justify= 'left', relief= 'solid', bg= co10, fg= co0)
    e_email.place(x= 7, y= 100)

    l_tel = Label(frame_detalhes, text= 'Telefone: *', height= 1, anchor= NW, font= ('Ivy 10'), bg= co8, fg= co1)
    l_tel.place(x= 4, y= 130)
    e_tel = Entry(frame_detalhes, width= 20, justify= 'left', relief= 'solid', bg= co10, fg= co0)
    e_tel.place(x= 7, y= 160)

    # Combobox Sexo
    l_sexo = Label(frame_detalhes, text= 'Sexo: *', height= 1, anchor= NW, font= ('Ivy 10'), bg= co8, fg= co1)
    l_sexo.place(x= 183, y= 130)
    c_sexo = ttk.Combobox(frame_detalhes, width= 12, font= ('Ivy 8 bold'))
    c_sexo['values'] = ('M', 'F')
    c_sexo.place(x= 188, y= 160)

    l_data_nascimento = Label(frame_detalhes, text= 'Data de nascimento: *', height= 1, anchor= NW, font= ('Ivy 10'), bg= co8, fg= co1)
    l_data_nascimento.place(x= 366, y= 10)
    data_nascimento = DateEntry(frame_detalhes, date_pattern= 'yyyy-mm-dd', width= 18, background= co5, foreground= 'white', borderwidth= 2, year= 2025)
    data_nascimento.place(x= 370, y= 40)

    l_cpf = Label(frame_detalhes, text= 'CPF: *', height= 1, anchor= NW, font= ('Ivy 10'), bg= co8, fg= co1)
    l_cpf.place(x= 365, y= 70)
    e_cpf = Entry(frame_detalhes, width= 20, justify= 'left', relief= 'solid', bg= co10, fg= co0)
    e_cpf.place(x= 369, y= 100)

    # Pegando os cursos (substituir dados)
    turmas = listar_turmas()
    turma = []

    for i in turmas:
        turma.append(i[1])

    l_turma = Label(frame_detalhes, text= 'Turma: *', height= 1, anchor= NW, font= ('Ivy 10'), bg= co8, fg= co1)
    l_turma.place(x= 366, y= 130)
    
    c_turma = ttk.Combobox(frame_detalhes, width= 20, font= ('Ivy 8 bold'))
    c_turma['values'] = (turma)
    c_turma.place(x= 370, y= 160)

    # Linha separatória
    l_linha = Label(frame_detalhes, relief= GROOVE, text= 'h', width= 1, height= 100, anchor= NW, font= ('Ivy 1'), bg= co0, fg= co0)
    l_linha.place(x= 520, y= 10)

    # Procurar aluno----------
    l_nome = Label(frame_detalhes, text= 'Procurar Aluno [ Entra o nome ]', height= 1, anchor= NW, font= ('Ivy 10'),  bg= co8, fg= co1)
    l_nome.place(x= 540, y= 10)
    e_nome_procurar = Entry(frame_detalhes, width= 29, justify= 'center', relief= 'solid', font= ('Ivy 10'), bg= co10, fg= co0)
    e_nome_procurar.place(x= 543, y= 35)
    

    botao_procurar = Button(frame_detalhes, command= procurar_aluno, anchor= CENTER, text= 'Procurar', width= 9, overrelief= RIDGE, font= ('Ivy 7 bold'), bg= co8, fg= co1)
    botao_procurar.place(x= 760, y= 35.5)
    # ----------

    # Botão Salvar
    botao_salvar = Button(frame_detalhes, command= novo_aluno, anchor= CENTER, text= 'Salvar'.upper(), width= 9, overrelief= RIDGE, font= ('Ivy 7 bold'), bg= co3, fg= co1)
    botao_salvar.place(x= 544, y= 110)

    # Botão Atualizar
    botao_atualizar = Button(frame_detalhes,command= update_aluno, anchor= CENTER, text= 'Atualizar'.upper(), width= 9, overrelief= RIDGE, font= ('Ivy 7 bold'), bg= co6, fg= co1)
    botao_atualizar.place(x= 544, y= 135)

    # Botão Deletar
    botao_deletar = Button(frame_detalhes, command= delete_aluno, anchor= CENTER, text= 'Deletar'.upper(), width= 9, overrelief= RIDGE, font= ('Ivy 7 bold'), bg= co7, fg= co1)
    botao_deletar.place(x= 544, y= 160)

    # Botão Ver
    botao_ver = Button(frame_detalhes, anchor= CENTER, text= 'Ver'.upper(), width= 9, overrelief= RIDGE, font= ('Ivy 7 bold'), bg= co8, fg= co1)
    botao_ver.place(x= 760, y= 160)

    # Tabela Alunos
    def mostrar_alunos():
        app_nome = Label(frame_tabela, text= 'Tabela de Alunos', height= 1, pady= 0, padx=0, relief= 'flat', anchor= NW, font= ('Ivy 10 bold'), bg= co8, fg= co1)
        app_nome.grid(row= 0, column= 0, padx= 0, pady= 10, sticky= NSEW)

        # Criando
        list_header = ['ID', 'Nome', 'E-mail', 'Telefone', 'CPF', 'sexo', 'Data nasc', 'Turma / Curso']
        
        df_list = listar_alunos()
        
        global tree_aluno
        
        tree_aluno = ttk.Treeview(frame_tabela, selectmode= 'extended', columns= list_header, show= 'headings')

        # Vertical Scrollbar
        vsb = ttk.Scrollbar(frame_tabela, orient= 'vertical', command= tree_aluno.yview)

        # Horizontal Scrollbar
        hsb = ttk.Scrollbar(frame_tabela, orient='horizontal', command= tree_aluno.xview)
        
        tree_aluno.configure(yscrollcommand= vsb.set, xscrollcommand= hsb.set)
        
        tree_aluno.grid(column= 0, row= 1, sticky= 'nsew')
        vsb.grid(column= 1, row= 1, sticky= 'ns')
        hsb.grid(column= 0, row= 2, sticky= 'ew')
        frame_tabela.grid_rowconfigure(0, weight= 12)
        
        hd=["nw", "nw", "nw", "center", "center", "center", "center", "center"]
        h=[40, 210, 180, 90, 90, 35, 75, 90]
        n=0
        
        for col in list_header:
            tree_aluno.heading(col, text= col.title(), anchor= NW)
        
            tree_aluno.column(col, width= h[n], anchor= hd[n])
        
            n+=1
        
        for item in df_list:
            tree_aluno.insert('', 'end', values=item)
        
    mostrar_alunos()

    


# ----------------------------------------------------





# FUNÇÃO TELA - adidionar turmas e cursos-----------------------------------------
def adicionar():
    
    frame_tabela_curso = Frame(frame_tabela, width= 300, height= 100, bg= co8)
    frame_tabela_curso.grid(row= 0, column= 0, pady= 0, padx= 10, sticky=NSEW)

    frame_tabela_linha = Frame(frame_tabela, width= 30, height= 200, bg= co8)
    frame_tabela_linha.grid(row= 0, column= 1, pady= 0, padx= 10, sticky=NSEW)

    frame_tabela_turma = Frame(frame_tabela, width= 300, height= 200, bg= co8)
    frame_tabela_turma.grid(row= 0, column= 2, pady= 0, padx= 10, sticky=NSEW)

    # Detalhes do curso ----------

    # BOTÃO - Função Novo Curso
    def novo_curso():
        # Botão Salvar----------
        nome_curso = e_nomecurso.get()
        carga_horaria = e_duracao.get()
        preco = e_preco.get()

        lista = [nome_curso, carga_horaria, preco]
        
        # Verifica se possui valor vazio
        for i in lista:
            if i == '':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return
        
        # Inserindo os danos no banco
        inserir_curso(nome_curso, carga_horaria, preco)

        # Mostrar mensagem de sucesso
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')
        # ----------

        # Botão Deletar----------
        e_nomecurso.delete(0,END)
        e_duracao.delete(0,END)
        e_preco.delete(0,END)

        # Mostrar os valores na tabela
        mostrar_cursos()
        adicionar()

    # BOTÃO - Função Atualizar Curso
    def update_curso():
        e_nomecurso.delete(0, END)
        e_duracao.delete(0, END)
        e_preco.delete(0, END)
        
        try:
            tree_itens = tree_curso.focus()
            tree_dicionario = tree_curso.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            # Botão Atualizar - Insere os valores nas entries
            e_nomecurso.insert(0, tree_lista[1])
            e_duracao.insert(0, tree_lista[2])
            e_preco.insert(0, tree_lista[3])

            # FUNÇÃO - Atualizar
            def update():
                nome_curso = e_nomecurso.get()
                carga_horaria = e_duracao.get()
                preco = e_preco.get()

                lista = [valor_id, nome_curso, carga_horaria, preco]
                
                # Verifica se possui valor vazio
                for i in lista:
                    if i == '':
                        messagebox.showerror('Erro', 'Preencha todos os campos')
                        return
                
                # Inserindo os danos no banco
                atualizar_curso(valor_id, nome_curso, carga_horaria, preco)

                # Mostrar mensagem de sucesso
                messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')
                # ----------

                # Botão Deletar----------
                e_nomecurso.delete(0, END)
                e_duracao.delete(0, END)
                e_preco.delete(0, END)

                # Mostrar os valores na tabela
                mostrar_cursos()
                adicionar()

                # Destruir botão Salvar (Sumir depois que atualiza os dados)
                botao_salvar.destroy()
           
            # Botão SALVAR
            botao_salvar = Button(frame_detalhes, command= update, anchor= CENTER, text= 'Salvar Atualização'.upper(), overrelief= RIDGE, font=('Ivy 7 bold'), bg= co3, fg= co1)
            botao_salvar.place(x= 229, y= 130)

        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos cursos da tabela')
        

        
    # BOTÃO - Função Deletar Curso
    def delete_curso():
        try:
            tree_itens = tree_curso.focus()
            tree_dicionario = tree_curso.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            # Botão deletar
            deletar_curso([valor_id])

            # Mostrar mensagem de sucesso
            messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')

            mostrar_cursos()
            adicionar()


        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos cursos da tabela')

        
    
    # Campo NOME DO CURSO
    l_nome = Label(frame_detalhes, text= 'Nome do curso: *', height= 1, anchor= NW, font= ('Ivy 10'), bg= co8, fg= co1)
    l_nome.place(x= 4, y= 10)
    e_nomecurso = Entry(frame_detalhes, width= 35, justify= 'left', relief= 'solid', bg= co10, fg= co0)
    e_nomecurso.place(x= 7, y= 40)

    # Campo DURAÇÃO
    l_duracao = Label(frame_detalhes, text= 'Duração: *', height= 1, anchor= NW, font= ('Ivy 10'), bg= co8, fg= co1)
    l_duracao.place(x= 4, y= 70)
    e_duracao = Entry(frame_detalhes, width= 20, justify= 'left', relief= 'solid', bg= co10, fg= co0)
    e_duracao.place(x= 7, y= 100)

    # Campo PREÇO
    l_preco = Label(frame_detalhes, text= 'Preço: *', height= 1, anchor= NW, font= ('Ivy 10'), bg= co8, fg= co1)
    l_preco.place(x= 4, y= 130)
    e_preco = Entry(frame_detalhes, width= 10, justify= 'left', relief= 'solid', bg= co10, fg= co0)
    e_preco.place(x= 7, y= 160)
    # ----------

    # Botões da Esquerda ----------
    # Botão SALVAR
    botao_carregar = Button(frame_detalhes, command= novo_curso, anchor= CENTER, text= 'Salvar'.upper(), width= 10, overrelief= RIDGE, font=('Ivy 7 bold'), bg= co3, fg= co1)
    botao_carregar.place(x= 107, y= 160)

    # Botão ATUALIZAR
    botao_atualizar = Button(frame_detalhes, command= update_curso, anchor= CENTER, text= 'Atualizar'.upper(), width= 10, overrelief= RIDGE, font=('Ivy 7 bold'), bg= co6, fg= co1)
    botao_atualizar.place(x= 187, y= 160)

    # Botão DELETAR
    botao_deletar = Button(frame_detalhes, command= delete_curso, anchor= CENTER, text= 'Deletar'.upper(), width= 10, overrelief= RIDGE, font=('Ivy 7 bold'), bg= co7, fg= co1)
    botao_deletar.place(x= 267, y= 160)

    # ----------

    # Tabela Cursos
    def mostrar_cursos():
        app_nome = Label(frame_tabela_curso, text= 'Tabela de Cursos', height= 1, pady= 0, padx=0, relief= 'flat', anchor= NW, font= ('Ivy 10 bold'), bg= co8, fg= co1)
        app_nome.grid(row= 0, column= 0, padx= 0, pady= 10, sticky= NSEW)

        # Criando
        list_header = ['ID', 'Curso', 'Duração', 'Preço']
        
        df_list = listar_cursos()
        
        global tree_curso
        
        tree_curso = ttk.Treeview(frame_tabela_curso, selectmode= 'extended', columns= list_header, show= 'headings')

        # Vertical Scrollbar
        vsb = ttk.Scrollbar(frame_tabela_curso, orient= 'vertical', command= tree_curso.yview)

        # Horizontal Scrollbar
        hsb = ttk.Scrollbar(frame_tabela_curso, orient='horizontal', command= tree_curso.xview)
        
        tree_curso.configure(yscrollcommand= vsb.set, xscrollcommand= hsb.set)
        
        tree_curso.grid(column= 0, row= 1, sticky= 'nsew')
        vsb.grid(column= 1, row= 1, sticky= 'ns')
        hsb.grid(column= 0, row= 2, sticky= 'ew')
        frame_tabela_curso.grid_rowconfigure(0, weight= 12)
        
        hd=["nw","nw","e","e"]
        h=[30, 150, 80, 60]
        n=0
        
        for col in list_header:
            tree_curso.heading(col, text= col.title(), anchor= NW)
        
            tree_curso.column(col, width= h[n], anchor= hd[n])
        
            n+=1
        
        for item in df_list:
            tree_curso.insert('', 'end', values=item)
        
    mostrar_cursos()
    
    # Linha separatória----------
    l_linha = Label(frame_detalhes, relief= GROOVE, text= 'h', width= 1, height= 100, anchor= NW, font= ('Ivy 1'), bg= co0, fg= co0)
    l_linha.place(x= 374, y= 10)

    l_linha = Label(frame_tabela_linha, relief= GROOVE, text= 'h', width= 1, height= 139, anchor= NW, font= ('Ivy 1'), bg= co0, fg= co0)
    l_linha.place(x= 6, y= 0)
    # ----------

    # Detalhes da turma-----------------------------------------------------------

    # BOTÃO - Função Nova Turma
    def nova_turma():
        # Botão Salvar----------
        nome = e_nome_turma.get()
        curso = c_curso.get()
        data = data_inicio.get()

        lista = [nome, curso, data]
        
        # Verifica se possui valor vazio
        for i in lista:
            if i == '':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return
        
        # Inserindo os danos no banco
        inserir_turma(nome, curso, data)

        # Mostrar mensagem de sucesso
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')
        # ----------

        # Botão Deletar----------
        e_nome_turma.delete(0,END)
        c_curso.delete(0,END)
        data_inicio.delete(0,END)

        # Mostrar os valores na tabela
        mostrar_turmas()
        adicionar()


    # BOTÃO - Função Atualizar Turma----------
    def update_turma():
        e_nome_turma.delete(0, END)
        c_curso.delete(0, END)
        data_inicio.delete(0, END)

        try:
            tree_itens = tree_turma.focus()
            tree_dicionario = tree_turma.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            # Botão Atualizar - Insere os valores nas entries
            e_nome_turma.insert(0, tree_lista[1])
            c_curso.insert(0, tree_lista[2])
            data_inicio.insert(0, tree_lista[3])

            # FUNÇÃO - Atualizar
            def update():
                nome = e_nome_turma.get()
                curso = c_curso.get()
                data = data_inicio.get()

                lista = [valor_id, nome, curso, data]
                
                # Verifica se possui valor vazio
                for i in lista:
                    if i == '':
                        messagebox.showerror('Erro', 'Preencha todos os campos')
                        return
                
                # Inserindo os danos no banco
                atualizar_turma(valor_id, nome, curso, data)

                # Mostrar mensagem de sucesso
                messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')
                # ----------

                # Botão Deletar----------
                e_nome_turma.delete(0, END)
                c_curso.delete(0, END)
                data_inicio.delete(0, END)

                # Mostrar os valores na tabela
                mostrar_turmas()
                adicionar()

                # Destruir botão Salvar (Sumir depois que atualiza os dados)
                botao_salvar.destroy()

            # Botão SALVAR
            botao_salvar = Button(frame_detalhes, command= update, anchor= CENTER, text= 'Salvar Atualização'.upper(), overrelief= RIDGE, font=('Ivy 7 bold'), bg= co3, fg= co1)
            botao_salvar.place(x= 629, y= 130)

        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos cursos da tabela')
        
    # BOTÃO - Função Deletar Turma
    def delete_turma():
        try:
            tree_itens = tree_turma.focus()
            tree_dicionario = tree_turma.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            # Botão deletar
            deletar_turma([valor_id])

            # Mostrar mensagem de sucesso
            messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')

            mostrar_turmas()
            adicionar()


        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos cursos da tabela')















    l_nome = Label(frame_detalhes, text= 'Nome da Turma: *', height= 1, font= ('Ivy 10'), bg= co8, fg= co1)
    l_nome.place(x= 404, y= 10)
    e_nome_turma = Entry(frame_detalhes, width= 35, justify= 'left', relief= 'solid', bg= co10, fg= co0)
    e_nome_turma.place(x= 407, y=40)

    l_turma = Label(frame_detalhes, text= 'Curso: *', height= 1, anchor= NW, font= ('Ivy 10'), bg= co8, fg= co1)
    l_turma.place(x= 404, y= 70)

    # Combobox Cursos (substituir dados)
    cursos = listar_cursos()
    curso = []

    for i in cursos:
        curso.append(i[1])
    
    c_curso = ttk.Combobox(frame_detalhes, width= 20, font= ('Ivy 8 bold'))
    c_curso['values'] = (curso)
    c_curso.place(x= 407, y= 100)

    # data
    l_data_inicio = Label(frame_detalhes, text= 'Data de início: *', height= 1, anchor= NW, font= ('Ivy 10'), bg= co8, fg= co1)
    l_data_inicio.place(x= 406, y= 130)
    data_inicio = DateEntry(frame_detalhes, date_pattern= 'yyyy-mm-dd', width= 10, background= co5, foreground= 'white', borderwidth= 2, year= 2025)
    data_inicio.place(x= 407, y= 160)

    # Botões da Direita ----------
    # Botão SALVAR
    botao_carregar = Button(frame_detalhes, command= nova_turma, anchor= CENTER, text= 'Salvar'.upper(), width= 10, overrelief= RIDGE, font=('Ivy 7 bold'), bg= co3, fg= co1)
    botao_carregar.place(x= 507, y= 160)

    # Botão ATUALIZAR
    botao_carregar = Button(frame_detalhes, command= update_turma, anchor= CENTER, text= 'Atualizar'.upper(), width= 10, overrelief= RIDGE, font=('Ivy 7 bold'), bg= co6, fg= co1)
    botao_carregar.place(x= 587, y= 160)

    # Botão DELETAR
    botao_carregar = Button(frame_detalhes, command= delete_turma, anchor= CENTER, text= 'Deletar'.upper(), width= 10, overrelief= RIDGE, font=('Ivy 7 bold'), bg= co7, fg= co1)
    botao_carregar.place(x= 667, y= 160)

    # Tabela Turmas
    def mostrar_turmas():
        app_nome = Label(frame_tabela_turma, text= 'Tabela de Turmas', height= 1, pady= 0, padx=0, relief= 'flat', anchor= NW, font= ('Ivy 10 bold'), bg= co8, fg= co1)
        app_nome.grid(row= 0, column= 0, padx= 0, pady= 10, sticky= NSEW)

        # Criando
        list_header = ['ID', 'Nome da Turma', 'Curso', 'DT de início']
        df_list = listar_turmas()
        
        global tree_turma
        
        tree_turma = ttk.Treeview(frame_tabela_turma, selectmode= 'extended', columns= list_header, show= 'headings')

        # Vertical Scrollbar
        vsb = ttk.Scrollbar(frame_tabela_turma, orient= 'vertical', command= tree_turma.yview)

        # Horizontal Scrollbar
        hsb = ttk.Scrollbar(frame_tabela_turma, orient='horizontal', command= tree_turma.xview)
        
        tree_turma.configure(yscrollcommand= vsb.set, xscrollcommand= hsb.set)
        tree_turma.grid(column= 0, row= 1, sticky= 'nsew')
        vsb.grid(column= 1, row= 1, sticky= 'ns')
        hsb.grid(column= 0, row= 2, sticky= 'ew')
        frame_tabela_turma.grid_rowconfigure(0, weight= 12)
        
        hd=["nw","nw","e","e"]
        h=[30, 130, 150, 80]
        n=0
        
        for col in list_header:
            tree_turma.heading(col, text= col.title(), anchor= NW)
        
            tree_turma.column(col, width= h[n], anchor= hd[n])
        
            n+=1
        
        for item in df_list:
            tree_turma.insert('', 'end', values=item)
        
    mostrar_turmas()


    # ----------

    

    

# -----------------------------------------------------------








def note():
    frame_tabela_alunos = Frame(frame_tabela, width= 300, height= 100, bg= co8)
    frame_tabela_alunos.grid(row= 0, column= 0, pady= 0, padx= 10, sticky=NSEW)

    # Função para carregar nomes dos alunos
    def carregar_nomes_alunos():
        try:
            alunos = listar_alunos()
            nomes = []
            for aluno in alunos:
                nomes.append(aluno[1]) 
            return nomes
        except Exception as e:
            print(f"Erro ao carregar nomes dos alunos: {e}")
            return []

    # Função para verificar se aluno já possui notas cadastradas
    def verificar_aluno_existe_notas(nome_aluno):
        try:
            # Buscar todas as notas existentes
            notas_existentes = alunos_por_notas()
            
            # Verificar se o nome do aluno já existe na lista de notas
            for nota in notas_existentes:
                if nota[1] == nome_aluno:  
                    return True
            return False
        except Exception as e:
            print(f"Erro ao verificar se aluno existe nas notas: {e}")
            return False

    # BOTÃO - Função Inserir/Atualizar nota
    def inserir_nota():
        nome = c_nome.get()  
        nota1 = e_nota1.get()
        nota2 = e_nota2.get()

        lista = [nome, nota1, nota2]

        # Verifica campos vazios
        for i in lista:
            if i == '':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return
        
        if verificar_aluno_existe_notas(nome):
            messagebox.showwarning('Aviso', f'O aluno "{nome}" já possui notas cadastradas!\n\nPara alterar as notas, selecione o aluno na tabela e clique em "Atualizar".')
            return
        
        try:
            # Converte as notas para float
            n1 = float(nota1)
            n2 = float(nota2)
            
            # Valida se as notas estão entre 0 e 10
            if n1 < 0 or n1 > 10 or n2 < 0 or n2 > 10:
                messagebox.showerror('Erro', 'As notas devem estar entre 0 e 10')
                return
            
        except ValueError:
            messagebox.showerror('Erro', 'Digite valores numéricos válidos para as notas')
            return
        
        # Inserir no BD 
        inserir_notas(nome, nota1, nota2)

        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

        # limpar campos de entrada
        c_nome.delete(0, END)  
        e_nota1.delete(0, END)
        e_nota2.delete(0, END)

        # Apresenta os valores na tabela
        mostrar_notas()

    # Função de Atualizar Nota
    def update_nota():
        try:
            tree_itens = tree_aluno.focus()
            tree_dicionario = tree_aluno.item(tree_itens)
            tree_lista = tree_dicionario['values']

            # Limpa os campos
            c_nome.delete(0, END)  
            e_nota1.delete(0, END)
            e_nota2.delete(0, END)

            # Preenche os campos 
            valor_id = tree_lista[0]
            c_nome.insert(0, tree_lista[1])  # Nome
            e_nota1.insert(0, tree_lista[2])  # Nota 1 
            e_nota2.insert(0, tree_lista[3])  # Nota 2 
         

            # FUNÇÃO - Salvar Atualização
            def salvar_atualizacao():

                nome = c_nome.get()  # 
                nota1 = e_nota1.get()
                nota2 = e_nota2.get()
                       

                lista = [valor_id,nome, nota1, nota2]
                
                # Verifica se possui valor vazio
                for i in lista:
                    if i == '':
                        messagebox.showerror('Erro', 'Preencha todos os campos')
                        return
                
                try:
                    # Converte as notas para float para facilitar a vida
                    n1 = float(nota1)
                    n2 = float(nota2)
                    
                    # Verificando as notas
                    if n1 < 0 or n1 > 10 or n2 < 0 or n2 > 10:
                        messagebox.showerror('Erro', 'As notas devem estar entre 0 e 10')
                        return
                    
                except ValueError:
                    messagebox.showerror('Erro', 'Digite valores numéricos válidos para as notas')
                    return
                
                # Atualizar no banco
                atualizar_notas( nome,nota1, nota2)

                messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')

                c_nome.delete(0, END)  
                e_nota1.delete(0, END)
                e_nota2.delete(0, END)

                # Mostrar os valores na tabela
                mostrar_notas()

                # Destruir botão Salvar Atualização
                botao_salvar_atualizacao.destroy()

            # Botão SALVAR ATUALIZAÇÃO
            botao_salvar_atualizacao = Button(frame_detalhes, command=salvar_atualizacao, anchor=CENTER, text='Salvar Atualização'.upper(), width=15, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
            botao_salvar_atualizacao.place(x=380, y=130)

        except IndexError:
            messagebox.showerror('Erro', 'Selecione um aluno da tabela')

    # BOTÃO - Função Deletar Nota
    def delete_nota():
        try:
            tree_itens = tree_aluno.focus()
            tree_dicionario = tree_aluno.item(tree_itens)
            tree_lista = tree_dicionario['values']

            nome = tree_lista[1]  
            resposta = messagebox.askyesno('Confirmar', f'Deseja realmente deletar as notas de {nome}?')
            
            if resposta:
                deletar_notas(nome)
                messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')

                mostrar_notas()

        except IndexError:
            messagebox.showerror('Erro', 'Selecione um aluno da tabela')

    # função para pesquisa
    def procurar_aluno():
        termo_procurar = e_nome_procurar.get().strip()
        
        if termo_procurar == '':
            messagebox.showerror('Erro', 'Digite um ID ou nome para procurar')
            return
        
        # Limpar a tela
        for item in tree_aluno.get_children():
            tree_aluno.delete(item)
        
        # Buscar por ID ou Nome
        df_list = alunos_por_notas()
        encontrou = False
        
        for item in df_list:
            id_aluno = str(item[0])  # ID do aluno
            nome_aluno = item[1]     # Nome do aluno
            
            # Verifica se o termo procurado corresponde ao ID ou está contido no nome
            if (termo_procurar.isdigit() and termo_procurar == id_aluno) or \
            (termo_procurar.lower() in nome_aluno.lower()):
                
                # Calcular média e situação para exibição
                nota1 = float(item[2]) if item[2] else 0
                nota2 = float(item[3]) if item[3] else 0
                media = (nota1 + nota2) / 2
                situacao = "Aprovado" if media >= 6 else "Reprovado"
                
                # Definir as tags de cor baseado na situação
                tags = ('aprovado',) if situacao == "Aprovado" else ('reprovado',)
                
                # Inserir na árvore com todos os dados E as tags de cor
                tree_aluno.insert('', 'end', 
                                values=[id_aluno, nome_aluno, f"{nota1:.1f}", f"{nota2:.1f}", f"{media:.1f}", situacao],
                                tags=tags)
                encontrou = True
        #atualizar
        if not encontrou:
            messagebox.showinfo('Não encontrado', f'Nenhum aluno encontrado com ID ou nome "{termo_procurar}"')
            mostrar_notas()  # Volta 

    # Função para atualizar a lista de nomes na combobox
    def atualizar_lista_nomes():
        nomes_alunos = carregar_nomes_alunos()
        c_nome['values'] = nomes_alunos

    # Campos de entrada
    l_nome = Label(frame_detalhes, text='Nome do Aluno: *', height=1, anchor=NW, font=('Ivy 10'), bg=co8, fg=co1)
    l_nome.place(x=4, y=10)
    
    # MUDANÇA PRINCIPAL: Substituindo Entry por Combobox
    c_nome = ttk.Combobox(frame_detalhes, width=42, font=('Ivy 9'))
    c_nome.place(x=7, y=40)
    
    # Carregar nomes dos alunos na combobox
    atualizar_lista_nomes()

    l_nota1 = Label(frame_detalhes, text='Nota 1 (0-10): *', height=1, anchor=NW, font=('Ivy 10'), bg=co8, fg=co1)
    l_nota1.place(x=4, y=70)
    e_nota1 = Entry(frame_detalhes, width=20, justify='left', relief='solid', bg=co10, fg=co0)
    e_nota1.place(x=7, y=100)

    l_nota2 = Label(frame_detalhes, text='Nota 2 (0-10): *', height=1, anchor=NW, font=('Ivy 10'), bg=co8, fg=co1)
    l_nota2.place(x=4, y=130)
    e_nota2 = Entry(frame_detalhes, width=20, justify='left', relief='solid', bg=co10, fg=co0)
    e_nota2.place(x=7, y=160)

    # Linha separatória
    l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
    l_linha.place(x=520, y=10)

    # Procurar aluno----------
    # ATUALIZADO: Agora permite busca por ID ou nome
    l_nome_procurar = Label(frame_detalhes, text='Procurar Aluno [Digite o ID ou nome]', height=1, anchor=NW, font=('Ivy 10'), bg=co8, fg=co1)
    l_nome_procurar.place(x=540, y=10)
    e_nome_procurar = Entry(frame_detalhes, width=29, justify='center', relief='solid', font=('Ivy 10'), bg=co10, fg=co0)
    e_nome_procurar.place(x=543, y=35)

    botao_procurar = Button(frame_detalhes, command=procurar_aluno, anchor=CENTER, text='Procurar', width=9, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co8, fg=co1)
    botao_procurar.place(x=760, y=35.5)
    # ----------

    # Botão Salvar
    botao_salvar = Button(frame_detalhes, command=inserir_nota, anchor=CENTER, text='Salvar'.upper(), width=9, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
    botao_salvar.place(x=544, y=110)

    # Botão Atualizar
    botao_atualizar = Button(frame_detalhes, command=update_nota, anchor=CENTER, text='Atualizar'.upper(), width=9, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co6, fg=co1)
    botao_atualizar.place(x=544, y=135)

    # Botão Deletar
    botao_deletar = Button(frame_detalhes, command=delete_nota, anchor=CENTER, text='Deletar'.upper(), width=9, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1)
    botao_deletar.place(x=544, y=160)

    # Botão Ver Todos
    botao_ver = Button(frame_detalhes, command=lambda: mostrar_notas(), anchor=CENTER, text='Ver Todos'.upper(), width=9, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co8, fg=co1)
    botao_ver.place(x=760, y=160)

   

    # Tabela Notas 
    def mostrar_notas():
        # Limpar tabela existente
        for widget in frame_tabela.winfo_children():
            widget.destroy()
            
        app_nome = Label(frame_tabela, text='Tabela de Notas', height=1, pady=0, padx=0, relief='flat', anchor=NW, font=('Ivy 10 bold'), bg=co8, fg=co1)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        # Criando header com ID incluído
        list_header = ['ID', 'Nome', 'Nota 1', 'Nota 2', 'Média', 'Situação']
        
        # Buscar no BD
        df_list = alunos_por_notas()
        
        # Processar dados para calcular média e situação
        processed_list = []
        for item in df_list:
            id_aluno = item[0]     # ID do aluno
            nome = item[1]         # Nome do aluno
            nota1 = float(item[2]) if item[2] else 0
            nota2 = float(item[3]) if item[3] else 0
            media = (nota1 + nota2) / 2
            situacao = "Aprovado" if media >= 6 else "Reprovado"
            
            processed_list.append([id_aluno, nome, f"{nota1:.1f}", f"{nota2:.1f}", f"{media:.1f}", situacao])
        
        global tree_aluno
        
        tree_aluno = ttk.Treeview(frame_tabela, selectmode='extended', columns=list_header, show='headings')

        # Vertical Scrollbar
        vsb = ttk.Scrollbar(frame_tabela, orient='vertical', command=tree_aluno.yview)

        # Horizontal Scrollbar
        hsb = ttk.Scrollbar(frame_tabela, orient='horizontal', command=tree_aluno.xview)
        
        tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        
        tree_aluno.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tabela.grid_rowconfigure(0, weight=12)
        
        # Configurações das colunas 
        hd = ["center", "nw", "center", "center", "center", "center"]
        h = [50, 150, 80, 80, 80, 100]  
        n = 0
        
        for col in list_header:
            tree_aluno.heading(col, text=col.title(), anchor=NW)
            tree_aluno.column(col, width=h[n], anchor=hd[n])
            n += 1
        
        # Inserir dados processados
        for item in processed_list:
            # Colorir linha baseado na situação
            tags = ('aprovado',) if item[5] == "Aprovado" else ('reprovado',)  # Situação agora está na posição 5
            tree_aluno.insert('', 'end', values=item, tags=tags)
        
        # Configurar cores das tags(deixa as cores pra facilitar a visualização)
        tree_aluno.tag_configure('aprovado', background='#d4edda', foreground='#155724')
        tree_aluno.tag_configure('reprovado', background='#f8d7da', foreground='#721c24')
        
    mostrar_notas()

# Função de controle--------------------------------------------------------------
def control(i):
    # cadastro de aluno
    if i == 'cadastro':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        
        # Chamando a função adicionar
        alunos()

    if i == 'adicionar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        
        # Chamando a função alunos
        adicionar()

    if i == 'note':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        
        # Chamando a função salvar
        note()

# --------------------------------------------------------------






# Loop da janela
alunos()
janela.mainloop()