---
MOP TITLE: High Density Rack Power Inspection — High Density AI Compute Rack
MOP NUMBER: MOP-POW-001
SYSTEM: Power
REVISION DATE: June 28, 2026
WRITTEN BY: UpTopFlow LLC

---

APPROVAL AND SIGN-OFF:
No step in this procedure may begin until all required signatures below are obtained and this document is formally authorized.

| Role | Name | Signature | Date |
|---|---|---|---|
| Prepared By | | | |
| Technically Reviewed | | | |
| Safety Reviewed | | | |
| Approved By | | | |
| Authorized By | | | |

---

ACTIVITY SUMMARY:

Project / Activity Name: High Density Rack Power Inspection — High Density AI Compute Rack
Facility: Test Data Center
Planned Date: June 28, 2026
Estimated Start Time: _______________
Estimated Completion Time: _______________
Actual Start Time: _______________
Actual Completion Time: _______________

Scope of Work: This procedure covers a structured power inspection of the High Density AI Compute Rack within the Test Data Center, including verification of upstream power sources, confirmation of branch circuit loading and integrity, inspection of the Power Distribution Unit (PDU) feeding the rack, verification of redundant power feed status, thermal scan assessment of all energized power components at and above the rack level, and documentation of all findings. The inspection encompasses the rack's serving PDU, its redundant PDU pair, the upstream MDP-UPS-O/P-3 feeder circuit, associated UPS system output, and all branch circuits terminating at the High Density AI Compute Rack. No planned power interruption to the rack is anticipated under normal execution; however, single-feed risk mitigation procedures are active throughout.

Participating Parties: Data Center Operations (DCO) Team Lead and Control Personnel; Switching Team; Verification and Metering Team; Rack Assessment Personnel; Electrical Maintenance Vendor (Exquis / Blackstone as applicable); Client Services Group (CSG) Representative; Facility Safety Officer

Key Risks:
1. Inadvertent loss of power to the High Density AI Compute Rack due to single-source feed configuration or unintended breaker operation during inspection
2. Arc flash exposure during energized inspection of PDU branch circuits, MDP-UPS-O/P-3, or upstream distribution panels
3. Incomplete load transfer verification resulting in undetected equipment outage affecting the High Density AI Compute Rack's compute workloads

Mitigation:
1. Confirm dual-source vs. single-source configuration of the High Density AI Compute Rack before any switching action; notify Client Services Group and client of single-source risk; do not operate any breaker without explicit Team 1 authorization and verified redundancy confirmation
2. Enforce arc flash PPE rated to the applicable incident energy level for all energized panel access; maintain NFPA 70E approach boundaries; prohibit unescorted vendor access to energized equipment
3. Assign dedicated rack assessment personnel to physically confirm equipment operational status at the High Density AI Compute Rack following every switching or verification action; require verbal confirmation back to Team 1 before proceeding

Contingency Plan: If execution must be aborted mid-procedure, Team 1 shall immediately issue a stop-work order to all teams via radio. All breakers shall be left in their current state — no partial switching actions shall be initiated or completed without full Team 1 authorization. The High Density AI Compute Rack shall be verified for power presence at both feeds before personnel stand down. The Facility Engineer and Vendor Lead shall be notified immediately. If the rack has lost power unexpectedly, the relevant PDU branch circuit or feeder shall be restored per the fallback procedures defined in the IF SOMETHING GOES WRONG section before any personnel depart. All LOTO devices remain in place until formally authorized for removal. A full incident log shall be documented and provided to management before the activity is rescheduled.

---

EQUIPMENT PHOTO:

[PHOTO REQUIRED: High Density AI Compute Rack — insert onsite photo showing equipment label, rack location identifier, nameplate data, current power feed configuration, and physical condition at time of inspection. Photo must be taken before any work begins and attached to this MOP record.]

---

PURPOSE:
This procedure establishes the controlled, step-by-step process for inspecting the power delivery system serving the High Density AI Compute Rack within the Test Data Center, ensuring all upstream and rack-level power components are operating within design parameters, all readings are within specification, and all findings are documented without causing unplanned disruption to rack operations.

---

SCOPE:
This procedure applies to the following equipment and systems:

- High Density AI Compute Rack (Test Data Center — primary subject of inspection)
- Serving PDU and its redundant PDU pair (per facility redundancy map — confirm PDU assignment from as-built drawings before execution)
- MDP-UPS-O/P-3 (Main Distribution Panel — UPS Output, located in Main Building EE Room 3)
- MDP-UPS-I/P-3 (Main Distribution Panel — UPS Input, located in Annex Building A-2F, UPS Room 3)
- WAB 3 Panel (located in Annex Building A-2F, UPS Room 3)
- LVMSB-3 (Low Voltage Main Switchboard 3, located in Annex Building A-2F, LVMSB Room 3)
- UPS-3A, UPS-3B, UPS-3C (located in Annex Building A-2F, UPS Room 3)
- Battery Banks — System 3 (located in Annex Building A-2F, Battery Room 3)
- Branch circuits from serving PDU terminating at the High Density AI Compute Rack
- Genset 1 (primary backup power source) and Genset 5 (fallback via MISS system)

This procedure does not include planned power interruption to the High Density AI Compute Rack under normal execution. Any deviation requiring a controlled outage must be escalated to the Facility Engineer and Authorized By signatory before proceeding.

---

PREREQUISITES:

All prerequisites must be confirmed true and documented before Step 1 is executed. No exceptions.

1. All approval and sign-off signatures on the cover page are obtained and the MOP is formally authorized.
2. A current, verified one-line diagram showing the complete power path from LVMSB-3 through MDP-UPS-O/P-3, through the serving PDU, to the High Density AI Compute Rack has been obtained from facility engineering and confirmed against as-built conditions.
3. The power source configuration of the High Density AI Compute Rack (dual-source or single-source) has been confirmed and documented. If single-source, client has been notified of the associated risk in writing.
4. The redundant PDU pair assignment for the serving PDU of the High Density AI Compute Rack has been confirmed from facility documentation and verified as active and carrying load.
5. A pre-activity thermal scan of all in-scope panels and the High Density AI Compute Rack has been completed within the prior 2–4 weeks by the EPM vendor. Thermal scan report and any rectification items are in hand.
6. Electrical load analysis of the serving PDU and upstream distribution has been completed by DCO within the prior 1–4 weeks. Results are documented.
7. All rectification items identified during thermal scanning and load analysis have been reviewed by the Facility Engineer. Items requiring immediate corrective action have been addressed or formally accepted as known risks before this procedure begins.
8. Client advisory notifications have been issued no later than 3 months, 2 months, and 1 month before the planned date. Client confirmation of awareness is on file.
9. No client access or change requests are pending for the High Density AI Compute Rack. All requests have been submitted and processed no later than 3 days before this activity. Day-of requests will not be accepted.
10. All equipment tagging has been completed no later than 3 days before this activity. Yellow tags are affixed to all equipment scheduled for inspection. Red or Orange tags are affixed to all equipment that will not be included in this cycle.
11. Toolbox meeting has been conducted no later than 1 hour before the first step is executed. All team members have confirmed understanding of roles, risks, communication protocol, and fallback procedures.
12. All personnel roles in the Required Personnel table are filled. Every assigned person is present, identified, and in confirmed radio communication.
13. All required PPE has been issued, inspected, and confirmed appropriate for the arc flash incident energy level applicable to each work area.
14. Calibrated digital multimeter (current calibration certificate verified) is on-site and assigned to the Verification Team.
15. All LOTO devices, locks, tags, and hasps required for this procedure are on-site and assigned to designated personnel.
16. Genset 1 is confirmed operational and available. Genset 5 and the MISS system transfer path are confirmed available as fallback. Both genset operators have been briefed.
17. Client Services Group (CSG) representative is on-site or reachable by phone and radio throughout the duration of this procedure.
18. Facility Engineer has confirmed that no other maintenance activities, power transfers, or switching operations are in progress or planned concurrently on any in-scope system.
19. All enclosure doors, panel covers, and cable management are in their normal closed and secured state prior to inspection commencement.
20. Advisory has been sent to TIM Teams and client notifying them that the activity is about to start.

