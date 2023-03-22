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

character_img = Image.open(f"{img_path}/Elara.png")

# Set the page title and icon and set layout to "wide" to minimise margains
st.set_page_config(page_title="Elara", page_icon=":dragon:", initial_sidebar_state="collapsed")
add_bg_from_local(f"{img_path}/bg.jpg")

# Header section
with st.container():
    # Add two columns for page formatting, with a width ratio of 1:1.75
    about_left_col, about_right_col = st.columns((2, 1))

    # Add content to the left columns
    with about_left_col:
        # Add title
        st.write("**Neurodiversity Celebration Week**")
        st.title("Elara Moonwhisper")
        st.header("Level 8 Sorcerer with Tourettes")
        st.write("Find all 5 charcters to spell the secret word and enter the draw on the Advancing Analytics stand. Secret letter: **E**")
    
    # Add content to the right column
    with about_right_col:
        # Add a lottie animation
        st.image(character_img)

    # Add a line divider
    st.write("---")

# Stats section
with st.container():
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    col1.metric("Str", 10, 0, help="Strength, measuring physical power")
    col2.metric("Con", 11, 0, help="Dexterity, measuring agility")
    col3.metric("Dex", 10, 0, help="Constitution, measuring endurance")
    col4.metric("Int", 17, 3, help="Intelligence, measuring reasoning and memory")
    col5.metric("Wis", 16, 3, help="Wisdom, measuring Perception and Insight")
    col6.metric("Cha", 18, 4, help="Charisma, measuring force of Personality")

# Backstory section
with st.container():
    st.title("Backstory")
    st.write("""
    Elara was born to a human mother and an elven father, but it quickly became apparent that she was different from other half-elves. From a young age, she began to display symptoms of Tourette's syndrome, including involuntary tics and outbursts of speech. This made her the target of ridicule and bullying, leading her to withdraw from society and embrace her wild, unpredictable magic.

    As Elara learned to control her magic, she also began to find ways to channel her tics into her spellcasting. Rather than being a hindrance, her Tourette's became a source of power, imbuing her spells with an unpredictable energy that could have amazing or disastrous consequences. Elara embraced the risk, taking pride in her unique connection to the wild magic that flowed through her veins.

    Despite her unorthodox methods, Elara soon gained a reputation as one of the most powerful sorcerers in the land. She used her magic to help those in need, never hesitating to take on the toughest challenges. However, her unpredictable nature often caused trouble, leading her to be seen as a wild card by some and a hero by others.

    Elara never let her Tourette's hold her back. Instead, she used it to her advantage, proving to the world that even those with disabilities can be powerful and capable individuals. She now travels the land, using her wild magic to protect the innocent and bring hope to those in need, always striving to be the best she can be despite the challenges she faces.
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