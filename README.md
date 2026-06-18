# 🌿 NGO Resource Planning Dashboard

## 📌 Overview

This project is a Streamlit-based interactive dashboard designed to help NGOs analyze their operational data and generate optimized resource planning strategies.

It allows users to upload datasets, visualize insights, and receive intelligent suggestions for improving event planning efficiency.

---

## 🎯 Objective

* Analyze NGO activity data
* Provide insights through visualizations
* Suggest better planning strategies based on input
* Improve resource allocation decisions

---

## ⚙️ Features

### 📊 Data Analysis

* Dataset upload functionality
* Overview metrics:

  * Total activities
  * Average success rate
  * Total budget
* Interactive data table

---

### 📈 Visualizations

* Activity-wise success rate (Bar chart)
* Region-wise budget distribution (Horizontal bar chart)
* Budget vs Success Rate (Scatter plot)
* Priority distribution (Pie chart)

---

### 🧠 Smart Planning Tool

* User inputs:

  * Activity type
  * Region
  * Team size
  * Resources allocated
  * Budget

* System evaluates:

  * Plan score
  * Efficiency level

* Output:

  * Good Plan ✅
  * Moderate Plan ⚠
  * Bad Plan ❌

---

### 🚀 Plan Recommendation System

* Suggests improved plans when input is weak
* Provides:

  * Moderate upgrade plan
  * Best optimized plan
* Calculates improved scores dynamically

---

## 💡 Working Logic

The system calculates a score using:

* Team contribution
* Resource utilization
* Budget efficiency

Based on the score:

* High score → Good plan
* Medium score → Moderate plan
* Low score → Improvement suggestions

---

## 📂 Project Structure

```bash
planner_app.py      # Main Streamlit application
planner_data.csv    # Sample dataset
README.md           # Project documentation
```

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install streamlit pandas matplotlib
```

### 2. Run the application

```bash
python -m streamlit run planner_app.py
```

### 3. Open in browser

```
http://localhost:8501
```

---

## 🛠 Technologies Used

* Python
* Streamlit
* Pandas
* Matplotlib

---

## ✨ Conclusion

This project demonstrates how data analytics can assist NGOs in making smarter operational decisions and improving overall impact.

---