---

REQUIRED PPE:

All PPE requirements below are mandatory minimums. The Facility Safety Officer or designated safety reviewer must confirm arc flash incident energy calculations from the facility's current arc flash study before personnel approach any energized equipment. If incident energy at any location exceeds the PPE class specified below, upgrade PPE to the required rating before proceeding.

**Data Center Floor — High Density AI Compute Rack and PDU Inspection Area:**
- Arc flash rated face shield or arc flash hood, minimum 8 cal/cm² incident energy rating (confirm against facility arc flash study)
- Arc flash rated gloves, voltage class appropriate to circuit voltage (minimum Class 00 for 120/208V circuits; Class 0 or higher if 480V circuits are present at PDU)
- Arc flash rated long-sleeve shirt and pants or arc flash suit — minimum 8 cal/cm²
- Safety glasses worn under face shield or hood at all times
- Hard hat, Class E rated
- Leather over-gloves over insulating rubber gloves
- Safety-toed boots, leather, non-conductive sole
- No loose jewelry, watches, rings, or metallic accessories

**EE Room 3 — MDP-UPS-O/P-3 Inspection Area:**
- Arc flash rated hood or face shield, minimum 40 cal/cm² (confirm against facility arc flash study — MDP panels carry higher incident energy)
- Arc flash rated suit, minimum 40 cal/cm²
- Voltage-rated rubber insulating gloves, Class 2 (rated to 17,000V) with leather over-gloves
- Hard hat, Class E
- Safety glasses worn under arc flash hood
- Safety-toed leather boots, non-conductive sole
- Cotton or arc-rated underlayers only — no synthetics

**Annex Building A-2F — UPS Room 3 (MDP-UPS-I/P-3, WAB 3 Panel):**
- Same PPE as EE Room 3 above — confirm incident energy from arc flash study
- Additional: Insulated tools rated for voltage class present

**Annex Building A-2F — Battery Room 3:**
- Arc flash rated face shield, minimum 8 cal/cm²
- Acid-resistant gloves (in addition to voltage-rated insulating gloves)
- Safety glasses
- Acid-resistant apron or arc flash suit with acid-resistant outer layer
- Hard hat, Class E
- Ventilation must be confirmed operational before entry — risk of hydrogen gas accumulation
- No open flames, sparks, or non-intrinsically safe electrical equipment permitted in Battery Room 3

**Annex Building A-2F — LVMSB Room 3:**
- Arc flash rated hood, minimum 40 cal/cm² (confirm against facility arc flash study — switchboard level equipment)
- Arc flash rated suit, minimum 40 cal/cm²
- Voltage-rated rubber insulating gloves, Class 2 with leather over-gloves
- Hard hat, Class E
- Safety glasses
- Safety-toed leather boots, non-conductive sole

---

SAFETY WARNINGS:

**⚠ WARNING — ARC FLASH HAZARD:** The High Density AI Compute Rack, its serving PDU, MDP-UPS-O/P-3, MDP-UPS-I/P-3, WAB 3 Panel, LVMSB-3, and all associated branch circuits are energized systems. Arc flash can cause severe burns, blindness, and death. Do not open any panel, remove any dead front, or probe any terminal without wearing PPE rated to the incident energy level calculated in the facility's current arc flash study. Confirm incident energy values from the study before approaching any equipment.

**⚠ WARNING — ENERGIZED EQUIPMENT — NO UNAUTHORIZED ACCESS:** The High Density AI Compute Rack and all upstream distribution equipment including MDP-UPS-O/P-3, MDP-UPS-I/P-3, WAB 3 Panel, and LVMSB-3 are energized under normal operating conditions. Only authorized and qualified personnel wearing appropriate PPE may approach or interact with energized equipment. Vendors must be escorted by Team 6 at all times and must not operate any panel without explicit authorization from Team 1.

**⚠ WARNING — LOCKOUT/TAGOUT (LOTO) REQUIREMENTS:** Any time a panel or circuit is de-energized for physical inspection or maintenance, LOTO must be applied immediately at the isolation point before any physical contact with internal components. LOTO must not be removed until Team 1 has explicitly authorized removal and all personnel are confirmed clear of the equipment. Unauthorized re-energization of any de-energized system is strictly prohibited and may result in fatal injury.

**⚠ WARNING — UPS SYSTEM IS NOT FULLY DE-ENERGIZED AFTER INVERTER OFF:** UPS-3A, UPS-3B, and UPS-3C remain in STS mode with battery output active and LCD display live after the inverter is switched off. The UPS output is still live and capable of delivering lethal voltage. Full de-energization of UPS-3A, UPS-3B, and UPS-3C requires opening all battery bank breakers individually in Battery Room 3 after the inverter is switched off. Do not treat inverter-off state as a safe de-energized condition.

**⚠ WARNING — HYDROGEN GAS HAZARD IN BATTERY ROOM 3:** Battery banks in Battery Room 3 generate hydrogen gas during charging and discharging. Hydrogen gas is explosive and flammable. Before entering Battery Room 3, confirm ventilation systems are operational and the space has been confirmed safe by facility personnel. No open flames, arcing tools, or non-intrinsically safe electrical equipment are permitted in Battery Room 3 at any time during this procedure.

**⚠ WARNING — SINGLE-SOURCE EQUIPMENT WILL LOSE POWER COMPLETELY:** If the High Density AI Compute Rack is confirmed as single-source fed, any interruption to its serving PDU or branch circuit will result in complete loss of power to the rack. There is no redundant feed to catch the load. Client must be specifically notified of this condition in advance. Inspect the rack's power configuration before any switching action and confirm client awareness before proceeding.

