class TransportSystem:
    def __init__(self, banana_weights, vehicle_limit):
        self.banana_weights = banana_weights
        self.vehicle_limit = vehicle_limit

    def calculate_min_vehicles(self):
        self.banana_weights.sort()
        start, end, vehicles_count = 0, len(self.banana_weights) - 1, 0

        while start <= end:
            if self.banana_weights[start] + self.banana_weights[end] <= self.vehicle_limit:
                start += 1
            end -= 1
            vehicles_count += 1

        return vehicles_count

# Input
weights_list = list(map(int, input().split()))
max_weight_limit = int(input())

# Process and Output
transport_system = TransportSystem(weights_list, max_weight_limit)
result = transport_system.calculate_min_vehicles()
print(result)
