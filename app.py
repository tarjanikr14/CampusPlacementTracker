
import streamlit as st

from database import (
    create_table,
    create_interview_table,
    create_preparation_table
)

from theme import apply_theme

st.set_page_config(
    page_title="Campus Placement Tracker",
    page_icon="🎀",
    layout="wide"
)

# Initialise database
create_table()
create_interview_table()
create_preparation_table()

# Apply theme
apply_theme()

# Register pages


pages = {
    "Placement Tracker": [
        st.Page("pages/1_Dashboard.py", title="Dashboard", icon="📊"),
    ],

    "Applications": [
        st.Page("pages/2_View_Applications.py", title="View Applications", icon="📋"),
        st.Page("pages/3_Add_Application.py", title="Add New Application", icon="➕"),
        st.Page("pages/4_Edit_Application.py", title="Edit Application", icon="✏️"),
        st.Page("pages/5_Delete_Application.py", title="Delete Application", icon="🗑️"),
    ],

    "Interviews": [
        st.Page("pages/6_View_Interviews.py", title="View Interviews", icon="📋"),
        st.Page("pages/10_Schedule_Interview.py", title="Schedule Interview", icon="📅"),
        st.Page("pages/11_Edit_Interview.py", title="Edit Interview", icon="✏️"),
        st.Page("pages/12_Delete_Interview.py", title="Delete Interview", icon="🗑️"),
    ],

    "Preparation": [
        st.Page("pages/13_View_Preparation.py", title="View Preparation", icon="📚"),
        st.Page("pages/14_Add_Preparation_Topic.py", title="Add Preparation Topic", icon="➕"),
        st.Page("pages/15_Edit_Preparation_Topic.py", title="Edit Preparation Topic", icon="✏️"),
        st.Page("pages/16_Delete_Preparation_Topic.py", title="Delete Preparation Topic", icon="🗑️"),
    ],

    "Analytics": [
        st.Page("pages/17_Placement_Overview.py", title="Placement Overview", icon="📊"),
        st.Page("pages/18_Application_Analytics.py", title="Application Analytics", icon="📈"),
        st.Page("pages/19_Interview_Analytics.py", title="Interview Analytics", icon="📉"),
        st.Page("pages/20_Preparation_Progress.py", title="Preparation Progress", icon="📚"),
    ],

    "Export Reports": [
        st.Page("pages/21_Export_Applications.py", title="Export Applications", icon="🏢"),
        st.Page("pages/22_Export_Interviews.py", title="Export Interviews", icon="📅"),
        st.Page("pages/23_Export_Preparation.py", title="Export Preparation", icon="📚"),
    ],
}

navigation = st.navigation(pages)
navigation.run()
