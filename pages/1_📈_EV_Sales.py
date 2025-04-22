import streamlit as st
from utils import load_data, show_bar_chart

# Load data
ev_sales_df, ev_sales_share_df = load_data()

# Title
st.title("📈 EV Sales")

st.divider()

# Subheader
st.subheader("🌍 EV Sales by Region")

region = st.selectbox("Select a region", ev_sales_df["region"].unique())

filtered_df = ev_sales_df[ev_sales_df["region"] == region]

show_bar_chart(filtered_df, "year", "value", "powertrain")

st.divider()