# Interface ActivationSystem

**Source:** `java.rmi\java\rmi\activation\ActivationSystem.html`

### Class Description

```java
public interface
ActivationSystem

extends
Remote
```

The

ActivationSystem

provides a means for registering
groups and "activatable" objects to be activated within those groups.
The

ActivationSystem

works closely with the

Activator

, which activates objects registered via the

ActivationSystem

, and the

ActivationMonitor

,
which obtains information about active and inactive objects,
and inactive groups.

**All Superinterfaces:** Remote

---

### Field Details

#### static final int SYSTEM_PORT

The port to lookup the activation system.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### ActivationID
registerObject​(
ActivationDesc
desc)
throws
ActivationException
,

UnknownGroupException
,

RemoteException

The

registerObject

method is used to register an
activation descriptor,

desc

, and obtain an
activation identifier for a activatable remote object. The

ActivationSystem

creates an

ActivationID

(a activation identifier) for the
object specified by the descriptor,

desc

, and
records, in stable storage, the activation descriptor and its
associated identifier for later use. When the

Activator

receives an

activate

request for a specific identifier, it
looks up the activation descriptor (registered previously) for
the specified identifier and uses that information to activate
the object.

**Parameters:**
- desc

- the object's activation descriptor

**Returns:**
- the activation id that can be used to activate the object

**Throws:**
- ActivationException

- if registration fails (e.g., database
update failure, etc).
- UnknownGroupException

- if group referred to in

desc

is not registered with this system
- RemoteException

- if remote call fails

**Since:**
- 1.2

---

#### void unregisterObject​(
ActivationID
id)
throws
ActivationException
,

UnknownObjectException
,

RemoteException

Remove the activation id and associated descriptor previously
registered with the

ActivationSystem

; the object
can no longer be activated via the object's activation id.

**Parameters:**
- id

- the object's activation id (from previous registration)

**Throws:**
- ActivationException

- if unregister fails (e.g., database
update failure, etc).
- UnknownObjectException

- if object is unknown (not registered)
- RemoteException

- if remote call fails

**Since:**
- 1.2

---

#### ActivationGroupID
registerGroup​(
ActivationGroupDesc
desc)
throws
ActivationException
,

RemoteException

Register the activation group. An activation group must be
registered with the

ActivationSystem

before objects
can be registered within that group.

**Parameters:**
- desc

- the group's descriptor

**Returns:**
- an identifier for the group

**Throws:**
- ActivationException

- if group registration fails
- RemoteException

- if remote call fails

**Since:**
- 1.2

---

#### ActivationMonitor
activeGroup​(
ActivationGroupID
id,

ActivationInstantiator
group,
long incarnation)
throws
UnknownGroupException
,

ActivationException
,

RemoteException

Callback to inform activation system that group is now
active. This call is made internally by the

ActivationGroup.createGroup

method to inform
the

ActivationSystem

that the group is now
active.

**Parameters:**
- id

- the activation group's identifier
- group

- the group's instantiator
- incarnation

- the group's incarnation number

**Returns:**
- monitor for activation group

**Throws:**
- UnknownGroupException

- if group is not registered
- ActivationException

- if a group for the specified

id

is already active and that group is not equal
to the specified

group

or that group has a different

incarnation

than the specified

group
- RemoteException

- if remote call fails

**Since:**
- 1.2

---

#### void unregisterGroup​(
ActivationGroupID
id)
throws
ActivationException
,

UnknownGroupException
,

RemoteException

Remove the activation group. An activation group makes this call back
to inform the activator that the group should be removed (destroyed).
If this call completes successfully, objects can no longer be
registered or activated within the group. All information of the
group and its associated objects is removed from the system.

**Parameters:**
- id

- the activation group's identifier

**Throws:**
- ActivationException

- if unregister fails (e.g., database
update failure, etc).
- UnknownGroupException

- if group is not registered
- RemoteException

- if remote call fails

**Since:**
- 1.2

---

#### void shutdown()
throws
RemoteException

Shutdown the activation system. Destroys all groups spawned by
the activation daemon and exits the activation daemon.

**Throws:**
- RemoteException

- if failed to contact/shutdown the activation
daemon

**Since:**
- 1.2

---

#### ActivationDesc
setActivationDesc​(
ActivationID
id,

ActivationDesc
desc)
throws
ActivationException
,

