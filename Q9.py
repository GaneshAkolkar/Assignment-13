
#Write a python script to calculate the LCM (Least Common Multiple) of two numbers:
def lcm(a, b):
    return (a * b) // gcd(a, b)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

lcm_result = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is {lcm_result}")