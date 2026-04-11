# Interface Activator

**Source:** `java.rmi\java\rmi\activation\Activator.html`

### Class Description

```java
public interface
Activator

extends
Remote
```

The

Activator

facilitates remote object activation. A
"faulting" remote reference calls the activator's

activate

method to obtain a "live" reference to a
"activatable" remote object. Upon receiving a request for activation,
the activator looks up the activation descriptor for the activation
identifier,

id

, determines the group in which the
object should be activated initiates object re-creation via the
group's

ActivationInstantiator

(via a call to the

newInstance

method). The activator initiates the
execution of activation groups as necessary. For example, if an
activation group for a specific group identifier is not already
executing, the activator initiates the execution of a VM for the
group.

The

Activator

works closely with

ActivationSystem

, which provides a means for registering
groups and objects within those groups, and

ActivationMonitor

,
which receives information about active and inactive objects and inactive
groups.

The activator is responsible for monitoring and detecting when
activation groups fail so that it can remove stale remote references
to groups and active object's within those groups.

**All Superinterfaces:** Remote

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### MarshalledObject
<? extends
Remote
> activate​(
ActivationID
id,
boolean force)
throws
ActivationException
,

UnknownObjectException
,

RemoteException

Activate the object associated with the activation identifier,

id

. If the activator knows the object to be active
already, and

force

is false , the stub with a
"live" reference is returned immediately to the caller;
otherwise, if the activator does not know that corresponding
the remote object is active, the activator uses the activation
descriptor information (previously registered) to determine the
group (VM) in which the object should be activated. If an

ActivationInstantiator

corresponding to the
object's group descriptor already exists, the activator invokes
the activation group's

newInstance

method passing
it the object's id and descriptor.

If the activation group for the object's group descriptor does
not yet exist, the activator starts an

ActivationInstantiator

executing (by spawning a
child process, for example). When the activator receives the
activation group's call back (via the

ActivationSystem

's

activeGroup

method) specifying the activation group's reference, the
activator can then invoke that activation instantiator's

newInstance

method to forward each pending
activation request to the activation group and return the
result (a marshalled remote object reference, a stub) to the
caller.

Note that the activator receives a "marshalled" object instead of a
Remote object so that the activator does not need to load the
code for that object, or participate in distributed garbage
collection for that object. If the activator kept a strong
reference to the remote object, the activator would then
prevent the object from being garbage collected under the
normal distributed garbage collection mechanism.

**Parameters:**
- id

- the activation identifier for the object being activated
- force

- if true, the activator contacts the group to obtain
the remote object's reference; if false, returning the cached value
is allowed.

**Returns:**
- the remote object (a stub) in a marshalled form

**Throws:**
- ActivationException

- if object activation fails
- UnknownObjectException

- if object is unknown (not registered)
- RemoteException

- if remote call fails

**Since:**
- 1.2

---

### Additional Sections

#### Interface Activator

**All Superinterfaces:** Remote

```java
public interface
Activator

extends
Remote
```

The

Activator

facilitates remote object activation. A
"faulting" remote reference calls the activator's

activate

method to obtain a "live" reference to a
"activatable" remote object. Upon receiving a request for activation,
the activator looks up the activation descriptor for the activation
identifier,

id

, determines the group in which the
object should be activated initiates object re-creation via the
group's

ActivationInstantiator

(via a call to the

newInstance

method). The activator initiates the
execution of activation groups as necessary. For example, if an
activation group for a specific group identifier is not already
executing, the activator initiates the execution of a VM for the
group.

The

Activator

works closely with

ActivationSystem

, which provides a means for registering
groups and objects within those groups, and

ActivationMonitor

,
which receives information about active and inactive objects and inactive
groups.

The activator is responsible for monitoring and detecting when
activation groups fail so that it can remove stale remote references
to groups and active object's within those groups.

**Since:** 1.2
**See Also:** ActivationInstantiator

,

ActivationGroupDesc

,

ActivationGroupID

public interface

Activator

extends

Remote

The

Activator

facilitates remote object activation. A
"faulting" remote reference calls the activator's

activate

method to obtain a "live" reference to a
"activatable" remote object. Upon receiving a request for activation,
the activator looks up the activation descriptor for the activation
identifier,

id

, determines the group in which the
object should be activated initiates object re-creation via the
group's

ActivationInstantiator

(via a call to the

newInstance

method). The activator initiates the
execution of activation groups as necessary. For example, if an
activation group for a specific group identifier is not already
executing, the activator initiates the execution of a VM for the
group.

