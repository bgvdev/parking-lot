from abc import ABC, abstractmethod

class Slot(ABC):
    SLOT_TYPE_FOR_CAR = "LARGE"
    SLOT_TYPE_FOR_BIKE = "SMALL"

    def __init__(self, type, id):
        self.__id = id
        self.__type = type
        self.__is_occupied = False
        self.__vehicle = None

    @abstractmethod
    def can_park(self, vehicle):
        pass
    
    def park_vehicle(self, vehicle):
        if self.__is_occupied:
            raise Exception("Slot is already occupied.")
        if not self.can_park(vehicle):
            raise Exception(f"Vehicle type {vehicle.get_type()} cannot be parked in this slot type {self.__type}.")
        self.__vehicle = vehicle
        self.__is_occupied = True
    
    def vacate_slot(self):
        if not self.__is_occupied:
            raise Exception("Slot is already vacant.")
        self.__vehicle = None
        self.__is_occupied = False

    def get_slot_id(self):
        return self.__id

    def get_slot_type(self):
        return self.__type

    def is_occupied(self):
        return self.__is_occupied
    