UnknownObjectException
,

UnknownGroupException
,

RemoteException

Set the activation descriptor,

desc

for the object with
the activation identifier,

id

. The change will take
effect upon subsequent activation of the object.

**Parameters:**
- id

- the activation identifier for the activatable object
- desc

- the activation descriptor for the activatable object

**Returns:**
- the previous value of the activation descriptor

**Throws:**
- UnknownGroupException

- the group associated with

desc

is not a registered group
- UnknownObjectException

- the activation

id

is not registered
- ActivationException

- for general failure (e.g., unable
to update log)
- RemoteException

- if remote call fails

**See Also:**
- getActivationDesc(java.rmi.activation.ActivationID)

**Since:**
- 1.2

---

#### ActivationGroupDesc
setActivationGroupDesc​(
ActivationGroupID
id,

ActivationGroupDesc
desc)
throws
ActivationException
,

UnknownGroupException
,

RemoteException

Set the activation group descriptor,

desc

for the object
with the activation group identifier,

id

. The change will
take effect upon subsequent activation of the group.

**Parameters:**
- id

- the activation group identifier for the activation group
- desc

- the activation group descriptor for the activation group

**Returns:**
- the previous value of the activation group descriptor

**Throws:**
- UnknownGroupException

- the group associated with

id

is not a registered group
- ActivationException

- for general failure (e.g., unable
to update log)
- RemoteException

- if remote call fails

**See Also:**
- getActivationGroupDesc(java.rmi.activation.ActivationGroupID)

**Since:**
- 1.2

---

#### ActivationDesc
getActivationDesc​(
ActivationID
id)
throws
ActivationException
,

UnknownObjectException
,

RemoteException

Returns the activation descriptor, for the object with the activation
identifier,

id

.

**Parameters:**
- id

- the activation identifier for the activatable object

**Returns:**
- the activation descriptor

**Throws:**
- UnknownObjectException

- if

id

is not registered
- ActivationException

- for general failure
- RemoteException

- if remote call fails

**See Also:**
- setActivationDesc(java.rmi.activation.ActivationID, java.rmi.activation.ActivationDesc)

**Since:**
- 1.2

---

#### ActivationGroupDesc
getActivationGroupDesc​(
ActivationGroupID
id)
throws
ActivationException
,

UnknownGroupException
,

RemoteException

Returns the activation group descriptor, for the group
with the activation group identifier,

id

.

**Parameters:**
- id

- the activation group identifier for the group

**Returns:**
- the activation group descriptor

**Throws:**
- UnknownGroupException

- if

id

is not registered
- ActivationException

- for general failure
- RemoteException

- if remote call fails

**See Also:**
- setActivationGroupDesc(java.rmi.activation.ActivationGroupID, java.rmi.activation.ActivationGroupDesc)

**Since:**
- 1.2

---

### Additional Sections

#### Interface ActivationSystem

**All Superinterfaces:** Remote

```java
public interface
ActivationSystem

extends
Remote
```

The

ActivationSystem

provides a means for registering
groups and "activatable" objects to be activated within those groups.
The

ActivationSystem

works closely with the

Activator

, which activates objects registered via the

ActivationSystem

, and the

ActivationMonitor

,
which obtains information about active and inactive objects,
and inactive groups.

**Since:** 1.2
**See Also:** Activator

,

ActivationMonitor

public interface

ActivationSystem

extends

Remote

The

ActivationSystem

provides a means for registering
groups and "activatable" objects to be activated within those groups.
The

ActivationSystem

works closely with the

Activator

, which activates objects registered via the

ActivationSystem

, and the

ActivationMonitor

,
which obtains information about active and inactive objects,
and inactive groups.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

SYSTEM_PORT

The port to lookup the activation system.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ActivationMonitor

activeGroup

​(

ActivationGroupID

id,

ActivationInstantiator

group,
long incarnation)

Callback to inform activation system that group is now
active.

ActivationDesc

getActivationDesc

​(

ActivationID

id)

Returns the activation descriptor, for the object with the activation
identifier,

id

.

ActivationGroupDesc

getActivationGroupDesc

​(

ActivationGroupID

id)

Returns the activation group descriptor, for the group
with the activation group identifier,

id

.

ActivationGroupID

registerGroup

​(

ActivationGroupDesc

desc)

Register the activation group.

