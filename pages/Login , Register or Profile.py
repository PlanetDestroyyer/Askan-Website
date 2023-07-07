# import streamlit as st
# import pandas as pd
# import base64

# st.set_page_config(page_title="Login , Register or Profile",page_icon="logo.jpg",layout="centered",initial_sidebar_state="auto",menu_items=None)

# def add_bg_from_local(image_file):
#     with open(image_file, "rb") as file:
#         encoded_string = base64.b64encode(file.read()).decode("utf-8")
#     return f"data:image/{image_file.split('.')[-1]};base64,{encoded_string}"

# def run_app():
#     st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background:url({add_bg_from_local("bg.jpeg")});
#             background-size: cover;
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )
# run_app()

# # Function to check if the user is logged in
# def is_logged_in():
#     session_state = get_session_state()
#     return session_state.get('username') is not None

# # Function to store the logged-in user
# def set_logged_in(username):
#     session_state = get_session_state()
#     session_state['username'] = username

# # Function to get the session state
# def get_session_state():
#     if 'session_state' not in st.session_state:
#         st.session_state['session_state'] = {}
#     return st.session_state['session_state']

# def main_page():
#     st.title("Login , Register or Profile")
#     page = st.sidebar.selectbox("Select Page", ("Login", "Registration", "Profile"))

#     if page == "Login":
#         login()
#     elif page == "Registration":
#         registeration()
#     elif page == "Profile":
#         if is_logged_in():
#             show_profile()

# def append(appendind_data):
#     df = pd.DataFrame(appendind_data)
#     df.to_csv('new1.csv', mode='a', index=False, header=False)

# def login():
#     st.subheader("Login")
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")
#     login_button = st.button("Login")

#     if login_button:
#         df = pd.read_csv('new1.csv')
#         if any((df['Name'] == username) & (df['Password'] == password)):
#             st.success("You have successfully logged in.")
#             set_logged_in(username)
#         else:
#             st.error("Invalid username or password.")

# def registeration():
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
#         if signup_button:
#             if password == confirm_password:
#                 df = pd.read_csv('new1.csv')
#                 if username in df['Name'].tolist():
#                     st.error("Username already exists. Please choose a different username.")
#                 else:
#                     st.success("Thanks for registering.")
#                     append({"Name": username, "Password": password})
#                     set_logged_in(username)
#         else:
#             st.error("Password and Confirm Password do not match.")

#     except:
#         st.write("Log in first to get to the Profile")

# def hideAll():

#     hide = """
#         <style>
#         #MainMenu {visibility: hidden;}
#         footer {visibility: hidden;}
#         header {visibility: hidden;}
#         </style>
#         """
#     st.markdown(hide, unsafe_allow_html=True)

# # Main function
# def main():

#     st.title("Login, Register, or Profile")
#     page = st.sidebar.selectbox("Select Page", ("Login", "Registration", "Profile"))

#     if page == "Login":
#         login()
#     elif page == "Registration":
#         registration()
#     elif page == "Profile":
#         if is_logged_in():
#             show_profile()

# # Function to append data to CSV file
# def append(data):
#     df = pd.DataFrame(data)
#     df.to_csv('new1.csv', mode='a', index=False, header=False)

# # Function for the login page
# def login():
#     st.subheader("Login")
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")
#     login_button = st.button("Login")

#     if login_button:
#         df = pd.read_csv('new1.csv')
#         if any((df['Name'] == username) & (df['Password'] == password)):
#             st.success("You have successfully logged in.")
#             set_logged_in(username)
#         else:
#             st.error("Invalid username or password.")

# # Function for the registration page
# def registration():
#     try:
#         st.subheader("Registration")
#         username = st.text_input("Username")
#         password = st.text_input("Password", type="password")
#         confirm_password = st.text_input("Confirm Password", type="password")
#         area_working = st.number_input("Area Working:")
#         country = st.text_input("Country", placeholder="Currently Selected India")
#         gender = st.selectbox("Gender:", ("Male", "Female"))
#         qualification = st.selectbox("Qualification:", ("Educated (10th pass)", "Uneducated"))
#         purpose = st.selectbox("Purpose:", ("Domestic", "Commercial"))
#         message = st.selectbox("Allow Personalized Message:", ("Yes", "No"))
#         mobile_number = st.text_input("Mobile Number:")
#         email = st.text_input("Email:")
#         signup_button = st.button("Register")

#         if signup_button:
#             if password == confirm_password:
#                 df = pd.read_csv('new1.csv')
#                 if username in df['Name'].tolist():
#                     st.error("Username already exists. Please choose a different username.")
#                 else:
#                     st.success("Thanks for registering.")
#                     append({
#                         "Name": [username],
#                         "Password": [password],
#                         "Region": [country],
#                         "Area Working" : [area_working],
#                         "Gender": [gender],
#                         "Qualification": [qualification],
#                         "Purpose": [purpose],
#                         "Message": [message],
#                         "Mobile Number": [mobile_number],
#                         "Email": [email]
#                     })
#                     session['username'] = username  # Store the registered username
#                     set_logged_in(username)
#             else:
#                 st.error("Password and Confirm Password do not match.")

