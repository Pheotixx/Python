import csv
import numpy as np
import plotly.express as px

with open('CupsOfCoffee vs SleepHours.csv') as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df, x = "Coffee in ml", y = "sleep in hours")

    fig.show()

def getDataSource(data_path):
    sleep = []
    coffee_cups = []

    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)

        for i in df:
            sleep.append(float(i["Coffee in ml"]))
            coffee_cups.append(float(i["sleep in hours"]))
            
    return{"x":coffee_cups, "y": sleep}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("The correlation is ",correlation[0,1])

def setup():
    data_path = "./CupsOfCoffee vs SleepHours.csv"

    data_source = getDataSource(data_path)
    findCorrelation(data_source)

setup()
