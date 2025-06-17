from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess
import sys

from PIL import ImageTk, Image

co0 = '#2e2d2b' 
co1 = '#feffff' 
co2 = '#e5e5e5'
co3 = '#00a095' 
co4 = '#403d3d'  
co5 = '#003480' 
co6 = '#038cfc' 
co7 = '#ef5350' 
co8 = '#263238'  
co9 = '#e9edf5' 
co10 = '#a1a1a1' 
co11 = '#d3af37'

class LoginApp:
    def __init__(self):
        self.janela = Tk()
        self.setup_window()
        self.create_widgets()
        
    def setup_window(self):
        """Configuração inicial da janela"""
        self.janela.title('Login - Colégio Golden Ball')
        self.janela.geometry('450x400')  # Aumentada altura para 400px
        self.janela.configure(background=co8)
        self.janela.resizable(width=FALSE, height=FALSE)
        
        # Centralizar janela na tela
        self.janela.eval('tk::PlaceWindow . center')
        
        # Estilo da janela
        style = Style(self.janela)
        style.theme_use('clam')
    
    def create_widgets(self):
        """Criação dos widgets da interface"""
        
        # Frame principal
        frame_principal = Frame(self.janela, width=450, height=400, bg=co8)
        frame_principal.pack(fill=BOTH, expand=TRUE)
        
        # Frame do logo/header
        frame_logo = Frame(frame_principal, width=450, height=80, bg=co5)
        frame_logo.pack(fill=X, pady=0)
        frame_logo.pack_propagate(False)
        
        # Logo e título
        try:
            app_lg1 = Image.open('img-estudante-96.png')
            app_lg2 = app_lg1.resize((60, 60))
            app_lg3 = ImageTk.PhotoImage(app_lg2)
            app_logo = Label(frame_logo, image=app_lg3, text='  Sistema de Login', 
                           width=450, compound=LEFT, relief=RAISED, anchor=W, 
                           font=('Ivy 16 bold'), bg=co5, fg=co1, padx=20)
            app_logo.pack(fill=BOTH, expand=TRUE)
            #Imagem do app
            app_logo.image = app_lg3
        except:
            # Caso a imagem não seja encontrada
            app_logo = Label(frame_logo, text='Sistema de Login', 
                           width=450, relief=RAISED, anchor=CENTER, 
                           font=('Ivy 16 bold'), bg=co5, fg=co1)
            app_logo.pack(fill=BOTH, expand=TRUE)
        
        # Linha divisória
        ttk.Separator(frame_principal, orient=HORIZONTAL).pack(fill=X, pady=0)
        
        frame_form = Frame(frame_principal, bg=co8)
        frame_form.pack(expand=TRUE, fill=BOTH, padx=40, pady=20)
        
        # Título 
        titulo = Label(frame_form, text='Acesso ao Sistema', 
                      font=('Ivy 14 bold'), bg=co8, fg=co1)
        titulo.pack(pady=(0, 20))
        
        frame_campos = Frame(frame_form, bg=co8)
        frame_campos.pack(expand=TRUE, fill=BOTH)
        
        # Campo Usuário
        label_usuario = Label(frame_campos, text='Usuário:', 
                            font=('Ivy 11'), bg=co8, fg=co1, anchor=W)
        label_usuario.pack(fill=X, pady=(0, 5))
        
        self.entry_usuario = Entry(frame_campos, font=('Ivy 11'), 
                                 relief='solid', bg=co10, fg=co0, 
                                 borderwidth=2, justify='center', width=30)
        self.entry_usuario.pack(pady=(0, 15), ipady=6)
        
        # Campo Senha
        label_senha = Label(frame_campos, text='Senha:', 
                          font=('Ivy 11'), bg=co8, fg=co1, anchor=W)
        label_senha.pack(fill=X, pady=(0, 5))
        
        self.entry_senha = Entry(frame_campos, font=('Ivy 11'), 
                               relief='solid', bg=co10, fg=co0, 
                               borderwidth=2, show='*', justify='center', width=30)
        self.entry_senha.pack(pady=(0, 25), ipady=6)
        
        # Frame dos botões
        frame_botoes = Frame(frame_campos, bg=co8)
        frame_botoes.pack(pady=10)
        
        # Botão Login
        btn_login = Button(frame_botoes, text='ENTRAR', command=self.fazer_login,
                         font=('Ivy 11 bold'), bg=co3, fg=co1, 
                         relief='raised', borderwidth=2, cursor='hand2')
        btn_login.pack(side=LEFT, padx=(0, 10), ipadx=15, ipady=6)
        
        # Botão Cancelar
        btn_cancelar = Button(frame_botoes, text='CANCELAR', command=self.cancelar,
                            font=('Ivy 11 bold'), bg=co7, fg=co1, 
                            relief='raised', borderwidth=2, cursor='hand2')
        btn_cancelar.pack(side=LEFT, ipadx=15, ipady=6)
    
        self.janela.bind('<Return>', lambda event: self.fazer_login())
        
        # Focar no campo usuário
        self.entry_usuario.focus()
    
    def fazer_login(self):
        """Função para validar o login"""
        usuario = self.entry_usuario.get().strip()
        senha = self.entry_senha.get().strip()
        
        # Verificar se os campos estão preenchidos
        if not usuario or not senha:
            messagebox.showerror('Erro', 'Por favor, preencha todos os campos!')
            return
        
        # user e senha
        usuarios_validos = {
            'goldenball': '123',

        }
        
        if usuario in usuarios_validos and usuarios_validos[usuario] == senha:
            # Login bem-sucedido
            messagebox.showinfo('Sucesso', f'Bem-vindo, {usuario}!')
            self.abrir_sistema_principal()
        else:
            # Login falhou
            messagebox.showerror('Erro', 'Usuário ou senha incorretos!')
            self.entry_senha.delete(0, END)
            self.entry_usuario.focus()
    
    def abrir_sistema_principal(self):
       
        try:
            # Fechar janela de login
            self.janela.destroy()
            
            # Abrindo a tela principal
            subprocess.run([sys.executable, 'main.py'])
            
        except Exception as e:
            messagebox.showerror('Erro', f'Erro ao abrir o sistema principal: {str(e)}')
    
    def cancelar(self):
        """Função para cancelar e fechar a aplicação"""
        resposta = messagebox.askyesno('Confirmação', 'Deseja realmente sair?')
        if resposta:
            self.janela.quit()
    
    def executar(self):
        self.janela.mainloop()

# Função principal
def main():
    app = LoginApp()
    app.executar()

if __name__ == '__main__':
    main()