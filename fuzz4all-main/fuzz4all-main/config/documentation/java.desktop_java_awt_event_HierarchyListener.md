# Interface HierarchyListener

**Source:** `java.desktop\java\awt\event\HierarchyListener.html`

### Class Description

```java
public interface
HierarchyListener

extends
EventListener
```

The listener interface for receiving hierarchy changed events.
The class that is interested in processing a hierarchy changed event
should implement this interface.
The listener object created from that class is then registered with a
Component using the Component's

addHierarchyListener

method. When the hierarchy to which the Component belongs changes, the

hierarchyChanged

method in the listener object is invoked,
and the

HierarchyEvent

is passed to it.

Hierarchy events are provided for notification purposes ONLY;
The AWT will automatically handle changes to the hierarchy internally so
that GUI layout, displayability, and visibility work properly regardless
of whether a program registers a

HierarchyListener

or not.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void hierarchyChanged​(
HierarchyEvent
e)

Called when the hierarchy has been changed. To discern the actual
type of change, call

HierarchyEvent.getChangeFlags()

.

**Parameters:**
- e

- the event to be processed

**See Also:**
- HierarchyEvent.getChangeFlags()

---

### Additional Sections

#### Interface HierarchyListener

**All Superinterfaces:** EventListener

**All Known Implementing Classes:** AWTEventMulticaster

```java
public interface
HierarchyListener

extends
EventListener
```

The listener interface for receiving hierarchy changed events.
The class that is interested in processing a hierarchy changed event
should implement this interface.
The listener object created from that class is then registered with a
Component using the Component's

addHierarchyListener

method. When the hierarchy to which the Component belongs changes, the

hierarchyChanged

method in the listener object is invoked,
and the

HierarchyEvent

is passed to it.

Hierarchy events are provided for notification purposes ONLY;
The AWT will automatically handle changes to the hierarchy internally so
that GUI layout, displayability, and visibility work properly regardless
of whether a program registers a

HierarchyListener

or not.

**Since:** 1.3
**See Also:** HierarchyEvent

public interface

HierarchyListener

extends

EventListener

The listener interface for receiving hierarchy changed events.
The class that is interested in processing a hierarchy changed event
should implement this interface.
The listener object created from that class is then registered with a
Component using the Component's

addHierarchyListener

method. When the hierarchy to which the Component belongs changes, the

hierarchyChanged

method in the listener object is invoked,
and the

HierarchyEvent

is passed to it.

Hierarchy events are provided for notification purposes ONLY;
The AWT will automatically handle changes to the hierarchy internally so
that GUI layout, displayability, and visibility work properly regardless
of whether a program registers a

HierarchyListener

or not.

Hierarchy events are provided for notification purposes ONLY;
The AWT will automatically handle changes to the hierarchy internally so
that GUI layout, displayability, and visibility work properly regardless
of whether a program registers a

HierarchyListener

or not.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

hierarchyChanged

​(

HierarchyEvent

e)

Called when the hierarchy has been changed.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

hierarchyChanged

​(

HierarchyEvent

e)

Called when the hierarchy has been changed.

---

#### Method Summary

Called when the hierarchy has been changed.

============ METHOD DETAIL ==========

- Method Detail

- hierarchyChanged

```java
void hierarchyChanged​(
HierarchyEvent
e)
```

Called when the hierarchy has been changed. To discern the actual
type of change, call

HierarchyEvent.getChangeFlags()

.

**Parameters:** e

- the event to be processed
**See Also:** HierarchyEvent.getChangeFlags()

Method Detail

- hierarchyChanged

```java
void hierarchyChanged​(
HierarchyEvent
e)
```

Called when the hierarchy has been changed. To discern the actual
type of change, call

HierarchyEvent.getChangeFlags()

.

**Parameters:** e

- the event to be processed
**See Also:** HierarchyEvent.getChangeFlags()

---

#### Method Detail

hierarchyChanged

```java
void hierarchyChanged​(
HierarchyEvent
e)
```

Called when the hierarchy has been changed. To discern the actual
type of change, call

HierarchyEvent.getChangeFlags()

.

**Parameters:** e

- the event to be processed
**See Also:** HierarchyEvent.getChangeFlags()

---

#### hierarchyChanged

void hierarchyChanged​(

HierarchyEvent

e)

Called when the hierarchy has been changed. To discern the actual
type of change, call

HierarchyEvent.getChangeFlags()

.

---

