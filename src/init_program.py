import streamlit as st
from getPicture import process_image
from PIL import Image

# Selection box
options = ("Select upload method...",
           "Click From Camera", "Upload From Device")
selected = st.selectbox("How do you want to upload photo of coins?",
                        options,
                        index=0)

# calculate button and function
def calc_button(img):
    if st.button("Calculate"):
        process_image(st, Image.open(img))


# opt-1: Camera
if selected == options[0]:
    st.write("Please select upload method from above list")

elif selected == options[1]:
    cam_img = st.camera_input("Input from Camera")
    if cam_img:
        calc_button(cam_img)

# opt-2: Device upload
elif selected == options[2]:
    upload_img = st.file_uploader("Upload from device", 
                                  type=[".jpeg", ".jpg", ".png", ".gif", 
                                        ".bmp", ".tiff", ".tif", ".webp"])
    if upload_img:
        calc_button(upload_img)
