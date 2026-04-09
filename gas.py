def monitorar_gas(nivel_atual):
    if nivel_atual > 100:
        return "O nível do gás está alto."
    elif 20 <= nivel_atual <= 100:
        return "O nível do gás está médio."
    elif 5 <= nivel_atual < 20:
        return "O nível do gás está baixo. Considere reabastecer."
    else:
        return "O nível do gás está crítico! Reabasteça imediatamente."

def exibir_informacao(nivel_atual):
    mensagem = monitorar_gas(nivel_atual)
    print(mensagem)

# Simulando níveis de gás
niveis_de_gas = [70, 40, 15, 3]

for nivel in niveis_de_gas:
    exibir_informacao(nivel)

def exibir_informacao(nivel_atual):
    mensagem = monitorar_gas(nivel_atual)
    print(mensagem)

# Simulando níveis de gás
niveis_de_gas = [70, 40, 15, 3]

for nivel in niveis_de_gas:
    exibir_informacao(nivel)

import tkinter as tk

def exibir_informacao_gui(nivel_atual):
    mensagem = monitorar_gas(nivel_atual)
    label.config(text=mensagem)

# Configuração da janela
root = tk.Tk()
root.title("Monitor de Gás")

label = tk.Label(root, text="", font=("Helvetica", 16))
label.pack(pady=20)

# Simulando atualização de nível de gás
for nivel in niveis_de_gas:
    root.after(2000, lambda n=nivel: exibir_informacao_gui(n))
    root.update()

root.mainloop()

import tkinter as tk

def exibir_informacao_gui(nivel_atual):
    mensagem = monitorar_gas(nivel_atual)
    label.config(text=mensagem)

def atualizar_nivel():
    nivel_atual = ler_sensor()
    exibir_informacao_gui(nivel_atual)
    root.after(5000, atualizar_nivel)

# Configuração da janela
root = tk.Tk()
root.title("Monitor de Gás")

label = tk.Label(root, text="", font=("Helvetica", 16))
label.pack(pady=20)

# Iniciar o monitoramento
atualizar_nivel()

root.mainloop()
import tkinter as tk

def exibir_informacao_gui(nivel_atual):
    mensagem = monitorar_gas(nivel_atual)
    label.config(text=mensagem)

def atualizar_nivel():
    nivel_atual = ler_sensor()
    exibir_informacao_gui(nivel_atual)
    root.after(5000, atualizar_nivel)

# Configuração da janela
root = tk.Tk()
root.title("Monitor de Gás")

label = tk.Label(root, text="", font=("Helvetica", 16))
label.pack(pady=20)

# Iniciar o monitoramento
atualizar_nivel()

root.mainloop()
