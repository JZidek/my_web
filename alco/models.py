from django.db import models
from requests_html import HTMLSession, HTML
import pandas as pd
import datetime



class Tesco():
    def __init__(self):
        self.zdroje = []

    def update(self):
        self.zdroje = []
        try:
            print("try")
            with open("alco\\sources\\zdroje.csv", "r", encoding="UTF-8") as r:
                if str(r.readlines()[0].strip("\n")) == str(datetime.datetime.now().strftime("_%d%m")):
                    print("actual")
                else:
                    print("not actual")
        
                

        #stazeni zdroju na disk
                    
                    session = HTMLSession()
                    url = "https://nakup.itesco.cz/groceries/cs-CZ/promotions/all?superdepartment=19612&page=1"
                    stranka = session.get(url)
                    for i in stranka.html.find('.pagination--button'):
                        if i.text != "":
                            max_str = i.text
                        
                    print(max_str)
                        
                    for i in range(1,int(max_str)+1):
                        url = "https://nakup.itesco.cz/groceries/cs-CZ/promotions/all?superdepartment=19612&page="+str(i)
                        print(url)
                        stranka = session.get(url)
                        uloziste = "alco\\sources\\tesco_"+str(i)+".html"
                        self.zdroje.append(uloziste)
                        with open(uloziste, "w", encoding="UTF-8") as W:
                            for j in stranka.html.html:
                                W.write(j)
                    with open("alco\\sources\\zdroje.csv", "w", encoding="UTF-8") as W:
                        W.write(str(datetime.datetime.now().strftime("_%d%m\n")))
                        for i in self.zdroje:
                            W.write(i+"\n")

                    #vycet seznamu zdrojovych html na disku
                    
                    with open("alco\\sources\\zdroje.csv", "r", encoding="UTF-8") as R:
                        for i, value in enumerate(R.readlines()):
                            if i > 0:
                                self.zdroje.append(value.strip("\n"))
                    print(self.zdroje)
                    
                    with open("alco\\sources\\tab.csv", "w", encoding="UTF-8") as W:
                            W.write("nazev,mira,sleva,stara_cena,nova_cena,platnost\n")

                    
                    #prohledani vsech zdrojovych html a rozbor nalezenych prvku
                    for i in range(0,len(self.zdroje)):
                    
                        uloziste = self.zdroje[i]
                        soubor = open(uloziste, encoding="UTF-8")
                        obsah = soubor.read()
                        soubor.close()
                        html = HTML(html=obsah)
                        nr = 0
                        zapis = []
                        

                        for j in html.find('.product-details--content'): 
                            if j.text == "Více z kategorie":
                                pass
                            else:
                                if nr == 1:
                                    nr = 2
                                else:
                                    nr = 1
                                slova = []
                                slovo = ""
                                nazev = ""
                                mira = ""
                                sleva = ""
                                stara = ""
                                nova = ""
                                platnost = ""
                                text = ""
                                
                                if nr == 2:          
                                    for i in j.text:
                                        if i != " ":
                                            if i == ",":
                                                i = "."
                                            
                                            slovo = slovo + i              
                                        else:
                                            slova.append(slovo)
                                            slovo = ""
                                    slova.append(slovo)
                                    slovo = ""
                                    sleva = slova[0]
                                    stara = slova[3]
                                    nova = slova[5].strip("Cena")
                                    platnost = slova[11]
                                    zapis.append(sleva)
                                    zapis.append(stara)
                                    zapis.append(nova)
                                    zapis.append(platnost)
                                    for i in zapis:
                                        text = text + i + ","
                                    text = text.strip(",")+"\n"

                                    with open("alco\\sources\\tab.csv", "a", encoding="UTF-8") as A:
                                        A.write(text)
                                        zapis= []
                                    
                                #if j.text.find("pivo") != -1:
                                if nr == 1:
                                    for i in j.text:
                                        if i != " ":
                                            if i == ",":
                                                i = "."
                                            slovo = slovo + i              
                                        else:
                                            slova.append(slovo)
                                            slovo = ""
                                    slova.append(slovo)
                                        
                                    for i, value in enumerate(slova):
                                            if i < len(slova)-1:
                                                nazev = nazev + " " + value
                                            else:
                                                mira = value
                                    zapis.append(nazev)
                                    zapis.append(mira)
                    
        except:
            print("zdroje.csv nenalezeny")         
        
    def search(self):     
        pass

# Create your models here.
