# Name: Krishnil Prasad      Student ID: 001023381

from HashTable import HashTable
from Packages import Package
from datetime import datetime
from datetime import timedelta
from Truck import Truck


def load_packages():
    # Reads data from the package file and creates package objects
    packages = []

    file = open("packages.txt", "r")

    for line in file:
        data = line.split(",")
        package = Package(int(data[0]), data[1], data[2], data[3], int(data[4]), data[5], int(data[6]), data[7],
                          data[8])
        packages.append(package)

    file.close()

    return packages


def load_locations():
    # Reads locations and their neighbours from the locations file and creates a dictionary
    dictionary = {}

    file = open("locations.txt", "r")

    for line in file:
        data = line.split(",")
        dictionary[data[0]] = {'HUB': float(data[1]), '1060 Dalton Ave S': float(data[2]),
                               '1330 2100 S': float(data[3]),
                               '1488 4800 S': float(data[4]),
                               '177 W Price Ave': float(data[5]), '195 W Oakland Ave': float(data[6]),
                               '2010 W 500 S': float(data[7]),
                               '2300 Parkway Blvd': float(data[8]), '233 Canyon Rd': float(data[9]),
                               '2530 S 500 E': float(data[10]),
                               '2600 Taylorsville Blvd': float(data[11]), '2835 Main St': float(data[12]),
                               '300 State St': float(data[13]),
                               '3060 Lester St': float(data[14]), '3148 S 1100 W': float(data[15]),
                               '3365 S 900 W': float(data[16]),
                               '3575 W Valley Central Station bus Loop': float(data[17]),
                               '3595 Main St': float(data[18]), '380 W 2880 S': float(data[19]),
                               '410 S State St': float(data[20]), '4300 S 1300 E': float(data[21]),
                               '4580 S 2300 E': float(data[22]),
                               '5025 State St': float(data[23]), '5100 South 2700 West': float(data[24]),
                               '5383 S 900 East #104': float(data[25]),
                               '600 E 900 South': float(data[26]), '6351 South 900 East': float(data[27])}
    file.close()

    return dictionary


def main_menu():
    # Prints menu on the screen for the interface
    print()
    print("\t1: Lookup Package by ID")
    print("\t2: Show Status of all Packages and Trucks:")
    print("\t3: Show Mileage")
    print("\t4: Exit")
    print()


def sort_packages(hub):
    # Sorts the packages according to the level of priority.
    sorted_list = []

    # Low priority and delayed packages are appended to the list first.
    for package in hub:
        if package.notes == "Wrong address":
            sorted_list.append(package)

    for package in hub:
        if package.deadline == "EOD" and package.notes == "N/A":
            sorted_list.append(package)

    # High priority packages with deadlines are appended for Truck 2.
    for package in hub:
        if (package.deadline != 'EOD' or package.notes == 'Deliver together') and package.status != 'Delayed':
            sorted_list.append(package)

    # Packages with specific instruction and delayed packages with deadlines are appended for Truck 3
    for package in hub:
        if package.status == 'Delayed':
            sorted_list.append(package)

    for package in hub:
        if package.notes == "Truck 2":
            sorted_list.append(package)

    return sorted_list


def get_route(delivery_list):
    # Gets the addresses from the sorted list and create a dictionary with location and distance = 0
    route1 = {}
    route2 = {}
    route3 = {}
    for i in range(0, 16):
        address = deliveryList[i].address
        route1[address] = 0

    for i in range(16, 32):
        address = deliveryList[i].address
        route2[address] = 0

    for i in range(32, len(delivery_list)):
        address = deliveryList[i].address
        route3[address] = 0

    return route1, route2, route3


def sort_route(plan, citymap):
    # Sorts the route by getting the nearest location from the hub
    # and recursively calls the function for all the locations.
    sorted_route = {}
    route = plan
    city = citymap
    location = 'HUB'

    def get_next(location, route, sorted_route, city):
        addresses = {}
        for address, distance in city[location].items():
            if address in route:
                addresses[address] = distance
        for address, distance in addresses.items():
            if distance == min(addresses.values()):
                sorted_route[address] = distance
                location = address
                if len(route.values()) == 1:
                    sorted_route['HUB'] = city[location]['HUB']
                    break
                else:
                    route.pop(address)
                    get_next(location, route, sorted_route, city)
        return sorted_route

    get_next(location, route, sorted_route, city)

    return sorted_route


def deliver_packages(truck, time, delivery_list):
    # Delivers the packages and updates the time for the packages.
    # Updates the mileage for the trucks.
    truck.track['left'] = time.strftime("%H:%M")
    # A list to store the packages in each truck.
    list = []
    for package in delivery_list:
        package.track[time.strftime("%H:%M")] = 'Out for Delivery'
        list.append(package.id)
    truck.track['packages'] = list

    for location, distance in truck.route.items():
        time += timedelta(hours=(distance / 18))
        for package in delivery_list:
            if package.address == location:
                package.time = time
                package.status = "Delivered at " + time.strftime("%H:%M")
        truck.mileage += distance

    truck.track['arrived'] = time.strftime("%H:%M")
    return truck.mileage


