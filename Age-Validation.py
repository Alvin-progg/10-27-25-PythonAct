class Person:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Age must be a non-negative integer.")
        self._age = value

if __name__ == "__main__":
    try:
        person = Person(25)
        print(f"Person's age: {person.age}")

        person.age = 30
        print(f"Updated person's age: {person.age}")

        person.age = -5  
    except ValueError as e:
        print(e)