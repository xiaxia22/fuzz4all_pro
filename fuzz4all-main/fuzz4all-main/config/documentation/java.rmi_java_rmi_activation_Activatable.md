# Class Activatable

**Source:** `java.rmi\java\rmi\activation\Activatable.html`

### Class Description

```java
public abstract class
Activatable

extends
RemoteServer
```

The

Activatable

class provides support for remote
objects that require persistent access over time and that
can be activated by the system.

For the constructors and static

exportObject

methods,
the stub for a remote object being exported is obtained as described in

UnicastRemoteObject

.

An attempt to serialize explicitly an instance of this class will
fail.

**All Implemented Interfaces:** Serializable

,

Remote

---

### Field Details

*No entries found.*

### Constructor Details

#### protected Activatable​(
String
location,

MarshalledObject
<?> data,
boolean restart,
int port)
throws
ActivationException
,

RemoteException

Constructs an activatable remote object by registering
an activation descriptor (with the specified location, data, and
restart mode) for this object, and exporting the object with the
specified port.

Note:

Using the

Activatable

constructors that both register and export an activatable remote
object is strongly discouraged because the actions of registering
and exporting the remote object are

not

guaranteed to be
atomic. Instead, an application should register an activation
descriptor and export a remote object separately, so that exceptions
can be handled properly.

This method invokes the

exportObject

method with this object, and the specified location,
data, restart mode, and port. Subsequent calls to

getID()

will return the activation identifier returned from the call to

exportObject

.

**Parameters:**
- location

- the location for classes for this object
- data

- the object's initialization data
- port

- the port on which the object is exported (an anonymous
port is used if port=0)
- restart

- if true, the object is restarted (reactivated) when
either the activator is restarted or the object's activation group
is restarted after an unexpected crash; if false, the object is only
activated on demand. Specifying

restart

to be

true

does not force an initial immediate activation of
a newly registered object; initial activation is lazy.

**Throws:**
- ActivationException

- if object registration fails.
- RemoteException

- if either of the following fails:
a) registering the object with the activation system or b) exporting
the object to the RMI runtime.
- UnsupportedOperationException

- if and only if activation is
not supported by this implementation.

**Since:**
- 1.2

---

#### protected Activatable​(
String
location,

MarshalledObject
<?> data,
boolean restart,
int port,

RMIClientSocketFactory
csf,

RMIServerSocketFactory
ssf)
throws
ActivationException
,

RemoteException

Constructs an activatable remote object by registering
an activation descriptor (with the specified location, data, and
restart mode) for this object, and exporting the object with the
specified port, and specified client and server socket factories.

Note:

Using the

Activatable

constructors that both register and export an activatable remote
object is strongly discouraged because the actions of registering
and exporting the remote object are

not

guaranteed to be
atomic. Instead, an application should register an activation
descriptor and export a remote object separately, so that exceptions
can be handled properly.

This method invokes the

exportObject

method with this object, and the specified location,
data, restart mode, port, and client and server socket factories.
Subsequent calls to

getID()

will return the activation
identifier returned from the call to

exportObject

.

**Parameters:**
- location

- the location for classes for this object
- data

- the object's initialization data
- restart

- if true, the object is restarted (reactivated) when
either the activator is restarted or the object's activation group
is restarted after an unexpected crash; if false, the object is only
activated on demand. Specifying

restart

to be

true

does not force an initial immediate activation of
a newly registered object; initial activation is lazy.
- port

- the port on which the object is exported (an anonymous
port is used if port=0)
- csf

- the client-side socket factory for making calls to the
remote object
- ssf

- the server-side socket factory for receiving remote calls

**Throws:**
- ActivationException

- if object registration fails.
- RemoteException

- if either of the following fails:
a) registering the object with the activation system or b) exporting
the object to the RMI runtime.
- UnsupportedOperationException

- if and only if activation is
not supported by this implementation.

**Since:**
- 1.2

---

#### protected Activatable​(
ActivationID
id,
int port)
throws
RemoteException

Constructor used to activate/export the object on a specified
port. An "activatable" remote object must have a constructor that
takes two arguments:

- the object's activation identifier (

ActivationID

), and

the object's initialization data (a

MarshalledObject

).

A concrete subclass of this class must call this constructor when it is

activated

via the two parameter constructor described above. As
a side-effect of construction, the remote object is "exported"
to the RMI runtime (on the specified

port

) and is
available to accept incoming calls from clients.

**Parameters:**
- id

- activation identifier for the object
- port

- the port number on which the object is exported

**Throws:**
- RemoteException

- if exporting the object to the RMI
runtime fails
- UnsupportedOperationException

- if and only if activation is
not supported by this implementation

**Since:**
- 1.2

---

#### protected Activatable​(
ActivationID
id,
int port,

RMIClientSocketFactory
csf,

RMIServerSocketFactory
ssf)
throws
RemoteException

Constructor used to activate/export the object on a specified
port. An "activatable" remote object must have a constructor that
takes two arguments:

- the object's activation identifier (

ActivationID

), and

the object's initialization data (a

MarshalledObject

).

A concrete subclass of this class must call this constructor when it is

activated

via the two parameter constructor described above. As
a side-effect of construction, the remote object is "exported"
to the RMI runtime (on the specified

port

) and is
available to accept incoming calls from clients.

**Parameters:**
- id

- activation identifier for the object
- port

- the port number on which the object is exported
- csf

- the client-side socket factory for making calls to the
remote object
- ssf

- the server-side socket factory for receiving remote calls

**Throws:**
- RemoteException

- if exporting the object to the RMI
runtime fails
- UnsupportedOperationException

- if and only if activation is
not supported by this implementation

**Since:**
- 1.2

---

### Method Details

#### protected
ActivationID
getID()

Returns the object's activation identifier. The method is
protected so that only subclasses can obtain an object's
identifier.

**Returns:**
- the object's activation identifier

**Since:**
- 1.2

---

#### public static
Remote
register​(
ActivationDesc
desc)
throws
UnknownGroupException
,

ActivationException
,

RemoteException

Register an object descriptor for an activatable remote
object so that is can be activated on demand.

**Parameters:**
- desc

- the object's descriptor

**Returns:**
- the stub for the activatable remote object

**Throws:**
- UnknownGroupException

- if group id in

desc

is not registered with the activation system
- ActivationException

- if activation system is not running
- RemoteException

- if remote call fails
- UnsupportedOperationException

- if and only if activation is
not supported by this implementation

**Since:**
- 1.2

---

#### public static boolean inactive​(
ActivationID
id)
throws
UnknownObjectException
,

ActivationException
,

RemoteException

Informs the system that the object with the corresponding activation

id

is currently inactive. If the object is currently
active, the object is "unexported" from the RMI runtime (only if
there are no pending or in-progress calls)
so the that it can no longer receive incoming calls. This call
informs this VM's ActivationGroup that the object is inactive,
that, in turn, informs its ActivationMonitor. If this call
completes successfully, a subsequent activate request to the activator
will cause the object to reactivate. The operation may still
succeed if the object is considered active but has already
unexported itself.

**Parameters:**
- id

- the object's activation identifier

**Returns:**
- true if the operation succeeds (the operation will
succeed if the object in currently known to be active and is
either already unexported or is currently exported and has no
pending/executing calls); false is returned if the object has
pending/executing calls in which case it cannot be deactivated

**Throws:**
- UnknownObjectException

- if object is not known (it may
already be inactive)
- ActivationException

- if group is not active
- RemoteException

- if call informing monitor fails
- UnsupportedOperationException

- if and only if activation is
not supported by this implementation

**Since:**
- 1.2

---

#### public static void unregister​(
ActivationID
id)
throws
UnknownObjectException
,

ActivationException
,

RemoteException

Revokes previous registration for the activation descriptor
associated with

id

. An object can no longer be
activated via that

id

.

**Parameters:**
- id

- the object's activation identifier

**Throws:**
- UnknownObjectException

- if object (

id

) is unknown
- ActivationException

- if activation system is not running
- RemoteException

- if remote call to activation system fails
- UnsupportedOperationException

- if and only if activation is
not supported by this implementation

**Since:**
- 1.2

---

#### public static
ActivationID
exportObject​(
Remote
obj,

String
location,

MarshalledObject
<?> data,
boolean restart,
int port)
throws
ActivationException
,

RemoteException

Registers an activation descriptor (with the specified location,
data, and restart mode) for the specified object, and exports that
object with the specified port.

Note:

Using this method (as well as the

Activatable

constructors that both register and export
an activatable remote object) is strongly discouraged because the
actions of registering and exporting the remote object are

not

guaranteed to be atomic. Instead, an application should
register an activation descriptor and export a remote object
separately, so that exceptions can be handled properly.

This method invokes the

exportObject

method with the specified object, location, data,
restart mode, and port, and

null

for both client and
server socket factories, and then returns the resulting activation
identifier.

**Parameters:**
- obj

- the object being exported
- location

- the object's code location
- data

- the object's bootstrapping data
- restart

- if true, the object is restarted (reactivated) when
either the activator is restarted or the object's activation group
is restarted after an unexpected crash; if false, the object is only
activated on demand. Specifying

restart

to be

true

does not force an initial immediate activation of
a newly registered object; initial activation is lazy.
- port

- the port on which the object is exported (an anonymous
port is used if port=0)

**Returns:**
- the activation identifier obtained from registering the
descriptor,

desc

, with the activation system
the wrong group

**Throws:**
- ActivationException

- if activation group is not active
- RemoteException

- if object registration or export fails
- UnsupportedOperationException

- if and only if activation is
not supported by this implementation

**Since:**
- 1.2

---

#### public static
ActivationID
exportObject​(
Remote
obj,

String
location,

MarshalledObject
<?> data,
boolean restart,
int port,

RMIClientSocketFactory
csf,

RMIServerSocketFactory
ssf)
throws
ActivationException
,

