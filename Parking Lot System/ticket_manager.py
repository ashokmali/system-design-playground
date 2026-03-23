from datetime import datetime
from vehicle import Vehicle
from parking_spot import ParkingSpot
from ticket import Ticket
from abc import ABC, abstractmethod

class FareCalculator(ABC):

    @abstractmethod
    def total_fare(self, ticket: Ticket):
        pass

class UniformFareCalculator(FareCalculator):

    def __init__(self):
        self.BASE_RATE = 1

    def total_fare(self, ticket: Ticket):
        time_diff = (ticket.exit_time[0] - ticket.entry_time[0]) / 60
        fee = time_diff * self.BASE_RATE

        multiplier = ticket.vehicle_details.get_multiplier()

        return fee*multiplier


class WeekendFareCalculator(FareCalculator):

    def __init__(self, discount: int):
        self.discount = discount

    def total_fare(self, ticket):
        base_fee = UniformFareCalculator().total_fare(ticket)
        multiply = 1 - (self.discount / 100)
        return base_fee * multiply


class SurgeFareCalculator(FareCalculator):

    def __init__(self, surge: int):
        self.surge = surge

    def total_fare(self, ticket):
        base_fee = UniformFareCalculator().total_fare(ticket)
        multiply = 1 + (self.surge / 100)
        return base_fee * multiply

class TicketManager:

    def __init__(self, strategy: FareCalculator):
        self.unique_id = 0
        self.logbook = {}
        self.strategy = strategy

    def set_strategy(self, strategy: FareCalculator):
        self.strategy = strategy

    def get_ticket(self, vehicle_details: Vehicle, spot_details: ParkingSpot):
        self.unique_id += 1
        entry_time = self._get_current_time()
        parking_ticket = Ticket(self.unique_id, vehicle_details, spot_details, entry_time)
        self.logbook[self.unique_id] = parking_ticket
        return parking_ticket

    def calculate_fee(self, ticket: Ticket):
        ticket.exit_time = self._get_current_time()
        ticket.fee = self.strategy.total_fare(ticket)
        return ticket.fee

    def _get_current_time(self):
        now = datetime.now()
        timestamp = now.timestamp()
        return [timestamp, now.day, now.month, now.year, now.hour, now.minute, now.second]









