from tkinter import * #updagre 1.2.1
import tkinter as tk #updagre 1.2.1
from tkinter import ttk
import datetime
from datetime import date
import os
import os.path
import funcao
import criacaoDiretorio
# import selecaoMercados #updagre 1.2.1



today = date.today()
# os.chdir("Entradas") #diretorio da pasta PAI

janela=Tk()

def infoDataHora():
    dt = datetime.datetime.now()
    go = dt.strftime("%A %d. %B %Y - %H:%M")
    return go

# Ficou em desuso com nvoso arquivos .py para o diretório
def verificandoDiretorios():
    if criacaoDiretorio.statusDiretororio == True:
        return salvar()
    else:
        print("Diretórios não encontrados.....")
        print("Trabalhando na criação dos diretórios.....")
        try:
            os.mkdir(f"{criacaoDiretorio.pastaPrincipal()}")
            if os.path.exists(f"{criacaoDiretorio.statusDiretororio}"):
                return salvar()
        except:
            print("Falha na criação dos diretórios..... ERRO")

def fechandoTela(janela, tempo):
        janela.after(tempo * 1000, lambda: janela.destroy())

def salvar():
        if os.path.exists(f"{criacaoDiretorio.pastaAno}/{criacaoDiretorio.pastaMes}/{criacaoDiretorio.pastaDia}") and criacaoDiretorio.statusDiretororio == True:
            diretorioSalvamento = f"{criacaoDiretorio.pastaAno}/{criacaoDiretorio.pastaMes}/{criacaoDiretorio.pastaDia}"
            try:
                os.chdir(f"{diretorioSalvamento}")
                # arquivo=open(f"{today}.txt","a+")
                arquivo = open("%s"%casanome.get()+"x"+"%s"%visitantenome.get()+".txt", "a+") #implementação
                #arquivo.write(f"{today}\n\n")
                arquivo.write("\nData: %s\n" % today)
                arquivo.write(f"Torneio: %s\n" % torneio.get())
                arquivo.write("%s" % casanome.get() + " x " + "%s\n"% visitantenome.get())
                arquivo.write("Operação: %s\n" % mercado.get()) # update 1.2.1
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
                arquivo.write("Porcentagem sobre a Stake: %s\n" % porcentagemLucroPrejuizo(valorEntrada.get(), resultadoOperacao.get())[1]) # update 1.2.3
                arquivo.write("\n\n")
                #arquivo.write(f'insert into input values(default,\'{today}\',\'{torneio.get()}\',{casanome.get()},{visitantenome.get()},{mercado.get()},{oddsEntrada.get()},{minEntrada.get()},{oddsSaida.get()},{minSaida.get()},{golsMandante.get()},{golsVisitante.get()},{golsMandanteSegundo.get()},{golsVisitanteSegundo.get()},{valorEntrada.get()},{funcao.scriptInputJogoRedGreen(resultadoOperacao.get())},{resultadoOperacao.get()},default);\n\n')
                arquivo.write(funcao.criacaoScriptMysql(torneio.get(),
                                                        casanome.get(),
                                                        visitantenome.get(),
                                                        mercado.get(),
                                                        oddsEntrada.get(),
                                                        minEntrada.get(),
                                                        oddsSaida.get(),
                                                        minSaida.get(),
                                                        golsMandante.get(),
                                                        golsVisitante.get(),
                                                        golsMandanteSegundo.get(),
                                                        golsVisitanteSegundo.get(),
                                                        valorEntrada.get(),
                                                        resultadoOperacao.get(),
                                                        porcentagemLucroPrejuizo(valorEntrada.get(),resultadoOperacao.get())[1]))

                arquivo.close()

                # info na janela
                res = Label(janela, text="Salvo Com Sucesso!", bg="#008", foreground="#00FF00", anchor=W).place(x=450, y=700, width=150,height=25)
                contagemDeTempo = Label(janela, text="Fechando Janela em 5 segundos", bg="#008", foreground="#00FF00",
                                        anchor=W).place(x=600, y=700, width=150, height=25)

                return res, contagemDeTempo, fechandoTela(janela,5) #, porcentagemLucroPrejuizo(valorEntrada.get(), resultadoOperacao.get())


            except:
                # info na janela
                erro = Label(janela, text="Erros no Salvamento", bg="#008", foreground="#FF0000", anchor=W).place(x=500, y=700, width=150,height=25)
                return erro

        else:
            try:
                os.mkdir(f"{criacaoDiretorio.pastaPrincipal()}")
                diretorioSalvamento = f"{criacaoDiretorio.pastaAno}/{criacaoDiretorio.pastaMes}/{criacaoDiretorio.pastaDia}"
                os.chdir(f"{diretorioSalvamento}")
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
                arquivo.write("Porcentagem sobre a Stake: %s\n" % porcentagemLucroPrejuizo(valorEntrada.get(),resultadoOperacao.get())[1]) # update 1.2.3
                arquivo.write("\n\n")
                #arquivo.write(f"insert into input values(default,{today},{torneio.get()},{casanome.get()},{visitantenome.get()},{mercado.get()},{oddsEntrada.get()},{minEntrada.get()},{oddsSaida.get()},{minSaida.get()},{golsMandante.get()},{golsVisitante.get()},{golsMandanteSegundo.get()},{golsVisitanteSegundo.get()},{valorEntrada.get()},{funcao.scriptInputJogoRedGreen(resultadoOperacao.get())},{resultadoOperacao.get()},default);\n\n")
                # arquivo.write("%s\n\n" %funcao.criacaoScriptMysql(torneio.get(), casanome.get(), visitantenome.get(), mercado.get(), oddsEntrada.get(), minEntrada.get(),oddsSaida.get(), minSaida.get(), golsMandante.get(), golsVisitante.get(), golsMandanteSegundo.get(), golsVisitanteSegundo.get(),valorEntrada.get(), resultadoOperacao.get()))
                arquivo.write(funcao.criacaoScriptMysql(torneio.get(),
                                                        casanome.get(),
                                                        visitantenome.get(),
                                                        mercado.get(),
                                                        oddsEntrada.get(),
                                                        minEntrada.get(),
                                                        oddsSaida.get(),
                                                        minSaida.get(),
                                                        golsMandante.get(),
                                                        golsVisitante.get(),
                                                        golsMandanteSegundo.get(),
                                                        golsVisitanteSegundo.get(),
                                                        valorEntrada.get(),
                                                        resultadoOperacao.get(),
                                                        porcentagemLucroPrejuizo(valorEntrada.get(),resultadoOperacao.get())[1]))

                arquivo.close()

                # info na janela
                res = Label(janela, text="Salvo Com Sucesso!", bg="#008", foreground="#00FF00", anchor=W).place(x=450, y=700,width=150,height=25)
                contagemDeTempo = Label(janela, text="Fechando Janela em 5 segundos", bg="#008", foreground="#00FF00", anchor=W).place(x=600,y=700,width=150,height=25)

                return res, contagemDeTempo, fechandoTela(janela,5)


            except:
                # info na janela
                erro = Label(janela, text="Erros no Salvamento", bg="#008", foreground="#FF0000", anchor=W).place(x=500, y=700,width=150,height=25)
                return erro


