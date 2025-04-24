import streamlit as st
import re

st.set_page_config(page_title="Password Strength Meter", page_icon="🔒")
st.title("🔒 Password Strength Meter")
st.markdown("""
## Welcome to the Ultimate Password Strength Meter! 👏
Use this app to check the strength of your password.
""")

password = st.text_input("Enter your password", type="password")

feedback = []
score = 0

if password:
    # Check length
    if len(password) >= 8:
        feedback.append("✅ Password is at least 8 characters long")
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long")
    
    # Check case
    if re.search(r'[a-z]', password) and re.search(r'[A-Z]', password):
        feedback.append("✅ Password contains both lowercase and uppercase characters")
        score += 1
    else:
        feedback.append("❌ Password should contain both lowercase and uppercase characters")
    
    # Check numbers
    if re.search(r'\d', password):
        feedback.append("✅ Password contains numbers")
        score += 1
    else:
        feedback.append("❌ Password should contain numbers")
    
    # Check special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        feedback.append("✅ Password contains special characters")
        score += 1
    else:
        feedback.append("❌ Password should contain special characters")
    
    # Display strength assessment
    st.markdown("### Password Strength:")
    for fb in feedback:
        st.write(fb)
    
    # Display overall strength
    if score == 4:
        st.success("Password is Strong! 💪")
    elif score == 3:
        st.warning("Password is Medium 🤔")
    else:
        st.error("Password is Weak 😟")
else:
    st.info("Enter your password to get started")
