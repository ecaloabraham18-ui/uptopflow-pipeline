---
EOP TITLE: Cooling System Failure During High Density AI Workload
EOP NUMBER: EOP-001
SEVERITY: CRITICAL
REVISION DATE: June 28, 2026
WRITTEN BY: UpTopFlow LLC

---

**READ COMPLETELY BEFORE TAKING ANY ACTION**

---

## TRIGGER CONDITIONS:

This EOP applies when ALL of the following are true simultaneously:

- One or more cooling units serving Data Center 1 (Main Building) have failed, alarmed, or stopped responding to controls
- AI workloads are actively running on compute racks fed by PDU 13, PDU 14, PDU 16, or PDU 17
- Rack inlet temperatures are rising and have not stabilized within 90 seconds of cooling alarm
- UPS-3A, UPS-3B, and/or UPS-3C are in active output mode (normal or STS) serving the affected racks
- No planned maintenance window is in progress — this is an uncontrolled event

If you are in a planned EPM window and cooling fails, stop all switching activity immediately and treat this as an uncontrolled emergency. This EOP takes precedence over all active MOPs.

---

## IMMEDIATE ACTIONS — First 60 Seconds:

1. Call out the emergency verbally to everyone present on the data center floor — do not assume others see it
2. Check the Building Management System (BMS) or DCIM display for current rack inlet temperatures on all racks fed by PDU 13, PDU 14, PDU 16, and PDU 17
3. Confirm whether cooling failure is total (all units down) or partial (some units still running) — look at the physical cooling units, not just the alarm panel
4. Do NOT begin load shedding, breaker switching, or workload migration until notifications in the NOTIFY IMMEDIATELY section are complete and you have been given direction
5. Position one person physically at the MDP-UPS-O/P-3 (EE Room 3) and one person on the data center floor — maintain radio or phone contact between them for the duration of this event

---

## NOTIFY IMMEDIATELY:

On-call engineer: _______________
Facility manager: _______________
Vendor emergency line (Exquis): _______________
Vendor emergency line (Blackstone): _______________

Do not proceed past this point without reaching at least one of the above. If no one is reachable within 3 minutes, escalate to the next level of management — do not guess, do not act alone on a critical switching decision.

---

## ASSESSMENT:

**Question 1: Are rack inlet temperatures currently BELOW the critical shutdown threshold for the compute equipment in the affected racks?**

*(Check BMS, DCIM, or direct thermal sensor readout. If you do not know the threshold, answer NO.)*

**YES:** Go to PATH A
**NO:** Go to PATH B

---

## PATH A:
*(Temperatures are below critical threshold — cooling has failed but you have time to act in a controlled manner)*

**Step A1:** Confirm which specific cooling units have failed. Identify whether the failure affects only the racks served by PDU 13, PDU 14, PDU 16, PDU 17, or the entire Data Center 1 floor. Report exact scope to the on-call engineer before taking any further action.

**Step A2:** Begin controlled reduction of AI compute load in coordination with the on-call engineer and the workload owner — reduce processing load rack by rack, starting with the highest-density racks, to reduce heat output while the cooling fault is diagnosed. Do not open any PDU breakers without explicit authorization from Team 1 (Control) and the on-call engineer.

**Step A3:** Verify that UPS-3A, UPS-3B, and UPS-3C are in normal operating mode (not STS mode) and that battery banks in Battery Room 3 are intact. Confirm MDP-UPS-O/P-3 is live and reading 400V L-L. Report status to on-call engineer.

**Step A4:** Monitor rack inlet temperatures continuously. If temperatures rise to within 5°C of the critical threshold at any point during PATH A, stop PATH A immediately and execute PATH B.

**Expected outcome:** Cooling fault is contained within a controlled diagnostic window. AI workloads are partially reduced. Temperatures stabilize or decline. On-call engineer and Exquis vendor are engaged and en route. No unplanned equipment shutdowns have occurred.

---

## PATH B:
*(Temperatures are at or above critical threshold — equipment is in immediate danger of thermal shutdown or damage)*

**Step B1:** Immediately notify all active workload owners that emergency load shedding is in progress — contact CSG (Client Services Group) to relay to affected clients. Do not wait for client confirmation before proceeding. Safety of equipment and personnel takes priority.

