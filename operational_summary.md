# Annual Electrical Preventive Maintenance MOP — Extracted Operational Information
## Data Center 1 — Main Building

---

## 1. DOCUMENT OVERVIEW

This is a Method of Procedure (MOP) for the Annual Electrical Preventive Maintenance (EPM) of the electrical distribution system in Data Center 1. It covers the controlled shutdown, physical maintenance, and restart of PDUs, MDP panels, UPS systems, WAB panels, and the LVMSB feeding those PDUs. The document defines team roles, shutdown/startup sequences, maintenance tasks, fallback steps, and client communication requirements.

---

## 2. KEY SYSTEMS AND EQUIPMENT MENTIONED

### Power Distribution Units (PDUs) — Data Center Floor
| PDU | Branch Circuits | Redundant Pair | Location |
|-----|----------------|----------------|----------|
| PDU 13 | 30 | PDU 12 | Main Bldg. DC 1 |
| PDU 14 | 60 | PDU 11 | Main Bldg. DC 1 |
| PDU 16 | 30 | PDU 3 | Main Bldg. DC 1 |
| PDU 17 | 60 | PDU 2 | Main Bldg. DC 1 |
| PDU 13A | Not specified | Redundant supply | Main Bldg. EE RM 3 / Telco |
| PDU 14A | Not specified | Redundant supply | Main Bldg. EE RM 3 / Telco |
| PDU 16A | Not specified | Redundant supply | Main Bldg. EE RM 3 / Telco |

### Upstream Electrical Distribution
| Equipment | Location |
|-----------|----------|
| MDP-UPS-O/P-3 (Output MDP) | Main Bldg. EE Room 3 |
| MDP-UPS-I/P-3 (Input MDP) | Annex Bldg. A-2F, UPS Room 3 |
| WAB 3 Panel | Annex Bldg. A-2F, UPS Room 3 |
| LVMSB-3 (Low Voltage Main Switchboard) | Annex Bldg. A-2F, LVMSB Room 3 |
| LVMSB-2 (upstream/tie source) | Annex Bldg. A-2F, LVMSB Room 2 |
| TIE-BREAKER / Bypass Breaker | LVMSB-2 Panel |

### UPS Systems
| Equipment | Location | Quantity |
|-----------|----------|----------|
| UPS-3A | Annex Bldg. A-2F, UPS Room 3 | 1 unit |
| UPS-3B | Annex Bldg. A-2F, UPS Room 3 | 1 unit |
| UPS-3C | Annex Bldg. A-2F, UPS Room 3 | 1 unit |
| Battery Banks (System 3) | Annex Bldg. A-2F, Battery Room 3 | Multiple breakers |

**UPS System note:** 3 units per system (3A, 3B, 3C). UPS operates in STS mode when inverter is off but input is live. Fully shuts down only after battery breakers are opened.

### Backup Power
| Equipment | Notes |
|-----------|-------|
| Genset 1 | Primary genset for affected system |
| Genset 5 | Fallback if Genset 1 fails — supplied via MISS system |

### Vendors
- **Exquis** — Primary electrical maintenance vendor
- **Blackstone** — Referenced for PDU 16 and verification activities

---

## 3. CRITICAL OPERATIONAL PARAMETERS

