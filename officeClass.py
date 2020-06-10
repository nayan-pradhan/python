class Employee:

    def __init__ (self, first, last, phone):
        self.first = first
        self.last = last
        self.phone = phone
        self.email = first.lower() + "." + last.lower() + "@company.com"
    
    def printData(self):
        print("First Name:", self.first)
        print("Last Name:", self.last)
        print("Phone Number:", self.phone)
        print("Email:", self.email)
        print('\n')

Emp1 = Employee("John", "Smith", 123456789)
Emp2 = Employee("Anthony", "Davis", 987654321)
Emp3 = Employee("Jade", "Stone", 545454545)

Emp1.printData()
Emp2.printData()
Emp3.printData()