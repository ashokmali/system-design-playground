from abc import ABC, abstractmethod

class PricingStrategy(ABC):

    @abstractmethod
    def get_price(self):
        pass


class NormalRate(PricingStrategy):

    def __init__(self, price: float):
        self.price = price

    def get_price(self):
        return self.price



class PremiumRate(PricingStrategy):

    def __init__(self, price: float):
        self.price = price

    def get_price(self):
        return self.price


class VIPRate(PricingStrategy):

    def __init__(self, price: float):
        self.price = price

    def get_price(self):
        return self.price


class Seat:

    def __init__(self, seat_no: str, pricing: PricingStrategy = None):
        self.seat_no = seat_no
        self.pricing = pricing