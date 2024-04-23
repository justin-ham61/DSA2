import csv
from Hash import HashMap
from Package import Package

#contains Address name keyed by i
addressHash = HashMap()
addressHash.setName('Address')

packageHash = HashMap()
packageHash.setName('Package')


#[i][j] to get distance between two addresses
distanceMatrix = []


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
        print(row)
        package = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        packageHash.add(row[0], package)

