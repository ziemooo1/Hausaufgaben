import os

class Trains:
    def __init__(self):
        self._connections = dict()
        self._cities = []

    def setup(self, filename):
        with open(filename) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split()
                source = parts[0]
                dest = parts[2]
                if source not in self._connections:
                    self._connections[source] = []
                self._connections[source].append(dest)
                
                if source not in self._cities:
                    self._cities.append(source)
                if dest not in self._cities:
                    self._cities.append(dest)

    def run(self):
        print("Available cities are: ", ", ".join(self._cities))

        current = input("Where do you want to start: ")
        while current not in self._connections:
            print("No departures from that city. Try again.")
            current = input("Where do you want to start: ")

        while True:
            destinations = self._connections[current]
            print(f"From {current} you can go to:")
            for city in destinations:
                print(f" {city}")

            next_city = input("Where do you want to go next: ")
            if next_city == "":
                break
            if next_city not in destinations:
                print("No direct connection. Try again.")
                continue
            current = next_city


trains = Trains()
trains.setup(os.path.join(os.path.dirname(__file__), "connections.txt"))
trains.run()
