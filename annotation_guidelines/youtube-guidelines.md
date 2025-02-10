# Annotation Guidelines for PRCT Detection in YouTube Comments

## Introduction
These guidelines are designed to assist annotators in identifying Population Replacement Conspiracy Theory (PRCT) content in YouTube comments. The goal is to ensure consistency and accuracy in labeling, which is crucial for evaluating the performance of detection models.

## PRCT Detection

### Definition
PRCT content includes:
- Explicit mentions of conspiracy theories related to population replacement:
  - Great Replacement Theory
  - White Genocide Theory
  - Eurabia
  - Kalergi Plan
- Claims of deliberate demographic changes
- Use of terms like "invasion" or "replacement"
- Suggestions that immigration is part of an organized conspiracy

### Labels
- **Label 0 (Non-PRCT)**: Content that discusses immigration in neutral terms, critiques policies, or addresses demographic changes without conspiracy elements.
- **Label 1 (PRCT)**: Content that explicitly mentions replacement theories, uses conspiracy-related language, or portrays immigration as part of a deliberate plan.

### Examples

#### Non-PRCT (Label 0):
- "Immigration numbers have increased by 20% this year"
- "We need better border control policies"
- "The economic impact of immigration needs to be studied carefully"
- "Integration of immigrants is a complex challenge"
- "Current immigration policies are too lenient/strict"

#### PRCT (Label 1):
- "This is clearly part of the great replacement agenda"
- "They're deliberately importing immigrants to replace us"
- "The Kalergi plan is in full effect"
- "This is white genocide through immigration"
- "It's an organized invasion to change our demographics"

## Annotation Process

1. **Read the Comment Carefully**: 
   - Consider the full context
   - Look for both explicit and implicit references to PRCT

2. **Check for Key Indicators**:
   - Explicit theory mentions
   - Conspiracy-related terminology
   - Claims of orchestrated demographic change
   - References to deliberate "replacement"

3. **Consider the Context**:
   - Even academic or critical discussions of PRCT should be labeled as PRCT
   - Policy criticism without conspiracy elements is Non-PRCT
   - Economic or social impact discussions without conspiracy elements are Non-PRCT

## Special Considerations for YouTube Comments

1. **Thread Context**:
   - Consider the comment in the context of the thread
   - Replies might reference PRCT content from parent comments

2. **Platform-Specific Language**:
   - Watch for YouTube-specific slang or abbreviations
   - Consider emoji usage and formatting
   - Be aware of platform-specific dog whistles

3. **Comment Length**:
   - Short comments may require more context interpretation
   - Long comments may contain mixed content (label as PRCT if any clear PRCT content exists)

## Frequently Asked Questions

1. **Q: What if a comment critically discusses PRCT?**
   A: Label it as PRCT (1). The presence of PRCT content, even in a critical context, warrants the PRCT label.

2. **Q: How should we handle ambiguous cases?**
   A: If there's no clear evidence of PRCT content, label as Non-PRCT (0). Only use the PRCT label when there are clear indicators.

3. **Q: What about comments discussing demographic changes without conspiracy elements?**
   A: Label as Non-PRCT (0). Discussion of demographic changes must include conspiracy elements to be labeled as PRCT.

4. **Q: Should we consider the video context when labeling comments?**
   A: Focus primarily on the comment content, but use video context when needed to understand unclear references.

## Examples of Borderline Cases

### Labeled as PRCT (1):
- "They're not even hiding the replacement anymore..." (implicit reference to replacement theory)
- "Look up Kalergi, this is all planned" (reference to PRCT theory)
- "This is demographic warfare against us" (portrays immigration as organized attack)

### Labeled as Non-PRCT (0):
- "Immigration rates are too high" (policy criticism without conspiracy)
- "We need stricter border controls" (security discussion without PRCT elements)
- "This will change our country's demographics" (demographic observation without conspiracy)
