rows = int(input("Number of rows: "))
cols = int(input("Seats per row: "))

if rows <= 0 or cols <= 0:
    print("Rows and columns must be positive.")
else:
    seats = [["." for _ in range(cols)] for _ in range(rows)]
    reserved_count = int(input("Number of reserved seats: "))

    for _ in range(reserved_count):
        r = int(input("Reserved row (1-based): ")) - 1
        c = int(input("Reserved seat (1-based): ")) - 1
        if 0 <= r < rows and 0 <= c < cols and seats[r][c] == ".":
            seats[r][c] = "R"
        else:
            print("Invalid or already reserved position; skipped.")

    seen = []
    student_count = int(input("Number of students to assign: "))
    for _ in range(student_count):
        roll = input("Student roll number: ").strip()
        if not roll or roll in seen:
            print("Empty or duplicate roll number; rejected.")
            continue

        placed = False
        for r in range(rows):
            for c in range(cols):
                if seats[r][c] == "." and not placed:
                    seats[r][c] = roll
                    placed = True
        if placed:
            seen.append(roll)
        else:
            print("No vacant seat for", roll)

    occupied = 0
    reserved = 0
    vacant = 0
    print("\n--- SEATING MATRIX ---")
    for row in seats:
        print(" | ".join(row))
        for seat in row:
            if seat == ".":
                vacant += 1
            elif seat == "R":
                reserved += 1
            else:
                occupied += 1
    print(f"Occupied: {occupied}; Reserved: {reserved}; Vacant: {vacant}")
