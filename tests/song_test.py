import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Eye of the tiger")

    def test_can_get_song_name(self):
        self.assertEqual("Eye of the tiger", self.song.name)