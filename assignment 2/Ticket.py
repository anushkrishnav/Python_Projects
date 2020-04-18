from datetime import date,time
class AirlinesReservation():
    def __init__(self):
        self.__flightnumber=""
        self.__date=date(2000,1,1)
        self.__time=time(0,0,0)
        self.__destination=""
    def getFlightNumber(self):
        return self.__flightnumber
    def getDepDate(self):
        return self.__date
    def getDepTime(self):
        return self.__time
    def getDestination(self):
        return self.__destination
    def setFlightNumber(self,value):
        self.__flightnumber=value
    def setDepDate(self,value):
        self.__date=value
    def setDepTime(self,value):
        self.__time=value
    def setDestination(self,value):
        self.__destination=value

