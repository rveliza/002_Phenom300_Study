import streamlit as st
import altair as alt
import pandas as pd
import numpy as np

from altair import vegalite as alt


def get_cg(moment, weight):
    arm = moment / weight
    return round((arm - 264.51) * 100 / 80.71, 1)


BEW_WEIGHT = 11354
BEW_ARM = 302.36
BEW_MOMENT = BEW_WEIGHT * BEW_ARM

with st.expander("Weight and Balance"):
    col1, col2, col3 = st.columns(3, gap="large", vertical_alignment="top")

    with col1:
        fwd_bag_weight =  st.number_input("Fwd Bag (110 max)", min_value=0, max_value=110, value=0, step=5)
        pilot_copilot_weight = st.number_input("Pilot and Copilot", min_value=0, value=400, step=5)
        lh_fwd_cabinet_weight = st.number_input("LH FWD Cab(44 max)", min_value=0, max_value=44, value=40, step=1)
        rh_refresh_ctr_weight = st.number_input("RH Refresh. Ctr (71 max)", min_value=0, max_value=71, value=0, step=1)
        pax_1_2_weight = st.number_input("Pax 1 and 2", min_value=0, value=400, step=5)

    with col2:
        pax_3_4_weight = st.number_input("Pax 3 and 4", min_value=0, value=200, step=5)
        pax_5_6_weight = st.number_input("Pax 5 and 6", min_value=0, value=0, step=5)
        lav_pax_weight = st.number_input("Lav (passenger)", min_value=0, value=0, step=5)
        lav_cab_weight = st.number_input("Lav Cab (33 max)", min_value=0, max_value=33, value=0, step=1)
        aft_bag_weight = st.number_input("Aft Bag (463 max)", min_value=0, max_value=463, value=100, step=1)
    
    with col3:
        ramp_fuel = st.number_input("Ramp Fuel", min_value=0, max_value=5401, value=4000, step=50)
        taxi_fuel = st.number_input("Taxi Fuel", min_value=0, value=55, step=5)
        take_off_fuel_arm = st.number_input("Takeoff Fuel Arm", min_value=256.38, max_value=275.73, value=268.29)
        land_fuel_weight = st.number_input("Est. Land fuel", min_value=0, max_value=5401, value=2000, step=50)
        land_fuel_arm =  st.number_input("Est. Land fuel arm",min_value=0.0, max_value=275.73, value=258.62)


FWD_BAG_ARM = 39.37
fwd_bar_moment = fwd_bag_weight * FWD_BAG_ARM
PILOT_COPILOT_ARM = 104.33
pilot_copilot_moment = pilot_copilot_weight * PILOT_COPILOT_ARM
LH_FWD_CABINET_ARM = 135.83
lh_fwd_cabinet_moment = lh_fwd_cabinet_weight * LH_FWD_CABINET_ARM
RH_REFRESH_CTR_ARM = 146.06
rh_refresh_ctr_moment = rh_refresh_ctr_weight * RH_REFRESH_CTR_ARM
PAX_1_2_ARM = 196.06
pax_1_2_moment = pax_1_2_weight * PAX_1_2_ARM
PAX_3_4_ARM = 239.76
pax_3_4_moment = pax_3_4_weight * PAX_3_4_ARM
PAX_5_6_ARM = 281.89
pax_5_6_moment = pax_5_6_weight * PAX_5_6_ARM
LAV_PAX_ARM = 318.11
lav_pax_moment = lav_pax_weight * LAV_PAX_ARM
LAV_CAB_ARM = 318.11
lav_cab_moment = lav_cab_weight * LAV_CAB_ARM
AFT_BAG_ARM = 396.85
aft_bag_moment = aft_bag_weight * AFT_BAG_ARM
zero_fuel_weight = BEW_WEIGHT + fwd_bag_weight + pilot_copilot_weight + lh_fwd_cabinet_weight + rh_refresh_ctr_weight + pax_1_2_weight + pax_3_4_weight + pax_5_6_weight + lav_cab_weight + lav_pax_weight + aft_bag_weight
zero_fuel_moment = BEW_MOMENT + fwd_bar_moment + pilot_copilot_moment + lh_fwd_cabinet_moment + rh_refresh_ctr_moment + pax_1_2_moment + pax_3_4_moment + pax_5_6_moment + lav_cab_moment + lav_pax_moment + aft_bag_moment
zero_fuel_cg = get_cg(zero_fuel_moment, zero_fuel_weight)
ramp_weight = zero_fuel_weight + ramp_fuel
take_off_fuel = ramp_fuel - taxi_fuel
take_off_fuel_moment = take_off_fuel * take_off_fuel_arm
take_off_weight = zero_fuel_weight + take_off_fuel
take_off_moment = zero_fuel_moment + take_off_fuel_moment
take_off_cg = get_cg(take_off_moment, take_off_weight)
land_fuel_moment = land_fuel_weight * land_fuel_arm
land_weight = zero_fuel_weight + land_fuel_weight
land_moment = zero_fuel_moment + land_fuel_moment
land_cg = get_cg(land_moment, land_weight)

c = {
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "description": "A simple bar chart with embedded data.",
  "width": 400,
  "height": 600,
 
  "layer": [
    {
      "data": {
        "values": [
          {"a": "36", "b": 11354, "c": 42, "d": 11354},
          {"a": "42", "b": 11354, "c": 38.8, "d": 14220},
          {"a": "38.8", "b": 14220, "c": 31.3, "d": 18387},
          {"a": "31.3", "b": 18387, "c": 19.4, "d": 18387},
          {"a": "19.4", "b": 18387, "c": 19, "d": 17968},
          {"a": "19", "b": 17968, "c": 19, "d": 15102},
          {"a": "19", "b": 15102, "c": 25, "d": 12346},
          {"a": "25", "b": 12346, "c": 36, "d": 11354}
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
          {"cg": "26.8", "lbs": 16439},
          {"cg": "28.1", "lbs": 14494},
          {"cg": "33.8", "lbs": 12494}
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