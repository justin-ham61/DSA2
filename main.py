import csv
from datetime import datetime, date
from Package import Package
from Truck import Truck
from shared import addressHash
from shared import packageHash
from shared import distanceMatrix

def main():


    #Prompts user to choose a time to look at the delivery status
    print("1: 8:45 a.m.")
    print("2: 9:45 a.m.")
    print("3: 10:45 a.m.")
    print("4: 11:45 a.m.")
    print("5: 12:45 a.m.")
    userInputWait = False
    while userInputWait == False:
        number = int(input("Please choose from the above options to get current delivery status for packages: "))
        if(number == 1):
            desiredTime = datetime(year=date.today().year, month=date.today().month, day=date.today().day, hour=8, minute=45)
            userInputWait = True
        elif number == 2:
            desiredTime = datetime(year=date.today().year, month=date.today().month, day=date.today().day, hour=9, minute=45)
            userInputWait = True
        elif number == 3: 
            desiredTime = datetime(year=date.today().year, month=date.today().month, day=date.today().day, hour=10, minute=45)
            userInputWait = True
        elif number == 4: 
            desiredTime = datetime(year=date.today().year, month=date.today().month, day=date.today().day, hour=11, minute=45)
            userInputWait = True
        elif number == 5:
            desiredTime = datetime(year=date.today().year, month=date.today().month, day=date.today().day, hour=12, minute=45)
            userInputWait = True

    #Iterable list of all packages
    packageList = []


    with open('WGUPS Distance Table.csv', newline='') as distanceFile:
        reader = csv.reader(distanceFile)

        #Skips the first 5 lines of the CSV file to get to necessary data
        for i in range(5):
            next(reader)

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
        for row in reader:
            package = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            packageList.append(package)
            packageHash.add(row[0], package)



    #Priorty/Early deadline truck
    truckA = Truck()
    #No deadline Truck
    truckB = Truck()
    #Late departure truck
    truckC = Truck()

    #Loading trucks
    for package in packageList:
        #If package contains a special note
        if package._note != '':
            if package._note == 'Can only be on truck 2':
                truckB.addEODPackage(package._packageID)   
            elif package._note == 'Delayed on flight---will not arrive to depot until 9:05 am':
                if package._deadline == 'EOD':
                    truckC.addEODPackage(package._packageID)
                else:
                    truckC.addPriorityPackage(package._packageID)
            elif package._note.startswith("Must be delivered with"):
                if package._deadline == 'EOD':
                    truckA.addEODPackage(package._packageID)
                else:
                    truckA.addPriorityPackage(package._packageID)
            elif package._note == 'Wrong address listed':
                truckC.addEODPackage(package._packageID)

        #Special case for 19 since it has to be delivered with other packages
        elif package._packageID == '19': 
            truckA.addPriorityPackage(package._packageID)

        #If package has no deadline AND isn't loaded in a vehicle already
        elif package._deadline == 'EOD':
            if((len(truckB.eod) + len(truckB.priority)) < 14):
                truckB.addEODPackage(package._packageID)
            else:
                truckC.addEODPackage(package._packageID)

        elif package._deadline != 'EOD':
            if(len(truckA.eod) + len(truckA.priority) < 16):
                truckA.addPriorityPackage(package._packageID)

    delivered = truckA.startRoute(8,0, desiredTime)
    delivered.extend(truckB.startRoute(8,0, desiredTime))
    delivered.extend(truckC.startRoute(9,5, desiredTime))

    for package in packageList:
        print(package.packageID, package.status)


main()