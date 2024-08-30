import streamlit as st

empty_value = "."
empty_value_none = ""
highlight = ":orange-background"
large_just = 120

st.title("Limitations")

############ WEIGHTS
mrw = ("18,078", "18,497", "18,617")
mtow = ("17,968", "18,387", "18,551")
mlw = ("16,865", "17,042", "17,272")
mzfw = ("13,999", "14,220", "14,263")


st.write("## Aircraft Weights")
off_on = st.toggle(label="off_on", value=False, label_visibility="collapsed")


if  not off_on:
    title = ""
    pos1 = empty_value
    pos2 = empty_value
    pos3 = empty_value
    pos4 = empty_value

elif st.session_state['pw535e1']:
    title = "PW535E1 engines"
    pos1 = mrw[2] + " lb"
    pos2 = mtow[2] + " lb"
    pos3 = mlw[2] + " lb"
    pos4 = mzfw[2] + " lb"


elif st.session_state['sb_505_00_0008']:
    title = "Post Mod: SB 505-00-0008"
    pos1 = mrw[1] + " lb"
    pos2 = mtow[1] + " lb"
    pos3 = mlw[1] + " lb"
    pos4 = mzfw[1] + " lb"

else:
    title = "Pre Mod: SB 505-00-0008"
    pos1 = mrw[0]
    pos2 = mtow[0]
    pos3 = mlw[0]
    pos4 = mlw[0]

table = """
        | (MRW) | (MTOW) | (MLW) | (MZFW) |
        | :---: | :---: | :---: | :---: |
        | {mrw} | {mtow}  | {mlw}  | {mzfw}  |
                    """.format(mrw=pos1, mtow=pos2, mlw=pos3, mzfw=pos4)

st.markdown(f"###### {title}")
st.write(table)


#################### LANDING GEAR SPEEDS
st.write("## Langing Gear Operation/Extended Speed ($v_{lo}$ & $v_{le}$)")

with st.expander("Maximum speed at which the Landing Gear can be safely extended & retracted ($V_{lo}$):"):
    st.write(f"{highlight}[**250 KIAS**]")

with st.expander("Maximum speed at which the Landing Gear can be safely extended & locked ($V_{le}$):"):
    st.write(f"{highlight}[**250 KIAS**]")

#################### Minimum Control Speed
st.write("## Minimum Control Speed ($V_{mc}$)")

if st.session_state['pw535e1']:
    vmc_takeoff = f"{highlight}[**99 KIAS**]"
else:
    vmc_takeoff = f"{highlight}[**97 KIAS**]"

vmc_land_no_ice = f"{highlight}[**91 KIAS**]"
vmc_land_ice = f"{highlight}[**95 KIAS**]"

with st.expander("Minimum Control Speed ($V_{mc}$) for takeoff (takeoff flaps):"):
    st.write(vmc_takeoff)

with st.expander("Minimum Control Speed ($V_{mc}$) for landing (landing flaps) in 'No icing Conditions:"):
    st.write(vmc_land_no_ice)

with st.expander("Minimum Control Speed ($V_{mc}$) for landing (landing flaps) in 'Icing Conditions:"):
    st.write(vmc_land_ice)


############################ Operating Maneuvering
st.write("## Operating Maneuvering Speed ($V_o$)")
with st.expander("Operating Maneuvering Speed ($V_o$):"):
    st.write(f"{highlight}[**205 KIAS**]")



############################# Flaps
st.write("## Maximum Flap Extendes Speed ($V_{fe}$)")
off_on = st.toggle(label="off_on", key="flaps_speeds", label_visibility="collapsed")

    
flaps_table = f"""
| Flap Pos | Ret Speed     | Min Man. Speed | Degr | Max Speed |
| -------- | :--------:                | :--------:    | :--------: | :------:    |
| Flap 0   |                           |   150 KIAS    | 0$\degree$ |             |
| Flap 1   | $\Rightarrow$ 0: V2 + 11  |   140 KIAS    | 8$\degree$ | :orange-background[180 KIAS]  |
| Flap 2 |$\Rightarrow$ 1: V2 + 9, 1$\Rightarrow$ 0: V2 + 20 |130 KIAS|8$\degree$| :orange-background[170 KIAS]|
| Flap 3   |     |   130 KIAS    | 26$\degree$| :orange-background[170 KIAS]    |
| Flap Full|     |   125 KIAS    | 35$\degree$| :orange-background[160 KIAS]    |
"""

