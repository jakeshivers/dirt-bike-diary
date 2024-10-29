from models.DirtBike import DirtBike
import json


class DirtBikeMaintenanceApp:
    def __init__(self):
        self.bikes = []

    def add_bike(self, bike):
        self.bikes.append(bike)

    def save_to_file(self, filename):
        # Load existing bikes from file
        try:
            with open(filename, "r") as file:
                existing_bikes_data = json.load(file)
                existing_bikes = [
                    DirtBike(
                        bike["name"], bike["insurance_date"], bike["registration_date"]
                    )
                    for bike in existing_bikes_data
                ]
        except (FileNotFoundError, json.JSONDecodeError):
            existing_bikes = []

        # Combine existing bikes with current app bikes
        all_bikes = existing_bikes + self.bikes

    def load_from_file(self, filename):
        with open(filename, "r") as file:
            bikes_data = json.load(file)
            self.bikes = [DirtBike(**bike) for bike in bikes_data]
