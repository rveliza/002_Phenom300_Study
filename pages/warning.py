import streamlit as st

hightlight = ":orange-background"
cols_settings = [20, 80]



st.title("Warning System")


st.write("## Question Bank")

with st.expander("Describe the low speed awareness tape?"):
     st.write(f"""
- {hightlight}[**Yellow band**] top of red + 3 knots
- {hightlight}[**Red Band**] Bottom of airspeed to airspeed at which the Stall Warning aural message will be activated
""")
     

with st.expander("Describe the aural alert associated with a configuration warning?"):
     st.write(f"""
- {hightlight}[**Too low gear**] 
- {hightlight}[**Too low flaps**] 
""")
     

with st.expander("Explain the alerting for an altitude deviation?"):
     st.write(f"""
- {hightlight}[**Deviation +/- 200 ft**] 
     - {hightlight}[**black box with yellow digits**] 
     - {hightlight}[**two aural tones**] 
     - {hightlight}[**'Altitude' voice alert**] 
""")
     

with st.expander("Explain the alerting as the aircraft approaches a selected altitude"):
     st.write(f"""
- {hightlight}[**Upon passing 1,000 ft of selected altitude**] 
     - {hightlight}[**the box changes to black text on a light blue background**] 
     - {hightlight}[**flashes for five seconds**] 
     - {hightlight}[**aural tone is generated**] 
     - {hightlight}[**Within 200 ft**] 
          - {hightlight}[**Selected altitude changes to light blue text on a black background**] 
          - {hightlight}[**Flashes for five seconds**] 
""")
     

with st.expander("What conditions will cause a takeoff configuration, on ground and throttles advanced for takeoff?"):
     st.write(f"""
- {hightlight}[**No Takeoff Brakes**] 
- {hightlight}[**No Takeoff Flaps**] 
- {hightlight}[**No Takeoff Spoilers**] 
- {hightlight}[**No Takeoff Trim**] 
""")
     