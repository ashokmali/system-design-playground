import heapq
from parking_spot import ParkingSpot, CompactSpot, RegularSpot, OversizedSpot
from vehicle import Vehicle

class ParkingManager:

    def __init__(self, layout: dict[str, int]):
        self.lot = {}
        self.layout = layout
        self._fill_lot(self.layout)

    def _fill_lot(self, diagram: dict[str, int]):
        for size in diagram:
            self.lot[size] = []
            for i in range(1, diagram[size]+1):
                spot = self._create_spot(size, i)
                heapq.heappush(self.lot[size], (i, spot))


    def _create_spot(self, size, spot_id: int):

        if size.lower() == "small":
            return CompactSpot(spot_id)
        elif size.lower() == "medium":
            return RegularSpot(spot_id)
        elif size.lower() == "large":
            return OversizedSpot(spot_id)

    def get_spot(self, vehicle: Vehicle):
        size = vehicle.get_size().lower()
        try:
            spot = heapq.heappop(self.lot[size])
            return spot
        except:
            return None

    def free_spot(self, spot: ParkingSpot):
        size = spot.get_size().lower()
        heapq.heappush(self.lot[size], (spot.spot_id, spot))

