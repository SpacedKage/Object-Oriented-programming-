from transportervehicle import TransporterVehicle

class Truck(TransporterVehicle):
    """Base class for Truck"""

    def __init__(self, unique_id, load_capacity, num_of_axels, classification):
        super().__init__(unique_id, load_capacity)

        self.num_of_axels = num_of_axels
        self.classification = classification

    def __str__(self):
        return f"Number of Axels {self.num_of_axels}."
