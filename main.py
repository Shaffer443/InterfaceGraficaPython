from tkinter import *
import datetime
from datetime import date
import os
import os.path
import funcao




today = date.today()
os.chdir("Entradas")

janela=Tk()

def infoDataHora():
    dt = datetime.datetime.now()
    go = dt.strftime("%A %d. %B %Y - %H:%M")
    return go

def criarPasta():
    if os.path.exists(f"{today}"):
        #print("\n\nDiretórios já existente. Não foi criado")

        return salvar()
    else:
        os.mkdir(f"{today}")
        salvar()

def limpar():
    emBranco = ''
    print("%s"%emBranco + " x "+ "%s\n"%emBranco.get())
    #print(f"Operação 1: %s"%primeira.get())
    #print(f"Operação 2: %s"%segunda.get())
    #print(f"Operação 3: %s"%terceira.get())

def fechandoTela(janela, tempo):
        janela.after(tempo * 1000, lambda: janela.destroy())

def salvar():

        if os.path.exists(f"{today}"):
            try:
                os.chdir(f"{today}")
                # arquivo=open(f"{today}.txt","a+")
                arquivo = open("%s"%casanome.get()+"x"+"%s"%visitantenome.get()+".txt", "a+") #implementação
                #arquivo.write(f"{today}\n\n")
                arquivo.write("\nData: %s\n" %today)
                arquivo.write(f"Torneio: %s\n" %torneio.get())
                arquivo.write("%s"%casanome.get() + " x " + "%s\n"%visitantenome.get()) #pode ser desnecessário
                arquivo.write("Operação: %s\n"%mercado.get())
                arquivo.write("Odds de Entrada: %s\n"%oddsEntrada.get())
                arquivo.write("Minuto da Entrada: %s\n"%minEntrada.get())
                arquivo.write("Odds de Saída: %s\n" %oddsSaida.get())
                arquivo.write("Minuto de Saída: %s\n" %minSaida.get())
                arquivo.write("Gols Mandante 1 tempo: %s\n" %golsMandante.get())
                arquivo.write("Gols Visitante 1 tempo: %s\n" % golsVisitante.get())
                arquivo.write("Gols Mandante 2 tempo: %s\n" % golsMandanteSegundo.get())
                arquivo.write("Gols Visitante 2 tempo: %s\n" % golsVisitanteSegundo.get())
                arquivo.write("Valor da Operação (R$ ou $): %s\n" % valorEntrada.get())
                arquivo.write("Retorno da Operação (R$ ou $): %s\n" % resultadoOperacao.get())
                arquivo.write("\n\n")
                #arquivo.write(f'insert into input values(default,\'{today}\',\'{torneio.get()}\',{casanome.get()},{visitantenome.get()},{mercado.get()},{oddsEntrada.get()},{minEntrada.get()},{oddsSaida.get()},{minSaida.get()},{golsMandante.get()},{golsVisitante.get()},{golsMandanteSegundo.get()},{golsVisitanteSegundo.get()},{valorEntrada.get()},{funcao.scriptInputJogoRedGreen(resultadoOperacao.get())},{resultadoOperacao.get()},default);\n\n')
                arquivo.write("%s\n\n"%funcao.criacaoScriptMysql(torneio.get(), casanome.get(), visitantenome.get(), mercado.get(), oddsEntrada.get(), minEntrada.get(),oddsSaida.get(), minSaida.get(), golsMandante.get(), golsVisitante.get(), golsMandanteSegundo.get(), golsVisitanteSegundo.get(),valorEntrada.get(), resultadoOperacao.get()))
                arquivo.close()

                # info na janela
                res = Label(janela, text="Salvo Com Sucesso!", bg="#008", foreground="#00FF00", anchor=W).place(x=450, y=620, width=150,height=25)
                contagemDeTempo = Label(janela, text="Fechando Janela em 5 segundos", bg="#008", foreground="#00FF00",
                                        anchor=W).place(x=600, y=620, width=150, height=25)
                return res, contagemDeTempo, fechandoTela(janela,5)


            except:
                # info na janela
                erro = Label(janela, text="Erros no Salvamento", bg="#008", foreground="#FF0000", anchor=W).place(x=500, y=620, width=150,height=25)
                return erro

        else:
            try:
                os.mkdir(f"{today}")
                os.chdir(f"{today}")
                #arquivo = open(f"{today}.txt", "a+")
                #arquivo = open(f"{casanome.get()}x{visitantenome.get()}.txt", "a+")  # implementação
                arquivo = open("%s" % casanome.get() + "x" + "%s" % visitantenome.get() + ".txt", "a+")  # implementação
                # arquivo.write(f"{today}\n\n")
                arquivo.write("\nData: %s\n" % today)
                arquivo.write(f"Torneio: %s\n" % torneio.get())
                arquivo.write("%s" % casanome.get() + " x " + "%s\n" % visitantenome.get())
                arquivo.write("Operação: %s\n" % mercado.get())
                arquivo.write("Odds de Entrada: %s\n" % oddsEntrada.get())
                arquivo.write("Minuto da Entrada: %s\n" % minEntrada.get())
                arquivo.write("Odds de Saída: %s\n" % oddsSaida.get())
                arquivo.write("Minuto de Saída: %s\n" % minSaida.get())
                arquivo.write("Gols Mandante 1 tempo: %s\n" % golsMandante.get())
                arquivo.write("Gols Visitante 1 tempo: %s\n" % golsVisitante.get())
                arquivo.write("Gols Mandante 2 tempo: %s\n" % golsMandanteSegundo.get())
                arquivo.write("Gols Visitante 2 tempo: %s\n" % golsVisitanteSegundo.get())
                arquivo.write("Valor da Operação (R$ ou $): %s\n" % valorEntrada.get())
                arquivo.write("Retorno da Operação (R$ ou $): %s\n" % resultadoOperacao.get())
                arquivo.write("\n\n")
                #arquivo.write(f"insert into input values(default,{today},{torneio.get()},{casanome.get()},{visitantenome.get()},{mercado.get()},{oddsEntrada.get()},{minEntrada.get()},{oddsSaida.get()},{minSaida.get()},{golsMandante.get()},{golsVisitante.get()},{golsMandanteSegundo.get()},{golsVisitanteSegundo.get()},{valorEntrada.get()},{funcao.scriptInputJogoRedGreen(resultadoOperacao.get())},{resultadoOperacao.get()},default);\n\n")
                arquivo.write("%s\n\n" %funcao.criacaoScriptMysql(torneio.get(), casanome.get(), visitantenome.get(), mercado.get(), oddsEntrada.get(), minEntrada.get(),oddsSaida.get(), minSaida.get(), golsMandante.get(), golsVisitante.get(), golsMandanteSegundo.get(), golsVisitanteSegundo.get(),valorEntrada.get(), resultadoOperacao.get()))

                arquivo.close()

                # info na janela
                res = Label(janela, text="Salvo Com Sucesso!", bg="#008", foreground="#00FF00", anchor=W).place(x=450, y=620,width=150,height=25)
                contagemDeTempo = Label(janela, text="Fechando Janela em 5 segundos", bg="#008", foreground="#00FF00", anchor=W).place(x=600,y=620,width=150,height=25)
                return res, contagemDeTempo, fechandoTela(janela,5)


            except:
                # info na janela
                erro = Label(janela, text="Erros no Salvamento", bg="#008", foreground="#FF0000", anchor=W).place(x=500, y=620,width=150,height=25)
                return erro


