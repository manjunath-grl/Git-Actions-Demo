import math

class check_Prime:
    def is_prime(num):
        '''Check if num is prime or not.'''
        for i in range(2,int(math.sqrt(num))+1):
            if num%i == 0:
                return False
        return True

provided_num = int(input("Please enter the number: "))

print("Given number is prime or not: ",check_Prime.is_prime(provided_num))
