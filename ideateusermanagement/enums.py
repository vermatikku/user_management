from enum import Enum

class YesNo(Enum):
    Y = 'Yes'
    N = 'No'
    @classmethod
    def choices(cls):
        return tuple((i.name,i.value) for i in cls)