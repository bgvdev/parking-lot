from vehicle import Vehicle

class Bike(Vehicle):
    
    def __init__(self, vehicle_number, parking_fee_strategy=None):
        super().__init__(Vehicle.TYPE_BIKE, vehicle_number, parking_fee_strategy)