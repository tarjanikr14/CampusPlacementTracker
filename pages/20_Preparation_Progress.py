
import streamlit as st
import pandas as pd

from database import get_preparation_topics
from theme import apply_theme

apply_theme()

st.title("📚 Preparation Progress")
st.caption("Monitor your study progress and completed preparation topics.")

st.divider()

topics = get_preparation_topics()

if topics:

    completed = sum(
        1 for topic in topics
        if topic["is_completed"]
    )

    total = len(topics)
    remaining = total - completed
    progress = completed / total

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Topics", total)
    col2.metric("Completed", completed)
    col3.metric("Remaining", remaining)

    st.divider()

    st.subheader("Overall Progress")

    st.progress(progress)

    st.metric(
        "Completion Percentage",
        f"{progress * 100:.1f}%"
    )

    st.divider()

    st.subheader("Topics by Company")

    topic_df = pd.DataFrame(topics)

    company_progress = (
        topic_df.groupby("company_name")
        .agg(
            Total_Topics=("id", "count"),
            Completed=("is_completed", "sum")
        )
        .reset_index()
    )

    company_progress["Remaining"] = (
        company_progress["Total_Topics"]
        - company_progress["Completed"]
    )

    company_progress["Completion Percentage"] = (
        company_progress["Completed"]
        / company_progress["Total_Topics"] * 100
    ).round(1)

    st.bar_chart(
        company_progress,
        x="company_name",
        y=["Completed", "Remaining"]
    )

    st.dataframe(
        company_progress,
        use_container_width=True,
        hide_index=True
    )

else:
    st.info("Add preparation topics to view your progress.")
