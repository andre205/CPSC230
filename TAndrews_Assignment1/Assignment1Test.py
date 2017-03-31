pretaxprice=input("How much does the item cost?")

taxrate=input("What is the sales tax, given as a percent?")

taxdecimal=(taxrate)/100
posttaxprice=(pretaxprice)*(1 + taxdecimal)

print("After tax, your item will cost,",posttaxprice)
