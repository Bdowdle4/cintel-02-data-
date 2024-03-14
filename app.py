# These are the packages you need for your histograms
import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly, render_widget
from palmerpenguins import (
    load_penguins,
)  # This package provides the Palmer Penguins dataset
import pandas as pd
import seaborn as sns
import plotly.graph_objects as go
from shiny import reactive, render, req

# Get the data
# ALWAYS familiarize yourself with the dataset you are working with first

# Use the built-in function to load the Palmer Penguins dataset
penguins = load_penguins()

# Define User Interface (ui) and add a fun title
ui.page_opts(title="Brittany's Data About Spectacular Penguins", fillable=True)

# Add a Shiny UI sidebar that will change based on the inputs
with ui.sidebar(open="open"):
    # Use ui.HTML() to include an h2 header with custom styling
    ui.HTML('<h2 style="font-style: italic;">Sidebar</h2>')
    ui.input_selectize(
        "selected_attribute",
        "Select an attribute below:",
        ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"],
    )
    ui.input_numeric(
        "plotly_bin_count", "Plotly Histogram Bins", value=20, min=1, max=100
    )
    ui.input_slider("seaborn_bin_count", "Seaborn Bins", min=1, max=50, value=10)
    ui.input_checkbox_group(
        "selected_species_list",
        "Filter by Species",
        choices=["Adelie", "Gentoo", "Chinstrap"],
        selected=["Adelie", "Chinstrap"],
        inline=True,
    )

    ui.hr()
    ui.a(
        "Brittany's GitHub Repo P2",
        href="https://github.com/Bdowdle4/cintel-02-data-",
        target="_blank",
    )

    
    with ui.navset_pill(id="tab"):
        with ui.nav_panel("Data Table"):

            @render.data_frame
            def penguins_df():
                return render.DataTable(penguins)

        with ui.nav_panel("Data Grid"):

            @render.data_frame
            def penguins_df2():
                return render.DataGrid(penguins)

    # Plotly Histogram
    with ui.navset_card_tab(id="tab"):
        with ui.nav_panel("Plotly Histogram"):

            @render_plotly
            def plotly_histogram():
                plotly_hist = px.histogram(
                    data_frame=penguins,
                    x=input.selected_attribute(),
                    nbins=input.plotly_bin_count(),
                    color="species",
                ).update_layout(
                    title="Plotly Penguins Data",
                    xaxis_title="Selected Attribute",
                    yaxis_title="Count",
                )
                return plotly_hist

        with ui.nav_panel("Seaborn Histogram"):

            @render.plot
            def seaborn_histogram():
                seaborn_hist = sns.histplot(
                    data=penguins,
                    x=input.selected_attribute(),
                    bins=input.seaborn_bin_count(),
                )
                seaborn_hist.set_title("Seaborn Penguin Data")
                seaborn_hist.set_xlabel("Selected Attribute")
                seaborn_hist.set_ylabel("Count")

        with ui.nav_panel("Plotly Scatterplot"):
            ui.card_header("Plotly Scatterplot: Species")

            @render_plotly
            def plotly_scatterplot():
                plotly_scatter = px.scatter(
                    penguins,
                    x="bill_depth_mm",
                    y="bill_length_mm",
                    color="species",
                    size_max=8,
                    labels={
                        "bill_depth_mm": "Bill Depth (mm)",
                        "bill_length_mm": "Bill Length(mm)",
                    },
                )
                return plotly_scatter


