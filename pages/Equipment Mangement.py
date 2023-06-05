import streamlit as st
import serial
import time

from streamlit_option_menu import option_menu

st.set_page_config(page_title="Activity",page_icon="logo.jpg",layout="centered",initial_sidebar_state="auto",menu_items=None)
st.markdown("""
    """
    ,
    unsafe_allow_html=True)


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

# Read and display temperature data
def temp():
    try:
        ser = serial.Serial('COM5', 9600) 
        while True:
            data = ser.readline().decode('utf-8').rstrip()
            if data:
                values = data.split(',')
                if len(values) == 2:
                    Temp = values[0]
                    Humid = values[1]
                    st.write("Temprature : ",Temp,"C")
                    st.write("Himidity : ", Humid,"%")
                    time.sleep(1)
    except:
        st.write("The Sensor is not Conneted or U have open the same tab agian so close it and try again.")

# Close the serial connection
temp()
style()
main()
