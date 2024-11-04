number = int(input("Enter a number between 6 and 16: "))
while number > 6 and number < 16:
    if number % 5 == 0:
        print(number , "is the first number divisible by 5")
        break
    elif number % 5 !=0:
        print(number,"is not divisible by 5")
        
else:
    print(number,"is out of range.")
