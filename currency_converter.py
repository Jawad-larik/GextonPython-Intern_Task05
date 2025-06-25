import streamlit as st
import requests
from datetime import datetime

API_URL = "https://api.exchangerate-api.com/v4/latest/"
API_KEY = "a68f87a4eb2ee173415a2054"

def fetch_exchange_rate(from_currency):
    try:
        resp = requests.get(API_URL + from_currency)
        resp.raise_for_status()
        return resp.json()["rates"]
    except requests.RequestException as e:
        st.error(f"Error fetching rates: {e}")
        return None

def log_conversion(amount, from_curr, to_curr, converted_amount):
    with open("conversion_log.txt", "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp}: {amount} {from_curr} = {converted_amount:.2f} {to_curr}\n")

st.set_page_config(page_title="Currency Converter", page_icon="💱")
st.title("💱 Real-Time Currency Converter")

amount = st.text_input("Amount:", "")
from_currency = st.selectbox(
    "From Currency:",
    ["USD", "EUR", "GBP", "PKR", "INR"],
)
to_currency = st.selectbox(
    "To Currency:",
    ["USD", "EUR", "GBP", "PKR", "INR"],
)

col1, col2 = st.columns(2)
with col1:
    convert_btn = st.button("Convert", use_container_width=True)
with col2:
    clear_btn = st.button("Clear", use_container_width=True)

converted_amount = None

if convert_btn:
    try:
        amount = float(amount)
        rates = fetch_exchange_rate(from_currency)
        if rates and to_currency in rates:
            rate = rates[to_currency]
            converted_amount = amount * rate
            st.success(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
            log_conversion(amount, from_currency, to_currency, converted_amount)
        else:
            st.error("Conversion failed. Check your currency codes.")
    except ValueError:
        st.error("Please enter a valid number.")

st.subheader("Conversion History Log")
if st.button("Refresh Log"):
    try:
        with open("conversion_log.txt") as f:
            log_content = f.read()
            st.text_area("", log_content, height=200)
    except FileNotFoundError:
        st.warning("No log file found yet!")

if clear_btn:
    st.rerun()