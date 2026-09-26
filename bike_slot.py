from slot import Slot
from vehicle import Vehicle

class BikeSlot(Slot):
    
    def __init__(self, id):
        super().__init__(id, Slot.SLOT_TYPE_FOR_BIKE)

    def can_park(self, vehicle):
        return vehicle.get_type() == Vehicle.TYPE_BIKE