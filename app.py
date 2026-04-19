from dotenv import load_dotenv
import os
from PIL import Image
import streamlit as st
import google.generativeai as genai
load_dotenv()
genai.configure(api_key=os.getenv('gemini_api_key'))
st.title('Image application')
uploaded_file=st.file_uploader('upload a image')

if uploaded_file is not None:
    st.image(Image.open(uploaded_file))
prompt=st.text_input('Enter your prompt')
img=Image.open(uploaded_file)

if st.button('Generate'):
    model=genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content([prompt, img])
    st.success(response.text)
    
# st.title('Image application')
# propmt=st.text_input
# img=Image.open