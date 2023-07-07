import streamlit as st
import base64


st.set_page_config(page_title="Activity",page_icon="logo.jpg",layout="centered",initial_sidebar_state="auto",menu_items=None)    
def main():
    st.header("ASKAN")
    st.write("#")
    st.subheader("A GOOD AGRICULTURE FOR BETTER TOMMOROW........!")


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
    st.title("ASKAN")
    st.subheader("A GOOD AGRICULTURE FOR A BETTER TOMORROW")
    st.markdown("---")

    st.markdown("""
        Welcome to our Hydroponic Farming Website!

        Are you ready to discover the future of agriculture? Look no further than hydroponic farming, 
        the innovative and sustainable method of growing plants without soil. We are here to provide you 
        with all the information you need to understand and embark on this exciting journey.

        **What is Hydroponic Farming?**
        Hydroponic farming is a revolutionary technique that allows plants to thrive in a controlled 
        environment without the need for traditional soil-based cultivation. Instead, plants are grown 
        in nutrient-rich water solutions, providing them with optimal conditions for growth and development. 
        By harnessing this method, hydroponic farming offers numerous advantages over traditional farming methods.
    """)

    st.markdown("---")
    st.subheader("Advantages of Hydroponic Farming:")
    st.markdown("""
        1. **Water Conservation**: Hydroponic farming uses up to 90% less water compared to conventional agriculture, 
        making it a highly efficient and sustainable option. By recirculating and reusing water, it significantly 
        reduces water wastage.

        2. **Space Efficiency**: Hydroponic systems can be set up vertically, maximizing the use of available space. 
        This vertical arrangement allows for higher plant density and increased yield per square foot, making it ideal 
        for urban areas or places with limited land.

        3. **Year-round Production**: With hydroponics, you have the ability to grow crops all year long, regardless 
        of the season or climate. By controlling the environment, including temperature, lighting, and humidity, 
        you can create the perfect conditions for plant growth, ensuring a constant supply of fresh produce.

        4. **Enhanced Nutrient Control**: Hydroponics enables precise control over the nutrients plants receive. 
        By directly providing essential nutrients to the root system, plants can absorb them more efficiently, 
        resulting in faster growth and healthier crops. This level of control also minimizes the use of chemical fertilizers.

        5. **Reduced Pest and Disease Pressure**: Since hydroponic systems are typically enclosed, pests and diseases 
        are less likely to affect your crops. By eliminating the need for pesticides and reducing the risk of contamination, 
        hydroponic farming promotes cleaner and healthier food production.
    """)

    st.markdown("---")
    st.subheader("Videos")
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.video("https://youtu.be/ygGUe-q3cww")
    with col2:
        st.video("https://youtu.be/LGF33NN4B8U")
    with col3:
        st.video("https://youtu.be/OqREBOP7A0I")

    st.markdown("---")
    st.subheader("How Does Hydroponic Farming Work?")
    st.subheader("Hydroponic farming utilizes various methods and systems to cultivate plants. Some popular techniques include:")
    st.markdown("""
        1. **Nutrient Film Technique (NFT)**: In NFT systems, a thin film of nutrient-rich water flows continuously over 
        the plant roots, providing essential nutrients while also allowing oxygen to reach them.

        2. **Deep Water Culture (DWC)**: DWC involves suspending plant roots in oxygenated nutrient solutions. Air stones 
        or diffusers are used to maintain adequate oxygen levels, promoting healthy root development.

        3. **Drip Irrigation**: Drip systems deliver nutrient solutions directly to the plant roots through a network of 
        tubes and emitters. This method offers flexibility and precision in nutrient delivery.

        4. **Aeroponics**: Aeroponic systems mist the plant roots with a nutrient-rich solution, ensuring they receive 
        ample nutrients and oxygen. This method allows for faster growth rates and efficient nutrient absorption.
    """)

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
    main()

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
            color: black;
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
            text-align: center;
        }

      
        ul {
            color: black;
            font-size: 24px;
            line-height: 1.5;
        }

        a {
            color: #1e90ff;
            text-decoration: none;
        }

       
        button {
            background-color: black;
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

style()
hideAll()
if __name__ == "__main__":
    run_app()

