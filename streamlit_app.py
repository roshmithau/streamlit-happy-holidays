from pathlib import Path
import json
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain

# Page configuration
st.set_page_config(page_title="Happy Holidays", page_icon="🎄")

# Directories and file paths
THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR / "style" / "styles.css"
ASSETS = THIS_DIR / "assets"
LOTTIE_ANIMATION = ASSETS / "animation_holiday.json"


# Check if the Lottie animation file exists
if not LOTTIE_ANIMATION.exists():
    st.error(f"File not found: {LOTTIE_ANIMATION}")
else:
    # Function to Load and display the Lottie animation
    def load_lottie_animation(file_path):
        try:
            with open(file_path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            st.error(f"File not found: {file_path}")
            return None
        except json.JSONDecodeError as e:
            st.error(f"Error loading JSON from {file_path}: {e}")
            return None

    # Function to apply snowfall effect
    def run_snow_animation():
        rain(emoji="❄️", font_size=20, falling_speed=5, animation_length="infinite")

    # Function to get the name from query parameters
    def get_person_name():
        query_params = st.experimental_get_query_params()
        return query_params.get("name", ["Friend"])[0]

    # Run snowfall animation
    run_snow_animation()

    # Apply custom CSS
    if CSS_FILE.exists():
        with open(CSS_FILE) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.error(f"CSS file not found: {CSS_FILE}")

    # Display header with personalized name
    PERSON_NAME = get_person_name()
    st.header(f"Happy Holidays, {PERSON_NAME}! 🎄", anchor=False)

    # Display the Lottie animation
    lottie_animation = load_lottie_animation(LOTTIE_ANIMATION)
    if lottie_animation:
        st_lottie(lottie_animation, key="lottie-holiday", height=300)
    else:
        st.error(f"Could not load Lottie animation from {LOTTIE_ANIMATION}")

    # Personalized holiday message
    st.markdown(
        f"Dear {PERSON_NAME}, wishing you a wonderful holiday season filled with joy and peace. 🌟"
    )








