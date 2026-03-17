import numpy as np
import matplotlib.pyplot as plt

print("Inventory Management Model\n")

try:
    
    daily_demand = float(input("Enter daily demand: "))
    lead_time = float(input("Enter lead time (days): "))
    demand_std = float(input("Enter demand standard deviation: "))
    service_level_z = float(input("Enter Z value (e.g., 1.65 for 95%): "))

    
    if daily_demand < 0 or lead_time < 0 or demand_std < 0:
        raise ValueError("Inputs must be non-negative.")

    
    demand_during_lead_time = daily_demand * lead_time
    safety_stock = service_level_z * demand_std * np.sqrt(lead_time)
    rop = demand_during_lead_time + safety_stock

    
    print("\n--- RESULTS ---")
    print(f"Demand during lead time: {round(demand_during_lead_time, 2)}")
    print(f"Safety Stock: {round(safety_stock, 2)}")
    print(f"Reorder Point (ROP): {round(rop, 2)}")

    
    days = np.arange(1, 31)
    simulated_demand = np.random.normal(daily_demand, demand_std, 30)

    
    plt.figure()
    plt.plot(days, simulated_demand, marker='o')
    plt.axhline(y=rop, linestyle='--')

    plt.title("Daily Demand vs Reorder Point")
    plt.xlabel("Days")
    plt.ylabel("Demand")
    plt.legend(["Demand", "Reorder Point"])
    plt.grid()

    plt.show()

except ValueError as e:
    print("\n⚠️ Error:", e)
    print("Please enter valid numeric values.")
