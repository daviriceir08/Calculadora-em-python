
import math
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


HISTORICO_MAX = 5
historico = []


def saudacao():
    hora = datetime.now().hour
    if hora < 12:
        return "Bom dia"
    elif hora < 18:
        return "Boa tarde"
    return "Boa noite"


def adicionar_historico(texto):
    historico.append(texto)
    if len(historico) > HISTORICO_MAX:
        historico.pop(0)
    atualizar_historico()


def atualizar_historico():
    caixa_historico.config(state="normal")
    caixa_historico.delete("1.0", tk.END)
    if not historico:
        caixa_historico.insert(tk.END, "Nenhuma conta realizada ainda.")
    else:
        for i, item in enumerate(historico, start=1):
            caixa_historico.insert(tk.END, f"{i}. {item}\n")
    caixa_historico.config(state="disabled")


def avaliar_expressao(expr):
    expr = expr.strip().replace("^", "**")
    if not expr:
        raise ValueError("Digite uma expressão.")

    permitidos = "0123456789+-*/()., %"
    for ch in expr:
        if ch not in permitidos:
            raise ValueError("Use apenas números, +, -, *, /, parênteses, ponto ou vírgula.")

    expr = expr.replace(",", ".")

    try:
        resultado = eval(expr, {"__builtins__": {}}, {})
    except ZeroDivisionError:
        raise ValueError("Não existe divisão por zero.")
    except Exception:
        raise ValueError("Expressão inválida. Exemplo: 10 + 5*2 - 3/2")

    return resultado


def calcular_expressao():
    try:
        expr = entrada_expressao.get().strip()
        resultado = avaliar_expressao(expr)
        texto = f"{expr} = {resultado}"
        lbl_resultado.config(text=texto)
        adicionar_historico(texto)
    except ValueError as e:
        messagebox.showerror("Erro", str(e))


def calcular_media():
    try:
        numeros = obter_lista_numeros(entrada_lista_media.get())
        resultado = sum(numeros) / len(numeros)
        texto = f"Média de {numeros} = {resultado}"
        lbl_resultado_media.config(text=texto)
        adicionar_historico(texto)
    except ValueError as e:
        messagebox.showerror("Erro", str(e))


def calcular_porcentagem():
    try:
        valor = float(entry_valor_porcentagem.get().replace(",", "."))
        percentual = float(entry_percentual.get().replace(",", "."))
        resultado = valor * (percentual / 100)
        texto = f"{percentual}% de {valor} = {resultado}"
        lbl_resultado_porcentagem.config(text=texto)
        adicionar_historico(texto)
    except ValueError:
        messagebox.showerror("Erro", "Digite números válidos na porcentagem.")


def calcular_raiz():
    try:
        numero = float(entry_raiz.get().replace(",", "."))
        if numero < 0:
            raise ValueError("Não existe raiz quadrada real de número negativo.")
        resultado = math.sqrt(numero)
        texto = f"Raiz quadrada de {numero} = {resultado}"
        lbl_resultado_raiz.config(text=texto)
        adicionar_historico(texto)
    except ValueError as e:
        messagebox.showerror("Erro", str(e))


def obter_lista_numeros(texto):
    texto = texto.strip()
    if not texto:
        raise ValueError("Digite pelo menos um número.")
    texto = texto.replace(";", ",")
    partes = [p.strip().replace(",", ".") for p in texto.split() if p.strip()]

    if len(partes) == 1 and ";" not in texto and "," in texto:
        partes = [p.strip().replace(",", ".") for p in texto.split(",") if p.strip()]

    numeros = []
    for parte in partes:
        numeros.append(float(parte))
    return numeros


