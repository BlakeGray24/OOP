import random


class Insect:


    def __init__(self,w,l):
        self.__wings = w
        self.__legs = l
        self.__flight = 0


    def flight_length(self):
        self.__flight = random.randint(0,10)



    def get_flight(self):
        return self.__flight