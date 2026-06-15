import re


def detect_red_flags(text):

    text = text.lower()

    flags = []

    # =====================================
    # Employment Related
    # =====================================

    if (
        "non-compete" in text
        or "competing business" in text
    ):

        flags.append({
            "severity": "HIGH",
            "title": "Non-Compete Clause",
            "description":
            "Restricts future employment opportunities."
        })

    if (
        "terminate employment" in text
        and "without notice" in text
    ):

        flags.append({
            "severity": "HIGH",
            "title": "One-Sided Termination",
            "description":
            "Employer may terminate employment without notice."
        })

    if (
        "90 day notice" in text
        or "90 days notice" in text
        or "90 days written notice" in text
    ):

        flags.append({
            "severity": "MEDIUM",
            "title": "Long Notice Period",
            "description":
            "Extended notice obligations may limit employee mobility."
        })

    # =====================================
    # Confidentiality
    # =====================================

    if "confidential information" in text:

        flags.append({
            "severity": "LOW",
            "title": "Confidentiality Obligation",
            "description":
            "Employee must protect company confidential information."
        })

    # =====================================
    # Auto Renewal
    # =====================================

    if (
        "automatically renew" in text
        or "automatic renewal" in text
        or "auto renewal" in text
    ):

        flags.append({
            "severity": "MEDIUM",
            "title": "Auto Renewal Clause",
            "description":
            "Contract may automatically renew if not terminated."
        })

    # =====================================
    # Arbitration
    # =====================================

    if "arbitration" in text:

        flags.append({
            "severity": "MEDIUM",
            "title": "Mandatory Arbitration",
            "description":
            "Disputes may need to be resolved through arbitration instead of court."
        })

    # =====================================
    # Unlimited Liability
    # =====================================

    if (
        "unlimited liability" in text
        or "liable for all damages" in text
    ):

        flags.append({
            "severity": "HIGH",
            "title": "Unlimited Liability",
            "description":
            "Party may be liable for unrestricted damages."
        })

    # =====================================
    # Indemnity Clause
    # =====================================

    if "indemnify" in text:

        flags.append({
            "severity": "MEDIUM",
            "title": "Indemnity Clause",
            "description":
            "One party agrees to compensate losses of another party."
        })

    # =====================================
    # Jurisdiction Outside India
    # =====================================

    if (
        "governed by the laws of" in text
        and "india" not in text
    ):

        flags.append({
            "severity": "HIGH",
            "title": "Foreign Jurisdiction",
            "description":
            "Legal disputes may be governed outside India."
        })

    return flags


def calculate_risk_score(flags):

    score = 0

    for flag in flags:

        if flag["severity"] == "HIGH":
            score += 30

        elif flag["severity"] == "MEDIUM":
            score += 15

        elif flag["severity"] == "LOW":
            score += 5

    return min(score, 100)