print("This list stores any three countries ")

countries = []

for i in range(3):
    country = input(f"Enter country #{i + 1}: ")
    countries.append(country)


print(" Your list of countries: ", countries)