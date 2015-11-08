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
    

