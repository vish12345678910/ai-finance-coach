import streamlit as st

st.set_page_config(page_title="AI Finance Coach", layout="centered")

st.title("🏠 AI-Powered Property Finance Coach")
st.markdown("""
Welcome to your smart assistant for deal analysis. Answer questions like:
- What rent do I need for a 10% ROI?
- What property price ensures no money left in the deal?

Clean. Fast. Accurate.
""")

st.header("🔢 Calculate Required Rent for Target ROI")
total_investment = st.number_input("Total Investment (£)", value=46000)
annual_expenses = st.number_input("Annual Expenses (£)", value=4000)
target_roi = st.number_input("Target ROI (%)", value=10.0)

if st.button("Calculate Required Rent"):
    annual_cash_flow_required = total_investment * (target_roi / 100)
    required_annual_rent = annual_cash_flow_required + annual_expenses
    required_monthly_rent = required_annual_rent / 12
    st.success(f"You need at least £{required_monthly_rent:,.2f} in monthly rent for a {target_roi}% ROI.")

st.header("🏷️ Max Purchase Price (No Money Left In Deal)")
refinance_value = st.number_input("Refinance Value (£)", value=130000)
refurb_costs = st.number_input("Refurbishment Costs (£)", value=15000)
fees = st.number_input("Other Fees (£)", value=6000)
deposit_percent = st.slider("Deposit Percentage (%)", min_value=10, max_value=50, value=25)
refi_ltv = st.slider("Refinance LTV (%)", min_value=60, max_value=85, value=75)

if st.button("Calculate Max Purchase Price"):
    cash_from_refi = refinance_value * (refi_ltv / 100)
    max_total_investment = cash_from_refi
    effective_rate = 1 + (deposit_percent / 100) * (1 / (1 - deposit_percent / 100))
    max_purchase_price = (max_total_investment - refurb_costs - fees) / effective_rate
    st.success(f"You should pay no more than £{max_purchase_price:,.2f} to leave no money in the deal.")
