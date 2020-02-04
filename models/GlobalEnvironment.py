from typing import List
from models.Environment import Environment


class GlobalEnvironment:
    # Singleton
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(GlobalEnvironment, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.environments = self.__create_environments()

    def tick(self):
        for env in self.environments:
            env.tick()

    def __create_environments(self) -> List[Environment]:
        return list()