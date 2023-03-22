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

character_img = Image.open(f"{img_path}/Findabhair.png")

# Set the page title and icon and set layout to "wide" to minimise margains
st.set_page_config(page_title="Findabhair", page_icon=":dragon:")
add_bg_from_local(f"{img_path}/bg.jpg")

# Header section
with st.container():
    # Add two columns for page formatting, with a width ratio of 1:1.75
    about_left_col, about_right_col = st.columns((2, 1))

    # Add content to the left columns
    with about_left_col:
        # Add title
        st.write("**Neurodiversity Celebration Week**")
        st.title("Findabhair the Fantastic")
        st.header("Level 12 Dyslexic Wizard")
        st.write("Find all 5 charcters to spell the secret word and enter the draw on the Advancing Analytics stand. Secret letter: **U**")
    
    # Add content to the right column
    with about_right_col:
        # Add a lottie animation
        st.image(character_img)

    # Add a line divider
    st.write("---")

# Stats section
with st.container():
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    col1.metric("Str", 8, -1, help="Strength, measuring physical power")
    col2.metric("Con", 14, 2, help="Dexterity, measuring agility")
    col3.metric("Dex", 7, -2, help="Constitution, measuring endurance")
    col4.metric("Int", 18, 4, help="Intelligence, measuring reasoning and memory")
    col5.metric("Wis", 17, 3, help="Wisdom, measuring Perception and Insight")
    col6.metric("Cha", 11, 0, help="Charisma, measuring force of Personality")

# Backstory section
with st.container():
    st.title("Backstory")
    st.write("""
    Findabhair was born into a family of wizards, and from a young age, it was clear that he had a natural talent for magic. However, Findabhair also struggled with reading and writing, a condition that was later diagnosed as dyslexia. Despite this, Findabhair was determined to follow in the footsteps of his family and become a wizard.

    Growing up, Findabhair found that traditional forms of learning, such as reading from spellbooks and writing incantations, were difficult for him. He often made mistakes and had trouble remembering the correct spell components. This led to frustration and feelings of inadequacy, especially when compared to his classmates who seemed to have no trouble with these tasks.

    However, Findabhair soon discovered that he had a unique talent - an innate understanding of magic that transcended the need for traditional forms of spellcasting. Instead of relying on written incantations, Findabhair learned to channel magic through his memories and instincts, unlocking new and unpredictable forms of magic in the process.

    With time and practice, Findabhair honed his skills and became a powerful wizard in his own right. He also learned to embrace his dyslexia, seeing it as a source of strength and creativity rather than a weakness. Findabhair now travels the land, using his unconventional magic to help those in need and prove that dyslexia need not be an obstacle to greatness.
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