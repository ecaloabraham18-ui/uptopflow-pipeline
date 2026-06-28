---
SOP TITLE: Daily Infrastructure Walkthrough
SOP NUMBER: SOP-001
SYSTEMS: Power, Cooling, BMS, Compute Racks
FREQUENCY: Daily — Every Shift
ESTIMATED TIME: 60–90 Minutes Per Shift
REVISION DATE: June 05, 2026
WRITTEN BY: UpTopFlow LLC

---

## PURPOSE:

This SOP establishes the minimum daily inspection requirements for TIM Data Center 1. Its purpose is to catch abnormal conditions — unusual readings, equipment alarms, physical damage, or environmental changes — before they develop into outages, equipment failures, or safety incidents.

This walkthrough is performed every shift, by every on-duty technician. It is not optional. Skipping or rushing this routine is the single most common factor in preventable data center failures.

Completing this SOP consistently protects:
- Client uptime and contractual SLA obligations
- The physical integrity of power, cooling, and compute infrastructure
- Technician safety in a high-voltage, high-density environment
- The facility's ability to detect and respond to early warning signs before they escalate

---

## SCOPE:

This SOP applies to all systems and physical areas listed below within TIM Data Center 1, Main Building and Annex Building A-2F:

**Power Distribution**
- PDUs 2, 3, 11, 12, 13, 14, 16, 17 — Data Center Floor, Main Building
- PDUs 13A, 14A, 16A — EE Room 3 / Telco Areas
- MDP-UPS-O/P-3 — EE Room 3, Main Building
- MDP-UPS-I/P-3 — UPS Room 3, Annex Building A-2F
- WAB 3 Panel — UPS Room 3, Annex Building A-2F
- LVMSB-3 — LVMSB Room 3, Annex Building A-2F
- LVMSB-2 and TIE-BREAKER — LVMSB Room 2, Annex Building A-2F

**UPS and Battery Systems**
- UPS-3A, UPS-3B, UPS-3C — UPS Room 3, Annex Building A-2F
- Battery Banks, System 3 — Battery Room 3, Annex Building A-2F

**Backup Power**
- Genset 1 — Primary genset for affected system
- Genset 5 — Fallback genset via MISS system

**Cooling Systems**
- All computer room air conditioning and air handling units serving Data Center 1
- Chilled water supply and return systems
- [VERIFY COOLING EQUIPMENT INVENTORY WITH ENGINEER — list specific unit IDs upon confirmation]

**BMS (Building Management System)**
- Central BMS dashboard and active alarm panel
- All monitored environmental sensors — temperature, humidity, leak detection

**Compute Racks**
- All client racks, Data Center Floor, Main Building
- Racks in EE Rooms 3 and 5

---

## REQUIRED TOOLS AND MATERIALS:

□ This completed SOP form — printed or loaded on facility tablet
□ Facility shift log — physical logbook or DCIM system login
□ Non-contact voltage tester (NCVT) — for visual verification only, do not open panels
□ Calibrated handheld digital multimeter — if directed by engineer to take readings
□ Calibrated infrared thermometer — for hotspot spot checks on racks and panels
□ Flashlight or headlamp — for low-light equipment rooms
□ Two-way radio or facility communication device — charged and tested before walkthrough begins
□ Facility key card and room access credentials
□ Pen or stylus for marking checkboxes and signing off
□ Camera or facility-issued mobile device — for photographing any abnormal conditions
□ Personal alarm or buddy communication plan if entering battery or UPS rooms alone

---

## REQUIRED PPE:

□ Safety-rated work boots — steel or composite toe, rated for electrical environments
□ Arc flash-rated personal protective equipment — arc rating matched to facility's calculated incident energy levels [VERIFY ARC FLASH RATING REQUIREMENTS WITH FACILITY SAFETY ENGINEER]
□ Safety glasses or face shield — required in all electrical equipment rooms
□ Electrical-rated insulating gloves — minimum Class 00 for general inspection proximity; do not open panels or touch energized parts without engineer authorization
□ High-visibility vest — when walking data center floor around active rack rows
□ Hearing protection — when inspecting generator room if unit is running

**Note:** This SOP is a visual inspection and reading verification routine only. Technicians are not authorized to open energized switchgear, PDU dead fronts, or UPS enclosures during this routine. If PPE requirements for any task during this walkthrough appear insufficient for conditions encountered, stop and call your supervisor.

