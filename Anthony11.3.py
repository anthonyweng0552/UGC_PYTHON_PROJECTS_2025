Loop = True
Backpack = []
def Options():
    print("\nChoose an option:")
    print("1. Add item")
    print("2. Remove item")
    print("3. Show backpack")
    print("4. Sort items")
    print("5. Pop last item")
    print("6. Exit")


while Loop == True:
    Options()
    Choice = int(input("Enter choice (1-6): "))
    print()

    if Choice == 1:
        Item = str(input("What item would you like to add? "))
        Backpack.append(Item)
        print(f"\n{Item} added")
    elif Choice == 2:
        Remove = str(input("What item would you like to remove? "))
        There = False
        for stuff in Backpack:
            if stuff.lower() == Remove.lower():
                Backpack.remove(stuff)
                print(f"\n{Remove} was Removed")
                There = True
        if not There:
            print("\nItem not found")
    elif Choice == 3:
        print("Backpack: ", Backpack)
    elif Choice == 4:
        Backpack.sort()
        print("Backpack sorted")
    elif Choice == 5:
        Backpack.pop()
        print("Item popped")
    elif Choice == 6:
        print(f"Final items are {Backpack}\n")
        break
    else:
        print("Not an option")