def calcular_primeiro_grau():
    try:
        a = float(entry_a1.get().replace(",", "."))
        b = float(entry_b1.get().replace(",", "."))

        if a == 0:
            raise ValueError("Não é uma equação do 1º grau se a = 0.")

        x = -b / a
        texto = f"Equação do 1º grau ({a}x + {b} = 0) -> x = {x}"
        lbl_resultado_1.config(text=texto)
        adicionar_historico(texto)

    except ValueError as e:
        messagebox.showerror("Erro", str(e))


def calcular_segundo_grau():
    try:
        a = float(entry_a2.get().replace(",", "."))
        b = float(entry_b2.get().replace(",", "."))
        c = float(entry_c2.get().replace(",", "."))

        if a == 0:
            raise ValueError("Não é uma equação do 2º grau se a = 0.")

        delta = b**2 - 4*a*c

        if delta < 0:
            texto = f"Equação do 2º grau ({a}x² + {b}x + {c} = 0) -> Delta = {delta}. Não existem raízes reais."
        elif delta == 0:
            x = -b / (2*a)
            texto = f"Equação do 2º grau ({a}x² + {b}x + {c} = 0) -> Delta = {delta}. x = {x}"
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            texto = f"Equação do 2º grau ({a}x² + {b}x + {c} = 0) -> Delta = {delta}. x1 = {x1}, x2 = {x2}"

        lbl_resultado_2.config(text=texto)
        adicionar_historico(texto)

    except ValueError as e:
        messagebox.showerror("Erro", str(e))


def limpar_tudo():
    entrada_expressao.delete(0, tk.END)
    entrada_lista_media.delete(0, tk.END)
    entry_valor_porcentagem.delete(0, tk.END)
    entry_percentual.delete(0, tk.END)
    entry_raiz.delete(0, tk.END)
    entry_a1.delete(0, tk.END)
    entry_b1.delete(0, tk.END)
    entry_a2.delete(0, tk.END)
    entry_b2.delete(0, tk.END)
    entry_c2.delete(0, tk.END)

    lbl_resultado.config(text="Resultado da expressão aparecerá aqui.")
    lbl_resultado_media.config(text="Resultado da média aparecerá aqui.")
    lbl_resultado_porcentagem.config(text="Resultado da porcentagem aparecerá aqui.")
    lbl_resultado_raiz.config(text="Resultado da raiz aparecerá aqui.")
    lbl_resultado_1.config(text="Resultado da equação do 1º grau aparecerá aqui.")
    lbl_resultado_2.config(text="Resultado da equação do 2º grau aparecerá aqui.")


def limpar_historico():
    historico.clear()
    atualizar_historico()


janela = tk.Tk()
janela.title("Calculadora Completa - Projeto em Python")
janela.geometry("980x760")
janela.minsize(930, 700)

style = ttk.Style()
try:
    style.theme_use("clam")
except:
    pass

container = ttk.Frame(janela, padding=16)
container.pack(fill="both", expand=True)

titulo = ttk.Label(
    container,
    text="Calculadora Completa em Python",
    font=("Segoe UI", 20, "bold")
)
titulo.pack(anchor="w")

subtitulo = ttk.Label(
    container,
    text=f"{saudacao()}! Faça contas misturadas, equações e acompanhe o histórico.",
    font=("Segoe UI", 11)
)
subtitulo.pack(anchor="w", pady=(0, 12))

notebook = ttk.Notebook(container)
notebook.pack(fill="both", expand=True)

aba_basica = ttk.Frame(notebook, padding=16)
aba_primeiro = ttk.Frame(notebook, padding=16)
aba_segundo = ttk.Frame(notebook, padding=16)
aba_historico = ttk.Frame(notebook, padding=16)

notebook.add(aba_basica, text="Calculadora básica")
notebook.add(aba_primeiro, text="1º grau")
notebook.add(aba_segundo, text="2º grau")
notebook.add(aba_historico, text="Histórico")


# Aba básica
ttk.Label(
    aba_basica,
    text="Aqui você pode misturar contas, como numa calculadora real.",
    font=("Segoe UI", 11, "bold")
).pack(anchor="w")