---

## SAFETY REMINDERS:

**High-Voltage Hazard — Electrical Rooms**
LVMSB-3, LVMSB-2, MDP panels, and UPS rooms contain high-voltage equipment. Do not open panels. Do not reach past safety barriers. Observe and record only. Report any open panels, missing dead fronts, or exposed conductors immediately.

**UPS Battery Hazard — Battery Room 3**
Battery banks produce hydrogen gas and store substantial energy even when UPS output is off. No open flames. No sparking tools. Ensure ventilation is operational before entering. Do not touch battery terminals or inter-cell connectors.

**Redundant Power Pairs — Do Not Confuse PDU Status**
PDUs operate in redundant pairs. PDU 13 ↔ PDU 12. PDU 14 ↔ PDU 11. PDU 16 ↔ PDU 3. PDU 17 ↔ PDU 2. A single PDU showing unusual readings does not mean the pair has failed — but it must be reported immediately. Never assume load is protected without verifying both units.

**Arc Flash Risk**
Electrical equipment in this facility poses arc flash hazard. Do not approach open or damaged panels without arc flash PPE appropriate to the panel's incident energy level. If you find a panel door open that should be closed, do not close it yourself — isolate the area and call supervision.

**Do Not Reset Alarms Without Authorization**
If the BMS or UPS displays an active alarm you do not recognize, do not acknowledge or reset it without supervisor instruction. Resetting an alarm without understanding it can mask a developing failure.

**Buddy Rule — UPS and Battery Rooms**
Do not enter UPS Room 3 or Battery Room 3 alone. Confirm a second technician or supervisor is aware of your location and expected return time before entering.

---

## PROCEDURE:

---

### SECTION 1: BMS DASHBOARD — CONTROL ROOM OR MONITORING STATION
*(Complete this section first. The BMS gives you an overview of facility status before you walk the floor. Any active alarms found here will direct your attention during the physical walkthrough.)*

---

□ **Step 1: Log into BMS and verify system is online and displaying live data.**
   Normal reading or condition: BMS dashboard loads fully. All monitored points are actively updating. No "communication lost" or "sensor offline" indicators are present.
   If abnormal: If BMS is offline or not updating, escalate immediately to the on-call engineer before proceeding with the physical walkthrough. Do not rely on last-known readings as current conditions.

□ **Step 2: Review active alarm panel. Record the count and category of all active alarms.**
   Normal reading or condition: Zero active critical alarms. Minor or informational alarms, if present, are previously reviewed and acknowledged by the prior shift with notes in the shift log.
   If abnormal: Any new active alarm not documented in the prior shift log must be investigated and escalated before completing this SOP. Record alarm ID, description, and time of trigger in the shift log. Photograph the alarm display.

