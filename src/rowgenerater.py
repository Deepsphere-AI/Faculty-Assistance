

def rowgen(prompt):
    pmt=len(prompt)
    rows=[]
    num=1 
    new=400
    for i in range(pmt):
        ans=str(num)+" to "+ str(new)+" words"
        rows.append(ans)
        num,new = new+1,new+400
    return rows