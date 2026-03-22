from movie import Movie
from room import Room
from datetime import datetime

class Screening:

    def __init__(self, movie: Movie, room: Room, start_time: datetime, end_time: datetime):
        self.movie = movie
        self.room = room
        self.start_time = start_time
        self.end_time = end_time

    def get_duration(self):
        return (((self.end_time - self.start_time).total_seconds()//60)//30) + 1