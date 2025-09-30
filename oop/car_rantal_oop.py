
class Car:
    def __init__(self,name,modal,year):
        self.name= name
        self.modal=modal
        self.year=year
        self.available=True

    def __str__(self):
        return f"{self.year} {self.modal} {self.name}"
    
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

    def return_car(self, car: Car):
        if car in self.rented_cars:
            self.rented_cars.remove(car)
            car.return_car()   # ✅ mark available again
            return f"You have successfully returned {car.year} {car.modal}"
        return f"You can't return what you didn't borrow"
    
class CarRentalService :
    def __init__(self, name ):
        self.name = name
        self.car_list=[]

    def add_car(self,car:Car):
        self.car_list.append(car)

    def list_cars(self):
        if not self.car_list:
            print("No cars available.")
        else:
            for car in self.car_list:
                status = "Available" if car.available else "Rented"
                print(f"{car} - {status}")
    
    def find_car(self,name,modal):
        for car in self.car_list :
                 if name == car.name and modal == car.modal:
                   return "Available" if car.available else "Rented"
        return "Not found"
            

service = CarRentalService("Speedy Rentals")

car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Tesla", "Model 3", 2023)

print(car2.__str__())

service.add_car(car1)
service.add_car(car2)
# print(service.list_cars())

customer = Customer("Great", "C001")

print(service.find_car("Toyota", "Corolla"))  # Available
customer.rent_car(car1)
print(service.find_car("Toyota", "Corolla"))  # Rented
print(service.find_car("Honda", "Civic"))     # Not found

service.list_cars()
customer.rent_car(car1)
service.list_cars()
customer.rent_car(car1)   # should say already rented
customer.return_car(car1)
service.list_cars()