RemoteException

Registers an activation descriptor (with the specified location,
data, and restart mode) for the specified object, and exports that
object with the specified port, and the specified client and server
socket factories.

Note:

Using this method (as well as the

Activatable

constructors that both register and export
an activatable remote object) is strongly discouraged because the
actions of registering and exporting the remote object are

not

guaranteed to be atomic. Instead, an application should
register an activation descriptor and export a remote object
separately, so that exceptions can be handled properly.

This method first registers an activation descriptor for the
specified object as follows. It obtains the activation system by
invoking the method

ActivationGroup.getSystem

. This method then obtains an

ActivationID

for the object by invoking the activation system's

registerObject

method with
an

ActivationDesc

constructed with the specified object's
class name, and the specified location, data, and restart mode. If
an exception occurs obtaining the activation system or registering
the activation descriptor, that exception is thrown to the caller.

Next, this method exports the object by invoking the

exportObject

method with the specified remote object, the
activation identifier obtained from registration, the specified
port, and the specified client and server socket factories. If an
exception occurs exporting the object, this method attempts to
unregister the activation identifier (obtained from registration) by
invoking the activation system's

unregisterObject

method with the
activation identifier. If an exception occurs unregistering the
identifier, that exception is ignored, and the original exception
that occurred exporting the object is thrown to the caller.

Finally, this method invokes the

activeObject

method on the activation
group in this VM with the activation identifier and the specified
remote object, and returns the activation identifier to the caller.

**Parameters:**
- obj

- the object being exported
- location

- the object's code location
- data

- the object's bootstrapping data
- restart

- if true, the object is restarted (reactivated) when
either the activator is restarted or the object's activation group
is restarted after an unexpected crash; if false, the object is only
activated on demand. Specifying

restart

to be

true

does not force an initial immediate activation of
a newly registered object; initial activation is lazy.
- port

- the port on which the object is exported (an anonymous
port is used if port=0)
- csf

- the client-side socket factory for making calls to the
remote object
- ssf

- the server-side socket factory for receiving remote calls

**Returns:**
- the activation identifier obtained from registering the
descriptor with the activation system

**Throws:**
- ActivationException

- if activation group is not active
- RemoteException

- if object registration or export fails
- UnsupportedOperationException

- if and only if activation is
not supported by this implementation

**Since:**
- 1.2

---

#### public static
Remote
exportObject​(
Remote
obj,

ActivationID
id,
int port)
throws
RemoteException

Export the activatable remote object to the RMI runtime to make
the object available to receive incoming calls. The object is
exported on an anonymous port, if

port

is zero.

During activation, this

exportObject

method should
be invoked explicitly by an "activatable" object, that does not
extend the

Activatable

class. There is no need for objects
that do extend the

Activatable

class to invoke this
method directly because the object is exported during construction.

**Parameters:**
- obj

- the remote object implementation
- id

- the object's activation identifier
- port

- the port on which the object is exported (an anonymous
port is used if port=0)

**Returns:**
- the stub for the activatable remote object

**Throws:**
- RemoteException

- if object export fails
- UnsupportedOperationException

- if and only if activation is
not supported by this implementation

**Since:**
- 1.2

---

#### public static
Remote
exportObject​(
Remote
obj,

ActivationID
id,
int port,

RMIClientSocketFactory
csf,

RMIServerSocketFactory
ssf)
throws
RemoteException

Export the activatable remote object to the RMI runtime to make
the object available to receive incoming calls. The object is
exported on an anonymous port, if

port

is zero.

During activation, this

exportObject

method should
be invoked explicitly by an "activatable" object, that does not
extend the

Activatable

class. There is no need for objects
that do extend the

Activatable

class to invoke this
method directly because the object is exported during construction.

**Parameters:**
- obj

- the remote object implementation
- id

- the object's activation identifier
- port

- the port on which the object is exported (an anonymous
port is used if port=0)
- csf

- the client-side socket factory for making calls to the
remote object
- ssf

- the server-side socket factory for receiving remote calls

**Returns:**
- the stub for the activatable remote object

**Throws:**
- RemoteException

- if object export fails
- UnsupportedOperationException

- if and only if activation is
not supported by this implementation

**Since:**
- 1.2

---

#### public static boolean unexportObject​(
Remote
obj,
boolean force)
throws
NoSuchObjectException

Remove the remote object, obj, from the RMI runtime. If
successful, the object can no longer accept incoming RMI calls.
If the force parameter is true, the object is forcibly unexported
even if there are pending calls to the remote object or the
remote object still has calls in progress. If the force
parameter is false, the object is only unexported if there are
no pending or in progress calls to the object.

**Parameters:**
- obj

- the remote object to be unexported
- force

- if true, unexports the object even if there are
pending or in-progress calls; if false, only unexports the object
if there are no pending or in-progress calls

**Returns:**
- true if operation is successful, false otherwise

**Throws:**
- NoSuchObjectException

- if the remote object is not
currently exported
- UnsupportedOperationException

- if and only if activation is
not supported by this implementation

**Since:**
- 1.2

---

### Additional Sections

#### Class Activatable

java.lang.Object

- java.rmi.server.RemoteObject
- - java.rmi.server.RemoteServer
- - java.rmi.activation.Activatable

java.rmi.server.RemoteObject

- java.rmi.server.RemoteServer
- - java.rmi.activation.Activatable

java.rmi.server.RemoteServer

- java.rmi.activation.Activatable

java.rmi.activation.Activatable

**All Implemented Interfaces:** Serializable

,

Remote

```java
public abstract class
Activatable

extends
RemoteServer
```

The

Activatable

class provides support for remote
objects that require persistent access over time and that
can be activated by the system.

For the constructors and static

exportObject

methods,
the stub for a remote object being exported is obtained as described in

UnicastRemoteObject

.

An attempt to serialize explicitly an instance of this class will
fail.

**Since:** 1.2

public abstract class

Activatable

extends

RemoteServer

The

Activatable

class provides support for remote
objects that require persistent access over time and that
can be activated by the system.

For the constructors and static

exportObject

methods,
the stub for a remote object being exported is obtained as described in

UnicastRemoteObject

.

An attempt to serialize explicitly an instance of this class will
fail.

For the constructors and static

exportObject

methods,
the stub for a remote object being exported is obtained as described in

UnicastRemoteObject

.

An attempt to serialize explicitly an instance of this class will
fail.

An attempt to serialize explicitly an instance of this class will
fail.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.rmi.server.

RemoteObject

ref

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Activatable

​(

String

location,

MarshalledObject

<?> data,
boolean restart,
int port)

Constructs an activatable remote object by registering
an activation descriptor (with the specified location, data, and
restart mode) for this object, and exporting the object with the
specified port.

protected

Activatable

​(

String

location,

MarshalledObject

<?> data,
boolean restart,
int port,

RMIClientSocketFactory

csf,

RMIServerSocketFactory

ssf)

Constructs an activatable remote object by registering
an activation descriptor (with the specified location, data, and
restart mode) for this object, and exporting the object with the
specified port, and specified client and server socket factories.

protected

Activatable

​(

ActivationID

id,
int port)

Constructor used to activate/export the object on a specified
port.

protected

Activatable

​(

ActivationID

id,
int port,

RMIClientSocketFactory

csf,

RMIServerSocketFactory

ssf)

Constructor used to activate/export the object on a specified
port.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

ActivationID

exportObject

​(

Remote

obj,

String

location,

MarshalledObject

<?> data,
boolean restart,
int port)

Registers an activation descriptor (with the specified location,
data, and restart mode) for the specified object, and exports that
object with the specified port.

static

ActivationID

exportObject

​(

Remote

obj,

String

location,

MarshalledObject

<?> data,
boolean restart,
int port,

RMIClientSocketFactory

csf,

RMIServerSocketFactory

ssf)

Registers an activation descriptor (with the specified location,
data, and restart mode) for the specified object, and exports that
object with the specified port, and the specified client and server
socket factories.

static

Remote

exportObject

​(

Remote

obj,

ActivationID

id,
int port)

Export the activatable remote object to the RMI runtime to make
the object available to receive incoming calls.

static

Remote

exportObject

​(

Remote

obj,

ActivationID

id,
int port,

RMIClientSocketFactory

csf,

RMIServerSocketFactory

ssf)

Export the activatable remote object to the RMI runtime to make
the object available to receive incoming calls.

protected

ActivationID

getID

()

Returns the object's activation identifier.

static boolean

inactive

​(

ActivationID

id)

Informs the system that the object with the corresponding activation

id

is currently inactive.

static

Remote

register

​(

ActivationDesc

desc)

Register an object descriptor for an activatable remote
object so that is can be activated on demand.

static boolean

unexportObject

​(

Remote

obj,
boolean force)

Remove the remote object, obj, from the RMI runtime.

static void

unregister

​(

ActivationID

id)

Revokes previous registration for the activation descriptor
associated with

id

.

- Methods declared in class java.rmi.server.

RemoteServer

getClientHost

,

getLog

,

setLog

- Methods declared in class java.rmi.server.

RemoteObject

equals

,

getRef

,

hashCode

,

toString

,

toStub

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

Field Summary

- Fields declared in class java.rmi.server.

RemoteObject

ref

---

#### Field Summary

Fields declared in class java.rmi.server.

RemoteObject

ref

---

#### Fields declared in class java.rmi.server. RemoteObject

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Activatable

​(

String

location,

MarshalledObject

<?> data,
boolean restart,
int port)

Constructs an activatable remote object by registering
an activation descriptor (with the specified location, data, and
restart mode) for this object, and exporting the object with the
specified port.

protected

Activatable

