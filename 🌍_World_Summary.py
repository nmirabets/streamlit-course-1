import streamlit as st
import plotly.express as px
from utils import load_data, show_bar_chart

# Load the data
ev_sales_df, ev_sales_share_df = load_data()

# Page Config
st.set_page_config(
    page_title="EV Adoption Tracker",
    layout="centered", # or wide
    page_icon="🚗", # choose your favorite icon
    initial_sidebar_state="collapsed" # or expanded
)

# Title
st.title("🚗 EV Adoption Tracker")

# Subheader
st.subheader("🌍 World Summary")

# Expander with datasource expalanation IEA
with st.expander("💡 Where does the data come from?", expanded=False):
    st.write("The data for this app is sourced from the IEA EV Sales dataset.")
    st.write("The dataset can be found [here](https://www.iea.org/data-and-statistics/data-tools/global-ev-data-explorer).")

# Metrics

col1, col2, col3 = st.columns(3)

card1 = col1.container(border=True)
card2 = col2.container(border=True)
card3 = col3.container(border=True)

card1.metric("Metric Name", "42%", 2)

card2.metric("Metric Name", "42%", 2)

card3.metric("Metric Name", "42%", 2)

# World Sales Chart

st.subheader("📊 World Sales")

st.divider()

world_sales_df = ev_sales_df[ev_sales_df["region"] == "World"]

show_bar_chart(world_sales_df, "year", "value", "powertrain")
