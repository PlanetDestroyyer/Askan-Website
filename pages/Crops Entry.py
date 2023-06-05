import streamlit as st
import pandas as pd

def append(appendind_data):
    df = pd.DataFrame(appendind_data)
    df.to_csv('new1.csv', mode='a', index=False, header=False)

def main():
    st.title("Crop Entry.py")
    st.subheader("Crop Details")
    region = st.text_input("Enter your region (For India Only):")
    area_working = st.number_input("Area of working (in square meters):", min_value=0.0)
    avg_temp_min = st.number_input("Average Temperature - Minimum (°C):", min_value=-1.0, max_value=100.0, value=0.0)
    avg_temp_max = st.number_input("Average Temperature - Maximum (°C):", min_value=-1.0, max_value=100.0, value=0.0)
    crop_name = st.text_input("Name of Crop:")
    crop_breed = st.text_input("Breed of Crop:")
    avg_height = st.number_input("Average Height of Crops (in meters):", min_value=0.0)
    seed_source = st.selectbox("Select Seed Source:", ("Home Made", "Purchased from Provider"))

    if st.button("Save"):
        # Create a dictionary to store the crop details
        # crop_details = {
        #     df['Region']: region,
        #     df['Area working']: area_working,
        #     df['Avergae Temp Min']: avg_temp_min,
        #     df: avg_temp_max,
        #     : crop_name,
        #     : crop_breed,
        #     : avg_height,
        #     df['seed source']: seed_source
        
        # Save the crop details in a CSV file
        append(crop_details)

        st.success("Crop details saved successfully!")

    # Check if the CSV file exists

    # If the file exists, load the existing data and append the new crop details
    # if file_exists is not None:
    #     with open(csv_file, "a") as f:
    #         writer = csv.DictWriter(f, fieldnames=crop_details.keys())
    #         writer.writerow(crop_details)
    # else:
    #     # If the file doesn't exist, create a new file and write the crop details
    #     with open(csv_file, "w") as f:
    #         writer = csv.DictWriter(f, fieldnames=crop_details.keys())
    #         writer.writeheader()
    #         writer.writerow(crop_details)
def hideAll():
    hide = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """   
    st.markdown(hide,unsafe_allow_html=True)
hideAll()

def style():
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


style()
main()
