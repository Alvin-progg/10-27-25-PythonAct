

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_pay(self):
        pass

class HourlyEmployee(Employee):
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def calculate_pay(self):
        return self.hours * self.rate

class SalariedEmployee(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_pay(self):
        return self.salary

# Example usage:
if __name__ == "__main__":
    hourly = HourlyEmployee("John", 40, 20)
    salaried = SalariedEmployee("Jane", 3000)
    
    print(f"{hourly.name} - Hourly Employee Pay: ${hourly.calculate_pay()}")
    print(f"{salaried.name} - Salaried Employee Pay: ${salaried.calculate_pay()}")
    

