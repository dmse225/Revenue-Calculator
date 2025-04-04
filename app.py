import streamlit as st

def calculate_revenue_impact(base_fees, visit_volumes, incentive_percent):
    total_impact = sum((fee * (incentive_percent / 100)) * volume for fee, volume in zip(base_fees, visit_volumes))
    return total_impact

# Streamlit UI
st.title("Healthcare Revenue Impact Calculator")
st.write("Calculate the total revenue impact of an incentive adjustment.")

# User Inputs
base_fees = st.text_input("Enter base fees (comma-separated):", "75, 200, 100")
visit_volumes = st.text_input("Enter visit volumes (comma-separated):", "1500, 2000, 1800")
incentive_percent = st.number_input("Enter incentive percent:", min_value=0.0, max_value=100.0, value=10.0)

# Convert inputs to lists
try:
    base_fees = [float(x.strip()) for x in base_fees.split(",")]
    visit_volumes = [int(x.strip()) for x in visit_volumes.split(",")]

    if len(base_fees) == len(visit_volumes):
        total_revenue_impact = calculate_revenue_impact(base_fees, visit_volumes, incentive_percent)
        st.success(f"Total Revenue Impact: ${total_revenue_impact:,.2f}")
    else:
        st.error("Error: Base fees and visit volumes must have the same number of values.")
except ValueError:
    st.error("Please enter valid numbers for base fees and visit volumes.")
