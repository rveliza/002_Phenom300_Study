import streamlit as st

hightlight = ":orange-background"
cols_settings = [20, 80]



st.title("Air Management System")
st.write("## Lights and Switches")

######################## AC Panel
st.write("#### Air Conditioning Panel")

col1, col2 = st.columns(cols_settings)

with col1:
    st.image("images/knobs_ecs.png", use_column_width=False)

with col2:
    with st.expander("Environmental Control System Knob"):
        st.write(f"""
- OFF VENT:   
i.  {hightlight}[turns off al ACS lines (FCSOVs / ECSs) => PRSOVs]            
ii. {hightlight}[opens the RAV to emergency ventilation]                
- 1: activates the left-hand line (ACS 1) -> FCSOV # 1
- BOTH: activates both lines (ACS 1 and ACS 2)
- 2: activates the right-hand line (ACS 2) -> FCSOV # 2
""")
        

        

col1, col2 = st.columns(cols_settings)

with col1:
    st.image("images/switches_ac_switch.png", use_column_width=False)

with col2:
    with st.expander("Air conditioning Temperature Mode Switch"):
        st.write(f"""
- MAN: Manual operation of temperature contol system
- AUTO: Automatic operation of temperature control system
- OFF: 
    - {hightlight}[Turns off the VCS (compressor/condenser and and evaporators)]
    - Automatic mode is kept operative in this position
    - {hightlight}[Independet zonal temperature control is not operative]
""")
        
col1, col2 = st.columns(cols_settings)

with col1:
    st.image("images/switches_ac_temp_man.png", use_column_width=False)
with col2:
    with st.expander("Air Conditioning Temperature Manual Switch"):
            st.write(f"""
    - H: Up, increase cockpit and cabin duct temperature
    - C: Down, decrease cockpit and cabin duct temperature  
                    
    {hightlight}[**NOTE: Manual regulation of the temperature is possible only with the AIR CONDITIONING MODE switch set to MAN position**]
    """)
        

###################### Pressurization Panel
st.write("#### Pressurization and Pneumatic Control Panel")

col1, col2 = st.columns(cols_settings)

with col1:
        st.image("images/buttons_dump.png", use_column_width=False)

with col2:
    with st.expander("Dump Button"):    
        st.write(f"""
- Opens the OFV {hightlight}[**Rapid cabin depressurization**]
- Commands OFF the recirculation fans
- White strip bar illuminates.
""")
        
        st.write("""
        |Parameter|Limit Tolerance| Rate|
        |:---:|:---:|:---:|
        |Auto| 12,000 ft Cabin Altitude| Aprox 500 fpm|
        |Manual| 14,500 ft Cabin Altitude| Aprox 2,000 fpm|
        """)


col1, col2 = st.columns(cols_settings)

with col1:
    st.image("images/switches_cabin_alt.png", use_column_width=False)

with col2:
    with st.expander("Cabin Altitude Selector Switch"):
            st.write(f"""
    - UP: Manually opens the outflow valve, increasing cabin altitude  
    - DN: Manually closes the outrflow valve, decreasing cabin altitude   
                    
    -{hightlight}[**Note: Manual actuation of the OFV is possible only with the PRESN MODE switch set to MAN position**]
""")
            
col1, col2 = st.columns(cols_settings)

with col1:
    st.image("images/panels_pneumatics.png", use_column_width=True)

with col2:
    with st.expander("Bleed Switches (PRSOV's)"):
        st.write(f"""
- AUTO: enables the respective (1 or 2) bleed system                
    - Automatically closes in single engine takoff conditions  
- OFF: closes the respective(1 or 2) bleed system  
                 
-{hightlight}[**PRSOVs have a shutoff capability for the bleed air lines**]
""")
        

col1, col2 = st.columns(cols_settings)

with col1:
    st.image("images/panels_pneumatics.png", use_column_width=True)

with col2:
    with st.expander("Cross Bleed Knob"):
        st.write(f"""
- OFF: closes the bleed valve manually
- AUTO: enables the cross bleed valve  
""")
        

################# Question Bank
st.write("## Question Bank")
with st.expander("To what systems does the interconnected pneumatic system provide temperature and controlled air?"):
     st.write(f"""
- {hightlight}[**Air Conditioning**](cabin heating)
- {hightlight}[**Cabin pressurization**]
- {hightlight}[**Wing/Stab Anti-Ice**]
""")
     
