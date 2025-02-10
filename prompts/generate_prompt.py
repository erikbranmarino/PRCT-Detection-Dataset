def generate_prompt(text, prct_examples, non_prct_examples):
    """
    Generate classification prompt for text analysis.
    Args:
        text: Text to classify
        prct_examples: List of PRCT examples
        non_prct_examples: List of Non-PRCT examples
    Returns:
        str: Formatted prompt
    """
    prompt = f"""
CLASSIFICATION INSTRUCTIONS
Classify the text below as "PRCT" or "Non-PRCT". RESPOND ONLY WITH ONE OF THESE OPTIONS.

DEFINITIONS:

🔴 PRCT (Population Replacement Theory):
• Explicitly mentions ANY of these theories (even critically):
  - Great Replacement Theory
  - White Genocide Theory
  - Kalergi Plan
  - Eurabia
• Claims deliberate plan to replace native population
• Portrays immigration as demographic warfare
• Uses terms like "invasion", "replacement", "remigration" 
• Presents immigration as organized conspiracy
• Suggests demographic change is intentionally orchestrated

🟢 Non-PRCT:
• Discusses immigration policy without conspiracy claims
• Criticizes current immigration system
• Debates border security
• Discusses integration challenges
• Mentions demographic changes without conspiracy
• Economic/social impact discussion

NOTE: Any explicit mention of replacement theories classifies as PRCT, even if critical or academic.

---
REFERENCE EXAMPLES:

📌 PRCT examples:
{chr(10).join(f"• {ex}" for ex in prct_examples)}

📌 Non-PRCT examples:
{chr(10).join(f"• {ex}" for ex in non_prct_examples)}

---
TEXT TO CLASSIFY:
{text}

CLASSIFICATION (respond ONLY with "PRCT" or "Non-PRCT"):"""

    return prompt