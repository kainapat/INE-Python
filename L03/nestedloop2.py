rows = int(input("Enter the rows: "))
count = 0
for i in range(1, 101):
    print(i, end= " ")
    count += 1
    if count % rows == 0:
        print("\n")