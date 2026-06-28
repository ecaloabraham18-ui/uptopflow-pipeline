# Method of Procedure

## Annual Electrical Preventive Maintenance (Data Center 1)

**Title:**
**Activity:** TBD
**Date:**

### Activity Duration:
| No. | Activity                                                                 | Estimated Duration | Actual Duration |
|-----|--------------------------------------------------------------------------|--------------------|-----------------|
| 1   | Checking and sending of Advisory to affected clients                     |                    |                 |
| 2   | Sending of advisory to TIM Teams and client                              |                    |                 |
| 3   | PDU 13 shutdown &#x26; maintenance                                             |                    |                 |
| 4   | PDU 14 shutdown &#x26; maintenance                                             |                    |                 |
| 5   | PDU 16 shutdown &#x26; maintenance                                             |                    |                 |
| 6   | PDU 17 shutdown &#x26; maintenance                                             |                    |                 |
| 7   | PDU 13A, 14A &#x26; 16A shutdown &#x26; maintenance                                 |                    |                 |
| 8   | LVMSB -3, WAB 3, UPS-O/P-3 and MDP-UPS-1/P-3 shutdown                  |                    |                 |
| 9   | Maintenance for;                                                         |                    |                 |
|     | MDP-UPS-1/P-3                                                           |                    |                 |
| 10  | UPS-O/P-3 Panel                                                          |                    |                 |
| 11  | WAB 3 Panel                                                              |                    |                 |
| 12  | LVMSB -3                                                                 |                    |                 |
| 13  | LVMSB -3, WAB 3, UPS-O/P-3, and MDP-UPS-1/P-3 start up                 |                    |                 |
| 14  | MDP Panel-system 3 and PDU 13, PDU 14, PDU 16, PDU 17, PDU 13A, PDU 14A &#x26; PDU 16A start up |                    |                 |

### Post-Activity
1. Visual checking
2. Inform management
3. Inform client


---PAGE BREAK---


```plaintext
4  Thermal scanning

Impact      Client dual source equipment will be single power within the timeframe of activity.
on the      Only Single source equipment will be affected.
users:
Purpose
of MOP:     To conduct Preventive Maintenance and rectify electrical components of the Data Center
Electrical System

Note:
DCO Teams:

1.     Team 1 (Control Team): TBD
2.     Team 2 (Switching Team): TBD
3.     Team 3 (Verification Team): TBD
4.     Team 4 (Rack Assessment Team 1): TBD
5.     Team 5 (Rack Assessment Team 2): TBD
6.     Team 6 (Vendor Assistance Team): TBD
7.     Team 7 (Operations Team): TBD

CSG Teams:

1.     TBD

Vendors:
Note: The personnel list for vendors is subject to change based on their availability

1.     Exquis: TBD

METHODS OF PROCEDURE

Duration
Time                  Activity                     Location  Responsible  Esti  Actu  Remarks
mate  al

Pre-Activity steps
Request Data Center clients to access
their rack to verify the equipment list                CSG &#x26; DCO
as an attachment for the EPM
advisory.
Check, verify, and update the client’s                                        Note: Once
rack equipment list including the                      DCO                    the activity is
following:                                                                    done, all
clients that
```


---PAGE BREAK---


