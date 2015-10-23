<h1>Patriot Missile</h1>
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

<h2>Hardware</h2> 

+ The Patriot was not equipped with an embedded (internal) data recorder to retain system performance information. Although portable, external data recorders were available, U.S. commanders decided not to use them because they believed the recorders could cause an unanticipated system shutdown. However, Israeli commanders used data recorders on the Patriot systems they controlled and provided this data to the U.S. Army.

+ Because the Israelis were using the data recorder, they were able to identify the problem quicker than U.S. forces

> On February 11, 1991, the Patriot Project Office received Israeli data identifying a 20 percent shift in the Patriot system's radar range gate after the system had been running for 8 consecutive hours. This shift is significant because it meant that the target (in this case, the Scud) was no longer in the center of the range gate. The target needs to be in the center ofthe range gate to ensure the highest probability of tracking the target. As previously mentioned, the range gate is calculated by an algorithm that determines if the detected target is a Scud, and if the Scud is in the Patriot's firing range. If these conditions are met, the Patriot fires its missiles...

> Patriot Project Office officials said that the Patriot system will not track a Scud when there is a range gate shift of 50 percent or more. Because the shift is directly proportional to time, extrapolating the Israeli data (which indicated a 20 percent shift after 8 hours) determined that the range gate would shift 50 percent after about 20 hours of continuous use. Specifically, after about 20 hours, the inaccurate time calculation becomes sufficiently large to cause the radar to look in the wrong place for the target. Consequently, the system fails to track and intercept the Scud.

http://fas.org/spp/starwars/gao/im92026.htm

<h2>User</h2>

+ Operation Doctrine not explained to operators, they were unaware that the system was intended to target medium to high altitude missiles and be mobile and operate for a few hours. 

+ There US Army ignored warnings from the Patriot Office, and found the Israeli use of the system atypical.

> "When the Patriot Office told the Army, extended use can cause miscalculations, they ignored the memo and did not tell the field users because they thought the Patriot System was still being used as a mobile system"

<h1>Vancouver Stock Exchange</h1>

+ Things were looking grim at the Vancouver Stock Exchange. Brokers and investors on the free-wheeling penny-stock market wondered where the North American bull market had gone, as the exchange index kept dropping. The index, which was established in January 1982 at a level of 1,000, in 1983 had been hitting lows in the 520 range.

+ The exchange had incorrectly calculated the index. The index was based on the selling price of all 1,400 or so stocks listed on the exchange. Every time a stock price changed, which happened 2,800 times on a average day, a computer recalculated the index to three decimal places. The mistake was made in calculating the last decimal place. If the index stood at, say, 540.32567, the computer simply dropped the last two digits, making it 540.325. Instead, it should have rounded off the last digit, making the index 540.326.

+ When the mistake was made a few thousand times a day, the index slipped by up to a point or two daily. Since the mistakes were cumulative, the distortion increased daily. 

+ When the error was identified, the index was updated to reflect the true value of the index, with the values included from the 
truncation. Before the fix, the index was sitting at 524.811. On Monday, the index opened at 1098.892. 

<h1>Ariane 5</h1>

<h2>Quick Background and Disaster</h2>

    + Ariane 5 is a European heavy lift launch vehicle that is part of the Ariane rocket family, an expendable launch system used to deliver payloads into geostationary transfer orbit (GTO) or low Earth orbit (LEO). Ariane 5 rockets are manufactured under the authority of the European Space Agency (ESA) and the Centre National d'Etudes Spatiales.
    
    + On 4 June 1996, the maiden flight of the Ariane 5 launcher ended in a failure. Only about 40 seconds after initiation of the flight sequence, at an altitude of about 3700 m, the launcher veered off its flight path, broke up and exploded.

<h2>Overview of failure</h2>

    + The origin of the failure was thus rapidly narrowed down to the flight control system and more particularly to the Inertial Reference Systems, which obviously ceased to function almost simultaneously at around H0 + 36.7 seconds

    + Events that caused the failure to occur:
        1. The value of Horizontal Bias were much higher than expected because the early part of the trajectory of Ariane 5 differs from that of Ariane 4 and results in considerably higher horizontal velocity values
        2. The Operand Error occurred due to an unexpected high value of an internal alignment function result called BH, Horizontal Bias, related to the horizontal velocity sensed by the platform. This value is calculated as an indicator for alignment precision over time.

        3. The alignment function is operative for 50 seconds after starting of the Flight Mode of the SRIs which occurs at H0 - 3 seconds for Ariane 5. Consequently, when lift-off occurs, the function continues for approx. 40 seconds of flight. This time sequence is based on a requirement of Ariane 4 and is not required for Ariane 5.
            
            + Had this function been eliminated from the software of the Ariane 5, the disaster could have been averted

            + The error occurred in a part of the software that only performs alignment of the strap-down inertial platform. This software module computes meaningful results only before lift-off. As soon as the launcher lifts off, this function serves no purpose.

        4. The internal SRI software exception was caused during execution of a data conversion from 64-bit floating point to 16-bit signed integer value. The floating point number which was converted had a value greater than what could be represented by a 16-bit signed integer. This resulted in an Operand Error. The data conversion instructions (in Ada code) were not protected from causing an Operand Error, although other conversions of comparable variables in the same place in the code were protected.

        5. The OBC could not switch to the back-up SRI 1 because that unit had already ceased to function during the previous data cycle (72 milliseconds period) for the same reason as SRI 2.

        6. Ultimately, the launcher began to disintegrate, which led to the triggering of the self-destruct sequence. 


<h2>Failure in Software</h2>

+ The design of the Ariane 5 SRI was practically the same as that of an SRI which is presently used on Ariane 4, particularly as regards the software.

+ Events that caused the 




