The

Activator

works closely with

ActivationSystem

, which provides a means for registering
groups and objects within those groups, and

ActivationMonitor

,
which receives information about active and inactive objects and inactive
groups.

The activator is responsible for monitoring and detecting when
activation groups fail so that it can remove stale remote references
to groups and active object's within those groups.

The

Activator

works closely with

ActivationSystem

, which provides a means for registering
groups and objects within those groups, and

ActivationMonitor

,
which receives information about active and inactive objects and inactive
groups.

The activator is responsible for monitoring and detecting when
activation groups fail so that it can remove stale remote references
to groups and active object's within those groups.

The activator is responsible for monitoring and detecting when
activation groups fail so that it can remove stale remote references
to groups and active object's within those groups.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

MarshalledObject

<? extends

Remote

>

activate

​(

ActivationID

id,
boolean force)

Activate the object associated with the activation identifier,

id

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

MarshalledObject

<? extends

Remote

>

activate

​(

ActivationID

id,
boolean force)

Activate the object associated with the activation identifier,

id

.

---

#### Method Summary

Activate the object associated with the activation identifier,

id

.

============ METHOD DETAIL ==========

- Method Detail

- activate

```java
MarshalledObject
<? extends
Remote
> activate​(
ActivationID
id,
boolean force)
throws
ActivationException
,

UnknownObjectException
,

RemoteException
```

Activate the object associated with the activation identifier,

id

. If the activator knows the object to be active
already, and

force

is false , the stub with a
"live" reference is returned immediately to the caller;
otherwise, if the activator does not know that corresponding
the remote object is active, the activator uses the activation
descriptor information (previously registered) to determine the
group (VM) in which the object should be activated. If an

ActivationInstantiator

corresponding to the
object's group descriptor already exists, the activator invokes
the activation group's

newInstance

method passing
it the object's id and descriptor.

If the activation group for the object's group descriptor does
not yet exist, the activator starts an

ActivationInstantiator

executing (by spawning a
child process, for example). When the activator receives the
activation group's call back (via the

ActivationSystem

's

activeGroup

method) specifying the activation group's reference, the
activator can then invoke that activation instantiator's

newInstance

method to forward each pending
activation request to the activation group and return the
result (a marshalled remote object reference, a stub) to the
caller.

Note that the activator receives a "marshalled" object instead of a
Remote object so that the activator does not need to load the
code for that object, or participate in distributed garbage
collection for that object. If the activator kept a strong
reference to the remote object, the activator would then
prevent the object from being garbage collected under the
normal distributed garbage collection mechanism.

**Parameters:** id

- the activation identifier for the object being activated
**Parameters:** force

- if true, the activator contacts the group to obtain
the remote object's reference; if false, returning the cached value
is allowed.
**Returns:** the remote object (a stub) in a marshalled form
**Throws:** ActivationException

- if object activation fails
**Throws:** UnknownObjectException

- if object is unknown (not registered)
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2

Method Detail

- activate

```java
MarshalledObject
<? extends
Remote
> activate​(
ActivationID
id,
boolean force)
throws
ActivationException
,

UnknownObjectException
,

RemoteException
```

Activate the object associated with the activation identifier,

id

. If the activator knows the object to be active
already, and

force

is false , the stub with a
"live" reference is returned immediately to the caller;
otherwise, if the activator does not know that corresponding
the remote object is active, the activator uses the activation
descriptor information (previously registered) to determine the
group (VM) in which the object should be activated. If an

ActivationInstantiator

corresponding to the
object's group descriptor already exists, the activator invokes
the activation group's

newInstance

method passing
it the object's id and descriptor.

If the activation group for the object's group descriptor does
not yet exist, the activator starts an

ActivationInstantiator

executing (by spawning a
child process, for example). When the activator receives the
activation group's call back (via the

ActivationSystem

's

activeGroup

method) specifying the activation group's reference, the
activator can then invoke that activation instantiator's

newInstance

method to forward each pending
activation request to the activation group and return the
result (a marshalled remote object reference, a stub) to the
caller.

Note that the activator receives a "marshalled" object instead of a
Remote object so that the activator does not need to load the
code for that object, or participate in distributed garbage
collection for that object. If the activator kept a strong
reference to the remote object, the activator would then
prevent the object from being garbage collected under the
normal distributed garbage collection mechanism.

**Parameters:** id

- the activation identifier for the object being activated
**Parameters:** force

