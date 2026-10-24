"""Operators perform calculations and comparisons on values.
This example demonstrates arithmetic, comparison, logical, and assignment operators.
"""

# Operators in Python

# Arithmetic operators
num1 = 10
num2 = 3
print("Arithmetic operators:")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor division:", num1 // num2)
print("Modulus:", num1 % num2)
print("Exponentiation:", num1 ** num2)

# Assignment operators
x = 5
x += 3
x *= 2
x -= 4
print("\nAssignment operators:", x)

# Comparison operators
print("\nComparison operators:")
print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 >= num2)
print(num1 < num2)
print(num1 <= num2)

# Logical operators
print("\nLogical operators:")
print((num1 > 0) and (num2 > 0))
print((num1 > 0) or (num2 < 0))
print(not (num1 < 0))

# Identity operators
print("\nIdentity operators:")
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)
print(a is c)
print(a is not c)

# Membership operators
print("\nMembership operators:")
nums = [1, 2, 3, 4, 5]
print(3 in nums)
print(6 not in nums)

# Bitwise operators
print("\nBitwise operators:")
p = 6  # 110
q = 3  # 011
print("AND:", p & q)
print("OR:", p | q)
print("XOR:", p ^ q)
print("NOT:", ~p)
print("Left shift:", p << 1)
print("Right shift:", p >> 1)
# Topic 4: Operators