| Parameter | Value | Context |
|-----------|-------|---------|
| PDU 13 branch circuits | 30 | Shutdown and restart one by one per client rack |
| PDU 14 branch circuits | 60 | Shutdown and restart one by one per client rack |
| PDU 16 branch circuits | 30 | Shutdown and restart one by one per client rack |
| PDU 17 branch circuits | 60 | Shutdown and restart one by one per client rack |
| MDP output voltage (startup verification) | 400V Line-to-Line | Must be confirmed before energizing PDUs |
| UPS state after inverter off | STS mode | LCD still active, alarm present, running on battery |
| UPS state after battery breakers opened | Fully shut down | No output — confirmed de-energized |
| Client advisory lead time — first notice | 3 months before EPM | |
| Client advisory lead time — second follow-up | 2 months before EPM | |
| Client advisory lead time — third follow-up | 1 month before EPM | |
| Client request cutoff | 3 days before EPM | No requests accepted on day of activity |
| Pre-thermal scan window | 2–4 weeks before activity | By EPM vendor |
| Electrical load analysis window | 1–4 weeks before activity | By DCO |
| Rectification items list | 2–4 weeks before activity | By DCO |
| Vendor meeting | 1 week before (or 1 month + 1 week) | By DCO |
| Equipment tagging | 3 days before activity | Yellow = will be maintained, Red/Orange = will not |
| Toolbox meeting | 1 hour before activity | By DCO |
| PDU dead front replacement duration | 30 mins each | PDU 13, PDU 16 confirmed; implied for others |
| PDU branch circuit maintenance duration | 15 mins per PDU | PDU 14, 16, 17 |
| PDU 13A/14A/16A maintenance duration | 45 mins | EE Room 3 |
| LVMSB-3 maintenance duration | 80 mins | |
| MDP-UPS-O/P-3 dead front replacement | 30 mins | Parallel with LVMSB-3 maintenance |
| WAB-3 dead front replacement | 30 mins | Parallel with LVMSB-3 maintenance |
| MDP-UPS-O/P-3 panel maintenance | 35 mins | |
| MDP-UPS-I/P-3 dead front replacement | 30 mins | Parallel with MDP-UPS-O/P-3 maintenance |
| WAB-3 panel maintenance | 35 mins | |
| LVMSB-3 dead front replacement | 30 mins | Parallel with WAB-3 maintenance |
| MDP-UPS-I/P-3 panel maintenance | 35 mins | |

---

## 4. KEY PROCEDURES OR PROCESSES DESCRIBED

### PRE-ACTIVITY (Weeks to Days Before)
1. Request clients to access racks and verify equipment list
2. Check and update equipment list: quantity, power source config (dual/single), brand/model
3. Create EPM advisory and equipment list attachment per client
4. Get management approval of advisory template
5. Email advisory 3 months out → 2 months out → 1 month out
6. Account managers (TIM AMs) verify client confirmations
7. Confirm equipment list is still valid 1 month before
8. Confirm any client special requests 1 week before
9. DCO conducts electrical load analysis (1–4 weeks before)
10. Vendor conducts pre-thermal scan (2–4 weeks before)
11. DCO lists all rectification items (2–4 weeks before)
12. DCO holds vendor preparation meeting (1 week before)
13. DCO tags equipment: Yellow = will be maintained, Red/Orange = will not be maintained (3 days before)
14. DCO conducts toolbox meeting (1 hour before)
15. DCO assigns teams for the activity
16. Send advisory to TIM Teams and clients that activity is about to start

---

### PDU SHUTDOWN SEQUENCE (Repeated for each PDU — PDU 13, 14, 16, 17)
1. Team 1 (Control) commands Team 2 to proceed
2. Team 2 turns off branch circuits **one by one per client rack** (do not batch-trip)
3. Team 3 monitors and verifies load has transferred to redundant PDU:
   - PDU 13 → PDU 12
   - PDU 14 → PDU 11
   - PDU 16 → PDU 3
   - PDU 17 → PDU 2
4. Teams 4 & 5 simultaneously walk the racks to confirm no equipment has gone offline
   - Any equipment found OFF → report to CSG → CSG verifies with client whether operations are impacted
5. After all branch circuits are off, Team 2 opens PDU main breaker → relays to Team 1
6. Team 1 opens the PDU feeder breaker at MDP-UPS-O/P-3 (EE Room 3) → relays to Team 6
7. Team 6 and vendor proceed with physical maintenance of the PDU

---

### PDU 13A, 14A, 16A SHUTDOWN SEQUENCE
1. Team 1 commands teams to proceed
2. Team 2 turns off PDU 13A, 14A, 16A branch circuits
3. Team 3 verifies load transferred to redundant supplies (monitored from EE Rooms 1 & 2)
4. Teams 4 & 5 check racks in EE Rooms 3 & 5 for any equipment going offline
5. Team 2 opens main breakers → relays to Team 1
6. Team 1 opens feeders at MDP-UPS-O/P-3 → relays to Team 6
7. Team 6 and vendor maintain PDU 13A, 14A, 16A (EE Room 3 and Telco Areas)

---

