import streamlit as st
from gpiozero import MCP3008
from RPLCD import CharLCD
from time import sleep

adc = MCP3008(channel=0)
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2)

st.title("Water Level Monitoring")

while True:
    value = adc.value

    st.subheader("Analog Value")
    st.write(f"Value: {value:.2f}")

    st.subheader("Water Level")
    if value == 0:
        st.write("Water Level: Empty")
    elif 0 < value < 0.34:
        st.write("Water Level: LOW")
    elif 0.34 <= value < 0.51:
        st.write("Water Level: Medium")
    else:
        st.write("Water Level: HIGH")

    # Update the LCD
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string(f"Value: {value:.2f}")
    lcd.cursor_pos = (1, 0)
    if value == 0:
        lcd.write_string("W Level: Empty")
    elif 0 < value < 0.34:
        lcd.write_string("W Level: LOW")
    elif 0.34 <= value < 0.51:
        lcd.write_string("W Level: Medium")
    else:
        lcd.write_string("W Level: HIGH")

    sleep(1)
