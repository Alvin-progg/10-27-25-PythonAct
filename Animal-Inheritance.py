class Animal:
    def speak(self):
        return self

class Dog(Animal):
    def speak(self):
        print("Woof!")
        print("Bark!")
        print("Growl!")

class Cat(Animal):
    def speak(self):
        print("Meow!")
        print("Purr!")
        print("Hiss!")

if __name__ == "__main__":
    dog = Dog()
    cat = Cat()
    print(dog.speak())  
    print(cat.speak())  


