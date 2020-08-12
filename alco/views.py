from django.shortcuts import render
import pandas as pd
import bokeh
from bokeh.plotting import figure, show
from bokeh.embed import components
import numpy as np
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.transform import factor_cmap
from .models import Tesco


def fct(request):

    tsc = Tesco()
    tsc.update()

    tsleva = []
    tcena = []
    tnazev = []
    tshoda = []
    filtr = []
    sleva = ""
    cena = ""
    nazev = ""
    dat = []
    data = pd.read_csv("alco\\sources\\tab.csv")
    msg = ""

    if request.method == "POST":
        print("post")
        try:
            int(request.POST["sleva"])
            float(request.POST["cena"])
        except:
            msg = "zadej spravne udaje!!!"
        if request.POST["nazev"] != "":
            nazev = request.POST["nazev"]
        if request.POST["sleva"] != "":
            sleva = request.POST["sleva"]
        if request.POST["cena"] != "":
            cena = request.POST["cena"]
        


    for i,value in enumerate(data["sleva"]):
        if sleva != "" and (int(value.strip("%"))*-1) > int(sleva):
            tsleva.append(i)
        elif sleva == "":
            tsleva.append(i)

    for i,value in enumerate(data["nova_cena"]):
        if cena != "" and int(value) < int(cena):
            tcena.append(i)
        elif cena == "":
            tcena.append(i)
 
    for i,value in enumerate(data["nazev"]):
        if nazev != "" and value.lower().find(nazev.lower()) != -1:
            tnazev.append(i)
        elif nazev == "":
            tnazev.append(i)
                
    for i in tnazev:
        for j in tcena:
            if i == j:
                tshoda.append(i)
    for i in tshoda:
        for j in tsleva:
            if i==j:
                filtr.append(i)
        
    for i in filtr:
        s = []      
        s.append(data["nazev"][i])
        s.append(data["mira"][i])
        s.append(data["sleva"][i])
        s.append(data["nova_cena"][i])
        s.append(data["platnost"][i])
        dat.append(s)

    head = ["Nazev", "mira", "sleva", "cena", "plati do"]

    return render(request, 'alco/start.html', dict(head=head, data=dat))
