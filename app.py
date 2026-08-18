import streamlit as st

st.set_page_config(page_title="TreeSense Imaging", layout="wide")

st.title("🌳 TreeSense Imaging: Tree Enumeration & Analytics")
st.write("Welcome to the TreeSense dashboard.")

# Embed your HTML frontend inside Streamlit if using static files
with open("treesense/index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=800, scrolling=True)
