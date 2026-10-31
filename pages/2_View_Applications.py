
import streamlit as st
import pandas as pd

from database import get_applications
from theme import apply_theme

apply_theme()

st.title("📋 View Applications")
st.caption("View and track all your placement applications.")

st.divider()

applications = get_applications()

if applications:

    # APPLICATION OVERVIEW

    st.subheader("Application Overview")

    total = len(applications)

    shortlisted = sum(
        1 for app in applications
        if app["status"] == "Shortlisted"
    )

    selected = sum(
        1 for app in applications
        if app["status"] == "Selected"
    )

    rejected = sum(
        1 for app in applications
        if app["status"] == "Rejected"
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Applications", total)
    col2.metric("Shortlisted", shortlisted)
    col3.metric("Selected", selected)
    col4.metric("Rejected", rejected)

    st.divider()

    # SEARCH AND FILTER

    st.subheader("Search & Filter Applications")

    col1, col2 = st.columns([1.5, 1])

    with col1:
        search = st.text_input(
            "Search",
            placeholder="Search by company or job role..."
        )

    with col2:
        statuses = [
            "All",
            "Applied",
            "Shortlisted",
            "Interview Scheduled",
            "Selected",
            "Rejected"
        ]

        selected_status = st.selectbox(
            "Filter by Status",
            statuses
        )

    filtered_applications = []

    for app in applications:

        matches_search = (
            search.lower() in app["company_name"].lower()
            or search.lower() in app["job_role"].lower()
        )

        matches_status = (
            selected_status == "All"
            or app["status"] == selected_status
        )

        if matches_search and matches_status:
            filtered_applications.append(app)

    st.caption(
        f"Showing {len(filtered_applications)} "
        f"of {total} applications"
    )

    # APPLICATION TABLE

    st.subheader("All Applications")

    if filtered_applications:

        display_data = []

        for app in filtered_applications:
            display_data.append({
                "Company": app["company_name"],
                "Job Role": app["job_role"],
                "Package (LPA)": app["package"],
                "Application Date": app["application_date"],
                "Status": app["status"]
            })

        st.dataframe(
            pd.DataFrame(display_data),
            use_container_width=True,
            hide_index=True
        )

    else:
        st.info("No matching applications found.")

    st.divider()

    # STATUS BREAKDOWN

    st.subheader("Application Status Breakdown")

    status_df = pd.DataFrame(applications)

    status_counts = (
        status_df["status"]
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
    st.info(
        "No applications added yet. "
        "Go to Add New Application to get started."
    )