​(

String

location,

MarshalledObject

<?> data,
boolean restart,
int port,

RMIClientSocketFactory

csf,

RMIServerSocketFactory

ssf)

Constructs an activatable remote object by registering
an activation descriptor (with the specified location, data, and
restart mode) for this object, and exporting the object with the
specified port, and specified client and server socket factories.

protected

Activatable

​(

ActivationID

id,
int port)

Constructor used to activate/export the object on a specified
port.

protected

Activatable

​(

ActivationID

id,
int port,

RMIClientSocketFactory

csf,

RMIServerSocketFactory

ssf)

Constructor used to activate/export the object on a specified
port.

---

#### Constructor Summary

Constructs an activatable remote object by registering
an activation descriptor (with the specified location, data, and
restart mode) for this object, and exporting the object with the
specified port.

Constructs an activatable remote object by registering
an activation descriptor (with the specified location, data, and
restart mode) for this object, and exporting the object with the
specified port, and specified client and server socket factories.

Constructor used to activate/export the object on a specified
port.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

ActivationID

exportObject

​(

Remote

obj,

String

location,

MarshalledObject

<?> data,
boolean restart,
int port)

Registers an activation descriptor (with the specified location,
data, and restart mode) for the specified object, and exports that
object with the specified port.

static

ActivationID

exportObject

​(

Remote

obj,

String

location,

MarshalledObject

<?> data,
boolean restart,
int port,

RMIClientSocketFactory

csf,

RMIServerSocketFactory

ssf)

Registers an activation descriptor (with the specified location,
data, and restart mode) for the specified object, and exports that
object with the specified port, and the specified client and server
socket factories.

static

Remote

exportObject

​(

Remote

obj,

ActivationID

id,
int port)

Export the activatable remote object to the RMI runtime to make
the object available to receive incoming calls.

static

Remote

exportObject

​(

Remote

obj,

ActivationID

id,
int port,

RMIClientSocketFactory

csf,

RMIServerSocketFactory

ssf)

Export the activatable remote object to the RMI runtime to make
the object available to receive incoming calls.

protected

ActivationID

getID

()

Returns the object's activation identifier.

static boolean

inactive

​(

ActivationID

id)

Informs the system that the object with the corresponding activation

id

is currently inactive.

static

Remote

register

​(

ActivationDesc

desc)

Register an object descriptor for an activatable remote
object so that is can be activated on demand.

static boolean

unexportObject

​(

Remote

obj,
boolean force)

Remove the remote object, obj, from the RMI runtime.

static void

unregister

​(

ActivationID

id)

Revokes previous registration for the activation descriptor
associated with

id

.

- Methods declared in class java.rmi.server.

RemoteServer

getClientHost

,

getLog

,

setLog

- Methods declared in class java.rmi.server.

RemoteObject

equals

,

getRef

,

hashCode

,

toString

,

toStub

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Registers an activation descriptor (with the specified location,
data, and restart mode) for the specified object, and exports that
object with the specified port.

Registers an activation descriptor (with the specified location,
data, and restart mode) for the specified object, and exports that
object with the specified port, and the specified client and server
socket factories.

Export the activatable remote object to the RMI runtime to make
the object available to receive incoming calls.

Returns the object's activation identifier.

Informs the system that the object with the corresponding activation

id

is currently inactive.

Register an object descriptor for an activatable remote
object so that is can be activated on demand.

Remove the remote object, obj, from the RMI runtime.

Revokes previous registration for the activation descriptor
associated with

id

.

Methods declared in class java.rmi.server.

RemoteServer

getClientHost

,

getLog

,

setLog

---

#### Methods declared in class java.rmi.server. RemoteServer

Methods declared in class java.rmi.server.

RemoteObject

equals

,

getRef

,

hashCode

,

toString

,

toStub

---

#### Methods declared in class java.rmi.server. RemoteObject

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Activatable

```java
protected Activatable​(
String
location,

MarshalledObject
<?> data,
boolean restart,
int port)
throws
ActivationException
,

RemoteException
```

Constructs an activatable remote object by registering
an activation descriptor (with the specified location, data, and
restart mode) for this object, and exporting the object with the
specified port.

Note:

Using the

Activatable

constructors that both register and export an activatable remote
object is strongly discouraged because the actions of registering
and exporting the remote object are

not

guaranteed to be
atomic. Instead, an application should register an activation
descriptor and export a remote object separately, so that exceptions
can be handled properly.

This method invokes the

exportObject

method with this object, and the specified location,
data, restart mode, and port. Subsequent calls to

getID()

will return the activation identifier returned from the call to

exportObject

.

**Parameters:** location

- the location for classes for this object
**Parameters:** data

- the object's initialization data
**Parameters:** port

- the port on which the object is exported (an anonymous
port is used if port=0)
**Parameters:** restart

- if true, the object is restarted (reactivated) when
either the activator is restarted or the object's activation group
is restarted after an unexpected crash; if false, the object is only
activated on demand. Specifying

restart

to be

true

does not force an initial immediate activation of
a newly registered object; initial activation is lazy.
**Throws:** ActivationException

- if object registration fails.
**Throws:** RemoteException

- if either of the following fails:
a) registering the object with the activation system or b) exporting
the object to the RMI runtime.
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation.
**Since:** 1.2

- Activatable

```java
protected Activatable​(
String
location,

MarshalledObject
<?> data,
boolean restart,
int port,

RMIClientSocketFactory
csf,

RMIServerSocketFactory
ssf)
throws
ActivationException
,

RemoteException
```

Constructs an activatable remote object by registering
an activation descriptor (with the specified location, data, and
restart mode) for this object, and exporting the object with the
specified port, and specified client and server socket factories.

Note:

Using the

Activatable

constructors that both register and export an activatable remote
object is strongly discouraged because the actions of registering
and exporting the remote object are

not

guaranteed to be
atomic. Instead, an application should register an activation
descriptor and export a remote object separately, so that exceptions
can be handled properly.

This method invokes the

exportObject

method with this object, and the specified location,
data, restart mode, port, and client and server socket factories.
Subsequent calls to

getID()

will return the activation
identifier returned from the call to

exportObject

.

**Parameters:** location

- the location for classes for this object
**Parameters:** data

- the object's initialization data
**Parameters:** restart

- if true, the object is restarted (reactivated) when
either the activator is restarted or the object's activation group
is restarted after an unexpected crash; if false, the object is only
activated on demand. Specifying

restart

to be

true

does not force an initial immediate activation of
a newly registered object; initial activation is lazy.
**Parameters:** port

- the port on which the object is exported (an anonymous
port is used if port=0)
**Parameters:** csf

- the client-side socket factory for making calls to the
remote object
**Parameters:** ssf

- the server-side socket factory for receiving remote calls
**Throws:** ActivationException

- if object registration fails.
**Throws:** RemoteException

- if either of the following fails:
a) registering the object with the activation system or b) exporting
the object to the RMI runtime.
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation.
**Since:** 1.2

- Activatable

```java
protected Activatable​(
ActivationID
id,
int port)
throws
RemoteException
```

Constructor used to activate/export the object on a specified
port. An "activatable" remote object must have a constructor that
takes two arguments:

- the object's activation identifier (

ActivationID

), and

the object's initialization data (a

MarshalledObject

).

A concrete subclass of this class must call this constructor when it is

activated

via the two parameter constructor described above. As
a side-effect of construction, the remote object is "exported"
to the RMI runtime (on the specified

port

) and is
available to accept incoming calls from clients.

**Parameters:** id

- activation identifier for the object
**Parameters:** port

- the port number on which the object is exported
**Throws:** RemoteException

- if exporting the object to the RMI
runtime fails
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

- Activatable

```java
protected Activatable​(
ActivationID
id,
int port,

RMIClientSocketFactory
csf,

RMIServerSocketFactory
ssf)
throws
RemoteException
```

Constructor used to activate/export the object on a specified
port. An "activatable" remote object must have a constructor that
takes two arguments:

- the object's activation identifier (

ActivationID

), and

the object's initialization data (a

MarshalledObject

).

A concrete subclass of this class must call this constructor when it is

activated

via the two parameter constructor described above. As
a side-effect of construction, the remote object is "exported"
to the RMI runtime (on the specified

port

) and is
available to accept incoming calls from clients.

**Parameters:** id

- activation identifier for the object
**Parameters:** port

- the port number on which the object is exported
**Parameters:** csf

- the client-side socket factory for making calls to the
remote object
**Parameters:** ssf

- the server-side socket factory for receiving remote calls
**Throws:** RemoteException

- if exporting the object to the RMI
runtime fails
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

============ METHOD DETAIL ==========

- Method Detail

- getID

```java
protected
ActivationID
getID()
```

Returns the object's activation identifier. The method is
protected so that only subclasses can obtain an object's
identifier.

**Returns:** the object's activation identifier
**Since:** 1.2

- register

```java
public static
Remote
register​(
ActivationDesc
desc)
throws
UnknownGroupException
,

ActivationException
,

RemoteException
```

Register an object descriptor for an activatable remote
object so that is can be activated on demand.

**Parameters:** desc

- the object's descriptor
**Returns:** the stub for the activatable remote object
**Throws:** UnknownGroupException

- if group id in

desc

is not registered with the activation system
**Throws:** ActivationException

- if activation system is not running
**Throws:** RemoteException

- if remote call fails
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

- inactive

```java
public static boolean inactive​(
ActivationID
id)
throws
UnknownObjectException
,

ActivationException
,

RemoteException
```

Informs the system that the object with the corresponding activation

id

is currently inactive. If the object is currently
active, the object is "unexported" from the RMI runtime (only if
there are no pending or in-progress calls)
so the that it can no longer receive incoming calls. This call
informs this VM's ActivationGroup that the object is inactive,
that, in turn, informs its ActivationMonitor. If this call
completes successfully, a subsequent activate request to the activator
will cause the object to reactivate. The operation may still
succeed if the object is considered active but has already
unexported itself.

