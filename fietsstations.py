import random

class Bike_station:
    
    def __init__(self,station_id, station_name, slot_amount):
        self.station_id = station_id
        self.station_name = station_name #the name of the station 
        self.slot_amount = slot_amount
        self.slots = self.create_slots() #the slots 

    def create_slots(self):
        """
        this method creates an i numbered of slots based on the slot_amount set
        """
        slots = []
        for i in range(1,self.slot_amount+1):
            slots.append(Bike_slot(self.station_id, i, False))

        return slots
    
    def lend_bike(self, user_object, simulatie_modus=False):
        available_bikes =  {}

        for slot in self.slots:
            #if there is a bike in the slot the bike can be checked out
            if slot.status == True:
                available_bikes[slot.slot_number] = slot
        
        #if the available_bikes dict is not filled then the station has no available bikes 
        if not available_bikes:
            print("No available bikes at this station.")
            return
        
        #a random slot must be chosen in simulation mode
        if simulatie_modus:

            slot_choice = random.choice(list(available_bikes.keys()))
        
        #prompt user for an input
        else:
            #print the slots which have a bike
            print("Available slots with bikes:")
            for available_slot in available_bikes:
                print(f"slot [{available_slot}] holds a bike")
            
            #prompt input 
            slot_choice = int(input("choose a slot: "))
            
            if slot_choice not in available_bikes:
                print(f"{input} slot does not have a bike or does not exist")
                return

        #find slot number assosiated with the bike
        slot_chosen = available_bikes[slot_choice]
        
        #grab the bike object attached to the slot
        bike_chosen = slot_chosen.bike

        #assign the bike to a user
        user_object.bike = bike_chosen
        
        #empty slot
        slot_chosen.status = False
        self.bike_object = ""

        # Check if the bike object is a string (indicating an error)
        if isinstance(user_object.bike, str):
            return
        else:
            print(f"\nbike {user_object.bike.bike_id} taken from slot: {slot_chosen.slot_number} at station: {self.station_name} by user: {user_object.user_id}")

    def check_bike_in(self, user_object, simulatie_modus=False):
        available_slots = {}

        for slot in self.slots:
            #if the slot is empty a bike can be checked in 
            if slot.status == False:
                available_slots[slot.slot_number] = slot
                
        #if the available slots stays empty exit the function
        if not available_slots:
            print("No available slots at this station.")
            return

        #a random slot must be chosen in simulation mode
        if simulatie_modus:

            slot_choice = random.choice(list(available_slots.keys()))

        else:
                
            #print the slots which have a bike
            print("Available slots:")
            for available_slot in available_slots:
                print(f"slot [{available_slot}] is free")
                    
            slot_choice = int(input(f"choose an empty slot:"))

            if slot_choice not in available_slots:
                print(f"slot: {slot_choice} Invalid slot number.")
                return

        chosen_slot = available_slots[slot_choice]

        #fill the slot with the bike object
        chosen_slot.bike = user_object.bike
        chosen_slot.status = True

        #take away the bike from the user object
        user_object.bike = ""

        # Check if the bike object is a string (indicating an error)
        if isinstance(chosen_slot.bike, str):
            return
        else:
            print(f"Bike: {chosen_slot.bike.bike_id} inserted in slot: {chosen_slot.slot_number} at station: {self.station_name} by user: {user_object.user_id}")
    
    def __str__(self):
        return str(f"station_id: {self.station_id}\nstation_name: {self.station_name}\nslot_amount: {len(self.slots)}\n---")
    
class Bike_slot:
    
    def __init__(self, bike_station, slot_number, status, bike_object=""):
        self.bike_station = bike_station #the bike_station object the slot is located at
        self.slot_number = slot_number #the slot number of that location
        self.status = status #boolean to determine if there is a bike in the slot
        self.bike = bike_object #the bike tied to the slot, if its eual to "" its empty

    def __str__(self):
        return str(f"Station: {self.bike_station}\nSlot_number: {self.slot_number}\nstatus: {self.status}")

class Bike:
    
    def __init__(self, bike_id):
        self.bike_id = bike_id #the bike number

class User:

    def __init__(self, user_id, name, lastname, bike=""):
        self.user_id = user_id #the ID of the user
        self.name = name #name of the user
        self.lastname = lastname #lastname of the user
        self.bike = bike #the bike the user could currently be using