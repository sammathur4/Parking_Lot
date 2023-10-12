from parking_lot import *


def main():
    parking_lot = ParkingLot()

    while True:
        print("\nOptions:")
        print("1. Assign a parking space")
        print("2. Retrieve parking spot")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            vehicle_number = input("Enter the vehicle number: ")
            result = parking_lot.assign_parking_spot(vehicle_number)
            print(result)
        elif choice == "2":
            vehicle_number = input("Enter the vehicle number: ")
            result = parking_lot.retrieve_parking_spot(vehicle_number)
            print(result)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
