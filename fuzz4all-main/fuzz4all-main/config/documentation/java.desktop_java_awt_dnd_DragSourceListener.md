# Interface DragSourceListener

**Source:** `java.desktop\java\awt\dnd\DragSourceListener.html`

### Class Description

```java
public interface
DragSourceListener

extends
EventListener
```

The

DragSourceListener

defines the
event interface for originators of
Drag and Drop operations to track the state of the user's gesture, and to
provide appropriate "drag over"
feedback to the user throughout the
Drag and Drop operation.

The drop site is

associated with the previous

dragEnter()

invocation

if the latest invocation of

dragEnter()

on this
listener:

- corresponds to that drop site and

is not followed by a

dragExit()

invocation on this listener.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void dragEnter​(
DragSourceDragEvent
dsde)

Called as the cursor's hotspot enters a platform-dependent drop site.
This method is invoked when all the following conditions are true:

- The cursor's hotspot enters the operable part of a platform-
dependent drop site.

The drop site is active.

The drop site accepts the drag.

**Parameters:**
- dsde

- the

DragSourceDragEvent

---

#### void dragOver​(
DragSourceDragEvent
dsde)

Called as the cursor's hotspot moves over a platform-dependent drop site.
This method is invoked when all the following conditions are true:

- The cursor's hotspot has moved, but still intersects the
operable part of the drop site associated with the previous
dragEnter() invocation.

The drop site is still active.

The drop site accepts the drag.

**Parameters:**
- dsde

- the

DragSourceDragEvent

---

#### void dropActionChanged​(
DragSourceDragEvent
dsde)

Called when the user has modified the drop gesture.
This method is invoked when the state of the input
device(s) that the user is interacting with changes.
Such devices are typically the mouse buttons or keyboard
modifiers that the user is interacting with.

**Parameters:**
- dsde

- the

DragSourceDragEvent

---

#### void dragExit​(
DragSourceEvent
dse)

Called as the cursor's hotspot exits a platform-dependent drop site.
This method is invoked when any of the following conditions are true:

- The cursor's hotspot no longer intersects the operable part
of the drop site associated with the previous dragEnter() invocation.

OR

- The drop site associated with the previous dragEnter() invocation
is no longer active.

OR

- The drop site associated with the previous dragEnter() invocation
has rejected the drag.

**Parameters:**
- dse

- the

DragSourceEvent

---

#### void dragDropEnd​(
DragSourceDropEvent
dsde)

This method is invoked to signify that the Drag and Drop
operation is complete. The getDropSuccess() method of
the

DragSourceDropEvent

can be used to
determine the termination state. The getDropAction() method
returns the operation that the drop site selected
to apply to the Drop operation. Once this method is complete, the
current

DragSourceContext

and
associated resources become invalid.

**Parameters:**
- dsde

- the

DragSourceDropEvent

---

### Additional Sections

#### Interface DragSourceListener

**All Superinterfaces:** EventListener

**All Known Implementing Classes:** DragSourceAdapter

,

DragSourceContext

```java
public interface
DragSourceListener

extends
EventListener
```

The

DragSourceListener

defines the
event interface for originators of
Drag and Drop operations to track the state of the user's gesture, and to
provide appropriate "drag over"
feedback to the user throughout the
Drag and Drop operation.

The drop site is

associated with the previous

dragEnter()

invocation

if the latest invocation of

dragEnter()

on this
listener:

- corresponds to that drop site and

is not followed by a

dragExit()

invocation on this listener.

**Since:** 1.2

public interface

DragSourceListener

extends

EventListener

The

DragSourceListener

defines the
event interface for originators of
Drag and Drop operations to track the state of the user's gesture, and to
provide appropriate "drag over"
feedback to the user throughout the
Drag and Drop operation.

The drop site is

associated with the previous

dragEnter()

invocation

if the latest invocation of

dragEnter()

on this
listener:

- corresponds to that drop site and

is not followed by a

dragExit()

invocation on this listener.

The drop site is

associated with the previous

dragEnter()

invocation

if the latest invocation of

dragEnter()

on this
listener:

- corresponds to that drop site and

is not followed by a

dragExit()

invocation on this listener.

corresponds to that drop site and

is not followed by a

dragExit()

invocation on this listener.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

dragDropEnd

​(

DragSourceDropEvent

dsde)

This method is invoked to signify that the Drag and Drop
operation is complete.

void

dragEnter

​(

DragSourceDragEvent

dsde)

Called as the cursor's hotspot enters a platform-dependent drop site.

void

dragExit

​(

DragSourceEvent

dse)

Called as the cursor's hotspot exits a platform-dependent drop site.

void

dragOver

​(

DragSourceDragEvent

dsde)

Called as the cursor's hotspot moves over a platform-dependent drop site.

void

dropActionChanged

​(

DragSourceDragEvent

dsde)

Called when the user has modified the drop gesture.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

dragDropEnd

​(

DragSourceDropEvent

dsde)

