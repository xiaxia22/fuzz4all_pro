# Class ActivationGroup

**Source:** `java.rmi\java\rmi\activation\ActivationGroup.html`

### Class Description

```java
public abstract class
ActivationGroup

extends
UnicastRemoteObject

implements
ActivationInstantiator
```

An

ActivationGroup

is responsible for creating new
instances of "activatable" objects in its group, informing its

ActivationMonitor

when either: its object's become
active or inactive, or the group as a whole becomes inactive.

An

ActivationGroup

is

initially

created in one
of several ways:

- as a side-effect of creating an

ActivationDesc

without an explicit

ActivationGroupID

for the
first activatable object in the group, or

via the

ActivationGroup.createGroup

method

as a side-effect of activating the first object in a group
whose

ActivationGroupDesc

was only registered.

Only the activator can

recreate

an

ActivationGroup

. The activator spawns, as needed, a
separate VM (as a child process, for example) for each registered
activation group and directs activation requests to the appropriate
group. It is implementation specific how VMs are spawned. An
activation group is created via the

ActivationGroup.createGroup

static method. The

createGroup

method has two requirements on the group
to be created: 1) the group must be a concrete subclass of

ActivationGroup

, and 2) the group must have a
constructor that takes two arguments:

- the group's

ActivationGroupID

, and

the group's initialization data (in a

java.rmi.MarshalledObject

)

When created, the default implementation of

ActivationGroup

will override the system properties
with the properties requested when its

ActivationGroupDesc

was created, and will set a

SecurityManager

as the default system
security manager. If your application requires specific properties
to be set when objects are activated in the group, the application
should create a special

Properties

object containing
these properties, then create an

ActivationGroupDesc

with the

Properties

object, and use

ActivationGroup.createGroup

before creating any

ActivationDesc

s (before the default

ActivationGroupDesc

is created). If your application
requires the use of a security manager other than

SecurityManager

, in the
ActivativationGroupDescriptor properties list you can set

java.security.manager

property to the name of the security
manager you would like to install.

**All Implemented Interfaces:** Serializable

,

ActivationInstantiator

,

Remote

---

### Field Details

*No entries found.*

### Constructor Details

#### protected ActivationGroup​(
ActivationGroupID
groupID)
throws
RemoteException

Constructs an activation group with the given activation group
identifier. The group is exported as a

java.rmi.server.UnicastRemoteObject

.

**Parameters:**
- groupID

- the group's identifier

**Throws:**
- RemoteException

- if this group could not be exported
- UnsupportedOperationException

- if and only if activation is
not supported by this implementation

**Since:**
- 1.2

---

### Method Details

#### public boolean inactiveObject​(
ActivationID
id)
throws
ActivationException
,

UnknownObjectException
,

RemoteException

The group's

inactiveObject

method is called
indirectly via a call to the

Activatable.inactive

method. A remote object implementation must call

Activatable

's

inactive

method when
that object deactivates (the object deems that it is no longer
active). If the object does not call

Activatable.inactive

when it deactivates, the
object will never be garbage collected since the group keeps
strong references to the objects it creates.

The group's

inactiveObject

method unexports the
remote object from the RMI runtime so that the object can no
longer receive incoming RMI calls. An object will only be unexported
if the object has no pending or executing calls.
The subclass of

ActivationGroup

must override this
method and unexport the object.

After removing the object from the RMI runtime, the group
must inform its

ActivationMonitor

(via the monitor's

inactiveObject

method) that the remote object is
not currently active so that the remote object will be
re-activated by the activator upon a subsequent activation
request.

This method simply informs the group's monitor that the object
is inactive. It is up to the concrete subclass of ActivationGroup
to fulfill the additional requirement of unexporting the object.

**Parameters:**
- id

- the object's activation identifier

**Returns:**
- true if the object was successfully deactivated; otherwise
returns false.

**Throws:**
- UnknownObjectException

- if object is unknown (may already
be inactive)
- RemoteException

- if call informing monitor fails
- ActivationException

- if group is inactive

**Since:**
- 1.2

---

#### public abstract void activeObject​(
ActivationID
id,

Remote
obj)
throws
ActivationException
,

UnknownObjectException
,

RemoteException

The group's

activeObject

method is called when an
object is exported (either by

Activatable

object
construction or an explicit call to

Activatable.exportObject

. The group must inform its

ActivationMonitor

that the object is active (via
the monitor's

activeObject

method) if the group
hasn't already done so.

**Parameters:**
- id

- the object's identifier
- obj

- the remote object implementation

**Throws:**
- UnknownObjectException

- if object is not registered
- RemoteException

- if call informing monitor fails
- ActivationException

- if group is inactive

**Since:**
- 1.2

---

#### public static
ActivationGroup
createGroup​(
ActivationGroupID
id,

ActivationGroupDesc
desc,
long incarnation)
throws
ActivationException

Create and set the activation group for the current VM. The
activation group can only be set if it is not currently set.
An activation group is set using the

createGroup

method when the

Activator

initiates the
re-creation of an activation group in order to carry out
incoming

activate

requests. A group must first be
registered with the

ActivationSystem

before it can
be created via this method.

The group class specified by the

ActivationGroupDesc

must be a concrete subclass of

ActivationGroup

and have a public constructor that
takes two arguments: the

ActivationGroupID

for the
group and the

MarshalledObject

containing the
group's initialization data (obtained from the

ActivationGroupDesc

.

If the group class name specified in the

ActivationGroupDesc

is

null

, then
this method will behave as if the group descriptor contained
the name of the default activation group implementation class.

Note that if your application creates its own custom
activation group, a security manager must be set for that
group. Otherwise objects cannot be activated in the group.

SecurityManager

is set by default.

If a security manager is already set in the group VM, this
method first calls the security manager's

checkSetFactory

method. This could result in a

SecurityException

. If your application needs to
set a different security manager, you must ensure that the
policy file specified by the group's

ActivationGroupDesc

grants the group the necessary
permissions to set a new security manager. (Note: This will be
necessary if your group downloads and sets a security manager).

After the group is created, the

ActivationSystem

is informed that the group is
active by calling the

activeGroup

method which
returns the

ActivationMonitor

for the group. The
application need not call

activeGroup

independently since it is taken care of by this method.

Once a group is created, subsequent calls to the

currentGroupID

method will return the identifier
for this group until the group becomes inactive.

**Parameters:**
- id

- the activation group's identifier
- desc

- the activation group's descriptor
- incarnation

- the group's incarnation number (zero on group's
initial creation)

**Returns:**
- the activation group for the VM

**Throws:**
- ActivationException

- if group already exists or if error
occurs during group creation
- SecurityException

- if permission to create group is denied.
(Note: The default implementation of the security manager

checkSetFactory

method requires the RuntimePermission "setFactory")
- UnsupportedOperationException

- if and only if activation is
not supported by this implementation

**See Also:**
- SecurityManager.checkSetFactory()

**Since:**
- 1.2

---

#### public static
ActivationGroupID
currentGroupID()

Returns the current activation group's identifier. Returns null
if no group is currently active for this VM.

**Returns:**
- the activation group's identifier

