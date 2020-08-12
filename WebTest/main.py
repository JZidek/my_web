import pandas as pd
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.plotting import figure

"""
df = pd.DataFrame({'year': [2015, 2016],
                   'month': [2, 3],
                   'day': [4, 5]})
data = pd.read_csv("TeplotyLakovna.csv")
year = []
month = []
day = []
hour = []
minute = []
time = []
for i in range(20):
    year.append(data["datum"][i][6:10]) 
    month.append(data["datum"][i][3:6])
    day.append(data["datum"][i][:3])
    hour.append(data["datum"][i][11:13])
    minute.append(data["datum"][i][14:])
    time.append(data["datum"][i])
print(time)
dt = pd.DataFrame({'year': year, 'month':month,'day':day, 'hour':hour, 'minute':minute})
#print(dt)
dt = pd.to_datetime(time, format='%d.%m.%Y_%H:%M', errors='coerce')
print(dt)
"""

data = pd.read_csv("C:\\naucse-python\\ITNet\\Django\\mysite\\WebTest\\vynos.csv")
for i in range(data.shape[0]):
    for j in data.loc[i]:
        print(j)
