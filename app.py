import streamlit as st
import requests
from prompts import generate_resume_prompt
from utils import create_pdf

st.title("🤖 AI Resume Writer (Local AI)")
st.write("Fill your details below 👇")

# ----------- HELPER FUNCTION -----------

def validate_phone(phone):
    digits = "".join(filter(str.isdigit, phone))
    if len(digits) != 10:
        return None
    return digits

# ----------- USER INPUTS (ORDER FIXED) -----------

# 1. Full Name
name = st.text_input("Full Name")

# 2. Contact Number
phone = st.text_input("Contact Number")

# Live warning
if phone and not phone.isdigit():
    st.warning("⚠️ Only numbers are allowed")

# 3. Email
email = st.text_input("Email Address")

# 4. Education
education = st.text_area("Education Details")
# Checkbox
is_student = st.checkbox("Currently pursuing")
# 5. College Name
college = st.text_input("College Name")

# 6. Skills
skills = st.text_area("Skills (comma separated)")

# . Projects
projects = st.text_area("Projects (describe your work)")

# 8. LinkedIn
linkedin = st.text_input("LinkedIn Profile URL")

# 9. GitHub
github = st.text_input("GitHub Profile URL")


resume = ""

# ----------- GENERATE RESUME -----------

if st.button("Generate Resume"):

    # Validate phone
    formatted_phone = validate_phone(phone)

    if not formatted_phone:
        st.error("❌ Please enter a valid 10-digit phone number (numbers only)")

    elif not name or not email:
        st.error("❌ Name and Email are required")

    else:
        prompt = generate_resume_prompt(
            name, formatted_phone, email, linkedin, github,
            college, education, is_student,
            skills, projects
        )

        try:
            response = requests.post(
                API_KEY-your-secret-key,
                json={
                    "model": "google/gemma-3-1b",
                    "messages": [
                        {"role": "user", "content": prompt}
                    ],
                    "temperature": 0.7,
                    "max_tokens": 800
                }
            )

            result = response.json()
            resume = result["choices"][0]["message"]["content"]

            st.subheader("📄 Your Resume")
            st.write(resume)

        except Exception as e:
            st.error("Error: " + str(e))
            st.write(response.text)

# ----------- DOWNLOAD PDF -----------

if resume:
    pdf = create_pdf(resume)
    st.download_button("📥 Download Resume", pdf, "resume.pdf")
