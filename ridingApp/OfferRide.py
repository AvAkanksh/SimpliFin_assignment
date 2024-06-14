from .Ride import Ride

class OfferRide(Ride):
    def __init__(self, id, user_id, vehicle_id, rideDetails):
        super().__init__(id, user_id, rideDetails)
        self.vehicle_id = vehicle_id
        self.avail_seats = rideDetails['avail_seats']