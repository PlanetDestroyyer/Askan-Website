import serial
import time

# Set up the serial connection
ser = serial.Serial('COM5', 9600)  # Replace 'COM3' with the correct port for your Arduino
time.sleep(2)  # Wait for the serial connection to be established

# Read and display temperature data
def main():
    while True:
        data = ser.readline().decode('utf-8').rstrip()
        if data:
            print('Temperature:', data, '°C')

# Close the serial connection
if __name__ == "__main__":
    main()
    ser.close()
