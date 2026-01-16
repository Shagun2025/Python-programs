# Program 1: Swap two numbers
a = 10
b = 20
a, b = b, a
print("a =", a, "b =", b)

# Program 2: Area of a circle
radius = float(input("Enter radius: "))
area = 3.14 * radius * radius
print("Area =", area)

# Program 3: Check data type
d = "hello world"
print(type(d))


# Program 4: Print with custom end and separator
print("python", end=' ')
print("21", "08", "25", sep="-")


# Program 5: Using f-strings
name = 'rahul'
age = 17
print(f"Hello, My name is {name} and I'm {age} years old")


# program 6: Celsius to Fahrenheit conversion
temp = int(input("Enter temperature in Celsius: "))
print(temp, "deg")
print("The temperature in Fahrenheit is", temp * 9/5 + 32, "deg")


# Program 7: Marks, average, percentage calculation
sub1 = int(input("Enter first subject marks: "))
sub2 = int(input("Enter second subject marks: "))
sub3 = int(input("Enter third subject marks: "))

total = sub1 + sub2 + sub3
average = total / 3
percentage = (average / 100) * 100 
print("Total:",total)
print("Average:",average)
print("Percentage:",percentage)


# Program 8: Concatenating strings with custom separator and end
user1 = input("Enter first username: ")
user2 = input("Enter second username: ")

print(user1, user2, sep="@gmail.com", end="@gmail.com")

