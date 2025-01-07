import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    with Image.open('images/pfp2-2025.png') as img:
        # Rotate the image by 270 degrees
        rotated_img = img.rotate(270, expand=True)
        # Save the rotated image to a temporary file
        rotated_img.save('images/rotated_pfp2-2025.png')
    # Display the rotated image in Streamlit
    st.image('images/rotated_pfp2-2025.png')

with col2:
    st.title("Megan Lynn")
    content = """
    Hi! I'm Megan! I'm a self-taught software engineer and I love to build things. Here's an intro at my personal website and projects I've worked on.
    """
    st.info(content)