□ **Step 3: Check BMS-monitored temperature readings across all data center zones.**
   Normal reading or condition: All zone temperatures within facility setpoints. Typical hot-aisle/cold-aisle differential is maintained. [VERIFY TEMPERATURE SETPOINTS BY ZONE WITH ENGINEER — record approved values in the facility's baseline parameter sheet]
   If abnormal: Any zone temperature reading above the facility high-temp alarm threshold must be escalated immediately. Note which zone, current reading, and setpoint. Do not wait to confirm during physical walkthrough — call it in now.

□ **Step 4: Check BMS-monitored humidity readings across all data center zones.**
   Normal reading or condition: Relative humidity within facility setpoints. [VERIFY HUMIDITY SETPOINTS WITH ENGINEER — typical data center range is 40%–60% RH but confirm facility-specific values]
   If abnormal: Humidity above or below setpoint range must be reported to the on-call engineer. High humidity increases condensation risk. Low humidity increases static discharge risk. Both are rack-level threats.

□ **Step 5: Check all BMS-connected water leak detection sensors.**
   Normal reading or condition: All leak detection sensors show normal / no leak detected. No active leak alarms.
   If abnormal: A leak detection alarm is an immediate escalation. Record sensor location, isolate foot traffic in the affected zone, and call the on-call engineer and facility manager. Do not wait. Do not attempt to locate or address the leak yourself without instruction.

□ **Step 6: Verify BMS shows all cooling units are running and in normal operating mode.**
   Normal reading or condition: All CRAC/CRAH/AHU units show as running. No units in fault, standby override, or alarm state unexpectedly.
   If abnormal: Any cooling unit showing fault or offline unexpectedly must be reported immediately. Verify whether redundant capacity is covering the lost unit. Record unit ID, fault code, and time observed.

□ **Step 7: Review UPS system status as shown on BMS, if integrated.**
   Normal reading or condition: UPS-3A, UPS-3B, UPS-3C shown as online in normal inverter mode. No bypass, STS mode, or battery mode indicators active.
   If abnormal: Any UPS shown in STS mode, bypass mode, or battery mode must be escalated immediately. This indicates the UPS is not providing full protection. See Section 3 for UPS physical checks.

□ **Step 8: Record BMS dashboard summary in the shift log before leaving the control room.**
   Normal reading or condition: All readings normal. Shift log entry completed with timestamp, technician name, and BMS status summary.
   If abnormal: Log all alarm details before proceeding. Do not skip documentation even if you are rushing to investigate an issue.

---

### SECTION 2: DATA CENTER FLOOR — COMPUTE RACKS, PDU VISUAL CHECKS
*(Walk rack rows systematically. Do not skip rows. Physical observation catches what sensors miss.)*

---

□ **Step 1: Walk all rack rows on the data center floor. Visually confirm all client racks are powered and operational.**
   Normal reading or condition: Rack indicator lights are consistent with client equipment in normal operating state. No visible warning LEDs, no beeping, no blank rack unit slots with failed equipment visible. No equipment lying on the floor or improperly seated in racks.
   If abnormal: Any rack with equipment that appears powered off, in fault state, or showing unusual indicators must be logged. Report to CSG (Client Services Group) immediately so they can verify with the client whether operations are impacted. Do not touch client equipment.

□ **Step 2: Check that all rack doors — front and rear — are properly closed and secured.**
   Normal reading or condition: All rack doors are closed, latched, and undamaged. No doors propped open. No open cable pathways creating airflow bypass.
   If abnormal: A propped-open rack door disrupts hot-aisle/cold-aisle airflow containment and can cause zone temperature rise. Close any unsecured door that does not have a client work order associated with it. Log the rack ID and condition found.

□ **Step 3: Inspect rack cable management at the top, bottom, and rear of all racks.**
   Normal reading or condition: Cables are routed and secured. No cables hanging loose in airflow paths. No cables showing visible damage, kinks, or pulling tension against connections.
   If abnormal: Log the rack ID and describe the cable condition. Photograph if possible. Do not attempt to reroute cables without a work order.

□ **Step 4: Visually inspect PDUs 2, 3, 11, 12, 13, 14, 16, and 17 on the data center floor.**
   Normal reading or condition: All PDU status lights are green or in normal operating condition per manufacturer indicators. PDU dead front panels are in place and fully secured. No visible damage, burn marks, discoloration, or unusual odors near any PDU. No audible buzzing, crackling, or arcing sounds.
   If abnormal: Any PDU showing a fault light, missing dead front, visible damage, unusual odor, or audible arcing sound is an immediate escalation. Do not approach closer than necessary. Alert the on-call engineer immediately and isolate the area if safe to do so.

□ **Step 5: Check PDU LCD or display panel readings on each PDU — record load readings in the shift log.**
   Normal reading or condition: PDU load is within normal operating range. Redundant PDU pairs should show roughly balanced or expected load split between them. [VERIFY NORMAL LOAD RANGES PER PDU WITH ENGINEER — record baseline values in the facility parameter sheet]
   - PDU 13 (30 branch circuits) ↔ paired with PDU 12
   - PDU 14 (60 branch circuits) ↔ paired with PDU 11
   - PDU 16 (30 branch circuits) ↔ paired with PDU 3
   - PDU 17 (60 branch circuits) ↔ paired with PDU 2
   If abnormal: A PDU showing a significant load spike, load imbalance with its pair, or zero load when it should be carrying load must be escalated. A zero-load reading on an active PDU may indicate upstream breaker trip or PDU main breaker open.

□ **Step 6: Listen and observe for any unusual sounds on the data center floor — fans, cooling units, electrical equipment.**
   Normal reading or condition: Consistent fan noise from racks and cooling units. No intermittent buzzing, clicking, popping, or high-pitched electrical sounds.
   If abnormal: Any unusual electrical sound is a potential arc flash or component failure precursor. Stop. Identify the source location. Do not approach the equipment. Escalate immediately.

□ **Step 7: Check temperature at the cold aisle face of rack rows using handheld infrared thermometer at three heights — top, middle, and bottom of the rack front.**
   Normal reading or condition: Cold aisle supply temperatures are consistent and within facility setpoints. Temperature gradient from bottom to top of rack should be moderate and expected. [VERIFY COLD AISLE TEMPERATURE SETPOINTS WITH ENGINEER]
   If abnormal: A significantly elevated reading at any rack face position may indicate a cooling unit fault, airflow blockage, or containment breach. Log the reading, rack row, and position. Report to engineer.

□ **Step 8: Inspect floor tiles and raised floor areas — if applicable — for displacement, damage, or blockage.**
   Normal reading or condition: All perforated and solid floor tiles are properly seated. No tiles are displaced, cracked, or missing. No obstructions blocking supply airflow.
   If abnormal: Displaced tiles create airflow bypass and hot spots. Reseat tiles carefully. Log any damaged tiles for replacement work order.

---

### SECTION 3: EE ROOM 3 — MDP-UPS-O/P-3, PDUs 13A, 14A, 16A
*(EE Room 3, Main Building. Confirm room access and check PPE before entering.)*

---

□ **Step 1: Visually inspect MDP-UPS-O/P-3 (Output Main Distribution Panel). Check that the panel dead front is in place, fully secured, and undamaged.**
   Normal reading or condition: Panel enclosure is fully closed. Dead front is secured. No burn marks, discoloration, swelling, or physical damage on or around the panel. No unusual odors.
   If abnormal: Missing or damaged dead front on an energized panel is an immediate safety escalation. Do not touch. Do not attempt to secure. Alert supervisor and on-call engineer. Isolate the area.

□ **Step 2: Verify MDP-UPS-O/P-3 output voltage. If metering is visible on the panel display, record the line-to-line voltage reading.**
   Normal reading or condition: Output voltage is 400V line-to-line. This is the confirmed energization threshold before PDUs are fed from this panel.
   If abnormal: A reading significantly above or below 400V line-to-line must be escalated immediately. Voltage deviation at the MDP level affects all downstream PDUs simultaneously.

□ **Step 3: Visually inspect PDU 13A, PDU 14A, and PDU 16A — confirm each unit's status panel or indicator lights show normal operation.**
   Normal reading or condition: All three PDUs show normal operating status. No fault indicators. Dead fronts are in place. No visible damage or unusual odors near units.
   If abnormal: Log the specific PDU, the fault indicator or condition observed, and escalate to on-call engineer. These PDUs serve EE Room 3 and Telco areas — their redundant supplies are monitored from EE Rooms 1 and 2.

□ **Step 4: Confirm PDU 13A, 14A, and 16A branch circuit indicator status — check for any tripped breakers visible through indicator windows if equipped.**
   Normal reading or condition: All branch circuit breakers are in the ON position. No tripped breakers indicated.
   If abnormal: A tripped branch circuit breaker must be logged with the circuit number, time, and reported to the engineer before any reset attempt. Do not reset a tripped breaker without authorization.

□ **Step 5: Check for any water intrusion, condensation, or environmental damage in EE Room 3.**
   Normal reading or condition: Room is dry. No condensation on walls, ceiling, or equipment. No water stains or puddles.
   If abnormal: Any water in an electrical room is an immediate emergency. Do not enter further. Alert facility manager and on-call engineer immediately.

---

### SECTION 4: UPS ROOM 3 — UPS-3A, UPS-3B, UPS-3C, MDP-UPS-I/P-3, WAB 3 PANEL
*(Annex Building A-2F, UPS Room 3. Buddy rule applies — do not enter alone.)*

---

□ **Step 1: Visually inspect UPS-3A, UPS-3B, and UPS-3C. Check that all three units are powered on, in normal inverter mode, and not in STS mode, bypass mode, or battery mode.**
   Normal reading or condition: All three UPS units — UPS-3A, UPS-3B, UPS-3C — are in normal inverter-on operating mode. LCD displays show no active alarms. No warning or fault LEDs are active.
   If abnormal: A UPS in STS mode indicates the inverter is off but input is live — the unit is running on static transfer switch without battery protection of the normal kind. A UPS in battery mode indicates loss of input power. Either condition is an immediate escalation. Do not reset or press any controls on the UPS without authorization from the on-call engineer.

□ **Step 2: Record UPS input voltage, output voltage, load percentage, and battery state of charge from each unit's LCD display — UPS-3A, UPS-3B, UPS-3C.**
   Normal reading or condition: Input and output voltages within normal operating tolerance for the UPS model installed. [VERIFY NORMAL UPS VOLTAGE RANGES WITH ENGINEER] Load percentage is within expected range. Battery state of charge is at or near 100%.
   If abnormal: Battery below [VERIFY MINIMUM ACCEPTABLE SOC WITH ENGINEER], unusual voltage deviation, or load above [VERIFY LOAD THRESHOLD WITH ENGINEER] must be escalated. Log the specific unit and all displayed readings.

□ **Step 3: Listen at each UPS unit for unusual sounds — excessive fan noise, buzzing, clicking, or arcing.**
   Normal reading or condition: Steady fan noise appropriate to the load level. No irregular sounds.
   If abnormal: Unusual sounds from a UPS unit — particularly buzzing or arcing — are precursors to component failure. Do not open the unit. Escalate immediately.

□ **Step 4: Visually inspect MDP-UPS-I/P-3 (Input Main Distribution Panel). Confirm panel is closed, dead front is in place, no damage, no burn marks, no unusual odors.**
   Normal reading or condition: Panel is fully closed and secured. No visible damage or abnormal conditions.
   If abnormal: See Section 3, Step 1 — same escalation applies. Any open or damaged panel in an energized state is an immediate safety escalation.

□ **Step 5: Visually inspect WAB 3 Panel. Confirm panel is closed, dead front is in place, no damage, no burn marks, no unusual odors.**
   Normal reading or condition: Panel is fully closed and secured. No visible damage or abnormal conditions.
   If abnormal: Log and escalate. Do not open. Do not touch.

□ **Step 6: Check room temperature and humidity in UPS Room 3 — read from wall-mounted sensor or BMS display if available.**
   Normal reading or condition: Room temperature and humidity within equipment operating specifications. [VERIFY UPS ROOM TEMPERATURE AND HUMIDITY LIMITS WITH ENGINEER]
   If abnormal: Elevated room temperature in a UPS room directly shortens battery lifespan and increases risk of thermal shutdown. Escalate to on-call engineer and check cooling units serving this room.

□ **Step 7: Verify UPS Room 3 ventilation and cooling units are operating.**
   Normal reading or condition: Cooling or ventilation units serving UPS Room 3 are running and functioning normally. No fault indicators.
   If abnormal: Report to on-call engineer. Elevated UPS room temperature is time-sensitive.

---

### SECTION 5: BATTERY ROOM 3 — BATTERY BANKS, SYSTEM 3
*(Annex Building A-2F, Battery Room 3. Buddy rule applies. No open flames. Confirm ventilation before entering.)*

---

□ **Step 1: Before entering Battery Room 3 — verify room ventilation is operational.**
   Normal reading or condition: Ventilation system for Battery Room 3 is running. No unusual smells — particularly sulfur or rotten egg odor — present at the doorway before entry.
   If abnormal: A sulfur odor at the battery room entrance indicates battery off-gassing, which is a hydrogen explosion and acid exposure hazard. Do not enter. Evacuate the area. Call on-call engineer and facility manager immediately.

□ **Step 2: Visually inspect battery banks — check all visible battery units for swelling, leakage, corrosion at terminals, or physical damage.**
   Normal reading or condition: All battery units are uniform in appearance. No swelling or distortion. No visible electrolyte leakage or puddles. Terminal connections show no white or green corrosion buildup. No cracked battery cases.
   If abnormal: Any battery showing swelling, leakage, or cracking is a safety and fire risk. Do not touch. Log the specific battery bank and unit location. Escalate immediately to on-call engineer.

□ **Step 3: Verify all battery bank breakers are in their expected ON position and none are tripped.**
   Normal reading or condition: All battery bank breakers are in the ON position consistent with normal UPS operation. No tripped breakers.
   If abnormal: A tripped battery bank breaker reduces or eliminates battery backup capacity. Log the specific breaker. Do not reset without authorization from the on-call engineer.

□ **Step 4: Check Battery Room 3 ambient temperature using wall sensor or handheld thermometer.**
   Normal reading or condition: Battery room temperature within the operating range specified for the installed battery chemistry. [VERIFY BATTERY ROOM TEMPERATURE LIMITS WITH ENGINEER — typical sealed lead-acid optimal is 20°C–25°C / 68°F–77°F, but confirm for installed battery type]
   If abnormal: Elevated battery room temperature accelerates battery aging and increases failure risk. Escalate to on-call engineer.

□ **Step 5: Record exit time and confirm room is secure — door locked — upon leaving Battery Room 3.**
   Normal reading or condition: Room secured. Exit time logged.
   If abnormal: Any signs of unauthorized access, damaged door hardware, or security bypass must be reported to facility security and the shift supervisor.

---

### SECTION 6: LVMSB ROOM 3 AND LVMSB ROOM 2 — LVMSB-3, LVMSB-2, TIE-BREAKER
*(Annex Building A-2F. High-voltage switchgear rooms. Visual inspection only. Do not open panels.)*

---

□ **Step 1: Visually inspect LVMSB-3 from outside the equipment barrier. Confirm cabinet doors are closed, no damage visible, no burn marks, no unusual odors.**
   Normal reading or condition: LVMSB-3 is fully closed and secured. No visible damage, burn marks, discoloration, or heat distortion on the enclosure. No unusual smell.
   If abnormal: Any open door, visible damage, burn marks, or unusual smell at the LVMSB is an immediate escalation. Do not enter the equipment zone. Alert on-call engineer and facility manager immediately.

□ **Step 2: Verify LVMSB-3 status indicators — if a status panel or mimic display is accessible — confirm normal operational state.**
   Normal reading or condition: All indicators show normal. No fault or trip indicators active. [VERIFY EXPECTED INDICATOR STATES WITH ENGINEER AND DOCUMENT AS BASELINE]
   If abnormal: Any unexpected fault or trip indicator at LVMSB level has potential to affect the entire electrical distribution system downstream. Escalate immediately.

□ **Step 3: Visually inspect LVMSB-2 and TIE-BREAKER panel in LVMSB Room 2. Confirm TIE-BREAKER is in its expected position for normal operations.**
   Normal reading or condition: TIE-BREAKER is in its normal operating position as defined by the facility's standard electrical configuration. [VERIFY TIE-BREAKER NORMAL POSITION — OPEN OR CLOSED — WITH ENGINEER AND DOCUMENT AS BASELINE]
   If abnormal: The TIE-BREAKER position directly affects whether LVMSB-3 is isolated from or connected to LVMSB-2. Any unexpected change from the documented normal position must be escalated immediately to the on-call engineer. This is a critical operational status point.

□ **Step 4: Check ambient temperature in LVMSB Rooms 3 and 2.**
   Normal reading or condition: Room temperature within acceptable limits for high-voltage switchgear operation. [VERIFY TEMPERATURE LIMITS WITH ENGINEER]
   If abnormal: Elevated temperature in a switchgear room increases risk of insulation failure and arc flash events. Escalate to on-call engineer.

□ **Step 5: Confirm both LVMSB rooms are secure — doors locked — and no unauthorized equipment or personnel are present.**
   Normal reading or condition: Both rooms are secure, properly locked, and contain only installed facility equipment.
   If abnormal: Any sign of unauthorized access, unfamiliar equipment, or tampered locks must be reported to facility security and the shift supervisor immediately.

---

### SECTION 7: GENERATOR ROOM — GENSET 1 AND GENSET 5
*(Confirm hearing protection is worn before entering if either unit is running.)*

---

□ **Step 1: Visually inspect Genset 1. Check fuel level, coolant level indicators, oil level if visible, and any warning lights or fault indicators on the generator control panel.**
   Normal reading or condition: Genset 1 is in standby/auto mode — ready to start on demand. Fuel level is within the facility's minimum required standby reserve. No active fault or warning indicators. [VERIFY MINIMUM FUEL LEVEL THRESHOLD WITH ENGINEER]
   If abnormal: A Genset 1 fault indicator, low fuel condition, or unexpected mode other than auto-standby must be escalated to the on-call engineer. Genset 1 is the primary backup for the UPS System 3 infrastructure — its availability is critical.

□ **Step 2: Visually inspect Genset 5. Check control panel status — confirm Genset 5 is in standby/auto mode and shows no fault indicators.**
   Normal reading or condition: Genset 5 is in standby/auto mode via the MISS system. No fault indicators. Fuel level adequate. [VERIFY FUEL LEVEL MINIMUM WITH ENGINEER]
   If abnormal: Genset 5 is the fallback if Genset 1 fails. A fault on Genset 5 when Genset 1 is also not fully operational is a dual-failure condition. Escalate immediately.

□ **Step 3: Check the generator room for fluid leaks — fuel, coolant, or oil — on the floor around either unit.**
   Normal reading or condition: Floor is dry. No fluid pooling or staining under or around either generator.
   If abnormal: Any fuel leak is a fire hazard. Any coolant or oil leak indicates a developing mechanical fault. Do not attempt to clean or contain fuel spills without proper hazmat training. Alert facility manager immediately.

□ **Step 4: Verify generator room exhaust venting and ventilation appear unobstructed.**
   Normal reading or condition: Exhaust pathways and ventilation louvers are clear. No obstruction visible.
   If abnormal: Blocked generator exhaust creates carbon monoxide hazard and overheating risk. Do not start generators if exhaust is blocked. Report immediately.

□ **Step 5: Record Genset 1 and Genset 5 hour meter readings if meters are present.**
   Normal reading or condition: Hour meter readings are recorded and show expected accumulation since last shift log entry.
   If abnormal: An unexpected large jump in hours since the last shift suggests a generator started and ran — possibly on an automated test or during an undocumented event. Investigate and report.

---

### SECTION 8: COOLING SYSTEM — VISUAL AND READING CHECKS
*(Walk all CRAC/CRAH/AHU units serving Data Center 1. Check from front and rear of each unit.)*

---

□ **Step 1: Inspect each CRAC/CRAH unit on the data center floor — verify unit is running, status indicator is green or normal, and no fault lights or alarms are active.**
   Normal reading or condition: All cooling units are in normal operating mode. No fault or alarm indicators. Supply and return fans are audibly running at normal speed.
   If abnormal: A cooling unit in fault or shutdown will reduce overall cooling capacity. Log the unit ID and fault code displayed. Escalate to on-call engineer. Do not reset faults without authorization.

□ **Step 2: Record supply air temperature and return air temperature from each cooling unit display — if displayed.**
   Normal reading or condition: Supply and return temperatures are within facility setpoints. [VERIFY SUPPLY AND RETURN AIR TEMPERATURE SETPOINTS WITH ENGINEER FOR EACH UNIT]
   If abnormal: Supply temperature above setpoint means the unit is not cooling adequately. Return temperature significantly above design delta means the room is not removing heat effectively. Both require escalation.

□ **Step 3: Check for any condensate drainage issues — pooling water, clogged drain pans, or water on the floor near cooling units.**
   Normal reading or condition: No standing water near cooling units. Drain pans are clear. No visible moisture on unit exteriors or surrounding floor areas.
   If abnormal: Condensate pooling near cooling units in a raised floor environment can saturate underfloor space and reach electrical connections. Report any water pooling immediately.

□ **Step 4: Verify chilled water supply and return lines — if visible — show no leaks, unusual condensation, or pipe damage.**
   Normal reading or condition: Piping is dry, insulated, and undamaged. No drips or water stains below pipe connections or valves.
   If abnormal: Any leak at a chilled water connection or valve must be reported immediately. Identify the location, isolate the area if possible, and escalate.

□ **Step 5: Record chilled water supply and return pressure readings — if gauges are present and accessible.**
   Normal reading or condition: [VERIFY CHILLED WATER PRESSURE SETPOINTS WITH ENGINEER — record approved ranges on facility parameter sheet]
   If abnormal: Pressure outside normal range indicates a pump fault, valve position issue, or leak in the chilled water circuit. Escalate to on-call engineer.

---

## DOCUMENTATION REQUIREMENTS:

Every step completed during this walkthrough must be documented. Incomplete documentation is not acceptable — a blank checkbox is indistinguishable from a skipped check.

**Shift Log Entry — Required at Completion of Every Walkthrough:**
- Technician name and employee ID
- Shift date and walkthrough start time and end time
- Facility system status summary: Power / Cooling / BMS / Compute Racks — Normal or Abnormal
- All abnormal conditions found: description, location, time observed, action taken, and who was notified
- Any alarms active at the start of shift and their status at the end of the walkthrough
- BMS alarm count at start of walkthrough and at completion
- PDU load readings for PDUs 13, 14, 16, 17, 13A, 14A, 16A
- UPS status for UPS-3A, UPS-3B, UPS-3C — mode and battery SOC
- MDP-UPS-O/P-3 output voltage reading
- Genset 1 and