**Parameters:** id

- the object's activation identifier
**Returns:** true if the operation succeeds (the operation will
succeed if the object in currently known to be active and is
either already unexported or is currently exported and has no
pending/executing calls); false is returned if the object has
pending/executing calls in which case it cannot be deactivated
**Throws:** UnknownObjectException

- if object is not known (it may
already be inactive)
**Throws:** ActivationException

- if group is not active
**Throws:** RemoteException

- if call informing monitor fails
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

- unregister

```java
public static void unregister​(
ActivationID
id)
throws
UnknownObjectException
,

ActivationException
,

RemoteException
```

Revokes previous registration for the activation descriptor
associated with

id

. An object can no longer be
activated via that

id

.

**Parameters:** id

- the object's activation identifier
**Throws:** UnknownObjectException

- if object (

id

) is unknown
**Throws:** ActivationException

- if activation system is not running
**Throws:** RemoteException

- if remote call to activation system fails
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

- exportObject

```java
public static
ActivationID
exportObject​(
Remote
obj,

String
location,

MarshalledObject
<?> data,
boolean restart,
int port)
throws
ActivationException
,

RemoteException
```

Registers an activation descriptor (with the specified location,
data, and restart mode) for the specified object, and exports that
object with the specified port.

Note:

Using this method (as well as the

Activatable

constructors that both register and export
an activatable remote object) is strongly discouraged because the
actions of registering and exporting the remote object are

not

guaranteed to be atomic. Instead, an application should
register an activation descriptor and export a remote object
separately, so that exceptions can be handled properly.

This method invokes the

exportObject

method with the specified object, location, data,
restart mode, and port, and

null

for both client and
server socket factories, and then returns the resulting activation
identifier.

**Parameters:** obj

- the object being exported
**Parameters:** location

- the object's code location
**Parameters:** data

- the object's bootstrapping data
**Parameters:** restart

- if true, the object is restarted (reactivated) when
either the activator is restarted or the object's activation group
is restarted after an unexpected crash; if false, the object is only
activated on demand. Specifying

restart

to be

true

does not force an initial immediate activation of
a newly registered object; initial activation is lazy.
**Parameters:** port

- the port on which the object is exported (an anonymous
port is used if port=0)
**Returns:** the activation identifier obtained from registering the
descriptor,

desc

, with the activation system
the wrong group
**Throws:** ActivationException

- if activation group is not active
**Throws:** RemoteException

- if object registration or export fails
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

- exportObject

```java
public static
ActivationID
exportObject​(
Remote
obj,

String
location,

MarshalledObject
<?> data,
boolean restart,
int port,

RMIClientSocketFactory
csf,

RMIServerSocketFactory
ssf)
throws
ActivationException
,

RemoteException
```

Registers an activation descriptor (with the specified location,
data, and restart mode) for the specified object, and exports that
object with the specified port, and the specified client and server
socket factories.

Note:

Using this method (as well as the

Activatable

constructors that both register and export
an activatable remote object) is strongly discouraged because the
actions of registering and exporting the remote object are

not

guaranteed to be atomic. Instead, an application should
register an activation descriptor and export a remote object
separately, so that exceptions can be handled properly.

This method first registers an activation descriptor for the
specified object as follows. It obtains the activation system by
invoking the method

ActivationGroup.getSystem

. This method then obtains an

ActivationID

for the object by invoking the activation system's

registerObject

method with
an

ActivationDesc

constructed with the specified object's
class name, and the specified location, data, and restart mode. If
an exception occurs obtaining the activation system or registering
the activation descriptor, that exception is thrown to the caller.

Next, this method exports the object by invoking the

exportObject

method with the specified remote object, the
activation identifier obtained from registration, the specified
port, and the specified client and server socket factories. If an
exception occurs exporting the object, this method attempts to
unregister the activation identifier (obtained from registration) by
invoking the activation system's

unregisterObject

method with the
activation identifier. If an exception occurs unregistering the
identifier, that exception is ignored, and the original exception
that occurred exporting the object is thrown to the caller.

Finally, this method invokes the

activeObject

method on the activation
group in this VM with the activation identifier and the specified
remote object, and returns the activation identifier to the caller.

**Parameters:** obj

- the object being exported
**Parameters:** location

- the object's code location
**Parameters:** data

- the object's bootstrapping data
**Parameters:** restart

- if true, the object is restarted (reactivated) when
either the activator is restarted or the object's activation group
is restarted after an unexpected crash; if false, the object is only
activated on demand. Specifying

restart

to be

true

does not force an initial immediate activation of
a newly registered object; initial activation is lazy.
**Parameters:** port

- the port on which the object is exported (an anonymous
port is used if port=0)
**Parameters:** csf

- the client-side socket factory for making calls to the
remote object
**Parameters:** ssf

- the server-side socket factory for receiving remote calls
**Returns:** the activation identifier obtained from registering the
descriptor with the activation system
**Throws:** ActivationException

- if activation group is not active
**Throws:** RemoteException

- if object registration or export fails
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

- exportObject

```java
public static
Remote
exportObject​(
Remote
obj,

ActivationID
id,
int port)
throws
RemoteException
```

Export the activatable remote object to the RMI runtime to make
the object available to receive incoming calls. The object is
exported on an anonymous port, if

port

is zero.

During activation, this

exportObject

method should
be invoked explicitly by an "activatable" object, that does not
extend the

Activatable

class. There is no need for objects
that do extend the

Activatable

class to invoke this
method directly because the object is exported during construction.

**Parameters:** obj

- the remote object implementation
**Parameters:** id

- the object's activation identifier
**Parameters:** port

- the port on which the object is exported (an anonymous
port is used if port=0)
**Returns:** the stub for the activatable remote object
**Throws:** RemoteException

- if object export fails
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

- exportObject

```java
public static
Remote
exportObject​(
Remote
obj,

ActivationID
id,
int port,

RMIClientSocketFactory
csf,

RMIServerSocketFactory
ssf)
throws
RemoteException
```

Export the activatable remote object to the RMI runtime to make
the object available to receive incoming calls. The object is
exported on an anonymous port, if

port

is zero.

During activation, this

exportObject

method should
be invoked explicitly by an "activatable" object, that does not
extend the

Activatable

class. There is no need for objects
that do extend the

Activatable

class to invoke this
method directly because the object is exported during construction.

**Parameters:** obj

- the remote object implementation
**Parameters:** id

- the object's activation identifier
**Parameters:** port

- the port on which the object is exported (an anonymous
port is used if port=0)
**Parameters:** csf

- the client-side socket factory for making calls to the
remote object
**Parameters:** ssf

- the server-side socket factory for receiving remote calls
**Returns:** the stub for the activatable remote object
**Throws:** RemoteException

- if object export fails
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

- unexportObject

```java
public static boolean unexportObject​(
Remote
obj,
boolean force)
throws
NoSuchObjectException
```

Remove the remote object, obj, from the RMI runtime. If
successful, the object can no longer accept incoming RMI calls.
If the force parameter is true, the object is forcibly unexported
even if there are pending calls to the remote object or the
remote object still has calls in progress. If the force
parameter is false, the object is only unexported if there are
no pending or in progress calls to the object.

**Parameters:** obj

- the remote object to be unexported
**Parameters:** force

- if true, unexports the object even if there are
pending or in-progress calls; if false, only unexports the object
if there are no pending or in-progress calls
**Returns:** true if operation is successful, false otherwise
**Throws:** NoSuchObjectException

- if the remote object is not
currently exported
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

Constructor Detail

- Activatable

```java
protected Activatable​(
String
location,

MarshalledObject
<?> data,
boolean restart,
int port)
throws
ActivationException
,

RemoteException
```

Constructs an activatable remote object by registering
an activation descriptor (with the specified location, data, and
restart mode) for this object, and exporting the object with the
specified port.

Note:

Using the

Activatable

constructors that both register and export an activatable remote
object is strongly discouraged because the actions of registering
and exporting the remote object are

not

guaranteed to be
atomic. Instead, an application should register an activation
descriptor and export a remote object separately, so that exceptions
can be handled properly.

This method invokes the

exportObject

method with this object, and the specified location,
data, restart mode, and port. Subsequent calls to

getID()

will return the activation identifier returned from the call to

exportObject

.

**Parameters:** location

- the location for classes for this object
**Parameters:** data

- the object's initialization data
**Parameters:** port

- the port on which the object is exported (an anonymous
port is used if port=0)
**Parameters:** restart

- if true, the object is restarted (reactivated) when
either the activator is restarted or the object's activation group
is restarted after an unexpected crash; if false, the object is only
activated on demand. Specifying

restart

to be

true

does not force an initial immediate activation of
a newly registered object; initial activation is lazy.
**Throws:** ActivationException

- if object registration fails.
**Throws:** RemoteException

- if either of the following fails:
a) registering the object with the activation system or b) exporting
the object to the RMI runtime.
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation.
**Since:** 1.2

- Activatable

```java
protected Activatable​(
String
location,

MarshalledObject
<?> data,
boolean restart,
int port,

RMIClientSocketFactory
csf,

RMIServerSocketFactory
ssf)
throws
ActivationException
,

RemoteException
```

Constructs an activatable remote object by registering
an activation descriptor (with the specified location, data, and
restart mode) for this object, and exporting the object with the
specified port, and specified client and server socket factories.

Note:

Using the

Activatable

constructors that both register and export an activatable remote
object is strongly discouraged because the actions of registering
and exporting the remote object are

not

guaranteed to be
atomic. Instead, an application should register an activation
descriptor and export a remote object separately, so that exceptions
can be handled properly.

