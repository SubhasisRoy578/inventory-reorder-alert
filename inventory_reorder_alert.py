import csv

INPUT_FILE = "inventory.csv"
OUTPUT_FILE = "restock_report.csv"

restock_items = []

try:
    with open(INPUT_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                item = row["item_name"].strip()

                if row["current_quantity"] == "" or row["reorder_threshold"] == "":
                    print(f"Skipping malformed row: {row}")
                    continue

                quantity = int(row["current_quantity"])
                threshold = int(row["reorder_threshold"])

                if threshold <= 0:
                    print(f"Invalid threshold for {item}")
                    continue

                if quantity < threshold:
                    if quantity < threshold * 0.25:
                        priority = "Critical"
                    else:
                        priority = "Low"

                    reorder_quantity = (threshold * 2) - quantity

                    restock_items.append({
                        "Item": item,
                        "Current Quantity": quantity,
                        "Threshold": threshold,
                        "Priority": priority,
                        "Suggested Reorder": reorder_quantity
                    })

            except (ValueError, KeyError):
                print(f"Skipping malformed row: {row}")

except FileNotFoundError:
    print(f"Error: {INPUT_FILE} not found.")
    exit()

print("\n========== RESTOCK REPORT ==========\n")

if not restock_items:
    print("All inventory levels are healthy.")
else:
    for item in restock_items:
        print(
            f"{item['Item']} | "
            f"Current: {item['Current Quantity']} | "
            f"Threshold: {item['Threshold']} | "
            f"Priority: {item['Priority']} | "
            f"Reorder: {item['Suggested Reorder']}"
        )

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "Item",
                "Current Quantity",
                "Threshold",
                "Priority",
                "Suggested Reorder"
            ]
        )
        writer.writeheader()
        writer.writerows(restock_items)

    print(f"\nCSV report saved as '{OUTPUT_FILE}'")

print("\n========== EMAIL ALERT ==========\n")
print("Subject: Inventory Restock Alert\n")

if restock_items:
    print("The following items require restocking:\n")
    for item in restock_items:
        print(
            f"- {item['Item']} "
            f"({item['Priority']}) - "
            f"Current Stock: {item['Current Quantity']}, "
            f"Suggested Reorder: {item['Suggested Reorder']}"
        )
else:
    print("No items require restocking today.")
