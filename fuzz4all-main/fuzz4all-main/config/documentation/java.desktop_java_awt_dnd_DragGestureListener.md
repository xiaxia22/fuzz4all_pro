# Interface DragGestureListener

**Source:** `java.desktop\java\awt\dnd\DragGestureListener.html`

### Class Description

```java
public interface
DragGestureListener

extends
EventListener
```

The listener interface for receiving drag gesture events.
This interface is intended for a drag gesture recognition
implementation. See a specification for

DragGestureRecognizer

for details on how to register the listener interface.
Upon recognition of a drag gesture the

DragGestureRecognizer

calls this interface's

dragGestureRecognized()

method and passes a

DragGestureEvent

.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void dragGestureRecognized​(
DragGestureEvent
dge)

This method is invoked by the

DragGestureRecognizer

when the

DragGestureRecognizer

detects a platform-dependent
drag initiating gesture. To initiate the drag and drop operation,
if appropriate,

startDrag()

method on
the

DragGestureEvent

has to be invoked.

**Parameters:**
- dge

- the

DragGestureEvent

describing
the gesture that has just occurred

**See Also:**
- DragGestureRecognizer

,

DragGestureEvent

---

### Additional Sections

#### Interface DragGestureListener

**All Superinterfaces:** EventListener

```java
public interface
DragGestureListener

extends
EventListener
```

The listener interface for receiving drag gesture events.
This interface is intended for a drag gesture recognition
implementation. See a specification for

DragGestureRecognizer

for details on how to register the listener interface.
Upon recognition of a drag gesture the

DragGestureRecognizer

calls this interface's

dragGestureRecognized()

method and passes a

DragGestureEvent

.

**See Also:** DragGestureRecognizer

,

DragGestureEvent

,

DragSource

public interface

DragGestureListener

extends

EventListener

The listener interface for receiving drag gesture events.
This interface is intended for a drag gesture recognition
implementation. See a specification for

DragGestureRecognizer

for details on how to register the listener interface.
Upon recognition of a drag gesture the

DragGestureRecognizer

calls this interface's

dragGestureRecognized()

method and passes a

DragGestureEvent

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

dragGestureRecognized

​(

DragGestureEvent

dge)

This method is invoked by the

DragGestureRecognizer

when the

DragGestureRecognizer

detects a platform-dependent
drag initiating gesture.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

dragGestureRecognized

​(

DragGestureEvent

dge)

This method is invoked by the

DragGestureRecognizer

when the

DragGestureRecognizer

detects a platform-dependent
drag initiating gesture.

---

#### Method Summary

This method is invoked by the

DragGestureRecognizer

when the

DragGestureRecognizer

detects a platform-dependent
drag initiating gesture.

============ METHOD DETAIL ==========

- Method Detail

- dragGestureRecognized

```java
void dragGestureRecognized​(
DragGestureEvent
dge)
```

This method is invoked by the

DragGestureRecognizer

when the

DragGestureRecognizer

detects a platform-dependent
drag initiating gesture. To initiate the drag and drop operation,
if appropriate,

startDrag()

method on
the

DragGestureEvent

has to be invoked.

**Parameters:** dge

- the

DragGestureEvent

describing
the gesture that has just occurred
**See Also:** DragGestureRecognizer

,

DragGestureEvent

Method Detail

- dragGestureRecognized

```java
void dragGestureRecognized​(
DragGestureEvent
dge)
```

This method is invoked by the

DragGestureRecognizer

when the

DragGestureRecognizer

detects a platform-dependent
drag initiating gesture. To initiate the drag and drop operation,
if appropriate,

startDrag()

method on
the

DragGestureEvent

has to be invoked.

**Parameters:** dge

- the

DragGestureEvent

describing
the gesture that has just occurred
**See Also:** DragGestureRecognizer

,

DragGestureEvent

---

#### Method Detail

dragGestureRecognized

```java
void dragGestureRecognized​(
DragGestureEvent
dge)
```

This method is invoked by the

DragGestureRecognizer

when the

DragGestureRecognizer

detects a platform-dependent
drag initiating gesture. To initiate the drag and drop operation,
if appropriate,

startDrag()

method on
the

DragGestureEvent

has to be invoked.

**Parameters:** dge

- the

DragGestureEvent

describing
the gesture that has just occurred
**See Also:** DragGestureRecognizer

,

DragGestureEvent

---

#### dragGestureRecognized

void dragGestureRecognized​(

DragGestureEvent

dge)

This method is invoked by the

DragGestureRecognizer

when the

DragGestureRecognizer

detects a platform-dependent
drag initiating gesture. To initiate the drag and drop operation,
if appropriate,

startDrag()

method on
the

DragGestureEvent

has to be invoked.

---

