import random
from Post import Post
from datetime import date
class ApplicationForm():
    def __init__(self):
        self.__id=0
        self.__name=""
        self.__interviewDate=date(2020,1,1)
        self.__post=""
    def Getpost(self):
        return self.__post
    def Setpost(self):
        value=Post.RANDOM()
        self.__post=value
    def Status(self):
        k=(random.choice(["Selected"," in Waiting list","Rejected"]))
        return k
    def GetID(self):
        return self.__id
    def SetID(self,value):
        self.__id=value
    def GetInterviewDate(self):
        return self.__interviewDate
    def SetInterviewDate(self,value):
        self.__interviewDate=value
    def GetName(self):
        return self.__name
    def SetName(self,value):
        self.__name=value
