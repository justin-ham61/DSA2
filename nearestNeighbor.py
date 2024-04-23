from shared import addressHash
from shared import packageHash
from shared import distanceMatrix
from getDistance import getDistance

def nearestNeighbor(currentAddress, packageList):
    minDistance = 1000.0
    minPackageID = 0
    for packageID in packageList:
        package = packageHash.get(packageID)
        distance = getDistance(currentAddress, package.address, distanceMatrix, addressHash)
        if float(distance) < float(minDistance):
            minDistance = distance
            minPackageID = packageID
    return [minPackageID, minDistance]