**⚠ WARNING — LVMSB-3 MAIN BREAKER MUST BE CONFIRMED OFF BEFORE TIE-BREAKER IS CLOSED:** Before closing the TIE-BREAKER at LVMSB-2 to transfer source to LVMSB-3, the LVMSB-3 main breaker must be physically confirmed in the OFF position. Failure to do so before closing the TIE-BREAKER may result in a fault condition, equipment damage, or uncontrolled energization.

**⚠ WARNING — VENDORS MUST BE CONFIRMED CLEAR BEFORE STARTUP:** Team 1 must physically confirm that no vendor personnel are present at or inside MDP-UPS-I/P-3 or any other panel scheduled for re-energization before issuing the command to close any breaker. Verbal confirmation alone is insufficient — visual verification is required.

**⚠ WARNING — PDU BRANCH CIRCUITS MUST BE SWITCHED ONE AT A TIME — DO NOT BATCH TRIP:** Branch circuits serving the High Density AI Compute Rack and all client racks fed from the serving PDU must be operated one by one, one rack at a time. Batch-tripping multiple circuits simultaneously is prohibited. Load transfer verification must be confirmed between each circuit operation.

**⚠ WARNING — MDP-UPS-O/P-3 VOLTAGE MUST BE VERIFIED AT 400V LINE-TO-LINE BEFORE PDU RE-ENERGIZATION:** Following any maintenance or switching that de-energizes MDP-UPS-O/P-3, voltage must be measured and confirmed at 400V line-to-line on both line and load sides before any PDU feeder circuit is closed. Do not close any PDU feeder on an unverified bus.

**⚠ WARNING — GENSET FAILURE IS A CREDIBLE SCENARIO:** If Genset 1 fails during this procedure, Genset 5 must be activated via the MISS system immediately. All personnel must know this fallback path before the first step is executed. Confirm Genset 5 availability and MISS system readiness as a prerequisite, not as a reactive measure.

---

ESTIMATED DURATION:

| Phase | Description | Estimated Duration |
|---|---|---|
| Phase 1 | Pre-Inspection Verification and Setup | 30 minutes |
| Phase 2 | Upstream System Status Verification (LVMSB-3, UPS System 3, MDP-UPS-O/P-3) | 45 minutes |
| Phase 3 | Serving PDU and Redundant PDU Inspection | 45 minutes |
| Phase 4 | High Density AI Compute Rack Branch Circuit and Power Inspection | 60 minutes |
| Phase 5 | Thermal Scan and Load Reading Documentation | 30 minutes |
| Phase 6 | Close-Out and Post-Inspection Verification | 30 minutes |
| **Total Estimated Duration** | | **~3 hours 30 minutes** |

Note: Duration estimates assume no unplanned findings requiring corrective action. If thermal scan or voltage readings reveal anomalies, the Facility Engineer must be notified and additional time budgeted before close-out is completed.

---

REQUIRED PERSONNEL:

| Role | Assigned Person | Contact | Minimum Qualification |
|---|---|---|---|
| Team 1 — Control Lead | TBD | _______________ | Licensed Electrician or Electrical Engineer with data center operations experience; authorized to command all switching actions; familiar with LVMSB-3, MDP-UPS-O/P-3, PDU, and UPS System 3 topology |
| Team 2 — Switching | TBD | _______________ | Licensed Electrician qualified to operate distribution-level breakers; trained in LOTO procedures; authorized to physically operate breakers at MDP-UPS-O/P-3 and serving PDU |
| Team 3 — Verification | TBD | _______________ | Qualified Electrician or Electrical Technician trained in use of calibrated digital multimeter; authorized to take voltage readings at MDP-UPS-O/P-3 and PDU; familiar with NFPA 70E approach boundaries |
| Rack Assessment — Teams 4 & 5 | TBD | _______________ | Data Center Operations Technician; trained to visually assess rack equipment operational status; in radio communication with Team 1 at all times |
| Team 6 — Vendor Escort and Assist | TBD | _______________ | Data Center Operations personnel qualified to escort and assist Exquis or Blackstone vendor personnel; familiar with all in-scope panel locations |
| Vendor Lead — Exquis / Blackstone | TBD | _______________ | Qualified electrical maintenance technician credentialed for data center electrical systems; vendor personnel must have current arc flash training and site-specific safety induction completed |
| Client Services Group (CSG) Representative | TBD | _______________ | Authorized to communicate with client regarding equipment status; available throughout the entire procedure by phone and radio |
| Facility Safety Officer | TBD | _______________ | Authorized to stop work at any time; responsible for arc flash PPE verification and LOTO compliance |

Note: All roles must be filled and all personnel must be in confirmed radio communication before Step 1 is executed. Personnel fields are editable — update assigned names when this MOP is reused for future maintenance cycles.

---

ONE-LINE DIAGRAM:

[INSERT ONE-LINE DIAGRAM HERE — obtain from facility engineering drawings. The diagram must show the complete power path including: LVMSB-3 (Annex Building A-2F, LVMSB Room 3) as upstream source; TIE-BREAKER connection between LVMSB-2 and LVMSB-3; MDP-UPS-I/P-3 (Annex Building A-2F, UPS Room 3); UPS-3A, UPS-3B, and UPS-3C with battery bank connections (Battery Room 3); WAB 3 Panel (Annex Building A-2F, UPS Room 3); MDP-UPS-O/P-3 (Main Building EE Room 3); all serving PDUs and their redundant PDU pairs (PDU 13/PDU 12, PDU 14/PDU 11, PDU 16/PDU 3, PDU 17/PDU 2); branch circuit feeds to the High Density AI Compute Rack; and Genset 1 and Genset 5 with MISS system transfer path. Diagram must be verified against as-built conditions by the Facility Engineer before execution begins.]

---

STEP BY STEP PROCEDURE:

---

**PHASE 1 — PRE-INSPECTION VERIFICATION AND SETUP**

**Step 1.** Confirm that all approval and sign-off signatures on the MOP cover page are complete and the document is formally authorized. Do not proceed if any signature is missing.

**Step 2.** Confirm that the toolbox meeting has been completed within the past hour and that all team members are present, have confirmed understanding of their roles, and are in active radio communication.

**Step 3.** Confirm that all prerequisite items listed in the PREREQUISITES section have been verified and documented.

**Step 4.** Confirm that the pre-activity thermal scan report and electrical load analysis report are in hand and have been reviewed by the Facility Engineer.

**Step 5.** Confirm PPE compliance for every team member assigned to each work area per the REQUIRED PPE section. The Facility Safety Officer must visually verify PPE for all personnel before any team moves to their work area.

**Step 6.** Confirm that the calibrated digital multimeter is on-site, calibration certificate is current, and the instrument is assigned to Team 3 — Verification.

**Step 7.** Confirm that all LOTO devices, locks, tags, and hasps are on-site, inventoried, and assigned to designated personnel.

**Step 8.** Confirm Genset 1 operational status with the facility operations team. Document genset status in the activity log.

