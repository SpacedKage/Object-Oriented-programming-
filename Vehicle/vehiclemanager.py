from bicycle import Bicycle
from car import Car
from truck import Truck

class VehicleManager:
    """Base class for vehicle manager"""

    def __init__(self, vehicles):
        self.vehicles = vehicles 





    def hire_vehicle(self, unique_id, hire_date):
        for vehicle in self.vehicles:
            if vehicle.unique_id == unique_id:
                vehicle.hire_date = hire_date
                vehicle.return_date = ""
                return

                #break or return to stop the loop

    def return_vehicle(self, unique_id, return_date):
        for vehicle in self.vehicles:
            if vehicle.unique_id == unique_id:
                vehicle.hire_date = ""
                vehicle.return_date = return_date
                return


    def available_trucks(self):
        list_of_available = []

        for vehicle in self.vehicles:
            if isinstance(vehicle, Truck) and vehicle.hire_date == "":
                list_of_available.append(vehicle)
        
        return list_of_available

    def available_cars(self):
        list_of_available = []

        for vehicle in self.vehicles:
            if isinstance(vehicle, Car) and vehicle.hire_date == "":
                list_of_available.append(vehicle)
        
        return list_of_available


    def available_bicycles(self):
        list_of_available = []

        for vehicle in self.vehicles:
            if isinstance(vehicle, Bicycle) and vehicle.hire_date == "":
                list_of_available.append(vehicle)
        
        return list_of_available

def __str__(self):
        return f"ID: {self.unique_id} Hire Date: {self.hire_date} Return Date: {self.return_date}."
        

