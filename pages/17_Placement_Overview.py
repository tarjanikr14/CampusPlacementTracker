
import streamlit as st

from database import (
    get_applications,
    get_interviews,
    get_preparation_topics
)

from theme import apply_theme

apply_theme()

st.title("📊 Placement Overview")
st.caption("Your complete placement journey at a glance.")

st.divider()

applications = get_applications()
interviews = get_interviews()
topics = get_preparation_topics()

total_applications = len(applications)
total_interviews = len(interviews)
total_topics = len(topics)

selected = sum(
    1 for app in applications
    if app["status"] == "Selected"
)

shortlisted = sum(
    1 for app in applications
    if app["status"] == "Shortlisted"
)

completed_topics = sum(
    1 for topic in topics
    if topic["is_completed"]
)

selection_rate = (
    selected / total_applications * 100
    if total_applications else 0
)

# Main summary cards

st.subheader("Your Placement Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Applications", total_applications)
col2.metric("Interviews", total_interviews)
col3.metric("Shortlisted", shortlisted)
col4.metric("Selected", selected)

st.divider()

# Selection overview

st.subheader("Selection Overview")

col1, col2 = st.columns(2)

col1.metric("Selection Rate", f"{selection_rate:.1f}%")
col2.metric(
    "Preparation Topics Completed",
    f"{completed_topics} / {total_topics}"
)

if total_topics:
    st.progress(completed_topics / total_topics)
else:
    st.caption("Add preparation topics to start tracking progress.")

st.divider()

# Quick snapshot

st.subheader("Placement Snapshot")

if applications:
    st.markdown(f"- You have applied to **{total_applications}** opportunities.")
    st.markdown(f"- **{shortlisted}** applications are shortlisted.")
    st.markdown(f"- **{selected}** applications have resulted in selection.")
else:
    st.info("Your application summary will appear here once you add applications.")

if interviews:
    st.write(f"• You have recorded **{total_interviews}** interviews.")
else:
    st.caption("No interviews recorded yet.")

st.divider()

st.caption("Keep learning, keep applying, and track your progress!")
