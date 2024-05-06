import json
import pickle
import random
import time
import sys 

#import de klassen
from fietsstations import *

def get_station_names():
    # Open the GeoJSON file
    with open('velo.geojson', 'r') as f:
        geojson_data = json.load(f)

    # Initialize an empty list to store the values of "Naam"
    name_list = []

    # Iterate over each feature in the GeoJSON data
    for feature in geojson_data['features']:
        # Check if the 'Naam' property exists in the feature's properties
        if 'Naam' in feature['properties']:
            # Append the value of 'Naam' to the naam_list
            name_list.append(feature['properties']['Naam'])
    # Print the list of 'Naam' values
    return name_list

def get_slot_amounts():
    # Open the GeoJSON file
    with open('velo.geojson', 'r') as f:
        geojson_data = json.load(f)

    slot_amounts = []

    for feature in geojson_data['features']:

        if 'Aantal_plaatsen' in feature['properties']:
            slot_amounts.append(feature['properties']['Aantal_plaatsen'])

    return slot_amounts

def create_objects(user_amount, bike_amount):
        """
        a function which creates the stations with slot objects, user objects and bike objects
        """
        
        station_names = get_station_names()
        slot_amounts = get_slot_amounts()

        stations = []
        users = []
        bikes = []

        #create the bike stations and slots (slots are created using the slot amount and added to a list per bike station)
        for i, (station_name, slot_amount) in enumerate(zip(station_names, slot_amounts)):
            stations.append(Bike_station(i, station_name, slot_amount))

        #create 500 users

        for i in range(1,user_amount):
            users.append(User(i,"John", "Smith"))

        #create 400 bikes

        for i in range(1,bike_amount):
            bikes.append(Bike(i))

        return stations, users, bikes

def assign_bikes_to_slots():
    """
    a function which adds the bikes to a random stations slot
    """
    for bike_object in bikes:

        #check if the slot is taken, if its taken select a new random slot
        while True:
            station = random.choice(stations)
            slot = random.choice(station.slots)

            #if the slot status is set to True, it allready has a bike
            if slot.status == True:
                station = random.choice(stations)
                slot = random.choice(station.slots)
            
            #else it is set to False, the bike slot is empty and can be filled
            else:
                
                slot.bike = bike_object #set the equal to the bike object
                slot.status = True #set the status to False
                break #break the infinite loop

def save_data(file_name, list_of_objects):
    """
    a function which saves the objects
    
    """
    with open(file_name, 'wb') as file:
        pickle.dump(list_of_objects, file)

def load_data(file):
    """
    a function which loads the stations.pkl, users.pkl and bikes.pkl files which hold saved objects
    """
    with open(file, 'rb') as file:
        # Load the serialized list of objects from the file
        objects = pickle.load(file)

    return objects

def start_simulation(user_time):
    start_time = time.time()
    print(f"starting simulation for {user_time}s...")

    while time.time() - start_time < user_time:
        
        #select random user
        random_user = random.choice(users)
        #select a random station to check a bike out of
        random_station_out = random.choice(stations)
        #select a random station to check a bike back in
        random_station_in = random.choice(stations)
        
        #simulate getting a bike
        random_station_out.lend_bike(random_user, True)
        
        #simulate check bike back in random station 2
        random_station_in.check_bike_in(random_user, True)


if __name__ == "__main__":

    simulation_mode = "-s" in sys.argv #a bool to represent simulation mode

    while True:

        if simulation_mode:
            choice = 3  # Set choice to 3 if the flag is provided
            simulation_mode = False

        else:

            print("[NOTE] choose Load existing data set if you want to use your simulated data from the simulation mode")
            choice = int(input("""
            1: create new data set
            2: Load existing data set
            3: Start Simulation mode\n: """))
        

        if choice == 1:
            # create the station with slots, 500 users and 1000 bikes
            user_amount = 500
            bike_amount = 1000
            stations, users, bikes = create_objects(user_amount+1, bike_amount+1)

            # assign the bike objects to a random station slot
            assign_bikes_to_slots()
            
            # save the objects with the pickle library
            print("saving new data set...")
            save_data("stations.pkl", stations)
            save_data("users.pkl", users)
            save_data("bikes.pkl", bikes)

            #break the first menu loop
            break

        if choice == 2:
            # load the store files
            print("loading in saved data...")
            stations = load_data("stations.pkl")
            users = load_data("users.pkl")
            bikes = load_data("bikes.pkl")
            
            #break the first menu loop
            break

        
        if choice == 3:
            # create the station with slots, 500 users and 1000 bikes
            user_amount = 500
            bike_amount = 1000
            stations, users, bikes = create_objects(user_amount+1, bike_amount+1)

            # assign the bike objects to a random station slot
            assign_bikes_to_slots()
            
            print("[NOTE] The data simulated will be saved automatically and used until you create a new data set\n")
            user_time = int(input("Input for how long you want to run the simulation (in seconds): "))
            start_simulation(user_time)
            
            # save the objects with the pickle library after simulation
            print("Saving simulated data...")
            save_data("stations.pkl", stations)
            save_data("users.pkl", users)
            save_data("bikes.pkl", bikes)
        
    #set a user
    user = random.choice(users)

    while True:
            print(f"Logged in as user: {user.user_id}")
            if isinstance(user.bike, str):
                print("you do not currently own a bike")
            else:
                print(f"you own bike: {user.bike.bike_id}")
            
            choice2 = int(input("""
        1: check bike in
        2: lend a bike\n:
        """))
            
            if choice2 == 1:
                #if the user has a bike then he can put it back in the slot
                if user.bike:
                    
                    for index, station in enumerate(stations):
                        print(f"{index} : {station.station_name}")

                    station_index = int(input("Choose a station(by index) you want to inser a bike in: "))

                    station_chosen = stations[station_index]

                    station_chosen.check_bike_in(user)

                    # save the objects with the pickle library after the checkin of a bike at a station
                    save_data("stations.pkl", stations)
                    save_data("users.pkl", users)
                    save_data("bikes.pkl", bikes)

                else:
                    print(f"you do not own a bike to check into a station")

            if choice2 == 2:
                #if the user bike is not set, then he can check out a bike
                if not user.bike:

                    for index, station in enumerate(stations):
                        print(f"{index} : {station.station_name}")

                    station_index = int(input("choose a station(by index) you want to take a bike from: "))

                    station_chosen = stations[station_index]

                    station_chosen.lend_bike(user)

                    # save the objects with the pickle library after a bike lend
                    save_data("stations.pkl", stations)
                    save_data("users.pkl", users)
                    save_data("bikes.pkl", bikes)

                else:
                    print(f"you still have bike {user.bike.bike_id} in your possesion, check it out before you take a new bike")


