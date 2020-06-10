import string
def execute(string):
    result=add(string)
    print(result)
def add(stri):
    tlist=[]
    temp=stri.split(sep=";")
    #print(temp)
    temp0=temp[0].split(sep='=')
    temp1=temp[1].split(sep='=')
    temp2=temp[2].split(sep='=')
    a=int(temp0[1])
    b=int(temp1[1])
    c=temp2[1][1]
    result=0
    if c=='+':
        result=a+b
    elif c=='-':
        result=a-b
    elif c=='*':
        result=a*b
    elif c=='/':
        result=a/b
    elif c=='**':
        result=a**b
    return result

execute("a=65;b=20;c=a-b;print c")     
execute("a=65;b=20;c=a+b;print c")     
execute("a=65;b=20;c=a/b;print c")     
execute("a=65;b=20;c=a*b;print c")     
