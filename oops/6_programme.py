# class varible


class Car:
    total_car = 0
    def __init__(self,brand,model):
        # self.brand = brand 
        self.__brand = brand   # it make private  varibale
        self.model = model

        Car.total_car += 1

    

class ElectricCar(Car):
    def __init__(self,brand,model,Battry_size):
        super().__init__(brand,model)
        self.Battry_size = Battry_size


    


my_tesla = ElectricCar('Tesla','model s', '85kwh')
Car('tata','safari')
print(Car.total_car)




