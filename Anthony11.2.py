print(" Welcome to the Top 3 SNakcs Collector!")

snacks = [] # Start with an empty list
count = 0

# Use while loop to collect 3 favorite snacks
while count < 3:
    snack = input(f"Enter snack #{count + 1}: ")
    snacks.append(snack)
    count += 1

print("\n Your favorite snacks are:", snacks)

# Let's sort the list!
snacks.sort()
print(" Sorted snacks:", snacks)

# Let's say you changed your mind!
remove_item = input("\nOops! Want to remove a snack? Type one in: ")
#the keyword "in" is used to check if the item by user is in the list

if remove_item in snacks:
    snacks.remove(remove_item)
    print(" Removed snack:", remove_item)
else:
    print(" Snack not found!")

# Show the final list
print("\n Final list:", snacks)
print("Total snacks now:", len(snacks))
