# ============================================
# 1. IDENTITY OPERATORS
# ============================================

print("===== Identity Operators =====")

a = [10, 20, 30]
b = a
c = [10, 20, 30]

print("a:", a)
print("b:", b)
print("c:", c)

print("a is b =", a is b)          # True
print("a is c =", a is c)          # False
print("a == c =", a == c)          # True
print("a is not c =", a is not c)  # True


# ============================================
# 2. LOGICAL OPERATORS
# ============================================

print("\n===== Logical Operators =====")

age = 20
citizen = True

print("Age >=18 and Citizen =", age >= 18 and citizen)

marks = 45
sports_quota = True

print("Marks >=50 or Sports Quota =", marks >= 50 or sports_quota)

logged_in = False

print("Not Logged In =", not logged_in)


# ============================================
# 3. MEMBERSHIP OPERATORS
# ============================================

print("\n===== Membership Operators =====")

fruits = ["Apple", "Banana", "Mango"]

print("Banana in fruits =", "Banana" in fruits)
print("Orange not in fruits =", "Orange" not in fruits)

text = "Python Programming"

print("'Python' in text =", "Python" in text)

student = {
    "name": "John",
    "age": 20
}

print("'name' in student =", "name" in student)
print("'John' in student =", "John" in student)


# ============================================
# 4. ASSIGNMENT OPERATORS
# ============================================

print("\n===== Assignment Operators =====")

x = 10
print("Initial x =", x)

x += 5
print("After += 5 :", x)

x -= 3
print("After -= 3 :", x)

x *= 2
print("After *= 2 :", x)

x /= 4
print("After /= 4 :", x)

x //= 2
print("After //= 2 :", x)

x %= 3
print("After %= 3 :", x)

x **= 2
print("After **= 2 :", x)


# ============================================
# 5. REAL LIFE EXAMPLE
# ============================================

print("\n===== Real Life Example =====")

users = ["Alice", "Bob", "Charlie"]

username = "Alice"
logged_in = True

if username in users and logged_in:
    print("Access Granted")
else:
    print("Access Denied")