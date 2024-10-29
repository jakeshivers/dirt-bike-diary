import json
from datetime import datetime
from models.DirtBike import DirtBike
from models.DirtBikeMaintenanceApp import DirtBikeMaintenanceApp
import pprint


# Example usage
if __name__ == "__main__":

    is_active = True
    action = input("Do you want to add a bike? (y/n): ")
    if action == "y":
        try:
            with open("bikes.json", "r") as file:
                bikes_data = json.load(file)
        except FileNotFoundError:
            bikes_data = []

        bike_name = input("Enter bike name: ")
        insurance_date = input("Enter insurance date (YYYY-MM-DD): ")
        registration_date = input("Enter registration date (YYYY-MM-DD): ")

        new_bike = {
            "name": bike_name,
            "insurance_date": insurance_date,
            "registration_date": registration_date,
        }
        bikes_data.append(new_bike)

        with open("bikes.json", "w") as file:
            json.dump(bikes_data, file, indent=4)
        bike1 = DirtBike(bike_name, insurance_date, registration_date)
        # bike1.log_ride("mountain", "2 hours", "Rocky Mountain", "sunny")
        app = DirtBikeMaintenanceApp()
        app.add_bike(bike1)
        app.save_to_file("bikes.json")

    print("Bike added successfully!")
    print("Bike details: ")
    with open("bikes.json", "r") as file:
        bikes_data = json.load(file)
        for bike in bikes_data:
            print(f"Bike Name: {bike['name']}")
            print(f"Insurance Date: {bike['insurance_date']}")
            print(f"Registration Date: {bike['registration_date']}")
            print("\n")

    action = input("Do you want to add your bike preferences? (y/n): ")
    if action == "y":
        bike_name = input("Enter bike name: ")
        bike1 = DirtBike(bike_name)
        bike1.add_preference(bike_name)

    action = input("Do you want to log a ride? (y/n): ")
    if action == "y":
        bike_name = input("Enter bike name: ")
        terrain = input("Enter terrain: ")
        duration = input("Enter duration: ")
        location = input("Enter location: ")
        weather = input("Enter weather: ")
        event_date = input("Enter event date (YYYY-MM-DD): ")
        bike1 = DirtBike(bike_name)
        bike1.log_ride(terrain, duration, location, weather, event_date)
        print("Ride logged successfully!")
        print("Ride details: ")
        print(f"Terrain: {terrain}")
        print(f"Duration: {duration}")
        print(f"Location: {location}")
        print(f"Weather: {weather}")
        print(f"Event Date: {event_date}")
        print("\n")
