import streamlit as st
import google.generativeai as genai
import base64

def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load your CSS styles
load_css('style.css') 

# Configure the API key
genai.configure(api_key="AIzaSyD8cqxyUjlP-eT07BVDkV__6IfNKZ83u1c")

# Set the title of the app
st.markdown("""<h1 class="heading">buddy . . .👻</h1>""", unsafe_allow_html=True)

# Specify the path to your background image
image_path = "./tech_1.jpg"  # Make sure this path is correct

# Function to load the image and encode it to base64
def load_image(image_file):
    with open(image_file, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# Use the image as background
background_image = load_image(image_path)
st.markdown(
    f"""
    <style>
    .main {{
        background-image: url("data:image/jpeg;base64,{background_image}");
        background-size: cover;  
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: white;  /* Change text color to be readable on the background */
        height: 100vh;  /* Make the background cover the entire viewport height */
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Display a heading for the user prompt
# st.markdown("""<h6 class="prompt_label">Ask here...</h6>""", unsafe_allow_html=True)

# Create a text input for the user prompt using the custom class
user_prompt = st.text_input("Type your question here...", key="user_input", placeholder="Ask here...", label_visibility="hidden")

# Add custom class to the input field using HTML
st.markdown(
    """
    <style>
    .prompt_input {
        border: 2px solid white;
        padding: 10px;
        border-radius: 5px;
        font-size: 1.2em;
        width: 80%;
        margin: 20px auto;
        display: block;
        color: white; /* Adjust text color */
    }
    </style>
    """, unsafe_allow_html=True
)

# Button to generate response
if st.button("Results"):
    if user_prompt:  # Check if user input is provided
        try:
            # Generate content using the Gemini model
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(user_prompt)
            st.text_area("Response:", value=response.text, height=400,label_visibility="hidden")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter some text to generate a response.")
