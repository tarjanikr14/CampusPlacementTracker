
import streamlit as st
from datetime import date

from database import (
    get_applications,
    get_interviews,
    update_interview
)

from theme import apply_theme

apply_theme()

st.title("✏️ Edit Interview")
st.caption("Update the details of an existing interview.")

st.divider()

# SUCCESS MESSAGE AFTER SAVING

if st.session_state.get("interview_updated"):
    st.success("Interview updated successfully!")
    st.session_state.interview_updated = False

applications = get_applications()
interviews = get_interviews()

if applications and interviews:

    application_options = {
        app["id"]: app for app in applications
    }

    interview_options = {
        interview["id"]: interview for interview in interviews
    }

    selected_id = st.selectbox(
        "Select Interview",
        options=list(interview_options.keys()),
        format_func=lambda x: (
            interview_options[x]["company_name"]
            + " - "
            + interview_options[x]["round_name"]
            + " - "
            + interview_options[x]["interview_date"]
        )
    )

    selected_interview = interview_options[selected_id]

    with st.form("edit_interview_form"):

        selected_application = st.selectbox(
            "Select Company",
            options=list(application_options.keys()),
            index=list(application_options.keys()).index(
                selected_interview["application_id"]
            ),
            format_func=lambda x: (
                application_options[x]["company_name"]
                + " - "
                + application_options[x]["job_role"]
            )
        )

        round_options = [
            "Aptitude",
            "Technical",
            "HR",
            "Group Discussion",
            "Other"
        ]

        current_round = selected_interview["round_name"]

        if current_round not in round_options:
            round_options.append(current_round)

        round_name = st.selectbox(
            "Interview Round",
            round_options,
            index=round_options.index(current_round)
        )

        interview_date = st.date_input(
            "Interview Date",
            value=date.fromisoformat(
                selected_interview["interview_date"]
            )
        )

        status_options = [
            "Scheduled",
            "Completed",
            "Cleared",
            "Not Cleared"
        ]

        current_status = selected_interview["status"]

        interview_status = st.selectbox(
            "Interview Status",
            status_options,
            index=status_options.index(current_status)
        )

        notes = st.text_area(
            "Interview Notes",
            value=selected_interview["notes"] or ""
        )

        submitted = st.form_submit_button(
            "Save Changes",
            use_container_width=True
        )

        if submitted:
            try:
                update_interview(
                    selected_id,
                    selected_application,
                    round_name,
                    interview_date,
                    interview_status,
                    notes
                )

                st.session_state.interview_updated = True
                st.rerun()

            except Exception as e:
                st.error(f"Unable to update interview: {e}")

else:
    st.info("Add a company application and schedule an interview first.")
