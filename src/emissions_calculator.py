from lifecycle_model import lifecycle_emissions

def fleet_emissions(device, quantity, country):
    single = lifecycle_emissions(device, country)
    return {k: v * quantity for k, v in single.items()}

if __name__ == "__main__":
    device = input("Device type: ")
    quantity = int(input("Quantity: "))
    country = input("Country (finland/france): ")

    result = fleet_emissions(device, quantity, country)

    print("\nTotal Lifecycle Emissions:")
    for k, v in result.items():
        print(f"{k}: {v:.2f} kg CO2e")
