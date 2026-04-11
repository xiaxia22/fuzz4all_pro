# Class DragSourceAdapter

**Source:** `java.desktop\java\awt\dnd\DragSourceAdapter.html`

### Class Description

```java
public abstract class
DragSourceAdapter

extends
Object

implements
DragSourceListener
,
DragSourceMotionListener
```

An abstract adapter class for receiving drag source events. The methods in
this class are empty. This class exists only as a convenience for creating
listener objects.

Extend this class to create a

DragSourceEvent

listener
and override the methods for the events of interest. (If you implement the

DragSourceListener

interface, you have to define all of
the methods in it. This abstract class defines null methods for them
all, so you only have to define methods for events you care about.)

Create a listener object using the extended class and then register it with
a

DragSource

. When the drag enters, moves over, or exits
a drop site, when the drop action changes, and when the drag ends, the
relevant method in the listener object is invoked, and the

DragSourceEvent

is passed to it.

The drop site is

associated with the previous

dragEnter()

invocation

if the latest invocation of

dragEnter()

on this
adapter corresponds to that drop site and is not followed by a

dragExit()

invocation on this adapter.

**All Implemented Interfaces:** DragSourceListener

,

DragSourceMotionListener

,

EventListener

---

### Field Details

*No entries found.*

### Constructor Details

#### public DragSourceAdapter()

*No description found.*

---

### Method Details

#### public void dragEnter​(
DragSourceDragEvent
dsde)

Called as the cursor's hotspot enters a platform-dependent drop site.
This method is invoked when all the following conditions are true:

- The cursor's hotspot enters the operable part of
a platform-dependent drop site.

The drop site is active.

The drop site accepts the drag.

**Specified by:**
- dragEnter

in interface

DragSourceListener

**Parameters:**
- dsde

- the

DragSourceDragEvent

---

#### public void dragOver​(
DragSourceDragEvent
dsde)

Called as the cursor's hotspot moves over a platform-dependent drop site.
This method is invoked when all the following conditions are true:

- The cursor's hotspot has moved, but still intersects the
operable part of the drop site associated with the previous
dragEnter() invocation.

The drop site is still active.

The drop site accepts the drag.

**Specified by:**
- dragOver

in interface

DragSourceListener

**Parameters:**
- dsde

- the

DragSourceDragEvent

---

#### public void dragMouseMoved​(
DragSourceDragEvent
dsde)

Called whenever the mouse is moved during a drag operation.

**Specified by:**
- dragMouseMoved

in interface

DragSourceMotionListener

**Parameters:**
- dsde

- the

DragSourceDragEvent

---

#### public void dropActionChanged​(
DragSourceDragEvent
dsde)

Called when the user has modified the drop gesture.
This method is invoked when the state of the input
device(s) that the user is interacting with changes.
Such devices are typically the mouse buttons or keyboard
modifiers that the user is interacting with.

**Specified by:**
- dropActionChanged

in interface

DragSourceListener

**Parameters:**
- dsde

- the

DragSourceDragEvent

---

#### public void dragExit​(
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

**Specified by:**
- dragExit

in interface

DragSourceListener

**Parameters:**
- dse

- the

DragSourceEvent

---

#### public void dragDropEnd​(
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

**Specified by:**
- dragDropEnd

in interface

DragSourceListener

**Parameters:**
- dsde

- the

DragSourceDropEvent

---

### Additional Sections

#### Class DragSourceAdapter

java.lang.Object

- java.awt.dnd.DragSourceAdapter

java.awt.dnd.DragSourceAdapter

**All Implemented Interfaces:** DragSourceListener

,

DragSourceMotionListener

,

EventListener

```java
public abstract class
DragSourceAdapter

extends
Object

implements
DragSourceListener
,
DragSourceMotionListener
```

An abstract adapter class for receiving drag source events. The methods in
this class are empty. This class exists only as a convenience for creating
listener objects.

Extend this class to create a

DragSourceEvent

listener
and override the methods for the events of interest. (If you implement the

DragSourceListener

interface, you have to define all of
the methods in it. This abstract class defines null methods for them
all, so you only have to define methods for events you care about.)

Create a listener object using the extended class and then register it with
a

DragSource

. When the drag enters, moves over, or exits
a drop site, when the drop action changes, and when the drag ends, the
relevant method in the listener object is invoked, and the

DragSourceEvent

is passed to it.

The drop site is

associated with the previous

dragEnter()

invocation

if the latest invocation of

dragEnter()

on this
adapter corresponds to that drop site and is not followed by a

dragExit()

invocation on this adapter.

**Since:** 1.4
**See Also:** DragSourceEvent

,

DragSourceListener

,

DragSourceMotionListener

public abstract class

DragSourceAdapter

extends

Object

implements

