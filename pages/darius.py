import base64
import streamlit as st
from pathlib import Path
from PIL import Image

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

# Load the assets for the app
img_path = Path(__file__).parents[0]

character_img = Image.open(f"{img_path}/Darius.png")

# Set the page title and icon and set layout to "wide" to minimise margains
st.set_page_config(page_title="Darius", page_icon=":dragon:", initial_sidebar_state="collapsed")
add_bg_from_local(f"{img_path}/bg.jpg")

# Header section
with st.container():
    # Add two columns for page formatting, with a width ratio of 1:1.75
    about_left_col, about_right_col = st.columns((2, 1))

    # Add content to the left columns
    with about_left_col:
        # Add title
        st.write("**Neurodiversity Celebration Week**")
        st.title("Darius Dingleberry")
        st.header("Level 5 Bard with Anxiety")
        st.write("Find all 5 charcters to spell the secret word and enter the draw on the Advancing Analytics stand. Secret letter: **N**")
    
    # Add content to the right column
    with about_right_col:
        # Add a lottie animation
        st.image(character_img)

    # Add a line divider
    st.write("---")

# Stats section
with st.container():
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    col1.metric("Str", 9, -1, help="Strength, measuring physical power")
    col2.metric("Con", 12, 1, help="Dexterity, measuring agility")
    col3.metric("Dex", 12, 1, help="Constitution, measuring endurance")
    col4.metric("Int", 17, 3, help="Intelligence, measuring reasoning and memory")
    col5.metric("Wis", 16, 3, help="Wisdom, measuring Perception and Insight")
    col6.metric("Cha", 14, 2, help="Charisma, measuring force of Personality")

# Backstory section
with st.container():
    st.title("Backstory")
    st.write("""
    Darius was born into a family of bards, known for their musical talent and storytelling prowess. However, from a young age, Darius struggled with anxiety, feeling overwhelmed by new experiences and social situations. Despite his natural musical ability, he found it difficult to perform in front of others, leading him to withdraw from the bardic community and seek solace in his music.

    As Darius practiced and honed his skills, he also learned to manage his anxiety. He discovered that playing his lute and singing helped him to calm his nerves and find inner peace. With time and practice, he gained the confidence to perform in front of others, using his music to spread hope and joy to those around him.

    Despite his struggles with anxiety, Darius never lost his love for adventure. He joined a group of adventurers, using his bardic talents to lift the spirits of his companions and bolster their resolve in the face of danger. His anxiety was still a constant companion, but he refused to let it hold him back, using it as a source of motivation to overcome his fears and become the best bard he could be.

    Darius's experiences have taught him that everyone has their own struggles and that it's important to be kind to yourself and others. He now travels the land, using his music to spread hope and comfort to those in need, always striving to be the best he can be despite the challenges he faces.
    """)
    st.write("---")


# About section
with st.container():
    st.header("What is Neurodiversity Celebration Week?")
    st.write("""
    Neurodiversity Celebration Week is an annual event that promotes awareness and acceptance of neurological differences, such as autism, ADHD, dyslexia, and Tourette's syndrome. This week-long celebration aims to highlight the unique strengths and abilities of neurodivergent individuals, while challenging stigma and discrimination.

    At Advancing Analytics, we have created a series of neurodivergent characters for Dungeons & Dragons. Each character is uniquely designed to showcase the strengths and abilities associated with their specific neurodivergent traits.

    These characters demonstrate that neurodiversity is not a weakness, but rather a source of strength and creativity. By celebrating and embracing these differences, we can create a more inclusive and diverse world.
    """)