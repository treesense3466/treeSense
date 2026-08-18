import os
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="TreeSense Imaging", layout="wide")

st.title("🌳 TreeSense Imaging: Tree Enumeration & Analytics")
st.write("Welcome to the TreeSense dashboard.")

# Base directory where app.py resides
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Check relative paths dynamically
html_path = os.path.join(BASE_DIR, "treesense", "index.html")
if not os.path.exists(html_path):
    html_path = os.path.join(BASE_DIR, "index.html")

if os.path.exists(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=800, scrolling=True)
else:
    st.error(f"Could not locate index.html at {html_path}")