### UPS SYSTEM 3 SHUTDOWN SEQUENCE
1. Open MDP-UPS-O/P-3 main breaker (EE Room 3)
2. Press **Inverter OFF** on UPS-3A, UPS-3B, UPS-3C **one by one** → UPS enters STS mode
3. Open MDP-UPS-I/P-3 main input breaker (UPS Room 3) → UPS now on battery; LCD active with alarm
4. Open WAB 3 branch circuits, then WAB 3 main breaker (UPS Room 3)
5. Go to Battery Room 3 → open battery bank breakers **one by one** → UPS fully shut down
6. Team 2 isolates LVMSB-3 from LVMSB-2 by opening the TIE-BREAKER in LVMSB-2 panel
7. Team 2 advises all teams that LVMSB-3, WAB 3, MDP-UPS-O/P-3, and MDP-UPS-I/P-3 are ready for maintenance

---

### PRE-MAINTENANCE SAFETY VERIFICATION
- Team 3 and vendor check voltage on line side of UPS panel before work begins
- Confirm de-energized: MDP-UPS-O/P-3, MDP-UPS-I/P-3, WAB 3, LVMSB-3 and all branches

---

### PANEL MAINTENANCE SEQUENCE (Parallel Tasks)
Execute the following in parallel where indicated:
| Task | Duration | Parallel With |
|------|----------|---------------|
| Dead front replacement — MDP-UPS-O/P-3 | 30 mins | LVMSB-3 maintenance |
| Dead front replacement — WAB-3 | 30 mins | LVMSB-3 maintenance |
| Maintenance — MDP-UPS-O/P-3 | 35 mins | — |
| Dead front replacement — MDP-UPS-I/P-3 | 30 mins | MDP-UPS-O/P-3 maintenance |
| Maintenance — WAB-3 | 35 mins | — |
| Dead front replacement — LVMSB-3 | 30 mins | WAB-3 maintenance |
| Maintenance — MDP-UPS-I/P-3 | 35 mins | — |
| Maintenance — LVMSB-3 | 80 mins | — |

---

### UPS SYSTEM 3 STARTUP SEQUENCE
1. Team 1 verifies no vendors are present at MDP-UPS-I/P-3 and its breaker is OFF
2. Switch ON MDP-UPS-I/P-3 → UPS automatically comes up in STS mode
3. Go to Battery Room 3 → turn ON battery bank breakers
4. Press **Inverter ON** one by one: UPS-3A → UPS-3B → UPS-3C → UPS now in **normal mode**
5. Confirm all alarms are cleared
6. Team 1 informs Team 3 that UPS System 3 is in normal mode

---

### MDP AND PDU STARTUP SEQUENCE
1. Team 3 confirms with Team 1 that UPS System 3 is online
2. Switch ON MDP-UPS-O/P-3 main breaker
3. **Take voltage reading** on line and load side — must read **400V L-L**
4. Team 3 informs Team 1 that MDP is active
5. For each PDU (13, 14, 16, 17, 13A, 14A, 16A), repeat:
   - Team 3 switches ON PDU feeder at MDP-UPS-O/P-3 (EE Room 3)
   - Team 3 relays to Team 4 that PDU is ready
   - Team 4 switches ON PDU main input breaker
   - Team 4 gradually turns ON branches **by client rack group** (not all at once)
   - Team 5 verifies power has transferred back from redundant PDU
   - Team 6 verifies both PDUs (maintenance unit and redundant) are working

---

### POST-ACTIVITY
1. Thorough visual inspection of all equipment inside racks
2. Thermal scanning by DCO
3. Inform management that activity is complete
4. CSG updates all clients that EPM is done
5. All single-source equipment clients must be sent an STS proposal by Account Management

---

### FALLBACK PROCEDURES
- **Power loss to racks:** Turn ON the tripped breaker; reset redundant PDU circuit if needed
- **Genset 1 failure:** Switch to Genset 5 to supply the affected load via the MISS system

---

## 5. IMPORTANT WARNINGS OR RISK FACTORS

