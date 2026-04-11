# Interface ActivationMonitor

**Source:** `java.rmi\java\rmi\activation\ActivationMonitor.html`

### Class Description

```java
public interface
ActivationMonitor

extends
Remote
```

An

ActivationMonitor

is specific to an

ActivationGroup

and is obtained when a group is
reported active via a call to

ActivationSystem.activeGroup

(this is done
internally). An activation group is responsible for informing its

ActivationMonitor

when either: its objects become active or
inactive, or the group as a whole becomes inactive.

**All Superinterfaces:** Remote

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void inactiveObject​(
ActivationID
id)
throws
UnknownObjectException
,

RemoteException

An activation group calls its monitor's

inactiveObject

method when an object in its group
becomes inactive (deactivates). An activation group discovers
that an object (that it participated in activating) in its VM
is no longer active, via calls to the activation group's

inactiveObject

method.

The

inactiveObject

call informs the

ActivationMonitor

that the remote object reference
it holds for the object with the activation identifier,

id

, is no longer valid. The monitor considers the
reference associated with

id

as a stale reference.
Since the reference is considered stale, a subsequent

activate

call for the same activation identifier
results in re-activating the remote object.

**Parameters:**
- id

- the object's activation identifier

**Throws:**
- UnknownObjectException

- if object is unknown
- RemoteException

- if remote call fails

**Since:**
- 1.2

---

#### void activeObject​(
ActivationID
id,

MarshalledObject
<? extends
Remote
> obj)
throws
UnknownObjectException
,

RemoteException

Informs that an object is now active. An

ActivationGroup

informs its monitor if an object in its group becomes active by
other means than being activated directly (i.e., the object
is registered and "activated" itself).

**Parameters:**
- id

- the active object's id
- obj

- the marshalled form of the object's stub

**Throws:**
- UnknownObjectException

- if object is unknown
- RemoteException

- if remote call fails

**Since:**
- 1.2

---

#### void inactiveGroup​(
ActivationGroupID
id,
long incarnation)
throws
UnknownGroupException
,

RemoteException

Informs that the group is now inactive. The group will be
recreated upon a subsequent request to activate an object
within the group. A group becomes inactive when all objects
in the group report that they are inactive.

**Parameters:**
- id

- the group's id
- incarnation

- the group's incarnation number

**Throws:**
- UnknownGroupException

- if group is unknown
- RemoteException

- if remote call fails

**Since:**
- 1.2

---

### Additional Sections

#### Interface ActivationMonitor

**All Superinterfaces:** Remote

```java
public interface
ActivationMonitor

extends
Remote
```

An

ActivationMonitor

is specific to an

ActivationGroup

and is obtained when a group is
reported active via a call to

ActivationSystem.activeGroup

(this is done
internally). An activation group is responsible for informing its

ActivationMonitor

when either: its objects become active or
inactive, or the group as a whole becomes inactive.

**Since:** 1.2
**See Also:** Activator

,

ActivationSystem

,

ActivationGroup

public interface

ActivationMonitor

extends

Remote

An

ActivationMonitor

is specific to an

ActivationGroup

and is obtained when a group is
reported active via a call to

ActivationSystem.activeGroup

(this is done
internally). An activation group is responsible for informing its

ActivationMonitor

when either: its objects become active or
inactive, or the group as a whole becomes inactive.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

activeObject

​(

ActivationID

id,

MarshalledObject

<? extends

Remote

> obj)

Informs that an object is now active.

void

inactiveGroup

​(

ActivationGroupID

id,
long incarnation)

Informs that the group is now inactive.

void

inactiveObject

​(

ActivationID

id)

An activation group calls its monitor's

inactiveObject

method when an object in its group
becomes inactive (deactivates).

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

activeObject

​(

ActivationID

id,

MarshalledObject

<? extends

Remote

> obj)

Informs that an object is now active.

void

inactiveGroup

​(

ActivationGroupID

id,
long incarnation)

Informs that the group is now inactive.

void

inactiveObject

​(

ActivationID

id)

An activation group calls its monitor's

inactiveObject

method when an object in its group
becomes inactive (deactivates).

---

#### Method Summary

Informs that an object is now active.

Informs that the group is now inactive.

An activation group calls its monitor's

inactiveObject

method when an object in its group
becomes inactive (deactivates).

============ METHOD DETAIL ==========

- Method Detail

- inactiveObject

```java
void inactiveObject​(
ActivationID
id)
throws
UnknownObjectException
,

RemoteException
```

An activation group calls its monitor's

inactiveObject

method when an object in its group
becomes inactive (deactivates). An activation group discovers
that an object (that it participated in activating) in its VM
is no longer active, via calls to the activation group's

inactiveObject

method.

The

inactiveObject

call informs the

ActivationMonitor

that the remote object reference
it holds for the object with the activation identifier,

id

, is no longer valid. The monitor considers the
reference associated with

id

as a stale reference.
Since the reference is considered stale, a subsequent

activate

call for the same activation identifier
results in re-activating the remote object.

**Parameters:** id

- the object's activation identifier
**Throws:** UnknownObjectException

- if object is unknown
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2

- activeObject

```java
void activeObject​(
ActivationID
id,

MarshalledObject
<? extends
Remote
> obj)
throws
UnknownObjectException
,

RemoteException
```

Informs that an object is now active. An

ActivationGroup

informs its monitor if an object in its group becomes active by
other means than being activated directly (i.e., the object
is registered and "activated" itself).

**Parameters:** id

- the active object's id
**Parameters:** obj

- the marshalled form of the object's stub
**Throws:** UnknownObjectException

- if object is unknown
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2

- inactiveGroup

