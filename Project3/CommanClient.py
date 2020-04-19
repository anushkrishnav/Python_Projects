from Country import country
from India import India
from US import USA

class Fun_call():
    def call():
        print("-------Runtime Polymorphism-------")
        print("Country Parent")
        country.capital()
        country.language()
        country.status()
        print("India")
        India.capital()
        India.language()
        India.status()
        print("USA")
        USA.capital()
        USA.language()
        USA.status()