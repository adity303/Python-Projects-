#Wap to print all prime numbers.
lower = int(input('Enter lower limit here: '))
upper = int(input('Enter upper limit here: '))

for num in range (lower, upper + 1):
    if num > 1: # conditional statement 
        for i in range (2, num):
            if num%i == 0: # verification of a prime number
                break
        else:
            print(num)