This method invokes the

exportObject

method with this object, and the specified location,
data, restart mode, port, and client and server socket factories.
Subsequent calls to

getID()

will return the activation
identifier returned from the call to

exportObject

.

**Parameters:** location

- the location for classes for this object
**Parameters:** data

- the object's initialization data
**Parameters:** restart

- if true, the object is restarted (reactivated) when
either the activator is restarted or the object's activation group
is restarted after an unexpected crash; if false, the object is only
activated on demand. Specifying

restart

to be

true

does not force an initial immediate activation of
a newly registered object; initial activation is lazy.
**Parameters:** port

- the port on which the object is exported (an anonymous
port is used if port=0)
**Parameters:** csf

- the client-side socket factory for making calls to the
remote object
**Parameters:** ssf

- the server-side socket factory for receiving remote calls
**Throws:** ActivationException

- if object registration fails.
**Throws:** RemoteException

- if either of the following fails:
a) registering the object with the activation system or b) exporting
the object to the RMI runtime.
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation.
**Since:** 1.2

- Activatable

```java
protected Activatable​(
ActivationID
id,
int port)
throws
RemoteException
```

Constructor used to activate/export the object on a specified
port. An "activatable" remote object must have a constructor that
takes two arguments:

- the object's activation identifier (

ActivationID

), and

the object's initialization data (a

MarshalledObject

).

A concrete subclass of this class must call this constructor when it is

activated

via the two parameter constructor described above. As
a side-effect of construction, the remote object is "exported"
to the RMI runtime (on the specified

port

) and is
available to accept incoming calls from clients.

**Parameters:** id

- activation identifier for the object
**Parameters:** port

- the port number on which the object is exported
**Throws:** RemoteException

- if exporting the object to the RMI
runtime fails
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

- Activatable

```java
protected Activatable​(
ActivationID
id,
int port,

RMIClientSocketFactory
csf,

RMIServerSocketFactory
ssf)
throws
RemoteException
```

Constructor used to activate/export the object on a specified
port. An "activatable" remote object must have a constructor that
takes two arguments:

- the object's activation identifier (

ActivationID

), and

the object's initialization data (a

MarshalledObject

).

A concrete subclass of this class must call this constructor when it is

activated

via the two parameter constructor described above. As
a side-effect of construction, the remote object is "exported"
to the RMI runtime (on the specified

port

) and is
available to accept incoming calls from clients.

**Parameters:** id

- activation identifier for the object
**Parameters:** port

- the port number on which the object is exported
**Parameters:** csf

- the client-side socket factory for making calls to the
remote object
**Parameters:** ssf

- the server-side socket factory for receiving remote calls
**Throws:** RemoteException

- if exporting the object to the RMI
runtime fails
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

---

#### Constructor Detail

Activatable

```java
protected Activatable​(
String
location,

MarshalledObject
<?> data,
boolean restart,
int port)
throws
ActivationException
,

RemoteException
```

Constructs an activatable remote object by registering
an activation descriptor (with the specified location, data, and
restart mode) for this object, and exporting the object with the
specified port.

Note:

Using the

Activatable

constructors that both register and export an activatable remote
object is strongly discouraged because the actions of registering
and exporting the remote object are

not

guaranteed to be
atomic. Instead, an application should register an activation
descriptor and export a remote object separately, so that exceptions
can be handled properly.

This method invokes the

exportObject

method with this object, and the specified location,
data, restart mode, and port. Subsequent calls to

getID()

will return the activation identifier returned from the call to

exportObject

.

**Parameters:** location

- the location for classes for this object
**Parameters:** data

- the object's initialization data
**Parameters:** port

- the port on which the object is exported (an anonymous
port is used if port=0)
**Parameters:** restart

- if true, the object is restarted (reactivated) when
either the activator is restarted or the object's activation group
is restarted after an unexpected crash; if false, the object is only
activated on demand. Specifying

restart

to be

true

does not force an initial immediate activation of
a newly registered object; initial activation is lazy.
**Throws:** ActivationException

- if object registration fails.
**Throws:** RemoteException

- if either of the following fails:
a) registering the object with the activation system or b) exporting
the object to the RMI runtime.
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation.
**Since:** 1.2

---

#### Activatable

protected Activatable​(

String

location,

MarshalledObject

<?> data,
boolean restart,
int port)
throws

ActivationException

,

RemoteException

Constructs an activatable remote object by registering
an activation descriptor (with the specified location, data, and
restart mode) for this object, and exporting the object with the
specified port.

Note:

Using the

Activatable

constructors that both register and export an activatable remote
object is strongly discouraged because the actions of registering
and exporting the remote object are

not

guaranteed to be
atomic. Instead, an application should register an activation
descriptor and export a remote object separately, so that exceptions
can be handled properly.

This method invokes the

exportObject

method with this object, and the specified location,
data, restart mode, and port. Subsequent calls to

getID()

will return the activation identifier returned from the call to

exportObject

.

Note:

Using the

Activatable

constructors that both register and export an activatable remote
object is strongly discouraged because the actions of registering
and exporting the remote object are

not

guaranteed to be
atomic. Instead, an application should register an activation
descriptor and export a remote object separately, so that exceptions
can be handled properly.

This method invokes the

exportObject

method with this object, and the specified location,
data, restart mode, and port. Subsequent calls to

getID()

will return the activation identifier returned from the call to

exportObject

.

This method invokes the

exportObject

method with this object, and the specified location,
data, restart mode, and port. Subsequent calls to

getID()

will return the activation identifier returned from the call to

exportObject

.

Activatable

```java
protected Activatable​(
String
location,

MarshalledObject
<?> data,
boolean restart,
int port,

RMIClientSocketFactory
csf,

RMIServerSocketFactory
ssf)
throws
ActivationException
,

RemoteException
```

Constructs an activatable remote object by registering
an activation descriptor (with the specified location, data, and
restart mode) for this object, and exporting the object with the
specified port, and specified client and server socket factories.

Note:

Using the

Activatable

constructors that both register and export an activatable remote
object is strongly discouraged because the actions of registering
and exporting the remote object are

not

guaranteed to be
atomic. Instead, an application should register an activation
descriptor and export a remote object separately, so that exceptions
can be handled properly.

This method invokes the

exportObject

method with this object, and the specified location,
data, restart mode, port, and client and server socket factories.
Subsequent calls to

getID()

will return the activation
identifier returned from the call to

exportObject

.

**Parameters:** location

- the location for classes for this object
**Parameters:** data

- the object's initialization data
**Parameters:** restart

- if true, the object is restarted (reactivated) when
either the activator is restarted or the object's activation group
is restarted after an unexpected crash; if false, the object is only
activated on demand. Specifying

restart

to be

true

does not force an initial immediate activation of
a newly registered object; initial activation is lazy.
**Parameters:** port

- the port on which the object is exported (an anonymous
port is used if port=0)
**Parameters:** csf

- the client-side socket factory for making calls to the
remote object
**Parameters:** ssf

- the server-side socket factory for receiving remote calls
**Throws:** ActivationException

- if object registration fails.
**Throws:** RemoteException

- if either of the following fails:
a) registering the object with the activation system or b) exporting
the object to the RMI runtime.
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation.
**Since:** 1.2

---

#### Activatable

protected Activatable​(

String

location,

MarshalledObject

<?> data,
boolean restart,
int port,

RMIClientSocketFactory

csf,

RMIServerSocketFactory

ssf)
throws

ActivationException

,

RemoteException

Constructs an activatable remote object by registering
an activation descriptor (with the specified location, data, and
restart mode) for this object, and exporting the object with the
specified port, and specified client and server socket factories.

Note:

Using the

Activatable

constructors that both register and export an activatable remote
object is strongly discouraged because the actions of registering
and exporting the remote object are

not

guaranteed to be
atomic. Instead, an application should register an activation
descriptor and export a remote object separately, so that exceptions
can be handled properly.

This method invokes the

exportObject

method with this object, and the specified location,
data, restart mode, port, and client and server socket factories.
Subsequent calls to

getID()

will return the activation
identifier returned from the call to

exportObject

.

Note:

Using the

Activatable

constructors that both register and export an activatable remote
object is strongly discouraged because the actions of registering
and exporting the remote object are

not

guaranteed to be
atomic. Instead, an application should register an activation
descriptor and export a remote object separately, so that exceptions
can be handled properly.

This method invokes the

exportObject

method with this object, and the specified location,
data, restart mode, port, and client and server socket factories.
Subsequent calls to

getID()

will return the activation
identifier returned from the call to

exportObject

.

This method invokes the

exportObject

method with this object, and the specified location,
data, restart mode, port, and client and server socket factories.
Subsequent calls to

getID()

will return the activation
identifier returned from the call to

exportObject

.

Activatable

```java
protected Activatable​(
ActivationID
id,
int port)
throws
RemoteException
```

Constructor used to activate/export the object on a specified
port. An "activatable" remote object must have a constructor that
takes two arguments:

- the object's activation identifier (

ActivationID

), and

the object's initialization data (a

MarshalledObject

).

A concrete subclass of this class must call this constructor when it is

activated

via the two parameter constructor described above. As
a side-effect of construction, the remote object is "exported"
to the RMI runtime (on the specified

port

) and is
available to accept incoming calls from clients.

**Parameters:** id

- activation identifier for the object
**Parameters:** port

- the port number on which the object is exported
**Throws:** RemoteException

- if exporting the object to the RMI
runtime fails
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

---

#### Activatable

protected Activatable​(

ActivationID

id,
int port)
throws

RemoteException

Constructor used to activate/export the object on a specified
port. An "activatable" remote object must have a constructor that
takes two arguments:

- the object's activation identifier (

