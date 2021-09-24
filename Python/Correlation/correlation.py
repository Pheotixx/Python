import csv
import numpy as np
import plotly.express as px

with open('data.csv') as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df, x = "Size of TV", y = "Average time spent watching TV in a week (hours)")

    fig.show()

def getDataSource(data_path):
    size_of_tv = []
    average_time_spent = []

    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)

        for i in df:
            size_of_tv.append(float(i["Size of TV"]))
            average_time_spent.append(float(i["Average time spent watching TV in a week (hours)"]))
            
    return{"x": size_of_tv, "y": average_time_spent}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("The correlation is ",correlation[0,1])

def setup():
    data_path = "./data.csv"

    data_source = getDataSource(data_path)
    findCorrelation(data_source)

setup()


    