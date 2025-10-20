import pyautogui
import time


pyautogui.PAUSE = 1.5
#Passo 1: entrar no sistema da empresa - site da empresa https://dlp.hashtagtreinamentos.com/python/intensivao/login
#abrir o chrome e digitar o site.
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

#Passo 2: Fazer login e preencher email
pyautogui.click(x=534, y=408)
pyautogui.write("juninho@hotmail.com")
pyautogui.press("tab")
pyautogui.write("senha123")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=898, y=361)

#Passo 3: Importar a base de dados.
import pandas as pd
tabela = pd.read_csv("produtos.csv")
print(tabela)

#Passo 4: Cadastrar 1 produto
for linha in tabela.index:
    pyautogui.click(x=432, y=288)
    # pegar da tabela o campo que a gente quer preencher
    codigo = tabela.loc[linha , "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha , "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha , "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha , "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha , "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha , "custo"]))
    pyautogui.press("tab")
    if not pd.isna: # Se NAO tiver preenchimento, somente pular. Se tiver, escreve.
        pyautogui.write(str(tabela.loc[linha , "obs"]))
    
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(10000)



#Passo 5: Repetir para todos os produtos