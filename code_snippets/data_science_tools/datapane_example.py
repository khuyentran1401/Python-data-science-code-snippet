# pip install datapane 
# pip install plotly

import datapane as dp 
import pandas as pd 
import numpy as np 
import plotly.express as px

# Scripts to create df and chart 
df = px.data.gapminder()

chart = px.scatter(df.query("year==2007"), x="gdpPercap", y="lifeExp",
	         size="pop", color="continent",
                 hover_name="country", log_x=True, size_max=60)

# Once you have the df and the chart, simply use
r = dp.Report(
    dp.Text("my simple report"), # add description
    dp.DataTable(df), # create a table
    dp.Plot(chart) # create a chart
)

# Publish your report
r.publish(name='example', visibility = dp.Visibility.PUBLIC)