flaps_table_off = f"""
| Flap Pos | Ret Speed      | Min Man. Speed | Degr | Max Speed   |
| --------      | :--------:                                         | :--------:    | :--------: | :------:    |
| Flap 0        |                                                    |   .    | . |             |
| Flap 1        | .                           |   .    | . | .    |
| Flap 2        | . |   .    | . | .    |
| Flap 3        |                                                    |   .    | .| .    |
| Flap Full     |                                                    |   .    | .| .    |
"""

if off_on:
    st.write(flaps_table)
else:
    st.write(flaps_table_off)


####################################### ALTITUDE FLAPS EXTENDED
st.write("## Maximum Altitude For Flaps Extended")

with st.expander("Maximum altitude with extended Flaps:"):
    st.write(f"{highlight}[**18,000 ft**]")



####################################### Tire Speed
st.write("## Maximum Tire Ground Speed")

with st.expander("Maximum Tire Ground Speed:"):
    st.write(f"{highlight}[**182 Kt**]")

max_tire_speed = f"{highlight}[**182 Kt**]"


#################################### Runway Slope
st.write("## Runway")

question_a = "Runway slope:"
question_b = "Type of runway surface:"

slope = f"{highlight}[**-2% to +2%]"
surface = f"{highlight}[**Paved**]"

with st.expander(f"""
{question_a}  

{question_b} 
"""):
    st.write(f"""
{question_a} {slope}   
{question_b} {surface}
""")


######### Load Factors 
st.write("## Load Factor Limit (G Loads)")

with st.expander("Load Factor Limit (G laods) with Flaps UP:"):
    st.write(f"{highlight}[**3.00 g**]")

with st.expander("Load Factor Limit (G loads) with Flaps DOWN (1, 2, 3 & FULL)"):
    st.write(f"{highlight}[**2.00 g**]")



############ Baggage Loading
st.write("## Baggage Loading")
st.write("###### Maximum loading:")
off_on = st.toggle(label="off_on", key="baggage", label_visibility="collapsed")

if off_on:
    max_lh = f"{highlight}[**44 Lb**]"
    max_lav = f"{highlight}[**33 Lb**]"
    max_aft = f"{highlight}[**463 Lb**]"
    max_fwd = f"{highlight}[**110 Lb**]"
    max_ctr = f"{highlight}[**71 Lb**]"
    max_side = f"{highlight}[**36 Lb**]"
    
else:
    max_lh = max_lav = max_aft = max_fwd = max_ctr = max_side = empty_value_none
    
baggage_load_text = f"""
LH Forward Cabinet.......................................{max_lh}  
Lavatory Cabinet............................................{max_lav}  
Aft Baggage Compartment............................{max_aft}  
Forward Baggage Compartment...................{max_fwd}  
Refreshment Center.......................................{max_ctr}  
Side-Facing Divan Stowage Compartments..{max_side}
"""

st.write(baggage_load_text)


################### Wind Limitations
st.write("## Wind Limitations")

with st.expander("Max takoff and landing tailwind component:"):
    st.write(f"{highlight}[**10 KTS**]")

with st.expander("Max takeoff and landing tailwind component"):
    st.write(f"{highlight}[**18 KTS**]")



############################### Hydraulic
if not st.session_state['sb_505_29_0005']:
    st.write("## Hydraulic")
    with st.expander("For airplanes pre-mod SB-29-0005, the hydraulic system accumulator pre-charge check interval:"):
        st.write(f"{highlight}[**Every 15 days or before the next flight, whechever ocfurs last**]")
    

########################### Warning
st.write("## Warning")
with st.expander("Stall Warning and Protection System must be tested:"):
    st.write(f"{highlight}[**Prior to each flight**]")



########################## Syntetic Vision
st.write("## Synthetic Vision")
with st.expander("What are the prohibitions associated with the use of the SVS?"):
    st.write(f"{highlight}[**Use of the SVS as primary information to base decisions and/or plan maneuvers, to navigate or to avoid terrain, obstacles, or traffic is prohibited**]")


########################### Electrical
st.write("## Electrical")

with st.expander("Maximum battery voltage required for engine start:"):
    st.write(f"{highlight}[**24 V**]")

with st.expander("Maximum GPU voltage required for battery charging"):
    st.write(f"{highlight}[**27 V**]")

with st.expander("Maximum generator load on ground:"):
    st.write(f"{highlight}[**330 Amps each**]")
             
with st.expander("Maximum generator load if flight:"):
    st.write(f"{highlight}[**390 Amps each**]")


################################ Fuel
st.write("## Fuel")

if st.session_state['pw535e1']:
    usable_fuel = f"{highlight}[**2,702 lb**]"
    unusuable_fuel = f"{highlight}[**24.2 lb**]"
    max_fuel = f"{highlight}[**5,427.6 lb**]"
