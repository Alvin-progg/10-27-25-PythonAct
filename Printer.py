class InkPrinter:
    def __init__(self, model, ink_level):
        self.model = model
        self.ink_level = ink_level  

    def print_document(self, pages):
        ink_needed = pages * 5  
        if self.ink_level >= ink_needed:
            self.ink_level -= ink_needed
            return f"Printed {pages} pages using Ink Printer {self.model}. Remaining ink level: {self.ink_level}%"
        else:
            return "Not enough ink to print the document."

class LaserPrinter:
    def __init__(self, model, toner_level):
        self.model = model
        self.toner_level = toner_level  

    def print_document(self, pages):
        toner_needed = pages * 3  
        if self.toner_level >= toner_needed:
            self.toner_level -= toner_needed
            return f"Printed {pages} pages using Laser Printer {self.model}. Remaining toner level: {self.toner_level}%"
        else:
            return "Not enough toner to print the document."

if __name__ == "__main__":
    ink_printer = InkPrinter("HP InkJet", 80)
    laser_printer = LaserPrinter("Canon Laser", 60)

    print(ink_printer.print_document(10))
    print(laser_printer.print_document(10))
