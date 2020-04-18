import unittest
from Employees import Employee
em=Employee(1,"anush",100)
da_expectedResult=12
empno_expectedResult=1
empname_expectedResult='anush'
Basicsalary_expectedResult=100
hra_expectedResult=20
it_expectedResult=15
pf_expectedResult=12
gs_expectedResult=132
ns_expectedResult=105
class TestEmployee(unittest.TestCase):
    def test_da(self):
        result=em.DA()
        self.assertEqual(result,da_expectedResult)
        #self.assertNotEqual(result,da_expectedResult)
    def test_empno(self):
        result=em.Empno()
        self.assertEqual(result,empno_expectedResult)
    def test_empname(self):
        result=em.Ename()
        self.assertEqual(result,empname_expectedResult)
    def test_BasicSalary(self):
        result=em.BasicSalary()
        self.assertEqual(result,Basicsalary_expectedResult)
    def test_HRA(self):
        result=em.HRA()
        self.assertEqual(result,hra_expectedResult)
    def test_it(self):
        result=em.IT()
        self.assertEqual(result,it_expectedResult)
    def test_pf(self):
        result=em.PF()
        self.assertEqual(result,pf_expectedResult)
    def test_gs(self):
        result=em.GS()
        self.assertEqual(result,gs_expectedResult)
    def test_ns(self):
        result=em.NS()
        self.assertEqual(result,ns_expectedResult)

        