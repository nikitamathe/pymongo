number = int(input("Enter a number between 6 and 16: "))
while number > 6 and number < 16:
    if number % 5 == 0:
        print(number , "is the first number divisible by 5")
        break
    elif number % 5 !=0:
        print(number,"is not divisible by 5")
        check_again = (input("Do you want to check another number?(yes/no):"))
        if check_again != yes:
            break
        elif check_again == yes:
            print("Enter a new number between 6 and 16: ")
        number = int(input()) 
        
else:
    print(number,"is out of range.")
