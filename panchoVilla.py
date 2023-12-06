import slack
from slack_sdk import WebClient
from bs4 import BeautifulSoup 

import os
from pathlib import Path
from dotenv import load_dotenv

from fpdf import FPDF
import requests
import time
from datetime import date

env_path = Path('.') /'.env'
load_dotenv(dotenv_path=env_path)
pdf = FPDF('P', 'mm','Letter')

pdf.add_page()

pdf.set_font('Helvetica', "", 16)

client = WebClient(token=os.environ['SLACK_TOKEN'])

def aika():
    #PÄIVÄMÄÄRÄ TÄNÄÄN
    today = date.today()

    datetime_month = today.month
    datetime_day = today.day
    #YHDISTETÄÄN PÄIVÄ JA KUUKAUSI
    aika_tänään = (f'{datetime_day}.{datetime_month}')
    #MUUTETAAN STRING MUOTOON
    inputText = aika_tänään
    return inputText

def find_ruoka():
    #RUOKALISTA SIVUN KOKO HTML TEKSTI
    html_text = requests.get('https://www.lounaat.info/lounas/pancho-villa/lappeenranta').text
    #SIVULLE TEHTIIN JOTAIN XD
    soup = BeautifulSoup(html_text,'lxml')
    #LÖYDETÄÄN KAIKKI LI, MENU-LIST_ITEM, koska sieltä löytyy ruokalistan sisältö
    datas = soup.find_all('div', class_="item")
    
    
    
    
    
    
    
    
    
    for data in datas:
        data = data.text
        #JOS TÄMÄ PÄIVÄMÄÄRÄ LÖYTYY RUOKALISTALTA, ruokalista tulostuu slackkiin
        if aika() in data:
            print(data, end='')
            kaava = data
            
            kaava = data.replace('€', ' euro')
            pdf.cell(40,10,kaava)
            pdf.output('pdf_1.pdf')
            #lient.chat_postMessage(channel='#lunch-bot', text = (f'Cafe Hullu Lounas:\n{kaava}'))
            client.files_upload(
                channels="#lunch-bot",
                title="ruokalistaData",
                file="./pdf_1.pdf",
                initial_comment="Päivän ruokalista :",
            )
            break
        else:
            #VIIKONLOPPU TAI EI RUOKAILUA
            print("ei ruokailua")




    


        






find_ruoka()