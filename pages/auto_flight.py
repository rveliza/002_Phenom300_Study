import streamlit as st

hightlight = ":orange-background"
cols_settings = [20, 80]



st.title("Automatic Flight")
st.write("## Lights and Switches")


st.write("#### Control Wheel")


col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/buttons_auto_off.png", use_container_width=True)

with col2:
    with st.expander("Quick Disconnect Button"):
        st.write(f"""
{hightlight}[**Provides the means to disengage:**]  
- Autopilot
- Yaw Damper
- Trim
- Pusher
- EDM
""")
        
col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/panels_throttles.png", use_container_width=True)

with col2:
    with st.expander("Takeoff and Go-Around Button"):
        st.write(f"""
- {hightlight}[**Selects the TO or GA modes**] according to the airplane status (AIR/GND)
- {hightlight}[**FMA lateral mode**] annunciation displays the following:
    - **ROL**: takeoff lateral mode
- {hightlight}[**FMA vertical mode**] annunciation displays the following:
    - **TO**: takeoff vertical mode
    - **GA**: go-around lateral mode

""")


col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/buttons_auto_off.png", use_container_width=True)

with col2:
    with st.expander("Control Wheel Steering Button"):
        st.write(f"""
**Pressing and holding:**
- {hightlight}[**Disengages the pitch servos**]
- {hightlight}[**Disengages the roll servos**]
- {hightlight}[**Allows the airplane to be hand flown**]
- {hightlight}[**Pitch trim is interrupted**]
- {hightlight}[**Yaw damper engagement is unaffected**]
- {hightlight}[**AP annunciation is temporarily replaced by CWS in white**]
""")