if __name__ == "__main__":

    # Loads the packages and inserts them into the hashtable.
    # loads location and sorts the packages according to priority.
    hub = load_packages()
    ht = HashTable()
    for package in hub:
        ht.hash_insert(package)
    locations = load_locations()
    deliveryList = sort_packages(hub)

    # Updates the time and status of all packages.
    time = datetime(2000, 1, 1, 8)
    for package in deliveryList:
        if package.status == 'Delayed':
            package.track[time.strftime("%H:%M")] = 'Delayed'
        else:
            package.track[time.strftime("%H:%M")] = 'At Hub'

    # Create Truck objects.
    truck1 = Truck('Truck 3', 0)
    truck2 = Truck('Truck 1', 0)
    truck3 = Truck('Truck 2', 0)

    # Gets three routes, then sorts and assigns to respective trucks.
    plan1, plan2, plan3 = get_route(deliveryList)
    truck1.set_route(sort_route(plan1, locations))
    truck2.set_route(sort_route(plan2, locations))
    truck3.set_route(sort_route(plan3, locations))

    # Sets the Departure time for all packages.
    for package in deliveryList[0:16]:
        package.time = datetime(2000, 1, 1, 11)
    for package in deliveryList[16:32]:
        package.time = datetime(2000, 1, 1, 8)
    for package in deliveryList[32:len(deliveryList) + 1]:
        package.time = datetime(2000, 1, 1, 9, 5)

    # Delivers the first set of packages with deadlines.
    mileage = deliver_packages(truck2, time, deliveryList[16:32])

    # Updates the status for all packages for tracking at 9 am.
    time = datetime(2000, 1, 1, 9)
    for package in deliveryList:
        if package.time < time:
            package.track[time.strftime("%H:%M")] = 'Out for Delivery'
        else:
            package.track[time.strftime("%H:%M")] = package.status

    # Second truck leaves with delayed packages at 9:05 am. Mileage is updated.
    time = datetime(2000, 1, 1, 9, 5)
    mileage += deliver_packages(truck3, time, deliveryList[32:len(deliveryList) + 1])

    # Updates the status for all packages for tracking at 10 am.
    time = datetime(2000, 1, 1, 10)
    for package in deliveryList:
        if package.time < time:
            package.track[time.strftime("%H:%M")] = 'Out for Delivery'
        else:
            package.track[time.strftime("%H:%M")] = package.status

    # Updates the status for all packages for tracking at 11 am
    time = datetime(2000, 1, 1, 11)
    for package in deliveryList:
        if package.time < time:
            package.track[time.strftime("%H:%M")] = 'Out for Delivery'
        else:
            package.track[time.strftime("%H:%M")] = package.status

    # Third truck leaves with EOD packages at 11 am. Mileage is updated.
    mileage += deliver_packages(truck1, time, deliveryList[0:16])

    # Updates the status for all packages for tracking at 12 pm.
    time = datetime(2000, 1, 1, 12)
    for package in deliveryList:
        if package.time < time:
            package.track[time.strftime("%H:%M")] = 'Out for Delivery'
        else:
            package.track[time.strftime("%H:%M")] = package.status

    # Updates the status for all packages for tracking at 1 pm.
    time = datetime(2000, 1, 1, 13)
    for package in deliveryList:
        if package.time < time:
            package.track[time.strftime("%H:%M")] = 'Out for Delivery'
        else:
            package.track[time.strftime("%H:%M")] = package.status

    # Interface
    try:
        main_menu()
        option = int(input())

        while 1 > option > 4:
            print("Error: Invalid input. Try again\t")
            option = int(input())
        while option != 4:
            if option == 1:
                # Gets input and looks up the package from the hashtable
                key = int(input("Enter Package ID:\t"))
                package = ht.hash_search(key)
                if package is None:
                    print("Package not Found")
                else:
                    print(package)

            elif option == 2:
                time = int(input("Enter time from 8 - 17 (24hr, hour only)\t"))
                while time < 8 or time > 17:
                    print("Invalid input.")
                    time = int(input("Enter time from 8 - 17 (24hr, hour only)\t"))
                for i in range(40):
                    # Gets the time and gets all packages' info from the hashtable according to that time.
                    print(ht.hash_search(i).track_time(datetime(2000, 1, 1, time)))
                print()
                print(truck2)
                print(truck3)
                print(truck1)

            elif option == 3:
                # Prints the mileage for each truck and the combined mileage
                print()
                print('Truck 1 Mileage = %0.2f miles\t' % truck1.mileage)
                print('Truck 2 Mileage = %0.2f miles\t' % truck2.mileage)
                print('Truck 3 Mileage = %0.2f miles\t' % truck3.mileage)
                print('Total Mileage = %0.2f miles\t' % mileage)
                print()
            main_menu()
            option = int(input())
        quit()
    except(ValueError, IndexError):
        print("Invalid input")
        quit()