```plaintext
Pre-requi      ∙     Equipment quantity             has single
sites                                               power
Activities:                                         equipment
must be sent
an STS
proposal by
∙     Equipment power source         AM)
configuration (Dual or Single source)

∙    Equipment brand and model
Create EPM advisory and equipment         CSG &#x26; DCO
list attachment per client.
Approval of EPM advisory template         Management
Email EPM advisory for all Data                        (Note: All
Center Clients 3 months before the        CSG          clients
said EPM schedule                                      requests
AMs will verify the client’s              TIM AM's     must be
confirmation for the activity                          requested 3
Email EPM follow-up advisory for all                   days prior to
Data Center Clients 2 months before       CSG          the EPM
the said EPM schedule                                  activity. Any
Email EPM follow-up advisory for all                   request in
Data Center Clients 1 month before        CSG          the day of
the said EPM schedule                                  the EPM
Follow-up confirmation from Clients if                 activity will
the equipment list is still valid and                  not be
updated 1 month before the EPM            CSG          entertained)
activity
Confirm any EPM client request for all
Data Center Clients 1 week before         DCO
the said EPM schedule
DCO will conduct an electrical load
analysis 1 (2-4) week before the          DCO
activity.
EPM vendor will conduct pre-thermal
checking (2-4) weeks before the
activity.
DCO will list down all rectification      DCO
items (2-4) weeks before the activity.
DCO will conduct a vendor meeting 1
week (1 month and 1 week) before          DCO
the EPM activity for preparations.
DCO will tag rooms and equipment
that will be (Yellow tag) and will not    DCO
be maintained (Red tag – Orange
tag) 3 days prior to the activity
DCO will conduct a toolbox meeting 1      DCO
hour before the activity.
DCO will assign teams for the EPM         DCO
activity
```


---PAGE BREAK---


```markdown
# Advisory to the TIM Team before DCO &#x26; CSG proceeding

## Affected Services:
Client dual source equipment will be single power within the timeframe of activity.

- Include list of clients

## Activities and Methods of Procedure

| Time       | Activity                                                                 | Location         | Responsible   | Estimated Duration | Actual Duration | Remarks |
|------------|--------------------------------------------------------------------------|------------------|---------------|--------------------|-----------------|---------|
|            | Start of Annual Electrical Preventive Maintenance                        | Main Bldg.       | Command center | DCO &#x26; CSG         |                    |         |
|            | Advisory to the TIM Team and Client that the activity is about to start. |                  |                |                    |                    |         |
|            | Start of PDU 13 shutdown                                                | Main Bldg.       |                |                    |                    |         |
|            | DCO Team 1 will command DCO Team 2 that they can proceed to shutdown PDU 13 | Main Bldg. - DC 1 | DCO Team 1    |                    |                    | PDU 13 &#x26; PDU 12 - 30 branch circuits |
|            | DCO Team 2 will turn off the PDU 13 – 30 branch circuits (one by one per client’s rack). | Main Bldg. - DC 1 | DCO Team 2    |                    |                    |         |
|            | DCO Team 3 will monitor and verify if the load was successfully transferred to PDU 12 – 30 branch circuits. | Main Bldg. - DC 1 | DCO Team 3    |                    |                    |         |
|            | DCO Team 4 and 5 will check the racks simultaneously when DCO Team 2 turns off the PDU 13 branch circuits. This is to verify that no equipment has been turned off. If there is equipment in off status, it will be reported to CSG, and will verify with the client if their business operations are affected. | Main Bldg. - DC 1 | DCO Team 4 &#x26; 5 |                    |                    |         |
|            | After PDU 13 branch circuits are turned off, Team 2 will turn off the PDU main breaker, and will be relayed to DCO Team 1 | Main Bldg. - DC 1 | DCO Team 2    |                    |                    |         |
|            | Team 1 will turn off the breaker for PDU 13 located in MDP-UPS-O/P-3 (EE Room 3) | Main Bldg. - EE RM 3 | DCO Team 1    |                    |                    |         |
|            | Team 1 will relay to Team 6 that the breaker is now in OFF status.     |                  |                |                    |                    |         |
|            | Upon confirmation of Team 1 to Team 6, Team 6 will proceed to assist the vendor with the maintenance of PDU 13 inside the data center. | Main Bldg. - DC 1 | DCO Team 6 &#x26; Exquis |                    |                    |         |
```


---PAGE BREAK---


