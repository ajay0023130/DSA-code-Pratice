
#Inheritance example
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def Full_Name(self):
        return F'{self.brand} {self.model}'
        


class ElectricCar(Car):
    def __init__(self,brand,model,Battry_size):
        super().__init__(brand,model)
        self.Battry_size = Battry_size


my_tesla = ElectricCar('Tesla','model s', '85kwh')
print(my_tesla.Battry_size)
print(my_tesla.model)
print(my_tesla.brand)
print(my_tesla.Full_Name())

