from vehicle import Vehicle
from slot import Slot 

class ParkingLot:
    
    __slots:list[Slot] = []

    def __init__(self, slots:list[Slot]):
        self.__slots = slots

    def find_available_slot(self, vehicle:Vehicle) -> Slot:
        for slot in self.__slots:
            if not slot.is_occupied() and slot.can_park(vehicle):
                return slot
        return None

    def park_vehicle(self, vehicle:Vehicle):
        slot = self.find_available_slot(vehicle)
        if slot is None:
            raise Exception("No available slot for this vehicle.")
        slot.park_vehicle(vehicle)
        print(f"Vehicle {vehicle.get_vehicle_number()} parked in slot {slot.get_slot_id()} successfully.")
        return slot.get_slot_id()

    def vacate_slot(self, slot_id):
        for slot in self.__slots:
            if slot.get_slot_id() == slot_id:
                slot.vacate_slot()
                print(f"Slot {slot_id} vacated successfully.")
                return
        raise Exception("Slot ID not found.")

    def get_slot_by_id(self, slot_id):
        for slot in self.__slots:
            if slot.get_slot_id() == slot_id:
                return slot
        raise Exception("Slot ID not found.")

    def get_slots(self):
        return self.__slots