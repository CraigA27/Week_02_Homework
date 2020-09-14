import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Room 1", 40, 4)
        self.guests = Guest("Rocky", 100, "Eye of the tiger")

    def test_room_has_name(self):
        self.assertEqual("Room 1", self.room.name)

    def test_room_has_price(self):
        self.assertEqual(40, self.room.price)

    def test_room_has_capacity(self):
        self.assertEqual(4, self.room.capacity)

    def test_can_get_current_guests(self):
        self.room.add_guest_to_room(self.guests)
        self.assertEqual(1, self.room.get_current_guests())
    
    def test_can_add_guest_to_room(self):
        guest = Guest("Rocky", 100, "Eye of the tiger")
        self.room.guests.append(guest)
        self.assertEqual(1, self.room.get_current_guests())

    def test_can_remove_guest_from_room(self):
        guest = Guest("Rocky", 100, "Eye of the tiger")
        self.room.guests.append(guest)
        self.room.guests.remove(guest)
        self.assertEqual (0, self.room.get_current_guests())

    def test_can_remove_all_guests_from_room(self):
        guest = Guest("Rocky", 100, "Eye of the tiger")
        self.room.guests.append(guest)
        self.room.guests = []
        self.assertEqual(0, self.room.get_current_guests())

    def test_can_add_guest_to_room_room_full(self):
        guest_1 = Guest("Rocky", 100, "Eye of the tiger")
        guest_2 = Guest("Apollo", 100, "Living in America")
        guest_3 = Guest("Adrian", 100, "No easy way out")
        guest_4 = Guest("Paulie", 100, "Heart's on fire")
        guest_5 = Guest("Ivan", 100, "Burning heart")
        self.room.guests.append(guest_1)
        self.room.guests.append(guest_2)
        self.room.guests.append(guest_3)
        self.room.guests.append(guest_4)
        self.assertEqual("Room is full", self.room.add_guest_to_room(guest_5))

    def test_can_take_room_payment_from_guest(self):
        self.assertEqual(40, self.room.take_room_payment_from_guest(self.guests))

    def test_can_add_song_to_room(self):
        song = Song("Eye of the tiger")
        self.assertEqual("Eye of the tiger", self.room.add_song_to_room(song))
    
        



