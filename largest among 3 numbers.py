#Wap to find the largest among three numbers
#Take 3 numbers and compare among them 
num1 = int(input('Enter first number here: '))
num2 = int(input('Enter second number here: '))
num3 = int(input('Enter third number here: '))
if num1 > num2 and (num1 > num3):  # checking for the first number 
    print(num1, "is a largest number")
elif (num2 > num1) and (num2 > num3):  #checking for the second number 
    print(num2, "is a largest number")
else:
    print(num3, "is the largest number") #printing the 3rd largest number 