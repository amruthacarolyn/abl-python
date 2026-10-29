transactions = []
n = int(input("Number of transactions: "))
threshold = float(input("Flag amounts above (₹): "))

for i in range(n):
    print(f"\nTransaction {i + 1}")
    transaction_id = input("Transaction ID: ").strip()
    amount = float(input("Amount (₹): "))
    if not transaction_id or amount < 0:
        print("Invalid transaction; skipped.")
    else:
        transactions.append((transaction_id, amount))

print("\n--- TRANSACTION AUDIT ---")
found = False
for i, (transaction_id, amount) in enumerate(transactions):
    flags = []
    for j in range(i):
        if transactions[j][0] == transaction_id:
            flags.append("duplicate ID")
            break
    if amount > threshold:
        flags.append("amount above threshold")
    if flags:
        found = True
        print(f"{transaction_id} | ₹{amount:.2f} | {', '.join(flags)}")

if not found:
    print("No suspicious transactions found.")