ActivationID

registerObject

​(

ActivationDesc

desc)

The

registerObject

method is used to register an
activation descriptor,

desc

, and obtain an
activation identifier for a activatable remote object.

ActivationDesc

setActivationDesc

​(

ActivationID

id,

ActivationDesc

desc)

Set the activation descriptor,

desc

for the object with
the activation identifier,

id

.

ActivationGroupDesc

setActivationGroupDesc

​(

ActivationGroupID

id,

ActivationGroupDesc

desc)

Set the activation group descriptor,

desc

for the object
with the activation group identifier,

id

.

void

shutdown

()

Shutdown the activation system.

void

unregisterGroup

​(

ActivationGroupID

id)

Remove the activation group.

void

unregisterObject

​(

ActivationID

id)

Remove the activation id and associated descriptor previously
registered with the

ActivationSystem

; the object
can no longer be activated via the object's activation id.

Field Summary

Fields

Modifier and Type

Field

Description

static int

SYSTEM_PORT

The port to lookup the activation system.

---

#### Field Summary

The port to lookup the activation system.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ActivationMonitor

activeGroup

​(

ActivationGroupID

id,

ActivationInstantiator

group,
long incarnation)

Callback to inform activation system that group is now
active.

ActivationDesc

getActivationDesc

​(

ActivationID

id)

Returns the activation descriptor, for the object with the activation
identifier,

id

.

ActivationGroupDesc

getActivationGroupDesc

​(

ActivationGroupID

id)

Returns the activation group descriptor, for the group
with the activation group identifier,

id

.

ActivationGroupID

registerGroup

​(

ActivationGroupDesc

desc)

Register the activation group.

ActivationID

registerObject

​(

ActivationDesc

desc)

The

registerObject

method is used to register an
activation descriptor,

desc

, and obtain an
activation identifier for a activatable remote object.

ActivationDesc

setActivationDesc

​(

ActivationID

id,

ActivationDesc

desc)

Set the activation descriptor,

desc

for the object with
the activation identifier,

id

.

ActivationGroupDesc

setActivationGroupDesc

​(

ActivationGroupID

id,

ActivationGroupDesc

desc)

Set the activation group descriptor,

desc

for the object
with the activation group identifier,

id

.

void

shutdown

()

Shutdown the activation system.

void

unregisterGroup

​(

ActivationGroupID

id)

Remove the activation group.

void

unregisterObject

​(

ActivationID

id)

Remove the activation id and associated descriptor previously
registered with the

ActivationSystem

; the object
can no longer be activated via the object's activation id.

---

#### Method Summary

Callback to inform activation system that group is now
active.

Returns the activation descriptor, for the object with the activation
identifier,

id

.

Returns the activation group descriptor, for the group
with the activation group identifier,

id

.

Register the activation group.

The

registerObject

method is used to register an
activation descriptor,

desc

, and obtain an
activation identifier for a activatable remote object.

Set the activation descriptor,

desc

for the object with
the activation identifier,

id

.

Set the activation group descriptor,

desc

for the object
with the activation group identifier,

id

.

Shutdown the activation system.

Remove the activation group.

Remove the activation id and associated descriptor previously
registered with the

ActivationSystem

; the object
can no longer be activated via the object's activation id.

============ FIELD DETAIL ===========

- Field Detail

- SYSTEM_PORT

```java
static final int SYSTEM_PORT
```

The port to lookup the activation system.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- registerObject

```java
ActivationID
registerObject​(
ActivationDesc
desc)
throws
ActivationException
,

UnknownGroupException
,

RemoteException
```

The

registerObject

method is used to register an
activation descriptor,

desc

, and obtain an
activation identifier for a activatable remote object. The

ActivationSystem

creates an

ActivationID

(a activation identifier) for the
object specified by the descriptor,

desc

, and
records, in stable storage, the activation descriptor and its
associated identifier for later use. When the

Activator

receives an

activate

request for a specific identifier, it
looks up the activation descriptor (registered previously) for
the specified identifier and uses that information to activate
the object.

**Parameters:** desc

- the object's activation descriptor
**Returns:** the activation id that can be used to activate the object
**Throws:** ActivationException

- if registration fails (e.g., database
update failure, etc).
**Throws:** UnknownGroupException

- if group referred to in

desc

is not registered with this system
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2

