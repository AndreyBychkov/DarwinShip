

class Creature:

    # global attributes
    @property
    def size(self):
        return 1.0
    
    @property
    def strength(self):
        return 1.0
    
    @property
    def dexterity(self):
        return 1.0
    
    @property
    def vigilance(self):
        return 1.0

    @property
    def max_health(self):
        return 1.0

    @property
    def max_hunger(self):
        return 1.0

    @property
    def max_age(self):
        return 1.0

    @property
    def max_energy(self):
        return 1.0
    
    # local attributes
    @property
    def health(self):
        return 1.0
    
    @property
    def hunger(self):
        return 1.0

    @property
    def age(self):
        return 1.0

    @property
    def energy(self):
        return 1.0

    # behavior
    def act(self):
        pass

