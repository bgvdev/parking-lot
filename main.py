from car import Car
from bike import Bike
from parking_lot import ParkingLot
from car_slot import CarSlot
from bike_slot import BikeSlot
from vehicle_factory import VehicleFactory
from payment import Payment
from vehicle import Vehicle
from regular_parking_fee_strategy import RegularParkingFeeStrategy
from premium_parking_fee_strategy import PremiumParkingFeeStrategy
from card_payment import CardPayment
from upi_payment import UPIPayment

@staticmethod
def get_payment_strategy(strategy_type):
    match strategy_type:
        case Payment.PAYMENT_STRATEGY_CASH:
            return UPIPayment()
        case Payment.PAYMENT_STRATEGY_CARD:
            return CardPayment()
        case _:
            raise ValueError(f"Unknown payment strategy type: {strategy_type}")

def main():

    parkingSlots = []
    parkingSlots.append(CarSlot(1))
    parkingSlots.append(CarSlot(2))
    parkingSlots.append(CarSlot(3))
    parkingSlots.append(BikeSlot(4))
    parkingSlots.append(BikeSlot(5))
    parkingSlots.append(BikeSlot(6))
    parkingSlots.append(BikeSlot(7))

    parkingLot = ParkingLot(parkingSlots)

    vehicleFactory = VehicleFactory()
    car1 = vehicleFactory.create_vehicle(Vehicle.TYPE_CAR, "CAR001", RegularParkingFeeStrategy())
    car2 = vehicleFactory.create_vehicle(Vehicle.TYPE_CAR, "CAR002", PremiumParkingFeeStrategy())
    car3 = vehicleFactory.create_vehicle(Vehicle.TYPE_CAR, "CAR003", PremiumParkingFeeStrategy())
    bike1 = vehicleFactory.create_vehicle(Vehicle.TYPE_BIKE, "BIKE001", RegularParkingFeeStrategy())
    bike2 = vehicleFactory.create_vehicle(Vehicle.TYPE_BIKE, "BIKE002", PremiumParkingFeeStrategy())
    bike3 = vehicleFactory.create_vehicle(Vehicle.TYPE_BIKE, "BIKE003", RegularParkingFeeStrategy())
    bike4 = vehicleFactory.create_vehicle(Vehicle.TYPE_BIKE, "BIKE004", PremiumParkingFeeStrategy())

    car1Slot = parkingLot.park_vehicle(car1)
    car2Slot = parkingLot.park_vehicle(car2)
    car3Slot = parkingLot.park_vehicle(car3)
    bike1Slot = parkingLot.park_vehicle(bike1)
    bike2Slot = parkingLot.park_vehicle(bike2)
    bike3Slot = parkingLot.park_vehicle(bike3)
    bike4Slot = parkingLot.park_vehicle(bike4)

    print("select payment method...")
    print("1. Cash")
    print("2. Card")
    choice = int(input("Enter your choice: "))

    if (car1Slot is not None):
        car1Fee = car1.calculate_parking_fee(2)
        paymentStrategy = get_payment_strategy(choice)
        paymentStrategy.process_payment(car1Fee)
        parkingLot.vacate_slot(car1Slot)
    
    if (bike2Slot is not None):
        bike2Fee = bike2.calculate_parking_fee(2)
        paymentStrategy = get_payment_strategy(choice)
        paymentStrategy.process_payment(bike2Fee)
        parkingLot.vacate_slot(bike2Slot)

if __name__ == "__main__":
    main()