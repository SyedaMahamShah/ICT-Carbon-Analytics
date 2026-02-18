import pandas as pd

# Device baseline values derived from thesis findings
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

def lifecycle_emissions(device_type, country, lifetime_override=None):
    device = DEVICE_DATA[device_type].copy()
    grid_factor = ELECTRICITY_FACTORS[country]

    # If user wants to override lifetime
    if lifetime_override is not None:
        device["lifetime_years"] = lifetime_override

    use_phase = (
        device["annual_use_kwh"] *
        grid_factor *
        device["lifetime_years"]
    )

    total = (
        device["production"] +
        use_phase +
        device["eol"]
    )

    return {
        "Production": device["production"],
        "Use Phase": use_phase,
        "End of Life": device["eol"],
        "Total": total
    }

def data_center_operational_emissions(it_energy_kwh, pue, country):
    """
    Calculate operational emissions of a data center
    including infrastructure overhead using PUE.
    """

    total_energy = it_energy_kwh * pue
    grid_factor = ELECTRICITY_FACTORS[country]

    emissions = total_energy * grid_factor

    return {
        "IT Energy (kWh)": it_energy_kwh,
        "Total Facility Energy (kWh)": total_energy,
        "Operational Emissions (kg CO2e)": emissions
    }

def get_device_data():
    data = {
        "device": ["smartphone", "laptop", "server"],
        "production_kg": [70, 250, 2000],
        "annual_use_kwh": [5, 50, 3000],
        "lifetime_years": [3, 4, 4],
        "eol_kg": [5, 15, 100]
    }
    return pd.DataFrame(data)

def calculate_lifecycle(device, country):
    df = get_device_data()
    row = df[df["device"] == device].iloc[0]

    electricity_factors = {
        "finland": 0.10,
        "france": 0.05
    }

    use_phase = (
        row["annual_use_kwh"] *
        electricity_factors[country] *
        row["lifetime_years"]
    )

    total = row["production_kg"] + use_phase + row["eol_kg"]

    return {
        "Production": row["production_kg"],
        "Use Phase": use_phase,
        "End of Life": row["eol_kg"],
        "Total": total
    }

def lifetime_sensitivity(device, country, min_year=2, max_year=8):
    results = []
    for year in range(min_year, max_year + 1):
        result = calculate_lifecycle(device, country)
        result["Lifetime"] = year
        results.append(result)

    return pd.DataFrame(results)