**Throws:**
- UnsupportedOperationException

- if and only if activation is
not supported by this implementation

**Since:**
- 1.2

---

#### public static void setSystem​(
ActivationSystem
system)
throws
ActivationException

Set the activation system for the VM. The activation system can
only be set it if no group is currently active. If the activation
system is not set via this call, then the

getSystem

method attempts to obtain a reference to the

ActivationSystem

by looking up the name
"java.rmi.activation.ActivationSystem" in the Activator's
registry. By default, the port number used to look up the
activation system is defined by

ActivationSystem.SYSTEM_PORT

. This port can be overridden
by setting the property

java.rmi.activation.port

.

If there is a security manager, this method first
calls the security manager's

checkSetFactory

method.
This could result in a SecurityException.

**Parameters:**
- system

- remote reference to the

ActivationSystem

**Throws:**
- ActivationException

- if activation system is already set
- SecurityException

- if permission to set the activation system is denied.
(Note: The default implementation of the security manager

checkSetFactory

method requires the RuntimePermission "setFactory")
- UnsupportedOperationException

- if and only if activation is
not supported by this implementation

**See Also:**
- getSystem()

,

SecurityManager.checkSetFactory()

**Since:**
- 1.2

---

#### public static
ActivationSystem
getSystem()
throws
ActivationException

Returns the activation system for the VM. The activation system
may be set by the

setSystem

method. If the
activation system is not set via the

setSystem

method, then the

getSystem

method attempts to
obtain a reference to the

ActivationSystem

by
looking up the name "java.rmi.activation.ActivationSystem" in
the Activator's registry. By default, the port number used to
look up the activation system is defined by

ActivationSystem.SYSTEM_PORT

. This port can be
overridden by setting the property

java.rmi.activation.port

.

**Returns:**
- the activation system for the VM/group

**Throws:**
- ActivationException

- if activation system cannot be
obtained or is not bound
(means that it is not running)
- UnsupportedOperationException

- if and only if activation is
not supported by this implementation

**See Also:**
- setSystem(java.rmi.activation.ActivationSystem)

**Since:**
- 1.2

---

#### protected void activeObject​(
ActivationID
id,

MarshalledObject
<? extends
Remote
> mobj)
throws
ActivationException
,

UnknownObjectException
,

RemoteException

This protected method is necessary for subclasses to
make the

activeObject

callback to the group's
monitor. The call is simply forwarded to the group's

ActivationMonitor

.

**Parameters:**
- id

- the object's identifier
- mobj

- a marshalled object containing the remote object's stub

**Throws:**
- UnknownObjectException

- if object is not registered
- RemoteException

- if call informing monitor fails
- ActivationException

- if an activation error occurs

**Since:**
- 1.2

---

#### protected void inactiveGroup()
throws
UnknownGroupException
,

RemoteException

This protected method is necessary for subclasses to
make the

inactiveGroup

callback to the group's
monitor. The call is simply forwarded to the group's

ActivationMonitor

. Also, the current group
for the VM is set to null.

**Throws:**
- UnknownGroupException

- if group is not registered
- RemoteException

- if call informing monitor fails

**Since:**
- 1.2

---

### Additional Sections

#### Class ActivationGroup

java.lang.Object

- java.rmi.server.RemoteObject
- - java.rmi.server.RemoteServer
- - java.rmi.server.UnicastRemoteObject
- - java.rmi.activation.ActivationGroup

java.rmi.server.RemoteObject

- java.rmi.server.RemoteServer
- - java.rmi.server.UnicastRemoteObject
- - java.rmi.activation.ActivationGroup

java.rmi.server.RemoteServer

- java.rmi.server.UnicastRemoteObject
- - java.rmi.activation.ActivationGroup

java.rmi.server.UnicastRemoteObject

- java.rmi.activation.ActivationGroup

java.rmi.activation.ActivationGroup

**All Implemented Interfaces:** Serializable

,

ActivationInstantiator

,

Remote

```java
public abstract class
ActivationGroup

extends
UnicastRemoteObject

implements
ActivationInstantiator
```

An

ActivationGroup

is responsible for creating new
instances of "activatable" objects in its group, informing its

ActivationMonitor

when either: its object's become
active or inactive, or the group as a whole becomes inactive.

An

ActivationGroup

is

initially

created in one
of several ways:

- as a side-effect of creating an

ActivationDesc

without an explicit

ActivationGroupID

for the
first activatable object in the group, or

via the

ActivationGroup.createGroup

method

as a side-effect of activating the first object in a group
whose

ActivationGroupDesc

was only registered.

Only the activator can

recreate

an

ActivationGroup

. The activator spawns, as needed, a
separate VM (as a child process, for example) for each registered
activation group and directs activation requests to the appropriate
group. It is implementation specific how VMs are spawned. An
activation group is created via the

ActivationGroup.createGroup

static method. The

createGroup

method has two requirements on the group
to be created: 1) the group must be a concrete subclass of

ActivationGroup

, and 2) the group must have a
constructor that takes two arguments:

- the group's

ActivationGroupID

, and

the group's initialization data (in a

java.rmi.MarshalledObject

)

When created, the default implementation of

ActivationGroup

will override the system properties
with the properties requested when its

ActivationGroupDesc

was created, and will set a

SecurityManager

as the default system
security manager. If your application requires specific properties
to be set when objects are activated in the group, the application
should create a special

Properties

object containing
these properties, then create an

ActivationGroupDesc

with the

Properties

object, and use

ActivationGroup.createGroup

before creating any

ActivationDesc

s (before the default

ActivationGroupDesc

is created). If your application
requires the use of a security manager other than

SecurityManager

, in the
ActivativationGroupDescriptor properties list you can set

java.security.manager

property to the name of the security
manager you would like to install.

**Since:** 1.2
**See Also:** ActivationInstantiator

,

ActivationGroupDesc

,

ActivationGroupID

,

Serialized Form

public abstract class

ActivationGroup

extends

UnicastRemoteObject

implements

ActivationInstantiator

An

ActivationGroup

is responsible for creating new
instances of "activatable" objects in its group, informing its

ActivationMonitor

when either: its object's become
active or inactive, or the group as a whole becomes inactive.

An

ActivationGroup

is

initially

created in one
of several ways:

- as a side-effect of creating an

ActivationDesc

without an explicit

ActivationGroupID

for the
first activatable object in the group, or

via the

ActivationGroup.createGroup

method

as a side-effect of activating the first object in a group
whose

ActivationGroupDesc

was only registered.

Only the activator can

recreate

an

ActivationGroup

. The activator spawns, as needed, a
separate VM (as a child process, for example) for each registered
activation group and directs activation requests to the appropriate
group. It is implementation specific how VMs are spawned. An
activation group is created via the

ActivationGroup.createGroup

static method. The

createGroup

method has two requirements on the group
to be created: 1) the group must be a concrete subclass of

ActivationGroup

, and 2) the group must have a
constructor that takes two arguments:

- the group's

ActivationGroupID

, and

the group's initialization data (in a

java.rmi.MarshalledObject

)

When created, the default implementation of

ActivationGroup

