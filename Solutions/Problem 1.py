#Finds the sum of all the multiples of 3 or 5 
#below the number given.


def multiplesof3and5(number):

    sum = 0 

    for i in range(number):
        if(i % 3 == 0 or i % 5 == 0):
            sum += i

    return sum


print(multiplesof3and5(1000))


    