ttk.Label(
    aba_basica,
    text="Exemplos: 10 + 5 * 2 | 100 / 4 + 7 | (8 + 2) * 3 | 2^3 + 4",
    font=("Segoe UI", 10)
).pack(anchor="w", pady=(0, 10))

ttk.Label(aba_basica, text="Digite a expressão completa:", font=("Segoe UI", 11)).pack(anchor="w")
entrada_expressao = ttk.Entry(aba_basica, width=80)
entrada_expressao.pack(fill="x", pady=(4, 10))

frame_expr = ttk.Frame(aba_basica)
frame_expr.pack(anchor="w", pady=(0, 14))
ttk.Button(frame_expr, text="Calcular expressão", command=calcular_expressao).pack(side="left", padx=(0, 8))
ttk.Button(frame_expr, text="Limpar tudo", command=limpar_tudo).pack(side="left")

lbl_resultado = ttk.Label(
    aba_basica,
    text="Resultado da expressão aparecerá aqui.",
    font=("Segoe UI", 11, "bold"),
    wraplength=850,
    justify="left"
)
lbl_resultado.pack(anchor="w", pady=(0, 16))

separador1 = ttk.Separator(aba_basica, orient="horizontal")
separador1.pack(fill="x", pady=8)

ttk.Label(
    aba_basica,
    text="Cálculos úteis do dia a dia",
    font=("Segoe UI", 11, "bold")
).pack(anchor="w", pady=(8, 10))

frame_media = ttk.LabelFrame(aba_basica, text="Média de vários números", padding=12)
frame_media.pack(fill="x", pady=(0, 10))

ttk.Label(frame_media, text="Digite números separados por espaço. Exemplo: 7 8 9 10").pack(anchor="w")
entrada_lista_media = ttk.Entry(frame_media, width=70)
entrada_lista_media.pack(fill="x", pady=(4, 8))
ttk.Button(frame_media, text="Calcular média", command=calcular_media).pack(anchor="w")
lbl_resultado_media = ttk.Label(frame_media, text="Resultado da média aparecerá aqui.", font=("Segoe UI", 10, "bold"))
lbl_resultado_media.pack(anchor="w", pady=(8, 0))

frame_porcentagem = ttk.LabelFrame(aba_basica, text="Porcentagem", padding=12)
frame_porcentagem.pack(fill="x", pady=(0, 10))

linha_porcentagem = ttk.Frame(frame_porcentagem)
linha_porcentagem.pack(anchor="w")
ttk.Label(linha_porcentagem, text="Valor:").pack(side="left")
entry_valor_porcentagem = ttk.Entry(linha_porcentagem, width=15)
entry_valor_porcentagem.pack(side="left", padx=(5, 15))
ttk.Label(linha_porcentagem, text="Percentual:").pack(side="left")
entry_percentual = ttk.Entry(linha_porcentagem, width=10)
entry_percentual.pack(side="left", padx=(5, 10))
ttk.Label(linha_porcentagem, text="%").pack(side="left")
ttk.Button(frame_porcentagem, text="Calcular porcentagem", command=calcular_porcentagem).pack(anchor="w", pady=(8, 0))
lbl_resultado_porcentagem = ttk.Label(frame_porcentagem, text="Resultado da porcentagem aparecerá aqui.", font=("Segoe UI", 10, "bold"))
lbl_resultado_porcentagem.pack(anchor="w", pady=(8, 0))

frame_raiz = ttk.LabelFrame(aba_basica, text="Raiz quadrada", padding=12)
frame_raiz.pack(fill="x", pady=(0, 10))

linha_raiz = ttk.Frame(frame_raiz)
linha_raiz.pack(anchor="w")
ttk.Label(linha_raiz, text="Número:").pack(side="left")
entry_raiz = ttk.Entry(linha_raiz, width=20)
entry_raiz.pack(side="left", padx=(5, 10))
ttk.Button(frame_raiz, text="Calcular raiz", command=calcular_raiz).pack(anchor="w", pady=(8, 0))
lbl_resultado_raiz = ttk.Label(frame_raiz, text="Resultado da raiz aparecerá aqui.", font=("Segoe UI", 10, "bold"))
lbl_resultado_raiz.pack(anchor="w", pady=(8, 0))


