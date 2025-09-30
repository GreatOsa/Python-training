
class Car:
    def __init__(self,name,modal,year):
        self.name= name
        self.modal=modal
        self.year=year
        self.available=True

    def __str__(self):
        return f"{self.year} {self.modal}"
    
    def rent(self):
        if self.available :
            self.available=False
            return True
        return False
    
    def return_car(self):
        self.available=True

class Customer :
    def __init__(self, name, customer_id,):
        self.name=name
        self.customer_id=customer_id
        self.rented_cars = []

    def rent_car(self,car:Car):
        if car.available :
            self.rented_cars.append(car)
            car.available=False
            return f"you just rented the {car.year} {car.modal}"
        return f"{car.year} {car.modal} is already taken"
    
    def return_car(self, car:Car):
        if car in self.rented_cars:
            self.rented_cars.remove(car)
            return f"you have successfull return {car.year} {car.modal}"
        return f"you can't return what you didn't borrow "
    
class CarRentalService :
    def __init__(self, name ):
        self.name = name
        self.car_list=[]

    def add_car(self,car:Car):
        self.car_list.append(car)

    def list_cars(self):
        return self.car_list
    
    def find_car(self,make,car:Car):
        for car.make in self.car_list :
            for car.model in self.car_list:
                 if car.modal in self.car_list:
                   return "Available"
                 return "Not found"
            

service = CarRentalService("Speedy Rentals")

car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Tesla", "Model 3", 2023)

# service.add_car(car1)
# service.add_car(car2)

# customer = Customer("Great", "C001")

# service.list_cars()
# customer.rent_car(car1)
# service.list_cars()
# customer.rent_car(car1)   # should say already rented
# customer.return_car(car1)
# service.list_cars()