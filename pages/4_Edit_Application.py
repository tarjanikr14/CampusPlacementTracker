
import streamlit as st
from datetime import date

from database import get_applications, update_application
from theme import apply_theme

apply_theme()

st.title("✏️ Edit Application")
st.caption("Update the details of an existing company application.")

st.divider()

applications = get_applications()

if applications:
    application_options = {app["id"]: app for app in applications}

    selected_id = st.selectbox(
        "Select application",
        options=list(application_options.keys()),
        format_func=lambda x: (
            application_options[x]["company_name"]
            + " - "
            + application_options[x]["job_role"]
        )
    )

    selected_app = application_options[selected_id]

    with st.form("edit_application_form"):

        company = st.text_input(
            "Company Name",
            value=selected_app["company_name"]
        )

        role = st.text_input(
            "Job Role",
            value=selected_app["job_role"]
        )

        col1, col2 = st.columns(2)

        with col1:
            package = st.number_input(
                "Package (LPA)",
                min_value=0.0,
                value=float(selected_app["package"]),
                step=0.5
            )

        with col2:
            application_date = st.date_input(
                "Application Date",
                value=date.fromisoformat(
                    selected_app["application_date"]
                )
            )

        status_options = [
            "Applied",
            "Shortlisted",
            "Interview Scheduled",
            "Selected",
            "Rejected"
        ]

        current_status = selected_app["status"]

        status = st.selectbox(
            "Application Status",
            status_options,
            index=status_options.index(current_status)
        )

        submitted = st.form_submit_button(
            "Save Changes",
            use_container_width=True
        )

        if submitted:
            if company.strip() and role.strip():

                try:
                    update_application(
                        selected_id,
                        company.strip(),
                        role.strip(),
                        package,
                        application_date,
                        status
                    )

                    st.success("Application updated successfully!")

                except Exception as e:
                    st.error(f"Unable to update application: {e}")

            else:
                st.warning(
                    "Company name and job role cannot be empty."
                )

else:
    st.info("No applications available. Add an application first.")
