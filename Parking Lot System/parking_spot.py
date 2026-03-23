from abc import ABC, abstractmethod
from enum import Enum

class SpotSize(Enum):
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"

class ParkingSpot(ABC):

    def __init__(self, spot_id:int, size: SpotSize):
        self.spot_id = spot_id
        self.size = size
        self.is_available = False

    @abstractmethod
    def get_size(self):
        pass

    def is_available(self):
        return self.is_available


class CompactSpot(ParkingSpot):

    def __init__(self, spot_id: int):
        super().__init__(spot_id, SpotSize.SMALL)

    def get_size(self):
        return self.size


class RegularSpot(ParkingSpot):

    def __init__(self, spot_id: int):
        super().__init__(spot_id, SpotSize.MEDIUM)

    def get_size(self):
        return self.size


class OversizedSpot(ParkingSpot):

    def __init__(self, spot_id: int):
        super().__init__(spot_id, SpotSize.LARGE)

    def get_size(self):
        return self.size
