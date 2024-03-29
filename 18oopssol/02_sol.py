class Car:
    def __init__(self,brand,model):
        self.mybrand = brand
        self.mymodel = model

    # 2nd sol
    
    def full_name(self):
        # return self.mybrand + " "+ self.mymodel
        return f"{self.mybrand}  {self.mymodel}"



my_car = Car("Toyota","Corolla")
print(my_car)
print(my_car.mybrand)
print(my_car.mymodel)
print(my_car.full_name())