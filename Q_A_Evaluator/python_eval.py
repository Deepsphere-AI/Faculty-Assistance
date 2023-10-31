import os
import openai
import streamlit as st
from Q_A_Evaluator.model import PythonEvaluator,DescriptiveAnswerEval
import source.title_1 as head

def evaluator():
    head.title()
    st.markdown("<p style='text-align: center; color: black; font-size: 20px; margin-top: -30px ;'>A personalized assessment platform powered by Large Language Model (LLM)</p>", unsafe_allow_html=True)
    st.markdown("<hr style=height:2.5px;margin-top:0px;background-color:gray;>",unsafe_allow_html=True)
    w1,col1,col2,w2=st.columns((1.5,2,2.5,0.7))
    w12,col11,col22,w22=st.columns((1.5,2,2.5,0.7))
    with col1:
        st.write("#")
        st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: 600'>Select Functionality</span></p>", unsafe_allow_html=True)
    with col2:
        type_of_evaluator= st.selectbox("",["Select","Python Evaluator","Assessment Evaluator"])
    if type_of_evaluator=="Python Evaluator":
        with col1:
            st.write("#")
            st.write("#")
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: 600'>Model Input (File Upload)</span></p>", unsafe_allow_html=True)
        with col2:
            vAR_file_input = st.file_uploader("", type=['txt'],key="upload1")
        if vAR_file_input != None:
            vAR_filename= vAR_file_input.name
            vAR_file_content=vAR_file_input.getvalue().decode("utf-8")
            with col2:
                st.write()
                st.code(vAR_file_content)
            with col2:
                if st.button("Submit"):
                    res=""
                    eval_response=PythonEvaluator(vAR_filename,vAR_file_content)
                    for i in eval_response:
                        res=res+i
                    with col2:
                        st.success(res)
    if type_of_evaluator=="Assessment Evaluator":
        with col1:
            st.write("#")
            st.write("#")
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: 600'>Actual Answer (File Upload)</span></p>", unsafe_allow_html=True)
        with col2:
            vAR_actual_file = st.file_uploader(" ", type=['txt'],key="upload2")
        if vAR_actual_file != None:
            vAR_actual_ans=vAR_actual_file.getvalue().decode("utf-8")
            with col2:
                st.write()
                st.write(vAR_actual_ans)
        with col11:
            st.write("#")
            st.write("### ")
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: 600'>Student Answer (File Upload)</span></p>", unsafe_allow_html=True)
        with col22:
            vAR_student_file = st.file_uploader(" ", type=['txt'],key="upload3")
            if vAR_student_file!=None:
                vAR_student_ans=vAR_student_file.getvalue().decode("utf-8")
                with col22:
                    st.write()
                    st.write(vAR_student_ans)
        with col22:
            if vAR_student_file!=None and vAR_actual_file!=None:
                if st.button("Submit"):
                    Desc_answer_obj=DescriptiveAnswerEval(vAR_actual_ans,vAR_student_ans)
                    # st.write(type(Desc_answer_obj))
                    result=""
                    for i in Desc_answer_obj:
                        result=result+i
                    st.success(result)








