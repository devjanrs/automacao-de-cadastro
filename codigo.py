# Importacoes
import pyautogui
import time

pyautogui.PAUSE = 0.3

# Abrir o navegador
pyautogui.press("win")
pyautogui.write("opera") # aqui digita-se o nome do navegador
pyautogui.press("enter")

# Entrar no site
pyautogui.click(x=730, y=1882) # foi necessario para poder abrir o navegador
time.sleep(3)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

# Digitar usuario e senha
pyautogui.click(x=1339, y=782) #selecionar o campo e-mail
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua senha")
pyautogui.press("tab")
pyautogui.press("enter")

# Importar a base de produtos para cadastro
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

# Cadastrar produtos

for linha in tabela.index:
    pyautogui.click(x=1328, y=541) # Clicar no campo do codigo do produto

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab") # Para pular para o proximo campo
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    pyautogui.press("enter") # Para cadastrar o produto (enviar)
    pyautogui.scroll(5000) #para scrollar a tela para cima

# O processo se repete ate o ultimo item