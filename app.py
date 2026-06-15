import os
import streamlit as st
import plotly.graph_objects as go

from modules.pdf_parser import extract_pdf_text
from modules.docx_parser import extract_docx
from modules.ocr_parser import image_to_text

from modules.legal_report import generate_legal_report
from modules.report_generator import create_pdf_report


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Legal Document Simplifier",
    page_icon="⚖️",
    layout="wide"
)

# ==================================================
# LOAD CSS
# ==================================================

if os.path.exists("assets/style.css"):
    with open("assets/style.css", "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.title("⚖️ Legal AI")

    st.markdown("---")

    st.success("Indian Law RAG")

    st.success("Document Analysis")

    st.success("Red Flag Detection")

    st.success("Risk Assessment")

    st.success("PDF Report Export")

    st.markdown("---")

    st.info(
        """
        **Supported Files**

        • PDF

        • DOCX

        • PNG

        • JPG

        • JPEG
        """
    )

    st.markdown("---")

    st.caption(
    "Powered by Qwen2.5 • FAISS • Indian Law RAG | Developed by Shivam Salve"
)

# ==================================================
# HEADER
# ==================================================

st.markdown(
    """
    <h1 style='text-align:center;color:#D4AF37'>
    ⚖️ Legal Document Simplifier
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h4 style='text-align:center;color:gray'>
    AI-Powered Legal Analysis System for Indian Laws
    </h4>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# ==================================================
# FILE UPLOAD
# ==================================================

uploaded_file = st.file_uploader(
    "Upload Legal Document",
    type=[
        "pdf",
        "docx",
        "png",
        "jpg",
        "jpeg"
    ]
)

# ==================================================
# PROCESS FILE
# ==================================================

if uploaded_file is not None:

    os.makedirs(
        "uploads",
        exist_ok=True
    )

    file_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Document uploaded successfully.")

    extension = uploaded_file.name.split(".")[-1].lower()

    # ==========================================
    # EXTRACT TEXT
    # ==========================================

    with st.spinner("Extracting document text..."):

        if extension == "pdf":

            text = extract_pdf_text(
                file_path
            )

        elif extension == "docx":

            text = extract_docx(
                file_path
            )

        else:

            text = image_to_text(
                file_path
            )

    # ==========================================
    # PREVIEW
    # ==========================================

    with st.expander("📄 Document Preview"):

        st.text_area(
            "Extracted Text",
            text[:10000],
            height=350
        )

    # ==========================================
    # ANALYZE BUTTON
    # ==========================================

    if st.button(
        "⚖️ Analyze Document",
        use_container_width=True
    ):

        with st.spinner(
            "Running Legal Analysis..."
        ):

            report = generate_legal_report(
                text
            )

        # ======================================
        # METRICS
        # ======================================

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Risk Score",
                report["risk_score"]
            )

        with col2:
            st.metric(
                "Flags Found",
                len(report["flags"])
            )

        with col3:
            st.metric(
                "Word Count",
                len(text.split())
            )

        # ======================================
        # RISK GAUGE
        # ======================================

        st.markdown("## 📊 Risk Assessment")

        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=report["risk_score"],
                title={"text": "Risk Score"},
                gauge={
                    "axis": {
                        "range": [0, 100]
                    }
                }
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # ======================================
        # SUMMARY
        # ======================================

        st.markdown("---")

        st.markdown(
            "## 📑 Executive Summary"
        )

        st.write(
            report["summary"]
        )

        # ======================================
        # RED FLAGS
        # ======================================

        st.markdown("---")

        st.markdown(
            "## 🚩 Detected Red Flags"
        )

        if len(report["flags"]) == 0:

            st.success(
                "No major legal risks detected."
            )

        else:

            for flag in report["flags"]:

                severity = flag["severity"]

                if severity == "HIGH":

                    st.error(
                        f"🔴 {flag['title']}"
                    )

                elif severity == "MEDIUM":

                    st.warning(
                        f"🟠 {flag['title']}"
                    )

                else:

                    st.info(
                        f"🟢 {flag['title']}"
                    )

                st.write(
                    flag["description"]
                )

        # ======================================
        # CLAUSE EXPLANATIONS
        # ======================================

        st.markdown("---")

        st.markdown(
            "## 🧠 Clause Explanations"
        )

        if isinstance(
            report["flag_explanations"],
            list
        ):

            for item in report[
                "flag_explanations"
            ]:

                with st.expander(
                    item["title"]
                ):

                    st.write(
                        item["explanation"]
                    )

        else:

            st.write(
                report["flag_explanations"]
            )

        # ======================================
        # LEGAL ANALYSIS
        # ======================================

        st.markdown("---")

        st.markdown(
            "## ⚖️ Legal Analysis"
        )

        st.write(
            report["legal_analysis"]
        )

        # ======================================
        # GENERATE PDF REPORT
        # ======================================

        st.markdown("---")

        with st.spinner(
            "Generating PDF Report..."
        ):

            os.makedirs(
                "reports",
                exist_ok=True
            )

            pdf_path = create_pdf_report(
                report,
                "reports/legal_report.pdf"
            )

        # ======================================
        # DOWNLOAD BUTTON
        # ======================================

        with open(
            pdf_path,
            "rb"
        ) as pdf_file:

            st.download_button(
                label="📥 Download PDF Report",
                data=pdf_file,
                file_name="legal_report.pdf",
                mime="application/pdf",
                use_container_width=True
            )