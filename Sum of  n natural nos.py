#Wap to find the sum of n natural nos.
num = int(input("Enter a number here: "))

if num < 0:
    print("Please enter positive number ")
else: 
    sum = 0
    #Condition for n natural nos
    while num>0:
        sum += num 
        num -= 1

print(sum)