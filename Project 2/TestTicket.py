from datetime import date,time
#from unittest import TestCase
from Ticket import AirlinesReservation
from ConfirmedTicket import ConfirmedTicket
from RequestedTicket import RequestedTicket
class TestTicket():
    print("Test parent ")
    a=AirlinesReservation()
    a.setFlightNumber("A101")
    a.setDepDate(date(2001,1,1))
    a.setDepTime(time(1,1,1))
    a.setDestination("chennai")
  
    print(a.getDepDate())
    print(a.getDepTime())
    print(a.getDestination())
    print(a.getFlightNumber())
    print("---------------------------")
    print("Test requested ticket")
    a=RequestedTicket()
    a.setFlightNumber("B201")
    a.setDepDate(date(2020,1,1))
    a.setDepTime(time(1,1,1))
    a.setDestination("chennai")
  
    print(a.getDepDate())
    print(a.getDepTime())
    print(a.getDestination())
    print(a.getFlightNumber())
    print("------------------------------")
    print("Test confirmed ticket")
    a=ConfirmedTicket()
    a.setFlightNumber("C301")
    a.setDepDate(date(2001,1,1))
    a.setDepTime(time(1,1,1))
    a.setDestination("Coimbatore")
  
    print(a.getDepDate())
    print(a.getDepTime())
    print(a.getDestination())
    print(a.getFlightNumber())