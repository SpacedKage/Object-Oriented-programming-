from bicycle import Bicycle
from vehiclemanager import VehicleManager
from car import Car
from truck import Truck
from vehicle import Vehicle

Tandem = Bicycle (1, 2, "Tandem")
Mountain = Bicycle (2, 1, "Mountain")
Bmx =Bicycle (3, 2, "BMX" )
#Use lowercase on the left for var names

Honda = Car (21, 4, 5, "Honda")
Audi_Q7 = Car (22, 6, 5, "Audi Q7 ")
Smart = Car (23, 2, 3, "Smart Fortwo")

Dump = Truck (50, "28,000 pounds", 4, "Dump Truck")
Garbage = Truck (51, "80,000 pounds", 3, "Garbage Truck")
Flatbed = Truck (52, "48,000 pounds", 2, "Flatbed Truck")

list_of_vehicles = [Tandem, Mountain, Bmx, Honda, Audi_Q7, Smart, Dump, Garbage, Flatbed]
list_of_available_cars = [Honda, Audi_Q7, Smart]
list_of_available_bicycles = [Tandem, Mountain, Bmx]
list_of_available_trucks = [Dump, Garbage, Flatbed]

vm1 = VehicleManager (list_of_vehicles)
vm1.hire_vehicle(Tandem.unique_id, "25/05/2021") 
vm1.hire_vehicle(Mountain.unique_id, "03/07/2021")
vm1.hire_vehicle(Bmx.unique_id, "09/02/2021")
vm1.hire_vehicle(Honda.unique_id, "17/03/2021")
vm1.hire_vehicle(Audi_Q7.unique_id, "20/05/2021")
vm1.hire_vehicle(Smart.unique_id, "14/10/2021")
vm1.hire_vehicle(Dump.unique_id, "28/01/2021") 
vm1.hire_vehicle(Garbage.unique_id, "21/11/2021")
vm1.hire_vehicle(Flatbed.unique_id, "06/03/2021")

"""print (list_of_vehicles)"""

print (f"Bicycles Available for hire {vm1.available_bicycles()} {Bmx.unique_id} {Tandem.unique_id} {Mountain.unique_id}.")
print (f"Trucks Available for hire {vm1.available_trucks()} {Dump.unique_id} {Garbage.unique_id} {Flatbed.unique_id}.")
print (f"Cars Available for hire {vm1.available_cars()}{Honda.unique_id} {Audi_Q7.unique_id} {Smart.unique_id}.")










