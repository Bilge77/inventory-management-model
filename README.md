# 📦 Inventory Management Model

Interactive Inventory Optimization Tool built with Python & Streamlit

This project demonstrates an inventory management system using Reorder Point (ROP) and Safety Stock calculations, enhanced with an interactive web application.

---

## Live Web App
You can try the interactive version here:  
https://inventory-management-model-5wymchtrhtnlitnfnczouk.streamlit.app/

---

## Objective
To determine when to reorder products based on demand variability and lead time, helping reduce stockouts and excess inventory.

---

## Features
- Interactive user inputs (web app)
- Reorder Point (ROP) calculation
- Safety Stock calculation
- Demand simulation based on lead time
- Visualization with dynamic graph
- Command-line & web-based usage

---

##  Model Explanation

- Daily Demand = 20 units  
- Lead Time = 5 days  
- Demand Standard Deviation = 4  
- Service Level = 95%  

---

## Formulas

ROP = (Demand × Lead Time) + Safety Stock  
Safety Stock = Z × σ × √Lead Time  

---

## Output Example

- Demand during lead time: 100  
- Safety Stock: ~14.75  
- Reorder Point: ~114.75  

---

## Visualization
The model includes a simulation of demand over the lead time and compares it with the reorder point to support decision-making.

---

## Business Value
This tool helps businesses optimize inventory decisions by balancing service level and demand variability, reducing both stockout risks and holding costs.

---

## How to Run Locally

1. Install dependencies:
```bash
pip install -r requirements.txt
