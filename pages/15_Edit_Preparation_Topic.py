
import streamlit as st

from database import (
    get_applications,
    get_preparation_topics,
    update_preparation_topic
)

from theme import apply_theme

apply_theme()

st.title("✏️ Edit Preparation Topic")
st.caption("Update an existing study topic or its notes.")

st.divider()

# DISPLAY SUCCESS MESSAGE
if st.session_state.get("preparation_topic_updated"):
    st.success("Preparation topic updated successfully!")
    st.session_state.preparation_topic_updated = False

applications = get_applications()
topics = get_preparation_topics()

if applications and topics:

    application_options = {
        app["id"]: app for app in applications
    }

    topic_options = {
        item["id"]: item for item in topics
    }

    selected_id = st.selectbox(
        "Select Topic",
        options=list(topic_options.keys()),
        format_func=lambda x: (
            topic_options[x]["company_name"]
            + " - "
            + topic_options[x]["topic"]
        )
    )

    selected_topic = topic_options[selected_id]

    with st.form("edit_preparation_form"):

        selected_application = st.selectbox(
            "Select Company",
            options=list(application_options.keys()),
            index=list(application_options.keys()).index(
                selected_topic["application_id"]
            ),
            format_func=lambda x: (
                application_options[x]["company_name"]
                + " - "
                + application_options[x]["job_role"]
            )
        )

        topic = st.text_input(
            "Topic",
            value=selected_topic["topic"]
        )

        notes = st.text_area(
            "Study Notes",
            value=selected_topic["notes"] or ""
        )

        submitted = st.form_submit_button(
            "Save Changes",
            use_container_width=True
        )

        if submitted:

            if topic.strip():

                try:
                    update_preparation_topic(
                        selected_id,
                        selected_application,
                        topic.strip(),
                        notes.strip()
                    )

                    st.session_state.preparation_topic_updated = True
                    st.rerun()

                except Exception as e:
                    st.error(f"Unable to update preparation topic: {e}")

            else:
                st.warning("Please enter a topic.")

else:
    st.info("Add a company application and preparation topic first.")
