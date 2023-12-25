#Wap to find the factorial of a number. 
#By using for loop 
#num = int(input("Enter the number here: "))

#fact = 1
#if num < 0:
#    print("Factorial of a 0 does not exist ")
#    if num == 0:
#        print("Factorial of 0 is", 1)
#    if num > 0:
        # General solution of a fact
#        for i in range (1, num+1):
#            fact = fact + i 
#    print("The factorial of a given number is: ", fact)

# Method 2 - Using Recursion 
def fact(a):
    if a == 0:
        return 1
    else:
        # Calling itself number 
        return ((a)*fact(a-1))
    
num = int(input("Enter the number here: "))

result = fact(num)
print("The factorial of a given number is: ", result)