| Risk | Detail |
|------|--------|
| **Single-source equipment goes completely dark during maintenance window** | Dual-source equipment stays on via redundant PDU. Single-source equipment loses power entirely. All single-source equipment owners must be identified and notified in advance. |
| **Equipment may go offline during branch circuit switching** | Teams 4 & 5 must physically walk and verify every rack as each branch circuit is opened. Do not assume load transferred successfully. |
| **UPS is NOT fully de-energized after inverter off** | After inverter off, UPS is in STS mode and still live on battery. LCD remains active. Full shutdown requires also opening battery bank breakers individually. |
| **Voltage must be verified before and after MDP energization** | Line and load side of MDP-UPS-O/P-3 must read 400V L-L before PDUs are re-energized. |
| **LVMSB-3 main breaker must be in OFF position before bypass is switched on** | Explicitly called out as a pre-condition before closing TIE-BREAKER to re-energize. |
| **Vendors must be clear of panels before startup** | Team 1 must physically confirm no vendors are present at MDP-UPS-I/P-3 before switching it ON. |
| **PDU branches must be turned on gradually by rack group** | Not all at once — inrush load management and client verification require staged re-energization. |
| **No client requests accepted on day of activity** | All access and change requests must be submitted minimum 3 days before EPM. Day-of requests will be refused. |
| **Genset failure is a credible fallback scenario** | Genset 5 via MISS system is the defined fallback — operators must know this path before starting. |
| **Pre-thermal scan is a prerequisite** | Undetected hot spots in panels must be found and listed as rectification items before work starts — do not skip. |

---

## 6. THINGS AN OPERATOR NEEDS TO KNOW

### Team Structure — Know Your Role Before the Day
- **Team 1 (Control):** Commands all switching actions; takes voltage readings; coordinates startup sequence
- **Team 2 (Switching):** Physically operates all breakers and switches
- **Team 3 (Verification):** Monitors panel loads, confirms transfers, verifies voltages at MDP
- **Teams 4 & 5 (Rack Assessment):** Walk the floor simultaneously with every switching action — eyes on equipment
- **Team 6 (Vendor Assist):** Escorts and assists Exquis/Blackstone during all physical maintenance
- **Team 7 (Operations):** Ongoing facility operations coverage during the activity

### Redundancy Map — Must Know Before Switching
| PDU Under Maintenance | Load Transfers To |
|-----------------------|------------------|
| PDU 13 | PDU 12 |
| PDU 14 | PDU 11 |
| PDU 16 | PDU 3 |
| PDU 17 | PDU 2 |
| PDU 13A / 14A / 16A | Redundant supply via EE Rooms 1 & 2 |

### The Three Communications That Must Happen Before Any Switch
1. Control (Team 1) gives go-ahead to Switching (Team 2)
2. Switching (Team 2) confirms breaker status back to Control (Team 1)
3. Control (Team 1) relays clearance to Vendor Assist (Team 6)
- **Do not skip any relay step.** Work does not begin until the confirmation chain is complete.

### Startup Is Not the Reverse of Shutdown — Follow the Exact Sequence
- UPS must be fully online and in normal mode **before** MDP is energized
- MDP must be confirmed at 400V L-L **before** any PDU feeder is closed
- PDU feeders must be confirmed closed **before** branch circuits are turned on
- Branch circuits go on **by client rack group, not all at once**

### Single-Source Equipment — This Is the Highest Client Risk
- Identify all single-source equipment during pre-activity rack surveys
- These clients lose power completely during maintenance on their serving PDU
- After the EPM, Account Management must propose STS (Static Transfer Switch) solutions to all single-source clients

### The Pre-Thermal Scan Is Not Optional
- Must be done 2–4 weeks before the activity
- Hot spots found become rectification items — the maintenance tasks may change based on findings
- A post-activity thermal scan is also performed as part of closeout

### If Something Goes Wrong
- Equipment off unexpectedly during switching: Stop, report to CSG, verify with client before doing anything else
- Power lost to racks post-restoration: Re-close the relevant breaker; reset redundant PDU circuit
- Genset 1 fails: Activate Genset 5 via MISS system immediately — know this path before you start

### Tagging System
- **Yellow tag:** Equipment scheduled for maintenance
- **Red/Orange tag:** Equipment that will NOT be maintained this cycle
- Tags must be placed 3 days before the activity