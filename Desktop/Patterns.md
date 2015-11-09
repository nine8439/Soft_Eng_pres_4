#Server Session Patterns

    +Maintain a session during while a client is interacting with a server and database
    +Object-Oriented Frameworks are structured in terms of client/server relationship between objects; an object's services are invoked by client objects through the operations of its interface
    + A common design requirement is for a server object to maintain state for each client that it is serving.
    + This is usually implemented by returning handles or untyped pointers to the client that are used to identify the per-client data structure holding its state
    + The lack of strong typing can lead to obscure errors that complicate debugging and maintenance

#Abstract Session

##Motivation

    + Allows objects to maintain per-client state with full type safety and no loss of efficiency
    + Also known as: Service Access Point, Context, Service Handler
    + Object interactions are defined in terms of abstract interface, which increase reusability and extensibility of the framework because the set of client and server types that can be used together is not bounded and can easily be extended by framework users. 
    + Although client objects are defined in terms of abstract interfaces, per-client state cannot be stored in the client objects themselves because different server implementations will have to store different information
    + Session Pattern imposes three-phase protocol on the interactions between the client and the server:
        1. Clients make an initial "request" call to the server when they begin to use it services. The server responds by allocating a per-client data structure for the new client and returns an identifier of that data structure to the client.
        2. The client passes the identifier it received as an argument to subsequent operations on the server. The server uses that identifier to find the per-client information it holds about the caller.
        3. When the client has finished using the server, it makes a final "release" call to the server, passing in the identifier that the server uses to find and deallocate the the appropriate per-client data structure.
    + Session pattern involves resolving the following forces:
        1. Per-client state: The server object must be able to store state about each client that is using its services
        2. Efficieny: Invocation of service operations should involve minimum run-time overhead
        3. Safety: The implementation should catch the use of incorrect session identifiers. Ideally, such error should be caught at compile-time

    + Two methods to map from identifiers to the data structures used internally to store per-client state:
        1. Untyped Pointers: Identifiers are defined to be untyped pointers that the server object initializes to point to an implementation-specific data structure and casts to the appropriate type on each invocation. 
        2. Handles: Identifiers are defined to be values of simple types, such as integers, or opaque values. The server uses a private associative container to map between identifiers and implementation-specific data structures and must perform a lookup each time a client makes a request.

    + Choosing between untyped pointers or handles is one of safety versus run-time efficiency. Untyped pointers are efficient, but passing an incorrect pointer to a server could cause the program to corrupt memory or crash.
    + Using handles as indices to an associative container allows incorrect identifiers to be detected at run-time but at the expense of performing a lookup on each invocation, which can be costly if many invocations are made during a time-critical part of a program.
    + Both approaches can be unsafe: a client can pass an incorrect identifier to the server without the errors being caught at compile time.

##Implementation 

    + A protocol service object, rather than providing a client with a handle to be passed as an argument to the operations of its abstract interface, instead creates an intermediate session object and returns a pointer to the session object to the client. 

    + The session object encapsulates the state information for the client that owns the session 

    + Use Abstract Session pattern:
        1. Interactions between server objects and client objects are defined in terms of abstract interfaces. 

        2. Server objects must maintain state for each client object that makes use of their services. 

##Structure and Participants

    + ServiceX: Classes of server objects that create session objects for clients that are bound to them

    + Abstract Session (Channel Session). The interface through which clients bound to a server object make use of the service provided by that object.

    + ServiceX::Session (TCPSession). The session classes used by the ServiceX classes to store information about clients that are bound to them. Clients invoke the Abstract Session interfaces of these objects to interact with the server objects to which they are bound. 

    + ClientN (HttpHandler, TalnetClient). Objects that are making use of ServiceX through the AbstractSession interface.


