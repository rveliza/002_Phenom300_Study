import streamlit as st

fuel_arms = {
    50: 256.38,
    100: 256.02,
    150: 255.64,
    200: 255.32,
    250: 255.07,
    300: 254.84,
    350: 254.66,
    400: 254.51,
    450: 254.38,
    500: 254.27,
    550: 254.22,
    600: 254.20,
    650: 254.19,
    700: 254.25,
    750: 254.30,
    800: 254.38,
    850: 254.50,
    900: 254.64,
    950: 254.80,
    1000: 254.94,
    1050: 255.11,
    1100: 255.29,
    1150: 255.46,
    1200: 255.61,
    1250: 255.83,
    1300: 256.02,
    1350: 256.19,
    1400: 256.38,
    1450: 256.53,
    1500: 256.71,
    1550: 256.90,
    1600: 257.06,
    1650: 257.26,
    1700: 257.40,
    1750: 257.61,
    1800: 257.80,
    1850: 257.96,
    1900: 258.20,
    1950: 258.37,
    2000: 258.62,
    2050: 258.83,
    2100: 259.04,
    2150: 259.32,
    2200: 259.55,
    2250: 259.78,
    2300: 260.00,
    2350: 260.24,
    2400: 260.48,
    2450: 260.76,
    2500: 261.01,
    2550: 261.28,
    2600: 261.48,
    2650: 261.77,
    2700: 262.05,
    2750: 262.26,
    2800: 262.54,
    2850: 262.76,
    2900: 263.06,
    2950: 263.28,
    3000: 263.58,
    3050: 263.80,
    3100: 264.05,
    3150: 264.36,
    3200: 264.59,
    3250: 264.82,
    3300: 265.05,
    3350: 265.39,
    3400: 265.62,
    3450: 265.86,
    3500: 266.08,
    3550: 266.34,
    3600: 266.57,
    3650: 266.83,
    3700: 267.08,
    3750: 267.32,
    3800: 267.56,
    3850: 267.79,
    3900: 268.05,
    3950: 268.29,
    4000: 268.54,
    4050: 268.79,
    4100: 269.03,
    4150: 269.28,
    4200: 269.52,
    4250: 269.76,
    4300: 269.92,
    4350: 270.16,
    4400: 270.31,
    4450: 270.32,
    4500: 270.88,
    4550: 271.12,
    4600: 271.35,
    4650: 271.6,
    4700: 271.83,
    4750: 272.08,
    4800: 272.34,
    4850: 272.57,
    4900: 272.80,
    4950: 273.12,
    5000: 273.36,
    5050: 273.68,
    5100: 273.99,
    5150: 274.29,
    5200: 274.67,
    5250: 275.03,
    5300: 275.39,
    5350: 275.73,
    5400: 275.73,
    5450: 275.73
}


def get_cg(moment, weight):
    arm = moment / weight
    return round((arm - 264.51) * 100 / 80.71, 1)

