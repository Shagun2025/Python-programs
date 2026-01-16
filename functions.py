# Function to check prime number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter number: "))
print(is_prime(num))

# Function: Calculate Factorial of a Number
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(factorial(5))

# Function : Reverse a String
def reverse_string(string):
    return string[::-1]

print(reverse_string("rahul"))

# Function : Count Vowels in a String
def count_vowels(string):
    count = 0
    for char in string:
        if char in 'aeiouAEIOU':
            count += 1
    return count

print(count_vowels("python"))

# Function : Generate Fibonacci Series
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

print(fibonacci(5))

# Function : Product of Variable Number of Arguments
def product(*numbers):
    prod = 1
    for num in numbers:
        prod *= num
    return prod

print(product(1, 2, 3, 4, 5, 6))

# Function 9: Merge Two Dictionaries
def merge_dicts(d1, d2):
    merged = d1.copy()
    for key, value in d2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged

dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 40}

print(merge_dicts(dict1, dict2))
