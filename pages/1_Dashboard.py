
import streamlit as st
import pandas as pd

from theme import apply_theme
from database import get_applications, get_interviews

apply_theme()

# --------------------------------------------------
# DASHBOARD STYLING
# --------------------------------------------------

st.markdown("""
<style>
    [data-testid="stMetric"] {
        background: #FFFFFF;
        border: 1px solid #E5E0EF;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 3px 12px rgba(41, 38, 61, 0.05);
        min-height: 120px;
    }

    [data-testid="stMetricLabel"] {
        color: #817995 !important;
        font-size: 12px !important;
        font-weight: 700 !important;
    }

    [data-testid="stMetricValue"] {
        color: #29263D !important;
        font-size: 32px !important;
        font-weight: 800 !important;
    }

    .dashboard-card {
        background: #FFFFFF;
        border: 1px solid #E5E0EF;
        border-radius: 16px;
        padding: 20px;
        min-height: 90px;
        box-shadow: 0 3px 12px rgba(41, 38, 61, 0.04);
        margin-bottom: 12px;
    }

    .dashboard-card h3 {
        color: #29263D;
        margin: 0;
        font-size: 20px;
    }

    .dashboard-subtitle {
        color: #817995;
        font-size: 13px;
        margin-top: 8px;
        margin-bottom: 0;
    }

    @media (max-width: 768px) {
        .dashboard-title {
            font-size: 28px !important;
            letter-spacing: 1px !important;
        }
    }
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# FETCH DATABASE RECORDS
# --------------------------------------------------

applications = get_applications()
interviews = get_interviews()


# --------------------------------------------------
# CALCULATE DASHBOARD METRICS
# --------------------------------------------------

total_applications = len(applications)

shortlisted = sum(
    1 for app in applications
    if app["status"] == "Shortlisted"
)

scheduled = sum(
    1 for interview in interviews
    if interview["status"] == "Scheduled"
)

selected = sum(
    1 for app in applications
    if app["status"] == "Selected"
)


# --------------------------------------------------
# DASHBOARD HEADING
# --------------------------------------------------

st.markdown(
    "<p class='dashboard-title' style='text-align:center; "
    "color:#29263D; font-size:46px; font-weight:800; "
    "letter-spacing:3px;'>"
    "CAMPUS PLACEMENT TRACKER</p>",
    unsafe_allow_html=True
)

st.markdown(
    "<h1 style='text-align:center; color:#9484BD; "
    "font-size:24px; font-weight:800;'>"
    "Your career journey starts here.</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center; color:#817995; font-size:16px;'>"
    "Track applications, prepare for interviews, and stay organised "
    "throughout your placement journey.</p>",
    unsafe_allow_html=True
)


# --------------------------------------------------
# PLACEMENT OVERVIEW
# --------------------------------------------------

st.markdown("## Placement Overview")
st.caption("A snapshot of your current placement progress.")

col1, col2, col3, col4 = st.columns(4)

col1.metric("TOTAL APPLICATIONS", total_applications)
col2.metric("SHORTLISTED", shortlisted)
col3.metric("INTERVIEWS SCHEDULED", scheduled)
col4.metric("OFFERS RECEIVED", selected)


# --------------------------------------------------
# QUICK ACTIONS
# --------------------------------------------------

st.markdown("")
st.markdown("## Quick Actions")
st.caption("Jump directly to the task you want to complete.")

action1, action2, action3 = st.columns(3)

with action1:
    st.page_link(
        "pages/3_Add_Application.py",
        label="➕ Add Application",
        use_container_width=True
    )

with action2:
    st.page_link(
        "pages/10_Schedule_Interview.py",
        label="📅 Schedule Interview",
        use_container_width=True
    )

with action3:
    st.page_link(
        "pages/14_Add_Preparation_Topic.py",
        label="📚 Add Preparation Topic",
        use_container_width=True
    )


# --------------------------------------------------
# APPLICATION ACTIVITY AND RECENT APPLICATIONS
# --------------------------------------------------

st.markdown("")
st.markdown("## Your Placement Activity")
st.caption("Review your application statistics and latest updates.")

left_col, right_col = st.columns([1.1, 1], gap="large")

with left_col:

    st.markdown(
        "<div class='dashboard-card'>"
        "<h3>Application Activity</h3>"
        "<p class='dashboard-subtitle'>"
        "Distribution of your application statuses."
        "</p>"
        "</div>",
        unsafe_allow_html=True
    )

    if applications:

        application_df = pd.DataFrame(
            [dict(app) for app in applications]
        )

        status_counts = (
            application_df["status"]
            .value_counts()
            .reset_index()
        )

        status_counts.columns = ["Status", "Count"]

        st.bar_chart(
            status_counts,
            x="Status",
            y="Count",
            color="#9484BD"
        )

    else:
        st.info("Add your first application to see your activity chart.")


with right_col:

    st.markdown(
        "<div class='dashboard-card'>"
        "<h3>Recent Applications</h3>"
        "<p class='dashboard-subtitle'>"
        "Your latest company applications."
        "</p>"
        "</div>",
        unsafe_allow_html=True
    )

    if applications:

        recent_df = pd.DataFrame(
            [dict(app) for app in applications[:5]]
        )

        display_columns = [
            column
            for column in ["company_name", "job_role", "status"]
            if column in recent_df.columns
        ]

        st.dataframe(
            recent_df[display_columns],
            use_container_width=True,
            hide_index=True
        )

    else:
        st.info("Your recent applications will appear here.")


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.markdown(
    "<p style='text-align:center; color:#817995; "
    "font-size:13px;'>"
    "Stay focused. Keep progressing."
    "</p>",
    unsafe_allow_html=True
)