# Aba 1º grau
ttk.Label(
    aba_primeiro,
    text="Formato: ax + b = 0",
    font=("Segoe UI", 11)
).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))

ttk.Label(aba_primeiro, text="Valor de a:").grid(row=1, column=0, sticky="w", padx=(0, 10), pady=5)
entry_a1 = ttk.Entry(aba_primeiro, width=25)
entry_a1.grid(row=1, column=1, sticky="w", pady=5)

ttk.Label(aba_primeiro, text="Valor de b:").grid(row=2, column=0, sticky="w", padx=(0, 10), pady=5)
entry_b1 = ttk.Entry(aba_primeiro, width=25)
entry_b1.grid(row=2, column=1, sticky="w", pady=5)

ttk.Button(aba_primeiro, text="Calcular equação do 1º grau", command=calcular_primeiro_grau).grid(
    row=3, column=0, columnspan=2, sticky="w", pady=(12, 10)
)

lbl_resultado_1 = ttk.Label(
    aba_primeiro,
    text="Resultado da equação do 1º grau aparecerá aqui.",
    font=("Segoe UI", 11, "bold"),
    wraplength=800,
    justify="left"
)
lbl_resultado_1.grid(row=4, column=0, columnspan=2, sticky="w")


# Aba 2º grau
ttk.Label(
    aba_segundo,
    text="Formato: ax² + bx + c = 0",
    font=("Segoe UI", 11)
).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))

ttk.Label(aba_segundo, text="Valor de a:").grid(row=1, column=0, sticky="w", padx=(0, 10), pady=5)
entry_a2 = ttk.Entry(aba_segundo, width=25)
entry_a2.grid(row=1, column=1, sticky="w", pady=5)

ttk.Label(aba_segundo, text="Valor de b:").grid(row=2, column=0, sticky="w", padx=(0, 10), pady=5)
entry_b2 = ttk.Entry(aba_segundo, width=25)
entry_b2.grid(row=2, column=1, sticky="w", pady=5)

ttk.Label(aba_segundo, text="Valor de c:").grid(row=3, column=0, sticky="w", padx=(0, 10), pady=5)
entry_c2 = ttk.Entry(aba_segundo, width=25)
entry_c2.grid(row=3, column=1, sticky="w", pady=5)

ttk.Button(aba_segundo, text="Calcular equação do 2º grau", command=calcular_segundo_grau).grid(
    row=4, column=0, columnspan=2, sticky="w", pady=(12, 10)
)

lbl_resultado_2 = ttk.Label(
    aba_segundo,
    text="Resultado da equação do 2º grau aparecerá aqui.",
    font=("Segoe UI", 11, "bold"),
    wraplength=800,
    justify="left"
)
lbl_resultado_2.grid(row=5, column=0, columnspan=2, sticky="w")


# Aba histórico
ttk.Label(
    aba_historico,
    text="Últimas 5 contas realizadas:",
    font=("Segoe UI", 11)
).pack(anchor="w", pady=(0, 8))

caixa_historico = tk.Text(aba_historico, width=90, height=18, state="disabled", font=("Consolas", 11))
caixa_historico.pack(fill="both", expand=True)

ttk.Button(aba_historico, text="Limpar histórico", command=limpar_historico).pack(anchor="w", pady=(10, 0))

rodape = ttk.Label(
    container,
    text="Projeto simples para portfólio em Python. Aceita contas misturadas na calculadora básica.",
    font=("Segoe UI", 9)
)
rodape.pack(anchor="w", pady=(10, 0))

atualizar_historico()
janela.mainloop()