#configurações de ambiente:

janela.title("Shaffer Dev - Trader Esportivo (Futebol)") # titulo na janela do programa
janela.geometry("1080x800") #tamanho da janela
janela.configure(background="#008") # cor de fundo em RGB


#rodapé:

#Update 1.2.3 - 10/10/2023
def porcentagemLucroPrejuizo(stake, resultadoDaOperacao):
    #print(type(stake))
    number_stake = float(stake)
    number_resultadoDaOperacao = float(resultadoDaOperacao)
    # print(type(number_stake))
    retorno = (number_resultadoDaOperacao/number_stake)*100
    # if funcao.scriptInputJogoRedGreen(resultadoDaOperacao) == "Red":
    if number_resultadoDaOperacao < 0:
        #print(f"Retorno: {funcao.scriptInputJogoRedGreen(resultadoDaOperacao)} = {retorno:.2f}%")
        # return resultado_label.config(text=f"Resultado: {funcao.scriptInputJogoRedGreen(resultadoDaOperacao)} = {retorno:.2f}%")
        resultado_label = Label(janela, text=f"Resultado: {funcao.scriptInputJogoRedGreen(resultadoDaOperacao)} = {retorno:.2f}%", background="#006", foreground="#FF0000").place(x=330, y=670,
                                                                                                        width=500,
                                                                                                        height=30)
        numero_porcentagem = f"{retorno:.2f}"
        return resultado_label, numero_porcentagem
    else:
        resultado_label = Label(janela,
                                text=f"Resultado: {funcao.scriptInputJogoRedGreen(resultadoDaOperacao)} = + {retorno:.2f}%",
                                background="#006", foreground="#00FF00").place(x=330, y=670,
                                                                            width=500,
                                                                            height=30)
        numero_porcentagem = f"{retorno:.2f}"
        return resultado_label, numero_porcentagem



autor=Label(janela,text="Criado por: Rafael Gouveia - https://linktr.ee/rafaelgouveia",background="#008",foreground="#fff")
autor.place(x=250, y=760, width=500, height=30)

