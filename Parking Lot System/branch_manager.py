from ticket_manager import TicketManager, UniformFareCalculator
from parking_manager import ParkingManager
from vehicle import Vehicle
from ticket import Ticket

class BranchManager:

    def __init__(self):
        self.LAYOUT = {"small":30, "medium":20, "large":10}
        self.tickets = TicketManager(UniformFareCalculator())
        self.lots = ParkingManager(self.LAYOUT)

    def entry(self, vehicle: Vehicle):
        spot = self.lots.get_spot(vehicle)
        if spot:
            customer_ticket = self.tickets.get_ticket(vehicle, spot)
            return customer_ticket
        else:
            print("No spot found")

    def exit(self, customer_ticket: Ticket):
        self.lots.free_spot(customer_ticket.spot_details)
        fee_generated = self.tickets.calculate_fee(customer_ticket)
        return fee_generated


if __name__ == "__main__":
    manager = BranchManager()


