import numpy as np

# Parameters
daily_demand = 20
lead_time = 5
demand_std = 4
service_level_z = 1.65  # 95% service level

# Calculations
demand_during_lead_time = daily_demand * lead_time
safety_stock = service_level_z * demand_std * np.sqrt(lead_time)
rop = demand_during_lead_time + safety_stock

print("Demand during lead time:", demand_during_lead_time)
print("Safety Stock:", round(safety_stock, 2))
print("Reorder Point (ROP):", round(rop, 2))