will override the system properties
with the properties requested when its

ActivationGroupDesc

was created, and will set a

SecurityManager

as the default system
security manager. If your application requires specific properties
to be set when objects are activated in the group, the application
should create a special

Properties

object containing
these properties, then create an

ActivationGroupDesc

with the

Properties

object, and use

ActivationGroup.createGroup

before creating any

ActivationDesc

s (before the default

ActivationGroupDesc

is created). If your application
requires the use of a security manager other than

SecurityManager

, in the
ActivativationGroupDescriptor properties list you can set

java.security.manager

property to the name of the security
manager you would like to install.

An

ActivationGroup

is

initially

created in one
of several ways:

- as a side-effect of creating an

ActivationDesc

without an explicit

ActivationGroupID

for the
first activatable object in the group, or

via the

ActivationGroup.createGroup

method

as a side-effect of activating the first object in a group
whose

ActivationGroupDesc

was only registered.

Only the activator can

recreate

an

ActivationGroup

. The activator spawns, as needed, a
separate VM (as a child process, for example) for each registered
activation group and directs activation requests to the appropriate
group. It is implementation specific how VMs are spawned. An
activation group is created via the

ActivationGroup.createGroup

static method. The

createGroup

method has two requirements on the group
to be created: 1) the group must be a concrete subclass of

ActivationGroup

, and 2) the group must have a
constructor that takes two arguments:

- the group's

ActivationGroupID

, and

the group's initialization data (in a

java.rmi.MarshalledObject

)

When created, the default implementation of

ActivationGroup

will override the system properties
with the properties requested when its

ActivationGroupDesc

was created, and will set a

SecurityManager

as the default system
security manager. If your application requires specific properties
to be set when objects are activated in the group, the application
should create a special

Properties

object containing
these properties, then create an

ActivationGroupDesc

with the

Properties

object, and use

ActivationGroup.createGroup

before creating any

ActivationDesc

s (before the default

ActivationGroupDesc

is created). If your application
requires the use of a security manager other than

SecurityManager

, in the
ActivativationGroupDescriptor properties list you can set

java.security.manager

property to the name of the security
manager you would like to install.

as a side-effect of creating an

ActivationDesc

without an explicit

ActivationGroupID

for the
first activatable object in the group, or

via the

ActivationGroup.createGroup

method

as a side-effect of activating the first object in a group
whose

ActivationGroupDesc

was only registered.

Only the activator can

recreate

an

ActivationGroup

. The activator spawns, as needed, a
separate VM (as a child process, for example) for each registered
activation group and directs activation requests to the appropriate
group. It is implementation specific how VMs are spawned. An
activation group is created via the

ActivationGroup.createGroup

static method. The

createGroup

method has two requirements on the group
to be created: 1) the group must be a concrete subclass of

ActivationGroup

, and 2) the group must have a
constructor that takes two arguments:

- the group's

ActivationGroupID

, and

the group's initialization data (in a

java.rmi.MarshalledObject

)

When created, the default implementation of

ActivationGroup

will override the system properties
with the properties requested when its

ActivationGroupDesc

was created, and will set a

SecurityManager

as the default system
security manager. If your application requires specific properties
to be set when objects are activated in the group, the application
should create a special

Properties

object containing
these properties, then create an

ActivationGroupDesc

with the

Properties

object, and use

ActivationGroup.createGroup

before creating any

ActivationDesc

s (before the default

ActivationGroupDesc

is created). If your application
requires the use of a security manager other than

SecurityManager

, in the
ActivativationGroupDescriptor properties list you can set

java.security.manager

property to the name of the security
manager you would like to install.

the group's

ActivationGroupID

, and

the group's initialization data (in a

java.rmi.MarshalledObject

)

When created, the default implementation of

ActivationGroup

will override the system properties
with the properties requested when its

ActivationGroupDesc

was created, and will set a

SecurityManager

as the default system
security manager. If your application requires specific properties
to be set when objects are activated in the group, the application
should create a special

Properties

object containing
these properties, then create an

ActivationGroupDesc

with the

Properties

object, and use

ActivationGroup.createGroup

before creating any

ActivationDesc

s (before the default

ActivationGroupDesc

is created). If your application
requires the use of a security manager other than

SecurityManager

, in the
ActivativationGroupDescriptor properties list you can set

java.security.manager

property to the name of the security
manager you would like to install.

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

ActivationGroup

​(

ActivationGroupID

groupID)

Constructs an activation group with the given activation group
identifier.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

activeObject

​(

ActivationID

id,

MarshalledObject

<? extends

Remote

> mobj)

This protected method is necessary for subclasses to
make the

activeObject

callback to the group's
monitor.

abstract void

activeObject

​(

ActivationID

id,

Remote

obj)

The group's

activeObject

