class Guest:
    
    def __init__(self, input_guest_name, input_guest_cash, input_favourite_song):
        self.name = input_guest_name
        self.cash = input_guest_cash
        self.fav_song = input_favourite_song

    def get_customer_name(self):
        return self.name

    def get_customer_cash(self):
        return self.cash

    def get_customer_fav_song(self):
        return self.fav_song

    def remove_cash(self, amount):
        self.cash -= (amount)
        return self.cash
