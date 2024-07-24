class Car:

    car_count = 0

    def __init__(self, name, mileage, color):
        self.name = name
        self.mileage = mileage
        self.color = color
        Car.car_count += 1
    
    def display_car(self):
        print(f"Name = {self.name}\nMileage = {self.mileage}\nColor = {self.color}")
    
    def update_car_name(self, name):
        self.name = name
    
    @classmethod
    def display_car_count(cls):
        print(f"Total Cars = {cls.car_count}")

car1 = Car('Marcedes Benz', 2222, 'blue')
car1.display_car()

car2 = Car('Ford', 1111, 'red')
car2.display_car()

car1.update_car_name('Mercedes Benz')
car1.display_car()

Car.display_car_count()

del car1.name  
print(car1.__dict__)

del car1
print(car1.__dict__)
