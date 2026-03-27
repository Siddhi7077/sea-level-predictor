import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10,6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Line of best fit (all data)
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = range(1880, 2051)
    y_pred = res.intercept + res.slope * pd.Series(x_pred)
    ax.plot(x_pred, y_pred, 'r', label='Best fit line (1880-2050)')

    # Line of best fit (from 2000 onwards)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_recent = range(2000, 2051)
    y_recent = res_recent.intercept + res_recent.slope * pd.Series(x_recent)
    ax.plot(x_recent, y_recent, 'g', label='Best fit line (2000-2050)')

    # Labels and title
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.legend()

    # Save plot
    fig.savefig('sea_level_plot.png')
    return fig
