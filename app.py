import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("📦 Inventory Management Model")

st.write("Calculate Reorder Point (ROP) and Safety Stock dynamically.")

# Inputs
daily_demand = st.number_input("Daily Demand", min_value=0.0, value=200.0)
lead_time = st.number_input("Lead Time (days)", min_value=0.0, value=6.0)
demand_std = st.number_input("Demand Standard Deviation", min_value=0.0, value=4.0)
service_level_z = st.number_input("Z Value (e.g., 1.65 for 95%)", value=1.65)

# Button
if st.button("Calculate"):

    # Calculations
    demand_during_lead_time = daily_demand * lead_time
    safety_stock = service_level_z * demand_std * np.sqrt(lead_time)
    rop = demand_during_lead_time + safety_stock

    st.subheader("Results")
    st.write(f"Demand during lead time: {round(demand_during_lead_time, 2)}")
    st.write(f"Safety Stock: {round(safety_stock, 2)}")
    st.write(f"Reorder Point (ROP): {round(rop, 2)}")

    # 🔥 FIXED SIMULATION (IMPORTANT)
    days = np.arange(1, 31)

    simulated_demand = np.random.normal(
        daily_demand * lead_time,
        demand_std * np.sqrt(lead_time),
        30
    )

    # Plot
    fig, ax = plt.subplots()
    ax.plot(days, simulated_demand, marker='o')
    ax.axhline(y=rop, linestyle='--')

    ax.set_title("Lead Time Demand vs Reorder Point")
    ax.set_xlabel("Days")
    ax.set_ylabel("Demand")

    ax.legend(["Lead Time Demand", "Reorder Point"])
    ax.grid()

    st.pyplot(fig)
