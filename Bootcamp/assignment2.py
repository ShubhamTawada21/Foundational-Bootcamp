class Vehicle:
    total_vehicles = 0
    def __init__(self, brand):
        self.brand = brand
        Vehicle.total_vehicles += 1
    def fuel_cost_per_km(self):
        pass
    def show_details(self):
        print(f"Vehicle: {self.brand}")
        print(f"Fuel cost per km: ₹{self.fuel_cost_per_km()}")
        print()
class Car(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)
    def fuel_cost_per_km(self):
        return 6
class Truck(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)
    def fuel_cost_per_km(self):
        return 12
class Motorcycle(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)
    def fuel_cost_per_km(self):
        return 2
vehicles = [
    Car("Toyota"),
    Truck("Volvo"),
    Motorcycle("Honda")
]
for vehicle in vehicles:
    vehicle.show_details()
print("Total vehicles:", Vehicle.total_vehicles)