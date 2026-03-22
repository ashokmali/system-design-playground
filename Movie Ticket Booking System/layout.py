from seat import Seat

class Layout:

    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.seats_by_number = {}
        self.seats_by_position = {}
        self._initialize_layout()

    def _initialize_layout(self):
        for row in range(self.rows):
            for col in range(self.cols):
                seat_no = str(row) + "-" + str(col)
                self.add_seat(seat_no, row, col, Seat(seat_no, None))


    def add_seat(self, seat_no: str, row: int, col: int, seat: Seat):
        self.seats_by_number[seat_no] = seat
        if row not in self.seats_by_position:
            self.seats_by_position[row] = {}
        self.seats_by_position[row][col] = seat

    def get_seat_by_number(self, seat_no: str):
        if seat_no in self.seats_by_number:
            return self.seats_by_number[seat_no]
        return None

    def get_seat_by_position(self, row: int, col: int):
        if row in self.seats_by_position:
            if col in self.seats_by_position[row]:
                return self.seats_by_position[row][col]
        return None

    def get_all_seats(self):
        seats = []
        for key in self.seats_by_number:
            seats.append(self.seats_by_number[key])
        return seats