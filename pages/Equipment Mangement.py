import streamlit as st
# import serial
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
# def style():
#     with open('style.css') as f:
#         st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

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
# def Water_level():  
#     # try:
# <<<<<<< HEAD
#     ser = serial.Serial('COM3', 9600)  # Replace '/dev/ttyUSB0' with your Arduino's serial port
# =======
#     ser = serial.Serial('COM7', 9600)  # Replace '/dev/ttyUSB0' with your Arduino's serial port
# >>>>>>> d0c6f43d9069d66bc599f501b420ab81c95f5f0d
#     # Thresholds
#     lowerThreshold = 310
#     upperThreshold = 510
#     # Function to print water level message
#     def print_water_level_message(level):
#         if level <= lowerThreshold:
#             st.write("Water Level: need more water")
#         elif lowerThreshold < level <= upperThreshold:
#             st.write("Water Level: need water")
#         else:
#             st.write("Water Level: full")
#     # Loop
#     while True:
#         # Read water level from the Arduino
#         line = ser.readline().decode().rstrip()
#         try:
#             waterLevel = int(line)  # Parse the received line as an integer
#             print_water_level_message(waterLevel)
#         except ValueError:
#             st.write(line) 
#         time.sleep(1)
#     # except:
#     #     st.write("The Sensor is not Conneted or U have open the same tab agian so close it and try again.")
   
# # Close the serial connection
# style()
main()

# temp()
# Water_level()
