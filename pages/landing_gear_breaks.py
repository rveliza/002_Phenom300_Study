import streamlit as st

hightlight = ":orange-background"
cols_settings = [20, 80]



st.title("Landing Gear and Brakes")
st.write("## Lights and Switches")

######################## Gear Panel
st.write("#### Landing Gear Panel")

col1, col2 = st.columns(cols_settings)

with col1:
    st.image("images/landing_gear_lever.png", use_container_width=False)

with col2:
    with st.expander("Landing Gear Panel"):
        st.write(f"""
- DN LCK REL: {hightlight}[Mechanically releases the landing gear lever lock]            
- WARNING BUTTON: {hightlight}[Inhibits landing gear warining when the landing flap is not selected and the difference between aiplane altitude and LFE is less than 700 ft during descent]  
     - Warning will not be silenced if flaps selected to 3 or Full and the landing gear is not down and locked.              
""")


st.write("## Question Bank")

with st.expander("Following a hydraulic system failure, how many actuations of the emergency parking brake are available?"):
     st.write(f"""
- {hightlight}[**6**] 
""")
     

with st.expander("What holds the Landing Gear in the UP position?"):
     st.write(f"""
- {hightlight}[**One uplock for each landing gear**] 
""")
     

with st.expander("How does the touchdown protection function work to avoid blowout on landing?"):
     st.write(f"""
- {hightlight}[**It prevents any brake application prior to WOW and main wheel spin up**] 
""")
     

with st.expander("Explain the Emergency Extension process"):
     st.write(f"""
- {hightlight}[**Pull out the free handle that activates the free-fall selector valve and releases all residual hydraulic pressure from the langing gear lines to the return line**] 
- {hightlight}[**Mechanically releases the landing gear uplocks**] 
- {hightlight}[**Gravitational and aerodynamic forces extend the landing gear**] 
- {hightlight}[**The downlock mechanism then locks the gear in its fully extended position**] 
""")
     

with st.expander("When flap lever is set to either 0, 1, or 2 position, when would the landing gear aural warning sound?"):
     st.write(f"""
- {hightlight}[**Difference between pressure altitude and LFE is less that 700 ft**] and,
- {hightlight}[**Airspeed is below 160 kts**] and,
- {hightlight}[**Either thrust lever is set below 26 $\\degree$ with the other below 40 $\\degree$ for two engines**] or,
- {hightlight}[**Thrust lever of operative engine is set below 40 $\\degree$ for OEI**] 
""")
     

with st.expander("When would the landing gear aural warning sound if flaps fail?"):
     st.write(f"""
- {hightlight}[**When the difference between pressure altitude and LFE is less than 700 ft while descending**] 
""")
     

with st.expander("What is the primary input to the Air/Ground system?"):
     st.write(f"""
- {hightlight}[**WOW**] 
""")
     

with st.expander("Name some of the aircraft systems that utilize the WOW signals?"):
     st.write(f"""
- {hightlight}[**Brake control system**] 
- {hightlight}[**Landing gear control lever**] 
- {hightlight}[**Electrical system**] 
- {hightlight}[**FADEC**]  
- {hightlight}[**Air conditioning and pressurization**] 
- {hightlight}[**Flight controls (Flaps and spoilers)**] 
- {hightlight}[**Avionics**] 
""")
     

with st.expander("What is the maximum turning radius?"):
     st.write(f"""
- {hightlight}[**20 degrees steering**] 
- {hightlight}[**23 thru differential braking and thrust**] 
""")
     

with st.expander("What would a 'LG WOW SYS FAIL' CAS message indicate?"):
     st.write(f"""
- {hightlight}[**There is a disagreement between the signals from R and L WOW sensors for more than 3 seconds**] 
""")
     

with st.expander("What type of brake system does the P300 have?"):
     st.write(f"""
- {hightlight}[**Carbon Brakes**] 
- {hightlight}[**Brake by wire**] 
""")
     

with st.expander("Functions of the brake system?"):
     st.write(f"""
- {hightlight}[**Locked Wheel Protection**] Prevents the main landing gear tire from bursting
- {hightlight}[**Anti Skid Protection**] Prevents tire skidding and maximizes brake efficiency
- {hightlight}[**Touchdown Protection**] Prevents brake application prior to airplane on ground
- {hightlight}[**Gear Retract Braking**] Provides break pressure during gear retraction
- {hightlight}[**Initiated Built In Test**] 
""")
     

with st.expander("What happens if the wheel speed input fails?"):
     st.write(f"""
- {hightlight}[**Antiskid is not available**] 
""")
     

with st.expander("Is Anti-skid available for the emergency/parking brake?"):
     st.write(f"""
- {hightlight}[**No**] 
""")
     

with st.expander("When does the anti-skid protection drop out on deceleration?"):
     st.write(f"""
- {hightlight}[**Below 10 kts**] 
""")
     

with st.expander("How many WOW sensors are installed?"):
     st.write(f"""
- {hightlight}[**Four, two on each main gear**] 
""")
     

with st.expander("What controls and monitors the brake pressure?"):
     st.write(f"""
- {hightlight}[**BCU**] Brake control unit 
""")
     

with st.expander("Aside from pedal pressure inputs from the pilot, what other inputs does the BCU receive before calculating brake pressure?"):
     st.write(f"""
- {hightlight}[**Landing gear control lever**] 
- {hightlight}[**Wheel speed**] 
- {hightlight}[**Brake pressure**] 
- {hightlight}[**WOW**] 
""")


with st.expander("What is the brake cooling time?"):
     st.write(f"""
- {hightlight}[**20 minutes**] 
     - {hightlight}[**POH vol 2 => Performance => 3-45-50(Approach and Landing) => page 8**] 
""")
     