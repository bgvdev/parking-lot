from vehicle import Vehicle
from parking_fee_strategy import ParkingFeeStrategy

class RegularParkingFeeStrategy(ParkingFeeStrategy):
    def calculate_fee(self, vehicleType, duration):
        match vehicleType:
            case Vehicle.TYPE_CAR:
                return 20 * duration
            case Vehicle.TYPE_BIKE:
                return 10 * duration
            case _:
                raise ValueError("Invalid vehicle type")