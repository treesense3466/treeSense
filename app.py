import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="TreeSense Imaging", layout="centered")

st.title("TreeSense Imaging")
st.write("Automated tree enumeration & green cover estimation using satellite/aerial imagery.")

uploaded_file = st.file_uploader("Choose a satellite or aerial image...", type=["jpg", "jpeg", "png"])

threshold_val = st.slider("Segmentation Threshold", min_value=0, max_value=255, value=127)

if uploaded_file is not None:
    # Convert uploaded file to OpenCV format
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img_bgr = cv2.imdecode(file_bytes, 1)

    # Convert to HSV color space for green detection
    hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
    lower_green = np.array([25, 40, 40])
    upper_green = np.array([85, 255, 255])
    
    mask = cv2.inRange(hsv, lower_green, upper_green)
    _, thresh = cv2.threshold(mask, threshold_val, 255, cv2.THRESH_BINARY)

    # Compute metrics
    total_pixels = thresh.size
    green_pixels = cv2.countNonZero(thresh)
    green_cover_pct = (green_pixels / total_pixels) * 100

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    tree_contours = [c for c in contours if cv2.contourArea(c) > 20]
    tree_count = len(tree_contours)

    # Draw contours on original image
    output_img = img_bgr.copy()
    cv2.drawContours(output_img, tree_contours, -1, (0, 0, 255), 2)
    output_rgb = cv2.cvtColor(output_img, cv2.COLOR_BGR2RGB)

    # Display results
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Estimated Tree Count", tree_count)
    with col2:
        st.metric("Green Cover Percentage", f"{green_cover_pct:.2f}%")

    st.image(output_rgb, caption="Processed Image with Detected Trees", use_column_width=True)
