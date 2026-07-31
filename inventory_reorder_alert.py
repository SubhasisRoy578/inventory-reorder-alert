import csv

INPUT_FILE = "inventory.csv"
OUTPUT_FILE = "restock_report.csv"

restock_items = []

# Read Inventory CSV
try:
    with open(INPUT_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                item_name = row["item_name"].strip()

                if not row["current_quantity"] or not row["reorder_threshold"]:
                    print(f"Skipping malformed row: {row}")
                    continue

                current_quantity = int(row["current_quantity"])
                reorder_threshold = int(row["reorder_threshold"])

                if reorder_threshold <= 0:
                    print(f"Invalid threshold for {item_name}. Skipping...")
                    continue

                # Check whether restocking is required
                if current_quantity < reorder_threshold:

                    # Priority Level
                    if current_quantity < (reorder_threshold * 0.25):
                        priority = "Critical"
                    else:
                        priority = "Low"

                    # Healthy stock level = 2 × threshold
                    healthy_stock = reorder_threshold * 2
                    reorder_quantity = healthy_stock - current_quantity

                    restock_items.append({
                        "Item": item_name,
                        "Current Quantity": current_quantity,
                        "Threshold": reorder_threshold,
                        "Priority": priority,
                        "Suggested Reorder": reorder_quantity
                    })

            except (ValueError, KeyError):
                print(f"Skipping malformed row: {row}")

except FileNotFoundError:
    print(f"Error: '{INPUT_FILE}' not found.")
    exit()

# -------------------------------
# Console Report
# -------------------------------

print("\n" + "=" * 60)
print("INVENTORY RESTOCK REPORT")
print("=" * 60)

if restock_items:
    for item in restock_items:
        print(
            f"\nItem: {item['Item']}"
            f"\nCurrent Stock : {item['Current Quantity']}"
            f"\nThreshold     : {item['Threshold']}"
            f"\nPriority      : {item['Priority']}"
            f"\nReorder Qty   : {item['Suggested Reorder']}"
        )
else:
    print("All inventory levels are healthy.")

# -------------------------------
# Export CSV Report
# -------------------------------

if restock_items:
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

    print(f"\nCSV report successfully saved as '{OUTPUT_FILE}'")

# -------------------------------
# Simulated Email Alert
# -------------------------------

print("\n" + "=" * 60)
print("SIMULATED EMAIL ALERT")
print("=" * 60)

print("Subject: Inventory Restock Alert\n")

print("Dear Warehouse Manager,\n")

if restock_items:
    print("The following inventory items require immediate attention:\n")

    for item in restock_items:
        print(
            f"- {item['Item']}"
            f" | Priority: {item['Priority']}"
            f" | Current Stock: {item['Current Quantity']}"
            f" | Suggested Reorder: {item['Suggested Reorder']}"
        )

    print("\nPlease arrange the required purchase orders at the earliest.")
else:
    print("No inventory items require restocking today.")

print("\nRegards,")
print("Inventory Monitoring System")
