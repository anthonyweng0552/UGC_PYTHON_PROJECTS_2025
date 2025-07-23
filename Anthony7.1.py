Rain = str(input("Is it raining? (yes/no): "))

if Rain.lower() == "yes" or Rain.lower() == "true":
    print("Take an umbrella")
elif Rain.lower() == "no" or Rain.lower() == "false":
    print("Enjoy its not raining!!!")