```
| Task Description                                      | Location         | Team         | Duration |
|-------------------------------------------------------|------------------|--------------|----------|
| Replacement of dead front of PDU 13 Panel.           | Main Bldg. - DC 1| DCO Team 6   | 30 mins  |
| Maintenance of the panel’s electrical components (PDU 13). |                  |              |          |
| Start of PDU 14 Shutdown                              | Main Bldg. - DC 1| DCO Team 6   | 15 mins  |
|                                                       |                  |              |          |
|                                                       | Main Bldg. - DC 1| DCO Team 1   |          |
| DCO Team 2 will turn off the PDU 14 – 60 branch circuits (one by one per client’s rack). | Main Bldg. - DC 1| DCO TEAM 2   |          |
| DCO Team 3 will monitor and verify if the load was successfully transferred to PDU 11 – 60 branch circuits. | Main Bldg. - DC 1| DCO Team 3   |          |
| DCO Team 4 and 5 will check the racks simultaneously when DCO Team 2 turns off the PDU 14 branch circuits. This is to verify that no equipment has been turned off. If there is equipment in off status, it will be reported to CSG, and will verify with the client if their business operations are affected. | Main Bldg. - DC 1| DCO Team 4 &#x26; 5 |          |
| After PDU 14 branch circuits are turned off, Team 2 will turn off the PDU main breaker, and will be relayed to DCO Team 1. | Main Bldg. - DC 1| DCO Team 2   |          |
| Team 1 will turn off the breaker for PDU 14 located in MDP-UPS-O/P-3 (EE Room 3) and will relayed to Team 6 that the breaker is now in OFF status. | Main Bldg. - EE RM 3| DCO Team 1   |          |
| Upon confirmation of Team 1 to Team 6. Team 6 will proceed to assist the vendor with the maintenance of PDU 14 inside the data center. | Main Bldg. - DC 1| DCO Team 6   |          |
| Maintenance of the panel’s electrical components (PDU 14). |                  |              |          |
| Start of PDU 16 Shutdown                              | Main Bldg. - DC 1| DCO Team 6   | 15 mins  |
|                                                       |                  |              |          |
|                                                       | Main Bldg. - DC 1| DCO Team 1   |          |
| DCO Team 2 will turn off the PDU 16 – 30 branch circuits (one by one per client’s rack). | Main Bldg. - DC 1| DCO Team 2   |          |
| DCO Team 3 will monitor and verify if the load was successfully transferred to PDU 3 – 30 branch circuits. | Main Bldg. - DC 1| DCO Team 3   |          |
```


---PAGE BREAK---


```plaintext
DCO Team 4 and 5 will check the racks simultaneously when DCO Team 2 turns off the PDU 16 branch circuits. This is to verify that no equipment has been turned off. If there is equipment in off status, it will be reported to CSG, and will verify with the client if their business operations are affected.

After PDU 16 branch circuits are turned off, Team 2 will turn off the PDU main breaker, and will be relayed to DCO Team 1.

Team 1 will turn off the breaker of PDU 16 located in MDP-UPS-O/P-3 (EE Room 3) and will relayed to Team 6 that the breaker is now in OFF status.

Upon confirmation of Team 1 to Team 6, Team 6 will proceed to assist the vendor for the rectification and maintenance of PDU 16 inside the data center.

Replacement of dead front of PDU 16 Panel.
Main Bldg. - DCO Team 6 30 mins.
DC 1 &#x26; Blackstone

Maintenance of the panel’s electrical components (PDU 16)
Start of PDU 17 shutdown
DCO Team 1 will command other DCO Teams that they can proceed to PDU 17.
Main Bldg. - DCO Team 6 15 mins.
DC 1 &#x26; Exquis

Main Bldg. - DCO Team 1
DC 1

DCO Team 2 will turn off the PDU 17 – 60 branch circuits (one by one per client’s rack).

DCO Team 3 will monitor and verify if the load was successfully transferred to PDU 2 – 60 branch circuits.

DCO Team 4 and 5 will check the racks simultaneously when DCO Team 2 turns off the PDU 17 branch circuits. This is to verify that no equipment has been turned off. If there is equipment in off status, it will be reported to CSG, and will verify with the client if their business operations are affected.

After PDU 17 branch circuits are turned off, Team 2 will turn off the PDU main breaker, and will be relayed to DCO Team 1.
```


