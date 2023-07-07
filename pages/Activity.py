import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

st.set_page_config(page_title="Activity",page_icon="logo.jpg",layout="wide",initial_sidebar_state="auto",menu_items=None)
# Sample data
data = {
    'Daily Use of Website': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'Date of Inspection': ['2023-01-02', '2023-01-04', '2023-01-06', '2023-01-07', '2023-01-09']
}

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
# Hide unnecessary elements
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Convert date columns to datetime format
df['Daily Use of Website'] = pd.to_datetime(df['Daily Use of Website'])
df['Date of Inspection'] = pd.to_datetime(df['Date of Inspection'])

# Create a graph for daily website usage
st.subheader('Daily Website Usage')
plt.figure(figsize=(10, 6))
sns.lineplot(x=df['Daily Use of Website'], y=df.index, marker='o')
plt.xlabel('Date')
plt.ylabel('Days')
st.pyplot()

# Create a calendar to mark the dates of inspection
st.subheader('Inspection Dates')
selected_date = st.date_input('Select a date', datetime.now().date())
if selected_date in df['Date of Inspection'].dt.date.tolist():
    st.write(f"The selected date ({selected_date}) is an inspection date.")
else:
    st.write(f"The selected date ({selected_date}) is not an inspection date.")
