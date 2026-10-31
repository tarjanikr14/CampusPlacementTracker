
import streamlit as st

from database import get_applications, delete_application
from theme import apply_theme

apply_theme()

st.title("🗑️ Delete Application")
st.caption("Remove an application from your placement tracker.")

st.divider()

# DISPLAY SUCCESS MESSAGE AFTER REFRESH

if st.session_state.get("application_deleted"):
    st.success("Application deleted successfully!")
    st.session_state.application_deleted = False

applications = get_applications()

if applications:
    application_options = {app["id"]: app for app in applications}

    selected_id = st.selectbox(
        "Select application to delete",
        options=list(application_options.keys()),
        format_func=lambda x: (
            application_options[x]["company_name"]
            + " - "
            + application_options[x]["job_role"]
        )
    )

    selected_app = application_options[selected_id]

    st.warning(
        f"You are about to delete the application for "
        f"{selected_app['company_name']}."
    )

    confirm = st.checkbox(
        "I confirm that I want to delete this application."
    )

    if st.button("Delete Application", use_container_width=True):

        if confirm:
            try:
                delete_application(selected_id)

                st.session_state.application_deleted = True
                st.rerun()

            except Exception as e:
                st.error(f"Unable to delete application: {e}")

        else:
            st.warning("Please confirm before deleting.")

else:
    st.info("There are no applications to delete.")
