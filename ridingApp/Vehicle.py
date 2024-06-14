class Vehicle:
    def __init__(self,id,vehicleDetails, user_id):
        self.id = id
        self.user_id = user_id
        self.vehicle_name, self.number_plate = vehicleDetails["name"], vehicleDetails["number_plate"]

    def __repr__(self) :
        return f"Vehicle({self.id}, OwnerId: {self.user_id}, Vehicle Name :  {self.vehicle_name} , Number Plate: {self.number_plate})"