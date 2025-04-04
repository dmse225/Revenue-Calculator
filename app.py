import streamlit as st

# Function to calculate revenue
def calculate_revenue(base_fees, visit_volumes, incentive_percent):
    revenue = sum((fee + (fee * (incentive_percent / 100))) * volume for fee, volume in zip(base_fees, visit_volumes))
    return revenue

# Streamlit UI
st.title("Healthcare Revenue Change Calculator")
st.write("Calculate the change in revenue due to a change in value-based program incentives.")

# User Inputs
base_fees = st.text_input("Enter base fees for E&M codes (comma-separated):", "75, 200, 100")
visit_volumes = st.text_input("Enter visit volumes for each E&M code (comma-separated):", "1500, 2000, 1800")
last_year_incentive = st.number_input("Enter last year's incentive percentage:", min_value=0.0, max_value=100.0, value=10.0)
this_year_incentive = st.number_input("Enter this year's projected incentive percentage:", min_value=0.0, max_value=100.0, value=5.0)

# Convert inputs to lists
try:
    base_fees = [float(x.strip()) for x in base_fees.split(",")]
    visit_volumes = [int(x.strip()) for x in visit_volumes.split(",")]

    if len(base_fees) == len(visit_volumes):
        # Calculate revenues
        last_year_revenue = calculate_revenue(base_fees, visit_volumes, last_year_incentive)
        this_year_revenue = calculate_revenue(base_fees, visit_volumes, this_year_incentive)
        revenue_change = this_year_revenue - last_year_revenue
        revenue_change_percent = (revenue_change / last_year_revenue) * 100

        # Display results
        st.success(f"Last Year's Revenue: ${last_year_revenue:,.2f}")
        st.success(f"This Year's Revenue: ${this_year_revenue:,.2f}")
        st.info(f"Change in Revenue: ${revenue_change:,.2f} ({revenue_change_percent:.2f}%)")
    else:
        st.error("Error: Base fees and visit volumes must have the same number of values.")
except ValueError:
    st.error("Please enter valid numbers for base fees and visit volumes.")
