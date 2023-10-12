import re


class ParkingLot:
    def __init__(self, num_levels=2, spots_per_level=20):
        self.num_levels = num_levels
        self.spots_per_level = spots_per_level
        self.available_spots = {level: list(range(1, spots_per_level + 1)) for level in range(1, num_levels + 1)}
        self.occupied_spots = {}

    def assign_parking_spot(self, vehicle_number):
        if vehicle_number == "" or vehicle_number is None or not re.match(r'^[A-Za-z0-9]*$', vehicle_number):
            return {"message": "Invalid vehicle number"}

        if vehicle_number in self.occupied_spots:
            return {"level": self.occupied_spots[vehicle_number]["level"], "spot": self.occupied_spots[vehicle_number]["spot"]}

        for level in range(1, self.num_levels + 1):
            if self.available_spots[level]:
                spot = self.available_spots[level].pop(0)
                self.occupied_spots[vehicle_number] = {"level": level, "spot": spot}
                return {"level": level, "spot": spot}

        return {"message": "Parking lot is full"}

    def retrieve_parking_spot(self, vehicle_number):
        if vehicle_number in self.occupied_spots:
            spot_info = self.occupied_spots.pop(vehicle_number)
            self.available_spots[spot_info["level"]].append(spot_info["spot"])
            return {"level": spot_info["level"], "spot": spot_info["spot"]}
        return {"message": "Vehicle not found"}



