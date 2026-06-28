---
QUICK REFERENCE: High Density Rack Power Inspection
FACILITY: Test Data Center
WRITTEN BY: UpTopFlow LLC
DATE: June 28, 2026

---

**SAFETY WARNINGS:**
1. PDUs 13, 14, 16, and 17 carry live high-voltage feeds — do not open panels without confirmed upstream isolation and lockout/tagout applied.
2. UPS-3A, UPS-3B, and UPS-3C remain energized in STS mode after inverter shutdown — treat all UPS output terminals as live until battery breakers are opened.
3. LVMSB-3 and MDP-UPS-O/P-3 retain stored energy after switching — wait for full discharge confirmation before touching internal components.

---

**BEFORE YOU START:**
□ Confirm client rack shutdown acknowledgment received at least 3 days before this inspection
□ Confirm yellow equipment tags are applied to all PDUs being inspected (PDU 13, 14, 16, 17)
□ Confirm MDP-UPS-O/P-3 output voltage reads 400V Line-to-Line before proceeding

---

**STEPS:**
1. Attend toolbox meeting with the DCO team 1 hour before starting work.
2. Verify Genset 1 is online and ready; confirm Genset 5 is standing by via the MISS system as fallback.
3. Confirm redundant PDU pairs are active: PDU 12 covering PDU 13, PDU 11 covering PDU 14, PDU 3 covering PDU 16, and PDU 2 covering PDU 17.
4. Notify the client that rack power transfer to redundant PDUs is beginning now.
5. Shut down PDU 13 branch circuits one by one, verifying each client rack transfers to PDU 12 before moving to the next circuit.
6. Shut down PDU 14 branch circuits one by one, verifying each client rack transfers to PDU 11 before moving to the next circuit.
7. Shut down PDU 16 branch circuits one by one, verifying each client rack transfers to PDU 3 before moving to the next circuit.
8. Shut down PDU 17 branch circuits one by one, verifying each client rack transfers to PDU 2 before moving to the next circuit.
9. Apply lockout/tagout to PDU 13, PDU 14, PDU 16, and PDU 17 at their local breakers.
10. Perform visual and thermal inspection on PDU 13, PDU 14, PDU 16, and PDU 17 — record any anomalies on the inspection sheet.
11. Replace PDU 13 and PDU 16 dead front panels (allow 30 minutes per unit).
12. Remove lockout/tagout only after all maintenance tasks on each PDU are signed off.
13. Restore PDU branch circuits in reverse order — bring up one circuit at a time and confirm rack load returns from redundant PDU.
14. Confirm MDP-UPS-O/P-3 output reads 400V Line-to-Line after all PDUs are restored.
15. Notify the client that all racks are confirmed back on primary PDU feeds and inspection is complete.

---

**IF SOMETHING GOES WRONG:**
Stop immediately. Do not improvise.
Call: _______________
Backup: _______________

---

**DONE WHEN:** All PDUs 13, 14, 16, and 17 are restored to normal feed, all branch circuits confirmed live, client notified, and inspection sheet is signed off.

---

Reviewed by: _____________ Date: _______