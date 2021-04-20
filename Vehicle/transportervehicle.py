from vehicle import Vehicle

class TransporterVehicle(Vehicle):
    """Base class for all Transporter Vehicles"""

    def __init__(self, unique_id, load_capacity):
       super().__init__(unique_id) 

       self.load_capacity = load_capacity
    

    def __str__(self):
        return f"Load Capacity: {self.load_capacity}."
