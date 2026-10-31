
import streamlit as st
from datetime import date

from database import get_applications, add_interview
from theme import apply_theme

apply_theme()

st.title("📅 Schedule Interview")
st.caption("Schedule an interview for one of your company applications.")

st.divider()

# SUCCESS MESSAGE AFTER SCHEDULING

if st.session_state.get("interview_added"):
    st.success("Interview scheduled successfully!")
    st.session_state.interview_added = False

applications = get_applications()

if applications:
    application_options = {app["id"]: app for app in applications}

    with st.form("interview_form"):

        selected_application = st.selectbox(
            "Select Company",
            options=list(application_options.keys()),
            format_func=lambda x: (
                application_options[x]["company_name"]
                + " - "
                + application_options[x]["job_role"]
            )
        )

        round_name = st.selectbox(
            "Interview Round",
            ["Aptitude", "Technical", "HR", "Group Discussion", "Other"]
        )

        interview_date = st.date_input(
            "Interview Date",
            value=date.today()
        )

        interview_status = st.selectbox(
            "Interview Status",
            ["Scheduled", "Completed", "Cleared", "Not Cleared"]
        )

        notes = st.text_area("Interview Notes")

        submitted = st.form_submit_button(
            "Schedule Interview",
            use_container_width=True
        )

        if submitted:
            try:
                add_interview(
                    selected_application,
                    round_name,
                    interview_date,
                    interview_status,
                    notes
                )

                st.session_state.interview_added = True
                st.rerun()

            except Exception as e:
                st.error(f"Unable to schedule interview: {e}")

else:
    st.info(
        "Please add a company application before scheduling an interview."
    )
