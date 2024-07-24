class Car:
    #Initializer/ Constructor
    def __init__(self, name, mileage, color):
        self.name = name
        self.mileage = mileage
        self.color = color
   
    #Setter     
    def set_values(self):
        name = input("Enter the name: ")
        mileage = int(input("Enter the mileage: "))
        color = input("Enter the color: ")
        self.name = name
        self.mileage = mileage
        self.color = color
    
    #Getter    
    def get_values(self):
        return(self.name, self.mileage, self.color)
        
    #Deleter
    def delete_mileage(self):
        del self.mileage
        
car1 = Car("BMW", 15, "White")
print(car1.__dict__)

car1.set_values()
name, mileage, color = car1.get_values()
print(name, mileage, color)

car1.delete_mileage()
print(car1.__dict__)
