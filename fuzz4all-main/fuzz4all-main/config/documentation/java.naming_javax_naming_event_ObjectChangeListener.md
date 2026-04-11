# Interface ObjectChangeListener

**Source:** `java.naming\javax\naming\event\ObjectChangeListener.html`

### Class Description

```java
public interface
ObjectChangeListener

extends
NamingListener
```

Specifies the method that a listener of a

NamingEvent

with event type of

OBJECT_CHANGED

must implement.

An

OBJECT_CHANGED

event type is fired when (the contents of)
an object has changed. This might mean that its attributes have been modified,
added, or removed, and/or that the object itself has been replaced.
How the object has changed can be determined by examining the

NamingEvent

's old and new bindings.

A listener interested in

OBJECT_CHANGED

event types must:

- Implement this interface and its method (

objectChanged()

)

Implement

NamingListener.namingExceptionThrown()

so that
it will be notified of exceptions thrown while attempting to
collect information about the events.

Register with the source using the source's

addNamingListener()

method.

A listener that wants to be notified of namespace change events
should also implement the

NamespaceChangeListener

interface.

**All Superinterfaces:** EventListener

,

NamingListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void objectChanged​(
NamingEvent
evt)

Called when an object has been changed.

The binding of the changed object can be obtained using

evt.getNewBinding()

. Its old binding (before the change)
can be obtained using

evt.getOldBinding()

.

**Parameters:**
- evt

- The nonnull naming event.

**See Also:**
- NamingEvent.OBJECT_CHANGED

---

### Additional Sections

#### Interface ObjectChangeListener

**All Superinterfaces:** EventListener

,

NamingListener

```java
public interface
ObjectChangeListener

extends
NamingListener
```

Specifies the method that a listener of a

NamingEvent

with event type of

OBJECT_CHANGED

must implement.

An

OBJECT_CHANGED

event type is fired when (the contents of)
an object has changed. This might mean that its attributes have been modified,
added, or removed, and/or that the object itself has been replaced.
How the object has changed can be determined by examining the

NamingEvent

's old and new bindings.

A listener interested in

OBJECT_CHANGED

event types must:

- Implement this interface and its method (

objectChanged()

)

Implement

NamingListener.namingExceptionThrown()

so that
it will be notified of exceptions thrown while attempting to
collect information about the events.

Register with the source using the source's

addNamingListener()

method.

A listener that wants to be notified of namespace change events
should also implement the

NamespaceChangeListener

interface.

**Since:** 1.3
**See Also:** NamingEvent

,

NamespaceChangeListener

,

EventContext

,

EventDirContext

public interface

ObjectChangeListener

extends

NamingListener

Specifies the method that a listener of a

NamingEvent

with event type of

OBJECT_CHANGED

must implement.

An

OBJECT_CHANGED

event type is fired when (the contents of)
an object has changed. This might mean that its attributes have been modified,
added, or removed, and/or that the object itself has been replaced.
How the object has changed can be determined by examining the

NamingEvent

's old and new bindings.

A listener interested in

OBJECT_CHANGED

event types must:

- Implement this interface and its method (

objectChanged()

)

Implement

NamingListener.namingExceptionThrown()

so that
it will be notified of exceptions thrown while attempting to
collect information about the events.

Register with the source using the source's

addNamingListener()

method.

A listener that wants to be notified of namespace change events
should also implement the

NamespaceChangeListener

interface.

An

OBJECT_CHANGED

event type is fired when (the contents of)
an object has changed. This might mean that its attributes have been modified,
added, or removed, and/or that the object itself has been replaced.
How the object has changed can be determined by examining the

NamingEvent

's old and new bindings.

A listener interested in

OBJECT_CHANGED

event types must:

- Implement this interface and its method (

objectChanged()

)

Implement

NamingListener.namingExceptionThrown()

so that
it will be notified of exceptions thrown while attempting to
collect information about the events.

Register with the source using the source's

addNamingListener()

method.

A listener that wants to be notified of namespace change events
should also implement the

NamespaceChangeListener

interface.

A listener interested in

OBJECT_CHANGED

event types must:

- Implement this interface and its method (

objectChanged()

)

Implement

NamingListener.namingExceptionThrown()

so that
it will be notified of exceptions thrown while attempting to
collect information about the events.

Register with the source using the source's

addNamingListener()

method.

A listener that wants to be notified of namespace change events
should also implement the

NamespaceChangeListener

interface.

Implement this interface and its method (

objectChanged()

)

Implement

NamingListener.namingExceptionThrown()

so that
it will be notified of exceptions thrown while attempting to
collect information about the events.

Register with the source using the source's

addNamingListener()

method.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

objectChanged

​(

NamingEvent

evt)

Called when an object has been changed.

- Methods declared in interface javax.naming.event.

NamingListener

namingExceptionThrown

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

objectChanged

​(

NamingEvent

evt)

Called when an object has been changed.

- Methods declared in interface javax.naming.event.

NamingListener

namingExceptionThrown

---

#### Method Summary

Called when an object has been changed.

Methods declared in interface javax.naming.event.

NamingListener

namingExceptionThrown

---

#### Methods declared in interface javax.naming.event. NamingListener

============ METHOD DETAIL ==========

- Method Detail

- objectChanged

```java
void objectChanged​(
NamingEvent
evt)
```

Called when an object has been changed.

The binding of the changed object can be obtained using

evt.getNewBinding()

. Its old binding (before the change)
can be obtained using

evt.getOldBinding()

.

**Parameters:** evt

- The nonnull naming event.
**See Also:** NamingEvent.OBJECT_CHANGED

Method Detail

- objectChanged

```java
void objectChanged​(
NamingEvent
evt)
```

Called when an object has been changed.

The binding of the changed object can be obtained using

evt.getNewBinding()

. Its old binding (before the change)
can be obtained using

evt.getOldBinding()

.

**Parameters:** evt

- The nonnull naming event.
**See Also:** NamingEvent.OBJECT_CHANGED

---

#### Method Detail

objectChanged

```java
void objectChanged​(
NamingEvent
evt)
```

Called when an object has been changed.

The binding of the changed object can be obtained using

evt.getNewBinding()

. Its old binding (before the change)
can be obtained using

evt.getOldBinding()

.

**Parameters:** evt

- The nonnull naming event.
**See Also:** NamingEvent.OBJECT_CHANGED

---

#### objectChanged

void objectChanged​(

NamingEvent

evt)

Called when an object has been changed.

The binding of the changed object can be obtained using

evt.getNewBinding()

. Its old binding (before the change)
can be obtained using

evt.getOldBinding()

.

The binding of the changed object can be obtained using

evt.getNewBinding()

. Its old binding (before the change)
can be obtained using

evt.getOldBinding()

.

---

