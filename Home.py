import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import base64
st.set_page_config(page_title="ASKAN",page_icon="logo.jpg",layout="wide",initial_sidebar_state="auto",menu_items=None)
want_to_contribute = st.button("Profile")
if want_to_contribute:
    switch_page('Profile')
def main():
    st.header("ASKAN")
    st.write("#")
    st.subheader("A GOOD AGRICULTURE FOR BETTER TOMMOROW........!")

    st.write("""
Welcome to our Hydroponic Farming Website!

Are you ready to discover the future of agriculture? Look no further than hydroponic farming, the innovative and sustainable method of growing plants without soil. We are here to provide you with all the information you need to understand and embark on this exciting journey.

What is Hydroponic Farming?
Hydroponic farming is a revolutionary technique that allows plants to thrive in a controlled environment without the need for traditional soil-based cultivation. Instead, plants are grown in nutrient-rich water solutions, providing them with optimal conditions for growth and development. By harnessing this method, hydroponic farming offers numerous advantages over traditional farming methods.""")
    
    st.write("---")
    st.subheader("Advantages of Hydroponic Farming:")
    st.write("""
    - 1) Water Conservation: Hydroponic farming uses up to 90% less water compared to conventional agriculture, making it a highly efficient and sustainable option. By recirculating and reusing water, it significantly reduces water wastage.

- 2) Space Efficiency: Hydroponic systems can be set up vertically, maximizing the use of available space. This vertical arrangement allows for higher plant density and increased yield per square foot, making it ideal for urban areas or places with limited land.
 
- 3) Year-round Production: With hydroponics, you have the ability to grow crops all year long, regardless of the season or climate. By controlling the environment, including temperature, lighting, and humidity, you can create the perfect conditions for plant growth, ensuring a constant supply of fresh produce.
 
- 4) Enhanced Nutrient Control: Hydroponics enables precise control over the nutrients plants receive. By directly providing essential nutrients to the root system, plants can absorb them more efficiently, resulting in faster growth and healthier crops. This level of control also minimizes the use of chemical fertilizers.

- 5) Reduced Pest and Disease Pressure: Since hydroponic systems are typically enclosed, pests and diseases are less likely to affect your crops. By eliminating the need for pesticides and reducing the risk of contamination, hydroponic farming promotes cleaner and healthier food production.""")
    st.write("---")
    st.subheader("Videos")
    st.write("---")
    colm1,colm2,colm3 = st.columns(3)
    with colm1:
        st.video("https://youtu.be/ygGUe-q3cww")
    with colm2:
        st.video("https://youtu.be/LGF33NN4B8U")
    with colm3:
        st.video("https://youtu.be/OqREBOP7A0I")
    st.write("---")
    st.subheader("How Does Hydroponic Farming Work?")
    st.subheader("Hydroponic farming utilizes various methods and systems to cultivate plants. Some popular techniques include:")
    st.write("""
    - 1) Nutrient Film Technique (NFT): In NFT systems, a thin film of nutrient-rich water flows continuously over the plant roots, providing essential nutrients while also allowing oxygen to reach them.

- 2) Deep Water Culture (DWC): DWC involves suspending plant roots in oxygenated nutrient solutions. Air stones or diffusers are used to maintain adequate oxygen levels, promoting healthy root development.

- 3) Drip Irrigation: Drip systems deliver nutrient solutions directly to the plant roots through a network of tubes and emitters. This method offers flexibility and precision in nutrient delivery.

- 4) Aeroponics: Aeroponic systems mist the plant roots with a nutrient-rich solution, ensuring they receive ample nutrients and oxygen. This method allows for faster growth rates and efficient nutrient absorption.""")
def style():
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('image.png')    
    
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
style()
hideAll()
main()

def footer():
    colm1,colm2,colum3 = st.columns(3)
    with colm2:
     st.markdown("---")
    st.subheader("Contact Us")
    st.write("E-mail: askan.hydroponics2023@gmail.com")
    st.write("Mo.No. - +91 7410545183")
    st.write("---")
    st.write("It is a Project Based Activity. Do share your feedback with us...")
    st.write("Thank You...!")
    st.write("---")
    st.write("Copyright - ©2023 All rights reserved by askan.hydroponics Ltd.")

def run_app():
    footer()

if __name__ == "__main__":
    run_app()
    