#configurações de ambiente:

janela.title("Shaffer Programas") # titulo na janela do programa
janela.geometry("1080x720") #tamanho da janela
janela.configure(background="#008") # cor de fundo em RGB


#rodapé:

autor=Label(janela,text="Criado por: Rafael Gouveia - https://linktr.ee/rafaelgouveia",background="#008",foreground="#fff")
autor.place(x=250, y=690, width=500, height=30)

ultimaAtualizacao=Label(janela,text=f"Última Atualização: 2023-05-20",background="#006",foreground="#fff")
ultimaAtualizacao.place(x=800, y=690, width=250, height=30)

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

torneioNome=Label(janela, text="Torneio", bg="#008", foreground="#fff").place(x=500,y=80, width=100, height=25)
torneio=Entry(janela)
torneio.place(x=400,y=110, width=300, height=25)

casa=Label(janela, text="Time Mandante (Casa)", bg="#008", foreground="#fff").place(x=260,y=150, width=200, height=25)
casanome=Entry(janela)
casanome.place(x=200,y=180, width=300, height=25)

vistante=Label(janela, text="Time Visitante", bg="#008", foreground="#fff").place(x=700,y=150, width=100, height=25)
visitantenome=Entry(janela)
visitantenome.place(x=600,y=180, width=300, height=25)


