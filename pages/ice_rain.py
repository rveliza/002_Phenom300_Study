import streamlit as st

hightlight = ":orange-background"
cols_settings = [20, 80]



st.title("Ice and Rain")
st.write("## Lights and Switches")


st.write("#### Ice and Rain Protection Control Panel")


col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/switches_windshield.png", width='stretch')
with col2:
    with st.expander("Windshield Heating Switch"):
        st.write(f"""
- **ON:** {hightlight}[**Activates the associated windshiel heating system**]
- **OFF:** {hightlight}[**Deactivates the associated windshield heating system**]
""")

col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/knobs_ads.png", width='stretch')
with col2:
    with st.expander("Air Data System/Angle of Attack Heating Knob"):
        st.write(f"""
- **OFF:** {hightlight}[**Deactivates the ADS heating system**]
- **AUTO:** {hightlight}[**Allows automatic operation of the ADS heating system**]
     - Automatic when at least one engine is running or,
     - The aircraft is not on the wheels
- **ON:** {hightlight}[**Activates the ADS heating system**]
""")

col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/switches_wingstab.png", width='stretch')
with col2:
    with st.expander("Wing/Stabilizer Ice Protection Switch"):
        st.write(f"""
- **ON:** {hightlight}[**Activates the wing and the horizontal stabilizer anti-ice systems**]
     - Stall warning activation angles are anticipated (Higher stall warning speeds)
     - SWPS ICE SPEED CAS message is displayed
- **OFF:** {hightlight}[**Deactivates the wing and the horizontal stabilizer anti-ice systems**]
- **ICE SPEED RESET:** {hightlight}[**Resets the SWPS to non-icing schedule and removes the SWPS ICE SPEED message**]
""")

col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/switches_engine_ice.png", width='stretch')
with col2:
    with st.expander("Engine Ice Protection Switch"):
        st.write(f"""
- **ON:** {hightlight}[**Activates the associated engine anti-ice system**]
     - Engine TTO probe is also heated electrically.
- **OFF:** {hightlight}[**Deactivates the associated engine anti-ice system**]
     - Energizes the EAIV to the CLOSE position. If electrical power is lost, the EAIV defaults to the OPEN position.
""")

        
st.write("## Question Bank")

with st.expander("Whith an engine failure in icing conditions, which anti-ice systems will be lost or significanlty degraded?"):
     st.write(f"""
- {hightlight}[**Engine AI of failed engine**] Lost
- {hightlight}[**Wing/Stab Anti-ice**] Degraded to 15,000 ft
- {hightlight}[**Windshield Heat**] Degraded to 1 matt
""")
     

with st.expander("What is the relationship of the FADEC to the Wing/Stab Anti-Ice?"):
     st.write(f"""
- {hightlight}[**FADEC will always calculate the power needed to satisfy the system**] 
- {hightlight}[**FADEC will limit the idle position to a power setting necessary to satisfy the system if the Langing Gear is up**] 
""")
     

with st.expander("Describe the AUTO mode for ADS heating system"):
     st.write(f"""
- {hightlight}[**Normal operation mode**] 
- {hightlight}[**Probes will be automatically energized if:**] 
    - {hightlight}[**at least one engine is running**] or,
    - {hightlight}[**the aircraft is not on the wheels**] 
""")
     

with st.expander("Wing and Horizontal Stabilizer icing protection is provided by?"):
     st.write(f"""
- {hightlight}[**A thermal anti-ice system using temperature and pressure controlled bleed air from the aircraft pneumatic system**] 
""")
     

with st.expander("Which subsystems do the ice and rain protection include?"):
     st.write(f"""
- {hightlight}[**Wings**] 
- {hightlight}[**Horizontal Stabilizer**] 
- {hightlight}[**Engine air intakes**] 
- {hightlight}[**Pitot and Static**] 
- {hightlight}[**Windshields**] 
     - Heating and Rain Repellent
""")
     

with st.expander("With the loss of electrical power, what is the default position of the engine A/I valves?"):
     st.write(f"""
- {hightlight}[**OPEN, providing continuous bleed air to the engine inlet**] 
""")
     

with st.expander("What does a 'A-I 1/2' CAS message indicate?"):
     st.write(f"""
- {hightlight}[**Loss of anti-ice protection to that engine**] 
""")
     

with st.expander("What does 'A-I WINGSTAB INHB' CAS message indicate?"):
     st.write(f"""
- {hightlight}[**WHSAIS switched ON outside the icing envelope**] or, 
- {hightlight}[**Aircraft is in single bleed configuration > 15,000 ft**] 
""")
     

with st.expander("At what altitude is the WHSAIS operation limited to in a single-bleed source scenario?"):
     st.write(f"""
- {hightlight}[**15,000 ft**] 
""")
     

with st.expander("What occurs when the Wingstab switch is placed to the ON position?"):
     st.write(f"""
- {hightlight}[**Activates the wing and horizontal stab anti-ice system**] 
- {hightlight}[**FADEC calculates and maintains a minimum N1**] 
- {hightlight}[**Stall warning and protection speeds are increased**] 
- {hightlight}[**SWPS ICE SPEED CAS is displayed**] 
""")
     

with st.expander("What else is heated when the Engine Switch 1 or 2 is activated?"):
     st.write(f"""
- {hightlight}[**TTO probe**] 
""")
     

