#Price with tax calculator with whiles

pretaxprice=float(input("How much does the item cost?"))

while pretaxprice <= 0:
    print("Please reenter a positive cost.")
    pretaxprice=float(input("How much does the item cost?"))

taxrate=float(input("What is the percent sales tax?"))

while taxrate < 0:
    print("Please reenter a positive tax rate.")
    taxrate=float(input("What is the percent sales tax?"))


taxdecimal=(taxrate)/100
posttaxprice=(pretaxprice)*(1 + taxdecimal)
    
print("After tax, your item will cost",posttaxprice,"dollars.")
