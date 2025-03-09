

import re
import streamlit as st

st.set_page_config(page_title="Password Strength Meter", layout="wide")
st.title("🔒 Password Strength Meter")

st.markdown(""" 
<style> 
    .main {text-align: center;} 
    .stTextInput {width: 60% !important; margin:auto;}
    .stButton button {width: 50%; background-color: #4CAF50; color: white; font-size: 18px;}
    .stButton button:hover {background-color: white;}    
</style>
""", unsafe_allow_html=True)

st.write("Enter your Password below:")

# User input
password = st.text_input("Enter Your Password", type="password", help="Ensure your password is strong")

# Function to check password strength
def password_strength_checker(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Check uppercase & lowercase letters
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Check for numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Check for special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Strength rating
    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.info("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.error("❌ Weak Password - Improve it using the suggestions below.")

    # Feedback for improvement
    if feedback:
        with st.expander("**Improve Your Password**"):
            for item in feedback:
                st.write(item)

# Button to check password strength
if st.button("Check Strength"):
    if password:
        password_strength_checker(password)  # Fixed function call
    else:
        st.warning("⚠️ Please enter a password first!")
