class Ride:
     def __init__(self, id,user_id, rideDetails):
         self.id = id
         self.user_id = user_id
         self.origin = rideDetails["origin"]
         self.destination = rideDetails["destination"]