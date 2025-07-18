import streamlit as st
import random

# Sample quotes
quotes = [
    "The best way to get started is to quit talking and begin doing. – Walt Disney",
    "Success is not in what you have, but who you are. – Bo Bennett",
    "The harder you work for something, the greater you’ll feel when you achieve it.",
    "Dream it. Wish it. Do it.",
    "Don’t watch the clock; do what it does. Keep going. – Sam Levenson",
    "Push yourself, because no one else is going to do it for you."
]

# Sample backgrounds
background_urls = [
    "https://source.unsplash.com/1600x900/?nature,water",
    "https://source.unsplash.com/1600x900/?mountain,sunset",
    "https://source.unsplash.com/1600x900/?stars,sky",
    "https://source.unsplash.com/1600x900/?forest,light",
    "https://source.unsplash.com/1600x900/?ocean,waves"
]

# Set page config
st.set_page_config(page_title="Inspo Generator", layout="wide")

# Initialize session state
if "quote" not in st.session_state:
    st.session_state.quote = random.choice(quotes)
    st.session_state.bg = random.choice(background_urls)

# Handle button click
if st.button("🔁 New Quote"):
    st.session_state.quote = random.choice(quotes)
    st.session_state.bg = random.choice(background_urls)

# Access session state
selected_quote = st.session_state.quote
selected_background = st.session_state.bg

# Custom CSS
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("{selected_background}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    .quote-box {{
        background-color: rgba(255, 255, 255, 0.75);
        padding: 2rem;
        border-radius: 15px;
        margin-top: 150px;
        box-shadow: 0 0 10px rgba(0,0,0,0.3);
    }}
    .quote {{
        font-size: 1.8rem;
        font-weight: 600;
        color: #333;
        text-align: center;
    }}
    </style>
""", unsafe_allow_html=True)

# App title
st.markdown("<h1 style='text-align: center; color: white;'>✨ Inspo Generator ✨</h1>", unsafe_allow_html=True)

# Display quote
with st.container():
    st.markdown(f"""
    <div class='quote-box'>
        <div class='quote'>{selected_quote}</div>
    </div>
    """, unsafe_allow_html=True)
