# check prime number function in python 3 
def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, n):
            if n % x == 0:
                return False
        return True

# print prime numbers between 1 to 100
for n in range(1, 100):
    if is_prime(n):
        print(n)

# generate other test cases for the function
for n in range(1, 100):
    if is_prime(n):
        print('assert is_prime({}) == True'.format(n))
    else:
        print('assert is_prime({}) == False'.format(n))