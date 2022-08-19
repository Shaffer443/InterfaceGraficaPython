from tkinter import *
import datetime
from datetime import date

today = date.today()

janela=Tk()

def infoDataHora():
    dt = datetime.datetime.now()
    go = dt.strftime("%A %d. %B %Y - %I:%M")
    return go

def impDados():
    print("%s"%casanome.get() + " x "+ "%s\n"%visitantenome.get())
    print(f"Operação 1: %s"%primeira.get())
    print(f"Operação 2: %s"%segunda.get())
    print(f"Operação 3: %s"%terceira.get())


def salvar():
    arquivo=open(f"{today}.txt","a+")
    #arquivo.write(f"{today}\n\n")
    arquivo.write("%s"%casanome.get() + " x "+ "%s\n"%visitantenome.get())
    arquivo.write("Operação 1: %s\n"%primeira.get())
    arquivo.write("Operação 2: %s\n"%segunda.get())
    arquivo.write("Operação 3: %s\n"%terceira.get())
    arquivo.write("\n\n")
    arquivo.close()



#configurações de ambiente:

janela.title("Shaffer Programas") # titulo na janela do programa
janela.geometry("1080x720") #tamanho da janela
janela.configure(background="#008") # cor de fundo em RGB


#rodapé:

autor=Label(janela,text="Criado por:Rafael Gouveia - https://linktr.ee/rafaelgouveia",background="#008",foreground="#fff")
autor.place(x=300, y=690, width=500, height=30)

#conteudo:

nome=Label(janela,text="Primeira Interface Gráfica com Python",background="#fff",)
nome.place(x=10, y=10, width=270, height=30)

nome=Label(janela,text="Versão beta",background="#000", foreground="#fff")
nome.place(x=960, y=10, width=100, height=30)

info=Label(janela,text= f"{infoDataHora()}",background="#000", foreground="#fff")
info.place(x=450, y=10, width=300, height=30)

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

#Botão

btn=Button(janela,text="Imprimir", command=impDados)
btn.place(x=400, y=350, width=80, height=25)

save=Button(janela,text="Salvar", command=salvar)
save.place(x=500, y=350, width=80, height=25)

janela.mainloop()