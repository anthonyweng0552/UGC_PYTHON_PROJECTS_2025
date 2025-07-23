print("EXAMPLE 1: Basic For loop")
print("-" * 25)

for i in range(5):
    print(f"This is loop number {i}")

print("Loop is finished!\n")

print("EXAMPLE 2: Counting 1 to 10")
print("-" * 25)

for number in range (1, 11):
    print(f"Count: {number}")

print("Counting complete!\n")

print("EXAMPLE 3: Looping Throught a List")
print("-" * 25)

favorite_foods = ["sushi", "taco", "lava cake", "pizza", "hash browns"]

for food in favorite_foods:
    print(f"I love {food}!")

print("Counting complete!\n")


print("EXAMPLE 4: Even Numbers")
print("-" * 25)

for num in range(0, 21, 2):
    print(f"Even number: {num}")

print("All even number from 0 to 20!\n")

print("EXAMPLE 5: Multiplication Table for 5")
print("-" * 25)

for i in range (1,11):
    product = 5 * i
    print(f"5 x {i} = {product}")

print("Multiplication table complete!\n")

word = "PYTHON"

for letter in word:
    print(f"Letter: {letter}")

print(f"The word '{word}' has {len(word)} letters!\n")

for row in range(3):
    print(f"Row {row + 1}: ", end="")

    for star in range(5):
        print("* ", end="")

    print()



print("Pattern complete!\n")


times = int(input("How many time sshould I say hello? "))

for i in range(times):
    print(f"Hello #{i + 1}!")

print("All dome saying hello!\n")