- unregisterObject

```java
void unregisterObject​(
ActivationID
id)
throws
ActivationException
,

UnknownObjectException
,

RemoteException
```

Remove the activation id and associated descriptor previously
registered with the

ActivationSystem

; the object
can no longer be activated via the object's activation id.

**Parameters:** id

- the object's activation id (from previous registration)
**Throws:** ActivationException

- if unregister fails (e.g., database
update failure, etc).
**Throws:** UnknownObjectException

- if object is unknown (not registered)
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2

- registerGroup

```java
ActivationGroupID
registerGroup​(
ActivationGroupDesc
desc)
throws
ActivationException
,

RemoteException
```

Register the activation group. An activation group must be
registered with the

ActivationSystem

before objects
can be registered within that group.

**Parameters:** desc

- the group's descriptor
**Returns:** an identifier for the group
**Throws:** ActivationException

- if group registration fails
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2

- activeGroup

```java
ActivationMonitor
activeGroup​(
ActivationGroupID
id,

ActivationInstantiator
group,
long incarnation)
throws
UnknownGroupException
,

ActivationException
,

RemoteException
```

Callback to inform activation system that group is now
active. This call is made internally by the

ActivationGroup.createGroup

method to inform
the

ActivationSystem

that the group is now
active.

**Parameters:** id

- the activation group's identifier
**Parameters:** group

- the group's instantiator
**Parameters:** incarnation

- the group's incarnation number
**Returns:** monitor for activation group
**Throws:** UnknownGroupException

- if group is not registered
**Throws:** ActivationException

- if a group for the specified

id

is already active and that group is not equal
to the specified

group

or that group has a different

incarnation

than the specified

group
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2

- unregisterGroup

```java
void unregisterGroup​(
ActivationGroupID
id)
throws
ActivationException
,

UnknownGroupException
,

RemoteException
```

Remove the activation group. An activation group makes this call back
to inform the activator that the group should be removed (destroyed).
If this call completes successfully, objects can no longer be
registered or activated within the group. All information of the
group and its associated objects is removed from the system.

**Parameters:** id

- the activation group's identifier
**Throws:** ActivationException

- if unregister fails (e.g., database
update failure, etc).
**Throws:** UnknownGroupException

- if group is not registered
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2

- shutdown

```java
void shutdown()
throws
RemoteException
```

Shutdown the activation system. Destroys all groups spawned by
the activation daemon and exits the activation daemon.

**Throws:** RemoteException

- if failed to contact/shutdown the activation
daemon
**Since:** 1.2

- setActivationDesc

```java
ActivationDesc
setActivationDesc​(
ActivationID
id,

ActivationDesc
desc)
throws
ActivationException
,

UnknownObjectException
,

UnknownGroupException
,

RemoteException
```

Set the activation descriptor,

desc

for the object with
the activation identifier,

id

. The change will take
effect upon subsequent activation of the object.

**Parameters:** id

- the activation identifier for the activatable object
**Parameters:** desc

- the activation descriptor for the activatable object
**Returns:** the previous value of the activation descriptor
**Throws:** UnknownGroupException

- the group associated with

desc

is not a registered group
**Throws:** UnknownObjectException

- the activation

id

is not registered
**Throws:** ActivationException

- for general failure (e.g., unable
to update log)
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2
**See Also:** getActivationDesc(java.rmi.activation.ActivationID)

- setActivationGroupDesc

```java
ActivationGroupDesc
setActivationGroupDesc​(
ActivationGroupID
id,

ActivationGroupDesc
desc)
throws
ActivationException
,

UnknownGroupException
,

RemoteException
```

Set the activation group descriptor,

desc

for the object
with the activation group identifier,

id

. The change will
take effect upon subsequent activation of the group.

**Parameters:** id

- the activation group identifier for the activation group
**Parameters:** desc

- the activation group descriptor for the activation group
**Returns:** the previous value of the activation group descriptor
**Throws:** UnknownGroupException

- the group associated with

id

is not a registered group
**Throws:** ActivationException

- for general failure (e.g., unable
to update log)
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2
**See Also:** getActivationGroupDesc(java.rmi.activation.ActivationGroupID)

- getActivationDesc

```java
ActivationDesc
getActivationDesc​(
ActivationID
id)
throws
ActivationException
,

UnknownObjectException
,

RemoteException
```

