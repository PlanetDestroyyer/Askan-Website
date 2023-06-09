# import streamlit as st
# import pandas as pd 
# from streamlit_extras.switch_page_button import switch_page
# # from pages.Profile import show_profile

# session = st.session_state

# def main():
#     st.title("Login Or Resigter")
#     page = st.sidebar.selectbox("Select Page", ("Login", "Registration","Profile"))
#     if page == "Login":
#         login()
#     elif page == "Registration":
#         signup()
#     elif page == "Profile":
#         show_profile(session.get('username'))  # Display the profile page
    
#     # Existing code

# def append(appendind_data):
#     df = pd.DataFrame(appendind_data)
#     df.to_csv('new1.csv', mode='a', index=False, header=False)


# def login():
#     df = pd.read_csv('new1.csv', sep=',')
#     try:
#         st.subheader("Login")
#         username = st.text_input("Username")
#         password = st.text_input("Password", type="password")
#         login_button = st.button("Login")

#         if login_button:
#             if username in df['Name'].tolist() and password in df['Password'].tolist():
#                 st.success("U have successfully entered into the app")
#                 show_profile(username)
#             else:
#                 st.write("Error")
#     except:
#         pass

# def signup():
#     try:
#         st.subheader("Registration")
#         username = st.text_input("Username")
#         password = st.text_input("Password", type="password")
#         confirm_password = st.text_input("Confirm Password", type="password")
#         Area_Working = st.number_input("Area_Working:")
#         Country = st.text_input("Country", placeholder="Currently Selected India")
#         Gender = st.selectbox("Gender:", ("Male", "Female"))
#         Qualification = st.selectbox("Qualification:", ("Educated (10th pass)", "Uneducated"))
#         Purpose = st.selectbox("Purpose:", ("Domestic", "Commercial"))
#         Message = st.selectbox("Allow Personalized Message:", ("Yes", "No"))
#         Number = st.text_input("Mobile Number :")
#         Email = st.text_input("Email :")
#         signup_button = st.button("Register")
        
#         if password == confirm_password:
#             st.success("Thanks for Registering")
#             append({"Name": [username], "Password": [password], "Region": [Country], "Area Working": [Area_Working], "Gender": [Gender], "Qualification": [Qualification], "Purpose": [Purpose], "Message": [Message], "Mobile": [Number], "Email": [Email]})
#             session['username'] = username  # Store the registered username
#             switch_page('Profile')  
#         else:
#             st.write("Password and Confirm Password should be the same")
#     except:
#         pass

# def show_profile(username):
#     st.title(f"Profile: {username}")
#     # Add code to display the profile information

# def hideAll():
#     hide = """
#         <style>
#         #MainMenu {visibility: hidden;}
#         footer {visibility: hidden;}
#         header {visibility: hidden;}
#         </style>
#         """   
#     st.markdown(hide,unsafe_allow_html=True)

# hideAll()

# if __name__ == "__main__":
#     main()                                                                                                                       
import streamlit as st
import pandas as pd

def main():
    st.title("Login or Register")
    page = st.sidebar.selectbox("Select Page", ("Login", "Registration", "Profile"))

    if page == "Login":
        login()
    elif page == "Registration":
        registeration()
    elif page == "Profile":
        if is_logged_in():
            show_profile()

def append(appendind_data):
    df = pd.DataFrame(appendind_data)
    df.to_csv('new1.csv', mode='a', index=False, header=False)

def login():
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        df = pd.read_csv('new1.csv')
        if any((df['Name'] == username) & (df['Password'] == password)):
            st.success("You have successfully logged in.")
            set_logged_in(username)
        else:
            st.error("Invalid username or password.")

def registeration():
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
        if signup_button:
            if password == confirm_password:
                df = pd.read_csv('new1.csv')
                if username in df['Name'].tolist():
                    st.error("Username already exists. Please choose a different username.")
                else:
                    st.success("Thanks for registering.")
                    append({"Name": username, "Password": password})
                    set_logged_in(username)
        else:
            st.error("Password and Confirm Password do not match.")

    except:
        st.write("Log in first to get to the Profile")


def show_profile():
    session_state = get_session_state()
    username = session_state['username']
    st.text(f"Profile: {username}")



def is_logged_in():
    df = pd.read_csv('new1.csv')
    number = df['Numbers'].tolist()
    names = df['Names'].tolist()
    if name in names:
        index = names.index(name)
        number = number[index]
        number = int(number)
        whatappp(number)
    session_state = get_session_state()
    return session_state.get('username') is not None

def set_logged_in(username):
    session_state = get_session_state()
    session_state['username'] = username

def get_session_state():
    if 'session_state' not in st.session_state:
        st.session_state['session_state'] = {}
    return st.session_state['session_state']

def hideAll():
    hide = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """   
    st.markdown(hide,unsafe_allow_html=True)

if __name__ == "__main__":
    hideAll()
    main()
