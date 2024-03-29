# class variables - 6. Class Variables
# Problem: Add a class variable to Car that keeps track of the number of cars created.


class Car:

    total_car = 0 # will be used to calculate no of times this class is used

    def __init__(self,brand,model):
        self.__mybrand = brand # if varailble start with __ it can't be called or not give any output outside class called encapsulation
        self.mymodel = model
        Car.total_car += 1

    def get__brand(self):
        return self.__mybrand + "!"

    
    def full_name(self):
        # return self.mybrand + " "+ self.mymodel
        return f"{self.__mybrand}  {self.mymodel}"
    
    def fuel_type(self):
        return "Petrol or Diesel !"
    


class ElectricCar(Car):

    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric charge"



my_tesla = ElectricCar("Tesla","Model S", "85kWh")
print(my_tesla.full_name())
# print(my_tesla.__mybrand)
print(my_tesla.mymodel)
print(my_tesla.fuel_type())

safari = Car("Tata","Safari")
print(safari.get__brand())
print(safari.fuel_type())

safariThree = Car("3tata","New-car")
print(safariThree.get__brand())

print(Car.total_car)
print(Car.total_car)

# my_car = Car("Toyota","Corolla")
# print(my_car)
# print(my_car.mybrand)
# print(my_car.mymodel)
# print(my_car.full_name())