else:
    usable_fuel = f"{highlight}[**2,676 lb**]"
    unusuable_fuel = f"{highlight}[**25.13 lb**]"
    max_fuel = f"{highlight}[**5,401 lb**]"

with st.expander("Maximum usable fuel quantity per tank:"):
    st.write(f"{usable_fuel}")

with st.expander("Unusable fuel quantity per tank:"):
    st.write(f"{unusuable_fuel}")

with st.expander("Maximum fuel capacity"):
    st.write(f"{max_fuel}")

with st.expander("Maximum permitted imbalance between tanks:"):
    st.write(f"{highlight}[**220 lbs**]")

with st.expander("Minimum Fuel Tank Temperature"):
    st.write(f"{highlight}[**-37$\degree$C**]")

with st.expander("Maximum Fuel Tank Temperature (On Ground)"):
    st.write(f"{highlight}[**52 $\degree$C**]")
    st.write("**NOTE: MAXIMUM FUEL TEMPERATURE CAN BE EXCEEDED UP TO 80$\degree$C IN FLIGHT**")

with st.expander("Position of 'XFEED' Knob during Takeoff and Landing:"):
    st.write(f"{highlight}[**'OFF'**]")



##################### Engine
st.write("## Engine Opeerational Limits")
off_on = st.toggle(label="off_on", key="engineLimits", label_visibility="collapsed")

engine_limits = """
|Thrus Setting|Time Limit|Max ITT$\degree$C|N2 %|N1 %|Oil Press. (psid)|Oil Temp$\degree$C| 
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|**Max Trhust**|10 minutes|725|101|100|45 to 160|10 to 132.2|
|**Takeoff Thrust**|5 minutes|700|101|100|45 to 160|10 to 132.2|
|**Maximum Continuous**| |680|101|100|45 to 160|10 to 132.2|
|**Maximum Climb**| |680|101|100|45 to 160|10 to 132.2|
|**Ground Idle**|N/A|N/A|Min 55.1(OEI) / Min 51.2(AEO)| |25 to 160|-40 to 132.2|
|**Flight Idle**|N/A|N/A|55.1| |25 to 160| |
|**Starting**| 5 seconds |765| | | |-40 minimum|
|**Transient**| 20 seconds |765| 103 | 102 | 0-20| |
|**Transient**| 200 seconds ||  |  | | 140.5 Maximum |
|**Transient**| 400 seconds ||  |  | 20-270 |  |
"""

engine_limits_off = """
|Thrus Setting|Time Limit|Max ITT$\degree$C|N2 %|N1 %|Oil Press. (psid)|Oil Temp$\degree$C| 
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|**Max Trhust**| .|.|.|.|.|.|
|**Takeoff Thrust**|.|.|.|.|.|.|
|**Maximum Continuous**| |.|.|.|.|.|
|**Maximum Climb**| |.|.|.|.|.|
|**Ground Idle**|N/A|N/A|.| |.|.|
|**Flight Idle**|N/A|N/A|.| |.| |
|**Starting**| 5 seconds |.| | | |.|
|**Transient**| 20 seconds |.| . | . |. | |
|**Transient**| 200 seconds ||  |  | | . |
|**Transient**| 400 seconds ||  |  | . |  |
"""

if off_on:
    st.write(engine_limits)
else:
    st.write(engine_limits_off)


########################## Starter Limits
st.write("## Starter Limits")
off_on = st.toggle(label="off_on", key="motoring", label_visibility="collapsed")

starter_limits = """
|MOTORING ATTEMT|COOL-DOWN TIME|
|:---:|:---:|
|$1^{st}$|60 seconds|
|$2^{nd}$|60 seconds|
|$3^{rd}$|15 minutes|
|$4^{th}$|30 minutes|
"""
starter_limits_off = """
|MOTORING ATTEMT|COOL-DOWN TIME|
|:---:|:---:|
|$1^{st}$|.|
|$2^{nd}$|.|
|$3^{rd}$|.|
|$4^{th}$|.|
"""

if off_on:
    st.write(starter_limits)
    st.write("""NOTE:AFTER FOUR SEQUENTIAL MOTORINGS,  
              CYCLE MAY BE REPEATED FOLLOWING A 30   
             MINUTE COOL-DOWN PERIOD""")
else:
    st.write(starter_limits_off)


######################### Air Conditioning
st.write("Air Conditioning")

with st.expander("For air conditioning system operation on ground: "):
    st.write(f"""
- GPU must be used or,
- one engine generator must be turned ON
""")
    

########################### Pressurization
st.write("Pressurization")

with st.expander("Maximum Differential Pressure"):
    st.write(f"{highlight}[**9.4 PSI**]")

