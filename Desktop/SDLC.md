#V-Model (See Image, credit: http://softobiz.com/wp-content/uploads/2012/03/v-model.png)

##Intro
    + Response to perceived weakness found in the waterfall model
    + Similar to waterfall model
    + Problems with the Waterfall model
        1. Errors and Bugs in the software in the development process, which is very late in the life cycle
        2. Fixing errors and bugs becomes costly and challenging because it is in a later stage in the life cycle
    + "V Model" was introduced to fix this problem
    + The development process does not emphasize any phase specifically. 
    + The process relies on verification from the previous steps before it moves forward.
    + Each cycle has multiple phases, and each one of these phases should yield a predefined product. 
    + When one phase completes, it then forms the foundation for the next phase.
    + Similar to waterfall, you only move on to the next step when the previous step has been completed. 
    + The product is verified at each stage, and cannot move forward until it has been completely verified at a stage

##Left Hand Side

    + Think about the V-shape of the diagram that the SDLC derives its name from
    + The following activities are what are traditional in waterfall, but they have a corresponding right hand side test

<h3>Requirement Analysis</h3>

    + The requirement analysis is the first stage in the V Model
    + The function is decided. Requirements are collected and the needs of the user are analyzed.
    + Determine what the "Ideal System" has to perfrom
    + Users are interviewed and requirements document is generated
    

<h3>System Design</h3>
    
    + Engineers analyze and understand the business of the proposed system by studying the user requirements document.
    + The Engineers devise the possibilites by which the user requirements can be implemented
    + User is informed in this state if any of the requirements are infeasible. The user document is then edited accordingly
    + After this, the software specification document for the development phase is generated. 
    + The software specification document contains how the general system is organized, menu structures, data structures, etc. 

<h3>Architecture Design</h3>

    + Choose the architecture where the work will be done.
    + Carry out the integration testing design 

<h3>Module Design</h3> 

    + The system is broken up into smaller units or modules.
    + Each module is explained to the programmer so that coding can begin directly. 
    + A low level design document is generated. It contains details of the functional logic of the module, the psuedocode for the following:
        1. database tabels
        2. Interface details with complete API references
        3. Dependency Issues
        4. Error message listings
        5. Input and outputs for module
    + The unit test design is developed

## Right Hand Side

    + The right hand side refers to the tests for the corresponding left hand activity

<h3>Unit Testing</h3> 
    + Unit Test Plans (UTPs) are developed during module design phase
    + UTPs executed to eliminate bugs at code level or unit level 
    + Unit: smallest entity which can independently exist
    + Unit testing verifies that the smallest entity can function correctly when isolated from the rest of the codes/units.
    
<h3>Integration Testing</h3>
    + Tests verify that units created and tested independently can coexist and communicate among themselves
    + Test results are shared with customer's team

<h3>System Testing</h3> 
    + System Tests Plans are developed during system design phase.
    + Contrary to unit and integration test plans, system test plans are composed by client's business team.
    + System Test ensures that expectations from application developed are met. 
    + The whole application is tested for its functionality, interdependency and communication
    + System Testing verifies that functional and non-functional requirements have been met
    + Load and performance testing, stress testing, regression testing, etc., are subsets of system testing

<h3>User acceptance testing</h3>
    + Test Plans are composed by business users.
    + User acceptance test is performed in a user environment that is similar to the production environment, using realistic data
    + The test verifies that delivered system meets user's requirement and system is ready for use in real time.

<h3>Benefits and Shortcomings of V Model</h3>

    + Pros
        1. The process is highly disciplined, only one phase is worked on at a time
        2. Easy to work with for smaller projects where requirements are easily understood
        3. The process is easy to manage because it is because it is rigid, an there are specific deliverables for each phase

    + Cons
        1. The model doesn't work well for large projects are projects that are object-oriented intensive
        2. The model doesn't work well for projects where requirements are at a decent risk of changing during work
        3. When an application is in the testing phase, it is difficult to go back and change the functionality
        4. Working software isn't produced until later in the life cycle    

#Big Bang Model(See image, http://api.ning.com/files/mOFzWoNURnZRK4gEqahd8QhfqrhX9iujdj0KKscxHWE0FPRPVNvZ01WObcYwCIV-d*JvTMsTAv5si-kA7BajcygDwVKBTECX/big_bang_model.bmp)

##Intro

    + Similar to the theory explaining the origin of the universe, the model requires huge amounts of money, people, and energy
    + Combining the these inputs, they work and then the output is a software product
    + There is no planning, scheduling, or formal development process.
    + Most of the effort is done developing software and writing the code
    + This model is used usually when there is a single developer, because he can perform the analysis and write the code
    + There is no designated testing phase 
    + This is the most popular model for students who program in introduction classes

###Pros and Cons
    
    + Pros
        1. No defined process
        2. Easy to manage
        3. Good way for students new to programming to start

    + Cons
        1. No defined process
        2. Doesn't scale well for complex projects
        3. Can be costly if requirements are misunderstood


#References 
    + https://lameguy.wordpress.com/2013/05/29/the-big-bang-software-development-lifecycle-model/
    + http://www.roberthalf.com/technology/blog/6-basic-sdlc-methodologies-the-pros-and-cons
    + http://istqbexamcertification.com/what-is-v-model-advantages-disadvantages-and-when-to-use-it/
    + http://www.clarotesting.com/page11.htm


#To Learn More

    + https://www.youtube.com/watch?v=j6rxyRwEdVU
    + https://www.youtube.com/watch?v=H59PBt1xKrE
    



