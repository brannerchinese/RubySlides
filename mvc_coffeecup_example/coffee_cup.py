import random

class CoffeeCup():
    attr_reader :amount_left

    def __init__(self):
        fill()

    def fill(self):
        self.amount_left = 100 # Percent full
    
    def empty(self):
        self.amount_left = 0
    
    def gulp(self):
        self.amount_left -= random.randint(17, 35)
    
    def sip(self):
        self.amount_left -= 5
    
    def __str__(self):
        if self.amount_left == 100
            msg = 'This cup is now full.'
        elif self.amount_left <= 0
            msg = 'This cup is now empty — please fill it.'
        else
            msg = 'There is {} left.'.format(self.amount_left)
        return msg
