from modules.summarizer import summarize_document

from modules.red_flag_engine import (
    detect_red_flags,
    calculate_risk_score
)

from modules.clause_explainer import (
    explain_flag
)

from modules.legal_rag import (
    legal_rag
)


def generate_legal_report(
        document_text
):

    report = {}

    # =====================================
    # Summary
    # =====================================

    summary = summarize_document(
        document_text
    )

    report["summary"] = summary

    # =====================================
    # Red Flags
    # =====================================

    flags = detect_red_flags(
        document_text
    )

    report["flags"] = flags

    # =====================================
    # Risk Score
    # =====================================

    risk_score = calculate_risk_score(
        flags
    )

    report["risk_score"] = risk_score

    # =====================================
    # AI Explanations
    # =====================================

    explanations = []

    for flag in flags:

        explanation = explain_flag(
            flag,
            document_text
        )

        explanations.append({

            "title":
            flag["title"],

            "severity":
            flag["severity"],

            "explanation":
            explanation
        })

    report[
        "flag_explanations"
    ] = explanations

    # =====================================
    # Legal Analysis
    # =====================================

    legal_analysis = legal_rag(
        "Analyze this legal document."
    )

    report[
        "legal_analysis"
    ] = legal_analysis

    return report