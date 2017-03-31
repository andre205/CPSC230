#Celcius to Fahrenheit

celcius=input("What is the current temperature in celcius?")
celcius_float=float(celcius)

fahrenheit_float=((celcius_float * 9/5) + 32)
fahrenheit_str=str(fahrenheit_float)

print("The current temperature in fahrenheit is",fahrenheit_str,"degrees")
