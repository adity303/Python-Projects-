#wap to print fibonacci series 
# By fibonacci sequence (for loop)
a = 0
b = 1

num = int(input("Enter a number to obtain fibonacci series: "))

if num == 1:
    print(a)
else:
    print(b)
    print(a)
    # general syntax for fibonacci series
    for i in range (1,num+1): 
        c = a + b
        a = b
        b = c 
        print(c)