---PAGE BREAK---


```
| Action Description                                                                 | Location                | Team         | Duration   |
|------------------------------------------------------------------------------------|------------------------|--------------|------------|
| Team 1 will turn off the breaker of PDU 17 located in MDP-UPS-O/P-3 (EE Room 3) | Main Bldg.             | DCO Team 1  |            |
| and will relay to Team 6 that the breaker is now in OFF status.                   | EE RM 3                |              |            |
| Upon confirmation of Team 1 to Team 6.                                            |                        |              |            |
| Team 6 will proceed to assist the vendor with the rectification and maintenance of | Main Bldg.             | DCO Team 6  |            |
| PDU 17 inside the data center.                                                    | DC 1                   | &#x26; Exquis     |            |
| Maintenance of the panel’s electrical components (PDU 17)                         | Main Bldg.             | DCO Team 6  | 15 mins.   |
| Start of PDU 13A, 14A, &#x26; 16A Shutdown                                             |                        |              |            |
| DCO Team 1 will command other DCO Teams that they can proceed to shutdown         | Main Bldg.             | DCO Team 1  |            |
| PDU 13A, 14A &#x26; 16A                                                                | EE RM. 3               |              |            |
| DCO Team 2 will turn off the PDU 13A, 14A &#x26; 16A.                                 | Main Bldg.             | DCO Team 2  |            |
| DCO Team 3 will monitor and verify if the load was successfully transferred to its | Main Bldg.             | DCO Team 3  |            |
| redundant power supply.                                                            | EE RM. 2               |              |            |
|                                                                                    | and EE RM. 1           |              |            |
| DCO Team 4 and 5 will check the racks simultaneously when DCO Team 2 turns off   | Main Bldg.             | DCO Team 4  |            |
| PDU 13A, 14A &#x26; 16A branch circuits. This is to verify that no equipment has been  | EE RM. 3 &#x26; 5          |              |            |
| turned off. If there is equipment in off status, it will be reported to CSG, and  |                        |              |            |
| we will verify with the client if their business operations are affected.         |                        |              |            |
| After PDU 13A, 14A &#x26; 16A branch circuits are turned off. Team 2 will turn off the | Main Bldg.             | DCO Team 2  |            |
| PDU main breaker and will be relayed to DCO Team 1.                              | EE RM. 3               |              |            |
| Team 1 will turn off the breaker of PDU 13A, 14A, and 16A located in             | Main Bldg.             | DCO Team 1  |            |
| MDP-UPS-O/P-3 (EE Room 3) and will relay to Team 6 that the breaker is now in    | EE RM. 3               |              |            |
| OFF status.                                                                        |                        |              |            |
| Upon confirmation of Team 1 to Team 6.                                            |                        |              |            |
| Team 6 will proceed to assist the vendor with their rectification and maintenance  | Main Bldg.             | DCO Team 6  |            |
| on PDU 13A, 14A &#x26; 16A inside the data center and Telco Areas.                     | EE RM. 3 &#x26; Vendors     |              |            |
| After all the PDUs on the said system are turned off. DCO Team 1 and 2 will turn | Annex Bldg.            | DCO Team 1  |            |
| off the system up to the WAB 3 Panel.                                             | A- 2F                  | &#x26; 2          | UPS Room 3 |
```


---PAGE BREAK---


