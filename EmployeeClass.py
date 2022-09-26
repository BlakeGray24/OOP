###employee in attributes: name, ID number, department, job title and monthly salary


from unicodedata import name


class Employee:

    def __init__(self,name,i,dept,job,salary):

        self.__name = name
        self.__id = i
        self.__dept = dept
        self.__job = job
        self.__salary = salary


    ##################################    

    def set_name(self,name):
        self.__name = name

    def set_id(self,i):
        self.__id = i

    def set_dept(self,dept):
        self.__dept = dept

    def set_job(self,job):
        self.__job = job

    def set_salary(self,salary):
        self.__salary = salary

    ##################################

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_dept(self):
        return self.__dept

    def get_job(self):
        return self.__job

    def get_salary(self):
        return self.__salary