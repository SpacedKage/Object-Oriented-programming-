from vehicle import Vehicle

class PassengerVehicle(Vehicle):
    """Base class for passenger vehicle"""

    def __init__(self, unique_id, max_num_of_passengers):
       super().__init__(unique_id) 

       self.max_num_of_passengers = max_num_of_passengers

    def __str__(self):
        return f"Maximum number of passengers: {self.max_num_of_passengers}."