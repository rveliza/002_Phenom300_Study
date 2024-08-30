import streamlit as st

hightlight = ":orange-background"
cols_settings = [20, 80]



st.title("Automatic Flight")
st.write("## Lights and Switches")


st.write("#### Electrical Panel")

col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/switches_gen_1.png", use_column_width=True)
with col2:
    with st.expander("Generator 1 Switch"):
        st.write(f"""
- **AUTO:**{hightlight}[**Closes the GEN 1 contactor, connecting generator 1 to the DC BUS 1**] 
- **OFF:**{hightlight}[**Opens the GEN 1 contactor isolating generator 1 from the DC BUS 1**] 
""")

col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/buttons_gpu.png", use_column_width=True)
with col2:
    with st.expander("Ground Power Unit (GPU) Button"):
        st.write(f"""
- **PUSH IN:** {hightlight}[**connects the DC GPU to the CENTRAL BUS, according to the soiurce priority**]
- **PUSH OUT:** {hightlight}isolates de DC GPU from the CENTRAL BUS
""")

col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/switches_gen_2.png", use_column_width=True)
with col2:
    with st.expander("Generator 2 Switch"):
        st.write(f"""
- **AUTO:**{hightlight}[**Closes the GEN 2 contactor, connecting generator 2 to the DC BUS 2**] 
- **OFF:**{hightlight}[**Opens the GEN 2 contactor isolating generator 2 from the DC BUS 2**] 
""")

col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/switches_batt_1.png", use_column_width=True)
with col2:
    with st.expander("Battery 1 Switch"):
        st.write(f"""
- **ON:** {hightlight}[**Closes BC 1 contactor, connecting HOT BATT BUS 1 to the EMERGENCY BUS**]
- **OFF:** Opens the BC 1 contactor
""")


col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/buttons_elec_emer.png", use_column_width=True)
with col2:
    with st.expander("Electrical Emergency Button"):
        st.write(f"""
- **PUSH IN:** Overrides the EPGDS automatic transfer to the electrical emergency circuitry, {hightlight}[**connecting the batteries directly to the EMERGENCY BUS,**] regardlesss of any other command from the Electrical Distribution Logic.
- **PUSH OUT** {hightlight}[**The power contactors operate automatically**] according to the Electrical Distribution Logic.
""")
        

col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/switches_batt_2.png", use_column_width=True)
with col2:
    with st.expander("Battery 2 Switch"):
        st.write(f"""
- **ON:** {hightlight}[**Closes BC 2 contactor, connecting HOT BATT BUS 2 to the CENTRAL BUS**]
- **OFF:** Opens the BC 2 contactor
""")

col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/knobs_bus_tie.png", use_column_width=True)
with col2:
    with st.expander("Bus Tie Knob"):
        st.write(f"""
- **1 OPEN:** Opens the {hightlight}[**BTC 1 isolating DC BUS 1 and allows the BTC 2 automatic opration**]
- **AUTO:**  Allows the EPGDS to {hightlight}[**automatically operate the BTC 1 and BTC 2**]
- **2 OPEN:** Opens the {hightlight}[**BTC 2 isolating DC BUS 2 and allows the BTC 1 automatic opration**]
""")


st.write("## Question Bank")

with st.expander("Minimum battery voltage prior to engine start:"):
     st.write(f"""
- {hightlight}[**24 volts**] 
""")

with st.expander("In flight with battery power only, which electrical busses are powered in Electrical Emergency?"):
     st.write(f"""
- {hightlight}[**Both Hot Battery Busses**] 
- {hightlight}[**Emergency Bus**] 
- {hightlight}[**Central Bus**] 
""")
     

with st.expander("How long will batteries last in Electrical Emergency?"):
     st.write(f"""
- {hightlight}[**45 minutes**] 
""")

with st.expander("What is the purpose of the Quiet Start Contactor?"):
     st.write(f"""
- {hightlight}[**Allows engine start without power surges to the avionics**] 
""")

with st.expander("What busses are normally powered by GEN 1?"):
     st.write(f"""
- {hightlight}[**DC BUS 1**] 
- {hightlight}[**SHED BUS 1**] 
- {hightlight}[**EMERGENCY BUS**] 
- {hightlight}[**HOT BATT BUSS 1**] 
""")


with st.expander("What busses are normally powered by GEN 2?"):
     st.write(f"""
- {hightlight}[**DC BUS 2**] 
- {hightlight}[**SHED BUS 2**] 
- {hightlight}[**CENTRAL BUS**] 
- {hightlight}[**HOT BATT BUSS 2**] 
""")

with st.expander("How many batteries power the airplane?"):
     st.write(f"""
- {hightlight}[**Two**] 
""")

with st.expander("What type of batteries are installed?"):
     st.write(f"""
- {hightlight}[**Lead Acid**] 
""")

with st.expander("How many volts and amps?"):
     st.write(f"""
- {hightlight}[**24 VDC**] 
- {hightlight}[**42 ah**] 
""")

with st.expander("Which battery provides power for engine starting?"):
     st.write(f"""
- {hightlight}[**#2 Battery**] 
""")

with st.expander("What is the minimum voltage for charging?"):
     st.write(f"""
- {hightlight}[**27 volts**]  
""")

with st.expander("What are the generator loads?"):
     st.write(f"""
- {hightlight}[**Ground 330 A**] 
- {hightlight}[**Flight 390 A**] 
""")


with st.expander("What is the minimum battery temperature for normal operation?"):
     st.write(f"""
- {hightlight}[**-10/-18 $\degree$C**] 
""")
     
with st.expander("If a single generator fails in flight, what happens?"):
     st.write(f"""
- {hightlight}[**Both SHED BUSSES lose power**] 
""")


with st.expander("What does it mean if the GPU is plugged in, but there is no GPU AVAIL light illuminated?"):
     st.write(f"""
- {hightlight}[**DC power requirement from th GPU of between 26V and 29V is not met**] 
""")

with st.expander("What are we looking for when we push in the Electrical Emergency Button on the before taxi checklist?"):
     st.write(f"""
- {hightlight}[**Batteries show at least 23.5 volts**] 
- Generators continue to power the DC busses in this scenario, but certain other relays open in order to confirm battery voltage
""")


with st.expander("If the GPU is powering the airplane, when do the generatos come on line?"):
     st.write(f"""
- {hightlight}[**When the GPU is disconnected**] 
""")
     
with st.expander("If the GPU is connected and the Electrical Emergency Button is pushed in, what happens?"):
     st.write(f"""
- {hightlight}[**The electrical system is forced into an electrical emergency, connecting the batteries directly to the emergency bus**] 
""")
     
with st.expander("What does the GPU supply power to?"):
     st.write(f"""
- {hightlight}[**Central Bus**] 
""")
     
with st.expander("How many transformer rectifiers does the P300 have?"):
     st.write(f"""
- {hightlight}[**None**] 
""")
     
with st.expander("What are the external power source (GPU) voltage requireents?"):
     st.write(f"""
- {hightlight}[**600 Amps min**] 
- {hightlight}[**25V-29V**] 
""")
     
with st.expander("What is necesarry for the Shed Busses to come online, on the ground?"):
     st.write(f"""
- {hightlight}[**Single Generator**] 
- {hightlight}[**GPU online**] 
""")
     

with st.expander("What causes an electrical emergency?"):
     st.write(f"""
- {hightlight}[**Loss of both generators**] 
""")
     
     
with st.expander("What busses will be lost during an engine failure in flight?"):
     st.write(f"""
- {hightlight}[**Shed Busses**] 
""")
     