DragSourceListener

,

DragSourceMotionListener

An abstract adapter class for receiving drag source events. The methods in
this class are empty. This class exists only as a convenience for creating
listener objects.

Extend this class to create a

DragSourceEvent

listener
and override the methods for the events of interest. (If you implement the

DragSourceListener

interface, you have to define all of
the methods in it. This abstract class defines null methods for them
all, so you only have to define methods for events you care about.)

Create a listener object using the extended class and then register it with
a

DragSource

. When the drag enters, moves over, or exits
a drop site, when the drop action changes, and when the drag ends, the
relevant method in the listener object is invoked, and the

DragSourceEvent

is passed to it.

The drop site is

associated with the previous

dragEnter()

invocation

if the latest invocation of

dragEnter()

on this
adapter corresponds to that drop site and is not followed by a

dragExit()

invocation on this adapter.

Extend this class to create a

DragSourceEvent

listener
and override the methods for the events of interest. (If you implement the

DragSourceListener

interface, you have to define all of
the methods in it. This abstract class defines null methods for them
all, so you only have to define methods for events you care about.)

Create a listener object using the extended class and then register it with
a

DragSource

. When the drag enters, moves over, or exits
a drop site, when the drop action changes, and when the drag ends, the
relevant method in the listener object is invoked, and the

DragSourceEvent

is passed to it.

The drop site is

associated with the previous

dragEnter()

invocation

if the latest invocation of

dragEnter()

on this
adapter corresponds to that drop site and is not followed by a

dragExit()

invocation on this adapter.

Create a listener object using the extended class and then register it with
a

DragSource

. When the drag enters, moves over, or exits
a drop site, when the drop action changes, and when the drag ends, the
relevant method in the listener object is invoked, and the

DragSourceEvent

is passed to it.

The drop site is

associated with the previous

dragEnter()

invocation

if the latest invocation of

dragEnter()

on this
adapter corresponds to that drop site and is not followed by a

dragExit()

invocation on this adapter.

The drop site is

associated with the previous

dragEnter()

invocation

if the latest invocation of

dragEnter()

on this
adapter corresponds to that drop site and is not followed by a

dragExit()

invocation on this adapter.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DragSourceAdapter

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

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

dragMouseMoved

​(

DragSourceDragEvent

dsde)

Called whenever the mouse is moved during a drag operation.

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

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

DragSourceAdapter

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

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

dragMouseMoved

​(

DragSourceDragEvent

dsde)

Called whenever the mouse is moved during a drag operation.

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

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

This method is invoked to signify that the Drag and Drop
operation is complete.

Called as the cursor's hotspot enters a platform-dependent drop site.

Called as the cursor's hotspot exits a platform-dependent drop site.

Called whenever the mouse is moved during a drag operation.

Called as the cursor's hotspot moves over a platform-dependent drop site.

Called when the user has modified the drop gesture.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DragSourceAdapter

```java
public DragSourceAdapter()
```

============ METHOD DETAIL ==========

- Method Detail

- dragEnter

```java
public void dragEnter​(
DragSourceDragEvent
dsde)
```

Called as the cursor's hotspot enters a platform-dependent drop site.
This method is invoked when all the following conditions are true:

- The cursor's hotspot enters the operable part of
a platform-dependent drop site.

The drop site is active.

The drop site accepts the drag.

**Specified by:** dragEnter

in interface

DragSourceListener
**Parameters:** dsde

- the

DragSourceDragEvent

- dragOver