This method is invoked to signify that the Drag and Drop
operation is complete.

void

dragEnter

​(

DragSourceDragEvent

dsde)

Called as the cursor's hotspot enters a platform-dependent drop site.

void

dragExit

​(

DragSourceEvent

dse)

Called as the cursor's hotspot exits a platform-dependent drop site.

void

dragOver

​(

DragSourceDragEvent

dsde)

Called as the cursor's hotspot moves over a platform-dependent drop site.

void

dropActionChanged

​(

DragSourceDragEvent

dsde)

Called when the user has modified the drop gesture.

---

#### Method Summary

This method is invoked to signify that the Drag and Drop
operation is complete.

Called as the cursor's hotspot enters a platform-dependent drop site.

Called as the cursor's hotspot exits a platform-dependent drop site.

Called as the cursor's hotspot moves over a platform-dependent drop site.

Called when the user has modified the drop gesture.

============ METHOD DETAIL ==========

- Method Detail

- dragEnter

```java
void dragEnter​(
DragSourceDragEvent
dsde)
```

Called as the cursor's hotspot enters a platform-dependent drop site.
This method is invoked when all the following conditions are true:

- The cursor's hotspot enters the operable part of a platform-
dependent drop site.

The drop site is active.

The drop site accepts the drag.

**Parameters:** dsde

- the

DragSourceDragEvent

- dragOver

```java
void dragOver​(
DragSourceDragEvent
dsde)
```

Called as the cursor's hotspot moves over a platform-dependent drop site.
This method is invoked when all the following conditions are true:

- The cursor's hotspot has moved, but still intersects the
operable part of the drop site associated with the previous
dragEnter() invocation.

The drop site is still active.

The drop site accepts the drag.

**Parameters:** dsde

- the

DragSourceDragEvent

- dropActionChanged

```java
void dropActionChanged​(
DragSourceDragEvent
dsde)
```

Called when the user has modified the drop gesture.
This method is invoked when the state of the input
device(s) that the user is interacting with changes.
Such devices are typically the mouse buttons or keyboard
modifiers that the user is interacting with.

**Parameters:** dsde

- the

DragSourceDragEvent

- dragExit

```java
void dragExit​(
DragSourceEvent
dse)
```

Called as the cursor's hotspot exits a platform-dependent drop site.
This method is invoked when any of the following conditions are true:

- The cursor's hotspot no longer intersects the operable part
of the drop site associated with the previous dragEnter() invocation.

OR

- The drop site associated with the previous dragEnter() invocation
is no longer active.

OR

- The drop site associated with the previous dragEnter() invocation
has rejected the drag.

**Parameters:** dse

- the

DragSourceEvent

- dragDropEnd

```java
void dragDropEnd​(
DragSourceDropEvent
dsde)
```

This method is invoked to signify that the Drag and Drop
operation is complete. The getDropSuccess() method of
the

DragSourceDropEvent

can be used to
determine the termination state. The getDropAction() method
returns the operation that the drop site selected
to apply to the Drop operation. Once this method is complete, the
current

DragSourceContext

and
associated resources become invalid.

**Parameters:** dsde

- the

DragSourceDropEvent

Method Detail

- dragEnter

```java
void dragEnter​(
DragSourceDragEvent
dsde)
```

Called as the cursor's hotspot enters a platform-dependent drop site.
This method is invoked when all the following conditions are true:

- The cursor's hotspot enters the operable part of a platform-
dependent drop site.

The drop site is active.

The drop site accepts the drag.

**Parameters:** dsde

- the

DragSourceDragEvent

- dragOver

```java
void dragOver​(
DragSourceDragEvent
dsde)
```

Called as the cursor's hotspot moves over a platform-dependent drop site.
This method is invoked when all the following conditions are true:

- The cursor's hotspot has moved, but still intersects the
operable part of the drop site associated with the previous
dragEnter() invocation.

The drop site is still active.

The drop site accepts the drag.

**Parameters:** dsde

- the

DragSourceDragEvent

- dropActionChanged

```java
void dropActionChanged​(
DragSourceDragEvent
dsde)
```

Called when the user has modified the drop gesture.
This method is invoked when the state of the input
device(s) that the user is interacting with changes.
Such devices are typically the mouse buttons or keyboard
modifiers that the user is interacting with.

**Parameters:** dsde

- the

DragSourceDragEvent

- dragExit

```java
void dragExit​(
DragSourceEvent
dse)
```

Called as the cursor's hotspot exits a platform-dependent drop site.
This method is invoked when any of the following conditions are true:

- The cursor's hotspot no longer intersects the operable part
of the drop site associated with the previous dragEnter() invocation.

OR

- The drop site associated with the previous dragEnter() invocation
is no longer active.

OR

- The drop site associated with the previous dragEnter() invocation
has rejected the drag.

**Parameters:** dse

- the

DragSourceEvent

- dragDropEnd

```java
void dragDropEnd​(
DragSourceDropEvent
dsde)
```

