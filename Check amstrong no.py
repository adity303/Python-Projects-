#Wap to check amstrong Number
num = int(input("Enter the number here: "))
order = len(str(num))

sum = 0
temp = num 

while temp> 0:
    digit = temp%10
    sum += digit ** order
    temp //=10
    
if sum == num:
    print("It is an armstrong Number ")
else:
    print("It is not Armstrong number ")