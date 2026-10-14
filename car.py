from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, vehicle_number, parking_fee_strategy=None):
        super().__init__(Vehicle.TYPE_CAR, vehicle_number, parking_fee_strategy)