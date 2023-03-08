import QuestionGeneration.final_prompt as final

def txt_file(txt_content,vAR_input_quetype,serial_no):
    if vAR_input_quetype == "Fill in the blanks":
        return final.fillup(txt_content,serial_no)
    if vAR_input_quetype == "Multiple choices":
        return final.mcq(txt_content,serial_no)
    if vAR_input_quetype == "True or False":
        return final.trf(txt_content,serial_no)
    if vAR_input_quetype == "Match the following":
        return final.matc(txt_content,serial_no)
