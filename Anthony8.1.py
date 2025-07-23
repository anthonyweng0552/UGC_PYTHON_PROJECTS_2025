Number_Of_Columns = int(input("Enter the number of columns: "))
Number_Of_Rows = int(input("Enter the number of rows: "))
What_Symbol = str(input("What pattern do you want to use?: "))
for Rows in range(Number_Of_Rows):
    print(f"Row {Rows + 1}: ", end="")
    for Columns in range(Number_Of_Columns):
        print(f"{What_Symbol} ", end="")

    print()

print("Pattern Complete!")
print(f"You made a {Number_Of_Columns} x {Number_Of_Rows} pattern using {What_Symbol}!")
print("Amazing work! You're a pattern master!")