from uuid import uuid4
import json
import datetime as dt


class DirtBike:
    def __init__(self, name, insurance_date=None, registration_date=None):
        self.id = str(uuid4())
        self.name = name
        self.insurance_date = insurance_date
        self.registration_date = registration_date

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

    def log_ride(self, bike_name):
        with open("bikes.json", "r") as file:
            bikes_data = json.load(file)

        bike_found = False
        for bike in bikes_data:
            if bike["name"] == bike_name:
                bike_found = True
                event_date = input("Enter event date (YYYY-MM-DD): ")
                terrain = input("Enter terrain: ")
                duration = input("Enter duration: ")
                location = input("Enter location: ")
                weather = input("Enter weather: ")

                if "rides" not in bike:
                    bike["rides"] = []
                bike["rides"].append(
                    {
                        "event_date": event_date,
                        "terrain": terrain,
                        "duration": duration,
                        "location": location,
                        "weather": weather,
                    }
                )

                print("Ride logged successfully!")
                print("Ride details: ")
                print(f"Terrain: {terrain}")
                print(f"Duration: {duration}")
                print(f"Location: {location}")
                print(f"Weather: {weather}")
                print(f"Event Date: {event_date}")
                print("\n")

        if not bike_found:
            print(f"No bike found with the name {bike_name}")

        with open("bikes.json", "w") as file:
            json.dump(bikes_data, file, indent=4)


# testing some stuff