**Step B2:** Begin emergency load shedding on the affected racks. Working with the person positioned at MDP-UPS-O/P-3 in EE Room 3, shut down branch circuits one by one per client rack on PDU 13, PDU 14, PDU 16, and PDU 17 — do NOT batch-trip or open the PDU main breaker all at once. Follow the branch-by-branch sequence: PDU 13 (30 circuits), PDU 14 (60 circuits), PDU 16 (30 circuits), PDU 17 (60 circuits). Announce each circuit before opening it.

**Step B3:** As each branch circuit is opened, have the person on the data center floor physically walk the racks and confirm which equipment has powered down. Report any equipment that has gone dark to CSG immediately. For single-source equipment (equipment without a redundant PDU feed), full power loss is expected — confirm this against the pre-existing equipment list. If the equipment list is not available, treat all equipment as potentially single-source.

**Step B4:** After load has been shed and temperatures begin to decline, do NOT re-energize any branch circuits until the cooling system fault has been identified, resolved, and confirmed stable by the on-call engineer. Confirm that redundant PDUs are carrying transferred loads — PDU 13 load to PDU 12, PDU 14 load to PDU 11, PDU 16 load to PDU 3, PDU 17 load to PDU 2.

**Step B5:** If power loss to the entire UPS System 3 is required (complete cooling failure with no recovery path), execute the UPS shutdown sequence only under direct instruction from the on-call engineer: open MDP-UPS-O/P-3 main breaker → press Inverter OFF on UPS-3A, UPS-3B, UPS-3C one by one → open MDP-UPS-I/P-3 main input breaker → open WAB 3 branch circuits and WAB 3 main breaker → open battery bank breakers one by one in Battery Room 3. Do not assume UPS is de-energized after inverter off — UPS remains live in STS mode until battery bank breakers are individually opened.

**Step B6:** If Genset 1 fails or is unavailable during this event, activate Genset 5 via the MISS system immediately. Confirm with Team 1 (Control) that the switchover is complete before taking any further switching actions.

**Expected outcome:** Heat-producing compute load is removed from the affected racks. Rack inlet temperatures decline and stabilize. UPS-3A, UPS-3B, and UPS-3C remain in a known and confirmed state. Affected clients have been notified. The data center floor is stable and under observation. No personnel have been exposed to energized equipment without proper authorization and confirmation.

---

## DO NOT ATTEMPT:

**DO NOT open PDU main breakers (PDU 13, 14, 16, or 17) without first turning off all branch circuits one by one.** Sudden loss of all branch circuits simultaneously removes all load from the redundant PDU pair at once and creates an uncontrolled and unverified load state.

**DO NOT assume UPS-3A, UPS-3B, or UPS-3C are de-energized because the inverter has been turned off.** After Inverter OFF, each UPS enters STS mode — it is still live, the LCD is still active, and alarms will be present. UPS is only fully de-energized after battery bank breakers in Battery Room 3 have been individually opened.

**DO NOT take any voltage readings or open any panels at MDP-UPS-O/P-3, MDP-UPS-I/P-3, WAB 3, or LVMSB-3 unless you have confirmed the full UPS shutdown sequence has been completed and verified by Team 3 (Verification) using a calibrated meter.**

**DO NOT close the TIE-BREAKER at LVMSB-2 to re-energize LVMSB-3 unless the LVMSB-3 main breaker has been confirmed in the OFF position.** Closing into an energized bus is a life-safety hazard.

**DO NOT re-energize any PDU feeder at MDP-UPS-O/P-3 unless the MDP has been confirmed at 400V line-to-line on both line side and load side.** Energizing a PDU without voltage verification can cause undetected faults to propagate to rack equipment.

**DO NOT turn on PDU branch circuits all at once during any restoration sequence.** Inrush current from simultaneous re-energization of high-density AI compute racks can trip upstream breakers and cause a secondary outage. Re-energize by client rack group only.

**DO NOT accept or act on any workload migration or equipment access requests from clients during this emergency.** All client requests require a minimum of 3 days lead time under normal operations. During an active emergency, all access decisions go through CSG and the on-call engineer only.

**DO NOT attempt to restart failed cooling equipment without Exquis or a qualified cooling vendor on-site or directing the action remotely.** Unauthorized restart of failed mechanical or refrigerant-based cooling systems can cause compressor damage, refrigerant release, or fire.

---

## STABILIZATION:

Proceed through the following steps in order only after the immediate emergency has been contained — meaning temperatures are declining, load has been shed to a safe level, and the on-call engineer has confirmed it is safe to begin stabilization:

