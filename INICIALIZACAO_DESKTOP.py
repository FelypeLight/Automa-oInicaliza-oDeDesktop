import pyautogui
from pyautogui import click, displayMousePosition, typewrite

from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import string
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import Select
import time

#teste primeiro branch

while pyautogui.onScreen(True):
            time.sleep(5)
            pyautogui.press("win")
            typewrite("edge")
            pyautogui.press("enter")
            time.sleep(5)

            # #WHATSAPP
            time.sleep(5)
            pyautogui.hotkey("w", "enter")
            
            #GEMINI // POST NO LINKEDIN
            pyautogui.hotkey('ctrl', 't')
            pyautogui.hotkey('g', 'e', 'm', 'enter', interval=1.00)
            typewrite("##Configuracoes: respostas com no maximo 500 tokens, economize o maximo de tokens possiveis.")
            pyautogui.hotkey("enter", interval=5.00)
            typewrite("##Instrucoes: Pesquise na Web as principais noticias atuais do mundo da Tecnologia da Informacao, e crie um Post sobre o assunto minha rede social profissional do Linkedin. ; ##Contexto: Preciso que meu Portfolio se mantenha atualizado, entao pretendo manter posts frequentes.; ##Atuacao:    ; ##Formatacao: Crie o texto do post em um quadro 'copia e cola' igual aos que você usa para demonstrar codigos de programacao para facilitar a copia; Crie o Post com linguagem formal seguindo as normas da Lingua Portuguesa;", interval=0.01)
            pyautogui.press('enter')
            time.sleep(20)
            typewrite("gere uma imagem ilustrativa para esta postagem")
            pyautogui.press('enter')
            

            pyautogui.hotkey('ctrl', 't') # nova guia( terceira) 
            pyautogui.typewrite("https://www.linkedin.com/feed/") # url do linkedin
            pyautogui.press('enter')
            time.sleep(10)
            click(1261, 418)
            click(484, 232, duration=5.00)
            #navegando entre abas navegador
            pyautogui.hotkey('ctrl', 'pageup')

            #de volta ao gemini para puxar imagem do post
            scroll = 1

            for scroll in range(10):
                pyautogui.press('down')
            
            time.sleep(60)
            pyautogui.moveTo(738, 453)
            pyautogui.dragTo(651, 17, button="left", duration=5.00)
            break               