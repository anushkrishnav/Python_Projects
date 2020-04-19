import random
from datetime import date,time
from Ticket import AirlinesReservation
from ConfirmedTicket import ConfirmedTicket
from RequestedTicket import RequestedTicket

class UserMenu():
    def __init__(self):
        pass
    def BookingTicket(self):
        #functional pointer
        fun_pt1=ConfirmedTicket
        fun_pt2=RequestedTicket
        user=random.choice([fun_pt1,fun_pt2])
        if user == fun_pt1:
            user=ConfirmedTicket()
            user.setFlightNumber("A101")
            user.setDepDate(date(2001,1,1))
            user.setDepTime(time(1,1,1))
            user.setDestination("chennai")
            user.setseatno()
            print("------Your ticket is confirmed--------")
            print("Departure date \t:",user.getDepDate())
            print("Departure time \t:",user.getDepTime())
            print("Destination \t:",user.getDestination())
            print("Flight number \t:",user.getFlightNumber())
            print("Seat number \t:",user.getseatno())
            print("---------------------------------------\n")
            print("\tHave a safe journey\n")
            print("---------------------------------------") 
        else :
            user=RequestedTicket()
            user.setFlightNumber("A101")
            user.setDepDate(date(2001,1,1))
            user.setDepTime(time(1,1,1))
            user.setDestination("chennai")
            user.setstatus()
            print("------Booking Status--------")
            print("Departure date \t:",user.getDepDate())
            print("Departure time \t:",user.getDepTime())
            print("Destination \t:",user.getDestination())
            print("Flight number \t:",user.getFlightNumber())
            print("Status \t:",user.getstatus())
            print("---------------------------------------\n")
            print("\tHave Patience\n")
            print("---------------------------------------")
