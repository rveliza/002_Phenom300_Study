import streamlit as st

st.title("Memory Items")

with st.expander(":red-background[SMOKE/FIRE/FUMES]"):
    st.write("""
1. Oxygen Masks - DON, EMERGENCY   
    -EMERGENCY then 100% after 2 minutes  
2. Dilution Valve - CLOSED
3. Smoke Goggles - DON
4. Communication - ESTABLISH
5. DUMP Button - PUSH IN  
**LAND AS SOON AS POSSIBLE**
""")
    
with st.expander(":red-background[SMOKE EVACUATION]"):
    st.write("""
1. Oxygen Masks - DON, EMERGENCY   
    -EMERGENCY then 100% after 2 minutes  
2. Dilution Valve - CLOSED
3. Smoke Goggles - DON
4. Communication - ESTABLISH
5. Oxygen Knob - CREW ONLY
6. DUMP Button - PUSH IN
7. ECS knob - OFF VENT  
**LAND AS SOON AS POSSIBLE**
""")
    
with st.expander(":red-background[DUAL ENGINE FAILURE]"):
    st.write("""
1. Thrust Levers - IDLE    
2. Oxygen Masks - DON 100%
3. Communication - ESTABLISH   
             
**LAND AS SOON AS POSSIBLE**
""")
    
with st.expander(":red-background[EMERGENCY DESCENT]"):
    st.write("""
1. Fasten Seat Belts Sign - ON 
2. Altitude - 10,000 FT OR MEA (WHICHEVER IS HIGHER)
3. Thrust Levers - IDLE
4. SPEED BRAKE switch - OPEN
5. Airspeed - MAX 250 KIAS/$M_{mo}$  
6. LDG GEAR Lever - DN
7. Transponder - 7700
8. ATC - NOTIFY
""")
    
with st.expander(":red-background[EMERGENCY EVACUATION]"):
    st.write("""
1. Thrust Levers - IDLE
2. Emergency/Parking Break - ON 
3. START/STOP knobs - STOP
4. SHUTOFF 1 & 2 Buttons - PUSH IN
5. PRESN MODE Switch - MAN
6. DUMP Button - Push In
7. ATC - NOTIFY
8. Evacuation - PERFORM
9. BATT 1 & 2 Switches - OFF
""")
    
with st.expander(":red-background[ENGINE ABNORMAL START]"):
    st.write("""
1. START/STOP knob - STOP
""")
    
with st.expander(":red-background[ENGINE FIRE, SEVERE DAMAGE OR SEPARATION]"):
    st.write("""
1. Autothrottle (if applicable) - DISENGAGE  
    **Affected Engine:**
2. Thrust Lever - IDLE
3. START/STOP knob - STOP
4. SHUTOFF Button - PUSH IN  
    **Wait 30 seconds and if fire persists:**
5. Bottle Switch - DISCH  
             
**LAND AS SOON AS POSSIBLE**
""")
    
with st.expander(":red-background[CAB ALTITUDE HI]"):
    st.write("""
1. Oxygen Masks - DON 100%
2. Communication - ESTABLISH
3. Fasten Seat Belts Sign - ON 
4. Altitude - 10,000 FT OR MEA (WHICHEVER IS HIGHER)
5. Thrust Levers - IDLE
6. SPEED BRAKE switch - OPEN
7. Airspeed - MAX 250 KIAS/$M_{mo}$ 
8. LDG GEAR Lever - DN
9. Transponder - 7700
10. ATC - NOTIFY
""")
    
    
with st.expander(":red-background[ELEC EMERGENCY]"):
    st.write("""
1. PRESS MODE Switch - MANUAL
2. CABIN ALT Switch - HOLD DOWN FOR 10 SECONDS     
**If at or above 25,000 ft:**  
Rudder Pedals - FIXED  
**If above 10,000 ft:**  
CAB ALT HI - ACCOMPLISH
""")
    

with st.expander(":red-background[ELEC XFR FAIL]"):
    st.write("""
1. ELEC EMER Button - PUSH IN  
**LAND AS SOON AS POSSIBLE**
""")
    
with st.expander(":red-background[ENGINE 1 (2) FIRE]"):
    st.write("""
1. Autothrottle (if applicable) - DISENGAGE  
    **Affected Engine:**
2. Thrust Lever - IDLE
3. START/STOP knob - STOP
4. SHUTOFF Button - PUSH IN  
    **On grounde or if Fire Persists after 30 seconds in flight:**
5. Bottle Switch - DISCH  
             
**LAND AS SOON AS POSSIBLE**       
""")
    
 
with st.expander(":red-background[TAKEOFF WITH ENGINE FAILURE AT OR ABOVE $V_{1}$]"):
    st.write("""
    1. At v$_r$ rotate the airplane according to the following table:
""")
    st.write("""
    |FLAP POSITION|   1   |   2   |
    |:---:|:---:|:---:|
    |PITCH ANGLE|10.5| 8 |
    """)
    st.write("""
    **With Positive rate of climb**  
    2. LDG Lever - UP
    3. Airspeed - $V_2$
    """)

with st.expander(":red-background[REJECTED TAKEOFF (AT OR BELOW $V_1$)]"):
    st.write("""
1. Thrust Levers - IDLE  
2. Brakes - APPLY MAXIMUM
3. Directional Control - MAINTAIN
""")
    
with st.expander(":red-background[WINDSHEAR]"):
    st.write("""
1. Autothrottles (is applicable) - DISENGAGE
2. Thrust Levers - MAX
3. Autopilot - DISENGAGE
4. Pitch Angle (nose up) - 15$\degree$
""")
    
with st.expander(":orange-background[GEAR LEVER CAN NOT BE MOVED UP]"):
    st.write("""
**If associated with engine failure and obstacle clearance, simultaneusly proceed:**
1. DN LCK REL Button - PRESS
2. LDG GEAR Lever - UP
""")
    
with st.expander(":orange-background[INADVERTENT PUSHER ACTUATION]"):
    st.write("""
1. QUICK DISCONNECT Button - PRESS
2. PUSHER CUTOUT Button - PUSH IN
""")
    
with st.expander(":orange-background[LD WOW SYS FAIL]"):
    st.write("""
**If associated with engine failure and obstacle clearance, simultaneusly proceed:**
1. DN LCK REL Button - PRESS
2. LDG GEAR Lever - UP
""")

    

    

  
  
    

    
