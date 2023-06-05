import streamlit as st
import pandas as pd 
from streamlit_extras.switch_page_button import switch_page
def main():
    st.title("Login and Sign-up")

    # Page selection
    page = st.sidebar.selectbox("Select Page", ("Login", "Sign-up"))

    if page == "Login":
        login()
    elif page == "Sign-up":
        signup()

def append(appendind_data):
    df = pd.DataFrame(appendind_data)
    df.to_csv('new1.csv', mode='a', index=False, header=False)

# df = pd.read_csv('new1.csv')

def login():
    df = pd.read_csv('new1.csv', sep=',')
    try:
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_button = st.button("Login")

        if login_button:
            # userList = 
            # print(df['Name'].tolist())
            if username in df['Name'].tolist() and password in df['Password'].tolist():
                st.success("U have successfully entered into the app")
                switch_page('Home')
            else:
                st.write("Error")
    except:
        pass

def signup():
    try:
        st.subheader("Sign-up")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        signup_button = st.button("Sign-up")
        if password == confirm_password:
            if signup_button:
                st.success("Thanks for Signing")
                append({"Name": [username],"Password":[password]})
                switch_page('Home')
            else:
                st.write("Please fill form")
        else:
            st.write("Password and Confirm Password should be same")
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
    