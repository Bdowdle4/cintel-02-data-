# These are the packages you need for your histograms
import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins # This package provides the Palmer Penguins dataset

# Get the data
# ALWAYS familiarize yourself with the dataset you are working with first

# Use the built-in function to load the Palmer Penguins dataset
penguins_df = palmerpenguins.load_penguins()

# Define User Interface (ui)
ui.page_opts(title="Brittany's Data About Spectacular Penguins", fillable=True)
with ui.layout_columns():

#These will create the visuals for your histograms    
    @render_plotly
    def plot1():
        return px.histogram(px.data.tips(), y="tip")

    @render_plotly
    def plot2():
        return px.histogram(px.data.tips(), y="total_bill")
