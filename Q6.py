#Write a python script to print the first N prime numbers:

def print_first_n_primes(n):
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            print(num, end=' ')
            count += 1
        num += 1

n = int(input("Enter the value of N: "))
print(f"The first {n} prime numbers are:")
print_first_n_primes(n)