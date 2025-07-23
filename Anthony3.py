import math

Item_Price = float(input("Enter item price: "))
Sales_Tax = Item_Price * 0.0825
Total_Cost = Item_Price + Sales_Tax

print("-----------------------------------------------------------")

print(f"Item price: $ {Item_Price:.2f}")
print(f"Sales Tax (8.25%): $ {Sales_Tax:.2f} ")
print(f"Total Cost: $ {Total_Cost:.2f}")

print("-----------------------------------------------------------")