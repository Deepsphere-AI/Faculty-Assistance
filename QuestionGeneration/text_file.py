import streamlit as st
import QuestionGeneration.question_gen as qg
import QuestionGeneration.final_prompt as final



def txt_file(txt_content,vAR_input_quetype):
    if vAR_input_quetype == "Fill in the blanks":
        return final.fillup(txt_content)
    if vAR_input_quetype == "Multiple choices questions":
        return final.mcq(txt_content)
    if vAR_input_quetype == "True or False":
        return final.trf(txt_content)
    if vAR_input_quetype == "Match the following":
        return final.matc(txt_content)

