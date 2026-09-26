from abc import ABC, abstractmethod

class ParkingFeeStrategy(ABC):
    @abstractmethod
    def calculate_fee(self, vehicleType, duration):
        pass