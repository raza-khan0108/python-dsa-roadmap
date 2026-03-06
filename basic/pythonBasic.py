x = 5           # int
y = 3.14        # float
name = "Raza"  # str
is_valid = True # bool

# Conditional statement
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")

# Loop
for i in range(x):
    print(i)

while x > 0:
    x -= 1
    print(x)
    
# Function
def greet(name):
    return f"Hello, {name}!"

print(greet("Raza"))

# List
numbers = [1, 2, 3, 4, 5]
print(numbers)
numbers.append(6)
print(numbers)

# Dictionary
person = {"name": "Raza", "age": 30}
print(person)
person["city"] = "New York" 
print(person)

# Tuple
coordinates = (10.0, 20.0)
print(coordinates)

# Set
unique_numbers = {1, 2, 3, 4, 5}
print(unique_numbers)
unique_numbers.add(6)
print(unique_numbers)   

