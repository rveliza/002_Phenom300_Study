import streamlit as st

hightlight = ":orange-background"
cols_settings = [20, 80]



st.title("Engines")
st.write("## Lights and Switches")


st.write("#### Engine Control Panel")


col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/knobs_engine.png", use_container_width=True)
with col2:
    with st.expander("Eng Start/Stop Knob"):
        st.write(f"""
- **STOP:** {hightlight}[**commands the FADEC to shut down the engine, provided the associated thrust lever is in the IDLE position**]
- **RUN:** {hightlight}[**normal operations for engine operation**]
    - Activates the Beacon
- **START** {hightlight}[**Initiates the engine starting sequence**]
""")

col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/switches_ign.png", use_container_width=True)
with col2:
    with st.expander("Eng Ignition Switch"):
        st.write(f"""
- **ON:** {hightlight}[**Enables FADEC to continuosly activate both exciters when the engine is running**]
- **AUTO:** {hightlight}[**FADEC automatically controls the ignition system, depending on engine requirements in normal operation or autorelight.**]
- **OFF:** {hightlight}[**Deactivates the ignition system.**]
    - When engine is running, at idle or above, the FADEC disregards OFF position
""")


        
st.write("## Question Bank")

with st.expander("Describe the AUTO position of the ignition switch"):
     st.write(f"""
- {hightlight}[**The FADEC automatically controls the ignition system, depending on engine requirements in normal operation and autorelight**] 
""")
     

with st.expander("True statement concerning flameout situation?"):
     st.write(f"""
- {hightlight}[**FADEC automatically sequences both igniters ON**] and,
- {hightlight}[**Schedules fuel flow for relight until the N2 speed drops below 40%**] 
""")
     

with st.expander("Yellow boxed FAIL indication displayed in the N1 dial indicates?"):
     st.write(f"""
- {hightlight}[**Engine flameout or shutdown without pilot action**] 
""")
     

with st.expander("What must be true in order to shutdown an engine with the Start/Stob knob?"):
     st.write(f"""
- {hightlight}[**The trust lever must be in the IDLE position**] 
""")
    

with st.expander("What engines are on the Phenem 300 and how many lbs of thrust?"):
     st.write(f"""
- {hightlight}[**PW535E**] 
- {hightlight}[**3,360 lbs**] 
""")
     

with st.expander("How are the engines controlled?"):
     st.write(f"""
- {hightlight}[**By dual channel FADEC's**] 
    - {hightlight}[**When one channel is in control, the other channel is in SBY**] 
""")
     

with st.expander("What supplies power to the FADEC?"):
     st.write(f"""
**Whichever is higher:**  
- {hightlight}[**28 VDC airframe**] 
- {hightlight}[**PMA**] 
""")
     


     

with st.expander("What are some functions of the FADEC?"):
     st.write(f"""
- {hightlight}[**During start, it accelerates the operating engine’s N2 to 72% to protect the gearbox from damage**] 
- {hightlight}[**Ensures no limits are exceeded on hot, hung or no start**] 
- {hightlight}[**Controls ATR**] 
- {hightlight}[**Provides WHSAIS envelope information to AMS controller**] 
- {hightlight}[**Schedules fuel flow during starting based on N2 speed and ambient conditions**] 
- {hightlight}[**Controls the igniters**] 
- {hightlight}[**Calculates an N1 speed setting corresponding to the TLA**] 
""")
     

with st.expander("During start, when are both igniters automatically energized?"):
     st.write(f"""
- {hightlight}[**One igniter when TTO > 0$\\degree$C**] 
- {hightlight}[**Both igniters when TTO < 0$\\degree$C**] 
- {hightlight}[**Both igniters for in-flight engine starts (assisted or windmilling)**] 
- {hightlight}[**Autorelight**] 
""")
     

with st.expander("How does the FADEC assist an In-Flight start?"):
     st.write(f"""
- {hightlight}[**Activates both igniters during start**] 
- {hightlight}[**Disables the abort start logic**] 
""")
     

with st.expander("How does the FADEC assist in Auto Relight?"):
     st.write(f"""
- {hightlight}[**Continuosly monitors the engine parameters**] 
- {hightlight}[**Automatically turns on both igniters and schedules the relight fuel flow in case an engine flameout is detected.**] 
""")
     

with st.expander("How is dry monitoring performed?"):
     st.write(f"""
- {hightlight}[**Setting ENG INGITION to OFF**] 
- {hightlight}[**ENG START/STOP knob to START**] 
""")
     

with st.expander("What is the purpose of the Permanent Magnetic Alternator (PMA)?"):
     st.write(f"""
- {hightlight}[**Primary source of AC power to both FADEC channels when engine is running above idle.**] 
""")
     

with st.expander("What is the purpose of the ATR?"):
     st.write(f"""
- {hightlight}[**Automatically provides maximum engine thurst (TO RSV or GA RSV) whenever it is armed, thrust levers are at least at TOGA and one of the following conditions occurs**] 
    - {hightlight}[**Difference of N1 values is > 20% between both engines**] (one engine fails)
    - {hightlight}[**Loss of communication between both engines**] 
- {hightlight}[**TO RSV also provided whenever both engines are operating and both thrust levers are positioned to MAX**] 
- {hightlight}[**When ATR is commanded, the FADEC will close the ECS flow control valve.**] 
""")
     

with st.expander("What will happen if the START/STOP knob is moved to STOP and the TLA is not at idle?"):
     st.write(f"""
- {hightlight}[**The FADEC will disregard the STOP selection and not shut down the engine**] 
""")
     

with st.expander("What does an E1/2 OIL IMP BYP CAS message indicate?"):
     st.write(f"""
- {hightlight}[**There is an impending blockage of an oil filter**] 
""")
     

with st.expander("List the start malfunction protections provided by the FADEC?"):
     st.write(f"""
- {hightlight}[**No light off**] 
- {hightlight}[**Hung Start**] 
- {hightlight}[**Hot Start**] 
""")
     


