classes = []
n = int(input("Number of classes: "))

for i in range(n):
    print(f"\nClass {i + 1}")
    course = input("Course: ").strip()
    day = input("Day: ").strip().lower()
    start = int(input("Start hour (0-23): "))
    end = int(input("End hour (1-24): "))
    room = input("Room: ").strip()

    if not course or not day or not room or start < 0 or end > 24 or start >= end:
        print("Invalid class entry; skipped.")
    else:
        classes.append((course, day, start, end, room))
conflicts = []
for i in range(len(classes)):
    for j in range(i + 1, len(classes)):
        c1, d1, s1, e1, r1 = classes[i]
        c2, d2, s2, e2, r2 = classes[j]
        if d1 == d2 and s1 < e2 and s2 < e1:
            message = f"{c1} and {c2}: overlapping classes on {d1}"
            if r1 == r2:
                message += f"; room clash in {r1}"
            conflicts.append(message)
print("\n--- TIMETABLE CHECK ---")
if conflicts:
    for item in conflicts:
        print("-", item)
else:
    print("No timetable conflicts found.")
