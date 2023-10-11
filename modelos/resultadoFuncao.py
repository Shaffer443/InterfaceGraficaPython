import tkinter as tk

def calcular_resultado():
    # Substitua esta função pela sua própria lógica de cálculo
    resultado = 42
    resultado_label.config(text=f"Resultado: {resultado}")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Exemplo Tkinter")

# Widget Label para exibir o resultado
resultado_label = tk.Label(janela, text="Resultado: ")
resultado_label.pack()

# Botão para calcular o resultado
calcular_botao = tk.Button(janela, text="Calcular", command=calcular_resultado)
calcular_botao.pack()

# Executa o loop principal da janela
janela.mainloop()
