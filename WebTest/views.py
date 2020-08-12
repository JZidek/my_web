import bokeh
from bokeh.plotting import figure, show
from bokeh.embed import components
from django.shortcuts import render
import pandas as pd
import numpy as np
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.transform import factor_cmap
import random



    
def start(request):

    return render(request, 'WebTest/start.html', dict())

def plc(request):
    obr = ['webtest/st7_1.jpg','webtest/t_1.jpg','webtest/t_2.jpg', 'webtest/t_3.jpg', 'webtest/l_1.jpg']
    i = random.randint(0,4)   
    source = obr[i]
    return render(request, 'WebTest/plc.html', dict(s=source))
  
def hmi(request):
    obr = ['webtest/wincc_hmi.jpg','webtest/tia_hmi.jpg','webtest/eb.jpg', 'webtest/cw.jpg']
    i = random.randint(0,3)   
    source = obr[i]
    return render(request, 'WebTest/hmi.html', dict(s = source))

def data(request):
    # LINEGRAF
    data_line = pd.read_csv("C:\\naucse-python\\ITNet\\Django\\mysite\\WebTest\\TeplotyLakovna.csv")
    PG1 = []
    PG2 = []
    PG3 = []
    LG1 = []
    LG2 = []
    LG3 = []
    x_line = []
    for i in range(20):
        x_line.append(data_line["datum"][i])
        PG1.append(data_line["PG1"][i])
        PG2.append(data_line["PG2"][i])
        PG3.append(data_line["PG3"][i])
        LG1.append(data_line["LG1"][i])
        LG2.append(data_line["LG2"][i])
        LG3.append(data_line["LG3"][i])
    x_line = pd.to_datetime(x_line, format='%d.%m.%Y_%H:%M', errors='coerce')
    p = figure(frame_width=700, frame_height=350, background_fill_color="rgb(215, 215, 215)", x_axis_type="datetime")
    p.line(x_line,PG1, color='red', line_width=2)
    p.line(x_line,PG2, color='blue',line_width=2)
    p.line(x_line,PG3, color='green',line_width=2)
    p1 = figure(frame_width=700, frame_height=350, background_fill_color="rgb(215, 215, 215)", x_axis_type="datetime")
    p1.line(x_line,LG1, color='red', line_width=2)
    p1.line(x_line,LG2, color='blue',line_width=2)
    p1.line(x_line,LG3, color='green',line_width=2)
    script, div = components(p)
    script1, div1 = components(p1)

    # BARGRAF
    data_bar = pd.read_csv("C:\\naucse-python\\ITNet\\Django\\mysite\\WebTest\\vynos.csv")
    x = data_bar["datum"]
    s1 = data_bar["silo1"]
    s2 = data_bar["silo2"]
    sila = ["silo1", "silo2"]
    palette = ["purple", "blue"]
    x = [(datum, silo) for datum in x for silo in sila]
    counts = sum(zip(data_bar["silo1"], data_bar["silo2"]), ())  
    source = ColumnDataSource(data=dict(x=x, counts=counts))
    p_bar = figure(x_range=FactorRange(*x), plot_width=1025, plot_height=300,
           toolbar_location=None, tools="")
    p_bar.vbar(x='x', top='counts', width=0.9, source=source, line_color="white",fill_color=factor_cmap('x', palette=palette, factors=sila, start=1, end=2))
    p_bar.y_range.start = 0
    p_bar.x_range.range_padding = 0.1
    p_bar.xaxis.major_label_orientation = 1
    p_bar.xgrid.grid_line_color = None
    script_bar, div_bar = components(p_bar)

    # TABULKA LINEGRAF
    head = data_line.head(1)
    length = data_line.shape[0]
    data = []
    for i in range(30):
        s = []
        for j in data_line.loc[i]:
            s.append(j) 
        data.append(s)

    # TABULKA BARGRAF
    head_bar = data_bar.head(1)
    data_b = []
    for i in range(len(data_bar["datum"])):
        t = []
        for j in data_bar.loc[i]:
            t.append(j)
        data_b.append(t)
    
    return render(request, 'WebTest/data.html', dict(script = script, script1=script1, div = div, div1=div1, script_bar=script_bar, div_bar=div_bar, head=head, data=data, head_bar=head_bar, data_bar=data_b)) 
        
def kontakt(request):
    return render(request, 'WebTest/kontakt.html', dict())

