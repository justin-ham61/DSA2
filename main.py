#Student ID: 012131356

import csv
from datetime import datetime, date
from Package import Package
from Truck import Truck
from shared import addressHash, packageHash, distanceMatrix

def main():
    #Prompts user to choose a time to look at the delivery status
    userInputWait = False
    while userInputWait == False:
        hour = int(input("Please enter the hour (between 0-24) to retrieve status from: "))
        if(isinstance(hour, int) and hour <= 24 and hour >= 0 ):
            minute = int(input("Please enter the minute (between 0-60) to retreive status from: "))
            if(isinstance(minute, int) and minute <= 60 and minute >= 0):
                desiredTime = datetime(year=date.today().year, month=date.today().month, day=date.today().day, hour=hour, minute=minute)
                userInputWait = True
        else:
            print("Please enter a valid number")

    #Iterable list of all packages
    packageList = []

    #CSV Parser for Distance Table.csv
    with open('WGUPS Distance Table.csv', newline='') as distanceFile:
        reader = csv.reader(distanceFile)

        #Skips the first 5 lines of the CSV file to get to necessary data
        for i in range(5):
            next(reader)

        #Loops through each row of the CSV file
        for i,row in enumerate(reader):
            #Adds address into addressHash
            address = row[1].split('\n')[0].strip()
            value = i
            addressHash.add(address, value)

            #Creates distance matrix
            matrixRow = []
            for j in range(len(row) - 2):
                cellValue = row[j + 2]
                matrixRow.append(cellValue)
                if cellValue != '' and cellValue != '0':
                    distanceMatrix[j][i] = cellValue
            distanceMatrix.append(matrixRow)


    #Creates Package class and adds them to the hashmap using Package ID as the key
    with open('WGUPS Package File.csv', newline='') as packageFile:
        reader = csv.reader(packageFile)

        #Skips the first 8 lines of the CSV file to get to necessary data
        for i in range(8):
            next(reader)
        
        #Loops thorugh the CSV file creating Package object for each row and adds them to the dictionary with key
        for row in reader:
            package = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            packageList.append(package)
            packageHash.add(row[0], package)



    #Priorty/Early deadline truck
    truck1 = Truck()
    truck1.setName('Truck 1')
    #No deadline Truck
    truck2 = Truck()
    truck2.setName('Truck 2')
    #Late departure truck
    truck3 = Truck()
    truck3.setName('Truck 3')

    #Loading trucks
    for package in packageList:
        #If package contains a special note
        if package._note != '':
            if package._note == 'Can only be on truck 2':
                truck2.addEODPackage(package._packageID)   
                package.setTruck('Truck 2')
            elif package._note == 'Delayed on flight---will not arrive to depot until 9:05 am':
                if package._deadline == 'EOD':
                    truck3.addEODPackage(package._packageID)
                    package.setTruck('Truck 3')
                else:
                    truck3.addPriorityPackage(package._packageID)
                    package.setTruck('Truck 3')
            elif package._note.startswith("Must be delivered with"):
                if package._deadline == 'EOD':
                    truck1.addEODPackage(package._packageID)
                    package.setTruck('Truck 1')
                else:
                    truck1.addPriorityPackage(package._packageID)
                    package.setTruck('Truck 1')
            elif package._note == 'Wrong address listed':
                truck3.addEODPackage(package._packageID)
                package.setTruck('Truck 3')

        #Special case for 19 since it has to be delivered with other packages
        elif package._packageID == '19': 
            truck1.addPriorityPackage(package._packageID)
            package.setTruck('Truck 1')

        #If package has no deadline AND isn't loaded in a vehicle already
        elif package._deadline == 'EOD':
            if((len(truck2.eod) + len(truck2.priority)) < 14):
                truck2.addEODPackage(package._packageID)
                package.setTruck('Truck 2')
            else:
                truck3.addEODPackage(package._packageID)
                package.setTruck('Truck 3')

        elif package._deadline != 'EOD':
            if(len(truck1.eod) + len(truck1.priority) < 16):
                truck1.addPriorityPackage(package._packageID)
                package.setTruck('Truck 1')

    #After all packages are loaded onto the truck, Truck 1 and Truck 2 leave at 8:00AM
    truckAData = truck1.startRoute(8,0, desiredTime)
    truckBData = truck2.startRoute(8,0, desiredTime)

    #Truck 3 Planned departure time
    truckCTime = datetime(year=date.today().year, month=date.today().month, day=date.today().day, hour=9, minute=5)

    #If Truck A or Truck B are returned before 9:05, Truck C leaves at 9:05 since package has arrived and one driver is available
    if(truckAData[1] < truckCTime or truckBData[1] < truckCTime):
        truckCData = truck3.startRoute(9,5, desiredTime)

    #If neither Truck A or B are back, the departure time for Truck C will be A or B
    else:
        hour = truckAData[1].hour
        minute = truckAData[1].minute
        truckCData = truck3.startRoute(hour, minute, desiredTime)

    #Calculate total mileage
    totalMile = truckAData[0] + truckBData[0] + truckCData[0]

    #Print results
    print()
    print("----------Retrieving data from: ", desiredTime)
    print()
    print("Total miles driven by all the trucks currently:", round(totalMile, 2), "Miles")
    print()

    print("------------------- Truck 1 Information ------------------------------------")
    print("Remaining Packages on", truck1.name, ":", truck1.priority+truck1.eod)
    print("Delivered by Truck 1:", truck1.delivered)
    print("Current truck location:", truck1.currentAddress)
    print("Miles driven by Truck 1:", truck1.milesDriven)
    print()
    print("------------------- Truck 2 Information ------------------------------------")
    print("Remaining Packages on", truck2.name, ":", truck2.priority+truck2.eod)
    print("Delivered by Truck 2:", truck2.delivered)
    print("Current truck location:", truck2.currentAddress)
    print("Miles driven by Truck 2:", truck2.milesDriven)
    print()
    print("------------------- Truck 3 Information ------------------------------------")
    print("Remaining Packages on", truck3.name, ":", truck3.priority+truck3.eod)
    print("Delivered by Truck 3:", truck3.delivered)
    print("Current truck location:", truck3.currentAddress)
    print("Miles driven by Truck 3:", truck3.milesDriven)
    print() 

    #Loops through package list and prints data for all package
    for package in packageList:
        print("Package:", package.packageID, "| Address:", package.address, "| Deadline:", package.deadline, "| Truck:", package.truck,"| Status:", package.status)


main()