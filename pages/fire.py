import streamlit as st

hightlight = ":orange-background"
cols_settings = [20, 80]



st.title("Fire Protection")
st.write("## Lights and Switches")


st.write("#### Engine Fire Protection Control Panel")


col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/buttons_eng.png", use_column_width=True)
with col2:
    with st.expander("Shutoff 1 and Shutoff 2 Buttons (Guarded)"):
        st.write(f"""
- **PUSHED IN:** 
    - {hightlight}[**Closes fuel valve**]
    - {hightlight}[**Closes the PRSOV valve**]
    - {hightlight}[**Closes the Hydraulic valve**]
    - {hightlight}[**Enables the fire extinguisher**]
    - {hightlight}[**Illuminates the white strip**]
- **PUSHED OUT:** {hightlight}[**Disables the fire extinguisher bottle discharge**]
""")

col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/switches_fire_ext.png", use_column_width=True)
with col2:
    with st.expander("Bottle Switch"):
        st.write(f"""
- **DISCH:** {hightlight}[**Discharges the fire extinguisher agent into the enabled engine**]
- **OFF:** {hightlight}[**The discharge circuitry is off**]
""")


        
st.write("## Question Bank")

with st.expander("Succesful baggage smoke test consists of?"):
     st.write(f"""
- {hightlight}[**BAG SMK CAS messages**] 
- {hightlight}[**Aural "Fire, Fire"**] 
""")
     

with st.expander("What happens when Engine Fire Shutoff Button is pressed?"):
     st.write(f"""
- {hightlight}[**The fuel shutoff valve closes**] 
- {hightlight}[**The PRSOV closes**] 
- {hightlight}[**The hydraulic shutoff valve closes**] 
- {hightlight}[**The fire bottle is armed**] 
- {hightlight}[**White strip illuminates**] 
""")
     

with st.expander("How many engine fire bottles are installed in the aircraft and what is the location of each?"):
     st.write(f"""
- {hightlight}[**One bottle**] 
- {hightlight}[**Aft fuselage**] 
""")
     

with st.expander("Fire detection system test indicatios?"):
     st.write(f"""
- {hightlight}[**Aural "FIRE, FIRE"**] 
- {hightlight}[**CAS ENG 1/2 FIRE**] 
- {hightlight}[**FIRE in ITT field**] 
- {hightlight}[**Red light illuminates in shutoff pushbutton**] 
""")
     

