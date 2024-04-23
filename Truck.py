
from shared import packageHash
from nearestNeighbor import nearestNeighbor
from datetime import datetime, date, timedelta
from shared import milesPerHour
from shared import addressUpdateTime

class Truck:
    def __init__(self):
        self.milesDriven = 0
        self.priority = []
        self.eod = []
        self.delivered = []
        self.currentAddress = 'HUB'
        self.time = ''

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
        #check for current time
        if self.time < desiredTime:
            for packageID in self.priority+self.eod:
                packageHash.get(packageID).setStatus('en Route')
            self.processDeliveries(self.priority, desiredTime)
            self.processDeliveries(self.eod, desiredTime)
            print(self.milesDriven)
        return self.delivered

    def processDeliveries(self, packageList, desiredTime):
        while(len(packageList) > 0):

            #Stops delivery process if time is past the desired time
            if self.time > desiredTime: 
                return
            
            nextTargetAndDistance = nearestNeighbor(self.currentAddress, packageList)
            self.milesDriven += float(nextTargetAndDistance[1])

            timepassed = (float(nextTargetAndDistance[1])/milesPerHour) * 60
            self.time += timedelta(minutes=timepassed)

            if self.time > addressUpdateTime:
                packageHash.get('9').setAddress('410 S State St')

            
            packageList.remove(nextTargetAndDistance[0])
            self.delivered.append(nextTargetAndDistance[0])

            package = packageHash.get(nextTargetAndDistance[0])
            package.setStatus("Delivered at: " + self.time.strftime('%Y-%m-%d %H:%M:%S'))
            self.currentAddress = package.address
        