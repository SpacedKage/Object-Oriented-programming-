from passengervehicle import PassengerVehicle

class Car(PassengerVehicle):
    """base class for car"""

    def __init__(self, unique_id, max_num_of_passengers, num_of_doors, classification):
        super().__init__(unique_id, max_num_of_passengers)

        self.num_of_doors = num_of_doors
        self.classification = classification

    def __str__(self):
        return f"Car:{self.unique_id} Max number of passengers: {self.max_num_of_passengers} Number of Doors {self.num_of_doors}."