from parking_fee_strategy import ParkingFeeStrategy

class Vehicle:
    TYPE_CAR = "Car"
    TYPE_BIKE = "Bike"
    TYPE_SCOOTER = "Scooter"

    parking_fee_strategy: ParkingFeeStrategy

    def __init__(self, type, vehicle_number=None, parking_fee_strategy=None):
        self.__type = type
        self.__vehicle_number = vehicle_number
        self.__parking_fee = parking_fee_strategy

    def calculate_parking_fee(self, duration):
        if self.__parking_fee is None:
            raise ValueError("Parking fee strategy not set for the vehicle.")
        return self.__parking_fee.calculate_fee(self.__type, duration)

    def get_type(self):
        return self.__type

    def get_vehicle_number(self):
        return self.__vehicle_number