```plaintext
Upon confirmation of Team 1 to Team 6.
Team 6 will proceed to assist the vendor          Main Bldg. –    DCO Team 6
with their rectification and maintenance            EE RM. 3       &#x26; Exquis
on PDU 13A, 14A &#x26; 16A inside the data
center.

Maintenance of the panel’s electrical             Main Bldg. –    DCO Team 6  45
components (PDU 13A, 14A &#x26; 16A)                     EE RM. 3       &#x26; Exquis  mins.

UPS Shutdown procedure

Turn off MDP-UPS-O/P-3 (EE Room 3) Main           Main Bldg. –
Breaker.                                            EE RM. 3

Press inverter off of UPS-3A, UPS-3B, and         Annex Bldg.
UPS-3C one by one (3 units per system)               A- 2F
then UPS will be in STS mode.                      UPS Room 3
Turn off the MDP-UPS-I/P-3 (UPS Room 3)
panel main input breaker to shut down the         Annex Bldg.
main supply of UPSs. The LCD panel is still          A- 2F
active, with an alarm, and is in battery           UPS Room 3    DCO Team 1
mode.

Turn off DC 1 WAB 3 (UPS Room 3) branch           Annex Bldg.
circuits and its main breaker.                       A- 2F
UPS Room 3

To shut down the UPS, go to battery room          Annex Bldg.
3 and turn off the breakers of the battery           A- 2F
banks one by one. Once turned off, UPS is         Battery
totally shut down.                                   Room 3

DCO Team 2 will isolate LVMSB-3 from              Annex Bldg.
LVMSB-2 by switching OFF the bypass                  A- 2F        DCO Team 2
breaker (TIE-BREAKER) in the LVMSB-2              LVMSB
panel.                                             Room 2 &#x26; 3
DCO Team 2 will advise the other DCO              Main Bldg. –     DCO Team
teams that they can proceed with the EPM            EE RM. 3        2, DCO
of MDP-UPS-O/P-3 (2F EE Room 3),                  and Annex        Team 6 &#x26;
MDP-UPS-I/P-3 (UPS Room 3), DC 1 WAB 3            Bldg. A- 2F      Vendors
(UPS Room 3) and LVMSB-3 (LV Room 3)               UPS Room 3
Electrical PM for MDP Panel, UPS Panels, and LVMSB
Checking of voltage at the
UPS Panel line side before proceeding to
the maintenance activity of the vendor.           Annex Bldg.      DCO Team
Ensure that MDP-UPS-O/P-3 (2F EE Room                A- 2F        3&#x26; Vendor
3), MDP-UPS-I/P-3 (UPS Room 3), DC 1               UPS Room 3
WAB 3 (UPS Room 3), LVMSB -3 and its
branches are de-energized.
Annex Bldg.
Maintenance of the panel’s electrical                A- 2F        DCO Team 6  80
components (LVMSB 3)                              LVMSB            &#x26; Exquis  mins.
Room 3
```


---PAGE BREAK---


| Activity Description                                   | Location         | Team         | Duration | Notes                                      |
|-------------------------------------------------------|------------------|--------------|----------|--------------------------------------------|
| Replacement of dead front of MDP UPS-O/P-3 Panel      | Main Bldg. EE RM. 3 | DCO Team 6  | 30 mins  | Be done in parallel with LVMSB-3 maintenance. |
| Replacement of dead front of WAB-3 Panel              | Annex Bldg. A-2F UPS Room 3 | DCO Team 6  | 30 mins  | Be done in parallel with LVMSB-3 maintenance. |
| Maintenance of MDP-UPS-O/P-3 Panel                    | Main Bldg. EE RM. 3 | DCO Team 6  | 35 mins  |                                            |
| Replacement of dead front of MDP UPS-I/P-3 Panel      | Annex Bldg. A-2F LVMSB Room 3 | DCO Team 6  | 30 mins  | Be done in parallel with MDP-UPS-O/P-3 maintenance. |
| Maintenance of WAB-3 Panel                             | Annex Bldg. LA-2F VMSB Room 3 | DCO Team 6  | 35 mins  |                                            |
| Replacement of dead front of LVMSB-3 Panel            | Annex Bldg. A-2F UPS Room 3 | DCO Team 6  | 30 mins  | Be done in parallel with WAB-3 maintenance. |
| Maintenance of MDP-UPS-I/P-3 Panel                     | Annex Bldg. A-2F LVMSB Room 3 | DCO Team 6  | 35 mins  |                                            |
| DCO Team 1 will inform the other DCO teams when the preventive maintenance activity for the MDP-UPS-O/P-3 Panel, MDP-UPS-I/P-3 Panel, WAB 3, and LVMSB-3 Panel is finished. | Annex Bldg. A-2F UPS Room 3 | DCO Team 3, Blackstone &#x26; Exquis |          |                                            |
| All TEAMS will verify that all maintenance and rectifications made by the vendor and DCO team are done. | Annex Bldg. A-2F UPS Room 3 | DCO Teams 3 to 6 |          |                                            |
| Before switching ON, make sure that the LVMSB-3 main breaker is in OFF status. | Annex Bldg. A-2F | DCO Teams  |          |                                            |
| DCO Team 2 will proceed with switching ON the bypass breaker to LVMSB-3 after confirming that all activities are done and is safe to do so. | Annex Bldg. LVMSB Room 2 &#x26; 3 | DCO Teams |          |                                            |
| UPS Start-up                                          |                  |              |          |                                            |



