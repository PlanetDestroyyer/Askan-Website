# # profile.py

import streamlit as st

def show_profile(username):
    if username in df['Name'].tolist() and password in df['Password'].tolist():
        # Retrieve user's data based on the username
        # Display the profile information
        st.write("Username:", username)
        # Add more fields as necessary


def profile():
    show_profile(session['username'])

if username in df['Name'].tolist() and password in df['Password'].tolist():

    session['username'] = name  # Store the logged-in username
    st.success("You have successfully entered into the app")
    show_profile(name)
