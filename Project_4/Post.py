import random
import enum
class Post(enum.Enum):
    Clerk="Clerk"
    ProbationaryOfficer ="Probationary Officer" 
    @classmethod
    def RANDOM(cls):
        return random.choice(list(cls.__members__.values()))