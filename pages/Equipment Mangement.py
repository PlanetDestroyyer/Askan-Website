import serial
import time

# Initialize serial communication
ser = serial.Serial('COM4', 9600)  # Replace 'COM4' with your Arduino's serial port

# Thresholds
lowerThreshold = 310
upperThreshold = 510

# Function to print water level message
def print_water_level_message(level):
    if level <= lowerThreshold:
        print("Water Level: need more water")
    elif lowerThreshold < level <= upperThreshold:
        print("Water Level: need water")
    else:
        print("Water Level: full")

# Loop
while True:
    # Read water level from the Arduino
    line = ser.readline().decode().rstrip()

    if line:
        try:
            waterLevel = int(line)  # Parse the received line as an integer
            print_water_level_message(waterLevel)
        except ValueError:
            print(line)  # Print any non-integer lines received from the Arduino
    else:
        print("The sensors are not connected or reload the website")

    time.sleep(1)

