conducted = int(input("Enter classes conducted: "))
attended = int(input("Enter classes attended: "))

if conducted <= 0 or attended < 0 or attended > conducted:
    print("Invalid attendance details.")
else:
    current = attended / conducted * 100
    needed = 0
    while (attended + needed) / (conducted + needed) * 100 < 75:
        needed += 1

    print(f"Current attendance: {current:.2f}%")
    if needed == 0:
        print("You already meet the 75% requirement.")
    else:
        print(f"Minimum consecutive classes to attend: {needed}")
        projected = (attended + needed) / (conducted + needed) * 100
        print(f"Projected attendance: {projected:.2f}%")
