arrow = int(input("Enter the size of the arrow: "))
for i in range(1, arrow + 1):
    if i <= arrow // 2 + 1: 
        print("*" * i)
    else: 
        print("*" * (arrow - i + 1))