#     except:
#         st.write("Log in first to get to the Profile")

# # Function to show the profile page
# def show_profile():

#     st.subheader("Profile")
#     session_state = get_session_state()
#     username = session_state['username']

#     df = pd.read_csv('new1.csv')

#     user_data = df[df['Name'] == username]

#     if not user_data.empty:
#         st.subheader(f"Profile: {username}")
#         st.write(f"Country: {user_data['Region'].iloc[0]}")
#         st.write(f"Gender: {user_data['Gender'].iloc[0]}")
#         st.write(f"Area Working: {user_data['Area Working'].iloc[0]}")
#         st.write(f"Qualification: {user_data['Qualification'].iloc[0]}")
#         st.write(f"Purpose: {user_data['Purpose'].iloc[0]}")
#         st.write(f"Message: {user_data['Message'].iloc[0]}")
#         st.write(f"Mobile: {user_data['Mobile Number'].iloc[0]}")
#         st.write(f"Email: {user_data['Email'].iloc[0]}")
#     else:
#         st.subheader(f"No profile data found for user: {username}")


# def main():
#     hideAll()
#     main_page()
#     show_profile()
#     registration()
#     login()
#     main_page()
#     run_app()

# if __name__ == "__main__":
#     main()
import streamlit as st
import pandas as pd
import base64

st.set_page_config(page_title="Login, Register or Profile", page_icon="logo.jpg", layout="centered", initial_sidebar_state="auto", menu_items=None)

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

def is_logged_in():
    session_state = get_session_state()
    return session_state.get('username') is not None

def set_logged_in(username):
    session_state = get_session_state()
    session_state['username'] = username

def get_session_state():
    if 'session_state' not in st.session_state:
        st.session_state['session_state'] = {}
    return st.session_state['session_state']

def main_page():
    st.title("Login, Register or Profile")
    page = st.sidebar.selectbox("Select Page", ("Login", "Registration", "Profile"))

    if page == "Login":
        login()
    elif page == "Registration":
        registration()
    elif page == "Profile":
        if is_logged_in():
            show_profile()

def append(data):
    df = pd.DataFrame(data)
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

def registration():
    try:
        st.subheader("Registration")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        area_working = st.number_input("Area Working:")
        country = st.text_input("Country", placeholder="Currently Selected India")
        gender = st.selectbox("Gender:", ("Male", "Female"))
        qualification = st.selectbox("Qualification:", ("Educated (10th pass)", "Uneducated"))
        purpose = st.selectbox("Purpose:", ("Domestic", "Commercial"))
        message = st.selectbox("Allow Personalized Message:", ("Yes", "No"))
        mobile_number = st.text_input("Mobile Number:")
        email = st.text_input("Email:")
        signup_button = st.button("Register")

        if signup_button:
            if password == confirm_password:
                df = pd.read_csv('new1.csv')
                if username in df['Name'].tolist():
                    st.error("Username already exists. Please choose a different username.")
                else:
                    st.success("Thanks for registering.")
                    append({
                        "Name": [username],
                        "Password": [password],
                        "Region": [country],
                        "Area Working" : [area_working],
                        "Gender": [gender],
                        "Qualification": [qualification],
                        "Purpose": [purpose],
                        "Message": [message],
                        "Mobile Number": [mobile_number],
                        "Email": [email]
                    })
                    session['username'] = username  # Store the registered username
                    set_logged_in(username)
            else:
                st.error("Password and Confirm Password do not match.")

    except:
        st.write("Log in first to get to the Profile")
def show_profile():
    session_state = get_session_state()
    username = session_state['username']

    df = pd.read_csv('new1.csv')
    user_data = df[df['Name'] == username]

    if not user_data.empty:
        st.subheader(f"Profile: {username}")
        st.write(f"Country: {user_data['Region'].iloc[0]}")
        st.write(f"Area Working: {user_data['Area Working'].iloc[0]}")
        st.write(f"Gender: {user_data['Gender'].iloc[0]}")
        st.write(f"Qualification: {user_data['Qualification'].iloc[0]}")
        st.write(f"Purpose: {user_data['Purpose'].iloc[0]}")
        st.write(f"Allow Personalized Message: {user_data['Message'].iloc[0]}")
        st.write(f"Mobile Number: {user_data['Mobile Number'].iloc[0]}")
        st.write(f"Email: {user_data['Email'].iloc[0]}")
    else:
        st.subheader(f"No profile data found for user: {username}")

def hideAll():
    hide = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
    st.markdown(hide, unsafe_allow_html=True)

def main():
    hideAll()
    main_page()
    run_app()

if __name__ == "__main__":
    main()
