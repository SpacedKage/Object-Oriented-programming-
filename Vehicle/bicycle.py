from passengervehicle import PassengerVehicle

class Bicycle(PassengerVehicle):
    """Base class for Bicycle"""

    def __init__(self, unique_id, max_num_of_passengers, classification):
        super().__init__(unique_id, max_num_of_passengers)

        self.classification = classification

    def __str__(self):
        return f" Classification: {self.classification}."