- if true, the activator contacts the group to obtain
the remote object's reference; if false, returning the cached value
is allowed.
**Returns:** the remote object (a stub) in a marshalled form
**Throws:** ActivationException

- if object activation fails
**Throws:** UnknownObjectException

- if object is unknown (not registered)
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2

---

#### Method Detail

activate

```java
MarshalledObject
<? extends
Remote
> activate​(
ActivationID
id,
boolean force)
throws
ActivationException
,

UnknownObjectException
,

RemoteException
```

Activate the object associated with the activation identifier,

id

. If the activator knows the object to be active
already, and

force

is false , the stub with a
"live" reference is returned immediately to the caller;
otherwise, if the activator does not know that corresponding
the remote object is active, the activator uses the activation
descriptor information (previously registered) to determine the
group (VM) in which the object should be activated. If an

ActivationInstantiator

corresponding to the
object's group descriptor already exists, the activator invokes
the activation group's

newInstance

method passing
it the object's id and descriptor.

If the activation group for the object's group descriptor does
not yet exist, the activator starts an

ActivationInstantiator

executing (by spawning a
child process, for example). When the activator receives the
activation group's call back (via the

ActivationSystem

's

activeGroup

method) specifying the activation group's reference, the
activator can then invoke that activation instantiator's

newInstance

method to forward each pending
activation request to the activation group and return the
result (a marshalled remote object reference, a stub) to the
caller.

Note that the activator receives a "marshalled" object instead of a
Remote object so that the activator does not need to load the
code for that object, or participate in distributed garbage
collection for that object. If the activator kept a strong
reference to the remote object, the activator would then
prevent the object from being garbage collected under the
normal distributed garbage collection mechanism.

**Parameters:** id

- the activation identifier for the object being activated
**Parameters:** force

- if true, the activator contacts the group to obtain
the remote object's reference; if false, returning the cached value
is allowed.
**Returns:** the remote object (a stub) in a marshalled form
**Throws:** ActivationException

- if object activation fails
**Throws:** UnknownObjectException

- if object is unknown (not registered)
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2

---

#### activate

MarshalledObject

<? extends

Remote

> activate​(

ActivationID

id,
boolean force)
throws

ActivationException

,

UnknownObjectException

,

RemoteException

Activate the object associated with the activation identifier,

id

. If the activator knows the object to be active
already, and

force

is false , the stub with a
"live" reference is returned immediately to the caller;
otherwise, if the activator does not know that corresponding
the remote object is active, the activator uses the activation
descriptor information (previously registered) to determine the
group (VM) in which the object should be activated. If an

ActivationInstantiator

corresponding to the
object's group descriptor already exists, the activator invokes
the activation group's

newInstance

method passing
it the object's id and descriptor.

If the activation group for the object's group descriptor does
not yet exist, the activator starts an

ActivationInstantiator

executing (by spawning a
child process, for example). When the activator receives the
activation group's call back (via the

ActivationSystem

's

activeGroup

method) specifying the activation group's reference, the
activator can then invoke that activation instantiator's

newInstance

method to forward each pending
activation request to the activation group and return the
result (a marshalled remote object reference, a stub) to the
caller.

Note that the activator receives a "marshalled" object instead of a
Remote object so that the activator does not need to load the
code for that object, or participate in distributed garbage
collection for that object. If the activator kept a strong
reference to the remote object, the activator would then
prevent the object from being garbage collected under the
normal distributed garbage collection mechanism.

If the activation group for the object's group descriptor does
not yet exist, the activator starts an

ActivationInstantiator

executing (by spawning a
child process, for example). When the activator receives the
activation group's call back (via the

ActivationSystem

's

activeGroup

method) specifying the activation group's reference, the
activator can then invoke that activation instantiator's

newInstance

method to forward each pending
activation request to the activation group and return the
result (a marshalled remote object reference, a stub) to the
caller.

Note that the activator receives a "marshalled" object instead of a
Remote object so that the activator does not need to load the
code for that object, or participate in distributed garbage
collection for that object. If the activator kept a strong
reference to the remote object, the activator would then
prevent the object from being garbage collected under the
normal distributed garbage collection mechanism.

Note that the activator receives a "marshalled" object instead of a
Remote object so that the activator does not need to load the
code for that object, or participate in distributed garbage
collection for that object. If the activator kept a strong
reference to the remote object, the activator would then
prevent the object from being garbage collected under the
normal distributed garbage collection mechanism.

---