---PAGE BREAK---


```plaintext
DCO Team 1 will verify with DCO Team 3      Main Bldg. –
that there are no vendors present on MDP      EE RM. 3         DCO Team 1
UPS I/P-3 and its breaker is turned OFF.

Switching ON of MDP-UPS-I/P-3 Panel and       Annex Bldg.
the UPS will automatically turn ON in STS      A- 2F           DCO Team 1
mode.                                        UPS Room 3
Annex Bldg.
Turn ON the battery breakers at battery        A- 2F           DCO Team 1
room.                                           Battery
Room 3
Press inverter ON one by one for UPS-3A,      Annex Bldg.
UPS3B, &#x26; UPS-3C and the UPS will now           A- 2F           DCO Team 1
operate in normal mode. All alarms should    UPS Room 3
be cleared now.

DCO Team 1 will inform DCO Team 3 that         Annex Bldg.
the UPS System 3 is in normal mode             A- 2F           DCO Team 1
UPS Room 3
MDP Panel start up

DCO Team 3 will verify with DCO team 1 if      Annex Bldg.     DCO Team 1
the UPS System 3 is online                     A- 2F              &#x26; 3
UPS Room 3
Main breaker of MDP UPS O/P-3 will be
switched ON. Voltage reading will be taken     Annex Bldg.
on line and load side of the breaker.          A- 2F           DCO Team 3
Reading must be 400V(L-L). DCO Team 3        UPS Room 3
will inform DCO Team 1 that MDP is now
active.

DCO team 3 will now proceed to turning         Main Bldg. -
ON the main supply of PDU 13 located at        EE RM 3         DCO Team 3
MDP UPS O/P-3 at EE Room 3.

DCO Team 4 will be on standby at PDU          Main Bldg. -
location inside the data center. DCO team 3    EE RM 3 &#x26;       DCO Team 3
will relay to DCO team 4 that PDU 13 is        DC 1               &#x26; 4
ready to be switch ON.

Upon confirming with DCO team 3, DCO
team 4 will now turn ON the main input of     Main Bldg. -     DCO Team 4
PDU 13 and will gradually turn ON the          EE RM 3 &#x26;          &#x26; 5
branches (30 branches) by client rack          DC 1
group.
At the same time, DCO team 5 will verify
that the power has transferred from its       Main Bldg. -     DCO Team 5
redundant power supply (PDU 12) and            EE RM 3 &#x26;          &#x26; 6
DCO team 6 will verify that both PDU are       DC 1
now working.

DCO team 3 will now proceed to turning        Main Bldg. -
ON the main supply of PDU 14 located at        EE RM 3 &#x26;       DCO Team 3
MDP UPS O/P-3 at EE Room 3.                    DC 1

DCO Team 4 will be on standby at PDU          Main Bldg. -
location inside the data center. DCO team 3    EE RM 3 &#x26;       DCO Team 3
will relay to DCO team 4 that PDU 14 is        DC 1               &#x26; 4
ready to be switch ON.
```


