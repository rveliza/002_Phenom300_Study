import streamlit as st

hightlight = ":orange-background"
cols_settings = [20, 80]


st.title("Regulations")
st.write("#### RVSM")


with st.expander("Where is the data required to operate in RVSM?"):
     st.write(f"""
- {hightlight}[**AFM Supplements**] 
""")
     

with st.expander("What is needed to operate in RVSM?"):
     st.write(f"""
- {hightlight}[**Two RVSM compiant ADS**] 
- {hightlight}[**One Autopilot with altitude hold mode**] 
- {hightlight}[**One Altitude alerter**] 
- {hightlight}[**One transponder**] 
""")
     

with st.expander("What is the maximum difference between the two primary altimeters for RVSM?"):
     st.write(f"""
- {hightlight}[**75 ft**] 
""")
     

with st.expander("Can the IESI be used for RVSM?"):
     st.write(f"""
- {hightlight}[**NO**] 
""")
     

with st.expander("Altitude Check Procedure"):
     st.write(f"""
- {hightlight}[**Set QNH and should display known elevation. 75ft of elevation**] 
- {hightlight}[**Upon reaching cruising altitude, at intervals not exceeding 1hr. Crosscheck between 2 primary alts.  No more than 200 feet difference**] 
- {hightlight}[**Notes should be done in flight plan.**] 
""")
     


