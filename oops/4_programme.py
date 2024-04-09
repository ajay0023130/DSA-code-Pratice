# encapsulation example
class Car:
    def __init__(self,brand,model):
        # self.brand = brand 
        self.__brand = brand   # it make private  varibale
        self.model = model

    def Full_Name(self):
        return F'{self.__brand} {self.model}'

    def get_brand(self): # getter method for access value 
        return self.__brand + '?'

        


class ElectricCar(Car):
    def __init__(self,brand,model,Battry_size):
        super().__init__(brand,model)
        self.Battry_size = Battry_size


my_tesla = ElectricCar('Tesla','model s', '85kwh')
print(my_tesla.Battry_size)
print(my_tesla.model)
# print(my_tesla.brand)
print(my_tesla.Full_Name())
print(my_tesla.get_brand())



