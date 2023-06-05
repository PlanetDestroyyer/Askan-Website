import streamlit as st


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
    st.title("Welcome to the page")

def style():
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

style()
main()
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Sample data
data = {
    'Daily Use of Website': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'Date of Inspection': ['2023-01-02', '2023-01-04', '2023-01-06', '2023-01-07', '2023-01-09']
}

st.set_option('deprecation.showPyplotGlobalUse', False)
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
cal_data = df['Date of Inspection'].dt.day.tolist()
cal = st.empty()
cal.calendar(datetime.now().date(), cal_data)


