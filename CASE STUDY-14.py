products = []
count = int(input("Number of products: "))

if count <= 0:
    print("Enter a positive number of products.")
else:
    for i in range(count):
        print(f"\nProduct {i + 1}")
        name = input("Name: ").strip()
        opening = int(input("Opening stock: "))
        received = int(input("Quantity received: "))
        dispatched = int(input("Quantity dispatched: "))
        recorded = int(input("Recorded closing stock: "))
        target = int(input("Target stock: "))

        if (not name or min(opening, received, dispatched, recorded, target) < 0
                or dispatched > opening + received):
            print("Invalid record; this product was not added.")
            continue

        expected = opening + received - dispatched
        difference = recorded - expected
        replenishment = max(0, target - expected)
        products.append((name, expected, recorded, difference, replenishment))

    print("\n--- INVENTORY RECONCILIATION ---")
    for name, expected, recorded, difference, replenishment in products:
        status = "MATCH" if difference == 0 else "DISCREPANCY"
        print(f"{name}: expected={expected}, recorded={recorded}, "
              f"difference={difference}, status={status}, replenish={replenishment}")
