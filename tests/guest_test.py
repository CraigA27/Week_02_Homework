import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Rocky", 100, "Eye of the tiger")

    def test_guest_has_name(self):
        self.assertEqual("Rocky", self.guest.name)

    def test_guest_has_cash(self):
        self.assertEqual(100, self.guest.cash)

    def test_guest_has_fav_song(self):
        self.assertEqual("Eye of the tiger", self.guest.fav_song)

    def test_remove_cash(self):
        self.assertEqual(60, self.guest.remove_cash(40))
    
    def test_favourite_song_on_playlist(self):
        room = Room("Room 1", 40, 4)
        room.songs = ["Eye of the tiger"]
        self.assertEqual("Whoo!", self.guest.favourite_song_on_playlist(room.songs))




