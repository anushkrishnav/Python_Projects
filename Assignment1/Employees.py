class Employee():
    def __init__(self,Eno=0,Ename="",bs=0.00):    
        self.__set_Empno(Eno)
        self.__set_Ename(Ename)
        self.__set_BasicSalary(bs)

    def __set_Empno(self,value):
        if value< 0:
            raise ValueError("Employee id can't be in negative")
        self.no=value
    def Empno(self):
        return self.no  
    def __set_Ename(self,value):
        if any(i.isdigit() for i in value)==True:
            raise ValueError("Name cannot contain numbers")
        self.name=value
    def Ename(self):
        return self.name
    def __set_BasicSalary(self,value):
        if value< 0:
            raise ValueError("Basic Salary cannot be in negative")
        self.Basicsalary=value
    def BasicSalary(self):
        return self.Basicsalary
    def DA(self):
        amt=self.Basicsalary*0.12
        return amt
    def HRA(self):
        amt=self.Basicsalary*0.20
        return amt
    def IT(self):
        amt=self.Basicsalary*0.15
        return amt
    def PF(self):
        amt=self.Basicsalary*0.12
        return amt
    def GS(self):
        amt=self.HRA()+self.Basicsalary+self.DA()
        return amt
    def NS(self):
        amt=self.GS()-(self.IT()+self.PF())
        return amt