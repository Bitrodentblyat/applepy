#take distance from user
kilometers = int(input("Enter the distance in Kms: "))

#ask for fuel price
fuel_p = int(input("Enter fuel price per liter: "))

#ask for vehicle mileage
mil = int(input("Enter mileage: "))

#cost
cost = (kilometers*fuel_p) / mil
print("This journey will cost you ₹", int(cost))