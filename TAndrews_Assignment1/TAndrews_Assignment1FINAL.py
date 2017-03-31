#Price with tax calculator

pretaxprice=input("How much does the item cost?")
pretaxprice_float=float(pretaxprice)

taxrate=input("What is the sales tax, given as a percent?")
taxrate_float=float(taxrate)

taxdecimal=(taxrate_float)/100

posttaxprice=(pretaxprice_float)*(1 + taxdecimal)
posttaxprice_str=str(posttaxprice)

print("After tax, your item will cost,",posttaxprice_str)
