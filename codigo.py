#Passo 1 - Entrar no sistema da empresa.
#    Link: https://dlp.hashtagtreinamentos.com/python/intensivao/login

#Passo 2 - Fazer login
#Passo 3 - Pegar / Importar a base de dados
#Passo 4 - Cadastrar um produto
#Passo 5 - Repetir o passo 4 até cadastrar todos os produtos.

# pip install pyautogui
# pip install pandas

import pyautogui # ferramenta que automatiza o mouse, teclado e tela. 
import time

# pyautogui.click : clicar com o mouse
# pyautogui.write : escrever um texto
# pyautogui.press : apertar uma tecla do teclado
# pyautogui.hotkey : combinação de teclas
# pyautogui.scroll : rolar a tela para cima ou para baixo.

pyautogui.PAUSE = 0.3 # a cada comando do pyautogui ele vai dar uma pausa.

# Passo 1 - Entrar no sistema da empresa.
 # Abrir o navegador
pyautogui.press("win") 
pyautogui.write("chrome")
pyautogui.press("enter")

 # Entrar no link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3) # vai esperar o segundos APENAS nesse lugar.

# Passo 2 - Fazer o login no sistema. 
# selecionar o campo de email
pyautogui.click(x=725, y=372)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("testeautomatizacao@gmail.com")

 # Passar para o campo de senha
pyautogui.press("tab")
pyautogui.write("minha senha")

pyautogui.click(x=951, y=530)

time.sleep(3)

#Passo 3 - Pegar / Importar a base de dados
import pandas as pd # Ferramenta para trabalhar com base de dados (CSV. SQL...)

tabela = pd.read_csv("produtos.csv")

print(tabela)

#Passo 4 - Cadastrar um produto
# Para cada linha da minha tabela, quero executar todo esse código:
# index: é uma lista com todas as linhas da minha tabela

for linha in tabela.index: 
    # codigo
    pyautogui.click(x=834, y=257)
    pyautogui.hotkey("ctrl", "a")  # Selecionar todo o texto
    pyautogui.press("backspace")  # Apagar o texto selecionado

    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    # marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(marca)
    # tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(tipo)
    # categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.press("tab")
    pyautogui.write(categoria)
    # preço_unitario
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write(preco)
    # custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.press("tab")
    pyautogui.write(custo)
    # obs
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))

    # clicar no botão de enviar
    time.sleep(1)  # Pequeno atraso antes do clique
    pyautogui.click(x=871, y=918)  # Coordenadas do botão "Enviar"
    time.sleep(1)  # Atraso após o clique para garantir o registro

#Passo 5 - Repetir o passo 4 até cadastrar todos os produtos.