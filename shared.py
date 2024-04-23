from Hash import HashMap
from datetime import datetime, date

#Average speed for deliverty truck
milesPerHour = 18

#contains Address name keyed by address
addressHash = HashMap()
addressHash.setName('Address')

#contains Package keyed by Package ID in String
packageHash = HashMap()
packageHash.setName('Package')

#[i][j] to get distance between two addresses
distanceMatrix = []

#Special update time for a wrong address occuring at 10:20
addressUpdateTime = datetime(year=date.today().year, month=date.today().month, day=date.today().day, hour=10, minute=20)