# Importando dependências do Tkinter
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

# Importando pillow
from PIL import ImageTk, Image

# tk calendar
from tkcalendar import Calendar, DateEntry
from datetime import date

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
co7 = '#ef5350' # Vermelho

co6 = '#038cfc' # Azul
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
app_lg = Image.open('img-estudante-96.png')
app_lg = app_lg.resize((50, 50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image= app_lg, text= 'Cadastro de Alunos', width= 850, compound= LEFT, relief= RAISED, anchor= NW, font= ('Ivy 15 bold'), bg= co5, fg= co1)
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
app_salvar = Button(frame_dados, command= lambda:control('salvar'), image= app_img_salvar, text= ' Salvar', width= 100, compound= LEFT, overrelief= RIDGE, font= ('Ivy 11'), bg= co8, fg= co1)
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
    c_sexo['values'] = ('Masculino', 'Feminino')
    c_sexo.place(x= 188, y= 160)

    l_data_nascimento = Label(frame_detalhes, text= 'Data de nascimento: *', height= 1, anchor= NW, font= ('Ivy 10'), bg= co8, fg= co1)
    l_data_nascimento.place(x= 366, y= 10)
    data_nascimento = DateEntry(frame_detalhes, width= 18, background= co5, foreground= 'white', borderwidth= 2, year= 2025)
    data_nascimento.place(x= 370, y= 40)

    l_cpf = Label(frame_detalhes, text= 'CPF: *', height= 1, anchor= NW, font= ('Ivy 10'), bg= co8, fg= co1)
    l_cpf.place(x= 365, y= 70)
    e_cpf = Entry(frame_detalhes, width= 20, justify= 'left', relief= 'solid', bg= co10, fg= co0)
    e_cpf.place(x= 369, y= 100)

    # Pegando os cursos (substituir dados)
    turmas = ['curso 1', 'curso 2', 'curso 3']
    turma = []

    for i in turmas:
        turma.append(i)

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
    

    botao_procurar = Button(frame_detalhes, anchor= CENTER, text= 'Procurar', width= 9, overrelief= RIDGE, font= ('Ivy 7 bold'), bg= co8, fg= co1)
    botao_procurar.place(x= 760, y= 35.5)
    # ----------

    # Botão Salvar
    botao_salvar = Button(frame_detalhes, anchor= CENTER, text= 'Salvar'.upper(), width= 9, overrelief= RIDGE, font= ('Ivy 7 bold'), bg= co3, fg= co1)
    botao_salvar.place(x= 544, y= 110)

    # Botão Atualizar
    botao_atualizar = Button(frame_detalhes, anchor= CENTER, text= 'Atualizar'.upper(), width= 9, overrelief= RIDGE, font= ('Ivy 7 bold'), bg= co6, fg= co1)
    botao_atualizar.place(x= 544, y= 135)

    # Botão Deletar
    botao_deletar = Button(frame_detalhes, anchor= CENTER, text= 'Deletar'.upper(), width= 9, overrelief= RIDGE, font= ('Ivy 7 bold'), bg= co7, fg= co1)
    botao_deletar.place(x= 544, y= 160)

    # Botão Ver
    botao_ver = Button(frame_detalhes, anchor= CENTER, text= 'Ver'.upper(), width= 9, overrelief= RIDGE, font= ('Ivy 7 bold'), bg= co8, fg= co1)
    botao_ver.place(x= 760, y= 160)

    # Tabela Alunos
    def mostrar_alunos():
        app_nome = Label(frame_tabela, text= 'Tabela de Alunos', height= 1, pady= 0, padx=0, relief= 'flat', anchor= NW, font= ('Ivy 10 bold'), bg= co8, fg= co1)
        app_nome.grid(row= 0, column= 0, padx= 0, pady= 10, sticky= NSEW)

        # Criando
        list_header = ['ID', 'Nome', 'E-mail', 'Telefone', 'sexo', 'Imagem', 'Data', 'CPF', 'Curso']
        
        df_list = []
        
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
        
        hd=["nw", "nw", "nw", "center", "center", "center", "center", "center", "center"]
        h=[40, 150, 150, 70, 70, 70, 80, 80, 100]
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

    # Função novo curso
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
    botao_atualizar = Button(frame_detalhes, anchor= CENTER, text= 'Atualizar'.upper(), width= 10, overrelief= RIDGE, font=('Ivy 7 bold'), bg= co6, fg= co1)
    botao_atualizar.place(x= 187, y= 160)

    # Botão DELETAR
    botao_deletar = Button(frame_detalhes, anchor= CENTER, text= 'Deletar'.upper(), width= 10, overrelief= RIDGE, font=('Ivy 7 bold'), bg= co7, fg= co1)
    botao_deletar.place(x= 267, y= 160)

    # ----------

    # Tabela Cursos
    def mostrar_cursos():
        app_nome = Label(frame_tabela_curso, text= 'Tabela de Cursos', height= 1, pady= 0, padx=0, relief= 'flat', anchor= NW, font= ('Ivy 10 bold'), bg= co8, fg= co1)
        app_nome.grid(row= 0, column= 0, padx= 0, pady= 10, sticky= NSEW)

        # Criando
        list_header = ['ID', 'Curso', 'Duração', 'Preço']
        
        df_list = []
        
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

    # Detalhes da turma---------
    l_nome = Label(frame_detalhes, text= 'Nome da Turma: *', height= 1, font= ('Ivy 10'), bg= co8, fg= co1)
    l_nome.place(x= 404, y= 10)
    e_nome_turma = Entry(frame_detalhes, width= 35, justify= 'left', relief= 'solid', bg= co10, fg= co0)
    e_nome_turma.place(x= 407, y=40)

    l_turma = Label(frame_detalhes, text= 'Curso: *', height= 1, anchor= NW, font= ('Ivy 10'), bg= co8, fg= co1)
    l_turma.place(x= 404, y= 70)

    # Combobox Cursos (substituir dados)
    cursos = ['curso 1', 'curso 2', 'curso 3']
    curso = []

    for i in cursos:
        curso.append(i)
    
    c_curso = ttk.Combobox(frame_detalhes, width= 20, font= ('Ivy 8 bold'))
    c_curso['values'] = (curso)
    c_curso.place(x= 407, y= 100)

    # data
    l_data_inicio = Label(frame_detalhes, text= 'Data de início: *', height= 1, anchor= NW, font= ('Ivy 10'), bg= co8, fg= co1)
    l_data_inicio.place(x= 406, y= 130)
    data_inicio = DateEntry(frame_detalhes, width= 10, background= co5, foreground= 'white', borderwidth= 2, year= 2025)
    data_inicio.place(x= 407, y= 160)

    # Botões da Direita ----------
    # Botão SALVAR
    botao_carregar = Button(frame_detalhes, anchor= CENTER, text= 'Salvar'.upper(), width= 10, overrelief= RIDGE, font=('Ivy 7 bold'), bg= co3, fg= co1)
    botao_carregar.place(x= 507, y= 160)

    # Botão ATUALIZAR
    botao_carregar = Button(frame_detalhes, anchor= CENTER, text= 'Atualizar'.upper(), width= 10, overrelief= RIDGE, font=('Ivy 7 bold'), bg= co6, fg= co1)
    botao_carregar.place(x= 587, y= 160)

    # Botão DELETAR
    botao_carregar = Button(frame_detalhes, anchor= CENTER, text= 'Deletar'.upper(), width= 10, overrelief= RIDGE, font=('Ivy 7 bold'), bg= co7, fg= co1)
    botao_carregar.place(x= 667, y= 160)

    # Tabela Turmas
    def mostrar_turmas():
        app_nome = Label(frame_tabela_turma, text= 'Tabela de Turmas', height= 1, pady= 0, padx=0, relief= 'flat', anchor= NW, font= ('Ivy 10 bold'), bg= co8, fg= co1)
        app_nome.grid(row= 0, column= 0, padx= 0, pady= 10, sticky= NSEW)

        # Criando
        list_header = ['ID', 'Nome da Turma', 'Curso', 'DT de início']
        
        df_list = []
        
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

    

    

# -----------------------------------------

# Função para salvar--------------------------------------------------------------
def salvar():
    print('Salvar')
# --------------------------------------------------------------



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

    if i == 'salvar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        
        # Chamando a função salvar
        salvar()

# --------------------------------------------------------------














































# Loop da janela
alunos()
janela.mainloop()