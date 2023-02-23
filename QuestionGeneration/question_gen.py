import streamlit as st
from streamlit_option_menu import option_menu
import os
import math
import docx 
import source.title_1 as head
import source.clear_content as cr
import QuestionGeneration.text_file as txt
import QuestionGeneration.split_prompt as spilt
import source.GPT_3 as gpt
import QuestionGeneration.final_prompt as final_pro
import QuestionGeneration.pdf as pdf
import QuestionGeneration.pdf_textretrive as pdf_retrive
import openai
from docx import Document
import QuestionGeneration.word_doc_que_gen as word_que
import source.to_pdf as cnvt

def quens_gen():
    head.title()
    st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to Question Generator    </p>", unsafe_allow_html=True)
    st.markdown("<hr style=height:2.5px;background-color:gray>",unsafe_allow_html=True)
    w12,col11,col22,w22=st.columns((1,2,2,1))
    up1,up2,up3=st.columns((1,2,1))
    w1,col1,col2,w2=st.columns((1,2,2,1))
    us1,bc1,bc2,us2=st.columns((4,3,3,6))

    c2,c1,c3=st.columns((1,2,1))
    openai.api_key = os.environ["API_KEY"]
    with col11:
        st.markdown("")
        st.write("# Input Type")   
    with col22:
        vAR_input_file_select = st.selectbox("",["Select","Files","Passage"],key="Clear_quetype")
        # file operations
        if  vAR_input_file_select == "Files":
            with col11:
                st.write("### ")
                st.write("# File Types")
            vAR_input_txt_pdf = st.selectbox("",["Select","Text file","PDF file"],key="Clear_txt_pdf")
            # txt file operations
            if vAR_input_txt_pdf =="Text file":
                with col11:
                    st.write("# ")
                    st.write("## ")
                    st.write("# Upload Here")
                with col1:
                        st.markdown("")
                        st.write("# Question Type")
                with col2:
                    vAR_input_quetype = st.selectbox("",["Select","Fill in the blanks","Multiple choices questions","True or False","Match the following"],key="Clear_inputfile") 
                with col22:
                    prompt_file_txt = st.file_uploader("")
                if prompt_file_txt:
                    txt_content = prompt_file_txt.getvalue().decode("utf-8")
                    to_split_content=spilt.fullstr(txt_content)
                    with bc1:    
                        st.markdown("")
                        if st.button("Submit"):
                            #Creating a new word document.
                            vAR_new_doc = docx.Document()
                            fin_txt = ""
                            for split_content in to_split_content:
                                
                                txt_prompt = txt.txt_file(split_content,vAR_input_quetype)
                                vAR_responce = gpt.generate_response3(txt_prompt)
                                fin_txt =fin_txt + vAR_responce
                            vAR_final_docs = word_que.heading_content_que_gen(vAR_new_doc,fin_txt,vAR_input_quetype)
                            with c1:
                                st.write("# ")
                                st.info("Response saved to "+vAR_input_quetype+".docx")
                                vAR_final_docs.save(str(vAR_input_quetype)+".docx")
                                cnvt.convertFiletoPDF(str(vAR_input_quetype)+".docx")
                                st.info("Response saved to "+vAR_input_quetype+".pdf")
                    with bc2:
                        st.markdown("")
                        st.button("Clear", on_click=cr.clear_text)
            # pdf file operatons 
            elif vAR_input_txt_pdf =="PDF file":
                with col11:
                    st.write("# ")
                    st.write("## ")
                    st.write("# Upload Here")
                with col1:
                        st.markdown("")
                        st.write("# Question Type")
                with col2:
                    vAR_input_quetype = st.selectbox("",["Select","Fill in the blanks","Multiple choices questions","True or False","Match the following"],key="Clear_inputfile") 
                prompt_file_pdf  = st.file_uploader("", type="pdf")
                with bc1:    
                    st.markdown("")
                    if st.button("Submit"):
                        if prompt_file_pdf is not None:
                            pdf.header_footer_cuter(prompt_file_pdf)
                            pdf_content = pdf_retrive.pdf_text()
                            #pdf_summary = summ.summarizing(pdf_content)
                            to_split_content=spilt.fullstr(pdf_content)
                            os.remove("Result//newfile.txt")
                            #Creating a new word document.
                            vAR_new_doc = docx.Document()
                            fin_txt = ""
                            for split_content in to_split_content:
                                split_content = gpt.summarizing(split_content)
                                
                                txt_prompt = txt.txt_file(split_content,vAR_input_quetype)
                                vAR_responce = gpt.generate_response3(txt_prompt)
                                fin_txt =fin_txt + vAR_responce
                            vAR_final_docs = word_que.heading_content_que_gen(vAR_new_doc,fin_txt,vAR_input_quetype)
                            with c1:
                                st.write("# ")
                                st.info("Response saved to "+vAR_input_quetype+".docx")
                                vAR_final_docs.save(str(vAR_input_quetype)+".docx")
                                cnvt.convertFiletoPDF(str(vAR_input_quetype)+".docx")
                                st.info("Response saved to "+vAR_input_quetype+".pdf")
                    with bc2:
                        st.markdown("")
                        st.button("Clear", on_click=cr.clear_text)
        # Passage operations
        elif  vAR_input_file_select == "Passage":
            with col1:
                    st.markdown("")
                    st.write("# Question Type")
            with col11:
                st.markdown("### ")
                st.write("# Enter the Passage")
            vAR_passage = st.text_area("",key = "Clear_input_para")
            to_split_content=spilt.fullstr(vAR_passage)
            with col2:
                    vAR_input_quetype = st.selectbox("",["Select","Fill in the blanks","Multiple choices questions","True or False","Match the following"],key="Clear_inputfile") 
            with bc1:    
                st.markdown("")
                if st.button("Submit"):
                    #Creating a new word document.
                    vAR_new_doc = docx.Document()
                    fin_txt = ""
                    for split_content in to_split_content:
                        txt_prompt = txt.txt_file(split_content,vAR_input_quetype)
                        vAR_responce = gpt.generate_response3(txt_prompt)
                        fin_txt =fin_txt + vAR_responce
                    vAR_final_docs = word_que.heading_content_que_gen(vAR_new_doc,fin_txt,vAR_input_quetype)
                    with c1:
                        st.write("# ")
                        st.info("Response saved to "+vAR_input_quetype+".docx")
                        vAR_final_docs.save(str(vAR_input_quetype)+".docx")
                        cnvt.convertFiletoPDF(str(vAR_input_quetype)+".docx")
                        st.info("Response saved to "+vAR_input_quetype+".pdf")
                with bc2:
                        st.markdown("")
                        st.button("Clear", on_click=cr.clear_text)
        
                