import streamlit as st

hightlight = ":orange-background"
cols_settings = [20, 80]

st.title("Flight Instruments")
        
st.write("## Question Bank")

with st.expander("Describe the ADS System"):
     st.write(f"""
- {hightlight}[**ADS 1 => IASP 1**] 
- {hightlight}[**ADS 2 => IASP 2**] 
- {hightlight}[**ADS SBY => Pitot Static => IESI**] 
""")
     

with st.expander("Describe AHRS system"):
     st.write(f"""
- {hightlight}[**AHRS 1**] 
    - {hightlight}[**PFD 1**] 
    - {hightlight}[**MFD**] 
    - {hightlight}[**IESI**] 
- {hightlight}[**AHRS 2**] 
    - {hightlight}[**PFD 2**] 
""")
     

with st.expander("PFD 1 auto reversion in case of AHRS 1 failure"):
     st.write(f"""
- {hightlight}[**AHRS 1 => AHRS 2 => IESI**] 
""")
     

with st.expander("Describe G3000 screen failures"):
     st.write(f"""
- {hightlight}[**Right instrument goes to reversionary mode**] 
""")
     

with st.expander("What is true concerning a reversionary mode?"):
     st.write(f"""
- {hightlight}[**Mode of operation in which both flight PFD symboogy and EICAS are displayed simultaneusly on one unit**] 
""")
     

with st.expander("How many GPS receivers does the airplane have?"):
     st.write(f"""
- {hightlight}[**Two, one in each GIA**] 
""")
     

with st.expander("What is the primary source of the IESI?"):
     st.write(f"""
- {hightlight}[**ADS Sby**] 
""")
     

with st.expander("How many ADS systems are available?"):
     st.write(f"""
- {hightlight}[**ADS 1**] 
- {hightlight}[**ADS 2**] 
- {hightlight}[**ADS SBY**] 
""")
     

with st.expander("What does a yellow altimeter setting indicate?"):
     st.write(f"""
- {hightlight}[**L and R altimeter settings differ by 0.02 Hg**] 
""")
     

with st.expander("What does the green circle on the airspeed indicator indicate?"):
     st.write(f"""
- {hightlight}[**1.3 of Pusher**] 
""")
     

with st.expander("What happens to PFD2 and MFD in the event the left side PFD fails?"):
     st.write(f"""
- {hightlight}[**MFD enters reversionary mode**] 
- {hightlight}[**PFD remains normal**] 
""")
     

with st.expander("What is the primary source of navigation in the P300?"):
     st.write(f"""
- {hightlight}[**GPS**] 
""")
     

with st.expander("What is the function of the CPL pushbutton?"):
     st.write(f"""
- {hightlight}[**Swaps autopilot between the PF and PM**] 
""")
     

with st.expander("When in T/O or G/A mode, what must be true for ALT pre-selected mode to arm?"):
     st.write(f"""
- {hightlight}[**The preselected altitude must be greater than or equal to 400 ft from the aircraft altitude**] 
""")
     

with st.expander("What is the primary source of power to the IESI?"):
     st.write(f"""
- {hightlight}[**The emergency bus**] 
    - {hightlight}[**Reverts to DC BUS 1 in case needed**] 
""")
     

with st.expander("How does the CDI indicate navigation source?"):
     st.write(f"""
- {hightlight}[**Magent for GPS**] 
- {hightlight}[**Green single needle for VOR/LOC 1**] 
- {hightlight}[**Green double needles for VOR/LOC 2**] 
""")
     

with st.expander("What is the source of heading information for the IESI?"):
     st.write(f"""
- {hightlight}[**AHRS 1**] 
""")
     

with st.expander("What is the primary source of attitude and heading information is?"):
     st.write(f"""
- {hightlight}[**AHRS 1 and AHRS 2**] 
""")
     

with st.expander("When will the takeoff references automatically be removed?"):
     st.write(f"""
- {hightlight}[**Accelerating through 160 KIAS**] 
""")
     