##Collaborations

    + A Client object that wants to use a server object request a session from the server. The server object creates a session object (which conforms to the AbstractSession interface), initializes the session with information about the client, and returns a pointer to the session back to the client.

    + The client uses the service provided by the server object by invoking the operations of its session object's Abstract Session interface. The session object cooperates with the server object to complete the invocation.

    + The server object uses information stored in the session object to process requests from its clients and can update the per-client information when events occur behind the scenes that relate to the client.

    + When a client object has finished using the service provided by the server object, it call the <i>release</i> operation of its session. Forcing clients to release sessions by calling <i>release</i> allows a service to hide the way it allocates session objects from its clients. A service could allocate sessions on the heap, in which case the <i>release</i> operation would free the session object, or a service could have a fixed number of sessions in an array, in which case <i>release</i> would update a record in the service object of the sessions that were unused and could be handed out to new clients.

##Advantages of Abstract Session Pattern

    + Type Safety: Interactions between clients and sessions and between sessions and servers are completely type-safe. This reduces the likelihood of obscure errors, making the code easier to debug and maintain.
    
    + Performance: The interactions between clients and sessions are as fast or faster than those using unsafe methods such as untyped pointer or handles.

    + Flexibility: The use of abstract interfaces and encapsulation of per client state within each server class reduces coupling between client and server classes. A client can use any server that creates sessions that implement the AbstractSession interface. 

    + Extensibility: The pattern makes it easy to add server classes to the system; such extensions do not require existing client and server classes to change.

##Disadvantages of Abstract Session Pattern

    + Dangling Pointers. It is possible that a session referenced and used after it has been released.

    + Distribution. It is difficult to pass a session object from the server to the client if the client and server exist in different address spaces. When creating a session, the server must send information to the client to allow the client to create a proxy session in its local address space. 

    + Multiple Languages. It is difficult to call Abstract Sessions from another language, especially from languages that are not object-oriented. This can be solved by writing an adapter layer that hides session objects behind a set of procedures callable from the other languages and that uses one of the unsafe implementations of the Session pattern to identify session objects.
    

##Different forms of implementation

    + Use of the heap. Allocating and deallocating memory from the heap is an expensive operation. Forcing clients to discard sessions via the <i>release</i> method in the AbstractSession interface, rather than an explicit deallocation of the session object, gives server objects more flexibility in the allocation of session objecs. For instance, if the server allocated the session from the heap, the <i>release</i> operation would delete the session object. However, a server might preallocate sessions in a cache; when a client invokes the <i>release</i> operation of a session, it need only mark that the session is unused rather than perform a heap deallocation. If a server object does not need to store any information about its clients, it can implement the AbstractSession interface itself, perhaps using private inheritance, in this case, the <i>release</i> operation would do nothing.

    + Object finalization. In a language with automatic garbage collection and object finalization, the act of releasing a session can be made synonymous with releasing the last reference to the Session object. The functionality of releasing a session can be performed by the finalization method of the Session object and so will be called automatically by the garbage collector.

    + Java outer/inner classes. A Java implementation of this pattern can be simplified using inner classes. The concrete Service class would be implemented as an outer class, and the concrete Session classes would be defined as inner classes. An inner class is associated with an instance of the outer class in which it is defined and can refer directly to the fields and methods of that instance. Thus, inner classes remove the need for explicit delegation from session to service and reduce the possibility of programming errors. 

    +   Defining server interfaces. If clients are always bound to servers by some third party that knows the complete type of all servers it is using, then server objects do not need to conform to an abstract interface. However, in some systems clients will bind themselves to servers by finding a suitable server object in something like a trader or namespace and then request a session from it, in this case servers will need to conform to some abstract interface that can be used polymorphically. 

