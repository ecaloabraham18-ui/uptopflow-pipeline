import os
import anthropic
from datetime import date
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def get_photo_reference(equipment_name, photos_dir="../photos"):
    """
    Checks if an onsite photo exists for the given equipment name.
    Returns the photo path if found, or a placeholder string if not.
    Photos should be named to match equipment names with hyphens replacing spaces.
    Example: PDU-13.jpg, UPS-3A.jpg, LVMSB-3.jpg
    """
    safe_name = equipment_name.replace(" ", "-").replace("/", "-")
    extensions = [".jpg", ".jpeg", ".png"]
    for ext in extensions:
        photo_path = os.path.join(photos_dir, f"{safe_name}{ext}")
        if os.path.exists(photo_path):
            return f"[PHOTO: {photo_path}]"
    return f"[PHOTO REQUIRED: {equipment_name} — insert onsite photo showing equipment label, location, and current state]"


def generate_mop(summary_path, task_name, equipment_name, system_type,
                 facility_name, output_path, personnel_names=None):
    """
    Generates a complete Method of Procedure (MOP).

    Parameters:
        summary_path: Path to the operational summary markdown file
        task_name: Name of the task being performed
        equipment_name: Primary equipment this MOP covers
        system_type: System type (Power, Cooling, BMS, etc.)
        facility_name: Name of the facility
        output_path: Where to save the generated MOP
        personnel_names: Optional dict of role to assigned person name.
                        Example: {
                            "Team 1 Control Lead": "John Smith",
                            "Team 2 Switching": "Maria Garcia",
                            "Team 3 Verification": "TBD"
                        }
                        If not provided, fields will be left blank for manual entry.
    """

    with open(summary_path, 'r', encoding='utf-8') as f:
        summary = f.read()

    # Build personnel section based on whether names were provided
    if personnel_names:
        personnel_rows = "\n".join([
            f"| {role} | {name} | _______________ | [Verify qualification] |"
            for role, name in personnel_names.items()
        ])
        personnel_section = f"""
| Role | Assigned Person | Contact | Minimum Qualification |
|------|----------------|---------|----------------------|
{personnel_rows}

Note: All roles must be filled and all personnel must be in radio communication before the first step is executed.
Personnel fields are editable — update assigned names when this MOP is reused for future maintenance cycles.
"""
    else:
        personnel_section = """
| Role | Assigned Person | Contact | Minimum Qualification |
|------|----------------|---------|----------------------|
| Team 1 Control Lead | _______________ | _______________ | Senior DCO Engineer or qualified Shift Lead |
| Team 2 Switching | _______________ | _______________ | Qualified Electrician with switching authorization |
| Team 3 Verification | _______________ | _______________ | Qualified Electrician or DCO Engineer |
| Team 4 Floor Patrol | _______________ | _______________ | DCO Staff — visual inspection qualified |
| Vendor Lead | _______________ | _______________ | Qualified EPM vendor technician |

Note: All roles must be filled and all personnel must be in radio communication before the first step is executed.
Personnel fields are editable — update assigned names when this MOP is reused for future maintenance cycles.
"""

    # Get photo reference for primary equipment
    photo_ref = get_photo_reference(equipment_name)

    prompt = f"""You are a technical documentation specialist for mission-critical data center facilities. Generate a complete Method of Procedure (MOP) using the information below.

TASK: {task_name}
EQUIPMENT: {equipment_name}
SYSTEM: {system_type}
FACILITY: {facility_name}
DATE: {date.today().strftime("%B %d, %Y")}
EQUIPMENT PHOTO STATUS: {photo_ref}

Format exactly as follows:

---
MOP TITLE: {task_name} — {equipment_name}
MOP NUMBER: MOP-{system_type[:3].upper()}-001
SYSTEM: {system_type}
REVISION DATE: {date.today().strftime("%B %d, %Y")}
WRITTEN BY: UpTopFlow LLC

APPROVAL AND SIGN-OFF:
No step in this procedure may begin until all required signatures below are obtained and this document is formally authorized.

| Role                  | Name | Signature | Date |
|-----------------------|------|-----------|------|
| Prepared By           |      |           |      |
| Technically Reviewed  |      |           |      |
| Safety Reviewed       |      |           |      |
| Approved By           |      |           |      |
| Authorized By         |      |           |      |

ACTIVITY SUMMARY:
Project / Activity Name: {task_name} — {equipment_name}
Facility: {facility_name}
Planned Date: {date.today().strftime("%B %d, %Y")}
Estimated Start Time: _______________
Estimated Completion Time: _______________
Actual Start Time: _______________
Actual Completion Time: _______________
Scope of Work: [One paragraph summary of exactly what this MOP covers and what systems are affected]
Participating Parties: [All teams, vendors, and roles involved]
Key Risks: [Top 3 risks for this specific activity]
Mitigation: [How each risk is controlled]
Contingency Plan: [What happens if execution must be aborted mid-procedure]

PURPOSE:
[One sentence explaining what this procedure accomplishes]

SCOPE:
[Which equipment and systems this covers — use exact equipment names from the source data]

PREREQUISITES:
[Number every prerequisite. Everything that must be confirmed true before any step begins.]

REQUIRED PPE:
[List PPE required for each work area. Be specific to voltage class and arc flash rating.]

SAFETY WARNINGS:
[Every safety hazard in bold. Include arc flash, LOTO requirements, energized equipment, battery hazards, hydrogen gas, single-fed equipment risks, and unauthorized re-energization. Use exact equipment names from the source data.]

ESTIMATED DURATION:
[Total estimated time with phase breakdown]

REQUIRED PERSONNEL:
{personnel_section}

ONE-LINE DIAGRAM:
[INSERT ONE-LINE DIAGRAM HERE — obtain from facility engineering drawings. Must show upstream source, switchboard, MDP panels, UPS systems, WAB panels, PDU relationships, and affected loads. Insert and verify against as-built conditions before execution.]

STEP BY STEP PROCEDURE:

For every step follow these rules:
- Number every step sequentially across all phases
- One discrete action per step only
- Use exact equipment names from the source data
- Add VERIFY CHECKPOINT after every load transfer, voltage verification, LOTO application or removal, equipment restoration, and system status confirmation
- Every VERIFY CHECKPOINT must state the specific reading or condition required before proceeding
- Flag every irreversible action with POINT OF NO RETURN before the step
- Add photo placeholders using format: [PHOTO REQUIRED: description of what the photo should show]

[Generate all phases and numbered steps here]

EXPECTED OUTCOME:
[Exact system state after successful completion. List every piece of in-scope equipment and its confirmed operational status.]

IF SOMETHING GOES WRONG:
[Numbered abort steps in sequence. Who to call. What state to leave equipment in if halted mid-procedure.]

ESCALATION CONTACTS:
Primary: _______________
Backup: _______________
Facility Engineer: _______________
Vendor Lead: _______________

---

APPENDIX A — PRE-ACTIVITY INFRASTRUCTURE VERIFICATION CHECKLIST
Complete before any step begins. All items confirmed before authorization to proceed.

| Equipment | Pre-Activity Condition | Verified By | Time |
|-----------|----------------------|-------------|------|
[Generate one row per piece of in-scope equipment from the source data]

---

APPENDIX B — LOTO CHECKLIST

LOTO APPLICATION LOG:
| Isolation Point | Applied By | Lock/Tag Number | Time Applied |
|----------------|-----------|-----------------|-------------|
| _______________ | _______________ | _______________ | ___________ |
| _______________ | _______________ | _______________ | ___________ |

LOTO REMOVAL LOG:
| Isolation Point | Removed By | Authorized By | Time Removed |
|----------------|-----------|---------------|-------------|
| _______________ | _______________ | _______________ | ___________ |
| _______________ | _______________ | _______________ | ___________ |

---

APPENDIX C — VOLTAGE VERIFICATION CHECKLIST
All readings taken with calibrated digital multimeter. Technician and verifier must both sign.

| Equipment / Location | Expected Reading | Actual Reading | Technician | Verifier | Time |
|---------------------|-----------------|---------------|-----------|---------|------|
[Generate one row per voltage verification point from the source data]

---

APPENDIX D — POST-ACTIVITY CLOSE-OUT CHECKLIST

□ All in-scope equipment restored to normal operation — Confirmed by: _______________
□ All monitoring systems show normal readings, no active alarms — Confirmed by: _______________
□ All tools and test equipment removed from all work areas — Confirmed by: _______________
□ All enclosure doors closed and secured — Confirmed by: _______________
□ All LOTO devices removed and accounted for — Confirmed by: _______________
□ All maintenance records signed and collected — Confirmed by: _______________
□ Client notification sent — Sent by: _______________
□ Activity log closed with final completion time — Closed by: _______________

Final Close-Out Sign-Off:
Declared complete by: _____________ Title: _____________ Date: _______ Time: _______

---

APPENDIX E — RISK ASSESSMENT

| Risk | Likelihood | Impact | Mitigation | Owner |
|------|-----------|--------|-----------|-------|
[Generate 3 to 5 risks specific to this procedure and equipment from the source data]

---

Use this technical data to make the procedure specific and accurate:
{summary[:15000]}"""

    print(f"Generating MOP: {task_name} (streaming...)")

    content = ""
    with client.messages.stream(
        model="claude-sonnet-4-6",
        max_tokens=32000,
        messages=[{"role": "user", "content": prompt}]
    ) as stream:
        for text in stream.text_stream:
            content += text
            print(text, end="", flush=True)

    print(f"\nMOP saved to: {output_path}")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return content


