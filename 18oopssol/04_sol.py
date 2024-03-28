# encapsulation


class Car:
    def __init__(self,brand,model):
        self.__mybrand = brand # if varailble start with __ it can't be called or not give any output outside class called encapsulation
        self.mymodel = model
    
    def get__brand(self):
        return self.__mybrand + "!"


    # 2nd sol
    
    def full_name(self):
        # return self.mybrand + " "+ self.mymodel
        return f"{self.__mybrand}  {self.mymodel}"
    


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size



my_tesla = ElectricCar("Tesla","Model S", "85kWh")
print(my_tesla.full_name())
# print(my_tesla.__mybrand)
print(my_tesla.mymodel)


# my_car = Car("Toyota","Corolla")
# print(my_car)
# print(my_car.mybrand)
# print(my_car.mymodel)
# print(my_car.full_name())