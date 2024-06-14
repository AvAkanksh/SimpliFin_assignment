from ridingApp.RideSharingManagement import RideShareManagement

rideShareManagement = RideShareManagement()
print("-"*15+"Task 1: Onboard users and vehicles"+"-"*15)
# add_user("Rohan, M, 36"); add_vehicle("Rohan, Swift, KA-01-12345")
# add_user("Shashank, M, 29"); add_vehicle("Shashank, Baleno, TS-05-62395")
# add_user("Nandini, F, 29")
# add_user("Shipra, F, 27"); add_vehicle("Shipra, Polo, KA-05-41491"); add_vehicle ("Shipra, Activa, KA-12-12332")
# add_user("Gaurav, M, 29")
# add_user("Rahul, M, 35"); add_vehicle("Rahul, XUV, KA-05-1234")

rideShareManagement.add_user_vehicle(userDetails={
    "name":"Rohan",
    "gender":"M",
    "age":36
},vehicleDetails=[
    {
        "name":"Swift",
        "number_plate":"KA-01-12345"
    }
])

rideShareManagement.add_user_vehicle(userDetails={
    "name":"Shashank",
    "gender":"M",
    "age":29
},vehicleDetails=[
    {
        "name":"Baleno",
        "number_plate":"TS-05-62395"
    }
])

rideShareManagement.add_user_vehicle(userDetails={
    "name":"Nandini",
    "gender":"F",
    "age":29
},vehicleDetails=[])

rideShareManagement.add_user_vehicle(userDetails={
    "name":"Shipra",
    "gender":"F",
    "age":27
},vehicleDetails=[
    {
        "name":"Polo",
        "number_plate":"KA-05-41491"
    },
    {
        "name":"Activa",
        "number_plate":"KA-12-12332"
    }
])

rideShareManagement.add_user_vehicle(userDetails={
    "name":"Gaurav",
    "gender":"M",
    "age":29
},vehicleDetails=[])

rideShareManagement.add_user_vehicle(userDetails={
    "name":"Rahul",
    "gender":"M",
    "age":35
},vehicleDetails=[
    {
        "name":"XUV",
        "number_plate":"KA-05-1234"
    }
])


print("-"*15+"Task 2: Offer Rides"+"-"*15)

# User(id=1, name=Rohan, gender=M, age=36, rides_offered=0, rides_taken=0)
# User(id=2, name=Shashank, gender=M, age=29, rides_offered=0, rides_taken=0)
# User(id=3, name=Nandini, gender=F, age=29, rides_offered=0, rides_taken=0)
# User(id=4, name=Shipra, gender=F, age=27, rides_offered=0, rides_taken=0)
# User(id=5, name=Gaurav, gender=M, age=29, rides_offered=0, rides_taken=0)
# User(id=6, name=Rahul, gender=M, age=35, rides_offered=0, rides_taken=0)


# Vehicle(1, OwnerId: 1, Vehicle Name :  Swift , Number Plate: KA-01-12345)
# Vehicle(2, OwnerId: 2, Vehicle Name :  Baleno , Number Plate: TS-05-62395)
# Vehicle(3, OwnerId: 4, Vehicle Name :  Polo , Number Plate: KA-05-41491)
# Vehicle(4, OwnerId: 4, Vehicle Name :  Activa , Number Plate: KA-12-12332)
# Vehicle(5, OwnerId: 6, Vehicle Name :  XUV , Number Plate: KA-05-1234)

# offer_ride("Rohan, Origin=Hyderabad, Available Seats=1, Vehicle-Swift, KA-01-12345, Destination=Bangalore")
# offer_ride("Shipra, Origin=Bangalore, Available Seats=1, Vehicle-Activa, KA-12-12332, Destination=Mysore")
# offer_ride("Shipra, Origin=Bangalore, Available Seats=2, Vehicle=Polo, KA-05-41491, Destination=Mysore")
# offer_ride("Shashank, Origin=Hyderabad, Available Seats=2, Vehicle=Baleno, TS-05-62395, Destination=Bangalore")
# offer_ride("Rahul, Origin=Hyderabad, Available Seats=5, Vehicle-XUV, KA-05-1234, Destination=Bangalore")
# offer_ride("Rohan, Origin=Bangalore, Available Seats=1, Vehicle=Swift, KA-01-12345, Destination=Pune")


rideShareManagement.offer_ride(1,1,{
    "origin":"Hyderabad",
    "destination":"Bangalore",
    "avail_seats":1
})

rideShareManagement.offer_ride(4,4,{
    "origin":"Bangalore",
    "destination":"Mysore",
    "avail_seats":1
})

rideShareManagement.offer_ride(4,3,{
    "origin":"Bangalore",
    "destination":"Mysore",
    "avail_seats":2
})

rideShareManagement.offer_ride(2,2,{
    "origin":"Hyderabad",
    "destination":"Bangalore",
    "avail_seats":2
})

rideShareManagement.offer_ride(6,5,{
    "origin":"Hyderabad",
    "destination":"Bangalore",
    "avail_seats":5
})

rideShareManagement.offer_ride(1,1,{
    "origin":"Bangalore",
    "destination":"Pune",
    "avail_seats":1
})

print("-"*15+"Task 3: Select Rides"+"-"*15)

# select_ride("Nandini, Origin-Bangalore, Destination-Mysore, Seats-1, Most Vacant") (2(c) is the desired output)
# select_ride("Gaurav, Origin-Bangalore, Destination-Mysore, Seats 1, Preferred Vehicle-Activa") (2(b) is the desired output)
# select_ride("Shashank, Origin=Mumbai, Destination-Bangalore, Seats-1, Most Vacant") (No rides found)
# select_ride("Rohan, Origin-Hyderabad, Destination-Bangalore, Seats-1, Preferred Vehicle-Baleno") (2(d) is the desired output)
# select ride("Shashank, Origin=Hyderabad, Destination-Bangalore, Seats=1, Preferred Vehicle Polo") (No rides found)

rideShareManagement.select_ride(3,{
    "origin":"Bangalore",
    "destination":"Mysore",
    "requested_seats":1
    # "preference":"Most Vacant" if nothing is mentioned in the constructor then its by defaulted as Most Vacant
})

rideShareManagement.select_ride(5,{
    "origin":"Bangalore",
    "destination":"Mysore",
    "requested_seats":1,
    "preferred_vehicle":"Activa"
})

rideShareManagement.select_ride(2,{
    "origin":"Mumbai",
    "destination":"Bangalore",
    "requested_seats":1
})

rideShareManagement.select_ride(4,{
    "origin":"Hyderabad",
    "destination":"Bangalore",
    "requested_seats":1,
    "preferred_vehicle":"Baleno"
})

rideShareManagement.select_ride(2,{
    "origin":"Hyderabad",
    "destination":"Bangalore",
    "requested_seats":1,
    "preferred_vehicle":"Polo"
})

print("-"*15+"Task 4: End Rides"+"-"*15)

# end_ride (2-a)
# end_ride (2-b)
# end_ride (2-c)
# end_ride (2-d)

rideShareManagement.end_ride(1)
rideShareManagement.end_ride(2)
rideShareManagement.end_ride(3)
rideShareManagement.end_ride(4)

print("-"*15+"Task 5: Print Stats"+"-"*15)

for user in rideShareManagement.users.values():
    print(user)

