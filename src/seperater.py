

def spliter(string):
    lis= string.split()
    prompt=[]
    for i in range(0,len(lis),400):
        prompt.append(" ".join(lis[i:i+400]))
    
    # print(rows)
    return prompt