---PAGE BREAK---


```plaintext
Upon confirming with DCO team 3, DCO team 4 will now turn ON the main input of Main Bldg. - PDU 14 and will gradually turn ON the branches (60 branches) by client rack group. At the same time, DCO team 5 will verify that the power has transferred from its redundant power supply (PDU 11) and DCO team 6 and 5 will verify that both PDU are now working.

DCO team 3 will now proceed to turning ON the main supply of PDU 16 located at MDP UPS O/P-3 at EE Room 3. DCO Team 4 will be on standby at PDU location inside the data center. DCO team 3 will relay to DCO team 4 that PDU 16 is ready to be switch ON.

Upon confirming with DCO team 3, DCO team 4 will now turn ON the main input of PDU 16 and will gradually turn ON the branches (30 branches) by client rack group. At the same time, DCO team 5 will verify that the power has transferred from its redundant power supply (PDU 3) and DCO team 6 and 5 will verify that both PDU are now working.

DCO team 3 will now proceed to turning ON the main supply of PDU 17 located at MDP UPS O/P-3 at EE Room 3. DCO Team 4 will be on standby at PDU location inside the data center. DCO team 3 will relay to DCO team 4 that PDU 17 is ready to be switch ON.

Upon confirming with DCO team 3, DCO team 4 will now turn ON the main input of PDU 17 and will gradually turn ON the branches (60 branches) by client rack group. At the same time, DCO team 5 will verify that the power has transferred from its redundant power supply (PDU 2) and DCO team 6 and 5 will verify that both PDU are now working.

DCO team 3 will now proceed to turning ON the main supply of PDU 13A, 14A, 16A located at MDP UPS I/O-1 at EE room 3. DCO Team 4 will be on standby at PDU location inside the data center and telco room. DCO team 3 will relay to DCO team 4 that PDU 13A, 14A, 16A is ready to be switch ON.
```


---PAGE BREAK---


```
Upon confirming with DCO team 3, DCO team 4 will now turn ON the affected circuit on PDU 13A, 14A, and 16A. At the same time, DCO team 5 will verify that the power has transferred from its redundant power supply and DCO team 6 will verify that both PDU are now working.

Post activity
Thoroughly visual Checking of the equipment inside the rack.
Inform the Management when the activity is done. Client Support Team will update clients that the Electrical Preventive is done.

Thermal Scanning                                                 DCO

Fall back steps

In case of power loss in the racks, turn ON the turned OFF breaker and reset its redundant PDU CKT if needed. In case of genset failure for Genset 1. Use genset 5 to supply the affected genset through MISS system.

Incident Management Trigger

Contact Data Center Operations (DCO)
Person Position: Manager
Contact Details:

Contact Details:
Data Center Operation (DCO)

Position: Team Lead
Email:
Mobile:

Customer Experience Group (CXG)

Position: CXG – Assistant Manager
```


---PAGE BREAK---


```
| Email:  |   |
| ------- | - |
| Mobile: |   |

# Electrical Services and Supplies Co.

| Position:        | Sr. Electrical Test Engineer |
| ---------------- | ---------------------------- |
| Contact Details: |                              |

| Prepared by: | Senior Data Center Engineer |
| ------------ | --------------------------- |
| Email:       |                             |

| Checked by: | Assistant Team Lead for Data Center Operations |
| ----------- | ---------------------------------------------- |
| Email:      |                                                |

| Evaluated by: | Team Lead |
| ------------- | --------- |
| Email:        |           |

| Approved by: | Data Center Operations – Manager |
| ------------ | -------------------------------- |
| Email:       |                                  |

```