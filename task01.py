from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass


class VehicleFactory(ABC):

    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motocycle(self, make, model):
        pass


class USVehicleFactory(VehicleFactory):

    def create_car(self, make, model):
        make_us_marked = f"{make} (US Spec)"
        return Car(make_us_marked, model)

    def create_motocycle(self, make, model):
        make_us_marked = f"{make} (US Spec)"
        return Motorcycle(make_us_marked, model)


class EUVehicleFactory(VehicleFactory):

    def create_car(self, make, model):
        make_eu_marked = f"{make} (EU Spec)"
        return Car(make_eu_marked, model)

    def create_motocycle(self, make, model):
        make_eu_marked = f"{make} (EU Spec)"
        return Motorcycle(make_eu_marked, model)


class Car(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"{self.make} {self.model}: Мотор заведено")


# Використання
eu_vehicle_factory = EUVehicleFactory()
vehicle1 = eu_vehicle_factory.create_car("Skoda", "Octavia")
vehicle1.start_engine()

us_vehicle_factory = USVehicleFactory()
vehicle2 = us_vehicle_factory.create_motocycle("Harley-Davidson", "Sportster")
vehicle2.start_engine()