ActivationID

), and

the object's initialization data (a

MarshalledObject

).

A concrete subclass of this class must call this constructor when it is

activated

via the two parameter constructor described above. As
a side-effect of construction, the remote object is "exported"
to the RMI runtime (on the specified

port

) and is
available to accept incoming calls from clients.

the object's activation identifier (

ActivationID

), and

the object's initialization data (a

MarshalledObject

).

A concrete subclass of this class must call this constructor when it is

activated

via the two parameter constructor described above. As
a side-effect of construction, the remote object is "exported"
to the RMI runtime (on the specified

port

) and is
available to accept incoming calls from clients.

Activatable

```java
protected Activatable​(
ActivationID
id,
int port,

RMIClientSocketFactory
csf,

RMIServerSocketFactory
ssf)
throws
RemoteException
```

Constructor used to activate/export the object on a specified
port. An "activatable" remote object must have a constructor that
takes two arguments:

- the object's activation identifier (

ActivationID

), and

the object's initialization data (a

MarshalledObject

).

A concrete subclass of this class must call this constructor when it is

activated

via the two parameter constructor described above. As
a side-effect of construction, the remote object is "exported"
to the RMI runtime (on the specified

port

) and is
available to accept incoming calls from clients.

**Parameters:** id

- activation identifier for the object
**Parameters:** port

- the port number on which the object is exported
**Parameters:** csf

- the client-side socket factory for making calls to the
remote object
**Parameters:** ssf

- the server-side socket factory for receiving remote calls
**Throws:** RemoteException

- if exporting the object to the RMI
runtime fails
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

---

#### Activatable

protected Activatable​(

ActivationID

id,
int port,

RMIClientSocketFactory

csf,

RMIServerSocketFactory

ssf)
throws

RemoteException

Constructor used to activate/export the object on a specified
port. An "activatable" remote object must have a constructor that
takes two arguments:

- the object's activation identifier (

ActivationID

), and

the object's initialization data (a

MarshalledObject

).

A concrete subclass of this class must call this constructor when it is

activated

via the two parameter constructor described above. As
a side-effect of construction, the remote object is "exported"
to the RMI runtime (on the specified

port

) and is
available to accept incoming calls from clients.

the object's activation identifier (

ActivationID

), and

the object's initialization data (a

MarshalledObject

).

A concrete subclass of this class must call this constructor when it is

activated

via the two parameter constructor described above. As
a side-effect of construction, the remote object is "exported"
to the RMI runtime (on the specified

port

) and is
available to accept incoming calls from clients.

Method Detail

- getID

```java
protected
ActivationID
getID()
```

Returns the object's activation identifier. The method is
protected so that only subclasses can obtain an object's
identifier.

**Returns:** the object's activation identifier
**Since:** 1.2

- register

```java
public static
Remote
register​(
ActivationDesc
desc)
throws
UnknownGroupException
,

ActivationException
,

RemoteException
```

Register an object descriptor for an activatable remote
object so that is can be activated on demand.

**Parameters:** desc

- the object's descriptor
**Returns:** the stub for the activatable remote object
**Throws:** UnknownGroupException

- if group id in

desc

is not registered with the activation system
**Throws:** ActivationException

- if activation system is not running
**Throws:** RemoteException

- if remote call fails
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

- inactive

```java
public static boolean inactive​(
ActivationID
id)
throws
UnknownObjectException
,

ActivationException
,

RemoteException
```

Informs the system that the object with the corresponding activation

id

is currently inactive. If the object is currently
active, the object is "unexported" from the RMI runtime (only if
there are no pending or in-progress calls)
so the that it can no longer receive incoming calls. This call
informs this VM's ActivationGroup that the object is inactive,
that, in turn, informs its ActivationMonitor. If this call
completes successfully, a subsequent activate request to the activator
will cause the object to reactivate. The operation may still
succeed if the object is considered active but has already
unexported itself.

**Parameters:** id

- the object's activation identifier
**Returns:** true if the operation succeeds (the operation will
succeed if the object in currently known to be active and is
either already unexported or is currently exported and has no
pending/executing calls); false is returned if the object has
pending/executing calls in which case it cannot be deactivated
**Throws:** UnknownObjectException

- if object is not known (it may
already be inactive)
**Throws:** ActivationException

- if group is not active
**Throws:** RemoteException

- if call informing monitor fails
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

- unregister

```java
public static void unregister​(
ActivationID
id)
throws
UnknownObjectException
,

ActivationException
,

RemoteException
```

Revokes previous registration for the activation descriptor
associated with

id

. An object can no longer be
activated via that

id

.

**Parameters:** id

- the object's activation identifier
**Throws:** UnknownObjectException

- if object (

id

) is unknown
**Throws:** ActivationException

- if activation system is not running
**Throws:** RemoteException

- if remote call to activation system fails
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

- exportObject

```java
public static
ActivationID
exportObject​(
Remote
obj,

String
location,

MarshalledObject
<?> data,
boolean restart,
int port)
throws
ActivationException
,

RemoteException
```

Registers an activation descriptor (with the specified location,
data, and restart mode) for the specified object, and exports that
object with the specified port.

Note:

Using this method (as well as the

Activatable

constructors that both register and export
an activatable remote object) is strongly discouraged because the
actions of registering and exporting the remote object are

not

guaranteed to be atomic. Instead, an application should
register an activation descriptor and export a remote object
separately, so that exceptions can be handled properly.

This method invokes the

exportObject

method with the specified object, location, data,
restart mode, and port, and

null

for both client and
server socket factories, and then returns the resulting activation
identifier.

**Parameters:** obj

- the object being exported
**Parameters:** location

- the object's code location
**Parameters:** data

- the object's bootstrapping data
**Parameters:** restart

- if true, the object is restarted (reactivated) when
either the activator is restarted or the object's activation group
is restarted after an unexpected crash; if false, the object is only
activated on demand. Specifying

restart

to be

true

does not force an initial immediate activation of
a newly registered object; initial activation is lazy.
**Parameters:** port

- the port on which the object is exported (an anonymous
port is used if port=0)
**Returns:** the activation identifier obtained from registering the
descriptor,

desc

, with the activation system
the wrong group
**Throws:** ActivationException

- if activation group is not active
**Throws:** RemoteException

- if object registration or export fails
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

- exportObject

```java
public static
ActivationID
exportObject​(
Remote
obj,

String
location,

MarshalledObject
<?> data,
boolean restart,
int port,

RMIClientSocketFactory
csf,

RMIServerSocketFactory
ssf)
throws
ActivationException
,

RemoteException
```

Registers an activation descriptor (with the specified location,
data, and restart mode) for the specified object, and exports that
object with the specified port, and the specified client and server
socket factories.

Note:

Using this method (as well as the

Activatable

constructors that both register and export
an activatable remote object) is strongly discouraged because the
actions of registering and exporting the remote object are

not

guaranteed to be atomic. Instead, an application should
register an activation descriptor and export a remote object
separately, so that exceptions can be handled properly.

This method first registers an activation descriptor for the
specified object as follows. It obtains the activation system by
invoking the method

ActivationGroup.getSystem

. This method then obtains an

ActivationID

for the object by invoking the activation system's

registerObject

method with
an

ActivationDesc

constructed with the specified object's
class name, and the specified location, data, and restart mode. If
an exception occurs obtaining the activation system or registering
the activation descriptor, that exception is thrown to the caller.

Next, this method exports the object by invoking the

exportObject

method with the specified remote object, the
activation identifier obtained from registration, the specified
port, and the specified client and server socket factories. If an
exception occurs exporting the object, this method attempts to
unregister the activation identifier (obtained from registration) by
invoking the activation system's

unregisterObject

method with the
activation identifier. If an exception occurs unregistering the
identifier, that exception is ignored, and the original exception
that occurred exporting the object is thrown to the caller.

Finally, this method invokes the

activeObject

method on the activation
group in this VM with the activation identifier and the specified
remote object, and returns the activation identifier to the caller.

**Parameters:** obj

- the object being exported
**Parameters:** location

- the object's code location
**Parameters:** data

- the object's bootstrapping data
**Parameters:** restart

- if true, the object is restarted (reactivated) when
either the activator is restarted or the object's activation group
is restarted after an unexpected crash; if false, the object is only
activated on demand. Specifying

restart

to be

true

does not force an initial immediate activation of
a newly registered object; initial activation is lazy.
**Parameters:** port

- the port on which the object is exported (an anonymous
port is used if port=0)
**Parameters:** csf

- the client-side socket factory for making calls to the
remote object
**Parameters:** ssf

- the server-side socket factory for receiving remote calls
**Returns:** the activation identifier obtained from registering the
descriptor with the activation system
**Throws:** ActivationException

- if activation group is not active
**Throws:** RemoteException

- if object registration or export fails
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

- exportObject

```java
public static
Remote
exportObject​(
Remote
obj,

ActivationID
id,
int port)
throws
RemoteException
```

Export the activatable remote object to the RMI runtime to make
the object available to receive incoming calls. The object is
exported on an anonymous port, if

port

is zero.

During activation, this

exportObject

method should
be invoked explicitly by an "activatable" object, that does not
extend the

Activatable

class. There is no need for objects
that do extend the

Activatable

class to invoke this
method directly because the object is exported during construction.

**Parameters:** obj

- the remote object implementation
**Parameters:** id

- the object's activation identifier
**Parameters:** port

- the port on which the object is exported (an anonymous
port is used if port=0)
**Returns:** the stub for the activatable remote object
**Throws:** RemoteException

- if object export fails
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

- exportObject

```java
public static
Remote
exportObject​(
Remote
obj,

ActivationID
id,
int port,

RMIClientSocketFactory
csf,

RMIServerSocketFactory
ssf)
throws
RemoteException
```

