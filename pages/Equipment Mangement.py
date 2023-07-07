import streamlit as st
import base64
import time

from streamlit_option_menu import option_menu

st.set_page_config(page_title="Equipment Mangement",page_icon="logo.jpg",layout="centered",initial_sidebar_state="auto",menu_items=None)
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
def hideAll():
    hide = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """   
    st.markdown(hide,unsafe_allow_html=True)

def remove_underline():
    st.markdown(
        """
        <style>
        a {
            text-decoration: none;
            color : black;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
hideAll()
def main():
    st.title("Welcome to the Equip page")
def style():
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

# # Read and display temperature data
# def temp():
#     try:
#         ser = serial.Serial('COM3', 9600) 
#         while True:
#             data = ser.readline().decode('utf-8').rstrip()
#             if data:
#                 values = data.split(',')
#                 if len(values) == 2:
#                     Temp = values[0]
#                     Humid = values[1]
#                     st.write("Temprature : ",Temp,"C")
#                     st.write("Himidity : ", Humid,"%")
#                     time.sleep(1)
#     except:
#         st.write("The Sensor is not Conneted or U have open the same tab agian so close it and try again.")

POWER_PIN = 7
SIGNAL_PIN = 5

value = 0  # variable to store the sensor value


def loop():
    print("Turning the sensor ON")
    time.sleep(1000)  # Simulate power-up delay
    print("Reading sensor value")
    value = simulate_sensor_reading()  # Simulate sensor reading
    print("Sensor value:", value)
    print("Turning the sensor OFF")
    time.sleep(1000)  # Simulate power-down delay

def simulate_sensor_reading():
    # Simulate the analog reading from the sensor
    return int(time.time() * 1000) % 1024

if __name__ == "_main_":
    while True:
        main()
        loop()
        time.sleep(1000)  