ultimaAtualizacao=Label(janela,text=f"Última Atualização: 11/10/2023",background="#006",foreground="#fff")
ultimaAtualizacao.place(x=800, y=760, width=250, height=30)

#conteudo (info Sistemas):

nome=Label(janela,text="Acompanhamento de Entradas: Trader Esportivo",background="#CCFFCC",)
nome.place(x=10, y=10, width=330, height=30)

nome=Label(janela,text="Versão beta 1.2.3",background="#000", foreground="#fff")
nome.place(x=940, y=10, width=130, height=30)

info=Label(janela,text= f"{infoDataHora()}",background="#000", foreground="#fff")
info.place(x=450, y=10, width=300, height=30)

# Definindo os Blocos

# Container de Informarções (Futuros upgrades)
fundo = "#fff"
cor_fonte = "#000"

subjanela=Label(janela,text="Dados Torneio", bg=fundo, fg=cor_fonte)
subjanela.pack(ipadx=20, ipady=20, padx=5, pady=150, side="left", fill=Y, expand=True, anchor=W)

#entradas

#Torneio (padrão atual)

# torneioNome=Label(janela, text="Torneio", bg="#008", foreground="#fff").place(x=500,y=80, width=100, height=25)
# torneio=Entry(janela)
# torneio.place(x=400,y=110, width=300, height=25)

########################################### Torneio - Update 1.2.2
torneioNome=Label(janela, text="Torneio", bg="#008", foreground="#fff").place(x=500,y=80, width=100, height=25)
torneio = tk.StringVar()
combo2 = ttk.Combobox(janela, textvariable=torneio)
combo2['values'] = ('Alemanha Supertaça', 'Amistoso de Elite', 'Brasileiro Série A', 'Brasileiro Série B', 'Bundesliga 2 Alemã',
                    'Bundesliga Alemã', 'CONMEBOL Libertadores', 'CONMEBOL Sudamericana', 'Capa do Mundo da FIFA Feminino',
                    'Copa Do Brasil', 'Copa da Alemanha', 'Copa da Itália', 'Copa do Nordeste', 'Escócia-Premiership', 'Espanha - La Liga',
                    'França - Ligue 1', 'Holanda - Eredivisie', 'Inglaterra Community Shield', 'Inglaterra Copa da Liga', 'Inglaterra Premier League',
                    'Itália - Série A', 'Itália - Serie B',  'Liga Conferência Europa', 'Liga Profissional da Arábia Saudita',
                    'Portugal Supertaça', 'Portugal - Primeira Liga', 'Premier League', 'Torneio Não Listado', 'UEFA Champions League',
                    'UEFA Euro Eliminatórias', 'UEFA Europa Conference League', 'UEFA Europa Conference League Classificatórias',
                    'UEFA Liga Conferência Europa Classificatórias', 'UEFA Liga Das Nações', 'UEFA Liga Europa',
                    'UEFA Liga dos Campeões Eliminatórias', 'UEFA Supertaça')
combo2.place(x=400,y=110, width=300, height=25)

casa=Label(janela, text="Time Mandante (Casa)", bg="#008", foreground="#fff").place(x=260,y=150, width=200, height=25)
casanome=Entry(janela)
casanome.place(x=200,y=180, width=300, height=25)

vistante=Label(janela, text="Time Visitante", bg="#008", foreground="#fff").place(x=700,y=150, width=100, height=25)
visitantenome=Entry(janela)
visitantenome.place(x=600,y=180, width=300, height=25)


####Input Dados

#mercado (padrão atual)
# mercadoNome=Label(janela, text="Mercado Alvo", bg="#008", foreground="#fff", anchor=W).place(x=500,y=220, width=100, height=25)
# mercado=Entry(janela)
# mercado.place(x=400,y=250, width=300, height=25)

########################################### Mercada - Update 1.2.1

mercadoNome=Label(janela, text="Mercado Alvo", bg="#008", foreground="#ffff00", anchor=W).place(x=500,y=220, width=100, height=25)
mercado = tk.StringVar()
combo = ttk.Combobox(janela, textvariable=mercado)
combo['values'] = ('Back Mandante','Back Visitante','Back Empate','Lay Empate','Lay Mandante','Lay Visitante','Over 0,5 no 2º tempo','Over 1,5','Over 2,5','Over 3,5','Under 1,5','Under 2,5','Under 3,5')
combo.place(x=400,y=250, width=300, height=25)
# combo.pack()


##############################################################
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

# btn=Button(janela,text="Apagar", command=limpar)
# btn.place(x=470, y=650, width=80, height=25)

save=Button(janela,text="Salvar", command=verificandoDiretorios)
save.place(x=570, y=730, width=80, height=25)


janela.mainloop()