def generate_eop(summary_path, emergency_scenario, systems_affected,
                 facility_name, output_path):
    """
    Generates a complete Emergency Operating Procedure (EOP).
    """

    with open(summary_path, 'r', encoding='utf-8') as f:
        summary = f.read()

    prompt = f"""You are a technical documentation specialist for mission-critical data center facilities. Generate a complete Emergency Operating Procedure (EOP).

EMERGENCY: {emergency_scenario}
SYSTEMS AFFECTED: {systems_affected}
FACILITY: {facility_name}
DATE: {date.today().strftime("%B %d, %Y")}

Format exactly as follows:

---
EOP TITLE: {emergency_scenario}
EOP NUMBER: EOP-001
SEVERITY: CRITICAL
REVISION DATE: {date.today().strftime("%B %d, %Y")}
WRITTEN BY: UpTopFlow LLC

READ COMPLETELY BEFORE TAKING ANY ACTION

TRIGGER CONDITIONS:
[Exactly what must be happening for this EOP to apply — be specific]

IMMEDIATE ACTIONS — First 60 Seconds:
1. [Action]
2. [Action]
3. [Action]
4. [Action]
5. [Action]

NOTIFY IMMEDIATELY:
On-call engineer: _______________
Facility manager: _______________
Vendor emergency line: _______________

ASSESSMENT:
Question 1: [Yes or No question only]
YES: Go to PATH A
NO: Go to PATH B

PATH A:
Step A1: [Action]
Step A2: [Action]
Expected outcome: [What should happen]

PATH B:
Step B1: [Action]
Step B2: [Action]
Expected outcome: [What should happen]

DO NOT ATTEMPT:
[Forbidden actions and why — be specific to this emergency and equipment]

STABILIZATION:
[Steps once immediate emergency is contained — in logical order]

POST-INCIDENT DOCUMENTATION:
[What must be recorded and reported within 24 hours — who records it and where it goes]

SIGN-OFF:
Incident declared stable by: _____________ Date: _______ Time: _______
Reviewed by: _____________ Date: _______
---

Rules for writing this EOP:
- Every decision point must be yes or no only — never maybe
- Every path must end in a defined outcome or escalation
- Use plain language readable under stress in 30 seconds
- No paragraphs in the immediate actions section — numbered steps only
- Safety always wins over equipment preservation
- If in doubt the default action is always escalate never guess
- Use exact equipment names from the source data

Use this technical data to make the EOP specific and accurate:
{summary[:15000]}"""

    print(f"Generating EOP: {emergency_scenario} (streaming...)")

    content = ""
    with client.messages.stream(
        model="claude-sonnet-4-6",
        max_tokens=32000,
        messages=[{"role": "user", "content": prompt}]
    ) as stream:
        for text in stream.text_stream:
            content += text
            print(text, end="", flush=True)

    print(f"\nEOP saved to: {output_path}")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return content


