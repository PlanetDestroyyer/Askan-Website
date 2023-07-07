import streamlit as st
import pandas as pd
import base64
import sqlite3
st.set_page_config(page_title="Crops Entry",page_icon="logo.jpg",layout="wide",initial_sidebar_state="auto",menu_items=None)
# Establish a connection to the SQLite database
conn = sqlite3.connect('crop_data.db')

# Create a table to store the crop details
conn.execute('''
    CREATE TABLE IF NOT EXISTS crops (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        region TEXT,
        area_working REAL,
        avg_temp_min REAL,
        avg_temp_max REAL,
        crop_name TEXT,
        crop_breed TEXT,
        avg_height REAL,
        seed_source TEXT
    )
''')
def add_bg_from_local(image_file):
    with open(image_file, "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode("utf-8")
    return f"data:image/{image_file.split('.')[-1]};base64,{encoded_string}"

def run_app():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background:url({add_bg_from_local("bg.jpeg")});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
run_app()
def insert_crop_details(username, region, area_working, avg_temp_min, avg_temp_max, crop_name, crop_breed, avg_height, seed_source):
    conn.execute('''
        INSERT INTO crops (username, region, area_working, avg_temp_min, avg_temp_max, crop_name, crop_breed, avg_height, seed_source)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (username, region, area_working, avg_temp_min, avg_temp_max, crop_name, crop_breed, avg_height, seed_source))
    conn.commit()

def main():
    st.title("Crop Entry.py")
    st.subheader("Crop Details")
    
    # Retrieve the username from the session state
    session_state = get_session_state()
    username = session_state['username']
    
    region = st.text_input("Enter your region (For India Only):")
    area_working = st.number_input("Area of working (in square meters):", min_value=0.0)
    avg_temp_min = st.number_input("Average Temperature - Minimum (°C):", min_value=-1.0, max_value=100.0, value=0.0)
    avg_temp_max = st.number_input("Average Temperature - Maximum (°C):", min_value=-1.0, max_value=100.0, value=0.0)
    crop_name = st.text_input("Name of Crop:")
    crop_breed = st.text_input("Breed of Crop:")
    avg_height = st.number_input("Average Height of Crops (in cm):", min_value=0.0)
    seed_source = st.selectbox("Select Seed Source:", ("Home Made", "Purchased from Provider"))

    if st.button("Save"):
        insert_crop_details(username, region, area_working, avg_temp_min, avg_temp_max, crop_name, crop_breed, avg_height, seed_source)
        st.success("Crop details saved successfully!")

def hideAll():
    hide = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """   
    st.markdown(hide, unsafe_allow_html=True)

def get_session_state():
    if 'session_state' not in st.session_state:
        st.session_state['session_state'] = {}
    return st.session_state['session_state']

if __name__ == "__main__":
    hideAll()
    main()
