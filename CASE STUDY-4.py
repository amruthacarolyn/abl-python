name = input("Enter employee name: ").strip()
basic = float(input("Enter basic pay (₹): "))
overtime_hours = float(input("Enter overtime hours: "))

if basic < 0 or overtime_hours < 0 or not name:
    print("Invalid input: enter a name and non-negative amounts.")
else:
    hra = basic * 0.20
    da = basic * 0.10
    overtime = overtime_hours * 200
    gross = basic + hra + da + overtime
    rate = 0.08 if gross > 30000 else 0.05
    deduction = gross * rate
    net = gross - deduction

    print("\n--- SALARY STATEMENT ---")
    print("Employee       :", name)
    print(f"Basic pay      : ₹{basic:.2f}")
    print(f"HRA            : ₹{hra:.2f}")
    print(f"DA             : ₹{da:.2f}")
    print(f"Overtime       : ₹{overtime:.2f}")
    print(f"Gross salary   : ₹{gross:.2f}")
    print(f"Deduction      : ₹{deduction:.2f} ({rate:.0%})")
    print(f"Net salary     : ₹{net:.2f}")
