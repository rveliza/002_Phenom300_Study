import streamlit as st

hightlight = ":orange-background"
cols_settings = [20, 80]



st.title("Flight Controls")
st.write("## Lights and Switches")


st.write("#### Trim Panel")


col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/switches_yaw.png", use_container_width=True)
with col2:
    with st.expander("Yaw Trim Switch (Spring Loaded to Neutral)"):
        st.write(f"""
- {hightlight}[**Commands the yaw trim to left or right**]
""")

col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/knobs_roll.png", use_container_width=True)
with col2:
    with st.expander("Roll Trim Switch (Spring Loaded to Neutral)"):
        st.write(f"""
- {hightlight}[**Commands the roll trim to left or right**]
""")

col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/switches_ptch_trim_man.png", use_container_width=True)
with col2:
    with st.expander("Pitch Trim Mode Switch"):
        st.write(f"""
- **BKP:** {hightlight}[**Enables the pitch trim backup mode and the pitch trim normal mode**]
- **OFF:** {hightlight}[**Enables the pitch trim normal mode and disables the pitch trim backup mode**]
""")

col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/switches_ptch_bckp.png", use_container_width=True)
with col2:
    with st.expander("Pitch Trim Backup Switch (Spring Loaded) to Neutral"):
        st.write(f"""
- Commands the pitch trim when backup mode is selected by the Pitch Trim MODE Switch
- {hightlight}[**Operation of the switch while the autopilot is engaged causes and autopilot disengagement**]

""")


        
st.write("## Question Bank")

with st.expander("What are the functions of the Multi-Function Spoilers?"):
     st.write(f"""
- {hightlight}[**Speed Brake**] 
    - Only available with flaps retracted
- {hightlight}[**Roll Spoiler**] 
    - When the flaps at any position other than 0, and the control wheel is rotated to a preset degree
- {hightlight}[**Ground Spoilers**] 
    - Aircraft on the ground
    - Thrust levers idle
    - Spoilers armed (deploy to 35 $\\degree$ at approximately 1.2 seconds)
""")
     

with st.expander("What is the purpose of the Ventral Rudder?"):
     st.write(f"""
- {hightlight}[**Provides yaw dampening when the yaw damper is off**] 
""")
     

with st.expander("Describe the flap system operation?"):
     st.write(f"""
- {hightlight}[**FCE operates one motor driving six flexible shafts thus six Irreversible Flap Linear Actuator's (IFLA's) which extend the flaps**] 
""")
     

with st.expander("What prevents trim runaway or mishandling beyond safe limits?"):
     st.write(f"""
- {hightlight}[**Limited to 3 seconds without releasing the trim switch**] 
""")
     

with st.expander("What are the primary flight controls?"):
     st.write(f"""
- {hightlight}[**Aileron**] 
- {hightlight}[**Elevator**] 
- {hightlight}[**Rudder**] 
""")
     

with st.expander("What are the secondary flight controls?"):
     st.write(f"""
- {hightlight}[**Flaps**] 
- {hightlight}[**Spoilers**] 
- {hightlight}[**Horizontal Stab**] 
- {hightlight}[**Gust Lock**] 
""")
     

with st.expander("What do each of the FCE's systems control?"):
     st.write(f"""
- {hightlight}[**FCE 1**] 
    - {hightlight}[**Pitch Trim Backup**] 
    - {hightlight}[**Flaps**] 
- {hightlight}[**FCE 2**] 
    - {hightlight}[**Normal Pitch Trim**] 
    - {hightlight}[**Spoilers**] 
""")
     

with st.expander("Flap position degrees and airspeed limitations?"):
     st.write(f"""
- {hightlight}[**1 / 180 KTS / 8$\\degree$**] 
- {hightlight}[**2,3 / 170 KTS / 26$\\degree$**] 
- {hightlight}[**4 / 160 KTS / 35$\\degree$**] 
""")
     

with st.expander("If extended, at what airspeed will the speed brakes retract?"):
     st.write(f"""
- {hightlight}[**125 Kts**] 
""")
     

with st.expander("Will the speed brakes retract if the power is advanced?"):
     st.write(f"""
- {hightlight}[**Yes**] 
""")
     

with st.expander("What is the purpose of the SLRBS System?"):
     st.write(f"""
- {hightlight}[**Provides assistance to the pilot in the rudder control in case of thrust asymmetry by controlling the spring preload of two tension springs**] 
- {hightlight}[**Preload is modified by means of a hydraulic actuator**] 
""")
     

with st.expander("What besides the aircraft's yaw damper provides yaw damping capability?"):
     st.write(f"""
- {hightlight}[**Ventral Rudder**] 
""")
     

with st.expander("Which trims are commanded by the TAC through the trim panel?"):
     st.write(f"""
- {hightlight}[**Aileron**] 
- {hightlight}[**Rudder**] 
""")
     

with st.expander("Where is the roll trim actuator installed?"):
     st.write(f"""
- {hightlight}[**On the left wing tip**] 
""")
     

with st.expander("How would roll or rudder trim failure be detected?"):
     st.write(f"""
- {hightlight}[**Switch activation will not move the trim tab**] 
- {hightlight}[**No CAS message**] 
""")
     

with st.expander("Where are the auto-tab surfaces located and what do they do?"):
     st.write(f"""
- {hightlight}[**Elevator surface trailing edge**] 
- {hightlight}[**Automatically deflected whenever there is an elevator surface deflection**] 
""")
     

with st.expander("How are elevator commands generated?"):
     st.write(f"""
- {hightlight}[**Autopilot**] 
- {hightlight}[**Control Wheel**] 
- {hightlight}[**Stick Pusher**] 
""")
     

with st.expander("What conditions must be met for speed brake deployment?"):
     st.write(f"""
- {hightlight}[**Flaps retracted**] 
- {hightlight}[**Any TLA lower than MAX CRZ**] 
- {hightlight}[**IAS > 125 Kt**] 
""")
     

with st.expander("Roll Mode description:"):
     st.write(f"""
- {hightlight}[**Below 6$\\degree$ = Wings Level**] 
- {hightlight}[*6$\\degree$ to 30$\\degree$ = Current bank**] 
- {hightlight}[**Above 30$\\degree$ = Comes back to 30$\\degree$**] 
""")
     
with st.expander("How many trim motors?"):
     st.write(f"""
**Two**  
- {hightlight}[**Normal**] 
- {hightlight}[**Backup**] 
""")
     

with st.expander("Config Check Test"):
     st.write(f"""
- {hightlight}[**Flaps**] 
- {hightlight}[**Trim**] 
- {hightlight}[**Brakes**] 
- {hightlight}[**Spoilers**] 
""")
     
with st.expander("Describe flap system operation"):
     st.write(f"""
- {hightlight}[**FCE operates one electric motor that drives felxible shafts which exted the flaps**] 
""")

