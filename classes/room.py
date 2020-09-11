class Room:

    def __init__(self, input_room_name, input_room_price, input_room_capacity):

        self.name = input_room_name
        self.price = input_room_price
        self.capacity = input_room_capacity
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

    def add_guest_to_room(self, guest):
        return self.guests.append(guest)

    def remove_guest_from_room(self, guest):
        return self.guests.remove(guest)

    def remove_all_guests_from_room(self):
        self.guests = []

    

    