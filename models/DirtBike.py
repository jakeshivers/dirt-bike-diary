from datetime import datetime
from uuid import uuid4
<<<<<<< HEAD
import json
=======
import datetime as dt
>>>>>>> 3f2ec5011767bb9c388f562bcbeb150e7f0efe13


class DirtBike:
    def __init__(self, name, insurance_date=None, registration_date=None):
        self.id = str(uuid4())
        self.name = name
        self.insurance_date = insurance_date
        self.registration_date = registration_date
        self.ride_logs = []

    def add_preference(self, bike_name):
        with open("bikes.json", "r") as file:
            bikes_data = json.load(file)

        for bike in bikes_data:
            if bike["name"] == bike_name:
                add_another = "y"
                while add_another == "y":
                    category = input("Enter category (tires/grips/chains/chemicals): ")
                    item = input("Enter item: ")

                    if "preferences" not in bike:
                        bike["preferences"] = {}
                    bike["preferences"][category] = item

                    print("Preferences added successfully!")
                    print("Bike details: ")
                    print(f"Bike Name: {bike['name']}")
                    print(f"Preferred {category}: {item}")
                    print("\n")

                    add_another = input(
                        "Do you want to add another preference? (y/n): "
                    )

        with open("bikes.json", "w") as file:
            json.dump(bikes_data, file, indent=4)

    def log_ride(self, terrain, duration, location, weather, event_date):
        ride = {
            "terrain": terrain,
            "duration": duration,
            "location": location,
            "weather": weather,
            "event_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        self.ride_logs.append(ride)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "insurance_date": self.insurance_date,
            "registration_date": self.registration_date,
            "preferred_tires": self.preferred_tires,
            "preferred_grips": self.preferred_grips,
            "preferred_chains": self.preferred_chains,
            "preferred_chemicals": self.preferred_chemicals,
            "ride_logs": self.ride_logs,
        }
