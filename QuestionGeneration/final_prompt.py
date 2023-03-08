
def fillup(prompt,serial_no):
    fillup_f = open("QuestionGeneration/prompt_fillup.txt", "r")
    fill=fillup_f.read()
    return fill+"\n Generate 5 fill in the blanks questions with answers as blank space for below content with serial numbers"+str(serial_no)+":"+'"'+prompt+'"'
def mcq(prompt,serial_no):
    multi_f = open("QuestionGeneration/prompt_mcq.txt", "r")
    multi=multi_f.read()
    return multi+"\n Generate 5 multiple choice questions with answers for below content with serial numbers"+str(serial_no)+":" +'"'+prompt+'"'
def trf(prompt,serial_no):
    torf_f = open("QuestionGeneration/prompt_trf.txt", "r")
    trfa=torf_f.read()
    return trfa+"\n generate 5 True or False questions with answers for below content with serial numbers"+str(serial_no)+":" +'"'+prompt+'"'
def matc(prompt,serial_no):
    mtf_f = open("QuestionGeneration/prompt_match.txt", "r")
    mtf=mtf_f.read()
    return mtf+"\n generate 5 set of Match the follwing question with answers for below content with serial numbers"+str(serial_no)+":" +'"'+prompt+'"'
    