candidates = []
rejected = []
n = int(input("Number of candidates: "))

for i in range(n):
    print(f"\nCandidate {i + 1}")
    name = input("Name: ").strip()
    marks = float(input("Academic marks (0-100): "))
    assessment = float(input("Assessment score (0-100): "))
    attendance = float(input("Attendance percentage (0-100): "))

    if not name or not (0 <= marks <= 100 and 0 <= assessment <= 100
                        and 0 <= attendance <= 100):
        print("Invalid record; skipped.")
        continue

    reasons = []
    if marks < 70:
        reasons.append("academic marks below 70")
    if assessment < 60:
        reasons.append("assessment below 60")
    if attendance < 75:
        reasons.append("attendance below 75%")

    if reasons:
        rejected.append((name, reasons))
    else:
        candidates.append((name, marks, assessment, attendance))

candidates.sort(key=lambda item: (-item[2], -item[1], -item[3], item[0].lower()))

print("\n--- ELIGIBLE CANDIDATE RANKING ---")
if not candidates:
    print("No eligible candidates.")
else:
    for rank, (name, marks, assessment, attendance) in enumerate(candidates, start=1):
        print(f"{rank}. {name} | Assessment: {assessment:.1f} | "
              f"Marks: {marks:.1f} | Attendance: {attendance:.1f}%")

print("\n--- NOT ELIGIBLE ---")
if not rejected:
    print("None")
else:
    for name, reasons in rejected:
        print(f"{name}: {', '.join(reasons)}")
