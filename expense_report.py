output_file = "expense_report.txt"

# Dictionary to store total reimbursements
reimbursements = {}

# Read data and calculate totals
with open("expenses.txt", "r") as f:
    for line in f:
        parts = line.strip().split()
        if not parts:
            continue  # skip blank lines

        name = parts[0]

        try:
            # Convert each amount to float
            amounts = [float(x) for x in parts[1:]]
        except ValueError:
            print(f"Skipping invalid line: {line.strip()}")
            continue

        total = sum(amounts)
        reimbursements[name] = reimbursements.get(name, 0) + total

# Write results to report file
with open(output_file, "w") as f:
    f.write("Expense Reimbursement Report\n")
    f.write("============================\n\n")

    for name, total in sorted(reimbursements.items()):
        f.write(f"{name:10s} ${total:10.2f}\n")

    f.write("\nReport generated successfully.\n")

print(f"Expense report saved to '{output_file}'.")
