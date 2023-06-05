import streamlit as st
import os
st.set_page_config(layout="wide")
st.markdown(
    """
    <style>
    body {
        zoom: 90%;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
import math
from PIL import Image
import os
from src.AI_text_Classifier import Text_Classifier

with open('style/final.css') as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
imcol1, imcol2, imcol3 = st.columns((3,5,2))
with imcol1:
    st.write("")
with imcol2:
    st.image('image/Logo_final.png')
    st.write("")
with imcol3:
    st.write("")
st.markdown("<p style='text-align: center; color: black; font-size:25px;'><span style='font-weight: bold'>ChatGPT Application: </span>Content Classifier</p>", unsafe_allow_html=True)
# st.markdown("<div style='display: flex; margin-top: -45px ; justify-content: center;'><hr style='height: 2px; background-color: gray; width: 440px; border: none;'></div>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: blue;margin-top: -10px ;font-size:20px;'><span style='font-weight: bold'></span>Classify Whether a Given Content is Written by Human or AI</p>", unsafe_allow_html=True)
st.markdown("<hr style=height:2.5px;margin-top:0px;background-color:gray;>",unsafe_allow_html=True)
#---------Side bar-------#

with st.sidebar:
    selected = st.selectbox("",['Content Classifier'],key='text')
    Library = st.selectbox("",
                     ["Library Used","Streamlit","Image","Pandas","Requests"],key='text1')
    Gcp_cloud = st.selectbox("",
                     ["GCP Services Used","VM Instance","Computer Engine","Cloud Storage"],key='text2')
    st.markdown("## ")
    href = """<form action="#">
            <input type="submit" value="Clear/Reset" />
            </form>"""
    st.sidebar.markdown(href, unsafe_allow_html=True)
    st.markdown("### ")
    st.markdown("<p style='text-align: center; color: White; font-size:20px;'>Build & Deployed on<span style='font-weight: bold'></span></p>", unsafe_allow_html=True)
    s1,s2=st.columns((2,2))
    with s1:
        st.image('image/002.png')
    with s2:    
        st.image("image/oie_png.png")
#--------------function calling-----------#
if __name__ == "__main__":
    try:
        if selected == 'Content Classifier':
            Text_Classifier()

    except BaseException as error:
        st.error(error)