from abc import ABC, abstractmethod
from enum import Enum


class VehicleSize(Enum):
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"


class Vehicle(ABC):

    def __init__(self, license_plate: str, size: VehicleSize):
        self.license_plate = license_plate
        self.size = size

    @abstractmethod
    def get_size(self):
        pass

    def get_multiplier(self):
        pass


class Motorcycle(Vehicle):

    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleSize.SMALL)

    def get_size(self):
        return self.size

    def get_multiplier(self):
        return 1.0


class Car(Vehicle):

    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleSize.MEDIUM)

    def get_size(self):
        return self.size

    def get_multiplier(self):
        return 1.2


class Truck(Vehicle):

    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleSize.LARGE)

    def get_size(self):
        return self.size

    def get_multiplier(self):
        return 1.5