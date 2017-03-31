#Pet Store Assignment

customerlist = []
petslist = []

class Customer(object):
    def __init__(self,first, last, address, phonenumber, pets=''):
        self.firstname = first
        self.lastname = last
        self.streetaddress = address
        self.phonenumber = phonenumber
        self.petslist = pets
    def __str__(self):
        return "{} {}, pets: {}".format\
                (self.firstname, self.lastname, self.petslist)

class Pets(object):
    def __init__(self, name, animal, food, expectancy, price='sold', owner="notsold"):
        self.petname = name
        self.animaltype = animal
        self.favoritefood = food
        self.lifeexpectancy = expectancy
        self.petprice = price
        self.petowner = owner
    def __str__(self):
        return "{}, Type: {}, Price: {}".format\
                (self.petname, self.animaltype, self.petprice)

JohnB = Customer("John", "Baker", "123 Fake Drive", "123123123", "Rex")
AlJ = Customer("Al", "Jones", "234 Madeup Lane", "77777777", "Squeekers")
BobS = Customer("Bob", "Smith", "456 Unreal Street", "8675309", "Cooper")

Chester = Pets("Chester", "Dog", "Peanut Butter", 12, 250)
Fluffy = Pets("Fluffy", "Cat", "Tuna", 11, 200)
Sandy = Pets("Sandy", "Lizard", "Crickets", 4, 75)
Bubbles = Pets("Bubbles", "Fish", "Fish Food", 1, 20)
Rex = Pets("Rex", "Dog", "Steak", 17, 'sold', JohnB)
Squeekers = Pets("Squeekers", "Mouse", "Cheese", 5, "sold", AlJ)
Cooper = Pets("Cooper", "Cat", "Chicken", 8, "sold", BobS)


customerlist = [JohnB, AlJ, BobS]
petslist = [Chester, Fluffy, Sandy, Bubbles, Rex, Squeekers, Cooper]

running = True
while running:
    x = int(input('''Would you like to:
    1. Calculate the price of an order
    2. Add a customer to the store records
    3. Remove a customer from the store records
    4. Print a list of customers and their pets
    5. Calculate a customer's pets' total life expectancy
    6. Remove a pet from the database
    7. Exit\n'''))
    
    if x == 1:
        ordertotal = 0
        print("Please compose your order")
        print("Type 999 to complete your order.")
        print("Available pets: \n")
        count1 = 1
        for pets in petslist:
            print(count1, pets)
            count1 += 1
        print()
            
        ordering = True
        while ordering:
            choice = int(input("Which pet would you like to add to your order? (Type a number)"))
            if choice == 0:
                print("Your order total is:", ordertotal, "dollars.\n")
                ordering = False
                break
            ordertotal += petslist[(choice - 1)].petprice
            print("Your current order total is:", ordertotal)
        
        
    elif x == 2:
        print("Please enter the following information")
        first = str(input("First name: "))
        last = str(input("Last name: "))
        address = str(input("Address: "))
        phonenumber = str(input("Phone number: "))
        pets = str(input("Current pet: (if none, press Enter)"))           
        first = Customer(first, last, address, phonenumber, pets)    
        customerlist.append(first)
        if pets != '':
            print("Please enter the following information about their pet.")
            name = pets
            animal = str(input("Animal Type: "))
            food = str(input("Favorite food: "))
            expectancy = int(input("Life expectancy: "))
            Pets(name, animal, food, expectancy, price='sold', owner=first)
            petslist.append(name)
        
    elif x == 3:
        print("Current customer list:")
        count3 = 1
        for customers in customerlist:
            print(count3, customers)
            count3 += 1
        print()
        removename = int(input("Who would you like to remove from the database? (Please enter a number)"))
        customerlist.pop((removename - 1))
        print("Customer", removename,"has been removed from the database\n")
        
    elif x == 4:
        print("Current customer list:")
        count4 = 1
        for customers in customerlist:
            print(count4, customers)
            count4 += 1
        print()
            
    elif x == 5:
        print("Current customer list:")
        count5 = 1
        for customers in customerlist:
            print(count5, customers)
            count5 += 1
        expectancychoice = int(input("For whom would you like to calculate the life expectancy of their pets? (Please enter a number):"))
        
    elif x == 6:
        print("Current pets list:")
        count6 = 1
        for pets in petslist:
            print(count6, pets)
            count6 += 1
        print()
        removepetname = int(input("Which pet would you like to remove from the database? (Please enter a number)"))
        petslist.pop((removepetname - 1))
        print("Pet", removepetname,"has been removed from the database\n")
        
    else:
        running = False
        break
