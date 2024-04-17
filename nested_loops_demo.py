# nested loop

for row in range(1, 4, 1):
    print(row, end="-> ")
    for col in range(1, 5, 1):
        print(col * 2, end=" ")
    print()

