# Class: Car
class Car:
    """
    This class represents a Car with attributes: make, model, and year.
    It includes a method to display the car's information.
    """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        """
        This method prints the car's information.
        """
        print(f"Car: {self.year} {self.make} {self.model}")

# User input for Car class
print("\n--- Car Class ---")
make = input("Enter car make: ")
model = input("Enter car model: ")
year = int(input("Enter car year: "))

my_car = Car(make, model, year)
print("Car information:")
my_car.display_info()
