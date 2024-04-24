
from getDistance import getDistance
from shared import packageHash
from nearestNeighbor import nearestNeighbor
from datetime import datetime, date, timedelta
from shared import milesPerHour
from shared import addressUpdateTime
from shared import addressHash
from shared import distanceMatrix

class Truck:
    def __init__(self):
        self.milesDriven = 0
        self.priority = []
        self.eod = []
        self.delivered = []
        self.currentAddress = 'HUB'
        self.time = ''
        self.name = ''

    def setName(self, name):
        self.name = name

    def addPriorityPackage(self, package):
        self.priority.append(package)
        return True

    def addEODPackage(self, package):
        self.eod.append(package)
        return True
    
    def printPackage(self):
        for package in self.priority:
            print(package._packageID)
        for package in self.eod:
            print(package._packageID)

    def startRoute(self, departureHour, departureMinute, desiredTime):
        self.time = datetime(year=date.today().year, month=date.today().month, day=date.today().day, hour=departureHour, minute=departureMinute)
        totalList = self.priority+self.eod
        #check for current time
        if self.time < desiredTime:
            for packageID in totalList:
                packageHash.get(packageID).setStatus('en Route')
            self.processDeliveries(self.priority, desiredTime)
            self.processDeliveries(self.eod, desiredTime)

        if(len(self.priority + self.eod) == 0):
            self.returnHome()
            
        return [self.milesDriven, self.time]

    def processDeliveries(self, packageList, desiredTime):
        while(len(packageList) > 0):
            if self.time > desiredTime: 
                return
            #Stops delivery process if time is past the desired time
            nextTargetAndDistance = nearestNeighbor(self.currentAddress, packageList)
            self.milesDriven += float(nextTargetAndDistance[1])

            timepassed = (float(nextTargetAndDistance[1])/milesPerHour) * 60
            self.time += timedelta(minutes=timepassed)

            if self.time > addressUpdateTime:
                packageHash.get('9').setAddress('410 S State St')

            if self.time < desiredTime: 
                packageList.remove(nextTargetAndDistance[0])
                self.delivered.append(nextTargetAndDistance[0])
                package = packageHash.get(nextTargetAndDistance[0])
                package.setStatus("Delivered at: " + self.time.strftime('%Y-%m-%d %H:%M:%S'))
                self.currentAddress = package.address
    
    def returnHome(self):
        distanceToHome = float(getDistance(self.currentAddress, 'HUB', distanceMatrix, addressHash))
        self.milesDriven += distanceToHome
        timepassed = (distanceToHome/milesPerHour) * 60
        self.time += timedelta(minutes=timepassed)
        self.currentAddress = 'HUB'

        