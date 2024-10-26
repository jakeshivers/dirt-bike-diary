from datetime import datetime
from uuid import uuid4


class DirtBike:
    def __init__(self, name, insurance_date, registration_date):
        self.id = str(uuid4())
        self.name = name
        self.insurance_date = insurance_date
        self.registration_date = registration_date
        self.preferred_tires = []
        self.preferred_grips = []
        self.preferred_chains = []
        self.preferred_chemicals = []
        self.ride_logs = []

    def add_preference(self, category, item):
        if category == "tires":
            self.preferred_tires.append(item)
        elif category == "grips":
            self.preferred_grips.append(item)
        elif category == "chains":
            self.preferred_chains.append(item)
        elif category == "chemicals":
            self.preferred_chemicals.append(item)

    def log_ride(self, terrain, duration, location, weather):
        ride = {
            "terrain": terrain,
            "duration": duration,
            "location": location,
            "weather": weather,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
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
