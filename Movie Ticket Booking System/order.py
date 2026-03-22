from datetime import datetime
from ticket import Ticket

class Order:

    def __init__(self, order_time: datetime):
        self.order_time = order_time
        self.tickets = []

    def add_tickets(self, ticket: Ticket):
        self.tickets.append(ticket)

    def calculate_total_price(self):
        total_price = 0
        for ticket in self.tickets:
            total_price += ticket.price
        return total_price