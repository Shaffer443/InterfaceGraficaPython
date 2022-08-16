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

#definindo valores e blocos

fundo = "#fff"
cor_fonte = "#000"

subjanela=Label(janela,text="Container 1", bg=fundo, fg=cor_fonte)
subjanela.pack(ipadx=20, ipady=20, padx=5, pady=150, side="left", fill=Y, expand=True, anchor=W)

#entradas

casa=Label(janela, text="Time Casa", bg="#008", foreground="#fff").place(x=300,y=150, width=100, height=25)
casanome=Entry(janela)
casanome.place(x=200,y=180, width=300, height=25)

vistante=Label(janela, text="Time Visitante", bg="#008", foreground="#fff").place(x=700,y=150, width=100, height=25)
visitantenome=Entry(janela)
visitantenome.place(x=600,y=180, width=300, height=25)

entradas=Label(janela, text="Entradas", bg="#008", foreground="#fff", anchor=W).place(x=200,y=230, width=100, height=25)

primeira=Entry(janela)
primeira.place(x=200,y=250, width=600, height=25)
segunda=Entry(janela)
segunda.place(x=200,y=278, width=600, height=25)
terceira=Entry(janela)
terceira.place(x=200,y=306, width=600, height=25)

janela.mainloop() #executa o programa