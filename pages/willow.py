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

character_img = Image.open(f"{img_path}/Willow.png")

# Set the page title and icon and set layout to "wide" to minimise margains
st.set_page_config(page_title="Willow", page_icon=":dragon:")
add_bg_from_local(f"{img_path}/bg.jpg")

# Header section
with st.container():
    # Add two columns for page formatting, with a width ratio of 1:1.75
    about_left_col, about_right_col = st.columns((2, 1))

    # Add content to the left columns
    with about_left_col:
        # Add title
        st.write("**Neurodiversity Celebration Week**")
        st.title("Willow Wildheart")
        st.header("Level 4 Druid with ADHD")
        st.write("Find all 5 charcters to spell the secret word and enter the draw on the Advancing Analytics stand. Secret letter: **O**")
    
    # Add content to the right column
    with about_right_col:
        # Add a lottie animation
        st.image(character_img)

    # Add a line divider
    st.write("---")

# Stats section
with st.container():
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    col1.metric("Str", 14, 2, help="Strength, measuring physical power")
    col2.metric("Con", 15, 2, help="Dexterity, measuring agility")
    col3.metric("Dex", 13, 1, help="Constitution, measuring endurance")
    col4.metric("Int", 15, 2, help="Intelligence, measuring reasoning and memory")
    col5.metric("Wis", 18, 4, help="Wisdom, measuring Perception and Insight")
    col6.metric("Cha", 11, 0, help="Charisma, measuring force of Personality")

# Backstory section
with st.container():
    st.title("Backstory")
    st.write("""
    Willow was born with a deep connection to the natural world, but from a young age, she struggled with ADHD, finding it difficult to focus and stay on task. Despite her love for nature and her strong connection to the wilderness, Willow found it challenging to follow the strict teachings of the druidic order.

    However, Willow refused to let her ADHD hold her back. She struck out on her own, using her connection to the natural world to explore and understand the mysteries of the wilderness. Her adventures led her to discover a unique magic, one that was wild and unpredictable, much like her own thoughts and emotions.

    Willow quickly learned to harness her new-found power, using it to protect the natural world and the creatures that called it home. Despite her unorthodox approach, Willow quickly gained a reputation as one of the most powerful druids in the land, using her wild magic to bring balance to an otherwise chaotic world.

    Despite the challenges she faced, Willow never lost her love for the natural world and her desire to protect it. She now travels the land, using her skills as a druid and her wild magic to defend the innocent and restore balance to the wilderness, always striving to be the best she can be. Willow is a shining example of how those with ADHD can channel their differences into strengths and make a positive impact on the world.
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