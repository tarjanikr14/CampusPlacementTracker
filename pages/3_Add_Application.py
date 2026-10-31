
import streamlit as st
from datetime import date

from database import add_application
from theme import apply_theme

apply_theme()

st.title("➕ Add New Application")
st.caption("Record a new company application.")

st.divider()

with st.form("application_form"):
    company = st.text_input("Company Name")
    role = st.text_input("Job Role")

    col1, col2 = st.columns(2)

    with col1:
        package = st.number_input(
            "Package (LPA)",
            min_value=0.0,
            step=0.5
        )

    with col2:
        application_date = st.date_input(
            "Application Date",
            value=date.today()
        )

    status = st.selectbox(
        "Application Status",
        [
            "Applied",
            "Shortlisted",
            "Interview Scheduled",
            "Selected",
            "Rejected"
        ]
    )

    submitted = st.form_submit_button(
        "Add Application",
        use_container_width=True
    )

    if submitted:
        if company.strip() and role.strip():
            add_application(
                company.strip(),
                role.strip(),
                package,
                application_date,
                status
            )

            st.success("Application added successfully!")
        else:
            st.warning("Please enter both company name and job role.")