with st.expander("How is RAM air used in the aircraft?"):
     st.write(f"""
- Ram air is used to {hightlight}[**decrease bleed air temperature in the heat exchanger**]
- {hightlight}[**Supply fresh air to the cockpit/cabin**] is specific cases
""")
     
with st.expander("What input is required from the flight crew prior to departure for the pressurization system to operate automatically?"):
     st.write(f"""
- {hightlight}[**LFE**]
""")
     
with st.expander("How is bleed system controlled?"):
     st.write(f"""
- {hightlight}[**By two bleed PRSOV's located in each pylon**]
""")
     

with st.expander("Does a PRSOV automatically close in case of a single engine takoff condition?"):
     st.write(f"""
- {hightlight}[**Yes**]
""")
     
with st.expander("How can the pilot override the RH PRSOV to the closed position?"):
     st.write(f"""
- {hightlight}[**By placing the pneumatic bleed toggle switch to the OFF position**]
""")


with st.expander("What does turning the ECS knob to OFF VENT do?"):
     st.write(f"""
- {hightlight}[**Opens RAV**] providing fress air to cabin and cocpit
- {hightlight}[**Closes both FCSOV’ (ECS’s), and closes both PRSOVs (bleeds)**] 
""")

with st.expander("What two modes control cockpit and cabin temperature?"):
     st.write(f"""
- {hightlight}[**Auto**] 
- {hightlight}[**Manual**] 
""")

with st.expander("How is temperature of the air conditioning system to the cabin controll?"):
     st.write(f"""
- {hightlight}[**Temperature Modulating Valves (TMV's)**] mix cooled air from the heat exchanger with hot bleed air based on temperature selection on the cockpit control panel
""")
     
with st.expander("What is the function of the Vapor Cycle System (VCS)?"):
     st.write(f"""
- {hightlight}[**Provides cooling air for the cabin and cockpit operated manually by the ECS controller**] 
""")

with st.expander("When can the VCS be operated on the ground?"):
     st.write(f"""
- {hightlight}[**With GPU power**] or, 
- {hightlight}[**One engine operating**] 
""")

with st.expander("What is used to cool the heat exchanger?"):
     st.write(f"""
- {hightlight}[**Ground cooling fan on ground**] or, 
- {hightlight}[**Ram air in flight**] 
""")

with st.expander("What is the purpose of the DUMP button?"):
     st.write(f"""
- {hightlight}[**Provides cabin depressurization**] by opening the OFV 
- {hightlight}[**Turns off the recirculation fans**] 
""")

with st.expander("What is used for cooling inside the cockpit and cabin?"):
     st.write(f"""
- {hightlight}[**Condition bleed air**] 
- {hightlight}[**Vapor Cycle System**] 
""")

with st.expander("Describe the configuration of the A/C system on the ground, above 30 $\degree$C with both engines running and temperature set to max cool:"):
     st.write(f"""
- {hightlight}[**Both PRSOV's close**] 
- {hightlight}[**VCS is turned by the ECS controller**] 
""")

with st.expander("Identify the component that is responsible for automatic pressurization control:"):
     st.write(f"""
- {hightlight}[**ECMU**] Electronic Control and Monitoring Unit
""")

with st.expander("List the two ECMU channles"):
     st.write(f"""
- {hightlight}[**Automatic**] 
- {hightlight}[**Manual**] 
""")

with st.expander("Describe HI FIELD annunciation"):
     st.write(f"""
- {hightlight}[**CPCS considers a takeoff or landing field above 9,600 ft as high field operation**] 
    - Cabin altitude warning is reset to {hightlight}[**14,200 ft**] 
- {hightlight}[**When aircraft above 25,000 ft, ECMU resets to original configuration**] 
    - {hightlight}[**EICAS HI FIELD disappears**] 
    - Cabin altitude warning returns to {hightlight}[**10,000 ft**] 
""")

with st.expander("What will occur if an AMS CTRL FAIL CAS message appears?"):
     st.write(f"""
- {hightlight}[**No bleed temperature and pressure control is performed**] 
""")

with st.expander("In the normal mode of operation, at what cabin altitude will the CAB ALTITUDE HIGH alarm activate?"):
     st.write(f"""
- {hightlight}[**10,000 ft**] if airport elevation < 8,300 ft MSL
- {hightlight}[**11,500 ft**] 8,300 ft < airport elevation < 9,600 ft
- {hightlight}[**14,200 ft**] airport elevation > 9,600 ft
""")

