#number= int(input("Enter number between 6 and 16:"))
for number in range (6,16) :
    if(number % 5 == 0) :
     print(number , "is the first number divisible by 5")
     break