Export the activatable remote object to the RMI runtime to make
the object available to receive incoming calls. The object is
exported on an anonymous port, if

port

is zero.

During activation, this

exportObject

method should
be invoked explicitly by an "activatable" object, that does not
extend the

Activatable

class. There is no need for objects
that do extend the

Activatable

class to invoke this
method directly because the object is exported during construction.

**Parameters:** obj

- the remote object implementation
**Parameters:** id

- the object's activation identifier
**Parameters:** port

- the port on which the object is exported (an anonymous
port is used if port=0)
**Parameters:** csf

- the client-side socket factory for making calls to the
remote object
**Parameters:** ssf

- the server-side socket factory for receiving remote calls
**Returns:** the stub for the activatable remote object
**Throws:** RemoteException

- if object export fails
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

- unexportObject

```java
public static boolean unexportObject​(
Remote
obj,
boolean force)
throws
NoSuchObjectException
```

Remove the remote object, obj, from the RMI runtime. If
successful, the object can no longer accept incoming RMI calls.
If the force parameter is true, the object is forcibly unexported
even if there are pending calls to the remote object or the
remote object still has calls in progress. If the force
parameter is false, the object is only unexported if there are
no pending or in progress calls to the object.

**Parameters:** obj

- the remote object to be unexported
**Parameters:** force

- if true, unexports the object even if there are
pending or in-progress calls; if false, only unexports the object
if there are no pending or in-progress calls
**Returns:** true if operation is successful, false otherwise
**Throws:** NoSuchObjectException

- if the remote object is not
currently exported
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

---

#### Method Detail

getID

```java
protected
ActivationID
getID()
```

Returns the object's activation identifier. The method is
protected so that only subclasses can obtain an object's
identifier.

**Returns:** the object's activation identifier
**Since:** 1.2

---

#### getID

protected

ActivationID

getID()

Returns the object's activation identifier. The method is
protected so that only subclasses can obtain an object's
identifier.

register

```java
public static
Remote
register​(
ActivationDesc
desc)
throws
UnknownGroupException
,

ActivationException
,

RemoteException
```

Register an object descriptor for an activatable remote
object so that is can be activated on demand.

**Parameters:** desc

- the object's descriptor
**Returns:** the stub for the activatable remote object
**Throws:** UnknownGroupException

- if group id in

desc

is not registered with the activation system
**Throws:** ActivationException

- if activation system is not running
**Throws:** RemoteException

- if remote call fails
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

---

#### register

public static

Remote

register​(

ActivationDesc

desc)
throws

UnknownGroupException

,

ActivationException

,

RemoteException

Register an object descriptor for an activatable remote
object so that is can be activated on demand.

inactive

```java
public static boolean inactive​(
ActivationID
id)
throws
UnknownObjectException
,

ActivationException
,

RemoteException
```

Informs the system that the object with the corresponding activation

id

is currently inactive. If the object is currently
active, the object is "unexported" from the RMI runtime (only if
there are no pending or in-progress calls)
so the that it can no longer receive incoming calls. This call
informs this VM's ActivationGroup that the object is inactive,
that, in turn, informs its ActivationMonitor. If this call
completes successfully, a subsequent activate request to the activator
will cause the object to reactivate. The operation may still
succeed if the object is considered active but has already
unexported itself.

**Parameters:** id

- the object's activation identifier
**Returns:** true if the operation succeeds (the operation will
succeed if the object in currently known to be active and is
either already unexported or is currently exported and has no
pending/executing calls); false is returned if the object has
pending/executing calls in which case it cannot be deactivated
**Throws:** UnknownObjectException

- if object is not known (it may
already be inactive)
**Throws:** ActivationException

- if group is not active
**Throws:** RemoteException

- if call informing monitor fails
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

---

#### inactive

public static boolean inactive​(

ActivationID

id)
throws

UnknownObjectException

,

ActivationException

,

RemoteException

Informs the system that the object with the corresponding activation

id

is currently inactive. If the object is currently
active, the object is "unexported" from the RMI runtime (only if
there are no pending or in-progress calls)
so the that it can no longer receive incoming calls. This call
informs this VM's ActivationGroup that the object is inactive,
that, in turn, informs its ActivationMonitor. If this call
completes successfully, a subsequent activate request to the activator
will cause the object to reactivate. The operation may still
succeed if the object is considered active but has already
unexported itself.

unregister

```java
public static void unregister​(
ActivationID
id)
throws
UnknownObjectException
,

ActivationException
,

RemoteException
```

Revokes previous registration for the activation descriptor
associated with

id

. An object can no longer be
activated via that

id

.

**Parameters:** id

- the object's activation identifier
**Throws:** UnknownObjectException

- if object (

id

) is unknown
**Throws:** ActivationException

- if activation system is not running
**Throws:** RemoteException

- if remote call to activation system fails
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

---

#### unregister

public static void unregister​(

ActivationID

id)
throws

UnknownObjectException

,

ActivationException

,

RemoteException

Revokes previous registration for the activation descriptor
associated with

id

. An object can no longer be
activated via that

id

.

exportObject

```java
public static
ActivationID
exportObject​(
Remote
obj,

String
location,

MarshalledObject
<?> data,
boolean restart,
int port)
throws
ActivationException
,

RemoteException
```

Registers an activation descriptor (with the specified location,
data, and restart mode) for the specified object, and exports that
object with the specified port.

Note:

Using this method (as well as the

Activatable

constructors that both register and export
an activatable remote object) is strongly discouraged because the
actions of registering and exporting the remote object are

not

guaranteed to be atomic. Instead, an application should
register an activation descriptor and export a remote object
separately, so that exceptions can be handled properly.

This method invokes the

exportObject

method with the specified object, location, data,
restart mode, and port, and

null

for both client and
server socket factories, and then returns the resulting activation
identifier.

**Parameters:** obj

- the object being exported
**Parameters:** location

- the object's code location
**Parameters:** data

- the object's bootstrapping data
**Parameters:** restart

- if true, the object is restarted (reactivated) when
either the activator is restarted or the object's activation group
is restarted after an unexpected crash; if false, the object is only
activated on demand. Specifying

restart

to be

true

does not force an initial immediate activation of
a newly registered object; initial activation is lazy.
**Parameters:** port

- the port on which the object is exported (an anonymous
port is used if port=0)
**Returns:** the activation identifier obtained from registering the
descriptor,

desc

, with the activation system
the wrong group
**Throws:** ActivationException

- if activation group is not active
**Throws:** RemoteException

- if object registration or export fails
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

---

#### exportObject

public static

ActivationID

exportObject​(

Remote

obj,

String

location,

MarshalledObject

<?> data,
boolean restart,
int port)
throws

ActivationException

,

RemoteException

Registers an activation descriptor (with the specified location,
data, and restart mode) for the specified object, and exports that
object with the specified port.

Note:

Using this method (as well as the

Activatable

constructors that both register and export
an activatable remote object) is strongly discouraged because the
actions of registering and exporting the remote object are

not

guaranteed to be atomic. Instead, an application should
register an activation descriptor and export a remote object
separately, so that exceptions can be handled properly.

This method invokes the

exportObject

method with the specified object, location, data,
restart mode, and port, and

null

for both client and
server socket factories, and then returns the resulting activation
identifier.

Note:

Using this method (as well as the

Activatable

constructors that both register and export
an activatable remote object) is strongly discouraged because the
actions of registering and exporting the remote object are

not

guaranteed to be atomic. Instead, an application should
register an activation descriptor and export a remote object
separately, so that exceptions can be handled properly.

This method invokes the

exportObject

method with the specified object, location, data,
restart mode, and port, and

null

for both client and
server socket factories, and then returns the resulting activation
identifier.

This method invokes the

exportObject

method with the specified object, location, data,
restart mode, and port, and

null

for both client and
server socket factories, and then returns the resulting activation
identifier.

exportObject

```java
public static
ActivationID
exportObject​(
Remote
obj,

String
location,

MarshalledObject
<?> data,
boolean restart,
int port,

RMIClientSocketFactory
csf,

RMIServerSocketFactory
ssf)
throws
ActivationException
,

RemoteException
```

Registers an activation descriptor (with the specified location,
data, and restart mode) for the specified object, and exports that
object with the specified port, and the specified client and server
socket factories.

Note:

Using this method (as well as the

Activatable

constructors that both register and export
an activatable remote object) is strongly discouraged because the
actions of registering and exporting the remote object are

not

guaranteed to be atomic. Instead, an application should
register an activation descriptor and export a remote object
separately, so that exceptions can be handled properly.

This method first registers an activation descriptor for the
specified object as follows. It obtains the activation system by
invoking the method

ActivationGroup.getSystem

. This method then obtains an

ActivationID

for the object by invoking the activation system's

registerObject

method with
an

ActivationDesc

constructed with the specified object's
class name, and the specified location, data, and restart mode. If
an exception occurs obtaining the activation system or registering
the activation descriptor, that exception is thrown to the caller.

Next, this method exports the object by invoking the

exportObject

method with the specified remote object, the
activation identifier obtained from registration, the specified
port, and the specified client and server socket factories. If an
exception occurs exporting the object, this method attempts to
unregister the activation identifier (obtained from registration) by
invoking the activation system's

unregisterObject

method with the
activation identifier. If an exception occurs unregistering the
identifier, that exception is ignored, and the original exception
that occurred exporting the object is thrown to the caller.

Finally, this method invokes the

activeObject

method on the activation
group in this VM with the activation identifier and the specified
remote object, and returns the activation identifier to the caller.

**Parameters:** obj

- the object being exported
**Parameters:** location

- the object's code location
**Parameters:** data

- the object's bootstrapping data
**Parameters:** restart

