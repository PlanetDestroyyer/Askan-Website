import streamlit as st
import pandas as pd


df = pd.read_csv('new1.csv')

def main():
    st.title("Profile Page")
    st.subheader("User Profile")
    st.session_state = False
    if st.session_state == False:
        name = st.text_input("Name:")
        email = st.text_input("Email:")
        phone_number = st.text_input("Mobile Number:")
        gender = st.selectbox("Gender:", ("Male", "Female"))
        qualification = st.selectbox("Qualification:", ("Educated (10th pass)", "Uneducated"))
        purpose = st.selectbox("Purpose:", ("Domestic", "Commercial"))
        allow_personalized_message = st.selectbox("Allow Personalized Message:", ("Yes", "No"))
    else:
        # df['Name'].tolist():

        name = df['Name']
        email = df['Email']
        phone_number = df['Mobile Number']
        gender = df['Name']
        qualification = df['Email']
        purpose = df["Email"]
        allow_personalized_message =df["Email"]

    if st.button("Save"):
        # Perform save action here
        st.write("Information saved successfully.")
        st.session_state.editable = False

    # if st.button("Edit"):
    #     st.session_state.editable = True

    # # Render the profile information as read-only if not editable
    # if not st.session_state.editable:
    #     st.text_input("Name:", value=name, key="name", disabled=True)
    #     st.text_input("Email:", value=email, key="email", disabled=True)
    #     st.text_input("Phone Number:", value=phone_number, key="phone_number", disabled=True)
    #     st.selectbox("Gender:", ("Male", "Female"), index=0 if gender == "Male" else 1, key="gender", disabled=True)
    #     st.selectbox("Qualification:", ("Educated (10th pass)", "Uneducated"), index=0 if qualification == "Educated (10th pass)" else 1, key="qualification", disabled=True)
    #     st.selectbox("Purpose:", ("Domestic", "Commercial"), index=0 if purpose == "Domestic" else 1, key="purpose", disabled=True)
    #     st.selectbox("Allow Personalized Message:", ("Yes", "No"), index=0 if allow_personalized_message == "Yes" else 1, key="allow_personalized_message", disabled=True)

    if st.button("Logout"):
        pass
        # Perform logout action here
        # session_state = st.session_state
        # if "logged_in" not in session_state:
        #     session_state["logged_in"] = False
    
        # if session_state["logged_in"]:
        #     # Display the main content for logged-in users
        #     st.title("Welcome to the App")
        #     # Your app content goes here
    
        #     # Logout button
        #     if st.button("Logout"):
        #         logout()
        # else:
        #     # Display the login form if the user is not logged in
        #     st.title("Login")
        #     username = st.text_input("Username")
        #     password = st.text_input("Password", type="password")
            
        #     if username == "your_username" and password == "your_password":
        #         # Set session state to logged-in
        #         session_state["logged_in"] = True
        #         st.success("Logged in successfully!")
        #     else:
        #         st.error("Invalid username or password")


def style():
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def hide_all():
    hide = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """   
    st.markdown(hide, unsafe_allow_html=True)

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

def app():
    hide_all()
    remove_underline()
    style()
    # if "editable" not in st.session_state:
    #     st.session_state.editable = True
    main()

if __name__ == '__main__':
    app()


    

