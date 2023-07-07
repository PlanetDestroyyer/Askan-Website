import streamlit as st
import base64
st.set_page_config(page_title="Contact US",page_icon="logo.jpg",layout="centered",initial_sidebar_state="auto",menu_items=None)

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

def hideAll():
    hide = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """   
    st.markdown(hide, unsafe_allow_html=True)

def style():
    st.markdown(
        """
        <style>

        
        @import url('https://fonts.googleapis.com/css2?family=Lobster&family=Pacifico&display=swap');

        
        body {
            font-family: 'Roboto', sans-serif;
            background-color: #f8f8f8;
            color:black;
        }

       
        h1 {
            color: #32df07;
            font-size: 60px; 
        }

        h2 {
            color: #1e90ff;
            font-size: 36px;
            font-weight: bold;
        }

        p {
            color: white;
            font-size: 24px;
            line-height: 1.5;
        }

       
        ul {
            color: black;
            font-size: 24px;
            line-height: 1.5;
        }

        .video-container {
            display: flex;
            justify-content: space-between;
        }

        
        h3 {
            color: #ff4500;
            font-size: 28px; 
            font-weight: bold;
            
        }

      

        a {
            color: #1e90ff;
            text-decoration: none;
        }

       
        button {
            background-color: #1e90ff;
            color: #fff;
            border: none;
            padding: 10px 20px;
            font-size: 18px;
            border-radius: 5px;
            cursor: pointer;
        }
        .css-aw8l5d e1akgbir1{
            background-color:black;
        }
       

        </style>
        """,
        unsafe_allow_html=True
    )



def footer():
    st.header("Contact Us")
    st.write("---")
    st.subheader("Email: askan.hydroponics2023@gmail.com")
    st.subheader("Mobile No.: +91 7410545183")
    st.subheader("It is a Project Based Activity. We appreciate your feedback!")
    st.markdown("---")
    st.header("© 2023 All rights reserved by ASKAN Hydroponics Ltd.")

def main():
    style()
    run_app()
    hideAll()
    footer()

if __name__ == "__main__":
    main()