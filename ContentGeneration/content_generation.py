import streamlit as st
from streamlit_option_menu import option_menu
import os
import math
import source.title_1 as head
import openai
import source.clear_content as cr
import source.GPT_3 as gpt
import docx
from docx.shared import RGBColor
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.oxml import OxmlElement, ns
from docx.shared import Inches, Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
import ContentGeneration.title as title
import ContentGeneration.toc as toc
import ContentGeneration.header as header
import ContentGeneration.pagenum as page_num
import ContentGeneration.convert as convert

def content_gen():
    head.title()
    st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to Question Generator    </p>", unsafe_allow_html=True)
    st.markdown("<hr style=height:2.5px;background-color:gray>",unsafe_allow_html=True)
    w12,col11,col22,w22=st.columns((1,2,2,1))
    up1,up2,up3=st.columns((1,2,1))
    w1,col1,col2,w2=st.columns((1,2,2,1))
    us1,bc1,bc2,us2=st.columns((3,4,3,6))
    c2,c1,c3=st.columns((1,2,1))
    with col1:
        st.write("### ")
        st.subheader("Enter a topic")
    with col2:
        vAR_prompt_file = st.text_input("",key="Clear1")
    with bc2:
        st.write("# ")
        st.button("Clear",on_click=cr.clear_text)

    #Giving a not static input and asking gpt3 to generate 25 random topics from the input.  
    vAR_topics_num = 5
    vAR_topics_list = ["Give "+str(vAR_topics_num)+" short topics from basics to advanced order for" + vAR_prompt_file]

    #Defining a prompt to instruct the gpt3 to generate content for each topics about 200 words. 
    vAR_elaborate_prompt = "Elaborate the topic for 200 words without conclusion and without repetition :"

    vAR_conclusion = "Write a conclusion for " + vAR_prompt_file
    #Creating a new word document.
    vAR_new_doc = docx.Document()

    title.title(vAR_new_doc,vAR_prompt_file)
    toc.toc(vAR_new_doc)
    header.header(vAR_new_doc)
    page_num.put_page_num(vAR_new_doc)
    with bc1:
        st.write("# ")
        if st.button("Generate content"):
            # with st.spinner('Processing data...'):
                for one_sentence in vAR_topics_list:
                    vAR_GPT_response_nonstatic = gpt.generate_response(one_sentence)
                    vAR_splitting_response_index = vAR_GPT_response_nonstatic.split("\n")
                    vAR_splitted_response = vAR_GPT_response_nonstatic.split("\n")
                    for topics in vAR_splitted_response:
                        if topics != "":
                            vAR_joined_topics=vAR_elaborate_prompt+topics
                            response_for_non_static = gpt.generate_response(vAR_joined_topics)
                            #response_for_non_static = gpt.summarizing(response_for_non_static)
                            response_for_conc = gpt.generate_response(vAR_conclusion)
                            if response_for_non_static:
                                    headx=vAR_new_doc.add_heading(topics)
                                    headx.style.font.color.rgb = RGBColor(0, 0, 139)
                                    headx.style.font.size = Pt(14)
                                    headx.style.font.bold = True
                                    headx.style.font.all_caps = True
                                    vAR_new_doc.add_paragraph(response_for_non_static)
                    vAR_new_doc.add_heading("Conclusion")
                    vAR_new_doc.add_paragraph(response_for_conc)
                                                    
                
                vAR_new_doc.save(str(vAR_prompt_file)+".docx")
                with c1:
                    st.write("# ")
                    st.info("Response saved to "+vAR_prompt_file+".docx")
                convert.convertFiletoPDF(str(vAR_prompt_file)+".docx")
                with c1:
                    st.write("# ")
                    st.info("Response saved to "+vAR_prompt_file+".pdf")