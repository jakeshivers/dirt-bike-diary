import json
from datetime import datetime
from models.DirtBike import DirtBike
from models.DirtBikeMaintenanceApp import DirtBikeMaintenanceApp


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
        bike1.add_preference("tires", "Michelin Starcross 5")
        bike1.log_ride("mountain", "2 hours", "Rocky Mountain", "sunny")
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

    # while is_active:
    #     app = DirtBikeMaintenanceApp()
    #     bike1 = DirtBike( " Yamaha YZ250F", "2023-12-01", "2023-11-01")
    #     bike1.add_preference("tires", "Michelin Starcross 5")
    #     bike1.log_ride("mountain", "2 hours", "Rocky Mountain", "sunny")
    #     app.add_bike(bike1)
    #     app.save_to_file("bikes.json")
