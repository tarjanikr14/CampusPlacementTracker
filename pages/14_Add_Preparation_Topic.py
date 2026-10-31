
import streamlit as st

from database import get_applications, add_preparation_topic
from theme import apply_theme

apply_theme()

st.title("➕ Add Preparation Topic")
st.caption("Add study topics to your placement preparation checklist.")

st.divider()

# DISPLAY SUCCESS MESSAGE
if st.session_state.get("preparation_topic_added"):
    st.success("Preparation topic added successfully!")
    st.session_state.preparation_topic_added = False

applications = get_applications()

if applications:

    application_options = {
        app["id"]: app for app in applications
    }

    with st.form("add_preparation_form"):

        selected_application = st.selectbox(
            "Select Company",
            options=list(application_options.keys()),
            format_func=lambda x: (
                application_options[x]["company_name"]
                + " - "
                + application_options[x]["job_role"]
            )
        )

        topic = st.text_input(
            "Topic",
            placeholder="Example: Python OOP Concepts"
        )

        notes = st.text_area(
            "Study Notes",
            placeholder="Enter important concepts to revise..."
        )

        submitted = st.form_submit_button(
            "Save Topic",
            use_container_width=True
        )

        if submitted:

            if topic.strip():

                try:
                    add_preparation_topic(
                        selected_application,
                        topic.strip(),
                        notes.strip()
                    )

                    st.session_state.preparation_topic_added = True
                    st.rerun()

                except Exception as e:
                    st.error(f"Unable to add preparation topic: {e}")

            else:
                st.warning("Please enter a topic.")

else:
    st.info("Please add a company application first.")
