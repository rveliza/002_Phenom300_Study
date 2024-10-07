import streamlit as st

st.title("Units Conversion")
cols_config = 2

col1, col2= st.columns(cols_config)

# Ceslius to Farenheit
with col1:
    celsius = st.number_input(f"Celsius to Fahrenheit")
    farenheit = (celsius * 1.8) + 32
    st.write(f"Fahrenheit: {farenheit:.1f}")
    st.divider()

# Farenheit to Celsius
with col2:
    farenheit = st.number_input("Farenheit to Celsius")
    celsius = (farenheit * .5556) -17.7778
    st.write(f"Celsius: {celsius:.1f}")
    st.divider()

col1, col2= st.columns(cols_config)
# # Feet (ft) to Meter (mt)
with col1:
    feet = st.number_input("Feet (ft) to Meter (mt)")
    meter = feet * .3048
    st.write(f"Meter (mt): {meter:.1f}")
    st.divider()

# # Meter (mt) to Feet (ft)
with col2:
    meter = st.number_input("Meter (mt) to Feet(ft)")
    feet = meter * 3.2808
    st.write(f"Feet (ft): {feet:.2f}")
    st.divider()


col1, col2= st.columns(cols_config)
with col1:
    inches = st.number_input("Inches (in)")
    millim = inches * 25.4
    st.write(f"Millimeter (mm): {millim}")