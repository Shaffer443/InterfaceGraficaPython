**Bibliotecas e Frameworks**

- pip install mysql-connector-python 
        (https://www.w3schools.com/python/python_mysql_getstarted.asp,
         https://dev.mysql.com/doc/connector-python/en/connector-python-installation-binary.html,
         https://pypi.org/project/mysql-connector-python/)


Documentação: https://docs.python.org/3.9/library/tkinter.html#a-simple-hello-world-program

from tkinter import * - importação de tudo.

janela.title("Shaffer Programas") # titulo na janela do programa
janela.geometry("1080x720") #tamanho da janela
janela.configure(background="#008") # cor de fundo em RGB

_variável_**.place** - Configuração de posição para que o Label funcione. Precisa-se dizer 
onde vai aparecer na tela.

_variável_**.pack** - É mais adequado para container que o place.

_variável_.mainloop() -  É o que executa o programa.

**ipadx | ipady** - Alocação entre direita e esquerda (ipadx). Alocação de expanção cima e baixo Y(ipady).
Caso use expand=True e um valor para o fill X ou Y, é para onde ele expandirá se adquando a tela.
O uso do expand é opcional. nâo usando, ele ficará em um tamanho fixo.

**padx | pady** - É o espassamento entre o o final do container ou bloco e as extremidades:
esquerda e direita (interno?)

**fill=x | fill=y** - Usado para expadir, através do código expend = True | False. O valor do fill
X ou Y, indicará se a expansão será no vetor Y ouButton(janela,text="Imprimir", command=impDados) vetor Y.

**side** (left, right, bottom, top) - posicionamento.

**anchor**(Âncora) - N | S | W | E (norte - sul - oeste - leste). nordeste(NE),suldeeste(SE) e outros
também funcionam.

**entry**- Usado para inserir texte e indicacar o seu master (pai), no exemplo é a variável _janela_,
que é a master(pai)
- Entry(janela)
Quando precisamos pegar os dados de um Text(), precisamos informar onde começa e onde termina 
o que desejamos pegar.

_Exemplo:_

- print("%s"%timecasa.get("1.0",END))

Traduzindo, estamos informando que queremos pegar da primeira linha até o final.

**text** - Um componente de texto multilinhas. Com mais de uma linha. Textos grandes.
- Text(janela)


**Inserindo Botões:**

Insere um botão que pdoemso concetar com uma função, para que seja conectada quando clicarmos.

sintaxe:

- Button(_master(pai)_,text="nome impresso no botão", command=_nome da função que queremo conectar_)

Exemplo:

btn=<mark>Button(janela,text="Imprimir", command=impDados)</mark><br>
btn.place(x=450, y=350, width=80, height=25)