```java
public void dragOver​(
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

**Specified by:** dragOver

in interface

DragSourceListener
**Parameters:** dsde

- the

DragSourceDragEvent

- dragMouseMoved

```java
public void dragMouseMoved​(
DragSourceDragEvent
dsde)
```

Called whenever the mouse is moved during a drag operation.

**Specified by:** dragMouseMoved

in interface

DragSourceMotionListener
**Parameters:** dsde

- the

DragSourceDragEvent

- dropActionChanged

```java
public void dropActionChanged​(
DragSourceDragEvent
dsde)
```

Called when the user has modified the drop gesture.
This method is invoked when the state of the input
device(s) that the user is interacting with changes.
Such devices are typically the mouse buttons or keyboard
modifiers that the user is interacting with.

**Specified by:** dropActionChanged

in interface

DragSourceListener
**Parameters:** dsde

- the

DragSourceDragEvent

- dragExit

```java
public void dragExit​(
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

**Specified by:** dragExit

in interface

DragSourceListener
**Parameters:** dse

- the

DragSourceEvent

- dragDropEnd

```java
public void dragDropEnd​(
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

**Specified by:** dragDropEnd

in interface

DragSourceListener
**Parameters:** dsde

- the

DragSourceDropEvent

Constructor Detail

- DragSourceAdapter

```java
public DragSourceAdapter()
```

---

#### Constructor Detail

DragSourceAdapter

```java
public DragSourceAdapter()
```

---

#### DragSourceAdapter

public DragSourceAdapter()

Method Detail

- dragEnter

```java
public void dragEnter​(
DragSourceDragEvent
dsde)
```

Called as the cursor's hotspot enters a platform-dependent drop site.
This method is invoked when all the following conditions are true:

- The cursor's hotspot enters the operable part of
a platform-dependent drop site.

The drop site is active.

The drop site accepts the drag.

**Specified by:** dragEnter

in interface

DragSourceListener
**Parameters:** dsde

- the

DragSourceDragEvent

- dragOver

```java
public void dragOver​(
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

**Specified by:** dragOver

in interface

DragSourceListener
**Parameters:** dsde

- the

DragSourceDragEvent

- dragMouseMoved

```java
public void dragMouseMoved​(
DragSourceDragEvent
dsde)
```

Called whenever the mouse is moved during a drag operation.

**Specified by:** dragMouseMoved

in interface

DragSourceMotionListener
**Parameters:** dsde

- the

DragSourceDragEvent

- dropActionChanged

```java
public void dropActionChanged​(
DragSourceDragEvent
dsde)
```

Called when the user has modified the drop gesture.
This method is invoked when the state of the input
device(s) that the user is interacting with changes.
Such devices are typically the mouse buttons or keyboard
modifiers that the user is interacting with.

**Specified by:** dropActionChanged

in interface

DragSourceListener
**Parameters:** dsde

- the

DragSourceDragEvent

- dragExit

```java
public void dragExit​(
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

**Specified by:** dragExit

in interface

DragSourceListener
**Parameters:** dse

- the

DragSourceEvent

- dragDropEnd

```java
public void dragDropEnd​(
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

**Specified by:** dragDropEnd

in interface

DragSourceListener
**Parameters:** dsde

- the

DragSourceDropEvent

---

#### Method Detail

dragEnter

```java
public void dragEnter​(
DragSourceDragEvent
dsde)
```

Called as the cursor's hotspot enters a platform-dependent drop site.
This method is invoked when all the following conditions are true:

- The cursor's hotspot enters the operable part of
a platform-dependent drop site.

The drop site is active.

The drop site accepts the drag.

**Specified by:** dragEnter

in interface

DragSourceListener
**Parameters:** dsde

- the

DragSourceDragEvent

---

#### dragEnter

public void dragEnter​(

DragSourceDragEvent

dsde)

Called as the cursor's hotspot enters a platform-dependent drop site.
This method is invoked when all the following conditions are true:

- The cursor's hotspot enters the operable part of
a platform-dependent drop site.

The drop site is active.

The drop site accepts the drag.

The cursor's hotspot enters the operable part of
a platform-dependent drop site.

The drop site is active.

The drop site accepts the drag.

dragOver

```java
public void dragOver​(
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

**Specified by:** dragOver

in interface

DragSourceListener
**Parameters:** dsde

- the

DragSourceDragEvent

---

#### dragOver

public void dragOver​(

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

dragMouseMoved

```java
public void dragMouseMoved​(
DragSourceDragEvent
dsde)
```

Called whenever the mouse is moved during a drag operation.

**Specified by:** dragMouseMoved

in interface

DragSourceMotionListener
**Parameters:** dsde

- the

DragSourceDragEvent

---

#### dragMouseMoved

public void dragMouseMoved​(

DragSourceDragEvent

dsde)

Called whenever the mouse is moved during a drag operation.

dropActionChanged

```java
public void dropActionChanged​(
DragSourceDragEvent
dsde)
```

Called when the user has modified the drop gesture.
This method is invoked when the state of the input
device(s) that the user is interacting with changes.
Such devices are typically the mouse buttons or keyboard
modifiers that the user is interacting with.

**Specified by:** dropActionChanged

in interface

DragSourceListener
**Parameters:** dsde

- the

DragSourceDragEvent

---

#### dropActionChanged

public void dropActionChanged​(

DragSourceDragEvent

dsde)

Called when the user has modified the drop gesture.
This method is invoked when the state of the input
device(s) that the user is interacting with changes.
Such devices are typically the mouse buttons or keyboard
modifiers that the user is interacting with.

dragExit

```java
public void dragExit​(
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

**Specified by:** dragExit

in interface

DragSourceListener
**Parameters:** dse

- the

DragSourceEvent

---

#### dragExit

public void dragExit​(

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
public void dragDropEnd​(
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

**Specified by:** dragDropEnd

in interface

DragSourceListener
**Parameters:** dsde

- the

DragSourceDropEvent

---

#### dragDropEnd

public void dragDropEnd​(

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

