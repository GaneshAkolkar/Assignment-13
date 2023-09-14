#Write a python script to find the next prime number after a given number:

def next_prime(num):
    num += 1
    while True:
        if is_prime(num):
            return num
        num += 1

num = int(input("Enter a number: "))
next_prime_num = next_prime(num)
print(f"The next prime number after {num} is {next_prime_num}")