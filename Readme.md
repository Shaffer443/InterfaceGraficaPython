Documentação: https://docs.python.org/3.9/library/tkinter.html#a-simple-hello-world-program

from tkinter import * - importação de tudo.

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
X ou Y, indicará se a expansão será no vetor Y ou vetor Y.

**side** (left, right, buttom, top) - posicionamento.

**anchor**(Âncora) - N | S | W | E (norte - sul - oeste - leste). nordeste(NE),suldeeste(SE) e outros
também funcionam.

**entry**- Usado para inserir texte e indicacar o seu master (pai), no exemplo é a variável _janela_,
que é a master(pai)
- Entry(janela)


**text** - Um componente de texto multilinhas. Com mais de uma linha. Textos grandes.
- Text(janela)

