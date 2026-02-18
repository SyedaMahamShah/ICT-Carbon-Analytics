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
