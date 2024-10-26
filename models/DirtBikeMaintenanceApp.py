from models.DirtBike import DirtBike
import json


class DirtBikeMaintenanceApp:
    def __init__(self):
        self.bikes = []

    def add_bike(self, bike):
        self.bikes.append(bike)

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            json.dump([bike.to_dict() for bike in self.bikes], file, indent=4)

    def write_json(self, filename):
        with open(filename, "r+") as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data inside emp_details
            file_data["filename"].append([bike.to_dict() for bike in self.bikes])
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent=4)

    def load_from_file(self, filename):
        with open(filename, "r") as file:
            bikes_data = json.load(file)
            self.bikes = [DirtBike(**bike) for bike in bikes_data]
