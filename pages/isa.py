import streamlit as st

st.title("International Standard Atmosphere")

altitude = st.number_input("Altitude/Elevation")
temp = st.number_input("OAT")

isa = 15 - (altitude/1000 * 2)
if isa >= -56:
    st.write(f"ISA: {isa}")
    st.write(f"ISA deviation: {temp - isa}")
else:
    st.write(f"ISA: -56")
    st.write(f"ISA deviation: {temp - 56}")


