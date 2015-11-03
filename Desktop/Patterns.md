#Server Session Patterns

    +Maintain a session during while a client is interacting with a server and database
    +Object-Oriented Frameworks are structured in terms of client/server relationship between objects; an object's services are invoked by client objects through the operations of its interface
    + A common design requirement is for a server object to maintain state for each client that it is serving.
    + This is usually implemented by returning handles or untyped pointers to the client that are used to identify the per-client data structure holding its state
    + The lack of strong typing can lead to obscure errors that complicate debugging and maintenance

#Abstract Session

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

