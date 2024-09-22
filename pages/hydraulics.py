import streamlit as st

hightlight = ":orange-background"
cols_settings = [20, 80]



st.title("Hydraulic System")
st.write("## Lights and Switches")


st.write("#### Hydraulic System Panel")


col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/panels_hydraulics.png", use_column_width=True)
with col2:
    with st.expander("Hydraulic Pump SOV Switch"):
        st.write(f"""
- **OPEN:** {hightlight}[**Command the Fire Shutoff Valve (FSOV) to open**]
- **CLOSED:** {hightlight}[**Command the Fire Shutoff Valve (FSOV) to close**]
""")

        
st.write("## Question Bank")

with st.expander("Where is the Hydraulic Valve FCSOV located?"):
     st.write(f"""
- {hightlight}[**In each wing root**] 
""")
     

with st.expander("HYD HI TEMP CAS indicates?"):
     st.write(f"""
- {hightlight}[**Hydraulic fluid has overheated**] 
""")
     

with st.expander("Purpose of priority valve?"):
     st.write(f"""
- {hightlight}[**Give systems using hydraulic power priority over the landing gear if they are used simultaneously**] 
""")
     

with st.expander("If one engine-driven hydraulic pump fails?"):
     st.write(f"""
- {hightlight}[**The remaining pump is cabaple of actuating all subsystems**] 
""")
     

with st.expander("What systems require hydraulic pressure?"):
     st.write(f"""
- {hightlight}[**Landing Gear**] 
- {hightlight}[**Main Brakes**] 
- {hightlight}[**Emergency Brakes**] 
- {hightlight}[**Pusher**] 
- {hightlight}[**Rudder Boost**] 
- {hightlight}[**Spoilers**] 
""")
     

with st.expander("In case of hydraulic pump malfunction, what prevents rotation without interfering with the continued operation of the engine?"):
     st.write(f"""
- {hightlight}[**The hydraulic pump connectint shaft to the AGB has a recess designed to work as a shaft shear point if the torque imposed by the hydraulic pump to the AGB exceeds limits**] 
""")
     

with st.expander("What encases the hydraulic fluid?"):
     st.write(f"""
- {hightlight}[**A spring loaded reservoir**] 
- {hightlight}[**50 psi reservoir pressure**] 
- {hightlight}[**3,000 psi system pressure**] 
""")
     

with st.expander("How much can it hold?"):
     st.write(f"""
- {hightlight}[**1.3 gals**] 
""")
     

with st.expander("What provides contamination protection for the system?"):
     st.write(f"""
- {hightlight}[**Two filter elements located on the lower portion of the high pressure line.  The filter can capture any particle greater than 5 micros**] 
""")
     

with st.expander("What would happen if the filter fails or is blocked by too much contamination?"):
     st.write(f"""
- {hightlight}[**A bypass valve will open**] 
""")
     

with st.expander("What is available to indicate that the filters need to be replaced?"):
     st.write(f"""
- {hightlight}[**Red 'pop-up' indicators**] 
""")
     

with st.expander("How are the Fire Shutoff Valves Closed?"):
     st.write(f"""
- {hightlight}[**Manually**] 
    - {hightlight}[**By the engine shutoff buttons**] 
    - {hightlight}[**By shutoff switches in hydraulic panel**] 
- {hightlight}[**Automatically**] 
    - {hightlight}[**High temperature**] 
""")
     

with st.expander("What does a HYD HI TEMP CAS message indicate?"):
     st.write(f"""
- {hightlight}[**Hydraulic fluid temp has risen > 235 $\\degree$F**] 
- {hightlight}[**Both FSOV automatically close**] 
""")
     

with st.expander("What does a HYD LO PRES CAS message indicate?"):
     st.write(f"""
- {hightlight}[**The system is not capable of providing flow at rated pressure**] 
""")
     

with st.expander("What does a HYD SOV 1/2 FAIL CAS message indicate?"):
     st.write(f"""
- {hightlight}[**A FSOV was commanded to close and didn't**] 
- {hightlight}[**A FSOV position does not agree with its switch position**] 
""")
     

with st.expander("Describe how to check the hydraulic fluid quantity?"):
     st.write(f"""
- {hightlight}[**Shutdown engines**] 
- {hightlight}[**Dump parking brake accumulator with wheels chocked**] 
""")
     

with st.expander("What effect an engine failure will have on the hydraulic system?"):
     st.write(f"""
- {hightlight}[**None, the remaining pump can support the entire system**] 
""")
     
