import streamlit as st
from src.web_Scapper import find_the_input
from src.seperater import spliter
from src.rowgenerater import rowgen
from src.web_Scapper import get_paragraphs
from src.pdf import header_footer_cuter
from src.pdf_textretrive import pdf_text,text_retrive
from src.table_design import table
import pandas as pd
def prev1():
    st.session_state['preview1']="No"
def prev2():
    st.session_state['preview2']="No"
def prev3():
    st.session_state['preview3']="No"


def Text_Classifier():
    w1,col1,col2,w2=st.columns((1.5,2.5,4,.1))
    cc2,cc1,cc3=st.columns((2,6,0.2))
    col11,col22,col33=st.columns((2,8,0.2))
    with col1:
        st.write("## ")
        st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Select Model</span></p>", unsafe_allow_html=True)
    with col2:
        vAR_Model = ['Select','GPT-3','GPT-3.5','GPT-4']
        vAR_input_model = st.radio(' ',vAR_Model,horizontal=True)
    if vAR_input_model!="Select":
        with col1:
            st.write("### ")
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Model Input Type</span></p>", unsafe_allow_html=True)
        with col2:
            vAR_input = st.radio('',['Direct User Entry','File Upload','Web URL'],horizontal=True)

        # Text input
        if vAR_input == 'Direct User Entry':
            with col1:
                st.write('# ')
                st.write('# ')
                st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Model Input Text</span></p>", unsafe_allow_html=True)
            with col2:
                vAR_text = st.text_area('')
                vAR_text = ' '.join(vAR_text.split())
            if vAR_text !="":
                with col2:
                    st.markdown("")
                    st.markdown("")
                    if st.button("Submit"):
                        if len(vAR_text)<400:
                            vAR_response = find_the_input(vAR_text)
                            with col2:
                                st.success(vAR_response)
                        else:
                            prompt=spliter(vAR_text)
                            result=[]
                            for j in prompt:
                                vAR_response = find_the_input(j)
                                result.append(vAR_response)
                            default=rowgen(result)
                            with col22:
                                df=pd.DataFrame({"Word Count in the Given Text":default,"Model Outcome (Classification/Prediction)":result})
                                st.markdown("## ")
                                table_style=table(df)
                                # Display the table using HTML
                                st.write(table_style, unsafe_allow_html=True)
        # files format
        elif vAR_input == 'File Upload':
            with col1:
                st.write('# ')
                st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Select File Format</span></p>", unsafe_allow_html=True)
            with col2:
                vAR_file_type = st.selectbox("",['Select','Text file','PDF file'])
            
            
            # Text file
            if vAR_file_type == 'Text file':
                with col1:
                    st.write('### ')
                    st.write('# ')
                    st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Upload File</span></p>", unsafe_allow_html=True)
                with col2:
                    vAR_file = st.file_uploader('',type='txt')
                if vAR_file is not None:
                    txt_content = text_retrive(vAR_file)
                    with col1:
                        st.write('# ')
                        st.write('# ')
                        st.write("## ")
                        st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Preview</span></p>", unsafe_allow_html=True)
                    with col2:
                        vAR_preview1 = st.selectbox("",['Select','Yes','No'],key='preview1')
                    with col22:
                        if vAR_preview1 == 'Yes':
                            st.write(txt_content)
                        elif vAR_preview1 == 'No':
                            pass
                        else:
                            pass
                    txt_content = ' '.join(txt_content.split())
                    if vAR_preview1 != "Select":
                        with col2:
                            try:
                                st.markdown("")
                                st.markdown("")
                                if st.button("Submit",on_click=prev1):
                                    if len(txt_content)<400:
                                        vAR_response = find_the_input(txt_content)
                                        with col2:
                                            st.success(vAR_response)
                                    else:
                                        prompt=spliter(txt_content)
                                        result=[]
                                        for j in prompt:
                                            vAR_response = find_the_input(j)
                                            result.append(vAR_response)
                                        default=rowgen(result)
                                        with col22:
                                            df=pd.DataFrame({"Word Count in the Given Text":default,"Model Outcome (Classification/Prediction)":result})
                                            st.markdown("## ")
                                            table_style=table(df)
                                            # Display the table using HTML
                                            st.write(table_style, unsafe_allow_html=True)
                                            #st.dataframe(df)
                            except Exception as e:
                                st.error("Text cannot be extracted from Uploaded File")
            # PDF file
            elif vAR_file_type == 'PDF file':
                with col1:
                    st.write('### ')
                    st.write('# ')
                    st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Upload File</span></p>", unsafe_allow_html=True)
                with col2:
                    vAR_file = st.file_uploader('',type='pdf')
                if vAR_file is not None:
                    try:
                        header_footer_cuter(vAR_file)
                        vAR_pdf_content = pdf_text()
                        with col1:
                            st.write('# ')
                            st.write('# ')
                            st.write("# ")
                            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Preview</span></p>", unsafe_allow_html=True)

                        with col2:
                            vAR_preview2 = st.selectbox("",['Select','Yes','No'],key='preview2')
                        with col22:
                            if vAR_preview2 == 'Yes':
                                st.write(vAR_pdf_content)
                            elif vAR_preview2 == 'No':
                                pass
                            else:
                                pass
                        vAR_pdf_content = ' '.join(vAR_pdf_content.split())
                        if vAR_preview2 != "Select":
                            with col2:
                                st.markdown("")
                                st.markdown("")
                                if st.button("Submit",on_click=prev2):
                                    if len(vAR_pdf_content)<400:
                                        vAR_response = find_the_input(vAR_pdf_content)
                                        with col2:
                                            st.success(vAR_response)
                                    else:
                                        prompt=spliter(vAR_pdf_content)
                                        result=[]
                                        for j in prompt:
                                            vAR_response = find_the_input(j)
                                            result.append(vAR_response)
                                        default=rowgen(result)
                                        with col22:
                                            df=pd.DataFrame({"Word Count in the Given Text":default,"Model Outcome (Classification/Prediction)":result})
                                            st.markdown("## ")
                                            table_style=table(df)
                                            # Display the table using HTML
                                            st.write(table_style, unsafe_allow_html=True)
                    except Exception as e:
                        st.error("Text cannot be extracted from Uploaded File")
        # websit input
        elif vAR_input =='Web URL':
            with col1:
                st.write('# ')
                st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Enter Valid Web URL</span></p>", unsafe_allow_html=True)
            with col2:
                vAR_link = st.text_input('')
            if vAR_link !="":
                vAR_text = get_paragraphs(vAR_link)
                with col1:
                    st.write('# ')
                    # st.write('# ')
                    # st.write("## ")
                    st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Preview</span></p>", unsafe_allow_html=True)
                with col2:
                    vAR_preview3 = st.selectbox("",['Select','Yes','No'],key='preview3')
                with col22:    
                    if vAR_preview3 == 'Yes':
                        st.write(vAR_text)
                    elif vAR_preview3 == 'No':
                        pass
                    else:
                        pass
                vAR_text = ' '.join(vAR_text.split())
                if vAR_preview3 != "Select":
                    with col2:
                        try:
                            st.markdown("")
                            st.markdown("")
                            if st.button("Submit",on_click=prev3):
                                if len(vAR_text)<400:
                                    vAR_response = find_the_input(txt_content)
                                    with col2:
                                        st.success(vAR_response)
                                else:
                                    prompt=spliter(vAR_text)
                                    result=[]
                                    for j in prompt:
                                        vAR_response = find_the_input(j)
                                        result.append(vAR_response)
                                    default=rowgen(result)
                                    with col22:
                                        df=pd.DataFrame({"Word Count in the Given Text":default,"Model Outcome (Classification/Prediction)":result})
                                        st.markdown("## ")
                                        table_style=table(df)
                                        # Display the table using HTML
                                        st.write(table_style, unsafe_allow_html=True)
                        except Exception as e:
                            st.error("Text cannot be extracted from Uploaded URL")