Returns the activation descriptor, for the object with the activation
identifier,

id

.

**Parameters:** id

- the activation identifier for the activatable object
**Returns:** the activation descriptor
**Throws:** UnknownObjectException

- if

id

is not registered
**Throws:** ActivationException

- for general failure
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2
**See Also:** setActivationDesc(java.rmi.activation.ActivationID, java.rmi.activation.ActivationDesc)

- getActivationGroupDesc

```java
ActivationGroupDesc
getActivationGroupDesc​(
ActivationGroupID
id)
throws
ActivationException
,

UnknownGroupException
,

RemoteException
```

Returns the activation group descriptor, for the group
with the activation group identifier,

id

.

**Parameters:** id

- the activation group identifier for the group
**Returns:** the activation group descriptor
**Throws:** UnknownGroupException

- if

id

is not registered
**Throws:** ActivationException

- for general failure
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2
**See Also:** setActivationGroupDesc(java.rmi.activation.ActivationGroupID, java.rmi.activation.ActivationGroupDesc)

Field Detail

- SYSTEM_PORT

```java
static final int SYSTEM_PORT
```

The port to lookup the activation system.

**See Also:** Constant Field Values

---

#### Field Detail

SYSTEM_PORT

```java
static final int SYSTEM_PORT
```

The port to lookup the activation system.

**See Also:** Constant Field Values

---

#### SYSTEM_PORT

static final int SYSTEM_PORT

The port to lookup the activation system.

Method Detail

- registerObject

```java
ActivationID
registerObject​(
ActivationDesc
desc)
throws
ActivationException
,

UnknownGroupException
,

RemoteException
```

The

registerObject

method is used to register an
activation descriptor,

desc

, and obtain an
activation identifier for a activatable remote object. The

ActivationSystem

creates an

ActivationID

(a activation identifier) for the
object specified by the descriptor,

desc

, and
records, in stable storage, the activation descriptor and its
associated identifier for later use. When the

Activator

receives an

activate

request for a specific identifier, it
looks up the activation descriptor (registered previously) for
the specified identifier and uses that information to activate
the object.

**Parameters:** desc

- the object's activation descriptor
**Returns:** the activation id that can be used to activate the object
**Throws:** ActivationException

- if registration fails (e.g., database
update failure, etc).
**Throws:** UnknownGroupException

- if group referred to in

desc

is not registered with this system
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2

- unregisterObject

```java
void unregisterObject​(
ActivationID
id)
throws
ActivationException
,

UnknownObjectException
,

RemoteException
```

Remove the activation id and associated descriptor previously
registered with the

ActivationSystem

; the object
can no longer be activated via the object's activation id.

**Parameters:** id

- the object's activation id (from previous registration)
**Throws:** ActivationException

- if unregister fails (e.g., database
update failure, etc).
**Throws:** UnknownObjectException

- if object is unknown (not registered)
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2

- registerGroup

```java
ActivationGroupID
registerGroup​(
ActivationGroupDesc
desc)
throws
ActivationException
,

RemoteException
```

Register the activation group. An activation group must be
registered with the

ActivationSystem

before objects
can be registered within that group.

**Parameters:** desc

- the group's descriptor
**Returns:** an identifier for the group
**Throws:** ActivationException

- if group registration fails
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2

- activeGroup

```java
ActivationMonitor
activeGroup​(
ActivationGroupID
id,

ActivationInstantiator
group,
long incarnation)
throws
UnknownGroupException
,

ActivationException
,

RemoteException
```

Callback to inform activation system that group is now
active. This call is made internally by the

ActivationGroup.createGroup

method to inform
the

ActivationSystem

that the group is now
active.

**Parameters:** id

- the activation group's identifier
**Parameters:** group

- the group's instantiator
**Parameters:** incarnation

- the group's incarnation number
**Returns:** monitor for activation group
**Throws:** UnknownGroupException

- if group is not registered
**Throws:** ActivationException

- if a group for the specified

id

is already active and that group is not equal
to the specified

group

or that group has a different

incarnation

than the specified

group
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2

- unregisterGroup

```java
void unregisterGroup​(
ActivationGroupID
id)
throws
ActivationException
,

UnknownGroupException
,

RemoteException
```

