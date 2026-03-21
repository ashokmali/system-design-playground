from vehicle import Vehicle
from parking_spot import ParkingSpot
from typing import List

class Ticket:

    def __init__(self, ticket_id: int, vehicle_details: Vehicle, spot_details: ParkingSpot, entry_time: List[int], exit_time: List[int] = None, fee: float = 0):
        self.ticket_id = ticket_id
        self.vehicle_details = vehicle_details
        self.spot_details = spot_details
        self.entry_time = entry_time
        self.exit_time = exit_time
        self.fee = fee


