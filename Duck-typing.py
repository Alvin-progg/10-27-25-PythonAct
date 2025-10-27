def make_it_speak(obj):
    obj.speak()

class Bird:
    def speak(self):
        print("Chirp chirp!")

class Robot:
    def speak(self):
        print("Beep boop!")
make_it_speak(Bird())  
make_it_speak(Robot()) 
#make_it_speak(123)      # Raises AttributeError