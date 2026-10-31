
import streamlit as st
import pandas as pd

from database import get_interviews
from theme import apply_theme

apply_theme()

st.title("📋 View Interviews")
st.caption("View and track all your placement interviews.")

st.divider()

interviews = get_interviews()

if interviews:

    total = len(interviews)
    scheduled = sum(i["status"] == "Scheduled" for i in interviews)
    completed = sum(i["status"] == "Completed" for i in interviews)
    cleared = sum(i["status"] == "Cleared" for i in interviews)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Interviews", total)
    col2.metric("Scheduled", scheduled)
    col3.metric("Completed", completed)
    col4.metric("Cleared", cleared)

    st.divider()

    st.markdown("### Search and Filter")

    search = st.text_input(
        "🔍 Search by company or job role",
        placeholder="Enter company name or job role..."
    )

    statuses = [
        "All",
        "Scheduled",
        "Completed",
        "Cleared",
        "Not Cleared"
    ]

    selected_status = st.selectbox(
        "Filter by Status",
        statuses
    )

    filtered = interviews

    if search:
        filtered = [
            i for i in filtered
            if search.lower() in i["company_name"].lower()
            or search.lower() in i["job_role"].lower()
        ]

    if selected_status != "All":
        filtered = [
            i for i in filtered
            if i["status"] == selected_status
        ]

    st.divider()

    st.markdown("### Interview Records")

    if filtered:

        df = pd.DataFrame([
            {
                "Company": i["company_name"],
                "Job Role": i["job_role"],
                "Interview Round": i["round_name"],
                "Interview Date": i["interview_date"],
                "Status": i["status"],
                "Notes": i["notes"]
            }
            for i in filtered
        ])

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        st.caption(f"Showing {len(filtered)} of {total} interviews.")

    else:
        st.warning("No interviews match your search or selected filter.")

else:
    st.info(
        "No interview records found. Schedule your first interview to get started."
    )

