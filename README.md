# Inventory Management Model

This project demonstrates a basic inventory management system using Reorder Point (ROP) and Safety Stock calculations.

## Objective
To determine when to reorder products based on demand and lead time.

## Model Explanation

- Daily Demand = 20 units
- Lead Time = 5 days
- Demand Standard Deviation = 4
- Service Level = 95%

## Formulas

ROP = (Demand × Lead Time) + Safety Stock  
Safety Stock = Z × σ × √Lead Time

##  Output Example

- Demand during lead time: 100  
- Safety Stock: ~14.75  
- Reorder Point: ~114.75  

## Technologies
- Python
- NumPy

  ## Visualization
This model also includes a simulation of daily demand compared to the reorder point.

## Author
Bilge Yuluğ – Industrial Engineering Student
