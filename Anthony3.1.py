import math

Bill = float(input("Enter the bill amount: "))
Tip = Bill * 0.15
Total = Bill + Tip

print("-----------------------------------------------------------")

print(f"Bill: $ {Bill:.2f}")
print(f"Tip (15%): $ {Tip:.2f} ")
print(f"Total: $ {Total:.2f}")

print("-----------------------------------------------------------")