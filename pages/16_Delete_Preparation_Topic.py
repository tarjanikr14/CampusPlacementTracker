
import streamlit as st

from database import get_preparation_topics, delete_preparation_topic
from theme import apply_theme

apply_theme()

st.title("🗑️ Delete Preparation Topic")
st.caption("Remove a study topic from your preparation checklist.")

st.divider()

topics = get_preparation_topics()

if topics:

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

    st.warning(
        f"You are about to delete '{selected_topic['topic']}' "
        f"for {selected_topic['company_name']}."
    )

    confirm = st.checkbox(
        "I confirm that I want to delete this topic."
    )

    if st.button("Delete Topic", disabled=not confirm):
        delete_preparation_topic(selected_id)
        st.success("Topic deleted successfully!")
        st.rerun()

else:
    st.info("There are no preparation topics to delete.")

