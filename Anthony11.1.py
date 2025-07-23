# Program purpose: starting favorite food of user and using list methods to modify

# Start with a basic list
foods = ["Pizza", "Tacos", "Burgers", "Sushi", "Fries"]
print(" Starting Food ListL", foods)

# Ask user to add a new food
new_food = input(" Enter one food to add to the list: ")
foods.append(new_food)
print(" Added! New List:", foods)

# Ask user to remove a food
remove_food = input(" Enter a food you want to remove from the list: ")
if remove_food in foods:
    foods.remove(remove_food)
    print(f"Removed {remove_food}.")
else:
    print(f" {remove_food} is not in the list.")
print(" Current List:", foods)

# Show number of items
print(" Total items in the list:", len(foods))

# Ask if user wants to sort the list
should_sort = input(" Do you want to sort the list alphabetically? (yes/no): ").lower()
if should_sort == "yes":
    foods.sort()
    print(" Sorted List:", foods)