1. **Confirm cooling system status.** Obtain a written or verbal confirmation from Exquis or the responsible cooling vendor that the cooling fault has been identified and either repaired or that a temporary cooling solution (portable CRACs, temporary precision cooling units, increased airflow from adjacent zones) is in place and confirmed operational.

2. **Verify UPS System 3 state.** Confirm UPS-3A, UPS-3B, and UPS-3C are in normal mode (not STS mode) and battery banks in Battery Room 3 are intact and fully connected. If any UPS unit is in STS mode, investigate the cause before re-energizing any load.

3. **Verify MDP-UPS-O/P-3 voltage.** Team 3 (Verification) must take voltage readings on both line side and load side of MDP-UPS-O/P-3 in EE Room 3 and confirm 400V line-to-line before any PDU feeder is re-closed.

4. **Restore PDU feeders in sequence.** For each PDU in the order PDU 13 → PDU 14 → PDU 16 → PDU 17: Team 1 (Control) authorizes, Team 3 closes the PDU feeder at MDP-UPS-O/P-3, then Team 4 closes the PDU main input breaker. Confirm each PDU is live before moving to the next.

5. **Re-energize branch circuits by client rack group.** For each PDU, restore branch circuits one by one per client rack group — not all at once. Team 5 physically walks the racks simultaneously to confirm equipment is coming back online as expected. Any equipment found unexpectedly off must be reported to CSG immediately before that rack's circuit is re-closed.

6. **Verify load transfer has reversed correctly.** Confirm that loads have transferred back from redundant PDUs to their primary PDUs: PDU 12 → PDU 13, PDU 11 → PDU 14, PDU 3 → PDU 16, PDU 2 → PDU 17. Both the primary and redundant PDU in each pair must be confirmed operational before the rack group is considered restored.

7. **Conduct floor walk and visual inspection.** After all branch circuits are restored, Teams 4 and 5 conduct a complete visual inspection of all racks in Data Center 1. Look for any equipment still off, any physical signs of heat damage (discoloration, smell, abnormal indicator lights), and any rack that did not come back as expected.

8. **Conduct post-event thermal scan.** DCO or designated facility staff perform an immediate thermal scan of all panels and racks involved in this event. Any hot spots identified are to be flagged as rectification items and reported to the facility manager and Exquis before the facility is returned to full production status.

9. **Confirm with on-call engineer that Data Center 1 is stable.** Obtain explicit verbal or written confirmation. Do not declare the event closed unilaterally.

10. **Notify all affected clients through CSG** that their systems are restored and that a full incident report will follow within 24 hours. Single-source equipment clients must receive an immediate follow-up from Account Management to begin the STS (Static Transfer Switch) proposal process.

---

## POST-INCIDENT DOCUMENTATION:

The following must be recorded and submitted within 24 hours of the incident being declared stable:

**What must be recorded:**

- Exact time cooling alarm was first triggered and by whom it was observed
- Time each notification was made (on-call engineer, facility manager, Exquis, Blackstone) and whether contact was successful on the first attempt
- Which PDUs were affected and which branch circuits were opened, in what order, and at what time
- Peak rack inlet temperatures recorded during the event and which racks reached them
- Which equipment went offline during load shedding — include rack ID, client name, equipment type, and whether it was single-source or dual-source
- UPS-3A, UPS-3B, and UPS-3C state at the time of the event and throughout (normal, STS, shutdown)
- Whether Genset 1 was running during the event and whether Genset 5 was activated
- Cooling fault root cause as identified by Exquis or the cooling vendor, if available within 24 hours
- Results of the post-event thermal scan
- Any deviations from this EOP and the reason for each deviation

**Who records it:**

- Team 1 (Control) is responsible for maintaining a real-time log during the event
- DCO (Data Center Operations) compiles the full incident report using Team 1's log, CSG communications, and thermal scan results
- Exquis submits a separate vendor incident report covering the cooling fault findings

**Where it goes:**

- Completed incident report submitted to the Facility Manager and Data Center Management within 24 hours
- Copy to CSG for client communication file
- Copy to the Exquis and Blackstone vendor files
- Flagged rectification items from thermal scan added to the next scheduled EPM scope
- All single-source equipment findings forwarded to Account Management for STS proposal initiation

---

## SIGN-OFF:

Incident declared stable by: _________________________ Date: _______________ Time: _______________

Reviewed by: _________________________ Date: _______________

---