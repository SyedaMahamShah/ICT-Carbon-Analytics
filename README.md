# ICT-Carbon-Analytics

Lifecycle Carbon Modeling Toolkit for ICT Infrastructure

Author: Maham Noor  
MSc, Aalto University (2025)

---

## Project Overview

ICT-Carbon-Analytics is a Python-based lifecycle carbon modeling toolkit
that quantifies greenhouse gas emissions (CO₂e) across the full lifecycle
of ICT equipment.

The model is derived from a comprehensive lifecycle assessment (LCA)
framework developed in my Master's thesis:

"Comprehensive Life Cycle Evaluation of Carbon Emission from ICT Equipment"

The project operationalizes lifecycle research into an executable
carbon analytics engine.

---

## Lifecycle Scope

The model evaluates:

- Raw material extraction
- Manufacturing & component fabrication
- Operational energy consumption
- End-of-life management

Lifecycle emissions are expressed in kg CO₂e.

---

## Devices Modeled

- Smartphones
- Laptops
- Data center servers

The model allows comparison across:

- Production vs Use phase dominance
- Country-specific electricity grid factors
- Fleet-scale infrastructure deployment

---

## Key Features

- Device-level lifecycle breakdown
- Production vs Use phase analysis
- Finland vs France electricity mix comparison
- Fleet-level emissions calculator
- Scenario modeling capability

---

## Electricity Grid Factors

| Country  | Grid Intensity (kg CO₂e/kWh) |
|-----------|-----------------------------|
| Finland  | 0.10 |
| France   | 0.05 |

The model demonstrates how low-carbon grids shift lifecycle dominance
toward embodied emissions.

---

## Example Usage

Run fleet emissions calculator:

