#Print all Prime numbers between two given numbers (inclusive):

def print_primes_between(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=' ')

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
print(f"Prime numbers between {start} and {end}:")
print_primes_between(start, end)