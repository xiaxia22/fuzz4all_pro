# Interface NamespaceChangeListener

**Source:** `java.naming\javax\naming\event\NamespaceChangeListener.html`

### Class Description

```java
public interface
NamespaceChangeListener

extends
NamingListener
```

Specifies the methods that a listener interested in namespace changes
must implement.
Specifically, the listener is interested in

NamingEvent

s
with event types of

OBJECT_ADDED, OBJECT_RENAMED

, or

OBJECT_REMOVED

.

Such a listener must:

- Implement this interface and its methods.

Implement

NamingListener.namingExceptionThrown()

so that
it will be notified of exceptions thrown while attempting to
collect information about the events.

Register with the source using the source's

addNamingListener()

method.

A listener that wants to be notified of

OBJECT_CHANGED

event types
should also implement the

ObjectChangeListener

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

#### void objectAdded​(
NamingEvent
evt)

Called when an object has been added.

The binding of the newly added object can be obtained using

evt.getNewBinding()

.

**Parameters:**
- evt

- The nonnull event.

**See Also:**
- NamingEvent.OBJECT_ADDED

---

#### void objectRemoved​(
NamingEvent
evt)

Called when an object has been removed.

The binding of the newly removed object can be obtained using

evt.getOldBinding()

.

**Parameters:**
- evt

- The nonnull event.

**See Also:**
- NamingEvent.OBJECT_REMOVED

---

#### void objectRenamed​(
NamingEvent
evt)

Called when an object has been renamed.

The binding of the renamed object can be obtained using

evt.getNewBinding()

. Its old binding (before the rename)
can be obtained using

evt.getOldBinding()

.
One of these may be null if the old/new binding was outside the
scope in which the listener has registered interest.

**Parameters:**
- evt

- The nonnull event.

**See Also:**
- NamingEvent.OBJECT_RENAMED

---

### Additional Sections

#### Interface NamespaceChangeListener

**All Superinterfaces:** EventListener

,

NamingListener

```java
public interface
NamespaceChangeListener

extends
NamingListener
```

Specifies the methods that a listener interested in namespace changes
must implement.
Specifically, the listener is interested in

NamingEvent

s
with event types of

OBJECT_ADDED, OBJECT_RENAMED

, or

OBJECT_REMOVED

.

Such a listener must:

- Implement this interface and its methods.

Implement

NamingListener.namingExceptionThrown()

so that
it will be notified of exceptions thrown while attempting to
collect information about the events.

Register with the source using the source's

addNamingListener()

method.

A listener that wants to be notified of

OBJECT_CHANGED

event types
should also implement the

ObjectChangeListener

interface.

**Since:** 1.3
**See Also:** NamingEvent

,

ObjectChangeListener

,

EventContext

,

EventDirContext

public interface

NamespaceChangeListener

extends

NamingListener

Specifies the methods that a listener interested in namespace changes
must implement.
Specifically, the listener is interested in

NamingEvent

s
with event types of

OBJECT_ADDED, OBJECT_RENAMED

, or

OBJECT_REMOVED

.

Such a listener must:

- Implement this interface and its methods.

Implement

NamingListener.namingExceptionThrown()

so that
it will be notified of exceptions thrown while attempting to
collect information about the events.

Register with the source using the source's

addNamingListener()

method.

A listener that wants to be notified of

OBJECT_CHANGED

event types
should also implement the

ObjectChangeListener

interface.

Such a listener must:

- Implement this interface and its methods.

Implement

NamingListener.namingExceptionThrown()

so that
it will be notified of exceptions thrown while attempting to
collect information about the events.

Register with the source using the source's

addNamingListener()

method.

A listener that wants to be notified of

OBJECT_CHANGED

event types
should also implement the

ObjectChangeListener

interface.

Implement this interface and its methods.

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

objectAdded

​(

NamingEvent

evt)

Called when an object has been added.

void

objectRemoved

​(

NamingEvent

evt)

Called when an object has been removed.

void

objectRenamed

​(

NamingEvent

evt)

Called when an object has been renamed.

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

objectAdded

​(

NamingEvent

evt)

Called when an object has been added.

void

objectRemoved

​(

NamingEvent

evt)

Called when an object has been removed.

void

objectRenamed

​(

NamingEvent

evt)

Called when an object has been renamed.

- Methods declared in interface javax.naming.event.

NamingListener

namingExceptionThrown

---

#### Method Summary

Called when an object has been added.

Called when an object has been removed.

Called when an object has been renamed.

