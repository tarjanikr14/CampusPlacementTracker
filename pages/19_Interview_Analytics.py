
import streamlit as st
import pandas as pd

from database import get_interviews
from theme import apply_theme

apply_theme()

st.title("📊 Interview Analytics")
st.caption("Analyse your interview activity and outcomes.")

st.divider()

interviews = get_interviews()

if interviews:

    total = len(interviews)

    scheduled = sum(
        1 for interview in interviews
        if interview["status"] == "Scheduled"
    )

    completed = sum(
        1 for interview in interviews
        if interview["status"] == "Completed"
    )

    cleared = sum(
        1 for interview in interviews
        if interview["status"] == "Cleared"
    )

    not_cleared = sum(
        1 for interview in interviews
        if interview["status"] == "Not Cleared"
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Interviews", total)
    col2.metric("Scheduled", scheduled)
    col3.metric("Cleared", cleared)
    col4.metric("Not Cleared", not_cleared)

    st.divider()

    st.subheader("Interview Status Breakdown")

    interview_df = pd.DataFrame(interviews)

    status_counts = (
        interview_df["status"]
        .value_counts()
        .reset_index()
    )

    status_counts.columns = ["Status", "Count"]

    st.bar_chart(
        status_counts,
        x="Status",
        y="Count"
    )

else:
    st.info("Schedule interviews to view interview analytics.")
import streamlit as st
import pandas as pd

from database import get_interviews
from theme import apply_theme

apply_theme()

st.title("📊 Interview Analytics")
st.caption("Analyse your interview activity and outcomes.")

st.divider()

interviews = get_interviews()

if interviews:

    total = len(interviews)

    scheduled = sum(
        1 for interview in interviews
        if interview["status"] == "Scheduled"
    )

    completed = sum(
        1 for interview in interviews
        if interview["status"] == "Completed"
    )

    cleared = sum(
        1 for interview in interviews
        if interview["status"] == "Cleared"
    )

    not_cleared = sum(
        1 for interview in interviews
        if interview["status"] == "Not Cleared"
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Interviews", total)
    col2.metric("Scheduled", scheduled)
    col3.metric("Cleared", cleared)
    col4.metric("Not Cleared", not_cleared)

    st.divider()

    st.subheader("Interview Status Breakdown")

    interview_df = pd.DataFrame(interviews)

    status_counts = (
        interview_df["status"]
        .value_counts()
        .reset_index()
    )

    status_counts.columns = ["Status", "Count"]

    status_counts["Percentage"] = (
        status_counts["Count"] / total * 100
    ).round(1)

    st.bar_chart(
        status_counts,
        x="Status",
        y="Count"
    )

    st.subheader("Status-wise Details")

    st.dataframe(
        status_counts,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("Interview Progress")

    completion_rate = (completed / total) * 100

    st.metric("Completed Interview Rate", f"{completion_rate:.1f}%")
    st.progress(completion_rate / 100)

else:
    st.info("Schedule interviews to view interview analytics.")
