#Print all Prime numbers under 100:

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def print_primes_under_100():
    for num in range(2, 101):
        if is_prime(num):
            print(num, end=' ')

print_primes_under_100()
