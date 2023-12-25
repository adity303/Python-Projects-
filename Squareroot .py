#Wap to find the square root of a number. 
#1st method - Using exponentiation 
#num = 65
#num1 = int(input("Enter a number here: "))
#sr = num**(0.5)
#print("The square root of a given number is", sr)

#2nd Method - using math module by sqrt 
import math
num = int(input("enter number here: "))
sr = math.sqrt(num)
print("The square root of the given number is: ", sr)