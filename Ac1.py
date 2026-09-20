print("Vechile Selcter:")
print("Select a vechile for your ride:")
print("\n 1. Bike")
print("\n 2. Car")

choice = int(input())

if (choice == 1):
    print("You have selected Bike.")
    print("Which Type of Bike you want?:")
    print("\n 1.Normal Bike")
    print("\n 2.Of-road Bike")

    choice2 = int(input())

    if (choice2 == 1):
        print("Name : Normal Bike")
        print("Speed : 80 km/h")
        print("Great for : A normal ride.")

    else:
        print("Name : Of-road Bike")
        print("Speed : 40 km/h")
        print("Great for : Going in a mountain type area for a ride.")

elif (choice == 2):
    print("You have selected Car")
    print("Which Type of car you want?:")
    print("\n 1.SUV")
    print("\n 2. Sedan")

    choice3 = int(input())

    if (choice3 == 1):
        print("Name : SUV")
        print("Seats : 7")
        print("Great for : Of-road trips")

    else:
        print("Name : Sedan")
        print("Seat : 5")
        print("Great for: Family Trips")

else:
    print("Your choice was not valid")
    print("Please enter 1 for Bike or 2 for Car.")


print("You have selected your vechile for your trip")
print("Have a nice day and a nice trip too!")