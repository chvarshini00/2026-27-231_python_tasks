# Precedence: ** > * / // % > + -
print("2 + 3 * 4 =", 2 + 3 * 4)
print("(2 + 3) * 4 =", (2 + 3) * 4)
print("2 * 3 ** 2 =", 2 * 3 ** 2)
print("10 - 4 - 3 =", 10 - 4 - 3)

# Associativity: ** is right to left, others left to right
print("2 ** 3 ** 2 =", 2 ** 3 ** 2)
print("(2 ** 3) ** 2 =", (2 ** 3) ** 2)