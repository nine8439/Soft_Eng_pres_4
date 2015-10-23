<h2>Patriot Missile System Background</h2>
1. The MIM-104 Patriot is a surface-to-air missile (SAM) system, the primary of its kind used by the United States Army and several allied nations. It is manufactured by the U.S. defense contractor Raytheon and derives its name from the radar component of the weapon system.

2. The AN/MPQ-53 at the heart of the system is known as the "Phased array Tracking Radar to Intercept on Target" or the bacronym PATRIOT.

3. Patriot uses an advanced aerial interceptor missile and high-performance radar systems.

4. It's initial purpose was as an anti-aircraft system, but it quickly became used as  anti-tactile ballistic missiles. 

5. The Patriot Missile system consists of an advanced radar system and an anti-ballistic missile.

6. The Patriot system has four major operational functions: communications, command and control, radar surveillance, and missile guidance. The four functions combine to provide a coordinated, secure, integrated, mobile air defense system.

<h2>Patriot Missile System Technology</h2>

1. The AN/MPQ-53/65 Radar Set is a passive electronically scanned array radar equipped with IFF, electronic counter-countermeasure (ECCM), and track-via-missile (TVM) guidance subsystems. The beam created by the Patriot's flat phased array radar is comparatively narrow and highly agile compared to a moving dish. This characteristic gives the radar the ability to detect small, fast targets like ballistic missiles, or low radar cross section targets such as stealth aircraft or cruise missiles.

2. AN/MSQ-104 engagement control station consists of: 
    1. Weapons control computer (WCC) - The computer of the patriot missile systems 
    2. Data Link Terminal – The interface to the missile launchers  
    3. UHF communications array – Creates the medium for network communications between the patriot missile systems 
    4. LRIU (Routing Logic Radio Interface Unit) – Router for all the data traffic of the patriot system 
    5. Two computer manstations  - stations where humans (operators) interface with the system

Also Important: It is contained in a mobile shelter capable of withstanding  Electromagnetic Interference, chemical/biological attacks, and also acts as protection against the elements.

3. OE-349 Antenna Mast Group, consists of mobile platform, and 4 antennas in two pairs with it's associated amplifiers and radios
Important: This creates the communications network for the system

4. M901 Launching Station: station where the missile is launched, self-contained.

<h2>Patriot Missile Technology</h2>

1. MIM-104A – solely for anti-aircraft purpose

2. MIM104C/D/E (PAC-2) - for anti-missile; intended to explode on engagement; consists of four sections
    1. Propulsion section
    2. Warhead section
    3. Guidance section – Consists of the auto-guidance systems and also the Track via guidance System (from ground control)
    4. Control actuator section – controls the fins of the missile for stability and steering

<h2>Use and Disaster in the Gulf War</h2>

+ The Persian Gulf War was the first usage of the Patriot missile system to shoot down ballistic missiles as opposed to only aircraft.

+ It was used 40 times to shoot down missiles, primarily Scud or Al Hussein short range ballistic missiles.

+ The initial launch was actually a computer glitch

+ The worst failure was when an army barracks in Dhahran, Saudi Arabia was hit by a Scud missile and 28 people died.

+ On the night of the 25th of February, 1991, a Patriot missile system operating in Dhahran, Saudi Arabia, failed to track and intercept an incoming Scud. The Iraqi missile impacted into an army barracks, killing 28 U.S. soldiers and injuring another 98.

+ The cause of the missile system failing to defend against the incoming Scud was traced back to a bug in Patriot's radar and tracking software

<h2>Overview of Disaster</h2>

+ Problem Statement: “System failed to identify a  enemy missile after the system had been running continuously for over 100 hours”

+ If we assume the Patriot Missile Systems was correctly working on the European War front prior to the Persian Gulf War, then these problems can be considered as requirements creep.

+ 4 areas where problems were encountered:
    1. Domain/Environment Change
    2. Software: clock drift/round-off error, reboot time, software delivery time, software upgrade time
    3. Hardware: No recorder, difference in ballistic missiles versus Aircraft/Cruise Missiles
    4. User Ware: no auditory alarms, information on Operation doctorine

<h2>Domain/Environment Change</h2>

+ Environmental Change: Changes were accounted for during the conflict. 

> “As information from all sources became available, software changes were made from August 1990 to February 199 1 by the Patriot Project Office in Huntsville, Alabama, to adapt the system to the Desert Storm environment.”

http://fas.org/spp/starwars/gao/im92026.htm

+ The Patriot system was originally designed to operate in Europe against Soviet medium- to high-altitude aircraft and cruise missiles traveling at speeds up to about MACH 2 (1500 mph). To avoid detection it was designed to be mobile and operate for only a few hours at one location.

+ This was the first time the Patriot had been used to defend against Scud missiles, which fly at approximately MACH 5 (3750 mph), the Army had much to learn about tracking and intercepting them. To obtain Scud data, the Army relied on operational experience conveyed by Patriot users as well as other intelligence sources.

+ The major change needed was the reduction of the dependence of the system to its mobile characteristic. The Patriot system was originally designed to operate in Europe against Soviet medium- to high-altitude aircraft and cruise missiles…To avoid detection it was designed to be mobile and operate for only a few hours at one location. This is a significant requirements creep. 

<h2>Software</h2>

+ The algorithm used to calculate the path of the Scud Missile was called the Range-Gate Algorithm.

+ However since it was only 24bit machine, there was a loss in precision as the time increased or the velocity has significantly higher.

+ The System had been on for over 100 hours and therefore the Range-Gate algorithm was significantly off and no missile was detected in the Dhahran attack.

> "The range gate's prediction of where the Scud will next appear is a function of the Scud's know velocity and the time of the last radar detection. Velocity is a real number that can be expressed as a whole number and a decimal (e.g., 3750.2563...miles per hour). Time is kept continuously by the system's internal clock in tenths of seconds but is expressed as an integer or whole number (e.g., 32, 33, 34...). The longer the system has been running, the larger the number representing time. To predict where the Scud will next appear, both time and velocity must be expressed as real numbers. Because of the way the Patriot computer performs its calculations and the fact that its registers(4) are only 24 bits long, the conversion of time from an integer to a real number cannot be any more precise than 24"

http://fas.org/spp/starwars/gao/im92026.htm

+ Reboot time to reset the clock wasn't a risk many military weren't willing to take. At the beginning of the War, only about a two minute window to actually detect and track the missile.  A reboot took 1.5 to 2 minutes, therefore a chance to miss an incoming missile.

+ To upgrade the software, it would require the system to be down for 1-2 hours, as mentioned above, commanders at the front line found this to be a difficult risk to take. 
















