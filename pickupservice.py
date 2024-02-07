class Passenger:
    def __init__(self, name, goods, tax):
        self.name = name
        self.goods = goods
        self.tax = tax

class Vehicle:
    def __init__(self, name, goods, tax):
        self.name = name
        self.goods = goods
        self.tax = tax

class TravelPlan:
    def __init__(self, num_cities):
        self.city_graph = {i: [] for i in range(1, num_cities + 1)}
        self.visited = [False] * (num_cities + 1)
        self.route = []

    def add_connection(self, city1, city2, goods, tax):
        self.city_graph[city1].append(Passenger(city2, goods, tax))
        self.city_graph[city2].append(Vehicle(city1, goods, tax))

    def dfs(self, city, exempted_city):
        self.visited[city] = True
        self.route.append(city)

        neighbors = sorted(self.cit
