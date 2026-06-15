import os

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def create_pdf_report(
        report,
        output_path
):

    os.makedirs(
        "reports",
        exist_ok=True
    )

    pdf = SimpleDocTemplate(
        output_path
    )

    styles = getSampleStyleSheet()

    content = []

    # ==========================
    # Title
    # ==========================

    content.append(
        Paragraph(
            "Legal Document Analysis Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    # ==========================
    # Risk Score
    # ==========================

    content.append(
        Paragraph(
            f"<b>Risk Score:</b> {report['risk_score']}",
            styles["Heading2"]
        )
    )

    content.append(
        Spacer(1, 15)
    )

    # ==========================
    # Summary
    # ==========================

    content.append(
        Paragraph(
            "Executive Summary",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            report["summary"],
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    # ==========================
    # Red Flags
    # ==========================

    content.append(
        Paragraph(
            "Detected Red Flags",
            styles["Heading1"]
        )
    )

    for flag in report["flags"]:

        content.append(
            Paragraph(
                f"<b>{flag['severity']}</b> - {flag['title']}",
                styles["Heading3"]
            )
        )

        content.append(
            Paragraph(
                flag["description"],
                styles["BodyText"]
            )
        )

        content.append(
            Spacer(1, 10)
        )

    # ==========================
    # Explanations
    # ==========================

    content.append(
        PageBreak()
    )

    content.append(
        Paragraph(
            "AI Clause Explanations",
            styles["Heading1"]
        )
    )

    for item in report[
        "flag_explanations"
    ]:

        content.append(
            Paragraph(
                item["title"],
                styles["Heading2"]
            )
        )

        content.append(
            Paragraph(
                item["explanation"],
                styles["BodyText"]
            )
        )

        content.append(
            Spacer(1, 10)
        )

    # ==========================
    # Legal Analysis
    # ==========================

    content.append(
        PageBreak()
    )

    content.append(
        Paragraph(
            "Legal Analysis",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            report[
                "legal_analysis"
            ],
            styles["BodyText"]
        )
    )

    pdf.build(
        content
    )

    return output_path