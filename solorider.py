class Customer:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y


class Vehicle:
    def __init__(self, number, x, y):
        self.number = number
        self.x = x
        self.y = y


class TransportSystem:
    def __init__(self, passengers, vehicles):
        self.passengers = passengers
        self.vehicles = vehicles

    def calculate_min_distance(self):
        self.passengers.sort(key=lambda x: x.name)
        self.vehicles.sort(key=lambda x: x.number)

        total_distance = 0
        for passenger in self.passengers:
            min_distance = float('inf')
            min_vehicle = None

            for vehicle in self.vehicles:
                distance = abs(passenger.x - vehicle.x) + abs(passenger.y - vehicle.y)

                if distance < min_distance or (distance == min_distance and vehicle.number < min_vehicle.number):
                    min_distance = distance
                    min_vehicle = vehicle

            total_distance += min_distance
            self.vehicles.remove(min_vehicle)


