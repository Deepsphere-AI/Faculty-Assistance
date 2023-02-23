
def fillup(prompt):
    fillup_f = open("source/prompt_fillup.txt", "r")
    fill=fillup_f.read()
    return fill+"\n Generate 5 fill in the blanks questions with answer as blank space for below content: "+prompt
def mcq(prompt):
    multi_f = open("source/prompt_mcq.txt", "r")
    multi=multi_f.read()
    return multi+"\n Generate 5 multiple choice question with answer for below content: "+prompt
def trf(prompt):
    torf_f = open("source/prompt_trf.txt", "r")
    trfa=torf_f.read()
    return trfa+"\n generate 5 True or False questions for below content: "+prompt
def matc(prompt):
    mtf_f = open("source/prompt_match.txt", "r")
    mtf=mtf_f.read()
    return mtf+"\n generate 5 Match the follwing for the given content below: "+prompt
    