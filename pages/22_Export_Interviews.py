
import streamlit as st
import pandas as pd

from database import get_interviews
from theme import apply_theme

apply_theme()

st.title("📅 Export Interviews")
st.caption("Download all your placement interview records.")

st.divider()

interviews = get_interviews()

if interviews:

    interviews_df = pd.DataFrame(interviews)

    csv_data = interviews_df.to_csv(
        index=False
    ).encode("utf-8")

    st.metric("Total Interviews", len(interviews))

    st.success("Your interviews report is ready to download!")

    st.download_button(
        "📥 Download Interviews CSV",
        data=csv_data,
        file_name="interviews_report.csv",
        mime="text/csv",
        use_container_width=True
    )

else:
    st.info("No interview records available to export.")
