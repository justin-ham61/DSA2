def getDistance(currentAddress, targetAddress, distanceMatrix, addressHash):
    keyA = addressHash.get(currentAddress)
    keyB = addressHash.get(targetAddress)
    return distanceMatrix[keyA][keyB]