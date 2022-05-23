class Plane:

    def __init__(self, name='', year=1900):
        self.name = name
        self.built_year = year


class CommercialPlane(Plane):

    def __init__(self, name='', year=1900, passengers=0, max_capacity=0):
        super().__init__(name, year)
        self.passengers = passengers
        self.max_capacity = max_capacity


class FreightPlane(Plane):

    def __init__(self, name='', year=1900, capacity=0, max_capacity=0):
        super().__init__(name, year)
        self.cargo_capacity = capacity
        self.max_capacity = max_capacity


class MilitaryPlane(Plane):
    def __init__(self, name='', year=1900, militaryVehicles=[]):
        super().__init__(name, year)
        # list of military vehicles being transported
        self.militaryVehicles = militaryVehicles
