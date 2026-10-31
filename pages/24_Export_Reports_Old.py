
import streamlit as st
import pandas as pd

from database import (
    get_applications,
    get_interviews,
    get_preparation_topics
)

from theme import apply_theme

apply_theme()

st.title("📥 Export Reports")
st.write("Download your placement records whenever you need them.")

st.divider()

# Applications Report
st.subheader("🏢 Applications Report")

applications = get_applications()

if applications:
    applications_df = pd.DataFrame(applications)

    csv_data = applications_df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        "Download Applications CSV",
        data=csv_data,
        file_name="applications_report.csv",
        mime="text/csv"
    )
else:
    st.info("No application records available.")

st.divider()

# Interviews Report
st.subheader("📅 Interviews Report")

interviews = get_interviews()

if interviews:
    interviews_df = pd.DataFrame(interviews)

    csv_data = interviews_df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        "Download Interviews CSV",
        data=csv_data,
        file_name="interviews_report.csv",
        mime="text/csv"
    )
else:
    st.info("No interview records available.")

st.divider()

# Preparation Report
st.subheader("📚 Preparation Report")

topics = get_preparation_topics()

if topics:
    topics_df = pd.DataFrame(topics)

    csv_data = topics_df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        "Download Preparation CSV",
        data=csv_data,
        file_name="preparation_report.csv",
        mime="text/csv"
    )
else:
    st.info("No preparation records available.")

st.divider()

st.caption("Your placement data, organised and ready to download. 🌸")
