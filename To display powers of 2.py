#Wap to display powers of 2 using Anonymous function. 
#Using Lambada function 
nterms = int(input("Enter the number of terms here: "))

result = list(map(Lambada x : 2 ** x, range(nterms+1)))

#print(result)

for i in range(nterms_+ 1):
    print("The value of 2 raised to power is: ", i, "is", result[i])