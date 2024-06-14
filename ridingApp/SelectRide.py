from .Ride import Ride

class SelectRide(Ride):
    def __init__(self, id, user_id, rideDetails):
        super().__init__(id,user_id,rideDetails)
        self.requested_seats = rideDetails['requested_seats']
        self.preferred_vehicle = rideDetails.get('preferred_vehicle',None)  # Optional field  , if not present then we will consider Most Vacant Vehicle