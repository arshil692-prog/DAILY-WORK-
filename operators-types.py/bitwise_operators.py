# --------------------------------------------
# PYTHON BITWISE OPERATORS - COMPLETE PROGRAM
# --------------------------------------------

# Taking Input
a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))

print("\n-------- BITWISE OPERATORS --------\n")

# Bitwise AND
print("1. Bitwise AND (&)")
print(f"{a} & {b} = {a & b}")
print()

# Bitwise OR
print("2. Bitwise OR (|)")
print(f"{a} | {b} = {a | b}")
print()

# Bitwise XOR
print("3. Bitwise XOR (^)")
print(f"{a} ^ {b} = {a ^ b}")
print()

# Bitwise NOT
print("4. Bitwise NOT (~)")
print(f"~{a} = {~a}")
print(f"~{b} = {~b}")
print()

# Left Shift
print("5. Left Shift (<<)")
print(f"{a} << 1 = {a << 1}")
print(f"{a} << 2 = {a << 2}")
print(f"{b} << 1 = {b << 1}")
print(f"{b} << 2 = {b << 2}")
print()

# Right Shift
print("6. Right Shift (>>)")
print(f"{a} >> 1 = {a >> 1}")
print(f"{a} >> 2 = {a >> 2}")
print(f"{b} >> 1 = {b >> 1}")
print(f"{b} >> 2 = {b >> 2}")
