from models.DirtBike import DirtBike
import json
import datetime as dt


class DirtBikeMaintenanceApp:
    def __init__(self):
        self.bikes = []

    def add_bike(self, bike):
        self.bikes.append(bike)

    def save_to_file(self, filename):
<<<<<<< HEAD
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
=======
           # Load existing bikes from file
        try:
            with open(filename, "r") as file:
                existing_bikes_data = json.load(file)
                existing_bikes = [DirtBike(bike['name'], bike['insurance_date'], bike['registration_date']) for bike in existing_bikes_data]
>>>>>>> 3f2ec5011767bb9c388f562bcbeb150e7f0efe13
        except (FileNotFoundError, json.JSONDecodeError):
            existing_bikes = []

        # Combine existing bikes with current app bikes
        all_bikes = existing_bikes + self.bikes
<<<<<<< HEAD
=======

        # Save all bikes back to file
        with open(filename, "w") as file:
            json.dump([bike.to_dict() for bike in all_bikes], file, indent=4)
>>>>>>> 3f2ec5011767bb9c388f562bcbeb150e7f0efe13

    def load_from_file(self, filename):
        with open(filename, "r") as file:
            bikes_data = json.load(file)
            self.bikes = [DirtBike(**bike) for bike in bikes_data]
