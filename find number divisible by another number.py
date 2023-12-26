# Wap to find number divisible by another number 
#Method 1 - For loop and conditional statements 
#print("The numbers divisible by 13 are: ")
#for i in range (1,100):
#    if i % 13 == 0:
#        print(i)
        
#Method - Using lambada function and filter()

l = [23,45,6,66,33,67,78,43]

result = list(filter(lambada x : x % 13 == 0,l))
print("The numbers are divisible by 13 are: ")