**Step 9.** Confirm Genset 5 availability and MISS system transfer path with facility operations. Document confirmation in the activity log.

**Step 10.** Confirm that the CSG Representative has sent the pre-activity advisory to TIM Teams and the client of the High Density AI Compute Rack notifying them the activity is about to start.

**Step 11.** Confirm the power source configuration (dual-source or single-source) of the High Density AI Compute Rack from as-built documentation and physically verify at the rack by inspecting the number of active power cords and their PDU source assignments.

[PHOTO REQUIRED: High Density AI Compute Rack — photograph showing all active power cords, their routing, and PDU connection labels. Capture both A-feed and B-feed connections if dual-source, or document single-source configuration. Include rack ID label in frame.]

**VERIFY CHECKPOINT 1:** Confirm the High Density AI Compute Rack power source configuration is documented as either dual-source (A-feed and B-feed active) or single-source. If single-source, confirm in writing that the CSG Representative has notified the client of the complete power loss risk during any branch circuit or PDU switching on the serving feed. Do not proceed until this confirmation is on record.

**Step 12.** Confirm the serving PDU assignment for the High Density AI Compute Rack from facility documentation and physically verify at the PDU that the assigned branch circuit is active and feeding the rack.

**Step 13.** Confirm the redundant PDU assignment for the serving PDU (per facility redundancy map) and verify that the redundant PDU is energized and carrying load.

[PHOTO REQUIRED: Serving PDU — photograph showing PDU nameplate, branch circuit breaker positions, and load indicator lights or metering display. Include PDU ID label in frame.]

[PHOTO REQUIRED: Redundant PDU — photograph showing redundant PDU nameplate and active status, confirming it is energized and operational.]

**VERIFY CHECKPOINT 2:** Confirm serving PDU is energized and the branch circuit assigned to the High Density AI Compute Rack is active. Confirm redundant PDU is energized and operational. Both conditions must be true before proceeding to Phase 2.

---

**PHASE 2 — UPSTREAM SYSTEM STATUS VERIFICATION**

**Step 14.** Team 1 — Control Lead directs Team 3 — Verification to proceed to MDP-UPS-O/P-3 in Main Building EE Room 3 to perform upstream status verification. Team 3 must don full arc flash PPE rated to the incident energy level at EE Room 3 before entering.

**Step 15.** Team 3 — Verification visually inspects MDP-UPS-O/P-3 exterior for any physical damage, warning indicators, active alarm lights, or abnormal conditions. Document all observations in the activity log.

[PHOTO REQUIRED: MDP-UPS-O/P-3 — photograph of full panel exterior showing nameplate, overall condition, any visible alarms or indicator lights, and panel identification label.]

**Step 16.** Team 3 — Verification, with appropriate PPE in place, opens the MDP-UPS-O/P-3 panel door and performs a visual inspection of internal components for signs of overheating, discoloration, burning, loose connections, or physical damage. Do not contact any internal component. Document all observations.

[PHOTO REQUIRED: MDP-UPS-O/P-3 — interior inspection photograph showing bus bars, breakers, and wiring. Ensure all thermal anomalies or discoloration are captured if present.]

**Step 17.** Team 3 — Verification uses the calibrated digital multimeter to take voltage readings at the line side of MDP-UPS-O/P-3. Record readings for all three phases line-to-line and line-to-neutral in Appendix C — Voltage Verification Checklist.

**VERIFY CHECKPOINT 3:** MDP-UPS-O/P-3 line-side voltage must read 400V line-to-line across all three phases (±5% tolerance per facility design parameters). If any reading deviates beyond tolerance, stop. Notify Team 1 — Control Lead and Facility Engineer before proceeding. Do not proceed with downstream inspection until voltage anomaly is resolved or formally accepted by the Facility Engineer.

**Step 18.** Team 3 — Verification takes voltage readings at the load side of MDP-UPS-O/P-3 at the feeder breaker position for the serving PDU of the High Density AI Compute Rack. Record readings in Appendix C.

**VERIFY CHECKPOINT 4:** MDP-UPS-O/P-3 load-side voltage at the serving PDU feeder must read 400V line-to-line (±5%). Document actual readings, technician name, verifier name, and time in Appendix C. Both technician and verifier must sign the entry before proceeding.

**Step 19.** Team 3 — Verification closes the MDP-UPS-O/P-3 panel door and confirms it is secured. Report panel status to Team 1 — Control Lead via radio.

**Step 20.** Team 1 — Control Lead directs Team 3 to proceed to Annex Building A-2F, UPS Room 3 to perform UPS System 3 status verification. Team 3 must confirm PPE is appropriate for UPS Room 3 work area before entering.

**Step 21.** Team 3 — Verification visually inspects UPS-3A, UPS-3B, and UPS-3C LCD displays and indicator panels for operational mode, active alarms, battery status, input voltage, output voltage, and load percentage. Record all readings in the activity log.

[PHOTO REQUIRED: UPS-3A LCD display — photograph showing current operational mode, input/output voltage, load percentage, and any active alarms.]

[PHOTO REQUIRED: UPS-3B LCD display — same as above.]

[PHOTO REQUIRED: UPS-3C LCD display — same as above.]

**VERIFY CHECKPOINT 5:** UPS-3A, UPS-3B, and UPS-3C must all be confirmed in normal operating mode (not STS mode, not bypass, not fault). No critical alarms should be active. If any UPS unit is not in normal mode or has an active critical alarm, stop. Notify Team 1 — Control Lead and Facility Engineer before proceeding.

**Step 22.** Team 3 — Verification visually inspects MDP-UPS-I/P-3 exterior for any physical damage, warning indicators, active alarms, or abnormal conditions. Document observations.

[PHOTO REQUIRED: MDP-UPS-I/P-3 — exterior photograph showing nameplate, overall condition, and panel identification label.]

**Step 23.** Team 3 — Verification visually inspects WAB 3 Panel exterior for any physical damage, active alarms, or abnormal conditions. Document observations.

[PHOTO REQUIRED: WAB 3 Panel — exterior photograph showing nameplate, overall condition, and panel identification label.]

**Step 24.** Team 3 — Verification reports all UPS Room 3 observations to Team 1 — Control Lead via radio and documents findings in the activity log.

**Step 25.** Team 1 — Control Lead directs Team 3 to proceed to Annex Building A-2F, LVMSB Room 3 to perform LVMSB-3 status verification. Team 3 must confirm PPE is appropriate for LVMSB Room 3 before entering.

**Step 26.** Team 3 — Verification visually inspects LVMSB-3 exterior for any physical damage, warning indicators, active alarms, breaker trip indicators, or abnormal conditions. Document all observations.

[PHOTO REQUIRED: LVMSB-3 — exterior photograph showing full switchboard face, nameplate, breaker positions, and any visible indicators or alarms.]

**Step 27.** Team 3 — Verification reports LVMSB-3 observations to Team 1 — Control Lead via radio and documents findings in the activity log.

