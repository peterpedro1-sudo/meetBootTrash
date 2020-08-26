import random as r
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
path = "c:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://www.google.com/accounts/Login?hl=pt-BR")

link = input("cole o link da reunião aqui:")
mensagem = "Madeira Jorge, madeira."
lista_de_mensagens = ("então isso se relaciona com o que nós vimos antes/faz bastante sentido agora/En"
                      "tão isso na verdade é bem interressante/gostei dessa materia/até que não é tão"
                      " dificíl/legal esse capitulo/e eu achando que essa matéria seria mais difcil/").split("/")
#lista_de_mensagens = ("celta preto vai chuve/É de capotar o corsa/veri nice/desculpa/").split("/")

def automatico():
    f = 0
    driver.get(link)
    vai = float(input("aperte 0 para começar: "))
    if vai == 0:
        while f <= 20:
            r.shuffle(lista_de_mensagens)
            for msg in lista_de_mensagens:
                time_down = r.randrange(60,300)
                time.sleep(time_down)
                caixa_de_texto = driver.find_element_by_name("chatTextInput")
                time.sleep(5)
                caixa_de_texto.click()
                caixa_de_texto.send_keys(msg)
                time.sleep(5)
                caixa_de_texto.send_keys(Keys.RETURN)

            f += 1

def comandos():
    driver.get(link)
    trava_de_seguranca = float(input("aperte 0 para começar"))
    reapeater = True
    if trava_de_seguranca == 0:
        while reapeater == True :
            chat = driver.find_element_by_class_name("vvTMTb")
            print(chat.text)
comandos()
