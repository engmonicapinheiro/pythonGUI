#chapter 21

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    print("Does python print this as well?")
    return a / b
    print("Does python print this?")

print("Let's do some math with just functions!")

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print(f"age: {age}; height: {height}; weight: {weight}; IQ: {iq}")

#A puzzle for the extra credit:
print("\nHere is a puzzle:")
what = add(age, subtract(height, multiply(weight, divide(iq,2))))
print("That becomes: ", what, ".Can you do it by hand?")

print("\nHere is another puzzle:")
result = multiply(weight, divide(iq,2))
result2 = subtract(height, result)
what = add(age, result2)
print("That becomes: ", what, ".Can you do it by hand?")