**VERIFY CHECKPOINT 6:** All upstream systems — LVMSB-3, MDP-UPS-I/P-3, WAB 3 Panel, UPS-3A, UPS-3B, UPS-3C, and MDP-UPS-O/P-3 — have been visually inspected and voltage verified at MDP-UPS-O/P-3. All systems are confirmed in normal operating condition. Findings are documented. Team 1 — Control Lead must confirm receipt of all Team 3 reports before Phase 3 begins.

---

**PHASE 3 — SERVING PDU AND REDUNDANT PDU INSPECTION**

**Step 28.** Team 1 — Control Lead directs Team 2 — Switching and Team 3 — Verification to proceed to the serving PDU location in Main Building Data Center 1. All personnel must don arc flash PPE appropriate for the PDU work area before approaching.

**Step 29.** Team 3 — Verification performs a visual inspection of the serving PDU exterior, including nameplate verification, branch circuit breaker positions, indicator lights, and metering display. Document all observations and confirm PDU identity matches the as-built assignment for the High Density AI Compute Rack.

[PHOTO REQUIRED: Serving PDU — photograph of full PDU exterior including nameplate, all branch circuit breaker positions (on/off state), metering display readings, and PDU identification label.]

**Step 30.** Team 3 — Verification records the current metering readings from the serving PDU display, including total load (amperes or kW), individual phase voltages, and any alarms. Document in the activity log.

**VERIFY CHECKPOINT 7:** Serving PDU metering readings are within the design load parameters for the High Density AI Compute Rack's assigned branch circuit. Voltage at PDU output must be consistent with upstream readings. Document actual readings, technician, verifier, and time in Appendix C. Both must sign before proceeding.

**Step 31.** Team 3 — Verification performs a visual inspection of the redundant PDU exterior, including nameplate verification, branch circuit breaker positions, indicator lights, and metering display. Document all observations.

[PHOTO REQUIRED: Redundant PDU — photograph of full PDU exterior including nameplate, branch circuit breaker positions, metering display readings, and PDU identification label.]

**Step 32.** Team 3 — Verification records the current metering readings from the redundant PDU display. Document in the activity log.

**VERIFY CHECKPOINT 8:** Redundant PDU is confirmed energized, operational, and showing load transfer capacity available. Redundant PDU is confirmed carrying appropriate load. Document actual readings, technician, verifier, and time in Appendix C.

**Step 33.** Team 3 — Verification, with Team 2 present, opens the serving PDU panel door and performs a visual internal inspection for signs of overheating, discoloration, burning, loose connections, or physical damage at the main input breaker, bus bars, and all branch circuit breakers. Do not contact any internal component. Document all observations.

[PHOTO REQUIRED: Serving PDU interior — photograph showing main input breaker, bus bars, and branch circuit breaker assembly. Capture any thermal anomalies, discoloration, or physical damage observed.]

**Step 34.** Team 3 — Verification closes the serving PDU panel door and confirms it is secured. Report to Team 1 — Control Lead via radio.

**VERIFY CHECKPOINT 9:** Serving PDU and redundant PDU inspections are complete. All findings are documented. Serving PDU panel door is confirmed closed and secured. Team 1 — Control Lead has received and acknowledged all Team 3 reports before Phase 4 begins.

---

**PHASE 4 — HIGH DENSITY AI COMPUTE RACK BRANCH CIRCUIT AND POWER INSPECTION**

**Step 35.** Team 1 — Control Lead confirms with Team 3 — Verification and Teams 4 & 5 — Rack Assessment that all upstream and PDU inspections are complete and all systems are confirmed in normal operating condition before Phase 4 begins.

**Step 36.** Teams 4 & 5 — Rack Assessment proceed to the High Density AI Compute Rack location on the data center floor. Confirm rack identity from nameplate and asset tag against the as-built equipment list.

[PHOTO REQUIRED: High Density AI Compute Rack — photograph showing full rack front view with rack ID label, asset tag, and current operational status of all installed equipment clearly visible (power indicators, status lights).]

**Step 37.** Teams 4 & 5 perform a visual inspection of the High Density AI Compute Rack exterior, including rack condition, cable management, physical integrity of the rack enclosure, and accessibility to all power connections.

**Step 38.** Teams 4 & 5 inspect all power cords installed in the High Density AI Compute Rack for physical integrity — check for fraying, abrasion, kinking, heat damage, or improper strain relief. Document all observations.

[PHOTO REQUIRED: High Density AI Compute Rack — close-up photograph of all power cord connections at the rack PDU inlets, showing power cord condition, labeling, and connection seating.]

**Step 39.** Teams 4 & 5 verify the branch circuit breaker labeling on the serving PDU against the actual rack power cord connections. Confirm that breaker labels match the rack assignment per as-built documentation.

**VERIFY CHECKPOINT 10:** High Density AI Compute Rack identity is confirmed. All power cords are physically intact, properly labeled, and correctly connected to the assigned branch circuits on the serving PDU. Any discrepancy between as-built documentation and field conditions must be reported to Team 1 — Control Lead and Facility Engineer immediately before proceeding.

**Step 40.** Team 3 — Verification proceeds to the serving PDU and uses the calibrated digital multimeter to measure the current draw on the branch circuit assigned to the High Density AI Compute Rack. Record phase current readings (L1, L2, L3 as applicable) in Appendix C.

**VERIFY CHECKPOINT 11:** Branch circuit current readings for the High Density AI Compute Rack are within the rated ampacity of the branch circuit breaker and within the expected load range from the pre-activity electrical load analysis. If current readings exceed 80% of the branch circuit breaker rating, notify Team 1 — Control Lead and Facility Engineer immediately before proceeding.

**Step 41.** Team 3 — Verification measures the voltage at the branch circuit termination at the serving PDU assigned to the High Density AI Compute Rack. Record readings in Appendix C.

**VERIFY CHECKPOINT 12:** Branch circuit voltage at the serving PDU must be within acceptable tolerance of 400V line-to-line (or applicable nominal voltage for the branch circuit). Document actual readings, technician, verifier, and time. Both must sign Appendix C entry before proceeding.

**Step 42.** Teams 4 & 5 — Rack Assessment perform a visual and operational status check of all equipment installed in the High Density AI Compute Rack, confirming all units are powered on, LEDs and status indicators are normal, and no equipment has gone offline or is showing fault conditions. Document the status of every equipment unit in the activity log.

[PHOTO REQUIRED: High Density AI Compute Rack — full rear view photograph showing all power connections, cable routing, and rear-panel equipment status indicators.]

**VERIFY CHECKPOINT 13:** All equipment installed in the High Density AI Compute Rack is confirmed operational and showing normal status indicators. No units are offline or in fault state. Teams 4 & 5 report findings to Team 1 — Control Lead via radio. Team 1 acknowledges receipt before Phase 5 begins.

---

**PHASE 5 — THERMAL SCAN AND LOAD READING DOCUMENTATION**

