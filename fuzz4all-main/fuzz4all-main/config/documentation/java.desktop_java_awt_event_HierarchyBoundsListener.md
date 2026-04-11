# Interface HierarchyBoundsListener

**Source:** `java.desktop\java\awt\event\HierarchyBoundsListener.html`

### Class Description

```java
public interface
HierarchyBoundsListener

extends
EventListener
```

The listener interface for receiving ancestor moved and resized events.
The class that is interested in processing these events either implements
this interface (and all the methods it contains) or extends the abstract

HierarchyBoundsAdapter

class (overriding only the method of
interest).
The listener object created from that class is then registered with a
Component using the Component's

addHierarchyBoundsListener

method. When the hierarchy to which the Component belongs changes by
the resizing or movement of an ancestor, the relevant method in the listener
object is invoked, and the

HierarchyEvent

is passed to it.

Hierarchy events are provided for notification purposes ONLY;
The AWT will automatically handle changes to the hierarchy internally so
that GUI layout works properly regardless of whether a
program registers an

HierarchyBoundsListener

or not.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void ancestorMoved​(
HierarchyEvent
e)

Called when an ancestor of the source is moved.

**Parameters:**
- e

- the event to be processed

---

#### void ancestorResized​(
HierarchyEvent
e)

Called when an ancestor of the source is resized.

**Parameters:**
- e

- the event to be processed

---

### Additional Sections

#### Interface HierarchyBoundsListener

**All Superinterfaces:** EventListener

**All Known Implementing Classes:** AWTEventMulticaster

,

HierarchyBoundsAdapter

```java
public interface
HierarchyBoundsListener

extends
EventListener
```

The listener interface for receiving ancestor moved and resized events.
The class that is interested in processing these events either implements
this interface (and all the methods it contains) or extends the abstract

HierarchyBoundsAdapter

class (overriding only the method of
interest).
The listener object created from that class is then registered with a
Component using the Component's

addHierarchyBoundsListener

method. When the hierarchy to which the Component belongs changes by
the resizing or movement of an ancestor, the relevant method in the listener
object is invoked, and the

HierarchyEvent

is passed to it.

Hierarchy events are provided for notification purposes ONLY;
The AWT will automatically handle changes to the hierarchy internally so
that GUI layout works properly regardless of whether a
program registers an

HierarchyBoundsListener

or not.

**Since:** 1.3
**See Also:** HierarchyBoundsAdapter

,

HierarchyEvent

public interface

HierarchyBoundsListener

extends

EventListener

The listener interface for receiving ancestor moved and resized events.
The class that is interested in processing these events either implements
this interface (and all the methods it contains) or extends the abstract

HierarchyBoundsAdapter

class (overriding only the method of
interest).
The listener object created from that class is then registered with a
Component using the Component's

addHierarchyBoundsListener

method. When the hierarchy to which the Component belongs changes by
the resizing or movement of an ancestor, the relevant method in the listener
object is invoked, and the

HierarchyEvent

is passed to it.

Hierarchy events are provided for notification purposes ONLY;
The AWT will automatically handle changes to the hierarchy internally so
that GUI layout works properly regardless of whether a
program registers an

HierarchyBoundsListener

or not.

Hierarchy events are provided for notification purposes ONLY;
The AWT will automatically handle changes to the hierarchy internally so
that GUI layout works properly regardless of whether a
program registers an

HierarchyBoundsListener

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

ancestorMoved

​(

HierarchyEvent

e)

Called when an ancestor of the source is moved.

void

ancestorResized

​(

HierarchyEvent

e)

Called when an ancestor of the source is resized.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

ancestorMoved

​(

HierarchyEvent

e)

Called when an ancestor of the source is moved.

void

ancestorResized

​(

HierarchyEvent

e)

Called when an ancestor of the source is resized.

---

#### Method Summary

Called when an ancestor of the source is moved.

Called when an ancestor of the source is resized.

============ METHOD DETAIL ==========

- Method Detail

- ancestorMoved

```java
void ancestorMoved​(
HierarchyEvent
e)
```

Called when an ancestor of the source is moved.

**Parameters:** e

- the event to be processed

- ancestorResized

```java
void ancestorResized​(
HierarchyEvent
e)
```

Called when an ancestor of the source is resized.

**Parameters:** e

- the event to be processed

Method Detail

- ancestorMoved

```java
void ancestorMoved​(
HierarchyEvent
e)
```

Called when an ancestor of the source is moved.

**Parameters:** e

- the event to be processed

- ancestorResized

```java
void ancestorResized​(
HierarchyEvent
e)
```

Called when an ancestor of the source is resized.

**Parameters:** e

- the event to be processed

---

#### Method Detail

ancestorMoved

```java
void ancestorMoved​(
HierarchyEvent
e)
```

Called when an ancestor of the source is moved.

**Parameters:** e

- the event to be processed

---

#### ancestorMoved

void ancestorMoved​(

HierarchyEvent

e)

Called when an ancestor of the source is moved.

ancestorResized

```java
void ancestorResized​(
HierarchyEvent
e)
```

Called when an ancestor of the source is resized.

**Parameters:** e

- the event to be processed

---

#### ancestorResized

void ancestorResized​(

HierarchyEvent

e)

Called when an ancestor of the source is resized.

---

