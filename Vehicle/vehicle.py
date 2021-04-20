
class Vehicle:
    """The base class for all Vehicles"""

    v_count = 0

    def __init__(self, unique_id):
        self.unique_id = unique_id
        self.hire_date = ""
        self.return_date = ""
        Vehicle.v_count += 1

    def __str__(self):
        return f"ID: {self.unique_id} Hire Date: {self.hire_date} Return Date: {self.return_date}."
        