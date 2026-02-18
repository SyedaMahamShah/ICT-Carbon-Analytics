import pandas as pd

DEVICE_DATA = {
    "smartphone": {
        "production": 70,
        "annual_use_kwh": 5,
        "lifetime_years": 3,
        "eol": 5
    },
    "laptop": {
        "production": 250,
        "annual_use_kwh": 50,
        "lifetime_years": 4,
        "eol": 15
    },
    "server": {
        "production": 2000,
        "annual_use_kwh": 3000,
        "lifetime_years": 4,
        "eol": 100
    }
}

ELECTRICITY_FACTORS = {
    "finland": 0.10,
    "france": 0.05
}

def lifecycle_emissions(device, country, lifetime_override=None):

    device_data = DEVICE_DATA[device].copy()
    grid = ELECTRICITY_FACTORS[country]

    if lifetime_override is not None:
        device_data["lifetime_years"] = lifetime_override

    use_phase = (
        device_data["annual_use_kwh"] *
        grid *
        device_data["lifetime_years"]
    )

    total = (
        device_data["production"] +
        use_phase +
        device_data["eol"]
    )

    return {
        "Production": device_data["production"],
        "Use Phase": use_phase,
        "End of Life": device_data["eol"],
        "Total": total
    }

def data_center_operational_emissions(it_energy_kwh, pue, country):

    total_energy = it_energy_kwh * pue
    grid = ELECTRICITY_FACTORS[country]

    emissions = total_energy * grid

    return {
        "IT Energy (kWh)": it_energy_kwh,
        "Total Facility Energy (kWh)": total_energy,
        "Operational Emissions (kg CO2e)": emissions
    }

def lifetime_sensitivity(device, country, min_year=2, max_year=8):

    results = []

    for year in range(min_year, max_year + 1):
        result = lifecycle_emissions(device, country, lifetime_override=year)
        result["Lifetime"] = year
        results.append(result)

    return pd.DataFrame(results)


if __name__ == "__main__":
    print(lifecycle_emissions("laptop", "finland"))