Remove the activation group. An activation group makes this call back
to inform the activator that the group should be removed (destroyed).
If this call completes successfully, objects can no longer be
registered or activated within the group. All information of the
group and its associated objects is removed from the system.

**Parameters:** id

- the activation group's identifier
**Throws:** ActivationException

- if unregister fails (e.g., database
update failure, etc).
**Throws:** UnknownGroupException

- if group is not registered
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2

- shutdown

```java
void shutdown()
throws
RemoteException
```

Shutdown the activation system. Destroys all groups spawned by
the activation daemon and exits the activation daemon.

**Throws:** RemoteException

- if failed to contact/shutdown the activation
daemon
**Since:** 1.2

- setActivationDesc

```java
ActivationDesc
setActivationDesc​(
ActivationID
id,

ActivationDesc
desc)
throws
ActivationException
,

UnknownObjectException
,

UnknownGroupException
,

RemoteException
```

Set the activation descriptor,

desc

for the object with
the activation identifier,

id

. The change will take
effect upon subsequent activation of the object.

**Parameters:** id

- the activation identifier for the activatable object
**Parameters:** desc

- the activation descriptor for the activatable object
**Returns:** the previous value of the activation descriptor
**Throws:** UnknownGroupException

- the group associated with

desc

is not a registered group
**Throws:** UnknownObjectException

- the activation

id

is not registered
**Throws:** ActivationException

- for general failure (e.g., unable
to update log)
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2
**See Also:** getActivationDesc(java.rmi.activation.ActivationID)

- setActivationGroupDesc

```java
ActivationGroupDesc
setActivationGroupDesc​(
ActivationGroupID
id,

ActivationGroupDesc
desc)
throws
ActivationException
,

UnknownGroupException
,

RemoteException
```

Set the activation group descriptor,

desc

for the object
with the activation group identifier,

id

. The change will
take effect upon subsequent activation of the group.

**Parameters:** id

- the activation group identifier for the activation group
**Parameters:** desc

- the activation group descriptor for the activation group
**Returns:** the previous value of the activation group descriptor
**Throws:** UnknownGroupException

- the group associated with

id

is not a registered group
**Throws:** ActivationException

- for general failure (e.g., unable
to update log)
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2
**See Also:** getActivationGroupDesc(java.rmi.activation.ActivationGroupID)

- getActivationDesc

```java
ActivationDesc
getActivationDesc​(
ActivationID
id)
throws
ActivationException
,

UnknownObjectException
,

RemoteException
```

Returns the activation descriptor, for the object with the activation
identifier,

id

.

**Parameters:** id

- the activation identifier for the activatable object
**Returns:** the activation descriptor
**Throws:** UnknownObjectException

- if

id

is not registered
**Throws:** ActivationException

- for general failure
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2
**See Also:** setActivationDesc(java.rmi.activation.ActivationID, java.rmi.activation.ActivationDesc)

- getActivationGroupDesc

```java
ActivationGroupDesc
getActivationGroupDesc​(
ActivationGroupID
id)
throws
ActivationException
,

UnknownGroupException
,

RemoteException
```

Returns the activation group descriptor, for the group
with the activation group identifier,

id

.

**Parameters:** id

- the activation group identifier for the group
**Returns:** the activation group descriptor
**Throws:** UnknownGroupException

- if

id

is not registered
**Throws:** ActivationException

- for general failure
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2
**See Also:** setActivationGroupDesc(java.rmi.activation.ActivationGroupID, java.rmi.activation.ActivationGroupDesc)

---

#### Method Detail

registerObject

```java
ActivationID
registerObject​(
ActivationDesc
desc)
throws
ActivationException
,

UnknownGroupException
,

RemoteException
```

The

registerObject

method is used to register an
activation descriptor,

desc

, and obtain an
activation identifier for a activatable remote object. The

ActivationSystem

creates an

ActivationID

(a activation identifier) for the
object specified by the descriptor,

desc

, and
records, in stable storage, the activation descriptor and its
associated identifier for later use. When the

Activator

receives an

activate

request for a specific identifier, it
looks up the activation descriptor (registered previously) for
the specified identifier and uses that information to activate
the object.

**Parameters:** desc

- the object's activation descriptor
**Returns:** the activation id that can be used to activate the object
**Throws:** ActivationException

- if registration fails (e.g., database
update failure, etc).
**Throws:** UnknownGroupException

- if group referred to in

desc

