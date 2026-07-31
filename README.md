# Inventory Reorder Alert

A Python automation script that reads inventory data from a CSV file, identifies low-stock items based on reorder thresholds, classifies priority levels, suggests reorder quantities, and exports a restock report.

## Features

- Read inventory from CSV
- Detect low stock
- Critical/Low priority classification
- Suggested reorder quantity
- Export report to CSV
- Email-style alert output
- Handles malformed data gracefully

## Files

- inventory_reorder_alert.py
- inventory.csv
- restock_report.csv

## Run

```bash
python inventory_reorder_alert.py

## Sample Console Output

----text

============================================================
INVENTORY RESTOCK REPORT
============================================================

Item: Laptop
Current Stock : 5
Threshold     : 10
Priority      : Low
Reorder Qty   : 15

Item: Keyboard
Current Stock : 2
Threshold     : 15
Priority      : Critical
Reorder Qty   : 28

Item: USB Cable
Current Stock : 0
Threshold     : 8
Priority      : Critical
Reorder Qty   : 16

Item: Monitor
Current Stock : 10
Threshold     : 12
Priority      : Low
Reorder Qty   : 14

CSV report successfully saved as 'restock_report.csv'

============================================================
SIMULATED EMAIL ALERT
============================================================

Subject: Inventory Restock Alert

Dear Warehouse Manager,

The following inventory items require immediate attention:

- Laptop | Priority: Low | Current Stock: 5 | Suggested Reorder: 15
- Keyboard | Priority: Critical | Current Stock: 2 | Suggested Reorder: 28
- USB Cable | Priority: Critical | Current Stock: 0 | Suggested Reorder: 16
- Monitor | Priority: Low | Current Stock: 10 | Suggested Reorder: 14

Please arrange the required purchase orders at the earliest.

Regards,
Inventory Monitoring System
