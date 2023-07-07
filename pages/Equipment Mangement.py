import streamlit as st
import base64
import time

from streamlit_option_menu import option_menu

st.set_page_config(page_title="Equipment Mangement",page_icon="logo.jpg",layout="centered",initial_sidebar_state="auto",menu_items=None)

def style():
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

POWER_PIN = 7
SIGNAL_PIN = 5

value = 0  # variable to store the sensor value

def simulate_sensor_reading():
    # Simulate the analog reading from the sensor
    return int(time.time() * 1000) % 1024

def loop():
    st.write("Turning the sensor ON")
    time.sleep(1000)  # Simulate power-up delay
    st.write("Reading sensor value")
    value = simulate_sensor_reading()  # Simulate sensor reading
    st.write("Sensor value:", value)
    st.write("Turning the sensor OFF")
    time.sleep(1000)  # Simulate power-down delay

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
def hideAll():
    hide = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """   
    st.markdown(hide,unsafe_allow_html=True)

    
def main():
    style()
    run_app()
    hideAll()
    st.title("Welcome to the Equip page")
 

