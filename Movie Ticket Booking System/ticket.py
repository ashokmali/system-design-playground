from screening import Screening
from seat import Seat

class Ticket:

    def __init__(self, seat: Seat, screening: Screening, price: float):
        self.seat = seat
        self.screening = screening
        self.price = price