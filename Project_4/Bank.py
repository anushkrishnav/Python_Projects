from Applicant import Applicant
from Post import Post
class Bank():
    def __init__(self):
        pass
    def BankPost(self):
        Post1=Post.Clerk
        Post2=Post.ProbatioryOfficer
        print("-----------------Available post Status-----------------------")
        print(Post1)
        print(Post2)
        WantApply=str(input("Want to Check your status ?? (Y/N) ")).strip().lower()
        if WantApply == "y":
            ApplicantClient=Applicant()
            ApplicantClient.ApplicationFormDetails()
        else :
            print("goodluck,BYE")
