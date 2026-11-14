rows = int(input("Enter rows: "))

for row in range(1, rows + 1):
    for col in range(1, rows - row + 2):
        print("*", end=" ")
    print()