**Step 43.** Team 1 — Control Lead directs the Vendor Lead (Exquis or Blackstone) to perform a thermal scan of the High Density AI Compute Rack, the serving PDU, and the redundant PDU using a calibrated infrared thermal imaging camera. Vendor Lead must be escorted by Team 6 at all times during this phase.

**Step 44.** Vendor Lead performs thermal imaging of the High Density AI Compute Rack from front and rear, capturing all power components, PDU inlets, and cable connections. Document all findings. Flag any thermal anomaly exceeding facility-defined temperature rise thresholds for immediate reporting.

[PHOTO REQUIRED: High Density AI Compute Rack — thermal image (infrared) of rack front showing temperature distribution across all installed equipment and power components. Attach thermal image file to MOP record.]

[PHOTO REQUIRED: High Density AI Compute Rack — thermal image (infrared) of rack rear showing power cord connections and rear PDU temperature distribution.]

**Step 45.** Vendor Lead performs thermal imaging of the serving PDU, capturing all branch circuit breakers, bus bars, and main input breaker. Document all findings and flag any anomalies.

[PHOTO REQUIRED: Serving PDU — thermal image (infrared) of PDU interior showing bus bars, branch circuit breakers, and main input breaker temperature distribution.]

**Step 46.** Vendor Lead performs thermal imaging of the redundant PDU. Document all findings.

[PHOTO REQUIRED: Redundant PDU — thermal image (infrared) showing operational temperature distribution.]

**Step 47.** Vendor Lead compiles all thermal imaging findings into a field report and presents findings to Team 1 — Control Lead.

**VERIFY CHECKPOINT 14:** Thermal scan of the High Density AI Compute Rack, serving PDU, and redundant PDU is complete. All thermal images are captured and attached to the MOP record. Any thermal anomaly exceeding facility-defined thresholds has been reported to Team 1 — Control Lead and Facility Engineer. Team 1 — Control Lead has reviewed and acknowledged all thermal findings before Phase 6 begins. If a critical thermal anomaly is found, execute the IF SOMETHING GOES WRONG procedure and notify the Facility Engineer before proceeding.

**Step 48.** Team 3 — Verification records final load readings from the serving PDU metering display and the redundant PDU metering display. Document all readings including total load, phase voltages, phase currents, and power factor (if available) in the activity log and Appendix C.

**VERIFY CHECKPOINT 15:** Final load readings are documented for both the serving PDU and the redundant PDU. All readings are consistent with design parameters and the pre-activity electrical load analysis baseline. Any significant deviation must be reported to the Facility Engineer before the procedure is closed.

---

**PHASE 6 — CLOSE-OUT AND POST-INSPECTION VERIFICATION**

**Step 49.** Teams 4 & 5 — Rack Assessment perform a final visual walk of the High Density AI Compute Rack and all surrounding racks affected by this inspection. Confirm all equipment is operational, all power cords are properly seated, and no tools or test equipment have been left in or around the rack.

[PHOTO REQUIRED: High Density AI Compute Rack — final state photograph showing full rack front with all equipment operational indicators visible, no tools or test equipment present, and rack in normal condition.]

**Step 50.** Team 3 — Verification performs a final check of the serving PDU and redundant PDU, confirming all panel doors are closed and secured and all metering readings are normal.

[PHOTO REQUIRED: Serving PDU — final state photograph showing closed and secured panel door and current metering display reading.]

**Step 51.** Team 2 — Switching confirms that no LOTO devices were applied during this inspection procedure (inspection-only activity with no de-energization). If any LOTO devices were applied for any reason during this procedure, Team 2 must confirm all LOTO devices have been removed and all isolation points returned to their pre-activity state per Appendix B — LOTO Checklist.

**VERIFY CHECKPOINT 16:** All LOTO devices are accounted for. If LOTO was applied at any point, confirm in Appendix B — LOTO Removal Log that all devices have been removed and all isolation points are authorized for return to service. All lock and tag numbers match the application log. Authorized By signature is present in the LOTO Removal Log for every entry.

**Step 52.** All team leads report to Team 1 — Control Lead via radio confirming their work areas are clear, all tools are collected, and all equipment is in normal operating condition.

**VERIFY CHECKPOINT 17:** Team 1 — Control Lead has received confirmation from every team that their work area is clear, all tools and test equipment are collected, all panels and enclosures are closed and secured, and all in-scope equipment is in normal operational status. Document this confirmation in the activity log with the time received.

**Step 53.** Team 1 — Control Lead confirms that all monitoring systems (DCIM, BMS, UPS monitoring) show normal readings and no active alarms are present for the High Density AI Compute Rack, serving PDU, redundant PDU, or any upstream in-scope equipment.

**VERIFY CHECKPOINT 18:** Monitoring systems confirm normal status and no active alarms for all in-scope equipment. Document confirmation in the activity log.

**Step 54.** Team 1 — Control Lead notifies management that the High Density Rack Power Inspection for the High Density AI Compute Rack is complete and findings are documented.

**Step 55.** CSG Representative notifies the client of the High Density AI Compute Rack that the inspection activity is complete and that a copy of findings will be provided.

**Step 56.** If the High Density AI Compute Rack was confirmed as single-source during this inspection, Team 1 — Control Lead must flag this finding to Account Management for mandatory follow-up. Account Management must propose a Static Transfer Switch (STS) solution to the client of the High Density AI Compute Rack.

**Step 57.** Team 1 — Control Lead completes the Appendix D — Post-Activity Close-Out Checklist and obtains all required signatures. Record actual completion time in the Activity Summary section.

**Step 58.** All inspection records, photos, thermal images, voltage readings from Appendix C, and the completed close-out checklist from Appendix D are compiled and filed in the facility maintenance record system.

---

EXPECTED OUTCOME:

Upon successful completion of this procedure, the following system state is confirmed:

- **High Density AI Compute Rack:** Fully operational. All installed equipment confirmed powered on and showing normal status indicators. All power cords confirmed physically intact, properly labeled, and correctly connected to assigned branch circuits. Branch circuit current and voltage readings are within design parameters and within 80% of rated breaker capacity.
- **Serving PDU:** Confirmed energized and operational. Panel door closed and secured. Branch circuit assigned to the High Density AI Compute Rack confirmed active and within rated load. Metering display showing normal readings. No thermal anomalies detected during infrared scan.
- **Redundant PDU:** Confirmed energized and operational. Confirmed carrying load and available for transfer. No thermal anomalies detected during infrared scan.
- **MDP-UPS-O/P-3:** Confirmed energized. Line-side and load-side voltage confirmed at 400V line-to-line (±5%). No visual anomalies observed. Panel door confirmed closed and secured.
- **UPS-3A, UPS-3B, UPS-3C:** Confirmed in normal operating mode. No critical alarms active. LCD displays showing normal input/output voltage and load readings.
- **MDP-UPS-I/P-3:** Visual inspection completed. No physical anomalies observed. Panel in normal condition.
- **WAB 3 Panel:** Visual inspection completed. No physical anomalies observed. Panel in normal condition.
- **LVMSB-3:** Visual inspection completed. No physical anomalies observed. Switchboard in normal operating condition.
- **Battery Banks — System 3:** No inspection of battery internals required under this procedure (inspection-only MOP). Battery room ventilation confirmed operational at time of observation.
- **Genset 1 and Genset 5:** Confirmed available and operational at start and confirmed no activation was required during this procedure.
- **All thermal imaging:** Completed for High Density AI Compute Rack, serving PDU, and redundant PDU. All images attached to MOP record. Any findings documented and reported to Facility Engineer.
- **All monitoring systems:** Confirmed showing normal readings with no active alarms for any in-scope equipment at close-out.
- **Client notification:** CSG Representative has notified the client of the High Density AI Compute Rack that the inspection is complete.
- **Single-source flag:** If applicable, Account Management has been notified to initiate STS proposal to client.

