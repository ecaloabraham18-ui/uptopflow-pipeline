import os
import anthropic
from datetime import date
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def generate_sop(summary_path, routine_name, systems_covered, 
                 frequency, facility_name, output_path):

    with open(summary_path, 'r', encoding='utf-8') as f:
        summary = f.read()

    prompt = f"""You are a technical documentation specialist for mission-critical data center facilities. Generate a complete Standard Operating Procedure (SOP).

ROUTINE: {routine_name}
SYSTEMS COVERED: {systems_covered}
FREQUENCY: {frequency}
FACILITY: {facility_name}
DATE: {date.today().strftime("%B %d, %Y")}

A SOP is the daily routine that keeps a facility running consistently. It tells technicians what to check, what to record, and what to do if something looks wrong — every shift, every day, every week.

Format exactly as follows:

---
SOP TITLE: {routine_name}
SOP NUMBER: SOP-001
SYSTEMS: {systems_covered}
FREQUENCY: {frequency}
ESTIMATED TIME: [How long this takes to complete]
REVISION DATE: {date.today().strftime("%B %d, %Y")}
WRITTEN BY: UpTopFlow LLC

PURPOSE:
[Why this routine exists and what problems it prevents]

SCOPE:
[Which systems, equipment, and areas this SOP covers]

REQUIRED TOOLS AND MATERIALS:
[Everything the technician needs to bring]

REQUIRED PPE:
[Personal protective equipment for this routine]

SAFETY REMINDERS:
[Key hazards to be aware of during this routine]

PROCEDURE:

SECTION 1: [First system or area]
□ Step 1: [Check / Verify / Record / Inspect — specific item]
   Normal reading or condition: [What normal looks like]
   If abnormal: [Exactly what to do]

□ Step 2: [Next check]
   Normal reading or condition: [What normal looks like]
   If abnormal: [Exactly what to do]

[Continue for all checks in this section]

SECTION 2: [Second system or area]
[Same format]

SECTION 3: [Third system or area if applicable]
[Same format]

DOCUMENTATION REQUIREMENTS:
[What must be logged, where, and in what format after completing this SOP]

SIGN-OFF:
Completed by: _____________ Date: _______ Time: _______
Reviewed by: _____________ Date: _______

ESCALATION:
[Who to call if any check reveals an abnormal condition]
Primary: _______________
Backup: _______________
---

Rules for writing this SOP:
- Use checkbox format for every check so technicians can physically mark completion
- Every check must include what normal looks like AND what to do if abnormal
- Include specific readings, temperatures, pressures, and values where available
- If a specific value is not in the source data write [VERIFY NORMAL RANGE WITH ENGINEER]
- Group checks by physical location so the technician walks the facility efficiently
- Keep language simple and direct — written for a technician not an engineer

Use this technical data to make the SOP specific and accurate:
{summary[:8000]}"""

    print(f"Generating SOP: {routine_name}")

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=8096,
        messages=[{"role": "user", "content": prompt}]
    )

    content = message.content[0].text

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"SOP saved to: {output_path}")
    return content


if __name__ == "__main__":

    generate_sop(
        summary_path="../outputs/operational_summary.md",
        routine_name="Daily AI Compute Infrastructure Walkthrough",
        systems_covered="Power, Cooling, BMS, Compute Racks",
        frequency="Daily — Every Shift",
        facility_name="Test Data Center",
        output_path="../outputs/SOP-OPS-001.md"
    )

    print("\nSOP generated. Check your outputs folder.")