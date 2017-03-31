#Price with tax calculator

pretaxprice=input("How much does the item cost?")
pretaxprice_int=int(pretaxprice)

taxrate=input("What is the sales tax, given as a percent?")
taxrate_int=int(taxrate)

taxdecimal=(taxrate_int)/100

posttaxprice=(pretaxprice_int)*(1 + taxdecimal)
posttaxprice_str=str(posttaxprice)

print("After tax, your item will cost,",posttaxprice_str)
