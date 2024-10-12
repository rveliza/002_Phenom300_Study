import streamlit as st

configuration_page = st.Page("pages/configuration.py", title="Aircraft Configuration", icon="⚙️")
limitations_page = st.Page("pages/limitations.py", title="Limitations", icon="🚫")
memory_items_page = st.Page("pages/memory_items.py", title="Memory Items", icon="🧠")
ac_general_page = st.Page("pages/aircraft_general.py", title="Aircraft General", icon="✈️")
ams_page = st.Page("pages/ams.py", title="Air Management System", icon="💨")
auto_flight_page = st.Page("pages/auto_flight.py", title="Automatic Flight", icon="🤖")
electrical_page = st.Page("pages/electrical.py", title="Electrical System", icon="⚡")
engines_page = st.Page("pages/engines.py", title="Engines", icon="🚀")
fire_page = st.Page("pages/fire.py", title="Fire Protection", icon="🔥")
flight_controls_page = st.Page("pages/flight_controls.py", title="Flight Controls", icon="🕹")
flight_instruments_page = st.Page("pages/flight_instruments.py", title="Flight Instruments", icon="🎛")
fuel_page = st.Page("pages/fuel.py", title="Fuel System", icon="⛽")
hydraulic_page = st.Page("pages/hydraulics.py", title="Hydraulic System", icon="🩸")
ice_rain_page = st.Page("pages/ice_rain.py", title="Ice and Rain", icon="🌨️")
landing_gear_brakes_page = st.Page("pages/landing_gear_breaks.py", title="Landing Gear and Brakes", icon="🚦")
oxygen_page = st.Page("pages/oxygen.py", title="Oxygen System", icon="🫁")
warning_page = st.Page("pages/warning.py", title="Warning System", icon="⚠️")
regulations_page = st.Page("pages/regulations.py", title="Regulations", icon="🏛️")
wb_page = st.Page("pages/weight_balance.py", title="Weight and Balance", icon="⚖️")
units_converter_page = st.Page("pages/units.py", title="Units Converter", icon="")
isa_page = st.Page("pages/isa.py", title="ISA")


if 'first_visit' not in st.session_state:
    st.session_state['first_visit'] = True
    st.session_state['pw535e1'] = False
    st.session_state['sb_505_00_0008'] = True
    st.session_state['sb_505_29_0005'] = True
    st.session_state['autothrottle'] = False

else:
    st.session_state['first_visit'] = False


# st.write(st.session_state)

pg = st.navigation({
                    "Must Know": [limitations_page, memory_items_page],
                    "Aircraft Systems": [ac_general_page, 
                                         ams_page,
                                         auto_flight_page,
                                         electrical_page,
                                         engines_page,
                                         fire_page,
                                         flight_controls_page,
                                         flight_instruments_page,
                                         fuel_page,
                                         hydraulic_page,
                                         ice_rain_page,
                                         landing_gear_brakes_page,
                                         oxygen_page,
                                         warning_page,
                                         ],
                    "Tools": [wb_page,
                              units_converter_page,
                              isa_page,
                              regulations_page,
                              configuration_page],
                     })

st.set_page_config(
    initial_sidebar_state="expanded"
)

pg.run()