Methods declared in interface javax.naming.event.

NamingListener

namingExceptionThrown

---

#### Methods declared in interface javax.naming.event. NamingListener

============ METHOD DETAIL ==========

- Method Detail

- objectAdded

```java
void objectAdded​(
NamingEvent
evt)
```

Called when an object has been added.

The binding of the newly added object can be obtained using

evt.getNewBinding()

.

**Parameters:** evt

- The nonnull event.
**See Also:** NamingEvent.OBJECT_ADDED

- objectRemoved

```java
void objectRemoved​(
NamingEvent
evt)
```

Called when an object has been removed.

The binding of the newly removed object can be obtained using

evt.getOldBinding()

.

**Parameters:** evt

- The nonnull event.
**See Also:** NamingEvent.OBJECT_REMOVED

- objectRenamed

```java
void objectRenamed​(
NamingEvent
evt)
```

Called when an object has been renamed.

The binding of the renamed object can be obtained using

evt.getNewBinding()

. Its old binding (before the rename)
can be obtained using

evt.getOldBinding()

.
One of these may be null if the old/new binding was outside the
scope in which the listener has registered interest.

**Parameters:** evt

- The nonnull event.
**See Also:** NamingEvent.OBJECT_RENAMED

Method Detail

- objectAdded

```java
void objectAdded​(
NamingEvent
evt)
```

Called when an object has been added.

The binding of the newly added object can be obtained using

evt.getNewBinding()

.

**Parameters:** evt

- The nonnull event.
**See Also:** NamingEvent.OBJECT_ADDED

- objectRemoved

```java
void objectRemoved​(
NamingEvent
evt)
```

Called when an object has been removed.

The binding of the newly removed object can be obtained using

evt.getOldBinding()

.

**Parameters:** evt

- The nonnull event.
**See Also:** NamingEvent.OBJECT_REMOVED

- objectRenamed

```java
void objectRenamed​(
NamingEvent
evt)
```

Called when an object has been renamed.

The binding of the renamed object can be obtained using

evt.getNewBinding()

. Its old binding (before the rename)
can be obtained using

evt.getOldBinding()

.
One of these may be null if the old/new binding was outside the
scope in which the listener has registered interest.

**Parameters:** evt

- The nonnull event.
**See Also:** NamingEvent.OBJECT_RENAMED

---

#### Method Detail

objectAdded

```java
void objectAdded​(
NamingEvent
evt)
```

Called when an object has been added.

The binding of the newly added object can be obtained using

evt.getNewBinding()

.

**Parameters:** evt

- The nonnull event.
**See Also:** NamingEvent.OBJECT_ADDED

---

#### objectAdded

void objectAdded​(

NamingEvent

evt)

Called when an object has been added.

The binding of the newly added object can be obtained using

evt.getNewBinding()

.

The binding of the newly added object can be obtained using

evt.getNewBinding()

.

objectRemoved

```java
void objectRemoved​(
NamingEvent
evt)
```

Called when an object has been removed.

The binding of the newly removed object can be obtained using

evt.getOldBinding()

.

**Parameters:** evt

- The nonnull event.
**See Also:** NamingEvent.OBJECT_REMOVED

---

#### objectRemoved

void objectRemoved​(

NamingEvent

evt)

Called when an object has been removed.

The binding of the newly removed object can be obtained using

evt.getOldBinding()

.

The binding of the newly removed object can be obtained using

evt.getOldBinding()

.

objectRenamed

```java
void objectRenamed​(
NamingEvent
evt)
```

Called when an object has been renamed.

The binding of the renamed object can be obtained using

evt.getNewBinding()

. Its old binding (before the rename)
can be obtained using

evt.getOldBinding()

.
One of these may be null if the old/new binding was outside the
scope in which the listener has registered interest.

**Parameters:** evt

- The nonnull event.
**See Also:** NamingEvent.OBJECT_RENAMED

---

#### objectRenamed

void objectRenamed​(

NamingEvent

evt)

Called when an object has been renamed.

The binding of the renamed object can be obtained using

evt.getNewBinding()

. Its old binding (before the rename)
can be obtained using

evt.getOldBinding()

.
One of these may be null if the old/new binding was outside the
scope in which the listener has registered interest.

The binding of the renamed object can be obtained using

evt.getNewBinding()

. Its old binding (before the rename)
can be obtained using

evt.getOldBinding()

.
One of these may be null if the old/new binding was outside the
scope in which the listener has registered interest.

---

