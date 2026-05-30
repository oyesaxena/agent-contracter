import streamlit as st
import requests


st.title(
    "Document Automation Agent"
)

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    with st.spinner(
        "Processing..."
    ):

        response = requests.post(
            "http://localhost:8000/documents/upload",
            files={
                "file": (
                    uploaded_file.name,
                    uploaded_file,
                    "application/pdf"
                )
            }
        )

        data = response.json()

        st.success(
            "Workflow Completed"
        )

        st.subheader(
            "Classification"
        )

        st.json(
            data["classification"]
        )

        st.subheader(
            "Extraction"
        )

        st.json(
            data["extraction"]
        )

        st.subheader(
            "Validation"
        )

        st.json(
            data["validation"]
        )

        st.metric(
            "Confidence Score",
            round(
                data[
                    "confidence_score"
                ],
                2
            )
        )

        if data[
            "review_required"
        ]:

            st.warning(
                "Needs Review"
            )

        else:

            st.success(
                "Automatically Approved"
            )