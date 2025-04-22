import pandas as pd
import plotly.express as px
import streamlit as st

def load_data():
    ev_url = "https://api.iea.org/evs?parameters=EV%20sales&category=Historical&mode=Cars&csv=true"
    ev_df = pd.read_csv(ev_url)
    # filter the dataframe to get the rows where parameter = "EV sales" and "EV sales share"
    ev_sales_df = ev_df[ev_df["parameter"] == "EV sales"]
    ev_sales_share_df = ev_df[ev_df["parameter"] == "EV sales share"]

    # Drop the unnecessary columns on both dataframes
    ev_sales_df = ev_sales_df.drop(columns=["category", "mode", "unit", "parameter"])
    ev_sales_share_df = ev_sales_share_df.drop(columns=["category", "mode", "unit", "parameter", "powertrain"])

    return ev_sales_df, ev_sales_share_df

def show_bar_chart(df, x, y, color):
    # Assuming world_sales_df is already defined
    fig = px.bar(df, x=x, y=y, color=color)

    # Disable zoom and other interactions
    fig.update_layout(
        dragmode=False,
    )
    fig.update_xaxes(fixedrange=True)
    fig.update_yaxes(fixedrange=True)

    # Display the chart
    st.plotly_chart(fig)