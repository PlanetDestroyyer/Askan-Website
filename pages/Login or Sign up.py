import streamlit as st
import pandas as pd 
from streamlit_extras.switch_page_button import switch_page
from pages.Profile import show_profile

session = st.session_state
def main():
    st.title("Login Or Resigter")
    page = st.sidebar.selectbox("Select Page", ("Login", "Registration"))

    if page == "Login":
        login()
    elif page == "Registration":
        signup()

def append(appendind_data):
    df = pd.DataFrame(appendind_data)
    df.to_csv('new1.csv', mode='a', index=False, header=False)

df = pd.read_csv('new1.csv')

def login():
    df = pd.read_csv('new1.csv', sep=',')
    try:
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_button = st.button("Login")

        if login_button:
            if username in df['Name'].tolist() and password in df['Password'].tolist():
                st.success("U have successfully entered into the app")
                
                switch_page('Home')
            else:
                st.write("Error")
    except:
        pass

def signup():
    try:
        st.subheader("Registration")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        Area_Working = st.number_input("Area_Working:")
        Country = st.text_input("Country", placeholder="Currently Selected India")
        Gender = st.selectbox("Gender:", ("Male", "Female"))
        Qualification = st.selectbox("Qualification:", ("Educated (10th pass)", "Uneducated"))
        Purpose = st.selectbox("Purpose:", ("Domestic", "Commercial"))
        Message = st.selectbox("Allow Personalized Message:", ("Yes", "No"))
        Number = st.text_input("Mobile Number :")
        Email = st.text_input("Email :")
        signup_button = st.button("Register")
        
        if password == confirm_password:
            st.success("Thanks for Registering")
            append({"Name": [username], "Password": [password], "Region": [Country], "Area Working": [Area_Working], "Gender": [Gender], "Qualification": [Qualification], "Purpose": [Purpose], "Message": [Message], "Mobile": [Number], "Email": [Email]})
            session['username'] = username  # Store the registered username
            show_profile(username)
        else:
            st.write("Password and Confirm Password should be the same")
    except:
        pass

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

if __name__ == "__main__":
    main()                                                                                                                       
    
