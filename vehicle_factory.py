from car import Car
from bike import Bike
from vehicle import Vehicle

class VehicleFactory:

    @staticmethod
    def create_vehicle(vehicle_type, *args, **kwargs):
        if vehicle_type == Vehicle.TYPE_CAR:
            return Car(*args, **kwargs)
        elif vehicle_type == Vehicle.TYPE_BIKE:
            return Bike(*args, **kwargs)
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")