is not registered with this system
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2

---

#### registerObject

ActivationID

registerObject​(

ActivationDesc

desc)
throws

ActivationException

,

UnknownGroupException

,

RemoteException

The

registerObject

method is used to register an
activation descriptor,

desc

, and obtain an
activation identifier for a activatable remote object. The

ActivationSystem

creates an

ActivationID

(a activation identifier) for the
object specified by the descriptor,

desc

, and
records, in stable storage, the activation descriptor and its
associated identifier for later use. When the

Activator

receives an

activate

request for a specific identifier, it
looks up the activation descriptor (registered previously) for
the specified identifier and uses that information to activate
the object.

unregisterObject

```java
void unregisterObject​(
ActivationID
id)
throws
ActivationException
,

UnknownObjectException
,

RemoteException
```

Remove the activation id and associated descriptor previously
registered with the

ActivationSystem

; the object
can no longer be activated via the object's activation id.

**Parameters:** id

- the object's activation id (from previous registration)
**Throws:** ActivationException

- if unregister fails (e.g., database
update failure, etc).
**Throws:** UnknownObjectException

- if object is unknown (not registered)
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2

---

#### unregisterObject

void unregisterObject​(

ActivationID

id)
throws

ActivationException

,

UnknownObjectException

,

RemoteException

Remove the activation id and associated descriptor previously
registered with the

ActivationSystem

; the object
can no longer be activated via the object's activation id.

registerGroup

```java
ActivationGroupID
registerGroup​(
ActivationGroupDesc
desc)
throws
ActivationException
,

RemoteException
```

Register the activation group. An activation group must be
registered with the

ActivationSystem

before objects
can be registered within that group.

**Parameters:** desc

- the group's descriptor
**Returns:** an identifier for the group
**Throws:** ActivationException

- if group registration fails
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2

---

#### registerGroup

ActivationGroupID

registerGroup​(

ActivationGroupDesc

desc)
throws

ActivationException

,

RemoteException

Register the activation group. An activation group must be
registered with the

ActivationSystem

before objects
can be registered within that group.

activeGroup

```java
ActivationMonitor
activeGroup​(
ActivationGroupID
id,

ActivationInstantiator
group,
long incarnation)
throws
UnknownGroupException
,

ActivationException
,

RemoteException
```

Callback to inform activation system that group is now
active. This call is made internally by the

ActivationGroup.createGroup

method to inform
the

ActivationSystem

that the group is now
active.

**Parameters:** id

- the activation group's identifier
**Parameters:** group

- the group's instantiator
**Parameters:** incarnation

- the group's incarnation number
**Returns:** monitor for activation group
**Throws:** UnknownGroupException

- if group is not registered
**Throws:** ActivationException

- if a group for the specified

id

is already active and that group is not equal
to the specified

group

or that group has a different

incarnation

than the specified

group
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2

---

#### activeGroup

ActivationMonitor

activeGroup​(

ActivationGroupID

id,

ActivationInstantiator

group,
long incarnation)
throws

UnknownGroupException

,

ActivationException

,

RemoteException

Callback to inform activation system that group is now
active. This call is made internally by the

ActivationGroup.createGroup

method to inform
the

ActivationSystem

that the group is now
active.

unregisterGroup

```java
void unregisterGroup​(
ActivationGroupID
id)
throws
ActivationException
,

UnknownGroupException
,

RemoteException
```

Remove the activation group. An activation group makes this call back
to inform the activator that the group should be removed (destroyed).
If this call completes successfully, objects can no longer be
registered or activated within the group. All information of the
group and its associated objects is removed from the system.

**Parameters:** id

- the activation group's identifier
**Throws:** ActivationException

- if unregister fails (e.g., database
update failure, etc).
**Throws:** UnknownGroupException

- if group is not registered
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2

---

#### unregisterGroup

void unregisterGroup​(

ActivationGroupID

id)
throws

ActivationException

,

UnknownGroupException

,

RemoteException

Remove the activation group. An activation group makes this call back
to inform the activator that the group should be removed (destroyed).
If this call completes successfully, objects can no longer be
registered or activated within the group. All information of the
group and its associated objects is removed from the system.

shutdown

```java
void shutdown()
throws
RemoteException
```

Shutdown the activation system. Destroys all groups spawned by
the activation daemon and exits the activation daemon.

