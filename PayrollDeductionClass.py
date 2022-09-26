

class Payroll:

    def __init__(self,desc,date,charge,empID):

        self.__desc = desc
        self.__date = date
        self.__charge =  charge
        self.__empID = empID


    def set_desc(self,desc):
        self.__desc = desc

    def set_date(self,date):
        self.__date = date

    def set_charge(self,charge):
        self.__charge = charge

    def set_empID(self,empID):
        self.__empID = empID

    #####################################


    def get_desc(self):
        return self.__desc

    def get_date(self):
        return self.__date

    def get_charge(self):
        return self.__charge

    def get_empID(self):
        return self.__empID


