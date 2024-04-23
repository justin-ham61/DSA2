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
    
    
    @packageID.setter
    def id(self, packageID):
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