---

IF SOMETHING GOES WRONG:

1. Team 1 — Control Lead issues an immediate stop-work order to all teams via radio. All teams acknowledge the stop-work order verbally before any action is taken.
2. All teams hold their current positions and do not operate any breaker, switch, or control without explicit authorization from Team 1 — Control Lead.
3. Team 1 — Control Lead assesses the nature of the problem. If equipment has gone offline or power has been lost to any rack, proceed to step 4. If a safety emergency (injury, arc flash, fire) has occurred, call emergency services immediately and activate facility emergency response procedures before any other action.
4. **If the High Density AI Compute Rack or any rack has lost power unexpectedly:** Teams 4 & 5 immediately proceed to the affected rack and confirm which equipment has gone offline. Do not attempt to restore power without Team 1 — Control Lead authorization. Report findings to Team 1 and CSG Representative immediately.
5. CSG Representative contacts the client of the High Density AI Compute Rack immediately to advise of the unexpected power loss and confirm which operations are impacted. Do not restore power without client awareness.
6. Team 1 — Control Lead determines whether the power loss was caused by a branch circuit breaker trip, PDU main breaker trip, or upstream fault.
7. **If branch circuit breaker tripped:** Team 2 — Switching may restore the tripped branch circuit breaker at the serving PDU under Team 1 authorization only. After restoration, Teams 4 & 5 confirm the High Density AI Compute Rack equipment has returned to normal. Report to Team 1.
8. **If redundant PDU circuit needs reset:** Team 2 resets the relevant redundant PDU circuit under Team 1 authorization. Verify load transfer restored. Teams 4 & 5 confirm rack equipment status.
9. **If Genset 1 fails:** Team 1 — Control Lead immediately directs facility operations to activate Genset 5 via the MISS system. Do not delay — activate the fallback path without waiting for further investigation of Genset 1. Notify Facility Engineer simultaneously.
10. **If a thermal anomaly is detected during Phase 5 that exceeds facility-defined thresholds:** Stop Phase 5 at the point of discovery. Vendor Lead documents the finding and presents it to Team 1 — Control Lead and Facility Engineer. Do not close out the procedure until the Facility Engineer has reviewed and dispositioned the finding in writing. If the anomaly represents an immediate risk, initiate a controlled de-energization of the affected circuit per a separate MOP — do not attempt de-energization under this inspection MOP without Facility Engineer authorization.
11. **If any personnel are injured:** Stop all work immediately. Call emergency services. Facility Safety Officer takes command of the work site. No work resumes until the Facility Safety Officer authorizes return to work. Notify facility management immediately.
12. Document the abort — record in the activity log: time of stop-work order, nature of the problem, current state of all in-scope equipment at time of abort, and all actions taken after the stop-work order.
13. Leave all equipment in a confirmed safe and stable state. Do not leave any equipment in a transitional or partially-switched state. If LOTO has been applied, all LOTO devices remain in place until formally authorized for removal by Team 1 — Control Lead.
14. Notify all escalation contacts listed below of the abort, findings, and current equipment state.

---

ESCALATION CONTACTS:

Primary: _______________
Backup: _______________
Facility Engineer: _______________
Vendor Lead: _______________

---

APPENDIX A — PRE-ACTIVITY INFRASTRUCTURE VERIFICATION CHECKLIST

Complete before any step begins. All items confirmed before authorization to proceed.

| Equipment | Pre-Activity Condition | Verified By | Time |
|---|---|---|---|
| High Density AI Compute Rack | All equipment operational, power source configuration confirmed (dual/single), power cords intact and labeled | | |
| Serving PDU | Energized, metering normal, branch circuit to rack active, panel door secured | | |
| Redundant PDU | Energized, operational, carrying load, available for transfer | | |
| MDP-UPS-O/P-3 | Energized, no alarms, panel door secured, feeding serving PDU | | |
| MDP-UPS-I/P-3 | Energized, no alarms, panel in normal condition | | |
| WAB 3 Panel | Energized, no alarms, panel in normal condition | | |
| LVMSB-3 | Energized, all breakers in normal position, no alarms | | |
| LVMSB-2 / TIE-BREAKER | In normal position, TIE-BREAKER confirmed in design state | | |
| UPS-3A | In normal operating mode, no critical alarms, battery status normal | | |
| UPS-3B | In normal operating mode, no critical alarms, battery status normal | | |
| UPS-3C | In normal operating mode, no critical alarms, battery status normal | | |
| Battery Banks — System 3 | All battery bank breakers in normal closed position, battery room ventilation operational | | |
| Genset 1 | Operational and available, fuel level confirmed adequate | | |
| Genset 5 | Operational and available via MISS system, transfer path confirmed | | |
| PDU 12 (redundant pair for PDU 13) | Energized and operational, if applicable to rack assignment | | |
| PDU 11 (redundant pair for PDU 14) | Energized and operational, if applicable to rack assignment | | |
| PDU 3 (redundant pair for PDU 16) | Energized and operational, if applicable to rack assignment | | |
| PDU 2 (redundant pair for PDU 17) | Energized and operational, if applicable to rack assignment | | |
| Calibrated Digital Multimeter | Current calibration certificate verified, instrument on-site and assigned to Team 3 | | |
| Thermal Imaging Camera | Calibration verified, on-site and assigned to Vendor Lead | | |
| Pre-Activity Thermal Scan Report | On-site, reviewed by Facility Engineer, rectification items documented | | |
| Electrical Load Analysis Report | On-site, reviewed by Facility Engineer | | |
| All LOTO Devices | Inventoried, on-site, assigned to designated personnel | | |
| Client Notifications | Advisory sent 3 months, 2 months, and 1 month prior; client confirmation on file | | |
| Equipment Tags | Yellow tags on in-scope equipment; red/orange tags on excluded equipment; applied 3 days prior | | |
| Toolbox Meeting | Completed within 1 hour of first step; all personnel attendance confirmed | | |

---

APPENDIX B — LOTO CHECKLIST

