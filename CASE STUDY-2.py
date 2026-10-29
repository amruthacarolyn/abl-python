units = float(input("Enter units consumed: "))
if units < 0:
    print("Invalid input: units cannot be negative.")
else:
    if units <= 100:
        energy = units * 1.50
    elif units <= 200:
        energy = 100 * 1.50 + (units - 100) * 2.50
    else:
        energy = 100 * 1.50 + 100 * 2.50 + (units - 200) * 4.00

    surcharge = energy * 0.05 if units > 250 else 0
    fixed_charge = 50
    total = energy + fixed_charge + surcharge

    print("\n--- ELECTRICITY BILL ---")
    print(f"Units consumed : {units:.1f}")
    print(f"Energy charge  : ₹{energy:.2f}")
    print(f"Fixed charge   : ₹{fixed_charge:.2f}")
    print(f"Surcharge      : ₹{surcharge:.2f}")
    print(f"Total bill     : ₹{total:.2f}")
