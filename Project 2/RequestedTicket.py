import random
from datetime import date
from datetime import time
from Ticket import AirlinesReservation
class RequestedTicket(AirlinesReservation):
    def __init__(self):
        self.__status=""
    def getstatus(self):
        return self.__status
    def setstatus(self):
        value=random.choice(['Rejected','Pending','Not Available'])
        self.__status=value
