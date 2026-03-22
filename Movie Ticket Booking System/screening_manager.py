from movie import Movie
from screening import Screening
from ticket import Ticket

class ScreeningManager:

    def __init__(self):
        self.screenings_by_movie = {}
        self.tickets_by_screening = {}

    def add_screening(self, movie: Movie, screening: Screening):
        if movie not in self.screenings_by_movie:
            self.screenings_by_movie[movie] = []
        self.screenings_by_movie[movie].append(screening)

    def get_screenings_for_movie(self, movie: Movie):
        if movie not in self.screenings_by_movie:
            return []
        return self.screenings_by_movie[movie]

    def add_ticket(self, ticket: Ticket, screening: Screening):
        if screening not in self.tickets_by_screening:
            self.tickets_by_screening[screening] = []
        self.tickets_by_screening[screening].append(ticket)

    def get_tickets_for_screening(self, screening: Screening):
        if screening not in self.tickets_by_screening:
            return []
        return self.tickets_by_screening[screening]

    def get_available_seats(self, screening: Screening):
        all_seats = screening.room.layout.get_all_seats()
        booked_tickets = self.get_tickets_for_screening(screening)
        for ticket in booked_tickets:
            all_seats.remove(ticket.seat)
        return all_seats