method is called when an
object is exported (either by

Activatable

object
construction or an explicit call to

Activatable.exportObject

.

static

ActivationGroup

createGroup

​(

ActivationGroupID

id,

ActivationGroupDesc

desc,
long incarnation)

Create and set the activation group for the current VM.

static

ActivationGroupID

currentGroupID

()

Returns the current activation group's identifier.

static

ActivationSystem

getSystem

()

Returns the activation system for the VM.

protected void

inactiveGroup

()

This protected method is necessary for subclasses to
make the

inactiveGroup

callback to the group's
monitor.

boolean

inactiveObject

​(

ActivationID

id)

The group's

inactiveObject

method is called
indirectly via a call to the

Activatable.inactive

method.

static void

setSystem

​(

ActivationSystem

system)

Set the activation system for the VM.

- Methods declared in class java.rmi.server.

UnicastRemoteObject

clone

,

exportObject

,

exportObject

,

exportObject

,

exportObject

,

exportObject

,

unexportObject

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

- Methods declared in interface java.rmi.activation.

ActivationInstantiator

newInstance

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

ActivationGroup

​(

ActivationGroupID

groupID)

Constructs an activation group with the given activation group
identifier.

---

#### Constructor Summary

Constructs an activation group with the given activation group
identifier.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

activeObject

​(

ActivationID

id,

MarshalledObject

<? extends

Remote

> mobj)

This protected method is necessary for subclasses to
make the

activeObject

callback to the group's
monitor.

abstract void

activeObject

​(

ActivationID

id,

Remote

obj)

The group's

activeObject

method is called when an
object is exported (either by

Activatable

object
construction or an explicit call to

Activatable.exportObject

.

static

ActivationGroup

createGroup

​(

ActivationGroupID

id,

ActivationGroupDesc

desc,
long incarnation)

Create and set the activation group for the current VM.

static

ActivationGroupID

currentGroupID

()

Returns the current activation group's identifier.

static

ActivationSystem

getSystem

()

Returns the activation system for the VM.

protected void

inactiveGroup

()

This protected method is necessary for subclasses to
make the

inactiveGroup

callback to the group's
monitor.

boolean

inactiveObject

​(

ActivationID

id)

The group's

inactiveObject

method is called
indirectly via a call to the

Activatable.inactive

method.

static void

setSystem

​(

ActivationSystem

system)

Set the activation system for the VM.

- Methods declared in class java.rmi.server.

UnicastRemoteObject

clone

,

exportObject

,

exportObject

,

exportObject

,

exportObject

,

exportObject

,

unexportObject

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

- Methods declared in interface java.rmi.activation.

ActivationInstantiator

newInstance

---

#### Method Summary

This protected method is necessary for subclasses to
make the

activeObject

callback to the group's
monitor.

The group's

activeObject

method is called when an
object is exported (either by

Activatable

object
construction or an explicit call to

Activatable.exportObject

.

Create and set the activation group for the current VM.

Returns the current activation group's identifier.

Returns the activation system for the VM.

This protected method is necessary for subclasses to
make the

inactiveGroup

callback to the group's
monitor.

The group's

inactiveObject

method is called
indirectly via a call to the

Activatable.inactive

method.

Set the activation system for the VM.

Methods declared in class java.rmi.server.

UnicastRemoteObject

clone

,

exportObject

,

exportObject

,

exportObject

,

exportObject

,

exportObject

,

unexportObject

---

#### Methods declared in class java.rmi.server. UnicastRemoteObject

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

Methods declared in interface java.rmi.activation.

ActivationInstantiator

newInstance

---

#### Methods declared in interface java.rmi.activation. ActivationInstantiator

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ActivationGroup

```java
protected ActivationGroup​(
ActivationGroupID
groupID)
throws
RemoteException
```

Constructs an activation group with the given activation group
identifier. The group is exported as a

java.rmi.server.UnicastRemoteObject

.

**Parameters:** groupID

- the group's identifier
**Throws:** RemoteException

- if this group could not be exported
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

============ METHOD DETAIL ==========

- Method Detail

- inactiveObject

```java
public boolean inactiveObject​(
ActivationID
id)
throws
ActivationException
,

UnknownObjectException
,

RemoteException
```

The group's

inactiveObject

method is called
indirectly via a call to the

Activatable.inactive

method. A remote object implementation must call

Activatable

's

inactive

method when
that object deactivates (the object deems that it is no longer
active). If the object does not call

Activatable.inactive

when it deactivates, the
object will never be garbage collected since the group keeps
strong references to the objects it creates.

The group's

inactiveObject

method unexports the
remote object from the RMI runtime so that the object can no
longer receive incoming RMI calls. An object will only be unexported
if the object has no pending or executing calls.
The subclass of

ActivationGroup

must override this
method and unexport the object.

After removing the object from the RMI runtime, the group
must inform its

ActivationMonitor

(via the monitor's

inactiveObject

method) that the remote object is
not currently active so that the remote object will be
re-activated by the activator upon a subsequent activation
request.

This method simply informs the group's monitor that the object
is inactive. It is up to the concrete subclass of ActivationGroup
to fulfill the additional requirement of unexporting the object.

**Parameters:** id

- the object's activation identifier
**Returns:** true if the object was successfully deactivated; otherwise
returns false.
**Throws:** UnknownObjectException

- if object is unknown (may already
be inactive)
**Throws:** RemoteException

- if call informing monitor fails
**Throws:** ActivationException

- if group is inactive
**Since:** 1.2

- activeObject

```java
public abstract void activeObject​(
ActivationID
id,

Remote
obj)
throws
ActivationException
,

UnknownObjectException
,

RemoteException
```

The group's

activeObject

method is called when an
object is exported (either by

Activatable

object
construction or an explicit call to

Activatable.exportObject

. The group must inform its

ActivationMonitor

that the object is active (via
the monitor's

activeObject

method) if the group
hasn't already done so.

**Parameters:** id

- the object's identifier
**Parameters:** obj

- the remote object implementation
**Throws:** UnknownObjectException

- if object is not registered
**Throws:** RemoteException

- if call informing monitor fails
**Throws:** ActivationException

- if group is inactive
**Since:** 1.2

- createGroup

```java
public static
ActivationGroup
createGroup​(
ActivationGroupID
id,

ActivationGroupDesc
desc,
long incarnation)
throws
ActivationException
```

Create and set the activation group for the current VM. The
activation group can only be set if it is not currently set.
An activation group is set using the

createGroup

method when the

Activator

initiates the
re-creation of an activation group in order to carry out
incoming

activate

requests. A group must first be
registered with the

ActivationSystem

before it can
be created via this method.

The group class specified by the

ActivationGroupDesc

must be a concrete subclass of

ActivationGroup

and have a public constructor that
takes two arguments: the

ActivationGroupID

for the
group and the

MarshalledObject

containing the
group's initialization data (obtained from the

ActivationGroupDesc

.

If the group class name specified in the

ActivationGroupDesc

is

null

, then
this method will behave as if the group descriptor contained
the name of the default activation group implementation class.

Note that if your application creates its own custom
activation group, a security manager must be set for that
group. Otherwise objects cannot be activated in the group.

SecurityManager

is set by default.

If a security manager is already set in the group VM, this
method first calls the security manager's

checkSetFactory

method. This could result in a

SecurityException

. If your application needs to
set a different security manager, you must ensure that the
policy file specified by the group's

ActivationGroupDesc

grants the group the necessary
permissions to set a new security manager. (Note: This will be
necessary if your group downloads and sets a security manager).

After the group is created, the

ActivationSystem

is informed that the group is
active by calling the

activeGroup

method which
returns the

ActivationMonitor

for the group. The
application need not call

activeGroup

independently since it is taken care of by this method.

Once a group is created, subsequent calls to the

currentGroupID

method will return the identifier
for this group until the group becomes inactive.

**Parameters:** id

- the activation group's identifier
**Parameters:** desc

- the activation group's descriptor
**Parameters:** incarnation

- the group's incarnation number (zero on group's
initial creation)
**Returns:** the activation group for the VM
**Throws:** ActivationException

- if group already exists or if error
occurs during group creation
**Throws:** SecurityException

- if permission to create group is denied.
(Note: The default implementation of the security manager

checkSetFactory

method requires the RuntimePermission "setFactory")
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2
**See Also:** SecurityManager.checkSetFactory()

- currentGroupID

```java
public static
ActivationGroupID
currentGroupID()
```

Returns the current activation group's identifier. Returns null
if no group is currently active for this VM.

**Returns:** the activation group's identifier
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

- setSystem

```java
public static void setSystem​(
ActivationSystem
system)
throws
ActivationException
```

Set the activation system for the VM. The activation system can
only be set it if no group is currently active. If the activation
system is not set via this call, then the

getSystem

method attempts to obtain a reference to the

ActivationSystem

by looking up the name
"java.rmi.activation.ActivationSystem" in the Activator's
registry. By default, the port number used to look up the
activation system is defined by

ActivationSystem.SYSTEM_PORT

. This port can be overridden
by setting the property

java.rmi.activation.port

.

If there is a security manager, this method first
calls the security manager's

checkSetFactory

method.
This could result in a SecurityException.

**Parameters:** system

- remote reference to the

ActivationSystem
**Throws:** ActivationException

- if activation system is already set
**Throws:** SecurityException

- if permission to set the activation system is denied.
(Note: The default implementation of the security manager

checkSetFactory

method requires the RuntimePermission "setFactory")
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2
**See Also:** getSystem()

,

SecurityManager.checkSetFactory()

- getSystem

```java
public static
ActivationSystem
getSystem()
throws
ActivationException
```

Returns the activation system for the VM. The activation system
may be set by the

setSystem

method. If the
activation system is not set via the

setSystem

method, then the

getSystem

method attempts to
obtain a reference to the

ActivationSystem

by
looking up the name "java.rmi.activation.ActivationSystem" in
the Activator's registry. By default, the port number used to
look up the activation system is defined by

ActivationSystem.SYSTEM_PORT

. This port can be
overridden by setting the property

java.rmi.activation.port

.

**Returns:** the activation system for the VM/group
**Throws:** ActivationException

- if activation system cannot be
obtained or is not bound
(means that it is not running)
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2
**See Also:** setSystem(java.rmi.activation.ActivationSystem)

- activeObject

```java
protected void activeObject​(
ActivationID
id,

MarshalledObject
<? extends
Remote
> mobj)
throws
ActivationException
,

UnknownObjectException
,

RemoteException
```

This protected method is necessary for subclasses to
make the

activeObject

callback to the group's
monitor. The call is simply forwarded to the group's

ActivationMonitor

.

**Parameters:** id

- the object's identifier
**Parameters:** mobj

- a marshalled object containing the remote object's stub
**Throws:** UnknownObjectException

- if object is not registered
**Throws:** RemoteException

- if call informing monitor fails
**Throws:** ActivationException

- if an activation error occurs
**Since:** 1.2

- inactiveGroup

```java
protected void inactiveGroup()
throws
UnknownGroupException
,

RemoteException
```

This protected method is necessary for subclasses to
make the

inactiveGroup

callback to the group's
monitor. The call is simply forwarded to the group's

ActivationMonitor

. Also, the current group
for the VM is set to null.

**Throws:** UnknownGroupException

- if group is not registered
**Throws:** RemoteException

- if call informing monitor fails
**Since:** 1.2

Constructor Detail

- ActivationGroup

```java
protected ActivationGroup​(
ActivationGroupID
groupID)
throws
RemoteException
```

Constructs an activation group with the given activation group
identifier. The group is exported as a

java.rmi.server.UnicastRemoteObject

.

**Parameters:** groupID

- the group's identifier
**Throws:** RemoteException

- if this group could not be exported
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

---

#### Constructor Detail

ActivationGroup

```java
protected ActivationGroup​(
ActivationGroupID
groupID)
throws
RemoteException
```

Constructs an activation group with the given activation group
identifier. The group is exported as a

java.rmi.server.UnicastRemoteObject

.

**Parameters:** groupID

- the group's identifier
**Throws:** RemoteException

- if this group could not be exported
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

---

#### ActivationGroup

protected ActivationGroup​(

ActivationGroupID

groupID)
throws

RemoteException

Constructs an activation group with the given activation group
identifier. The group is exported as a

java.rmi.server.UnicastRemoteObject

.

Method Detail

- inactiveObject

```java
public boolean inactiveObject​(
ActivationID
id)
throws
ActivationException
,

UnknownObjectException
,

RemoteException
```

The group's

inactiveObject

method is called
indirectly via a call to the

Activatable.inactive

method. A remote object implementation must call

Activatable

's

inactive

method when
that object deactivates (the object deems that it is no longer
active). If the object does not call

Activatable.inactive

when it deactivates, the
object will never be garbage collected since the group keeps
strong references to the objects it creates.

The group's

inactiveObject

method unexports the
remote object from the RMI runtime so that the object can no
longer receive incoming RMI calls. An object will only be unexported
if the object has no pending or executing calls.
The subclass of

ActivationGroup

must override this
method and unexport the object.

After removing the object from the RMI runtime, the group
must inform its

ActivationMonitor

(via the monitor's

inactiveObject

method) that the remote object is
not currently active so that the remote object will be
re-activated by the activator upon a subsequent activation
request.

This method simply informs the group's monitor that the object
is inactive. It is up to the concrete subclass of ActivationGroup
to fulfill the additional requirement of unexporting the object.

**Parameters:** id

- the object's activation identifier
**Returns:** true if the object was successfully deactivated; otherwise
returns false.
**Throws:** UnknownObjectException

- if object is unknown (may already
be inactive)
**Throws:** RemoteException

- if call informing monitor fails
**Throws:** ActivationException

- if group is inactive
**Since:** 1.2

- activeObject

```java
public abstract void activeObject​(
ActivationID
id,

Remote
obj)
throws
ActivationException
,

UnknownObjectException
,

RemoteException
```

The group's

activeObject

method is called when an
object is exported (either by

Activatable

object
construction or an explicit call to

Activatable.exportObject

. The group must inform its

ActivationMonitor

that the object is active (via
the monitor's

activeObject

method) if the group
hasn't already done so.

**Parameters:** id

- the object's identifier
**Parameters:** obj

- the remote object implementation
**Throws:** UnknownObjectException

- if object is not registered
**Throws:** RemoteException

- if call informing monitor fails
**Throws:** ActivationException

- if group is inactive
**Since:** 1.2

- createGroup

```java
public static
ActivationGroup
createGroup​(
ActivationGroupID
id,

ActivationGroupDesc
desc,
long incarnation)
throws
ActivationException
```

Create and set the activation group for the current VM. The
activation group can only be set if it is not currently set.
An activation group is set using the

createGroup

method when the

Activator

initiates the
re-creation of an activation group in order to carry out
incoming

activate

requests. A group must first be
registered with the

ActivationSystem

before it can
be created via this method.

The group class specified by the

ActivationGroupDesc

must be a concrete subclass of

ActivationGroup

and have a public constructor that
takes two arguments: the

ActivationGroupID

for the
group and the

MarshalledObject

containing the
group's initialization data (obtained from the

ActivationGroupDesc

.

If the group class name specified in the

ActivationGroupDesc

is

null

, then
this method will behave as if the group descriptor contained
the name of the default activation group implementation class.

Note that if your application creates its own custom
activation group, a security manager must be set for that
group. Otherwise objects cannot be activated in the group.

SecurityManager

is set by default.

If a security manager is already set in the group VM, this
method first calls the security manager's

checkSetFactory

method. This could result in a

SecurityException

. If your application needs to
set a different security manager, you must ensure that the
policy file specified by the group's

ActivationGroupDesc

grants the group the necessary
permissions to set a new security manager. (Note: This will be
necessary if your group downloads and sets a security manager).

After the group is created, the

ActivationSystem

is informed that the group is
active by calling the

activeGroup

method which
returns the

ActivationMonitor

for the group. The
application need not call

activeGroup

independently since it is taken care of by this method.

Once a group is created, subsequent calls to the

currentGroupID

method will return the identifier
for this group until the group becomes inactive.

**Parameters:** id

- the activation group's identifier
**Parameters:** desc

- the activation group's descriptor
**Parameters:** incarnation

- the group's incarnation number (zero on group's
initial creation)
**Returns:** the activation group for the VM
**Throws:** ActivationException

- if group already exists or if error
occurs during group creation
**Throws:** SecurityException

- if permission to create group is denied.
(Note: The default implementation of the security manager

checkSetFactory

method requires the RuntimePermission "setFactory")
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2
**See Also:** SecurityManager.checkSetFactory()

- currentGroupID

```java
public static
ActivationGroupID
currentGroupID()
```

Returns the current activation group's identifier. Returns null
if no group is currently active for this VM.

**Returns:** the activation group's identifier
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

- setSystem

```java
public static void setSystem​(
ActivationSystem
system)
throws
ActivationException
```

Set the activation system for the VM. The activation system can
only be set it if no group is currently active. If the activation
system is not set via this call, then the

getSystem

method attempts to obtain a reference to the

ActivationSystem

by looking up the name
"java.rmi.activation.ActivationSystem" in the Activator's
registry. By default, the port number used to look up the
activation system is defined by

ActivationSystem.SYSTEM_PORT

. This port can be overridden
by setting the property

java.rmi.activation.port

.

If there is a security manager, this method first
calls the security manager's

checkSetFactory

method.
This could result in a SecurityException.

**Parameters:** system

- remote reference to the

ActivationSystem
**Throws:** ActivationException

- if activation system is already set
**Throws:** SecurityException

- if permission to set the activation system is denied.
(Note: The default implementation of the security manager

checkSetFactory

method requires the RuntimePermission "setFactory")
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2
**See Also:** getSystem()

,

SecurityManager.checkSetFactory()

- getSystem

```java
public static
ActivationSystem
getSystem()
throws
ActivationException
```

Returns the activation system for the VM. The activation system
may be set by the

setSystem

method. If the
activation system is not set via the

setSystem

method, then the

getSystem

method attempts to
obtain a reference to the

ActivationSystem

by
looking up the name "java.rmi.activation.ActivationSystem" in
the Activator's registry. By default, the port number used to
look up the activation system is defined by

ActivationSystem.SYSTEM_PORT

. This port can be
overridden by setting the property

java.rmi.activation.port

.

**Returns:** the activation system for the VM/group
**Throws:** ActivationException

- if activation system cannot be
obtained or is not bound
(means that it is not running)
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2
**See Also:** setSystem(java.rmi.activation.ActivationSystem)

- activeObject

```java
protected void activeObject​(
ActivationID
id,

MarshalledObject
<? extends
Remote
> mobj)
throws
ActivationException
,

UnknownObjectException
,

RemoteException
```

This protected method is necessary for subclasses to
make the

activeObject

callback to the group's
monitor. The call is simply forwarded to the group's

ActivationMonitor

.

**Parameters:** id

- the object's identifier
**Parameters:** mobj

- a marshalled object containing the remote object's stub
**Throws:** UnknownObjectException

- if object is not registered
**Throws:** RemoteException

- if call informing monitor fails
**Throws:** ActivationException

- if an activation error occurs
**Since:** 1.2

- inactiveGroup

```java
protected void inactiveGroup()
throws
UnknownGroupException
,

RemoteException
```

This protected method is necessary for subclasses to
make the

inactiveGroup

callback to the group's
monitor. The call is simply forwarded to the group's

ActivationMonitor

. Also, the current group
for the VM is set to null.

**Throws:** UnknownGroupException

- if group is not registered
**Throws:** RemoteException

- if call informing monitor fails
**Since:** 1.2

---

#### Method Detail

inactiveObject

```java
public boolean inactiveObject​(
ActivationID
id)
throws
ActivationException
,

UnknownObjectException
,

RemoteException
```

The group's

inactiveObject

method is called
indirectly via a call to the

Activatable.inactive

method. A remote object implementation must call

Activatable

's

inactive

method when
that object deactivates (the object deems that it is no longer
active). If the object does not call

Activatable.inactive

when it deactivates, the
object will never be garbage collected since the group keeps
strong references to the objects it creates.

The group's

inactiveObject

method unexports the
remote object from the RMI runtime so that the object can no
longer receive incoming RMI calls. An object will only be unexported
if the object has no pending or executing calls.
The subclass of

ActivationGroup

must override this
method and unexport the object.

After removing the object from the RMI runtime, the group
must inform its

ActivationMonitor

(via the monitor's

inactiveObject

method) that the remote object is
not currently active so that the remote object will be
re-activated by the activator upon a subsequent activation
request.

This method simply informs the group's monitor that the object
is inactive. It is up to the concrete subclass of ActivationGroup
to fulfill the additional requirement of unexporting the object.

**Parameters:** id

- the object's activation identifier
**Returns:** true if the object was successfully deactivated; otherwise
returns false.
**Throws:** UnknownObjectException

- if object is unknown (may already
be inactive)
**Throws:** RemoteException

- if call informing monitor fails
**Throws:** ActivationException

- if group is inactive
**Since:** 1.2

---

#### inactiveObject

public boolean inactiveObject​(

ActivationID

id)
throws

ActivationException

,

UnknownObjectException

,

RemoteException

The group's

inactiveObject

method is called
indirectly via a call to the

Activatable.inactive

method. A remote object implementation must call

Activatable

's

inactive

method when
that object deactivates (the object deems that it is no longer
active). If the object does not call

Activatable.inactive

when it deactivates, the
object will never be garbage collected since the group keeps
strong references to the objects it creates.

The group's

inactiveObject

method unexports the
remote object from the RMI runtime so that the object can no
longer receive incoming RMI calls. An object will only be unexported
if the object has no pending or executing calls.
The subclass of

ActivationGroup

must override this
method and unexport the object.

After removing the object from the RMI runtime, the group
must inform its

ActivationMonitor

(via the monitor's

inactiveObject

method) that the remote object is
not currently active so that the remote object will be
re-activated by the activator upon a subsequent activation
request.

This method simply informs the group's monitor that the object
is inactive. It is up to the concrete subclass of ActivationGroup
to fulfill the additional requirement of unexporting the object.

The group's

inactiveObject

method unexports the
remote object from the RMI runtime so that the object can no
longer receive incoming RMI calls. An object will only be unexported
if the object has no pending or executing calls.
The subclass of

ActivationGroup

must override this
method and unexport the object.

After removing the object from the RMI runtime, the group
must inform its

ActivationMonitor

(via the monitor's

inactiveObject

method) that the remote object is
not currently active so that the remote object will be
re-activated by the activator upon a subsequent activation
request.

This method simply informs the group's monitor that the object
is inactive. It is up to the concrete subclass of ActivationGroup
to fulfill the additional requirement of unexporting the object.

After removing the object from the RMI runtime, the group
must inform its

ActivationMonitor

(via the monitor's

inactiveObject

method) that the remote object is
not currently active so that the remote object will be
re-activated by the activator upon a subsequent activation
request.

This method simply informs the group's monitor that the object
is inactive. It is up to the concrete subclass of ActivationGroup
to fulfill the additional requirement of unexporting the object.

This method simply informs the group's monitor that the object
is inactive. It is up to the concrete subclass of ActivationGroup
to fulfill the additional requirement of unexporting the object.

activeObject

```java
public abstract void activeObject​(
ActivationID
id,

Remote
obj)
throws
ActivationException
,

UnknownObjectException
,

RemoteException
```

The group's

activeObject

method is called when an
object is exported (either by

Activatable

object
construction or an explicit call to

Activatable.exportObject

. The group must inform its

ActivationMonitor

that the object is active (via
the monitor's

activeObject

method) if the group
hasn't already done so.

**Parameters:** id

- the object's identifier
**Parameters:** obj

- the remote object implementation
**Throws:** UnknownObjectException

- if object is not registered
**Throws:** RemoteException

- if call informing monitor fails
**Throws:** ActivationException

- if group is inactive
**Since:** 1.2

---

#### activeObject

public abstract void activeObject​(

ActivationID

id,

Remote

obj)
throws

ActivationException

,

UnknownObjectException

,

RemoteException

The group's

activeObject

method is called when an
object is exported (either by

Activatable

object
construction or an explicit call to

Activatable.exportObject

. The group must inform its

ActivationMonitor

that the object is active (via
the monitor's

activeObject

method) if the group
hasn't already done so.

createGroup

```java
public static
ActivationGroup
createGroup​(
ActivationGroupID
id,

ActivationGroupDesc
desc,
long incarnation)
throws
ActivationException
```

Create and set the activation group for the current VM. The
activation group can only be set if it is not currently set.
An activation group is set using the

createGroup

method when the

Activator

initiates the
re-creation of an activation group in order to carry out
incoming

activate

requests. A group must first be
registered with the

ActivationSystem

before it can
be created via this method.

The group class specified by the

ActivationGroupDesc

must be a concrete subclass of

ActivationGroup

and have a public constructor that
takes two arguments: the

ActivationGroupID

for the
group and the

MarshalledObject

containing the
group's initialization data (obtained from the

ActivationGroupDesc

.

If the group class name specified in the

ActivationGroupDesc

is

null

, then
this method will behave as if the group descriptor contained
the name of the default activation group implementation class.

Note that if your application creates its own custom
activation group, a security manager must be set for that
group. Otherwise objects cannot be activated in the group.

SecurityManager

is set by default.

If a security manager is already set in the group VM, this
method first calls the security manager's

checkSetFactory

method. This could result in a

SecurityException

. If your application needs to
set a different security manager, you must ensure that the
policy file specified by the group's

ActivationGroupDesc

grants the group the necessary
permissions to set a new security manager. (Note: This will be
necessary if your group downloads and sets a security manager).

After the group is created, the

ActivationSystem

is informed that the group is
active by calling the

activeGroup

method which
returns the

ActivationMonitor

for the group. The
application need not call

activeGroup

independently since it is taken care of by this method.

Once a group is created, subsequent calls to the

currentGroupID

method will return the identifier
for this group until the group becomes inactive.

**Parameters:** id

- the activation group's identifier
**Parameters:** desc

- the activation group's descriptor
**Parameters:** incarnation

- the group's incarnation number (zero on group's
initial creation)
**Returns:** the activation group for the VM
**Throws:** ActivationException

- if group already exists or if error
occurs during group creation
**Throws:** SecurityException

- if permission to create group is denied.
(Note: The default implementation of the security manager

checkSetFactory

method requires the RuntimePermission "setFactory")
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2
**See Also:** SecurityManager.checkSetFactory()

---

#### createGroup

public static

ActivationGroup

createGroup​(

ActivationGroupID

id,

ActivationGroupDesc

desc,
long incarnation)
throws

ActivationException

Create and set the activation group for the current VM. The
activation group can only be set if it is not currently set.
An activation group is set using the

createGroup

method when the

Activator

initiates the
re-creation of an activation group in order to carry out
incoming

activate

requests. A group must first be
registered with the

ActivationSystem

before it can
be created via this method.

The group class specified by the

ActivationGroupDesc

must be a concrete subclass of

ActivationGroup

and have a public constructor that
takes two arguments: the

ActivationGroupID

for the
group and the

MarshalledObject

containing the
group's initialization data (obtained from the

ActivationGroupDesc

.

If the group class name specified in the

ActivationGroupDesc

is

null

, then
this method will behave as if the group descriptor contained
the name of the default activation group implementation class.

Note that if your application creates its own custom
activation group, a security manager must be set for that
group. Otherwise objects cannot be activated in the group.

SecurityManager

is set by default.

If a security manager is already set in the group VM, this
method first calls the security manager's

checkSetFactory

method. This could result in a

SecurityException

. If your application needs to
set a different security manager, you must ensure that the
policy file specified by the group's

ActivationGroupDesc

grants the group the necessary
permissions to set a new security manager. (Note: This will be
necessary if your group downloads and sets a security manager).

After the group is created, the

ActivationSystem

is informed that the group is
active by calling the

activeGroup

method which
returns the

ActivationMonitor

for the group. The
application need not call

activeGroup

independently since it is taken care of by this method.

Once a group is created, subsequent calls to the

currentGroupID

method will return the identifier
for this group until the group becomes inactive.

The group class specified by the

ActivationGroupDesc

must be a concrete subclass of

ActivationGroup

and have a public constructor that
takes two arguments: the

ActivationGroupID

for the
group and the

MarshalledObject

containing the
group's initialization data (obtained from the

ActivationGroupDesc

.

If the group class name specified in the

ActivationGroupDesc

is

null

, then
this method will behave as if the group descriptor contained
the name of the default activation group implementation class.

Note that if your application creates its own custom
activation group, a security manager must be set for that
group. Otherwise objects cannot be activated in the group.

SecurityManager

is set by default.

If a security manager is already set in the group VM, this
method first calls the security manager's

checkSetFactory

method. This could result in a

SecurityException

. If your application needs to
set a different security manager, you must ensure that the
policy file specified by the group's

ActivationGroupDesc

grants the group the necessary
permissions to set a new security manager. (Note: This will be
necessary if your group downloads and sets a security manager).

After the group is created, the

ActivationSystem

is informed that the group is
active by calling the

activeGroup

method which
returns the

ActivationMonitor

for the group. The
application need not call

activeGroup

independently since it is taken care of by this method.

Once a group is created, subsequent calls to the

currentGroupID

method will return the identifier
for this group until the group becomes inactive.

If the group class name specified in the

ActivationGroupDesc

is

null

, then
this method will behave as if the group descriptor contained
the name of the default activation group implementation class.

Note that if your application creates its own custom
activation group, a security manager must be set for that
group. Otherwise objects cannot be activated in the group.

SecurityManager

is set by default.

If a security manager is already set in the group VM, this
method first calls the security manager's

checkSetFactory

method. This could result in a

SecurityException

. If your application needs to
set a different security manager, you must ensure that the
policy file specified by the group's

ActivationGroupDesc

grants the group the necessary
permissions to set a new security manager. (Note: This will be
necessary if your group downloads and sets a security manager).

After the group is created, the

ActivationSystem

is informed that the group is
active by calling the

activeGroup

method which
returns the

ActivationMonitor

for the group. The
application need not call

activeGroup

independently since it is taken care of by this method.

Once a group is created, subsequent calls to the

currentGroupID

method will return the identifier
for this group until the group becomes inactive.

Note that if your application creates its own custom
activation group, a security manager must be set for that
group. Otherwise objects cannot be activated in the group.

SecurityManager

is set by default.

If a security manager is already set in the group VM, this
method first calls the security manager's

checkSetFactory

method. This could result in a

SecurityException

. If your application needs to
set a different security manager, you must ensure that the
policy file specified by the group's

ActivationGroupDesc

grants the group the necessary
permissions to set a new security manager. (Note: This will be
necessary if your group downloads and sets a security manager).

After the group is created, the

ActivationSystem

is informed that the group is
active by calling the

activeGroup

method which
returns the

ActivationMonitor

for the group. The
application need not call

activeGroup

independently since it is taken care of by this method.

Once a group is created, subsequent calls to the

currentGroupID

method will return the identifier
for this group until the group becomes inactive.

If a security manager is already set in the group VM, this
method first calls the security manager's

checkSetFactory

method. This could result in a

SecurityException

. If your application needs to
set a different security manager, you must ensure that the
policy file specified by the group's

ActivationGroupDesc

grants the group the necessary
permissions to set a new security manager. (Note: This will be
necessary if your group downloads and sets a security manager).

After the group is created, the

ActivationSystem

is informed that the group is
active by calling the

activeGroup

method which
returns the

ActivationMonitor

for the group. The
application need not call

activeGroup

independently since it is taken care of by this method.

Once a group is created, subsequent calls to the

currentGroupID

method will return the identifier
for this group until the group becomes inactive.

After the group is created, the

ActivationSystem

is informed that the group is
active by calling the

activeGroup

method which
returns the

ActivationMonitor

for the group. The
application need not call

activeGroup

independently since it is taken care of by this method.

Once a group is created, subsequent calls to the

currentGroupID

method will return the identifier
for this group until the group becomes inactive.

Once a group is created, subsequent calls to the

currentGroupID

method will return the identifier
for this group until the group becomes inactive.

currentGroupID

```java
public static
ActivationGroupID
currentGroupID()
```

Returns the current activation group's identifier. Returns null
if no group is currently active for this VM.

**Returns:** the activation group's identifier
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

---

#### currentGroupID

public static

ActivationGroupID

currentGroupID()

Returns the current activation group's identifier. Returns null
if no group is currently active for this VM.

setSystem

```java
public static void setSystem​(
ActivationSystem
system)
throws
ActivationException
```

Set the activation system for the VM. The activation system can
only be set it if no group is currently active. If the activation
system is not set via this call, then the

getSystem

method attempts to obtain a reference to the

ActivationSystem

by looking up the name
"java.rmi.activation.ActivationSystem" in the Activator's
registry. By default, the port number used to look up the
activation system is defined by

ActivationSystem.SYSTEM_PORT

. This port can be overridden
by setting the property

java.rmi.activation.port

.

If there is a security manager, this method first
calls the security manager's

checkSetFactory

method.
This could result in a SecurityException.

**Parameters:** system

- remote reference to the

ActivationSystem
**Throws:** ActivationException

- if activation system is already set
**Throws:** SecurityException

- if permission to set the activation system is denied.
(Note: The default implementation of the security manager

checkSetFactory

method requires the RuntimePermission "setFactory")
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2
**See Also:** getSystem()

,

SecurityManager.checkSetFactory()

---

#### setSystem

public static void setSystem​(

ActivationSystem

system)
throws

ActivationException

Set the activation system for the VM. The activation system can
only be set it if no group is currently active. If the activation
system is not set via this call, then the

getSystem

method attempts to obtain a reference to the

ActivationSystem

by looking up the name
"java.rmi.activation.ActivationSystem" in the Activator's
registry. By default, the port number used to look up the
activation system is defined by

ActivationSystem.SYSTEM_PORT

. This port can be overridden
by setting the property

java.rmi.activation.port

.

If there is a security manager, this method first
calls the security manager's

checkSetFactory

method.
This could result in a SecurityException.

If there is a security manager, this method first
calls the security manager's

checkSetFactory

method.
This could result in a SecurityException.

getSystem

```java
public static
ActivationSystem
getSystem()
throws
ActivationException
```

Returns the activation system for the VM. The activation system
may be set by the

setSystem

method. If the
activation system is not set via the

setSystem

method, then the

getSystem

method attempts to
obtain a reference to the

ActivationSystem

by
looking up the name "java.rmi.activation.ActivationSystem" in
the Activator's registry. By default, the port number used to
look up the activation system is defined by

ActivationSystem.SYSTEM_PORT

. This port can be
overridden by setting the property

java.rmi.activation.port

.

**Returns:** the activation system for the VM/group
**Throws:** ActivationException

- if activation system cannot be
obtained or is not bound
(means that it is not running)
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2
**See Also:** setSystem(java.rmi.activation.ActivationSystem)

---

#### getSystem

public static

ActivationSystem

getSystem()
throws

ActivationException

Returns the activation system for the VM. The activation system
may be set by the

setSystem

method. If the
activation system is not set via the

setSystem

method, then the

getSystem

method attempts to
obtain a reference to the

ActivationSystem

by
looking up the name "java.rmi.activation.ActivationSystem" in
the Activator's registry. By default, the port number used to
look up the activation system is defined by

ActivationSystem.SYSTEM_PORT

. This port can be
overridden by setting the property

java.rmi.activation.port

.

activeObject

```java
protected void activeObject​(
ActivationID
id,

MarshalledObject
<? extends
Remote
> mobj)
throws
ActivationException
,

UnknownObjectException
,

RemoteException
```

This protected method is necessary for subclasses to
make the

activeObject

callback to the group's
monitor. The call is simply forwarded to the group's

ActivationMonitor

.

**Parameters:** id

- the object's identifier
**Parameters:** mobj

- a marshalled object containing the remote object's stub
**Throws:** UnknownObjectException

- if object is not registered
**Throws:** RemoteException

- if call informing monitor fails
**Throws:** ActivationException

- if an activation error occurs
**Since:** 1.2

---

#### activeObject

protected void activeObject​(

ActivationID

id,

MarshalledObject

<? extends

Remote

> mobj)
throws

ActivationException

,

UnknownObjectException

,

RemoteException

This protected method is necessary for subclasses to
make the

activeObject

callback to the group's
monitor. The call is simply forwarded to the group's

ActivationMonitor

.

inactiveGroup

```java
protected void inactiveGroup()
throws
UnknownGroupException
,

RemoteException
```

This protected method is necessary for subclasses to
make the

inactiveGroup

callback to the group's
monitor. The call is simply forwarded to the group's

ActivationMonitor

. Also, the current group
for the VM is set to null.

**Throws:** UnknownGroupException

- if group is not registered
**Throws:** RemoteException

- if call informing monitor fails
**Since:** 1.2

---

#### inactiveGroup

protected void inactiveGroup()
throws

UnknownGroupException

,

RemoteException

This protected method is necessary for subclasses to
make the

inactiveGroup

callback to the group's
monitor. The call is simply forwarded to the group's

ActivationMonitor

. Also, the current group
for the VM is set to null.

---