```java
void inactiveGroup​(
ActivationGroupID
id,
long incarnation)
throws
UnknownGroupException
,

RemoteException
```

Informs that the group is now inactive. The group will be
recreated upon a subsequent request to activate an object
within the group. A group becomes inactive when all objects
in the group report that they are inactive.

**Parameters:** id

- the group's id
**Parameters:** incarnation

- the group's incarnation number
**Throws:** UnknownGroupException

- if group is unknown
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2

Method Detail

- inactiveObject

```java
void inactiveObject​(
ActivationID
id)
throws
UnknownObjectException
,

RemoteException
```

An activation group calls its monitor's

inactiveObject

method when an object in its group
becomes inactive (deactivates). An activation group discovers
that an object (that it participated in activating) in its VM
is no longer active, via calls to the activation group's

inactiveObject

method.

The

inactiveObject

call informs the

ActivationMonitor

that the remote object reference
it holds for the object with the activation identifier,

id

, is no longer valid. The monitor considers the
reference associated with

id

as a stale reference.
Since the reference is considered stale, a subsequent

activate

call for the same activation identifier
results in re-activating the remote object.

**Parameters:** id

- the object's activation identifier
**Throws:** UnknownObjectException

- if object is unknown
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2

- activeObject

```java
void activeObject​(
ActivationID
id,

MarshalledObject
<? extends
Remote
> obj)
throws
UnknownObjectException
,

RemoteException
```

Informs that an object is now active. An

ActivationGroup

informs its monitor if an object in its group becomes active by
other means than being activated directly (i.e., the object
is registered and "activated" itself).

**Parameters:** id

- the active object's id
**Parameters:** obj

- the marshalled form of the object's stub
**Throws:** UnknownObjectException

- if object is unknown
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2

- inactiveGroup

```java
void inactiveGroup​(
ActivationGroupID
id,
long incarnation)
throws
UnknownGroupException
,

RemoteException
```

Informs that the group is now inactive. The group will be
recreated upon a subsequent request to activate an object
within the group. A group becomes inactive when all objects
in the group report that they are inactive.

**Parameters:** id

- the group's id
**Parameters:** incarnation

- the group's incarnation number
**Throws:** UnknownGroupException

- if group is unknown
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2

---

#### Method Detail

inactiveObject

```java
void inactiveObject​(
ActivationID
id)
throws
UnknownObjectException
,

RemoteException
```

An activation group calls its monitor's

inactiveObject

method when an object in its group
becomes inactive (deactivates). An activation group discovers
that an object (that it participated in activating) in its VM
is no longer active, via calls to the activation group's

inactiveObject

method.

The

inactiveObject

call informs the

ActivationMonitor

that the remote object reference
it holds for the object with the activation identifier,

id

, is no longer valid. The monitor considers the
reference associated with

id

as a stale reference.
Since the reference is considered stale, a subsequent

activate

call for the same activation identifier
results in re-activating the remote object.

**Parameters:** id

- the object's activation identifier
**Throws:** UnknownObjectException

- if object is unknown
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2

---

#### inactiveObject

void inactiveObject​(

ActivationID

id)
throws

UnknownObjectException

,

RemoteException

An activation group calls its monitor's

inactiveObject

method when an object in its group
becomes inactive (deactivates). An activation group discovers
that an object (that it participated in activating) in its VM
is no longer active, via calls to the activation group's

inactiveObject

method.

The

inactiveObject

call informs the

ActivationMonitor

that the remote object reference
it holds for the object with the activation identifier,

id

, is no longer valid. The monitor considers the
reference associated with

id

as a stale reference.
Since the reference is considered stale, a subsequent

activate

call for the same activation identifier
results in re-activating the remote object.

The

inactiveObject

call informs the

ActivationMonitor

that the remote object reference
it holds for the object with the activation identifier,

id

, is no longer valid. The monitor considers the
reference associated with

id

as a stale reference.
Since the reference is considered stale, a subsequent

activate

call for the same activation identifier
results in re-activating the remote object.

activeObject

```java
void activeObject​(
ActivationID
id,

MarshalledObject
<? extends
Remote
> obj)
throws
UnknownObjectException
,

RemoteException
```

Informs that an object is now active. An

ActivationGroup

informs its monitor if an object in its group becomes active by
other means than being activated directly (i.e., the object
is registered and "activated" itself).

**Parameters:** id

- the active object's id
**Parameters:** obj

- the marshalled form of the object's stub
**Throws:** UnknownObjectException

- if object is unknown
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2

---

#### activeObject

void activeObject​(

ActivationID

id,

MarshalledObject

<? extends

Remote

> obj)
throws

UnknownObjectException

,

RemoteException

Informs that an object is now active. An

ActivationGroup

informs its monitor if an object in its group becomes active by
other means than being activated directly (i.e., the object
is registered and "activated" itself).

inactiveGroup

```java
void inactiveGroup​(
ActivationGroupID
id,
long incarnation)
throws
UnknownGroupException
,

RemoteException
```

Informs that the group is now inactive. The group will be
recreated upon a subsequent request to activate an object
within the group. A group becomes inactive when all objects
in the group report that they are inactive.

**Parameters:** id

- the group's id
**Parameters:** incarnation

- the group's incarnation number
**Throws:** UnknownGroupException

- if group is unknown
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2

---

#### inactiveGroup

void inactiveGroup​(

ActivationGroupID

id,
long incarnation)
throws

UnknownGroupException

,

RemoteException

Informs that the group is now inactive. The group will be
recreated upon a subsequent request to activate an object
within the group. A group becomes inactive when all objects
in the group report that they are inactive.

---

