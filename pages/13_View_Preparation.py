
import streamlit as st
import pandas as pd

from database import get_preparation_topics, update_preparation_status
from theme import apply_theme

apply_theme()

st.title("📚 View Preparation")
st.caption("Track your study topics and monitor your preparation progress.")

st.divider()

# SUCCESS MESSAGE AFTER STATUS UPDATE

if st.session_state.get("preparation_status_message"):
    st.success(st.session_state.preparation_status_message)
    st.session_state.preparation_status_message = None

topics = get_preparation_topics()

if topics:

    completed_count = sum(
        1 for item in topics
        if item["is_completed"]
    )

    total_count = len(topics)

    col1, col2 = st.columns(2)

    col1.metric("Total Topics", total_count)
    col2.metric("Completed Topics", completed_count)

    st.progress(completed_count / total_count)

    st.caption(
        f"{completed_count} of {total_count} topics completed"
    )

    st.divider()

    search = st.text_input(
        "🔍 Search topics or companies",
        placeholder="Enter a topic or company name..."
    )

    filtered_topics = [
        item for item in topics
        if search.lower() in item["topic"].lower()
        or search.lower() in item["company_name"].lower()
        or search.lower() in item["job_role"].lower()
    ]

    if filtered_topics:

        for item in filtered_topics:

            st.markdown(
                f"**{item['company_name']} - {item['job_role']}**"
            )

            completed = st.checkbox(
                item["topic"],
                value=bool(item["is_completed"]),
                key=f"topic_{item['id']}"
            )

            if completed != bool(item["is_completed"]):

                try:
                    update_preparation_status(
                        item["id"],
                        completed
                    )

                    if completed:
                        st.session_state.preparation_status_message = (
                            "Topic marked as completed successfully!"
                        )
                    else:
                        st.session_state.preparation_status_message = (
                            "Topic marked as incomplete successfully!"
                        )

                    st.rerun()

                except Exception as e:
                    st.error(f"Unable to update topic status: {e}")

            if item["notes"]:
                st.caption("Notes: " + item["notes"])

            st.divider()

    else:
        st.info("No topics match your search.")

else:
    st.info(
        "No preparation topics added yet. "
        "Add your first topic to get started."
    )
