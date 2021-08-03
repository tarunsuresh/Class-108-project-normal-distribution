import csv
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as pe

df=pd.read_csv("data.csv")

fig=ff.create_distplot([df["Avg Rating"].tolist()],["Avg Rating"],show_hist=False)

#fig=pe.histogram(df,x="Mobile Brand",y="Avg Rating",)

fig.show()
