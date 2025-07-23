count = 1

while count <= 5:
    print(f"Count is: {count}")
    count = count + 1

print("Loop finished! Count is now: ", count)
print()

countdown = 10

while countdown > 0:
    print(f"Countdown: {countdown}")
    countdown -= 1

print("Blast off!\n")

password = "" 

while password != "python":
    password = input("Enter the secret password: ")

    if password != "python":
        print("Wrong password! Try again.")

print("Correct password! Welcome!\n")

total = 0
number = 1

print("Enter numbers to add up. Enter 0 to stop.")

while number != 0:
    number = int(input("Enter a number: "))

    if number != 0:
        total = total + number
        print(f"Running total: {total}")

print(f"Final total: {total}\n")