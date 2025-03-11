import streamlit as st
import re

st.set_page_config(page_title="Monster's Password Lab", page_icon="👾")

st.title("Monster's Password Lab 👾")
st.markdown("""
Where friendly monsters turn your mild passwords into mighty fortresses! 🔐
""")

password = st.text_input("Enter your password", type="password")
feedback = []

score = 0
if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❗ Password must be at least 8 characters long")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❗ Password must contain upper and lower case characters")
    
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❗ Password must contain at least one digit")
    
    if re.search(r'[!@#$%^&*()]', password):
        score += 1
    else:
        feedback.append("❗ Password must contain at least one special character (!@#$%^&*())")
    
    if score == 4:
        feedback.append("✅ Your Password Is Strong!")
    elif score == 3:
        feedback.append("🟡 Your Password Is Medium, It Could be Stronger!")
    else:
        feedback.append("🔴 Your Password Is Mild , Make it Mighty!")

    if feedback:
        st.markdown("## TIPS:")

for Tip in feedback:
    st.write(Tip)
else:
    st.info("Please Enter Your Password To Continue.")


    st.write("Made with 👾 by Shiree")



    
        



       