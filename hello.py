print("Hello from Python!")

# Variables and Types
x = 5
y = "hello"
z = 3.14

print(type(x))

# Collections: List, Tuples, Dictionaries
movies = ["Arrival", "Interstellar", "Dune"]  # list
point = (4, 9)                                # tuple
grades = {"Alice": 95, "Bob": 87}             # dict

print(movies[0])
movies.append("Blade Runner")

# Conditional Statements
score = 72

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("Keep going!")


# Loops
for i in range(5):
    print(i)

i = 1
while i <= 5:
    print(i)
    i += 1

# Functions
def greet(name):
    return f"Hello, {name}!"


print(greet("Alice"))

# Exceptions 
try:
    value = int("not a number")
except ValueError:
    print("That wasn’t an integer!")

#Write a snippet that catches a divide-by-zero error.
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

numbers = [1, 2, 3, 4]
for i in range(0, 4):
    print(numbers[i])



def test_sum():
    assert sum([1, 2, 3]) == 6


test_sum()