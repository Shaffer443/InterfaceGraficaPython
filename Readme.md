**Sistema para Acompanhamento de Entradas Esportvas**

**Premissa:** 

_Versão beta(Atual)_, Pode-se inserir os nomes de um Time A e B e três opções de possibilidades de 
operações esportivas. 

O arquivo é salvo em um arquivo de texto, e pode-se recorrer a ele para acompanhar suas analisaes inseridas.

**Bibliotecas ou Frameworks**

- from **tkinter** import * - (_Usado para criação de Interface gráfica_) <br>
- import **datetime** - (_Uso de data e hora_)<br>
- from **datetime** import **date** - (_Uso de data e hora_)<br>
- import **shutil** (_Usado para movimentação de arquivos entre pastas_)<br>
- import **os** - (_caminhos de diretório para salvamento_)<br>

**Documentações consultadas**

Documentação: https://docs.python.org/3.9/library/tkinter.html#a-simple-hello-world-program

**Informações de funções**

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

**entry**- Usado para inserir texte e indicar o seu master (pai), no exemplo é a variável _janela_,
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

Insere um botão que podemos conectar com uma função, para que seja conectada quando clicarmos.

sintaxe:

- Button(_master(pai)_,text="nome impresso no botão", command=_nome da função que queremo conectar_)

Exemplo:

btn=<mark>Button(janela,text="Imprimir", command=impDados)</mark><br>
btn.place(x=450, y=350, width=80, height=25)





