import streamlit as st

st.set_page_config(page_title="Cute Bold Calculator 💖", page_icon="🧮")

st.markdown("<h1 style='text-align:center; color:#e91e63;'>💖 Cute + Bold Calculator 💖</h1>", unsafe_allow_html=True)

# Input fields
a = st.text_input("Column A:")
b = st.text_input("Column B:")

# Result placeholder
result_placeholder = st.empty()

# Function to compute
def compute(op):
    try:
        a_val = float(a)
        b_val = float(b)

        if op == "add":
            res = a_val + b_val
        elif op == "sub":
            res = a_val - b_val
        elif op == "mul":
            res = a_val * b_val
        elif op == "div":
            if b_val == 0:
                return "❌ Can't divide by 0"
            res = a_val / b_val

        return int(res) if res == int(res) else round(res, 4)
    except:
        return "❌ Invalid input"

# Buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("➕ Add"):
        result_placeholder.success(f"Result: {compute('add')}")
    if st.button("✖ Multiply"):
        result_placeholder.success(f"Result: {compute('mul')}")

with col2:
    if st.button("➖ Subtract"):
        result_placeholder.success(f"Result: {compute('sub')}")
    if st.button("➗ Divide"):
        result_placeholder.success(f"Result: {compute('div')}")

# Footer
st.markdown("<hr><center>Made with 💖 by Tejaswani</center>", unsafe_allow_html=True)
