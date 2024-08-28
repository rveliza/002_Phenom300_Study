import streamlit as st

hightlight = ":orange-background"
cols_settings = [20, 80]



st.title("Oxygen System")
st.write("## Lights and Switches")


st.write("#### Oxygen Control Panel")


col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/knobs_oxygen.png", use_column_width=True)
with col2:
    with st.expander("Oxygen Supply Control Knob (Rotary Action)"):
        st.write(f"""
- **CREW ONLY: ** {hightlight}[**Disables automatic deployment of passenger oxygen masks**]
- **PAX AUTO:** {hightlight}[**Enables automatic deployment of passenger oxygen masks when cabin pressure altitude is above 14,700 ft (+300/-300 ft), if the OXYGEN SUPPLY handle is pushed**]
- **PAX OVRD** {hightlight}[**Enables manual deployment of passenger oxygen masks regardless of cabin altitude, if the OXYGEN SUPPLY handle is pushed**]
""")

col1, col2 = st.columns(cols_settings)
with col1:
    st.image("images/handles_oxygen.png", use_column_width=True)
with col2:
    with st.expander("Oxygen Supply Handle"):
        st.write(f"""
- **PULLED:** {hightlight}[**oxygen is not available in the distribution system**]
- **PUSHED:** {hightlight}[**oxygen is available in the distribution system**]

""")

st.write("## Question Bank")

with st.expander("What FAR requirements for crew oxygen in a pressurizaed/unpressurized cabin:?"):
     st.write(f"""
- {hightlight}[**Pressurized cabin:**] 
    - {hightlight}[**Above FL350**] SP must wear mask
    - {hightlight}[**At or below FL410**] MP, if both at seats, masks not required
- {hightlight}[**Unpressurized cabin:**] 
    - {hightlight}[**12,500 ft - 14,000 ft, 30 min max**] the oxygen is required
""")
     