import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(layout="wide")
import math
from PIL import Image
import source.title_1 as head
import QuestionGeneration.question_gen as ques
import ContentGeneration.content_generation as cont_gen
import os
import openai
openai.api_key = os.environ["API_KEY"]

with open('style/final.css') as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
imcol1, imcol2, imcol3 = st.columns((2,5,3))
with imcol1:
    st.write("")
with imcol2:
    st.image('image/Logo_final.png')
with imcol3:
    st.write("")
#---------Side bar-------#
with st.sidebar:
    selected = st.selectbox("",
                     ['Home',"Question Generation","Content Generation"],key='text')
    Library = st.selectbox("",
                     ["Library Used","Streamlit","Image","Math","Pandas"],key='text1')
    Gcp_cloud = st.selectbox("",
                     ["GCP Services Used","VM Instance","Computer Engine","Cloud Storage"],key='text2')
    st.markdown("")
    def clear_text():
            st.session_state["text"] = "Home"
            st.session_state["text1"] = "Library Used"
            st.session_state["text2"] = "GCP Services Used"
    st.button("Clear/Reset", on_click=clear_text)
#--------------function calling-----------#
if __name__ == "__main__":
    try:
        if selected == "Home":
            head.title()
        if selected == "Question Generation":
            ques.quens_gen()
        if selected == "Content Generation":
            cont_gen.content_gen()
    except BaseException as error:
        st.error(error)