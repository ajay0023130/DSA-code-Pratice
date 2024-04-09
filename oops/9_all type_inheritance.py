# Multiple Inheritance

class Emp:
    def __init__(self,name):
        self.name =  name

    

class Dancer:
    def __init__(self,dance):
        self.dance = dance

    


class DancerEmp(Emp,Dancer):
    def __init__(self,name,dance):
        self.name = name
        self.dance = dance

    

o = DancerEmp("kathak","shivani")

print(o.name)
print(o.dance)