**Throws:** RemoteException

- if failed to contact/shutdown the activation
daemon
**Since:** 1.2

---

#### shutdown

void shutdown()
throws

RemoteException

Shutdown the activation system. Destroys all groups spawned by
the activation daemon and exits the activation daemon.

setActivationDesc

```java
ActivationDesc
setActivationDesc​(
ActivationID
id,

ActivationDesc
desc)
throws
ActivationException
,

UnknownObjectException
,

UnknownGroupException
,

RemoteException
```

Set the activation descriptor,

desc

for the object with
the activation identifier,

id

. The change will take
effect upon subsequent activation of the object.

**Parameters:** id

- the activation identifier for the activatable object
**Parameters:** desc

- the activation descriptor for the activatable object
**Returns:** the previous value of the activation descriptor
**Throws:** UnknownGroupException

- the group associated with

desc

is not a registered group
**Throws:** UnknownObjectException

- the activation

id

is not registered
**Throws:** ActivationException

- for general failure (e.g., unable
to update log)
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2
**See Also:** getActivationDesc(java.rmi.activation.ActivationID)

---

#### setActivationDesc

ActivationDesc

setActivationDesc​(

ActivationID

id,

ActivationDesc

desc)
throws

ActivationException

,

UnknownObjectException

,

UnknownGroupException

,

RemoteException

Set the activation descriptor,

desc

for the object with
the activation identifier,

id

. The change will take
effect upon subsequent activation of the object.

setActivationGroupDesc

```java
ActivationGroupDesc
setActivationGroupDesc​(
ActivationGroupID
id,

ActivationGroupDesc
desc)
throws
ActivationException
,

UnknownGroupException
,

RemoteException
```

Set the activation group descriptor,

desc

for the object
with the activation group identifier,

id

. The change will
take effect upon subsequent activation of the group.

**Parameters:** id

- the activation group identifier for the activation group
**Parameters:** desc

- the activation group descriptor for the activation group
**Returns:** the previous value of the activation group descriptor
**Throws:** UnknownGroupException

- the group associated with

id

is not a registered group
**Throws:** ActivationException

- for general failure (e.g., unable
to update log)
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2
**See Also:** getActivationGroupDesc(java.rmi.activation.ActivationGroupID)

---

#### setActivationGroupDesc

ActivationGroupDesc

setActivationGroupDesc​(

ActivationGroupID

id,

ActivationGroupDesc

desc)
throws

ActivationException

,

UnknownGroupException

,

RemoteException

Set the activation group descriptor,

desc

for the object
with the activation group identifier,

id

. The change will
take effect upon subsequent activation of the group.

getActivationDesc

```java
ActivationDesc
getActivationDesc​(
ActivationID
id)
throws
ActivationException
,

UnknownObjectException
,

RemoteException
```

Returns the activation descriptor, for the object with the activation
identifier,

id

.

**Parameters:** id

- the activation identifier for the activatable object
**Returns:** the activation descriptor
**Throws:** UnknownObjectException

- if

id

is not registered
**Throws:** ActivationException

- for general failure
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2
**See Also:** setActivationDesc(java.rmi.activation.ActivationID, java.rmi.activation.ActivationDesc)

---

#### getActivationDesc

ActivationDesc

getActivationDesc​(

ActivationID

id)
throws

ActivationException

,

UnknownObjectException

,

RemoteException

Returns the activation descriptor, for the object with the activation
identifier,

id

.

getActivationGroupDesc

```java
ActivationGroupDesc
getActivationGroupDesc​(
ActivationGroupID
id)
throws
ActivationException
,

UnknownGroupException
,

RemoteException
```

Returns the activation group descriptor, for the group
with the activation group identifier,

id

.

**Parameters:** id

- the activation group identifier for the group
**Returns:** the activation group descriptor
**Throws:** UnknownGroupException

- if

id

is not registered
**Throws:** ActivationException

- for general failure
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2
**See Also:** setActivationGroupDesc(java.rmi.activation.ActivationGroupID, java.rmi.activation.ActivationGroupDesc)

---

#### getActivationGroupDesc

ActivationGroupDesc

getActivationGroupDesc​(

ActivationGroupID

id)
throws

ActivationException

,

UnknownGroupException

,

RemoteException

Returns the activation group descriptor, for the group
with the activation group identifier,

id

.

---

