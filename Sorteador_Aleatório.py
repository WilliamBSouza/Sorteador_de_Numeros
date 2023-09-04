import random
import tkinter as tk
from tkinter import messagebox
from tkinter import IntVar, Radiobutton

def sortear_numeros():
    try:
        numero_minimo = int(min_entry.get())
        numero_maximo = int(max_entry.get())
        quantidade_de_sorteios = int(quantidade_entry.get())
        
        if numero_minimo >= numero_maximo:
            messagebox.showerror("Erro", "O número mínimo deve ser menor que o número máximo.")
            return

        numeros_sorteados = []

        repetir_numeros = repeticao_var.get()  # Obter a escolha do usuário sobre repetição
        
        numeros_disponiveis = list(range(numero_minimo, numero_maximo + 1))  # Inicializar lista de números disponíveis

        for _ in range(quantidade_de_sorteios):
            if not numeros_disponiveis:
                messagebox.showerror("Erro", "Não há números disponíveis para sortear.")
                return

            numero_sorteado = random.choice(numeros_disponiveis)

            if not repetir_numeros:
                numeros_disponiveis.remove(numero_sorteado)  # Remover número sorteado da lista de disponíveis

            numeros_sorteados.append(numero_sorteado)

        # Dividir os números sorteados em grupos de até 13 números por linha
        grupos = [numeros_sorteados[i:i+13] for i in range(0, len(numeros_sorteados), 13 )]

        resultado_text = "Números sorteados:\n"
        for grupo in grupos:
            resultado_text += ", ".join(map(str, grupo)) + "\n"

        resultado_label.config(text=resultado_text)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

def copiar_resultados():
    resultado_text = resultado_label.cget("text")
    if resultado_text:
        root.clipboard_clear()
        root.clipboard_append(resultado_text)
        root.update()

# Configuração da janela principal
root = tk.Tk()
root.title("Sorteador de Números")
root.geometry("700x230")

# Rótulos e campos de entrada
min_label = tk.Label(root, text="Número Mínimo:")
min_label.place(x=10, y=10)
min_entry = tk.Entry(root)
min_entry.place(x=150, y=10)

max_label = tk.Label(root, text="Número Máximo:")
max_label.place(x=10, y=40)
max_entry = tk.Entry(root)
max_entry.place(x=150, y=40)

quantidade_label = tk.Label(root, text="Quantidade de Números a Serem Sorteados:")
quantidade_label.place(x=10, y=70)
quantidade_entry = tk.Entry(root)
quantidade_entry.place(x=250, y=70)

# Adicionar botões de seleção para repetição ou não repetição
repeticao_var = IntVar()
repeticao_var.set(1)  # Definir inicialmente como repetição permitida
repeticao_com = Radiobutton(root, text="Com Repetição", variable=repeticao_var, value=1)
repeticao_sem = Radiobutton(root, text="Sem Repetição", variable=repeticao_var, value=0)
repeticao_com.place(x=10, y=100)
repeticao_sem.place(x=150, y=100)

sortear_button = tk.Button(root, text="Sortear", command=sortear_numeros)
sortear_button.place(x=10, y=130)

copiar_button = tk.Button(root, text="Copiar Resultados", command=copiar_resultados)
copiar_button.place(x=130, y=130)

resultado_label = tk.Label(root, text="")
resultado_label.place(x=10, y=160)

root.mainloop()
