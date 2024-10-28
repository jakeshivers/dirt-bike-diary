from models.DirtBike import DirtBike
import json


class DirtBikeMaintenanceApp:
    def __init__(self):
        self.bikes = []

    def add_bike(self, bike):
        self.bikes.append(bike)

    def save_to_file(self, filename):
        with open(filename, "a") as file:
            json.dump([bike.to_dict() for bike in self.bikes], file, indent=4)

    def load_from_file(self, filename):
        with open(filename, "r") as file:
            bikes_data = json.load(file)
            self.bikes = [DirtBike(**bike) for bike in bikes_data]
