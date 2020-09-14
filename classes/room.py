from classes.guest import Guest
from classes.song import Song

class Room:

    def __init__(self, input_room_name, input_room_price, input_room_capacity):

        self.name = input_room_name
        self.price = input_room_price
        self.capacity = input_room_capacity
        self.till = []
        self.guests = []
        self.songs = []

    def get_room_name(self):
        return self.name

    def get_room_price(self):
        return self.price

    def get_room_capacity(self):
        return self.capacity

    def get_current_guests(self):
        return len(self.guests)

    def take_room_payment_from_guest(self, guest):
        guest.remove_cash(self.price)
        self.till.append(self.price)
        return int(self.till[-1])
        
    def add_guest_to_room(self, guest):
        capacity = self.get_room_capacity()
        current_guests = self.get_current_guests()
        if current_guests < capacity:

            return self.guests.append(guest)
        else:
            return "Room is full"

    def remove_guest_from_room(self, guest):
        return self.guests.remove(guest)

    def remove_all_guests_from_room(self):
        self.guests = []

    def add_song_to_room(self, song):
        self.songs.append(song.name)
        return self.songs[-1]



    

    