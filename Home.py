import streamlit as st
import pandas

st.set_page_config(layout="centered")

col1, col2 = st.columns(2)

with col1:
    st.image('images/rotated_pfp2-2025.png')

with col2:
    st.title("Megan Lynn")
    content = """
    Hi! I'm Megan! I'm a self-taught software engineer and I love to build things. I'm passionate about Philadelphia sports, Star Wars/Marvel movies, and
     Nintendo video games. Here's an intro at my personal website and projects I've worked on.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I've built with Python. Feel free to check them out!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

