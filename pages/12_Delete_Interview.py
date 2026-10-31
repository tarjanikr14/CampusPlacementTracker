
import streamlit as st

from database import get_interviews, delete_interview
from theme import apply_theme

apply_theme()

st.title("🗑️ Delete Interview")
st.caption("Remove an interview record from your tracker.")

st.divider()

# SUCCESS MESSAGE AFTER DELETION

if st.session_state.get("interview_deleted"):
    st.success("Interview deleted successfully!")
    st.session_state.interview_deleted = False

interviews = get_interviews()

if interviews:

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

    st.warning(
        f"You are about to delete the {selected_interview['round_name']} "
        f"interview at {selected_interview['company_name']}."
    )

    confirm = st.checkbox(
        "I confirm that I want to delete this interview."
    )

    if st.button("Delete Interview", disabled=not confirm):

        try:
            delete_interview(selected_id)

            st.session_state.interview_deleted = True
            st.rerun()

        except Exception as e:
            st.error(f"Unable to delete interview: {e}")

else:
    st.info("There are no interview records to delete.")
