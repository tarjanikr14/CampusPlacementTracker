
import streamlit as st
import pandas as pd

from database import get_applications
from theme import apply_theme

apply_theme()

st.title("🏢 Export Applications")
st.caption("Download all your placement application records.")

st.divider()

applications = get_applications()

if applications:

    applications_df = pd.DataFrame(applications)

    csv_data = applications_df.to_csv(
        index=False
    ).encode("utf-8")

    st.metric("Total Applications", len(applications))

    st.success("Your applications report is ready to download!")

    st.download_button(
        "📥 Download Applications CSV",
        data=csv_data,
        file_name="applications_report.csv",
        mime="text/csv",
        use_container_width=True
    )

else:
    st.info("No application records available to export.")