Note: This procedure is designed as an inspection-only MOP under normal execution and does not include planned de-energization. LOTO application is required only if an unplanned de-energization occurs or if an anomaly discovered during inspection requires a controlled isolation under Facility Engineer authorization. Complete this log if LOTO is applied for any reason during execution.

LOTO APPLICATION LOG:

| Isolation Point | Applied By | Lock/Tag Number | Time Applied |
|---|---|---|---|
| _______________ | _______________ | _______________ | ___________ |
| _______________ | _______________ | _______________ | ___________ |
| _______________ | _______________ | _______________ | ___________ |
| _______________ | _______________ | _______________ | ___________ |

LOTO REMOVAL LOG:

| Isolation Point | Removed By | Authorized By | Time Removed |
|---|---|---|---|
| _______________ | _______________ | _______________ | ___________ |
| _______________ | _______________ | _______________ | ___________ |
| _______________ | _______________ | _______________ | ___________ |
| _______________ | _______________ | _______________ | ___________ |

---

APPENDIX C — VOLTAGE VERIFICATION CHECKLIST

All readings taken with calibrated digital multimeter. Technician and verifier must both sign each entry.

| Equipment / Location | Expected Reading | Actual Reading | Technician | Verifier | Time |
|---|---|---|---|---|---|
| MDP-UPS-O/P-3 — Line Side, Phase L1-L2 | 400V L-L (±5%) | | | | |
| MDP-UPS-O/P-3 — Line Side, Phase L2-L3 | 400V L-L (±5%) | | | | |
| MDP-UPS-O/P-3 — Line Side, Phase L1-L3 | 400V L-L (±5%) | | | | |
| MDP-UPS-O/P-3 — Load Side, Serving PDU Feeder, L1-L2 | 400V L-L (±5%) | | | | |
| MDP-UPS-O/P-3 — Load Side, Serving PDU Feeder, L2-L3 | 400V L-L (±5%) | | | | |
| MDP-UPS-O/P-3 — Load Side, Serving PDU Feeder, L1-L3 | 400V L-L (±5%) | | | | |
| Serving PDU — Output Metering Voltage, Phase A | Per PDU design nominal | | | | |
| Serving PDU — Output Metering Voltage, Phase B | Per PDU design nominal | | | | |
| Serving PDU — Output Metering Voltage, Phase C | Per PDU design nominal | | | | |
| Serving PDU — Branch Circuit to High Density AI Compute Rack, L-N | Per circuit nominal | | | | |
| Serving PDU — Branch Circuit to High Density AI Compute Rack, Current (A) | ≤80% of breaker rating | | | | |
| Redundant PDU — Output Metering Voltage | Per PDU design nominal | | | | |
| Redundant PDU — Total Load Current | Within rated capacity | | | | |
| UPS-3A — Output Voltage (from LCD display) | Per UPS design nominal | | | | |
| UPS-3B — Output Voltage (from LCD display) | Per UPS design nominal | | | | |
| UPS-3C — Output Voltage (from LCD display) | Per UPS design nominal | | | | |

---

APPENDIX D — POST-ACTIVITY CLOSE-OUT CHECKLIST

□ All in-scope equipment restored to normal operation — Confirmed by: _______________
□ All monitoring systems show normal readings, no active alarms — Confirmed by: _______________
□ All tools and test equipment removed from all work areas — Confirmed by: _______________
□ All enclosure doors closed and secured — Confirmed by: _______________
□ All LOTO devices removed and accounted for (if applicable) — Confirmed by: _______________
□ All maintenance records signed and collected — Confirmed by: _______________
□ All thermal images and voltage records attached to MOP record — Confirmed by: _______________
□ Facility Engineer has reviewed and dispositioned all findings — Confirmed by: _______________
□ Single-source equipment flag sent to Account Management (if applicable) — Sent by: _______________
□ Client notification sent — Sent by: _______________
□ Activity log closed with final completion time — Closed by: _______________

Final Close-Out Sign-Off:
Declared complete by: _____________ Title: _____________ Date: _______ Time: _______

---

APPENDIX E — RISK ASSESSMENT

| Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|
| Inadvertent power loss to the High Density AI Compute Rack due to single-source feed configuration — any branch circuit or PDU anomaly during inspection results in complete rack outage with no redundant path to maintain compute loads | Medium | Critical | Confirm power source configuration (dual or single) during Phase 1 before any switching or inspection action. If single-source, obtain written client acknowledgment of risk. Assign Teams 4 & 5 to physically monitor rack status throughout all phases. Do not operate any breaker on the serving PDU without Team 1 authorization and confirmed redundancy status. | Team 1 — Control Lead |
| Arc flash exposure during energized inspection of MDP-UPS-O/P-3, serving PDU, or branch circuit terminations — high incident energy at distribution panel level presents lethal arc flash risk to inspection personnel | Medium | Critical | Enforce arc flash PPE at or above facility-calculated incident energy rating for each work area before any panel is approached or opened. Enforce NFPA 70E approach boundaries. Prohibit unescorted vendor access to energized equipment. Facility Safety Officer must visually verify PPE compliance before Phase 2 begins. | Facility Safety Officer |
| Thermal anomaly at serving PDU or High Density AI Compute Rack power components indicating imminent failure — if not identified and acted upon, could result in unplanned outage or fire | Medium | High | Conduct post-inspection thermal scan of serving PDU, redundant PDU, and High Density AI Compute Rack during Phase 5. Vendor Lead reviews all thermal images against facility-defined temperature rise thresholds. Any exceedance triggers immediate escalation to Facility Engineer before close-out. Pre-activity thermal scan must also be completed 2–4 weeks prior as a prerequisite. | Vendor Lead / Facility Engineer |
| Genset 1 failure during inspection activity — if upstream utility or UPS system experiences an unplanned fault during inspection, Genset 1 may fail to start, leaving the High Density AI Compute Rack without backup power | Low | Critical | Confirm Genset 1 operational status as a prerequisite before Step 1. Confirm Genset 5 availability and MISS system transfer path as a prerequisite before Step 1. Brief all team leads on the Genset 5 fallback path before the activity begins. Do not assume Genset 1 will start — verify, and know the fallback path before needing it. | Team 1 — Control Lead / Facility Operations |
| Branch circuit current loading at or near 80% rated capacity on the serving PDU — high density AI compute workloads may produce current draws close to or exceeding safe operating thresholds, creating overload risk during inspection or during any load shift event | Medium | High | Obtain and review electrical load analysis from DCO within 1–4 weeks before the activity. During Phase 4, measure actual branch circuit current with calibrated multimeter and compare to rated breaker capacity. If current exceeds 80% of rated breaker ampacity, stop and notify Facility Engineer before proceeding. Flag finding for capacity planning and remediation. | Team 3 — Verification / Facility Engineer |

---

*End of MOP-POW-001 — High Density Rack Power Inspection — High Density AI Compute Rack*
*Revision Date: June 28, 2026*
*Written By: UpTopFlow LLC*