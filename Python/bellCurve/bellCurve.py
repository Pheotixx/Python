import csv
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv('data.csv')

fig = ff.create_distplot([df['Height(Inches)'].tolist()],["Height"],show_hist= False)

#fig1 = ff.create_distplot([df['Weight(Pounds)'].tolist()],["Weight"],show_hist= False)

fig.show()
#fig1.show()