from logger import logger
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self) -> None:
        pass


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        pass

    @abstractmethod
    def create_motocycle(self, make: str, model: str) -> Vehicle:
        pass


class Car(Vehicle):
    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: Мотор заведено")


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        make_us_marked = f"{make} (US Spec)"
        return Car(make_us_marked, model)

    def create_motocycle(self, make: str, model: str) -> Vehicle:
        make_us_marked = f"{make} (US Spec)"
        return Motorcycle(make_us_marked, model)


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        make_eu_marked = f"{make} (EU Spec)"
        return Car(make_eu_marked, model)

    def create_motocycle(self, make: str, model: str) -> Vehicle:
        make_eu_marked = f"{make} (EU Spec)"
        return Motorcycle(make_eu_marked, model)


# Використання
def main() -> None:
    eu_vehicle_factory: VehicleFactory = EUVehicleFactory()
    vehicle1: Vehicle = eu_vehicle_factory.create_car("Skoda", "Octavia")
    vehicle1.start_engine()

    us_vehicle_factory: VehicleFactory = USVehicleFactory()
    vehicle2: Vehicle = us_vehicle_factory.create_motocycle(
        "Harley-Davidson", "Sportster"
    )
    vehicle2.start_engine()


if __name__ == "__main__":
    main()
