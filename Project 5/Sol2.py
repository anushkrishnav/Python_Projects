import string
def wordcount(string):
    list1=string.split(sep=" ")
    return len(list1)

def Reverse(string):
    stri=(string)[::-1]
    return stri

print(wordcount("Tom and Jerry are good friends"))
print(Reverse("Tom and Jerry are good friends"))