#Input Dados


mercadoNome=Label(janela, text="Mercado Alvo", bg="#008", foreground="#fff", anchor=W).place(x=500,y=220, width=100, height=25)
mercado=Entry(janela)
mercado.place(x=400,y=250, width=300, height=25)



oddsEntradaNome=Label(janela, text="Odds de Entrada", bg="#008", foreground="#fff", anchor=W).place(x=200,y=320, width=150, height=25)
oddsEntrada=Entry(janela)
oddsEntrada.place(x=330,y=320, width=100, height=25)

minEntradaNome=Label(janela, text="Minuto de Entrada", bg="#008", foreground="#fff", anchor=W).place(x=200,y=370, width=150, height=25)
minEntrada=Entry(janela)
minEntrada.place(x=330,y=370, width=100, height=25)



oddsSaidaNome=Label(janela, text="Odds de Saída", bg="#008", foreground="#fff", anchor=W).place(x=680,y=320, width=150, height=25)
oddsSaida=Entry(janela)
oddsSaida.place(x=800,y=320, width=100, height=25)

minSaidaNome=Label(janela, text="Minuto de Saída", bg="#008", foreground="#fff", anchor=W).place(x=680,y=370, width=150, height=25)
minSaida=Entry(janela)
minSaida.place(x=800,y=370, width=100, height=25)


gols=Label(janela, text="Gols", bg="#008", foreground="#fff", anchor=W).place(x=525,y=420, width=150, height=25)

primeiro=Label(janela, text="Primeiro Tempo", bg="#008", foreground="#fff", anchor=W).place(x=300,y=450, width=150, height=25)

segundo=Label(janela, text="Segundo Tempo", bg="#008", foreground="#fff", anchor=W).place(x=700,y=450, width=150, height=25)


golsMandantenome=Label(janela, text="Gols Mandante 1 Tempo", bg="#008", foreground="#fff", anchor=W).place(x=200,y=500, width=150, height=25)
golsMandante=Entry(janela)
golsMandante.place(x=380,y=500, width=80, height=25)

golsVisitantenome=Label(janela, text="Gols Visitante 1 Tempo", bg="#008", foreground="#fff", anchor=W).place(x=200,y=530, width=160, height=25)
golsVisitante=Entry(janela)
golsVisitante.place(x=380,y=530, width=80, height=25)



golsMandantenomeSegundo=Label(janela, text="Gols Mandante 2 Tempo", bg="#008", foreground="#fff", anchor=W).place(x=640,y=500, width=150, height=25)
golsMandanteSegundo=Entry(janela)
golsMandanteSegundo.place(x=820,y=500, width=80, height=25)


golsVisitantenomeSegundo=Label(janela, text="Gols Visitante 2 Tempo", bg="#008", foreground="#fff", anchor=W).place(x=640,y=530, width=160, height=25)
golsVisitanteSegundo=Entry(janela)
golsVisitanteSegundo.place(x=820,y=530, width=80, height=25)


ResultadoNome=Label(janela, text="Resultados", bg="#008", foreground="#fff", anchor=W).place(x=525,y=560, width=100, height=25)


valorEntradaNome=Label(janela, text="Valor da Entrada ($)", bg="#008", foreground="#fff", anchor=W).place(x=200,y=580, width=150, height=25)
valorEntrada=Entry(janela)
valorEntrada.place(x=380,y=580, width=80, height=25)


resultadoOperacaoNome=Label(janela, text="Resultado da Operação($)", bg="#008", foreground="#fff", anchor=W).place(x=640,y=580, width=170, height=25)
resultadoOperacao=Entry(janela)
resultadoOperacao.place(x=820,y=580, width=80, height=25)



#Botão

btn=Button(janela,text="Apagar", command=limpar)
btn.place(x=470, y=650, width=80, height=25)

save=Button(janela,text="Salvar", command=criarPasta)
save.place(x=570, y=650, width=80, height=25)

janela.mainloop()