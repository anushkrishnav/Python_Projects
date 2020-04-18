import random
from datetime import date
from datetime import time
from Ticket import AirlinesReservation
class ConfirmedTicket(AirlinesReservation):
    def __init__(self):
        self.__seatno=[]
    def getseatno(self):
        return self.__seatno
    def setseatno(self):
        value=[chr(random.randint(ord('I'), ord('Z'))),random.randint(1,25)]
        stri=" ".join([str(elem) for elem in value])
        self.__seatno=stri