def generate_quick_reference(summary_path, procedure_title,
                              system_type, facility_name, output_path):
    """
    Generates a one-page quick reference card for field use.
    Maximum 15 steps. Readable in 30 seconds under pressure.
    """

    with open(summary_path, 'r', encoding='utf-8') as f:
        summary = f.read()

    prompt = f"""You are writing a field quick reference card for a data center technician. This must be readable in 30 seconds under pressure.

PROCEDURE: {procedure_title}
SYSTEM: {system_type}
FACILITY: {facility_name}

Generate a ONE PAGE quick reference card with this exact format:

---
QUICK REFERENCE: {procedure_title}
FACILITY: {facility_name}
WRITTEN BY: UpTopFlow LLC
DATE: {date.today().strftime("%B %d, %Y")}

SAFETY WARNINGS:
1. [Most critical hazard in one sentence — use exact equipment name]
2. [Second most critical hazard in one sentence]
3. [Third most critical hazard in one sentence]

BEFORE YOU START:
□ [Prerequisite 1]
□ [Prerequisite 2]
□ [Prerequisite 3]

STEPS:
1. [Action — specific, one sentence, exact equipment name]
2. [Action]
3. [Action]
[Maximum 15 steps total]

IF SOMETHING GOES WRONG:
Stop immediately. Do not improvise.
Call: _______________
Backup: _______________

DONE WHEN: [One sentence describing completed state]

Reviewed by: _____________ Date: _______
---

Rules:
- Maximum 15 steps total
- Every step is one sentence
- No paragraphs anywhere
- No explanations just actions
- Use exact equipment names from the source data
- Plain language a junior technician can follow under pressure

Source data:
{summary[:4000]}"""

    print(f"Generating quick reference: {procedure_title}")

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1500,
        messages=[{"role": "user", "content": prompt}]
    )

    content = message.content[0].text

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Quick reference saved to: {output_path}")
    return content


if __name__ == "__main__":

    # Example with optional personnel names
    # Remove personnel_names parameter to leave fields blank for manual entry
    generate_mop(
        summary_path="outputs/operational_summary.md",
        task_name="High Density Rack Power Inspection",
        equipment_name="High Density AI Compute Rack",
        system_type="Power",
        facility_name="Test Data Center",
        output_path="outputs/MOP-POW-001.md",
        personnel_names={
            "Team 1 Control Lead": "TBD",
            "Team 2 Switching": "TBD",
            "Team 3 Verification": "TBD",
            "Vendor Lead": "TBD"
        }
    )

    generate_eop(
        summary_path="outputs/operational_summary.md",
        emergency_scenario="Cooling System Failure During High Density AI Workload",
        systems_affected="Cooling, Power, Compute Racks",
        facility_name="Test Data Center",
        output_path="outputs/EOP-COOL-001.md"
    )

    generate_quick_reference(
        summary_path="outputs/operational_summary.md",
        procedure_title="High Density Rack Power Inspection",
        system_type="Power",
        facility_name="Test Data Center",
        output_path="outputs/QUICK-REF-POW-001.md"
    )

    print("\nAll procedures generated. Check your outputs folder.")