def get_fuel_rnd_50(number):
    number -= 1
    return (number//50)*50+50


BEW_WEIGHT = 11354
BEW_ARM = 302.36
FWD_BAG_ARM = 39.37
BEW_MOMENT = BEW_WEIGHT * BEW_ARM
PILOT_COPILOT_ARM = 104.33
LH_FWD_CABINET_ARM = 135.83
RH_REFRESH_CTR_ARM = 146.06
PAX_1_2_ARM = 196.06
PAX_3_4_ARM = 239.76
PAX_5_6_ARM = 281.89
LAV_PAX_ARM = 318.11
LAV_CAB_ARM = 318.11
AFT_BAG_ARM = 396.85


with st.expander(f"Weight and Balance aircraft with BEW of {BEW_WEIGHT} lbs."):
    col1, col2, col3 = st.columns(3, gap="large", vertical_alignment="top")

    with col1:
        fwd_bag_weight =  st.number_input("Fwd Bag (110 max)", min_value=0, max_value=110, value=0, step=5)
        fwd_bar_moment = fwd_bag_weight * FWD_BAG_ARM
        
        pilot_copilot_weight = st.number_input("Pilot and Copilot", min_value=0, value=400, step=5)
        pilot_copilot_moment = pilot_copilot_weight * PILOT_COPILOT_ARM
        
        lh_fwd_cabinet_weight = st.number_input("LH FWD Cab(44 max)", min_value=0, max_value=44, value=40, step=1)
        lh_fwd_cabinet_moment = lh_fwd_cabinet_weight * LH_FWD_CABINET_ARM
        
        rh_refresh_ctr_weight = st.number_input("RH Refresh. Ctr (71 max)", min_value=0, max_value=71, value=0, step=1)
        rh_refresh_ctr_moment = rh_refresh_ctr_weight * RH_REFRESH_CTR_ARM
        
        pax_1_2_weight = st.number_input("Pax 1 and 2", min_value=0, value=400, step=5)
        pax_1_2_moment = pax_1_2_weight * PAX_1_2_ARM

    with col2:
        pax_3_4_weight = st.number_input("Pax 3 and 4", min_value=0, value=200, step=5)
        pax_3_4_moment = pax_3_4_weight * PAX_3_4_ARM
        
        pax_5_6_weight = st.number_input("Pax 5 and 6", min_value=0, value=0, step=5)
        pax_5_6_moment = pax_5_6_weight * PAX_5_6_ARM
        
        lav_pax_weight = st.number_input("Lav (passenger)", min_value=0, value=0, step=5)
        lav_pax_moment = lav_pax_weight * LAV_PAX_ARM
        
        lav_cab_weight = st.number_input("Lav Cab (33 max)", min_value=0, max_value=33, value=0, step=1)
        lav_cab_moment = lav_cab_weight * LAV_CAB_ARM
        
        aft_bag_weight = st.number_input("Aft Bag (463 max)", min_value=0, max_value=463, value=100, step=1)
        aft_bag_moment = aft_bag_weight * AFT_BAG_ARM
        
        zero_fuel_weight = BEW_WEIGHT + fwd_bag_weight + pilot_copilot_weight + lh_fwd_cabinet_weight + rh_refresh_ctr_weight + pax_1_2_weight + pax_3_4_weight + pax_5_6_weight + lav_cab_weight + lav_pax_weight + aft_bag_weight
        zero_fuel_moment = BEW_MOMENT + fwd_bar_moment + pilot_copilot_moment + lh_fwd_cabinet_moment + rh_refresh_ctr_moment + pax_1_2_moment + pax_3_4_moment + pax_5_6_moment + lav_cab_moment + lav_pax_moment + aft_bag_moment
        zero_fuel_cg = get_cg(zero_fuel_moment, zero_fuel_weight)
    
    with col3:
        ramp_fuel = st.number_input("Ramp Fuel", min_value=300, 
                                    max_value=5401, value=4000, step=10)
        ramp_weight = zero_fuel_weight + ramp_fuel
        
        taxi_fuel = st.number_input("Taxi Fuel", min_value=0, 
                                    value=55, step=5)
        take_off_fuel = ramp_fuel - taxi_fuel

        fuel_rnd_50 = get_fuel_rnd_50(take_off_fuel)
        take_off_fuel_arm = fuel_arms[fuel_rnd_50]
        st.write(f"Takeoff fuel arm: {take_off_fuel_arm}")
        take_off_fuel_moment = take_off_fuel * take_off_fuel_arm
        take_off_moment = zero_fuel_moment + take_off_fuel_moment
        take_off_weight = zero_fuel_weight + take_off_fuel
        take_off_cg = get_cg(take_off_moment, take_off_weight)
        
        land_fuel_weight = st.number_input("Est. Land fuel", min_value=0, 
                                           max_value=5401, value=2000, step=10)
        land_weight = zero_fuel_weight + land_fuel_weight
        
        land_fuel_rnd_50 = get_fuel_rnd_50(land_fuel_weight)
        land_fuel_arm = fuel_arms[land_fuel_rnd_50]
        st.write(f"Landing fuel arm: {land_fuel_arm}")
        land_fuel_moment = land_fuel_weight * land_fuel_arm
        land_moment = zero_fuel_moment + land_fuel_moment
        land_cg = get_cg(land_moment, land_weight)
        
      

c = {
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "description": "A simple bar chart with embedded data.",
  "width": 350,
  "height": 600,
 
  "layer": [
    {
      "data": {
        "values": [
          {"a": 36, "b": 11354, "c": 42, "d": 11354},
          {"a": 42, "b": 11354, "c": 38.8, "d": 14220},
          {"a": 38.8, "b": 14220, "c": 31.3, "d": 18387},
          {"a": 31.3, "b": 18387, "c": 31.3, "d": 18497},
          {"a": 31.3, "b": 18497, "c": 19.4, "d": 18497},
          {"a": 19.4, "b": 18497, "c": 19.4, "d": 18387},
          {"a": 38.8, "b": 14220, "c": 34.3, "d": 18387},  #
          {"a": 34.2, "b": 18387, "c": 17, "d": 18387},  #
          {"a": 17, "b": 18387, "c": 17, "d": 15102},  #
          {"a": 17, "b": 15102, "c":25, "d": 12346},  #
          {"a": 31.3, "b": 18387, "c": 19.4, "d": 18387},
          {"a": 19.4, "b": 18387, "c": 19, "d": 17968},
          {"a": 19, "b": 17968, "c": 19, "d": 15102},
          {"a": 19, "b": 15102, "c": 25, "d": 12346},
          {"a": 25, "b": 12346, "c": 36, "d": 11354}
        ]
      },
      "mark": "rule",
      "encoding": {
        "x": {"field": "a", 
              "type": "quantitative", 
              "axis": {
                "labelAngle": 0,
                "labelColor": "blue",
                "ticks": True,
                "tickColor": "orange",
                "tickCount": 9
                },
              "scale": {"domain": [10, 50]}
                },
        "y": {"field": "b", 
              "type": "quantitative",
              "scale":{"domain": [10000, 19200]}},
        "x2": {"field": "c", "type": "quantitative"},
        "y2": {"field": "d", "type": "quantitative"}
      }

    },
    {
      "data": {
        "values": [
          {"cg": take_off_cg, "lbs": take_off_weight},
          {"cg": land_cg, "lbs": land_weight},
          {"cg": zero_fuel_cg, "lbs": zero_fuel_weight}
        ]
      },
      "mark": "point",
      "encoding": {
        "x": {"field": "cg", "type": "quantitative", "axis": {"labelAngle": 0}},
        "y": {"field": "lbs", "type": "quantitative"}
      }
    }
  ]
}

st.vega_lite_chart(c)