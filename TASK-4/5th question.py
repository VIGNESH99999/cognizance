R = int(input("Enter the number of rows: "))
x = 2 * R - 2
for i in range(0, R):
    for j in range(0, x):
        print(end="")
    x = x - 2
    for j in range(0, i + 1):
        print("*", end="")
    print("")
