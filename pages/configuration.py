import streamlit as st

st.title("Aircraft Configuration")

st.session_state['pw535e1'] = st.toggle('PW535E1 engines', value=st.session_state['pw535e1'])
st.session_state['sb_505_00_0008'] = st.toggle('SB 505-00-0008: Operational Weight Increase', value=st.session_state
['sb_505_00_0008'])
st.session_state['sb_505_29_0005'] = st.toggle('SB 505-29-0005: Replacement of the hydraulic accumulator', value=st.session_state['sb_505_29_0005'])
st.session_state['autothrottle'] = st.toggle('Autothrottle', value=st.session_state['autothrottle'])

# st.json(st.session_state)





