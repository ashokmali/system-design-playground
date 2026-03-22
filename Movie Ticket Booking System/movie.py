class Movie:

    def __init__(self, title: str, genre: str, duration: int):
        self.title = title
        self.genre = genre
        self.duration = duration  # in minutes

    def get_duration(self):
        return (self.duration // 30) + 1

