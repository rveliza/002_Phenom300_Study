import streamlit as st

hightlight = ":orange-background"
cols_settings = [20, 80]



st.title("Fuel System")
st.write("## Lights and Switches")


st.write("#### Fuel Control Panel")


col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/switches_fuel_pump.png", use_column_width=True)
with col2:
    with st.expander("Fuel Pump Selector Switch"):
        st.write(f"""
**Emergency Bus**  
- **ON:** {hightlight}[**Activates the fuel pump**]
- **AUTO:** {hightlight}[**Automatically operates the fuel pump according to the system's logic**]
- **PFF** {hightlight}[**Deactivates the fuel pump**]
""")



col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/knobs_xfeed.png", use_column_width=True)
with col2:
    with st.expander("Crossfeed Valve Knob (XFEED)"):
        st.write(f"""
- **LO1:** {hightlight}[**Open the crossfeed valve and turns on electrical pump 2 (inside right tank).  Both engines are fed by the right tank**]
- **OFF:** {hightlight}[**Colse the crossfeed valve**]
- **LO2** {hightlight}[**Open the crossfeed valve and turns on electrical pump 1 (inside left tank).  Both engines are fed by the right tank**]
""")

st.write("## Question Bank")

with st.expander("Where is the temperature probe?"):
     st.write(f"""
- {hightlight}[**Right wing only**] 
""")
     

with st.expander("When must the Fuel XFEED be set to OFF?"):
     st.write(f"""
- {hightlight}[**Takeoff and Landing**] 
""")
     

with st.expander("Maximum fuel imbalance?"):
     st.write(f"""
- {hightlight}[**220 lbs**] 
""")
     

with st.expander("When are elecrric fuel pumps used?"):
     st.write(f"""
- {hightlight}[**Engine start**] 
- {hightlight}[**Ejector pump failure**] 
- {hightlight}[**Crossfeed operations**] 
""")
     

with st.expander("Purpose of scavenge pumps?"):
     st.write(f"""
- {hightlight}[**Maintain the level in the collector tank**] 
""")
     

with st.expander("Where is fuel stored?"):
     st.write(f"""
- {hightlight}[**Two integral wing tanks**] 
""")
     

with st.expander("How many pumps are found in each tank?"):
     st.write(f"""
**Three**  
- {hightlight}[**Ejector pump**] 
- {hightlight}[**Scavenge ejector pump**] 
- {hightlight}[**Electric fuel boost pump**] 
""")
     

with st.expander("What is normally used to supply fuel from the wing to the engie fuel control unit in flight?"):
     st.write(f"""
- {hightlight}[**Ejector pumps**] 
""")
     

with st.expander("How is the primary fuel ejector pump powered?"):
     st.write(f"""
- {hightlight}[**Motive flow from the respective engine.**] 
""")
     

with st.expander("What ensures that the differential pressure between the tank and ambient remains within structural limits and prevents fuel spillage?"):
     st.write(f"""
- {hightlight}[**A vent system including a NACA air inlet/outlet**] 
""")
     

with st.expander("How is crossfeed performed?"):
     st.write(f"""
- {hightlight}[**Select XFEED switch to the wing tank with the low fuel quantity**] 
- {hightlight}[**This opens the XFEED valve and turns opposite electric DC pump**] 
- {hightlight}[**Both engines will utilize fuel from that tank**] 
""")
     

with st.expander("Will the total tank quantity indication be lost if only one wing tank quantitiy indicator fails?"):
     st.write(f"""
- {hightlight}[**Yes**] 
""")
     

with st.expander("What is the only way to close a fuel shutoff valve?"):
     st.write(f"""
- {hightlight}[**By pusshing the fire shutoff pushbotton**] 
""")
     

with st.expander("What would cause a FUEL LO LEVEL CAS message?"):
     st.write(f"""
- {hightlight}[**310 lbs of fuel remaining in the respective tank**] 
""")
     

with st.expander("What would cause a FUEL IMBALANCE CAS message?"):
     st.write(f"""
- {hightlight}[**220 lbs imbalance**] 
""")
     

with st.expander("Is there de-fueling capability?"):
     st.write(f"""
- {hightlight}[**Yes, by means of a dump valve located under each wing**] 
""")
     

with st.expander("While refueling, what monitors the fuel quantity in the tanks and controls refueling flow into each tank?"):
     st.write(f"""
- {hightlight}[**EFCU - Electronif Fuel Control Unit**] 
""")
     

with st.expander("How long is maximum refueling time from empty to full?"):
     st.write(f"""
- {hightlight}[**Less than 12 minutes, at 50 psig**] 
""")
     

with st.expander("Explain the two critical test that should be accomplished before re-fueling?"):
     st.write(f"""
- {hightlight}[**LAMP TEST**] 
    - {hightlight}[**LH TANK and RH TANK indicator lights stay on**] 
    - {hightlight}[**FAIL indicator turns on**] 
    - {hightlight}[**Digits light up**] 
- {hightlight}[**Shut-Off Test**] 
    - {hightlight}[**LH TANK and RH TANK indicators come on**] 
    - {hightlight}[**Shut-off valves close**] 
    - {hightlight}[**FAIL indicator light must be off**] 
""")
     
with st.expander("In case of a fuel imbalance, when will the Fuel Imbalance CAS message estinguish?"):
     st.write(f"""
- {hightlight}[**88 lbs**] 
- {hightlight}[**44 lbs => Fuel Equal**] 
""")
     