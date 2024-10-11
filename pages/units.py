import streamlit as st

st.title("Units Conversion")
cols_config = 2

conversions = [
    {"conv1": "Degree Celsius (c)", "conv2": "Degree Fahrenheit (F)", "multiplier1": 1.8, "adder1": 32, "multiplier2": .5556,"adder2": -17.7778},
    {"conv1": "Feet (ft)", "conv2": "Meter (m)", "multiplier1": .3048, "adder1": 0, "multiplier2": 3.2808,"adder2": 0},
    {"conv1": "Inches (in)", "conv2": "Millimeter (mm)", "multiplier1": 25.4, "adder1": 0, "multiplier2": .0394,"adder2": 0},
    {"conv1": "Inches of Mercury (in.Hg)", "conv2": "Millibar (mbar)", "multiplier1": 33.8636, "adder1": 0, "multiplier2": .0295,"adder2": 0},
    {"conv1": "Kilogram (kg)", "conv2": "Pounds (lb)", "multiplier1": 2.2046, "adder1": 0, "multiplier2": .4536,"adder2": 0},
    {"conv1": "Kilogram per Square Meter (kg/m2)", "conv2": "Pound per Square Inch (psi)", "multiplier1": .0014, "adder1": 0, "multiplier2": 703.0740,"adder2": 0},
    {"conv1": "Kilometer (km)", "conv2": "Nautical Mile (NM)", "multiplier1": .5399, "adder1": 0, "multiplier2": 1.8520,"adder2": 0},
    {"conv1": "Kilometer per Hour (km/h)", "conv2": "Knot (kt)", "multiplier1": .5399, "adder1": 0, "multiplier2": 1.8520,"adder2": 0},
    {"conv1": "US Gallon", "conv2": "Imperial Gallon", "multiplier1": .8327, "adder1": 0, "multiplier2": 1.2009,"adder2": 0},
    {"conv1": "US Gallon", "conv2": "Liters", "multiplier1": 3.7854, "adder1": 0, "multiplier2": .2641,"adder2": 0},
    {"conv1": "Imperial Gallon", "conv2": "Liters", "multiplier1": 4.5461, "adder1": 0, "multiplier2": .2199,"adder2": 0},
]

col1, col2= st.columns(cols_config)

def convert(dict):
    # First Conversion
    with col1:
        input = st.number_input(f"{dict["conv1"]} to {dict["conv2"]}")
        formula = (input * dict["multiplier1"]) + dict["adder1"]
        st.write(f"{dict["conv2"]}: {formula:.2f}")
        st.divider()

    # # Second Conversion
    with col2:
        input = st.number_input(f"{dict["conv2"]} to {dict["conv1"]}")
        formula = (input * dict["multiplier2"]) + dict["adder2"]
        st.write(f"{dict["conv1"]}: {formula:.2f}")
        st.divider()

for c in conversions:
    convert(c)