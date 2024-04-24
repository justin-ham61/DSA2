class Package:
    def __init__(self, packageID, address, city, state, zipcode, deadline, weight, notes):
        self._packageID = packageID
        self._address = address
        self._city = city
        self._state = state
        self._zipcode = zipcode
        self._deadline = deadline
        self._weight = weight
        self._status = 'At the Hub'
        self._note = notes
        self._truck = 'No Truck'

    @property
    def truck(self):
        return self._truck
    
    @property
    def packageID(self):
        return self._packageID
    @property
    def address(self):
        return self._address
    @property
    def city(self):
        return self._city
    @property
    def state(self):
        return self._state
    @property
    def zipcode(self):
        return self._zipcode
    @property
    def deadline(self):
        return self._deadline
    @property
    def weight(self):
        return self._weight
    @property 
    def status(self):
        return self._status
    @property
    def notes(self):
        return self._notes
    
    def setStatus(self, status):
        self._status = status

    def setAddress(self, address):
        self._address = address 

    def setTruck(self, truck):
        self._truck = truck

    @truck.setter
    def truck(self, truck):
        self._truck = truck 
        
    @packageID.setter
    def packageID(self, packageID):
        self._packageID = packageID

    @address.setter
    def address(self, address):
        self._address = address

    @city.setter
    def city(self, city):
        self._city = city

    @state.setter
    def state(self, state):
        self._state = state

    @zipcode.setter
    def zipcode(self, zipcode):
        self._zipcode = zipcode

    @deadline.setter
    def deadline(self, deadline):
        self._deadline = deadline

    @weight.setter  
    def weight(self, weight):
        self._weight = weight

    @status.setter
    def status(self, status):
        self._status = status
        
    @notes.setter
    def notes(self, notes):
        self._notes = notes

    def print(self):
        print(self._packageID, self._address, self._city, self._deadline, self._note, self._status)
