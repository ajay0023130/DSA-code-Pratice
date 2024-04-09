# class method(static method)

class Car:
    def __init__(self,brand,model):
         
        self.brand = brand   
        self.model = model

    def Full_Name(self):
        return F'{self.brand} {self.model}'

    @staticmethod
    def Genral_Info():  #we did't need to pass self in staticmethods
        return 'Cars are means of Transport'

        
class ElectricCar(Car):
    def __init__(self,brand,model,Battry_size):
        super().__init__(brand,model)
        self.Battry_size = Battry_size

my_tesla = ElectricCar('Tesla','model s', '85kwh')
print(Car.Genral_Info())





