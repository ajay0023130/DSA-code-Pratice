# class method(static method) with  propetry

class Car:
    def __init__(self,brand,model):
         
        self.brand = brand   
        self.__model = model

    def Full_Name(self):
        return F'{self.brand} {self.__model}'

    @staticmethod
    def Genral_Info():  #we did't need to pass self in staticmethods
        return 'Cars are means of Transport'

    @property #property  didnot change current attribute name
    def model(self):
        return self.__model

    

        
class ElectricCar(Car):
    def __init__(self,brand,model,Battry_size):
        super().__init__(brand,model)
        self.Battry_size = Battry_size

my_tesla = ElectricCar('Tesla','model s', '85kwh')
# print(Car.Genral_Info())

my_car = Car('tata','safari')
# my_car.model='City'

# print(my_car.model())
print(my_car.model)





