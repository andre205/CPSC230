    #Store inventory assignment

descrip = {}
price = {}
quant = {}
items = []

entering = True

while entering:
    x = int(input("Enter an item ID: "))
    if x > 0:
        items.append(x)
        descrip[x] = input("What is it?")
        price[x] = float(input("How much does it cost?"))
        quant[x] = int(input("How many are in stock?"))
    elif x < 0:
        entering = False
        choosing = True


while choosing:
    choice = int(input('''Would you like to
    1. Get the description, price, and stock of an item?
    2. Get the price for an order?
    3. Exit?'''))
    if choice == 1:
        one = int(input("Enter an item ID: "))
        print("Item", one, "is",descrip[one],", it costs", price[one], "and there are", quant[one], "in stock.")
    elif choice == 2:
        ordering = True
        total = 0
        print("Please compose your order. To stop entering, type 0, rather than an item ID.")
        while ordering:
            itemid = int(input("Enter an item ID: "))
            if itemid == 0:
                ordering = False
                break
            itemquant = int(input("How many would you like? "))            
            if quant[itemid] < itemquant:
                print("Sorry, there are not enough in stock. Please reenter the item ID and choose a new quantity.")
            elif quant[itemid] > itemquant:
                total += (price[itemid] * itemquant)
        print("Your order total is", total)
    elif choice == 3:
        choosing = False
        break

