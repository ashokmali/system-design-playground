from screening_manager import ScreeningManager
from movie import Movie
from cinema import Cinema
from screening import Screening
from seat import Seat
from ticket import Ticket

class MovieBookingSystem:

    def __init__(self):
        self.movies = []
        self.cinemas = []
        self.screening_manager = ScreeningManager()

    def add_movie(self, movie: Movie):
        self.movies.append(movie)

    def add_cinema(self, cinema: Cinema):
        self.cinemas.append(cinema)

    def add_screening(self, movie: Movie, screening: Screening):
        self.screening_manager.add_screening(movie, screening)

    def book_ticket(self, screening: Screening, seat: Seat):
        price = seat.pricing.get_price()
        ticket = Ticket(seat, screening, price)
        self.screening_manager.add_ticket(ticket, screening)

    def get_screenings_for_movie(self, movie: Movie):
        return self.screening_manager.get_screenings_for_movie(movie)

    def get_available_seats(self, screening: Screening):
        return self.screening_manager.get_available_seats(screening)

    def get_ticket_count(self, screening: Screening):
        return len(self.screening_manager.get_tickets_for_screening(screening))

    def get_ticket_for_screening(self, screening: Screening):
        return self.screening_manager.get_tickets_for_screening(screening)


