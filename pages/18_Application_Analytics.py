
import streamlit as st
import pandas as pd

from database import get_applications
from theme import apply_theme

apply_theme()

st.title("📈 Application Analytics")
st.caption("Understand your placement application statistics.")

st.divider()

applications = get_applications()

if applications:

    total = len(applications)

    selected = sum(
        1 for app in applications
        if app["status"] == "Selected"
    )

    shortlisted = sum(
        1 for app in applications
        if app["status"] == "Shortlisted"
    )

    rejected = sum(
        1 for app in applications
        if app["status"] == "Rejected"
    )

    selection_rate = (selected / total) * 100

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Applications", total)
    col2.metric("Shortlisted", shortlisted)
    col3.metric("Selected", selected)
    col4.metric("Rejected", rejected)

    st.divider()

    st.subheader("Selection Rate")
    st.metric("Overall Selection Rate", f"{selection_rate:.1f}%")

    st.progress(selection_rate / 100)

    st.divider()

    st.subheader("Application Status Breakdown")

    application_df = pd.DataFrame(applications)

    status_counts = (
        application_df["status"]
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

else:
    st.info("Add applications to view application analytics.")

