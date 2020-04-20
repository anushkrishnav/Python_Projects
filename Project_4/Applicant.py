from datetime import date
import random
from ApplicationForm import ApplicationForm
class Applicant():
    def __init__(self):
    #def Post(self):
        self.AppPost=random.choice(["Clerk","ProbatioryOfficer"])
    def ApplicationFormDetails(self):
        Appli=ApplicationForm()
        Appli.SetID(random.randint(0,80))
        Appli.SetInterviewDate(date(2020,4,27))
        Appli.SetName(str(input("Enter your name\t :")))
        Appli.Setpost()
        print("-----------",Appli.Getpost(),"Application Form--------")
        print("You are ",Appli.Status())
        print("Name \t\t\t:",Appli.GetName())
        print("I.D\t\t\t:",Appli.GetID())
        print("Attended interview on\t:",Appli.GetInterviewDate())