with st.expander("Maximum Differential Overpressure"):
    st.write(f"{highlight}[**9.6 PSI**]")

with st.expander("Maximum Differential Negative Pressure"):
    st.write(f"{highlight}[**-0.3 PSI**]")

with st.expander("Maximum Differential Negative Pressure for Takeoff and Landing"):
    st.write(f"{highlight}[**0.2 PSI**]")


########################### Ice and Rain Protection
st.write("## Ice and Rain Protection")

with st.expander("When must the crew activate the Ice Protection System?"):
    st.write(f"{highlight}[**Crew must activate the ice protection system when icing conditions exist or are anticipated, as per Section 3, Normal Procedures**]")

with st.expander('Define "when icing conditions exist or are anticipated"'):
    st.write("""
1. SAT on ground for takeoff, or TAT in flight is 10 $\degree$C or below and visible moisture in any form is present (such as cloud, fog, with visibility of one mile or less, rain, snow, sleet or ice crystals)
             
2. SAT on the ground is 10$\degree$C or below and ramps, taxiways, or runways are contaminated with surface snow, ice, standing water, or slush.
""")
    
with st.expander("What is the limitation regarding contaminated aircraft surfaces?"):
    st.write(f"{highlight}[**Takeoff is prohibited**] with frost (polished or not), ice, snow or slush adhering to wings, control surfaces, engine inlets, or other critical surfaces")

with st.expander("In what environment condition is flight prohibited?"):
    st.write(f"""
- Flight in {highlight}[**freezing drizzle**] or {highlight}[**freezing rain**] is prohibited
- **The pilot must immediately exit the freezing rain or freezing drizzle conditions by changing altitude or course**
""")
    
with st.expander("What are the limitations regarding use of the Autopilot in icing conditions?"):
    st.write(f"""
Autopilot use is {highlight}[**prohibited**] in the following conditions:
- Severe Icing
- Unusual control force or control deflection, or unusually large control forces to move flight controls when the autopilot is disconnected.
- Indications of frequent autopilot re-trimming during stroight and level flight
""")
    

############################### Operating in Icing Conditions
st.write("## Operation In Icing Conditions")

with st.expander("Maximum Takeoff and Landing Altitude"):
    st.write(f"{highlight}[**10,000 ft**]")

with st.expander("""Maximum Airspeed (flap and gear up)   
                 Wing and Stabilizer Anti-Ice System Inhibited
                 """):
    st.write(f"{highlight}[**165 KIAS**]")

with st.expander("""Maximum Airspeed (flap and gear up)   
                 Wing and Stabilizer Anti-Ice System Inhibited
                 """):
    st.write(f"{highlight}[**165 KIAS**]")

with st.expander("""Maximum Airspeed (flap and gear up)   
                 Wing and Stabilizer Anti-Ice System Inhibited
                 """):
    st.write(f"{highlight}[**150 KIAS**]")


############################## Wing Inspection Light
st.write("## Wing Inspection Light")

with st.expander("When must the Wing Inspection Light be operative?"):
    st.write(f"{highlight}[**Prior to flight into known or forcast icing conditions, at night**]")


############################### Autopilot/Yaw Damper
st.write("## Autopilot / Yaw Damper")

with st.expander("Minimum Engagement height (dual engine)"):
    st.write(f"{highlight}[**600 ft AGL**]")

with st.expander("Minimum Engagement Height (single engine)"):
    st.write(f"{highlight}[**1,000 ft AGL**]")

with st.expander("Minimum Use Height (dual engine)"):
    st.write(f"{highlight}[**195 ft AGL**]")

with st.expander("Minimum Use Height (single engine)"):
    st.write(f"{highlight}[**220 ft AGL**]")

with st.expander("Altitude Loss (maneuvering/Cruise)"):
    st.write(f"{highlight}[**160 ft**]")

with st.expander("Yaw Damper OFF airspeed is limited to ______ if in icing conditions"):
    st.write(f"{highlight}[**180 KIAS**]")


################################# Autothrottle
if st.session_state['autothrottle']:
    st.write("## Autothrottle")

    with st.expander("The use of Autothrottle CLB (FLC) mode with flaps extended is only allowed during what phase of flight?"):
        st.write(f"{highlight}[**Go-around**]")

    with st.expander("In what situation is the use of the autothrottle prohibited?"):
        st.write(f"{highlight}[**Takeoff or go-around with engine failure**]")

    with st.expander("Minimum altitude (dual engine)"):
        st.write(f"{highlight}[**195 ft AGL**]")

    with st.expander("Minimum altitude (single engine)"):
        st.write(f"{highlight}[**220 ft AGL**]")

















