from typing import List
from models.Creature import Creature


class Environment:

    # static properties
    @property
    def climate(self):
        return None

    # dynamic properties
    @property
    def temperature(self):
        return 1.0

    @property
    def wind_velocity(self):
        return 1.0

    @property
    def lighting(self):
        return 1.0

    @property
    def humidity(self):
        return 1.0

    @property
    def creatures(self) -> List[Creature]:
        return list()

    def tick(self):
        for creature in self.creatures:
            creature.act()




