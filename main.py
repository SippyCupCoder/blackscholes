import streamlit as st
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

from blackScholes import BlackScholes

blackScholes = BlackScholes()

blackScholes.s = st.number_input(
    "Stock price", min_value=0, value=100, placeholder="Type a number..."
)

blackScholes.k = st.number_input(
    "Strike price", min_value=0, value=100, placeholder="Type a number..."
)

blackScholes.t = st.number_input(
    "Time to expiration", min_value=0, value=1, placeholder="Type a number..."
)

blackScholes.v = st.number_input(
    "Volatility", min_value=0.0, max_value=1.0, value=0.01, placeholder="Type a number..."
)


blackScholes.r = st.number_input(
    "Interest rate", min_value=0.0, value=0.01, placeholder="Type a number..."
)

st.write(blackScholes.calculateCallPrice())
st.write(blackScholes.calculatePutPrice())

minStrikePrice = st.number_input(
    "Min Strike Price", min_value=0.0, value=50.0, placeholder="Type a number..."
)
maxStrikePrice = st.number_input(
    "Max Strike Price", min_value=minStrikePrice, value=150.0, placeholder="Type a number..."
)
strikePriceRange = np.linspace(minStrikePrice, maxStrikePrice, blackScholes.size)

volatilitySlider = st.slider(
    "Volatility:", min_value=0.0, max_value=1.0, value=(0.0, 1.0)
)
volatilityRange = np.linspace(volatilitySlider[0], volatilitySlider[1], blackScholes.size)

blackScholes.calculateCallHeatMap(strikePriceRange, volatilityRange)
blackScholes.calculatePutHeatMap(strikePriceRange, volatilityRange)

callMap, axisCall = plt.subplots(figsize=(10, 8))
sns.heatmap(blackScholes.callHeatMap, xticklabels=np.round(strikePriceRange, 2), yticklabels=np.round(volatilityRange, 2), annot=True, ax=axisCall)
axisCall.set_title("Call")
axisCall.set_xlabel("Strike Price")
axisCall.set_ylabel("Volatility")

putMap, axisPut = plt.subplots(figsize=(10,8))
sns.heatmap(blackScholes.putHeatMap, xticklabels=np.round(strikePriceRange, 2), yticklabels=np.round(volatilityRange, 2), annot=True, ax=axisPut)
axisPut.set_title("Put")
axisPut.set_xlabel("Strike Price")
axisPut.set_ylabel("Volatility")

st.pyplot(callMap)
st.pyplot(putMap.get_figure())