- if true, the object is restarted (reactivated) when
either the activator is restarted or the object's activation group
is restarted after an unexpected crash; if false, the object is only
activated on demand. Specifying

restart

to be

true

does not force an initial immediate activation of
a newly registered object; initial activation is lazy.
**Parameters:** port

- the port on which the object is exported (an anonymous
port is used if port=0)
**Parameters:** csf

- the client-side socket factory for making calls to the
remote object
**Parameters:** ssf

- the server-side socket factory for receiving remote calls
**Returns:** the activation identifier obtained from registering the
descriptor with the activation system
**Throws:** ActivationException

- if activation group is not active
**Throws:** RemoteException

- if object registration or export fails
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

---

#### exportObject

public static

ActivationID

exportObject​(

Remote

obj,

String

location,

MarshalledObject

<?> data,
boolean restart,
int port,

RMIClientSocketFactory

csf,

RMIServerSocketFactory

ssf)
throws

ActivationException

,

RemoteException

Registers an activation descriptor (with the specified location,
data, and restart mode) for the specified object, and exports that
object with the specified port, and the specified client and server
socket factories.

Note:

Using this method (as well as the

Activatable

constructors that both register and export
an activatable remote object) is strongly discouraged because the
actions of registering and exporting the remote object are

not

guaranteed to be atomic. Instead, an application should
register an activation descriptor and export a remote object
separately, so that exceptions can be handled properly.

This method first registers an activation descriptor for the
specified object as follows. It obtains the activation system by
invoking the method

ActivationGroup.getSystem

. This method then obtains an

ActivationID

for the object by invoking the activation system's

registerObject

method with
an

ActivationDesc

constructed with the specified object's
class name, and the specified location, data, and restart mode. If
an exception occurs obtaining the activation system or registering
the activation descriptor, that exception is thrown to the caller.

Next, this method exports the object by invoking the

exportObject

method with the specified remote object, the
activation identifier obtained from registration, the specified
port, and the specified client and server socket factories. If an
exception occurs exporting the object, this method attempts to
unregister the activation identifier (obtained from registration) by
invoking the activation system's

unregisterObject

method with the
activation identifier. If an exception occurs unregistering the
identifier, that exception is ignored, and the original exception
that occurred exporting the object is thrown to the caller.

Finally, this method invokes the

activeObject

method on the activation
group in this VM with the activation identifier and the specified
remote object, and returns the activation identifier to the caller.

Note:

Using this method (as well as the

Activatable

constructors that both register and export
an activatable remote object) is strongly discouraged because the
actions of registering and exporting the remote object are

not

guaranteed to be atomic. Instead, an application should
register an activation descriptor and export a remote object
separately, so that exceptions can be handled properly.

This method first registers an activation descriptor for the
specified object as follows. It obtains the activation system by
invoking the method

ActivationGroup.getSystem

. This method then obtains an

ActivationID

for the object by invoking the activation system's

registerObject

method with
an

ActivationDesc

constructed with the specified object's
class name, and the specified location, data, and restart mode. If
an exception occurs obtaining the activation system or registering
the activation descriptor, that exception is thrown to the caller.

Next, this method exports the object by invoking the

exportObject

method with the specified remote object, the
activation identifier obtained from registration, the specified
port, and the specified client and server socket factories. If an
exception occurs exporting the object, this method attempts to
unregister the activation identifier (obtained from registration) by
invoking the activation system's

unregisterObject

method with the
activation identifier. If an exception occurs unregistering the
identifier, that exception is ignored, and the original exception
that occurred exporting the object is thrown to the caller.

Finally, this method invokes the

activeObject

method on the activation
group in this VM with the activation identifier and the specified
remote object, and returns the activation identifier to the caller.

This method first registers an activation descriptor for the
specified object as follows. It obtains the activation system by
invoking the method

ActivationGroup.getSystem

. This method then obtains an

ActivationID

for the object by invoking the activation system's

registerObject

method with
an

ActivationDesc

constructed with the specified object's
class name, and the specified location, data, and restart mode. If
an exception occurs obtaining the activation system or registering
the activation descriptor, that exception is thrown to the caller.

Next, this method exports the object by invoking the

exportObject

method with the specified remote object, the
activation identifier obtained from registration, the specified
port, and the specified client and server socket factories. If an
exception occurs exporting the object, this method attempts to
unregister the activation identifier (obtained from registration) by
invoking the activation system's

unregisterObject

method with the
activation identifier. If an exception occurs unregistering the
identifier, that exception is ignored, and the original exception
that occurred exporting the object is thrown to the caller.

Finally, this method invokes the

activeObject

method on the activation
group in this VM with the activation identifier and the specified
remote object, and returns the activation identifier to the caller.

Next, this method exports the object by invoking the

exportObject

method with the specified remote object, the
activation identifier obtained from registration, the specified
port, and the specified client and server socket factories. If an
exception occurs exporting the object, this method attempts to
unregister the activation identifier (obtained from registration) by
invoking the activation system's

unregisterObject

method with the
activation identifier. If an exception occurs unregistering the
identifier, that exception is ignored, and the original exception
that occurred exporting the object is thrown to the caller.

Finally, this method invokes the

activeObject

method on the activation
group in this VM with the activation identifier and the specified
remote object, and returns the activation identifier to the caller.

Finally, this method invokes the

activeObject

method on the activation
group in this VM with the activation identifier and the specified
remote object, and returns the activation identifier to the caller.

exportObject

```java
public static
Remote
exportObject​(
Remote
obj,

ActivationID
id,
int port)
throws
RemoteException
```

Export the activatable remote object to the RMI runtime to make
the object available to receive incoming calls. The object is
exported on an anonymous port, if

port

is zero.

During activation, this

exportObject

method should
be invoked explicitly by an "activatable" object, that does not
extend the

Activatable

class. There is no need for objects
that do extend the

Activatable

class to invoke this
method directly because the object is exported during construction.

**Parameters:** obj

- the remote object implementation
**Parameters:** id

- the object's activation identifier
**Parameters:** port

- the port on which the object is exported (an anonymous
port is used if port=0)
**Returns:** the stub for the activatable remote object
**Throws:** RemoteException

- if object export fails
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

---

#### exportObject

public static

Remote

exportObject​(

Remote

obj,

ActivationID

id,
int port)
throws

RemoteException

Export the activatable remote object to the RMI runtime to make
the object available to receive incoming calls. The object is
exported on an anonymous port, if

port

is zero.

During activation, this

exportObject

method should
be invoked explicitly by an "activatable" object, that does not
extend the

Activatable

class. There is no need for objects
that do extend the

Activatable

class to invoke this
method directly because the object is exported during construction.

During activation, this

exportObject

method should
be invoked explicitly by an "activatable" object, that does not
extend the

Activatable

class. There is no need for objects
that do extend the

Activatable

class to invoke this
method directly because the object is exported during construction.

exportObject

```java
public static
Remote
exportObject​(
Remote
obj,

ActivationID
id,
int port,

RMIClientSocketFactory
csf,

RMIServerSocketFactory
ssf)
throws
RemoteException
```

Export the activatable remote object to the RMI runtime to make
the object available to receive incoming calls. The object is
exported on an anonymous port, if

port

is zero.

During activation, this

exportObject

method should
be invoked explicitly by an "activatable" object, that does not
extend the

Activatable

class. There is no need for objects
that do extend the

Activatable

class to invoke this
method directly because the object is exported during construction.

**Parameters:** obj

- the remote object implementation
**Parameters:** id

- the object's activation identifier
**Parameters:** port

- the port on which the object is exported (an anonymous
port is used if port=0)
**Parameters:** csf

- the client-side socket factory for making calls to the
remote object
**Parameters:** ssf

- the server-side socket factory for receiving remote calls
**Returns:** the stub for the activatable remote object
**Throws:** RemoteException

- if object export fails
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

---

#### exportObject

public static

Remote

exportObject​(

Remote

obj,

ActivationID

id,
int port,

RMIClientSocketFactory

csf,

RMIServerSocketFactory

ssf)
throws

RemoteException

Export the activatable remote object to the RMI runtime to make
the object available to receive incoming calls. The object is
exported on an anonymous port, if

port

is zero.

During activation, this

exportObject

method should
be invoked explicitly by an "activatable" object, that does not
extend the

Activatable

class. There is no need for objects
that do extend the

Activatable

class to invoke this
method directly because the object is exported during construction.

During activation, this

exportObject

method should
be invoked explicitly by an "activatable" object, that does not
extend the

Activatable

class. There is no need for objects
that do extend the

Activatable

class to invoke this
method directly because the object is exported during construction.

unexportObject

```java
public static boolean unexportObject​(
Remote
obj,
boolean force)
throws
NoSuchObjectException
```

Remove the remote object, obj, from the RMI runtime. If
successful, the object can no longer accept incoming RMI calls.
If the force parameter is true, the object is forcibly unexported
even if there are pending calls to the remote object or the
remote object still has calls in progress. If the force
parameter is false, the object is only unexported if there are
no pending or in progress calls to the object.

**Parameters:** obj

- the remote object to be unexported
**Parameters:** force

- if true, unexports the object even if there are
pending or in-progress calls; if false, only unexports the object
if there are no pending or in-progress calls
**Returns:** true if operation is successful, false otherwise
**Throws:** NoSuchObjectException

- if the remote object is not
currently exported
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

---

#### unexportObject

public static boolean unexportObject​(

Remote

obj,
boolean force)
throws

NoSuchObjectException

Remove the remote object, obj, from the RMI runtime. If
successful, the object can no longer accept incoming RMI calls.
If the force parameter is true, the object is forcibly unexported
even if there are pending calls to the remote object or the
remote object still has calls in progress. If the force
parameter is false, the object is only unexported if there are
no pending or in progress calls to the object.

---

