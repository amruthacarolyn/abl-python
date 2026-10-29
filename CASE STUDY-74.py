fee = float(input("Registration fee per participant (₹): "))
participants = []
duplicates = []

n = int(input("Number of registration records: "))
for i in range(n):
    reg_id = input(f"Registration ID {i + 1}: ").strip()
    if not reg_id:
        print("Empty ID rejected.")
    elif reg_id in participants:
        duplicates.append(reg_id)
    else:
        participants.append(reg_id)

sponsor_count = int(input("Number of sponsorships: "))
sponsorships = []
for i in range(sponsor_count):
    amount = float(input(f"Sponsorship {i + 1} (₹): "))
    if amount >= 0:
        sponsorships.append(amount)
    else:
        print("Negative sponsorship rejected.")

expense_count = int(input("Number of expenses: "))
expenses = []
for i in range(expense_count):
    label = input(f"Expense {i + 1} description: ").strip()
    amount = float(input("Expense amount (₹): "))
    if label and amount >= 0:
        expenses.append((label, amount))
    else:
        print("Invalid expense rejected.")

registration_income = len(participants) * fee
sponsorship_income = sum(sponsorships)
expense_total = sum(amount for label, amount in expenses)
income = registration_income + sponsorship_income
balance = income - expense_total

print("\n--- FESTIVAL FINANCIAL AUDIT ---")
print("Valid unique participants:", len(participants))
print(f"Registration income: ₹{registration_income:.2f}")
print(f"Sponsorship income : ₹{sponsorship_income:.2f}")
print(f"Total income       : ₹{income:.2f}")
print(f"Total expenses     : ₹{expense_total:.2f}")
print(f"Final balance      : ₹{balance:.2f}")
print("Duplicate IDs      :", duplicates if duplicates else "None")
if balance > 0:
    print("Result: SURPLUS")
elif balance < 0:
    print("Result: DEFICIT")
else:
    print("Result: BREAK-EVEN")
