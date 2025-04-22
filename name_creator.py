import streamlit as st

# Page config
st.set_page_config(
    page_title="Superhero Name Creator",
    layout="wide", # or wide
    page_icon="🦸‍♂️🦸‍♀️", # choose your favorite icon
    initial_sidebar_state="collapsed" # or expanded
)

########################### USER INPUTS ##################################

# User inputs
st.title("What's Your Superhero Supername? 🦸‍♂️🦸‍♀️")

# Inputs for superhero name
favorite_color = st.text_input("", placeholder="What's your favorite color?")
favorite_animal = st.text_input("What's your favorite animal?", placeholder="Tiger")
lucky_number = st.number_input("Enter your lucky number:", min_value=1, step=1, value=7)

# Dropdown for superpower
superpower = st.selectbox("Choose your superpower:", 
                          ["Flying", "Invisibility", "Super Strength", "Mind Control", "Time Travel"])

# Generate superhero name on button click
if st.button("Generate My Superhero Name") == True:
    superhero_name = f"{favorite_color} {favorite_animal} of {lucky_number}"
    st.header(f"🦸 Your Superhero Name: {superhero_name}")
    st.write(f"🌟 Superpower: {superpower}")

    # Display a motto
    st.subheader("Your Superhero Motto:")
    st.write(f'"With great power comes great {superpower.lower()}!"')

