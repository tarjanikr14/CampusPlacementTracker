
import streamlit as st
import pandas as pd

from database import get_preparation_topics
from theme import apply_theme

apply_theme()

st.title("📚 Export Preparation Records")
st.caption("Download all your interview preparation topics and notes.")

st.divider()

topics = get_preparation_topics()

if topics:

    topics_df = pd.DataFrame(topics)

    csv_data = topics_df.to_csv(
        index=False
    ).encode("utf-8")

    st.metric("Total Preparation Topics", len(topics))

    st.success("Your preparation report is ready to download!")

    st.download_button(
        "📥 Download Preparation CSV",
        data=csv_data,
        file_name="preparation_report.csv",
        mime="text/csv",
        use_container_width=True
    )

else:
    st.info("No preparation records available to export.")

