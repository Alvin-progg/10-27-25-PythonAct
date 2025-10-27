class Vehicle:
    def __init__(self , brand , fuel:int):
        self.brand = brand
        self.fuel = fuel

class Car(Vehicle):
    def __init__(self, brand, fuel:int , doors:int):
        super().__init__(brand, fuel)
        self.doors = doors


    def Drive(self, distance: int):
        fuel_needed = distance * 0.1
        if self.fuel > fuel_needed:
            self.fuel -= fuel_needed
            print(f"Driven {distance} km. Remaining fuel: {self.fuel}")
        else:
            print("Not enough fuel to drive.")

        return f"{self.brand} car with {self.doors} doors is driving."


if __name__ == "__main__":
    my_car = Car("Toyota", 50, 4)
    print(my_car.Drive(50))