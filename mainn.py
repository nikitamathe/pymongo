number = int(input("Enter a number between 6 and 16: "))

while 6 < number < 16:
    if number % 5 == 0:
        print(number, "is the first number divisible by 5")
        break
    else:
        print(number, "is not divisible by 5")
        
        # Ask if the user wants to check another number
        while True:
            check_again = input("Do you want to check another number? (yes/no): ")
            if check_again != "yes":
                break  # Exit the inner loop and the main loop if the answer is not "yes"
            else:
                number = int(input("Enter a new number between 6 and 16: "))
                if not (6 < number < 16):  # Check if the new number is out of range
                    print(number, "is out of range.")
                elif number % 5 == 0:
                    print(number,"is divisible by 5")
                elif number % 5 != 0:
                    print(number,"is not divisible by 5")
                    break  # Exit both loops if the new number is out of range
        if check_again != "yes":  # Exit the outer loop if the user doesn't want to continue
            break
else:
    print(number, "is out of range.")
