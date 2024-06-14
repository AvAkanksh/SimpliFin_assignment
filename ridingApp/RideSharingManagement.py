from .User import User
from .Vehicle import Vehicle
from .OfferRide import OfferRide
from .SelectRide import SelectRide

class RideShareManagement:
    def __init__(self):
        self.users = {}
        self.vehicles = {}
        self.rides = {}
        self.next_user_id = 1
        self.next_vehicle_id = 1
        self.next_ride_id = 1
        self.next_ride_request_id = 1


    def add_user(self, userDetails):
        new_user = User(self.next_user_id,userDetails)
        self.users[self.next_user_id] = new_user
        self.next_user_id += 1
        return new_user.id


    def add_vehicle(self, vehicleDetails, user_id):
        new_vehicle = Vehicle(self.next_vehicle_id, vehicleDetails, user_id)
        self.vehicles[self.next_vehicle_id] = new_vehicle
        self.next_vehicle_id += 1
        return new_vehicle.id


    def add_user_vehicle(self,userDetails,vehicleDetails=[]):
        user_id = self.add_user(userDetails)
        
        for vehicle in vehicleDetails:
            self.add_vehicle(vehicle, user_id)


    def offer_ride(self,user_id, vehicle_id, rideDetails ):
        if(self.validate_offered_ride(vehicle_id)==False):
            print("Ride already offered for this vehicle")
            return -1
        new_ride = OfferRide(self.next_ride_id, user_id, vehicle_id, rideDetails)
        self.users[user_id].rides_offered.append(new_ride.id)
        self.next_ride_id += 1
        self.rides[new_ride.id] = new_ride
        return new_ride.id


    def validate_offered_ride(self, vehicle_id):
        for ride in self.rides:
            if(self.rides[ride].vehicle_id == vehicle_id):
                return False
        return True

    def select_ride(self, user_id, rideDetails):
        new_select_ride_request = SelectRide( self.next_ride_request_id,user_id, rideDetails)
        self.next_ride_request_id += 1
        selected_ride = None
        for ride in self.rides:
            ride = self.rides[ride]
            if(ride.origin == new_select_ride_request.origin and ride.destination == new_select_ride_request.destination and ride.avail_seats>=new_select_ride_request.requested_seats):
                if(new_select_ride_request.preferred_vehicle==None):
                    if(selected_ride==None):
                        selected_ride = ride.id
                    elif(ride.avail_seats > self.rides[selected_ride].avail_seats):
                        selected_ride = ride.id
                elif(self.vehicles[ride.vehicle_id].vehicle_name==new_select_ride_request.preferred_vehicle):
                    selected_ride = ride.id
                    break
        if(selected_ride == None):
            print("No rides found")
            return -1
        self.users[user_id].rides_taken.append(selected_ride)
        print(f"Ride got selected ride_id : {selected_ride}")
        return selected_ride
    
    def end_ride(self, ride_id):
        if(ride_id in self.rides):
            del self.rides[ride_id]
        else:
            print("Ride not found")
