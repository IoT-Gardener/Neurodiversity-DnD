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

character_img = Image.open(f"{img_path}/Reginald.png")

# Set the page title and icon and set layout to "wide" to minimise margains
st.set_page_config(page_title="Reginald", page_icon=":dragon:")
add_bg_from_local(f"{img_path}/bg.jpg")

# Header section
with st.container():
    # Add two columns for page formatting, with a width ratio of 1:1.75
    about_left_col, about_right_col = st.columns((2, 1))

    # Add content to the left columns
    with about_left_col:
        # Add title
        st.write("**Neurodiversity Celebration Week**")
        st.title("Sir Reginald the True")
        st.header("Level 10 Autistic Paladin")
        st.write("Find all 5 charcters to spell the secret word and enter the draw on the Advancing Analytics stand. Secret letter: **R**")
    
    # Add content to the right column
    with about_right_col:
        # Add a lottie animation
        st.image(character_img)

    # Add a line divider
    st.write("---")

# Stats section
with st.container():
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    col1.metric("Str", 16, 3, help="Strength, measuring physical power")
    col2.metric("Con", 18, 4, help="Dexterity, measuring agility")
    col3.metric("Dex", 14, 2, help="Constitution, measuring endurance")
    col4.metric("Int", 12, 1, help="Intelligence, measuring reasoning and memory")
    col5.metric("Wis", 13, 1, help="Wisdom, measuring Perception and Insight")
    col6.metric("Cha", 12, 1, help="Charisma, measuring force of Personality")

# Backstory section
with st.container():
    st.title("Backstory")
    st.write("""
    Reginald was born into a proud dwarven clan, known for their skill in battle and devotion to their gods. However, from a young age, it became clear that Reginald was different from his peers. He had trouble connecting with others, struggled with social cues, and often became overwhelmed by sensory stimuli. It wasn't until later in life that Reginald was diagnosed with autism.

    Despite these challenges, Reginald was determined to follow in the footsteps of his ancestors and become a paladin. He trained tirelessly, mastering the art of combat and honing his devotion to his deity. However, he often found that the rigid social expectations of paladins and their organizations were difficult for him to navigate.

    Reginald's autism gave him a unique perspective on the world, allowing him to see things that others missed and giving him a deep sense of empathy and compassion for those in need. This, combined with his devotion to his deity, made him an unstoppable force for good, a shining beacon of hope in an otherwise dark world.

    Despite the challenges he faced, Reginald embraced his differences and used them to his advantage, proving to others that those on the autism spectrum can be powerful, capable, and compassionate leaders. Reginald now travels the land, using his skills as a paladin to defend the innocent and spread the teachings of his deity, always striving to be the best he can be. 
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