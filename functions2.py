print("Welcome")
def calculate(a,b):
    return a+b,a-b,a/b

a = int(input("Enter firts number : "))
b = int(input("Enter second number : "))
addd,s,d = calculate(a,b)
print(f"Addition : {addd}")
print(f"Subtraction : {s}")
print(f"Division : {d}")

