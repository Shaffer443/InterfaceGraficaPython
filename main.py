from tkinter import *

janela=Tk()

#configurações de ambiente:

janela.title("Shaffer Programas") # titulo na janela do programa
janela.geometry("1080x720") #tamanho da janela
janela.configure(background="#008") # cor de fundo em RGB

#conteudo:

nome=Label(janela,text="Primeira Interface Gráfica com Python",background="#fff",)
nome.place(x=10, y=10, width=270, height=30)

nome=Label(janela,text="Versão beta",background="#000", foreground="#fff")
nome.place(x=960, y=10, width=100, height=30)

#finindo valores

fundo = "#fff"
cor_fonte = "#000"

subjanela=Label(janela,text="Container 1", bg=fundo, fg=cor_fonte)
subjanela.pack(ipadx=20, ipady=20, padx=150, pady=150, side="left", fill=Y, expand=True)


janela.mainloop() #executa o programa