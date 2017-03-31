#Price with tax calculator with nested ifs

pretaxprice=float(input("How much does the item cost?"))

if pretaxprice >= 0:
    taxrate=float(input("What is the percent sales tax?"))
    if taxrate >= 0:
        taxdecimal=(taxrate)/100

        posttaxprice=(pretaxprice)*(1 + taxdecimal)
    
        print("After tax, your item will cost",posttaxprice,"dollars.")
    elif taxrate < 0:
        print("You've entered an invalid tax rate.")
elif pretaxprice < 0:
    print("You've entered an invalid price.")