This method is invoked to signify that the Drag and Drop
operation is complete. The getDropSuccess() method of
the

DragSourceDropEvent

can be used to
determine the termination state. The getDropAction() method
returns the operation that the drop site selected
to apply to the Drop operation. Once this method is complete, the
current

DragSourceContext

and
associated resources become invalid.

**Parameters:** dsde

- the

DragSourceDropEvent

---

#### Method Detail

dragEnter

```java
void dragEnter​(
DragSourceDragEvent
dsde)
```

Called as the cursor's hotspot enters a platform-dependent drop site.
This method is invoked when all the following conditions are true:

- The cursor's hotspot enters the operable part of a platform-
dependent drop site.

The drop site is active.

The drop site accepts the drag.

**Parameters:** dsde

- the

DragSourceDragEvent

---

#### dragEnter

void dragEnter​(

DragSourceDragEvent

dsde)

Called as the cursor's hotspot enters a platform-dependent drop site.
This method is invoked when all the following conditions are true:

- The cursor's hotspot enters the operable part of a platform-
dependent drop site.

The drop site is active.

The drop site accepts the drag.

The cursor's hotspot enters the operable part of a platform-
dependent drop site.

The drop site is active.

The drop site accepts the drag.

dragOver

```java
void dragOver​(
DragSourceDragEvent
dsde)
```

Called as the cursor's hotspot moves over a platform-dependent drop site.
This method is invoked when all the following conditions are true:

- The cursor's hotspot has moved, but still intersects the
operable part of the drop site associated with the previous
dragEnter() invocation.

The drop site is still active.

The drop site accepts the drag.

**Parameters:** dsde

- the

DragSourceDragEvent

---

#### dragOver

void dragOver​(

DragSourceDragEvent

dsde)

Called as the cursor's hotspot moves over a platform-dependent drop site.
This method is invoked when all the following conditions are true:

- The cursor's hotspot has moved, but still intersects the
operable part of the drop site associated with the previous
dragEnter() invocation.

The drop site is still active.

The drop site accepts the drag.

The cursor's hotspot has moved, but still intersects the
operable part of the drop site associated with the previous
dragEnter() invocation.

The drop site is still active.

The drop site accepts the drag.

dropActionChanged

```java
void dropActionChanged​(
DragSourceDragEvent
dsde)
```

Called when the user has modified the drop gesture.
This method is invoked when the state of the input
device(s) that the user is interacting with changes.
Such devices are typically the mouse buttons or keyboard
modifiers that the user is interacting with.

**Parameters:** dsde

- the

DragSourceDragEvent

---

#### dropActionChanged

void dropActionChanged​(

DragSourceDragEvent

dsde)

Called when the user has modified the drop gesture.
This method is invoked when the state of the input
device(s) that the user is interacting with changes.
Such devices are typically the mouse buttons or keyboard
modifiers that the user is interacting with.

dragExit

```java
void dragExit​(
DragSourceEvent
dse)
```

Called as the cursor's hotspot exits a platform-dependent drop site.
This method is invoked when any of the following conditions are true:

- The cursor's hotspot no longer intersects the operable part
of the drop site associated with the previous dragEnter() invocation.

OR

- The drop site associated with the previous dragEnter() invocation
is no longer active.

OR

- The drop site associated with the previous dragEnter() invocation
has rejected the drag.

**Parameters:** dse

- the

DragSourceEvent

---

#### dragExit

void dragExit​(

DragSourceEvent

dse)

Called as the cursor's hotspot exits a platform-dependent drop site.
This method is invoked when any of the following conditions are true:

- The cursor's hotspot no longer intersects the operable part
of the drop site associated with the previous dragEnter() invocation.

OR

- The drop site associated with the previous dragEnter() invocation
is no longer active.

OR

- The drop site associated with the previous dragEnter() invocation
has rejected the drag.

The cursor's hotspot no longer intersects the operable part
of the drop site associated with the previous dragEnter() invocation.

The drop site associated with the previous dragEnter() invocation
is no longer active.

The drop site associated with the previous dragEnter() invocation
has rejected the drag.

dragDropEnd

```java
void dragDropEnd​(
DragSourceDropEvent
dsde)
```

This method is invoked to signify that the Drag and Drop
operation is complete. The getDropSuccess() method of
the

DragSourceDropEvent

can be used to
determine the termination state. The getDropAction() method
returns the operation that the drop site selected
to apply to the Drop operation. Once this method is complete, the
current

DragSourceContext

and
associated resources become invalid.

**Parameters:** dsde

- the

DragSourceDropEvent

---

#### dragDropEnd

void dragDropEnd​(

DragSourceDropEvent

dsde)

This method is invoked to signify that the Drag and Drop
operation is complete. The getDropSuccess() method of
the

DragSourceDropEvent

can be used to
determine the termination state. The getDropAction() method
returns the operation that the drop site selected
to apply to the Drop operation. Once this method is complete, the
current

DragSourceContext

and
associated resources become invalid.

---

