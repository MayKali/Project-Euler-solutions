
#Finds the sum of even-valued fibonacci terms that do not exceed the 
#given number

def sumofevenfibonacci(number):

    a_term = 1 
    b_term = 2
    sum = b_term

    while(b_term <= number):

        temp = a_term
        a_term = b_term
        b_term = temp + b_term
        
        if( b_term % 2 == 0):
            sum += b_term

    return sum

print(sumofevenfibonacci(4000000))