##Known Uses 

    + Abstract Session patter is widely used in the implementation of object-oriented communication protocol software. The x-kernel framework and the ACE communications toolkit both use this pattern.

    + Microsoft's Object Linking and Embedding framework
        1. Manage the size and location of embedded objects. 
        2. An object such as word-processing document that can contain embedded objects is known as a "container" and stores pointers to the IOleObject interfaces of its embedded objects. Through this interface the container can, among other things, query the required size of the embedded object and set the size and position of the object. 
        3. When a new IOleObject is embedded in the container, the container creates a Session object, know as a client-site, in which it stores information about the actual position and size of the embedded object.
        4. The client-site object implements the IOleClientSite interface that the container passes to the embedded object and through which the embedded object can request to be resized.
        5. When an embedded object makes a resize request through its IOleClientSite interface, the container updates the size and position of all its embedded objects base on the information stored in the client-site session object.

    + Java Abstract Windowing Toolkit (AWT)
        1. An example of where the Abstract Session pattern is used is the <i>Graphics</i> interface. 
        2. This interface provides a common interface for drawing graphics on a variety of devices, such as windows, bitmaps and printers.
        3. An object that wants to draw onto a device asks the device to create a graphics context object and receives a reference to the object's <i>Graphics</i> interface. 
        4. The graphics context stores the current drawing state, such as the current font, background and foreground colors, and other states required to render drawing operations onto the associated device. 

    + Related Patterns
        + Related to the Facade, Factory Method, and Mediator patterns
            1. The Facade pattern uses a single intermediate object to hide the complexities of a framework of cooperating objects from the users of that framework. In contrast, the Session pattern uses multiple intermediate objects to decouple objects that provide a service from the objects that use that service and to provide type-safe interaction between objects that interact only through abstract interfaces. 

            2. The Server object uses the Factory Method to create sessions for a client. This ensures that sessions can be initialized correctly by the server object.
            3. A Mediator object controls the interaction of multiple cooperating objects. The Server object of the Abstract Session pattern can be viewed as a form of Mediator controlling the interaction of all of its clients. The session objects can be viewed as simple Mediators controlling the interaction of the server and a single client. 

#Session Facade Pattern

    ##Motivation
        + Enterprise beans encapsulate business logic and business data and expose their interfaces, and thus the complexity of the distributed services, to the client tier.

    ##Problem 
        + In a multitiered Java 2 Platform, Enterprise Edition (J2EE) application environment, the following problems arise:
            1. Tight coupling, which leads to direct dependence between clients and business objects
            2. Too many method invocations between client and server, leading to network performance problems
            3. Lack of a uniform client access strategy, exposing business objects to misuse.

        + A multitiered J2EE application has numerous server-side objects that are implemented as enterprise beans. In addition, some other arbitrary objects may provide services, data, or both. These objects are collectively referred to as business objects, since they encapsulate business data and business logic.

        + J2EE applications implement business objects that provide processing services as session beans. Coarse-grained business objects that represent an object view of persistent storage and are shared by multiple users are usually implemented as entity beans.

        + Application clients need access to business objects to fulfill their responsibilities and to meet user requirements. Clients can directly interact with these business objects because they expose their interfaces. When you expose business objects to the client, the client must understand and be responsible for the business data object relationships, and must be able to handle business process flow.

        + However, direct interaction between the client and the business objects leads to tight coupling between the two, and such tight coupling makes the client directly dependent on the implementation of the business objects. Direct dependence means that the client must represent and implement the complex interactions regarding business object lookups and creations, and must manage the relationships between the participating business objects as well as understand the responsibility of transaction demarcation.

        + As client requirements increase, the complexity of interaction between various business objects increases. The client grows larger and more complex to fulfill these requirements. The client becomes very susceptible to changes in the business object layer; in addition, the client is unnecessarily exposed to the underlying complexity of the system.

        + Tight coupling between objects also results when objects manage their relationship within themselves. Often, it is not clear where the relationship is managed. This leads to complex relationships between business objects and rigidity in the application. Such lack of flexibility makes the application less manageable when changes are required.

        + When accessing the enterprise beans, clients interact with remote objects. Network performance problems may result if the client directly interacts with all the participating business objects. When invoking enterprise beans, every client invocation is potentially a remote method call. Each access to the business object is relatively fine-grained. As the number of participants increases in a scenario, the number of such remote method calls increases. As the number of remote method calls increases, the chattiness between the client and the server-side business objects increases. This may result in network performance degradation for the application, because the high volume of remote method calls increases the amount of interaction across the network layer.

        + A problem also arises when a client interacts directly with the business objects. Since the business objects are directly exposed to the clients, there is no unified strategy for accessing the business objects. Without such a uniform client access strategy, the business objects are exposed to clients and may reduce consistent usage.

    

