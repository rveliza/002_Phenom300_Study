import streamlit as st

st.title("Aircraft General")

with st.expander("Annunciator Test"):
    col1, col2 = st.columns(2)
    with col1:
        st.image("images/panels_test.png")
    with col2:
        st.write("""
    - Electrical Emergency Button 
    - Pusher Button
    - Parking Brake Button
    - Dump Button
    """)
    
with st.expander("Aircraft Dimensions"):
    col1, col2 = st.columns(2)
    with col1:
        st.image("images/dimensions.png")
        
    with col2:
        st.write("""
    - Length: 52 ft (16 m)
    - Width:  52 ft (16 m)
    - Height: 17 ft (6 m)
    """)
    
with st.expander("Turn Radius"):
        st.write("""
    - 60 ft aprox.
""")
    
    
with st.expander("Door Displays: Yellow vs Red"):
    st.write("""
- Yellow - Unpressurized
- Red - Pressurized
""")
    
with st.expander("Emergency Door Type"):
    st.write("""
- Plug type door
- **Bigger on the inside**
""")
    
with st.expander("Service ceiling"):
    st.write("""
- 45,000 ft
""")
    
    
with st.expander("First aid kit"):
    st.write("""
- Located in lavatory cabinet
""")
    
with st.expander("Water barrier"):
    st.write("""
- Installation - In front of Main Door
- Location - In back of captain seat
""")
    
with st.expander("Maximum takeoff and landing altitude"):
    st.write("""
- 8,300 ft
- 14,000 ft with AFM Supplement 2
""")
    
with st.expander("How is the rotating beacon turned on?"):
    st.write("""
- By turning one Stop/Start knob to Run
""")
    
with st.expander("AFM"):
    st.write("""
**Aircraft Specific**
- Limitations
- Supplements  
    i. RVSM  
    ii. Autothrottle  
- Weight and Balance
- CDL (Appendices Tab)
""")
    
with st.expander("POH"):
    st.write("""
- Detailed procedures (Checklist)
- Cold Weather ops   
- Aircraft Systems
- Comprehensive performance data
""")

    
with st.expander("QRH"):
    st.write("""
- Normal Procedures
- Emergency Procedures
- Symplified Takeoff Analysis and Landing Distance
""")
    
with st.expander("When does the LED on the toilet turn red?"):
     st.write(f"""
- {hightlight}[**Lavatory has reached 90% of total capacity**] 
""")
     
     
    

    

    

    
