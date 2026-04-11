# Class DragSourceContext

**Source:** `java.desktop\java\awt\dnd\DragSourceContext.html`

### Class Description

```java
public class
DragSourceContext

extends
Object

implements
DragSourceListener
,
DragSourceMotionListener
,
Serializable
```

The

DragSourceContext

class is responsible for managing the
initiator side of the Drag and Drop protocol. In particular, it is responsible
for managing drag event notifications to the

DragSourceListeners

and

DragSourceMotionListeners

, and providing the

Transferable

representing the source data for the drag operation.

Note that the

DragSourceContext

itself
implements the

DragSourceListener

and

DragSourceMotionListener

interfaces.
This is to allow the platform peer
(the

DragSourceContextPeer

instance)
created by the

DragSource

to notify
the

DragSourceContext

of
state changes in the ongoing operation. This allows the

DragSourceContext

object to interpose
itself between the platform and the
listeners provided by the initiator of the drag operation.

By default,

DragSourceContext

sets the cursor as appropriate
for the current state of the drag and drop operation. For example, if
the user has chosen

the move action

,
and the pointer is over a target that accepts
the move action, the default move cursor is shown. When
the pointer is over an area that does not accept the transfer,
the default "no drop" cursor is shown.

This default handling mechanism is disabled when a custom cursor is set
by the

setCursor(java.awt.Cursor)

method. When the default handling is disabled,
it becomes the responsibility
of the developer to keep the cursor up to date, by listening
to the

DragSource

events and calling the

setCursor()

method.
Alternatively, you can provide custom cursor behavior by providing
custom implementations of the

DragSource

and the

DragSourceContext

classes.

**All Implemented Interfaces:** DragSourceListener

,

DragSourceMotionListener

,

Serializable

,

EventListener

---

### Field Details

#### protected static final int DEFAULT

An

int

used by updateCurrentCursor()
indicating that the

Cursor

should change
to the default (no drop)

Cursor

.

**See Also:**
- Constant Field Values

---

#### protected static final int ENTER

An

int

used by updateCurrentCursor()
indicating that the

Cursor

has entered a

DropTarget

.

**See Also:**
- Constant Field Values

---

#### protected static final int OVER

An

int

used by updateCurrentCursor()
indicating that the

Cursor

is
over a

DropTarget

.

**See Also:**
- Constant Field Values

---

#### protected static final int CHANGED

An

int

used by updateCurrentCursor()
indicating that the user operation has changed.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public DragSourceContext​(
DragGestureEvent
trigger,

Cursor
dragCursor,

Image
dragImage,

Point
offset,

Transferable
t,

DragSourceListener
dsl)

Called from

DragSource

, this constructor creates a new

DragSourceContext

given the

DragSourceContextPeer

for this Drag, the

DragGestureEvent

that triggered the Drag, the initial

Cursor

to use for the Drag, an (optional)

Image

to display while the Drag is taking place, the offset
of the

Image

origin from the hotspot at the instant of the
triggering event, the

Transferable

subject data, and the

DragSourceListener

to use during the Drag and Drop
operation.

If

DragSourceContextPeer

is

null

NullPointerException

is thrown.

If

DragGestureEvent

is

null

NullPointerException

is thrown.

If

Cursor

is

null

no exception is thrown and
the default drag cursor behavior is activated for this drag operation.

If

Image

is

null

no exception is thrown.

If

Image

is not

null

and the offset is

null NullPointerException

is thrown.

If

Transferable

is

null

NullPointerException

is thrown.

If

DragSourceListener

is

null

no exception
is thrown.

**Parameters:**
- trigger

- the triggering event
- dragCursor

- the initial

Cursor

for this drag operation
or

null

for the default cursor handling;
see

class level documentation

for more details on the cursor handling mechanism during drag and drop
- dragImage

- the

Image

to drag (or

null

)
- offset

- the offset of the image origin from the hotspot at the
instant of the triggering event
- t

- the

Transferable
- dsl

- the

DragSourceListener

**Throws:**
- IllegalArgumentException

- if the

Component

associated
with the trigger event is

null

.
- IllegalArgumentException

- if the

DragSource

for the
trigger event is

null

.
- IllegalArgumentException

- if the drag action for the
trigger event is

DnDConstants.ACTION_NONE

.
- IllegalArgumentException

- if the source actions for the

DragGestureRecognizer

associated with the trigger
event are equal to

DnDConstants.ACTION_NONE

.
- NullPointerException

- if dscp, trigger, or t are null, or
if dragImage is non-null and offset is null

---

### Method Details

#### public
DragSource
getDragSource()

Returns the

DragSource

that instantiated this

DragSourceContext

.

**Returns:**
- the

DragSource

that
instantiated this

DragSourceContext

---

#### public
Component
getComponent()

Returns the

Component

associated with this

DragSourceContext

.

**Returns:**
- the

Component

that started the drag

---

#### public
DragGestureEvent
getTrigger()

Returns the

DragGestureEvent

that initially triggered the drag.

**Returns:**
- the Event that triggered the drag

---

#### public int getSourceActions()

Returns a bitwise mask of

DnDConstants

that
represent the set of drop actions supported by the drag source for the
drag operation associated with this

DragSourceContext

.

**Returns:**
- the drop actions supported by the drag source

---

#### public void setCursor​(
Cursor
c)

Sets the custom cursor for this drag operation to the specified

Cursor

. If the specified

Cursor

is

null

, the default drag cursor behavior is
activated for this drag operation, otherwise it is deactivated.

**Parameters:**
- c

- the initial

Cursor

for this drag operation,
or

null

for the default cursor handling;
see

class
level documentation

for more details
on the cursor handling during drag and drop

---

#### public
Cursor
getCursor()

Returns the current custom drag

Cursor

.

**Returns:**
- the current custom drag

Cursor

, if it was set
otherwise returns

null

.

**See Also:**
- setCursor(java.awt.Cursor)

---

#### public void addDragSourceListener​(
DragSourceListener
dsl)
throws
TooManyListenersException

Add a

DragSourceListener

to this

DragSourceContext

if one has not already been added.
If a

DragSourceListener

already exists,
this method throws a

TooManyListenersException

.

**Parameters:**
- dsl

- the

DragSourceListener

to add.
Note that while

null

is not prohibited,
it is not acceptable as a parameter.

**Throws:**
- TooManyListenersException

- if
a

DragSourceListener

has already been added

---

#### public void removeDragSourceListener​(
DragSourceListener
dsl)

Removes the specified

DragSourceListener

from this

DragSourceContext

.

**Parameters:**
- dsl

- the

DragSourceListener

to remove;
note that while

null

is not prohibited,
it is not acceptable as a parameter

---

#### public void transferablesFlavorsChanged()

Notifies the peer that the

Transferable

's

DataFlavor

s have changed.

---

#### public void dragEnter​(
DragSourceDragEvent
dsde)

Calls

dragEnter

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceDragEvent

.

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

Calls

dragOver

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceDragEvent

.

**Specified by:**
- dragOver

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

Calls

dragExit

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceEvent

.

**Specified by:**
- dragExit

in interface

DragSourceListener

**Parameters:**
- dse

- the

DragSourceEvent

---

#### public void dropActionChanged​(
DragSourceDragEvent
dsde)

Calls

dropActionChanged

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceDragEvent

.

**Specified by:**
- dropActionChanged

in interface

DragSourceListener

**Parameters:**
- dsde

- the

DragSourceDragEvent

---

#### public void dragDropEnd​(
DragSourceDropEvent
dsde)

Calls

dragDropEnd

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceDropEvent

.

**Specified by:**
- dragDropEnd

in interface

DragSourceListener

**Parameters:**
- dsde

- the

DragSourceDropEvent

---

#### public void dragMouseMoved​(
DragSourceDragEvent
dsde)

Calls

dragMouseMoved

on the

DragSourceMotionListener

s registered with the

DragSource

associated with this

DragSourceContext

, and them passes the specified

DragSourceDragEvent

.

**Specified by:**
- dragMouseMoved

in interface

DragSourceMotionListener

**Parameters:**
- dsde

- the

DragSourceDragEvent

**Since:**
- 1.4

---

#### public
Transferable
getTransferable()

Returns the

Transferable

associated with
this

DragSourceContext

.

**Returns:**
- the

Transferable

---

#### protected void updateCurrentCursor​(int sourceAct,
int targetAct,
int status)

If the default drag cursor behavior is active, this method
sets the default drag cursor for the specified actions
supported by the drag source, the drop target action,
and status, otherwise this method does nothing.

**Parameters:**
- sourceAct

- the actions supported by the drag source
- targetAct

- the drop target action
- status

- one of the fields

DEFAULT

,

ENTER

,

OVER

,

CHANGED

---

### Additional Sections

#### Class DragSourceContext

java.lang.Object

- java.awt.dnd.DragSourceContext

java.awt.dnd.DragSourceContext

**All Implemented Interfaces:** DragSourceListener

,

DragSourceMotionListener

,

Serializable

,

EventListener

```java
public class
DragSourceContext

extends
Object

implements
DragSourceListener
,
DragSourceMotionListener
,
Serializable
```

The

DragSourceContext

class is responsible for managing the
initiator side of the Drag and Drop protocol. In particular, it is responsible
for managing drag event notifications to the

DragSourceListeners

and

DragSourceMotionListeners

, and providing the

Transferable

representing the source data for the drag operation.

Note that the

DragSourceContext

itself
implements the

DragSourceListener

and

DragSourceMotionListener

interfaces.
This is to allow the platform peer
(the

DragSourceContextPeer

instance)
created by the

DragSource

to notify
the

DragSourceContext

of
state changes in the ongoing operation. This allows the

DragSourceContext

object to interpose
itself between the platform and the
listeners provided by the initiator of the drag operation.

By default,

DragSourceContext

sets the cursor as appropriate
for the current state of the drag and drop operation. For example, if
the user has chosen

the move action

,
and the pointer is over a target that accepts
the move action, the default move cursor is shown. When
the pointer is over an area that does not accept the transfer,
the default "no drop" cursor is shown.

This default handling mechanism is disabled when a custom cursor is set
by the

setCursor(java.awt.Cursor)

method. When the default handling is disabled,
it becomes the responsibility
of the developer to keep the cursor up to date, by listening
to the

DragSource

events and calling the

setCursor()

method.
Alternatively, you can provide custom cursor behavior by providing
custom implementations of the

DragSource

and the

DragSourceContext

classes.

**Since:** 1.2
**See Also:** DragSourceListener

,

DragSourceMotionListener

,

DnDConstants

,

Serialized Form

public class

DragSourceContext

extends

Object

implements

DragSourceListener

,

DragSourceMotionListener

,

Serializable

The

DragSourceContext

class is responsible for managing the
initiator side of the Drag and Drop protocol. In particular, it is responsible
for managing drag event notifications to the

DragSourceListeners

and

DragSourceMotionListeners

, and providing the

Transferable

representing the source data for the drag operation.

Note that the

DragSourceContext

itself
implements the

DragSourceListener

and

DragSourceMotionListener

interfaces.
This is to allow the platform peer
(the

DragSourceContextPeer

instance)
created by the

DragSource

to notify
the

DragSourceContext

of
state changes in the ongoing operation. This allows the

DragSourceContext

object to interpose
itself between the platform and the
listeners provided by the initiator of the drag operation.

By default,

DragSourceContext

sets the cursor as appropriate
for the current state of the drag and drop operation. For example, if
the user has chosen

the move action

,
and the pointer is over a target that accepts
the move action, the default move cursor is shown. When
the pointer is over an area that does not accept the transfer,
the default "no drop" cursor is shown.

This default handling mechanism is disabled when a custom cursor is set
by the

setCursor(java.awt.Cursor)

method. When the default handling is disabled,
it becomes the responsibility
of the developer to keep the cursor up to date, by listening
to the

DragSource

events and calling the

setCursor()

method.
Alternatively, you can provide custom cursor behavior by providing
custom implementations of the

DragSource

and the

DragSourceContext

classes.

Note that the

DragSourceContext

itself
implements the

DragSourceListener

and

DragSourceMotionListener

interfaces.
This is to allow the platform peer
(the

DragSourceContextPeer

instance)
created by the

DragSource

to notify
the

DragSourceContext

of
state changes in the ongoing operation. This allows the

DragSourceContext

object to interpose
itself between the platform and the
listeners provided by the initiator of the drag operation.

By default,

DragSourceContext

sets the cursor as appropriate
for the current state of the drag and drop operation. For example, if
the user has chosen

the move action

,
and the pointer is over a target that accepts
the move action, the default move cursor is shown. When
the pointer is over an area that does not accept the transfer,
the default "no drop" cursor is shown.

This default handling mechanism is disabled when a custom cursor is set
by the

setCursor(java.awt.Cursor)

method. When the default handling is disabled,
it becomes the responsibility
of the developer to keep the cursor up to date, by listening
to the

DragSource

events and calling the

setCursor()

method.
Alternatively, you can provide custom cursor behavior by providing
custom implementations of the

DragSource

and the

DragSourceContext

classes.

By default,

DragSourceContext

sets the cursor as appropriate
for the current state of the drag and drop operation. For example, if
the user has chosen

the move action

,
and the pointer is over a target that accepts
the move action, the default move cursor is shown. When
the pointer is over an area that does not accept the transfer,
the default "no drop" cursor is shown.

This default handling mechanism is disabled when a custom cursor is set
by the

setCursor(java.awt.Cursor)

method. When the default handling is disabled,
it becomes the responsibility
of the developer to keep the cursor up to date, by listening
to the

DragSource

events and calling the

setCursor()

method.
Alternatively, you can provide custom cursor behavior by providing
custom implementations of the

DragSource

and the

DragSourceContext

classes.

This default handling mechanism is disabled when a custom cursor is set
by the

setCursor(java.awt.Cursor)

method. When the default handling is disabled,
it becomes the responsibility
of the developer to keep the cursor up to date, by listening
to the

DragSource

events and calling the

setCursor()

method.
Alternatively, you can provide custom cursor behavior by providing
custom implementations of the

DragSource

and the

DragSourceContext

classes.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected static int

CHANGED

An

int

used by updateCurrentCursor()
indicating that the user operation has changed.

protected static int

DEFAULT

An

int

used by updateCurrentCursor()
indicating that the

Cursor

should change
to the default (no drop)

Cursor

.

protected static int

ENTER

An

int

used by updateCurrentCursor()
indicating that the

Cursor

has entered a

DropTarget

.

protected static int

OVER

An

int

used by updateCurrentCursor()
indicating that the

Cursor

is
over a

DropTarget

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DragSourceContext

​(

DragGestureEvent

trigger,

Cursor

dragCursor,

Image

dragImage,

Point

offset,

Transferable

t,

DragSourceListener

dsl)

Called from

DragSource

, this constructor creates a new

DragSourceContext

given the

DragSourceContextPeer

for this Drag, the

DragGestureEvent

that triggered the Drag, the initial

Cursor

to use for the Drag, an (optional)

Image

to display while the Drag is taking place, the offset
of the

Image

origin from the hotspot at the instant of the
triggering event, the

Transferable

subject data, and the

DragSourceListener

to use during the Drag and Drop
operation.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addDragSourceListener

​(

DragSourceListener

dsl)

Add a

DragSourceListener

to this

DragSourceContext

if one has not already been added.

void

dragDropEnd

​(

DragSourceDropEvent

dsde)

Calls

dragDropEnd

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceDropEvent

.

void

dragEnter

​(

DragSourceDragEvent

dsde)

Calls

dragEnter

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceDragEvent

.

void

dragExit

​(

DragSourceEvent

dse)

Calls

dragExit

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceEvent

.

void

dragMouseMoved

​(

DragSourceDragEvent

dsde)

Calls

dragMouseMoved

on the

DragSourceMotionListener

s registered with the

DragSource

associated with this

DragSourceContext

, and them passes the specified

DragSourceDragEvent

.

void

dragOver

​(

DragSourceDragEvent

dsde)

Calls

dragOver

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceDragEvent

.

void

dropActionChanged

​(

DragSourceDragEvent

dsde)

Calls

dropActionChanged

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceDragEvent

.

Component

getComponent

()

Returns the

Component

associated with this

DragSourceContext

.

Cursor

getCursor

()

Returns the current custom drag

Cursor

.

DragSource

getDragSource

()

Returns the

DragSource

that instantiated this

DragSourceContext

.

int

getSourceActions

()

Returns a bitwise mask of

DnDConstants

that
represent the set of drop actions supported by the drag source for the
drag operation associated with this

DragSourceContext

.

Transferable

getTransferable

()

Returns the

Transferable

associated with
this

DragSourceContext

.

DragGestureEvent

getTrigger

()

Returns the

DragGestureEvent

that initially triggered the drag.

void

removeDragSourceListener

​(

DragSourceListener

dsl)

Removes the specified

DragSourceListener

from this

DragSourceContext

.

void

setCursor

​(

Cursor

c)

Sets the custom cursor for this drag operation to the specified

Cursor

.

void

transferablesFlavorsChanged

()

Notifies the peer that the

Transferable

's

DataFlavor

s have changed.

protected void

updateCurrentCursor

​(int sourceAct,
int targetAct,
int status)

If the default drag cursor behavior is active, this method
sets the default drag cursor for the specified actions
supported by the drag source, the drop target action,
and status, otherwise this method does nothing.

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

Field Summary

Fields

Modifier and Type

Field

Description

protected static int

CHANGED

An

int

used by updateCurrentCursor()
indicating that the user operation has changed.

protected static int

DEFAULT

An

int

used by updateCurrentCursor()
indicating that the

Cursor

should change
to the default (no drop)

Cursor

.

protected static int

ENTER

An

int

used by updateCurrentCursor()
indicating that the

Cursor

has entered a

DropTarget

.

protected static int

OVER

An

int

used by updateCurrentCursor()
indicating that the

Cursor

is
over a

DropTarget

.

---

#### Field Summary

An

int

used by updateCurrentCursor()
indicating that the user operation has changed.

An

int

used by updateCurrentCursor()
indicating that the

Cursor

should change
to the default (no drop)

Cursor

.

An

int

used by updateCurrentCursor()
indicating that the

Cursor

has entered a

DropTarget

.

An

int

used by updateCurrentCursor()
indicating that the

Cursor

is
over a

DropTarget

.

Constructor Summary

Constructors

Constructor

Description

DragSourceContext

​(

DragGestureEvent

trigger,

Cursor

dragCursor,

Image

dragImage,

Point

offset,

Transferable

t,

DragSourceListener

dsl)

Called from

DragSource

, this constructor creates a new

DragSourceContext

given the

DragSourceContextPeer

for this Drag, the

DragGestureEvent

that triggered the Drag, the initial

Cursor

to use for the Drag, an (optional)

Image

to display while the Drag is taking place, the offset
of the

Image

origin from the hotspot at the instant of the
triggering event, the

Transferable

subject data, and the

DragSourceListener

to use during the Drag and Drop
operation.

---

#### Constructor Summary

Called from

DragSource

, this constructor creates a new

DragSourceContext

given the

DragSourceContextPeer

for this Drag, the

DragGestureEvent

that triggered the Drag, the initial

Cursor

to use for the Drag, an (optional)

Image

to display while the Drag is taking place, the offset
of the

Image

origin from the hotspot at the instant of the
triggering event, the

Transferable

subject data, and the

DragSourceListener

to use during the Drag and Drop
operation.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addDragSourceListener

​(

DragSourceListener

dsl)

Add a

DragSourceListener

to this

DragSourceContext

if one has not already been added.

void

dragDropEnd

​(

DragSourceDropEvent

dsde)

Calls

dragDropEnd

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceDropEvent

.

void

dragEnter

​(

DragSourceDragEvent

dsde)

Calls

dragEnter

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceDragEvent

.

void

dragExit

​(

DragSourceEvent

dse)

Calls

dragExit

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceEvent

.

void

dragMouseMoved

​(

DragSourceDragEvent

dsde)

Calls

dragMouseMoved

on the

DragSourceMotionListener

s registered with the

DragSource

associated with this

DragSourceContext

, and them passes the specified

DragSourceDragEvent

.

void

dragOver

​(

DragSourceDragEvent

dsde)

Calls

dragOver

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceDragEvent

.

void

dropActionChanged

​(

DragSourceDragEvent

dsde)

Calls

dropActionChanged

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceDragEvent

.

Component

getComponent

()

Returns the

Component

associated with this

DragSourceContext

.

Cursor

getCursor

()

Returns the current custom drag

Cursor

.

DragSource

getDragSource

()

Returns the

DragSource

that instantiated this

DragSourceContext

.

int

getSourceActions

()

Returns a bitwise mask of

DnDConstants

that
represent the set of drop actions supported by the drag source for the
drag operation associated with this

DragSourceContext

.

Transferable

getTransferable

()

Returns the

Transferable

associated with
this

DragSourceContext

.

DragGestureEvent

getTrigger

()

Returns the

DragGestureEvent

that initially triggered the drag.

void

removeDragSourceListener

​(

DragSourceListener

dsl)

Removes the specified

DragSourceListener

from this

DragSourceContext

.

void

setCursor

​(

Cursor

c)

Sets the custom cursor for this drag operation to the specified

Cursor

.

void

transferablesFlavorsChanged

()

Notifies the peer that the

Transferable

's

DataFlavor

s have changed.

protected void

updateCurrentCursor

​(int sourceAct,
int targetAct,
int status)

If the default drag cursor behavior is active, this method
sets the default drag cursor for the specified actions
supported by the drag source, the drop target action,
and status, otherwise this method does nothing.

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

Add a

DragSourceListener

to this

DragSourceContext

if one has not already been added.

Calls

dragDropEnd

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceDropEvent

.

Calls

dragEnter

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceDragEvent

.

Calls

dragExit

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceEvent

.

Calls

dragMouseMoved

on the

DragSourceMotionListener

s registered with the

DragSource

associated with this

DragSourceContext

, and them passes the specified

DragSourceDragEvent

.

Calls

dragOver

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceDragEvent

.

Calls

dropActionChanged

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceDragEvent

.

Returns the

Component

associated with this

DragSourceContext

.

Returns the current custom drag

Cursor

.

Returns the

DragSource

that instantiated this

DragSourceContext

.

Returns a bitwise mask of

DnDConstants

that
represent the set of drop actions supported by the drag source for the
drag operation associated with this

DragSourceContext

.

Returns the

Transferable

associated with
this

DragSourceContext

.

Returns the

DragGestureEvent

that initially triggered the drag.

Removes the specified

DragSourceListener

from this

DragSourceContext

.

Sets the custom cursor for this drag operation to the specified

Cursor

.

Notifies the peer that the

Transferable

's

DataFlavor

s have changed.

If the default drag cursor behavior is active, this method
sets the default drag cursor for the specified actions
supported by the drag source, the drop target action,
and status, otherwise this method does nothing.

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

============ FIELD DETAIL ===========

- Field Detail

- DEFAULT

```java
protected static final int DEFAULT
```

An

int

used by updateCurrentCursor()
indicating that the

Cursor

should change
to the default (no drop)

Cursor

.

**See Also:** Constant Field Values

- ENTER

```java
protected static final int ENTER
```

An

int

used by updateCurrentCursor()
indicating that the

Cursor

has entered a

DropTarget

.

**See Also:** Constant Field Values

- OVER

```java
protected static final int OVER
```

An

int

used by updateCurrentCursor()
indicating that the

Cursor

is
over a

DropTarget

.

**See Also:** Constant Field Values

- CHANGED

```java
protected static final int CHANGED
```

An

int

used by updateCurrentCursor()
indicating that the user operation has changed.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DragSourceContext

```java
public DragSourceContext​(
DragGestureEvent
trigger,

Cursor
dragCursor,

Image
dragImage,

Point
offset,

Transferable
t,

DragSourceListener
dsl)
```

Called from

DragSource

, this constructor creates a new

DragSourceContext

given the

DragSourceContextPeer

for this Drag, the

DragGestureEvent

that triggered the Drag, the initial

Cursor

to use for the Drag, an (optional)

Image

to display while the Drag is taking place, the offset
of the

Image

origin from the hotspot at the instant of the
triggering event, the

Transferable

subject data, and the

DragSourceListener

to use during the Drag and Drop
operation.

If

DragSourceContextPeer

is

null

NullPointerException

is thrown.

If

DragGestureEvent

is

null

NullPointerException

is thrown.

If

Cursor

is

null

no exception is thrown and
the default drag cursor behavior is activated for this drag operation.

If

Image

is

null

no exception is thrown.

If

Image

is not

null

and the offset is

null NullPointerException

is thrown.

If

Transferable

is

null

NullPointerException

is thrown.

If

DragSourceListener

is

null

no exception
is thrown.

**Parameters:** trigger

- the triggering event
**Parameters:** dragCursor

- the initial

Cursor

for this drag operation
or

null

for the default cursor handling;
see

class level documentation

for more details on the cursor handling mechanism during drag and drop
**Parameters:** dragImage

- the

Image

to drag (or

null

)
**Parameters:** offset

- the offset of the image origin from the hotspot at the
instant of the triggering event
**Parameters:** t

- the

Transferable
**Parameters:** dsl

- the

DragSourceListener
**Throws:** IllegalArgumentException

- if the

Component

associated
with the trigger event is

null

.
**Throws:** IllegalArgumentException

- if the

DragSource

for the
trigger event is

null

.
**Throws:** IllegalArgumentException

- if the drag action for the
trigger event is

DnDConstants.ACTION_NONE

.
**Throws:** IllegalArgumentException

- if the source actions for the

DragGestureRecognizer

associated with the trigger
event are equal to

DnDConstants.ACTION_NONE

.
**Throws:** NullPointerException

- if dscp, trigger, or t are null, or
if dragImage is non-null and offset is null

============ METHOD DETAIL ==========

- Method Detail

- getDragSource

```java
public
DragSource
getDragSource()
```

Returns the

DragSource

that instantiated this

DragSourceContext

.

**Returns:** the

DragSource

that
instantiated this

DragSourceContext

- getComponent

```java
public
Component
getComponent()
```

Returns the

Component

associated with this

DragSourceContext

.

**Returns:** the

Component

that started the drag

- getTrigger

```java
public
DragGestureEvent
getTrigger()
```

Returns the

DragGestureEvent

that initially triggered the drag.

**Returns:** the Event that triggered the drag

- getSourceActions

```java
public int getSourceActions()
```

Returns a bitwise mask of

DnDConstants

that
represent the set of drop actions supported by the drag source for the
drag operation associated with this

DragSourceContext

.

**Returns:** the drop actions supported by the drag source

- setCursor

```java
public void setCursor​(
Cursor
c)
```

Sets the custom cursor for this drag operation to the specified

Cursor

. If the specified

Cursor

is

null

, the default drag cursor behavior is
activated for this drag operation, otherwise it is deactivated.

**Parameters:** c

- the initial

Cursor

for this drag operation,
or

null

for the default cursor handling;
see

class
level documentation

for more details
on the cursor handling during drag and drop

- getCursor

```java
public
Cursor
getCursor()
```

Returns the current custom drag

Cursor

.

**Returns:** the current custom drag

Cursor

, if it was set
otherwise returns

null

.
**See Also:** setCursor(java.awt.Cursor)

- addDragSourceListener

```java
public void addDragSourceListener​(
DragSourceListener
dsl)
throws
TooManyListenersException
```

Add a

DragSourceListener

to this

DragSourceContext

if one has not already been added.
If a

DragSourceListener

already exists,
this method throws a

TooManyListenersException

.

**Parameters:** dsl

- the

DragSourceListener

to add.
Note that while

null

is not prohibited,
it is not acceptable as a parameter.
**Throws:** TooManyListenersException

- if
a

DragSourceListener

has already been added

- removeDragSourceListener

```java
public void removeDragSourceListener​(
DragSourceListener
dsl)
```

Removes the specified

DragSourceListener

from this

DragSourceContext

.

**Parameters:** dsl

- the

DragSourceListener

to remove;
note that while

null

is not prohibited,
it is not acceptable as a parameter

- transferablesFlavorsChanged

```java
public void transferablesFlavorsChanged()
```

Notifies the peer that the

Transferable

's

DataFlavor

s have changed.

- dragEnter

```java
public void dragEnter​(
DragSourceDragEvent
dsde)
```

Calls

dragEnter

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceDragEvent

.

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

Calls

dragOver

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceDragEvent

.

**Specified by:** dragOver

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

Calls

dragExit

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceEvent

.

**Specified by:** dragExit

in interface

DragSourceListener
**Parameters:** dse

- the

DragSourceEvent

- dropActionChanged

```java
public void dropActionChanged​(
DragSourceDragEvent
dsde)
```

Calls

dropActionChanged

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceDragEvent

.

**Specified by:** dropActionChanged

in interface

DragSourceListener
**Parameters:** dsde

- the

DragSourceDragEvent

- dragDropEnd

```java
public void dragDropEnd​(
DragSourceDropEvent
dsde)
```

Calls

dragDropEnd

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceDropEvent

.

**Specified by:** dragDropEnd

in interface

DragSourceListener
**Parameters:** dsde

- the

DragSourceDropEvent

- dragMouseMoved

```java
public void dragMouseMoved​(
DragSourceDragEvent
dsde)
```

Calls

dragMouseMoved

on the

DragSourceMotionListener

s registered with the

DragSource

associated with this

DragSourceContext

, and them passes the specified

DragSourceDragEvent

.

**Specified by:** dragMouseMoved

in interface

DragSourceMotionListener
**Parameters:** dsde

- the

DragSourceDragEvent
**Since:** 1.4

- getTransferable

```java
public
Transferable
getTransferable()
```

Returns the

Transferable

associated with
this

DragSourceContext

.

**Returns:** the

Transferable

- updateCurrentCursor

```java
protected void updateCurrentCursor​(int sourceAct,
int targetAct,
int status)
```

If the default drag cursor behavior is active, this method
sets the default drag cursor for the specified actions
supported by the drag source, the drop target action,
and status, otherwise this method does nothing.

**Parameters:** sourceAct

- the actions supported by the drag source
**Parameters:** targetAct

- the drop target action
**Parameters:** status

- one of the fields

DEFAULT

,

ENTER

,

OVER

,

CHANGED

Field Detail

- DEFAULT

```java
protected static final int DEFAULT
```

An

int

used by updateCurrentCursor()
indicating that the

Cursor

should change
to the default (no drop)

Cursor

.

**See Also:** Constant Field Values

- ENTER

```java
protected static final int ENTER
```

An

int

used by updateCurrentCursor()
indicating that the

Cursor

has entered a

DropTarget

.

**See Also:** Constant Field Values

- OVER

```java
protected static final int OVER
```

An

int

used by updateCurrentCursor()
indicating that the

Cursor

is
over a

DropTarget

.

**See Also:** Constant Field Values

- CHANGED

```java
protected static final int CHANGED
```

An

int

used by updateCurrentCursor()
indicating that the user operation has changed.

**See Also:** Constant Field Values

---

#### Field Detail

DEFAULT

```java
protected static final int DEFAULT
```

An

int

used by updateCurrentCursor()
indicating that the

Cursor

should change
to the default (no drop)

Cursor

.

**See Also:** Constant Field Values

---

#### DEFAULT

protected static final int DEFAULT

An

int

used by updateCurrentCursor()
indicating that the

Cursor

should change
to the default (no drop)

Cursor

.

ENTER

```java
protected static final int ENTER
```

An

int

used by updateCurrentCursor()
indicating that the

Cursor

has entered a

DropTarget

.

**See Also:** Constant Field Values

---

#### ENTER

protected static final int ENTER

An

int

used by updateCurrentCursor()
indicating that the

Cursor

has entered a

DropTarget

.

OVER

```java
protected static final int OVER
```

An

int

used by updateCurrentCursor()
indicating that the

Cursor

is
over a

DropTarget

.

**See Also:** Constant Field Values

---

#### OVER

protected static final int OVER

An

int

used by updateCurrentCursor()
indicating that the

Cursor

is
over a

DropTarget

.

CHANGED

```java
protected static final int CHANGED
```

An

int

used by updateCurrentCursor()
indicating that the user operation has changed.

**See Also:** Constant Field Values

---

#### CHANGED

protected static final int CHANGED

An

int

used by updateCurrentCursor()
indicating that the user operation has changed.

Constructor Detail

- DragSourceContext

```java
public DragSourceContext​(
DragGestureEvent
trigger,

Cursor
dragCursor,

Image
dragImage,

Point
offset,

Transferable
t,

DragSourceListener
dsl)
```

Called from

DragSource

, this constructor creates a new

DragSourceContext

given the

DragSourceContextPeer

for this Drag, the

DragGestureEvent

that triggered the Drag, the initial

Cursor

to use for the Drag, an (optional)

Image

to display while the Drag is taking place, the offset
of the

Image

origin from the hotspot at the instant of the
triggering event, the

Transferable

subject data, and the

DragSourceListener

to use during the Drag and Drop
operation.

If

DragSourceContextPeer

is

null

NullPointerException

is thrown.

If

DragGestureEvent

is

null

NullPointerException

is thrown.

If

Cursor

is

null

no exception is thrown and
the default drag cursor behavior is activated for this drag operation.

If

Image

is

null

no exception is thrown.

If

Image

is not

null

and the offset is

null NullPointerException

is thrown.

If

Transferable

is

null

NullPointerException

is thrown.

If

DragSourceListener

is

null

no exception
is thrown.

**Parameters:** trigger

- the triggering event
**Parameters:** dragCursor

- the initial

Cursor

for this drag operation
or

null

for the default cursor handling;
see

class level documentation

for more details on the cursor handling mechanism during drag and drop
**Parameters:** dragImage

- the

Image

to drag (or

null

)
**Parameters:** offset

- the offset of the image origin from the hotspot at the
instant of the triggering event
**Parameters:** t

- the

Transferable
**Parameters:** dsl

- the

DragSourceListener
**Throws:** IllegalArgumentException

- if the

Component

associated
with the trigger event is

null

.
**Throws:** IllegalArgumentException

- if the

DragSource

for the
trigger event is

null

.
**Throws:** IllegalArgumentException

- if the drag action for the
trigger event is

DnDConstants.ACTION_NONE

.
**Throws:** IllegalArgumentException

- if the source actions for the

DragGestureRecognizer

associated with the trigger
event are equal to

DnDConstants.ACTION_NONE

.
**Throws:** NullPointerException

- if dscp, trigger, or t are null, or
if dragImage is non-null and offset is null

---

#### Constructor Detail

DragSourceContext

```java
public DragSourceContext​(
DragGestureEvent
trigger,

Cursor
dragCursor,

Image
dragImage,

Point
offset,

Transferable
t,

DragSourceListener
dsl)
```

Called from

DragSource

, this constructor creates a new

DragSourceContext

given the

DragSourceContextPeer

for this Drag, the

DragGestureEvent

that triggered the Drag, the initial

Cursor

to use for the Drag, an (optional)

Image

to display while the Drag is taking place, the offset
of the

Image

origin from the hotspot at the instant of the
triggering event, the

Transferable

subject data, and the

DragSourceListener

to use during the Drag and Drop
operation.

If

DragSourceContextPeer

is

null

NullPointerException

is thrown.

If

DragGestureEvent

is

null

NullPointerException

is thrown.

If

Cursor

is

null

no exception is thrown and
the default drag cursor behavior is activated for this drag operation.

If

Image

is

null

no exception is thrown.

If

Image

is not

null

and the offset is

null NullPointerException

is thrown.

If

Transferable

is

null

NullPointerException

is thrown.

If

DragSourceListener

is

null

no exception
is thrown.

**Parameters:** trigger

- the triggering event
**Parameters:** dragCursor

- the initial

Cursor

for this drag operation
or

null

for the default cursor handling;
see

class level documentation

for more details on the cursor handling mechanism during drag and drop
**Parameters:** dragImage

- the

Image

to drag (or

null

)
**Parameters:** offset

- the offset of the image origin from the hotspot at the
instant of the triggering event
**Parameters:** t

- the

Transferable
**Parameters:** dsl

- the

DragSourceListener
**Throws:** IllegalArgumentException

- if the

Component

associated
with the trigger event is

null

.
**Throws:** IllegalArgumentException

- if the

DragSource

for the
trigger event is

null

.
**Throws:** IllegalArgumentException

- if the drag action for the
trigger event is

DnDConstants.ACTION_NONE

.
**Throws:** IllegalArgumentException

- if the source actions for the

DragGestureRecognizer

associated with the trigger
event are equal to

DnDConstants.ACTION_NONE

.
**Throws:** NullPointerException

- if dscp, trigger, or t are null, or
if dragImage is non-null and offset is null

---

#### DragSourceContext

public DragSourceContext​(

DragGestureEvent

trigger,

Cursor

dragCursor,

Image

dragImage,

Point

offset,

Transferable

t,

DragSourceListener

dsl)

Called from

DragSource

, this constructor creates a new

DragSourceContext

given the

DragSourceContextPeer

for this Drag, the

DragGestureEvent

that triggered the Drag, the initial

Cursor

to use for the Drag, an (optional)

Image

to display while the Drag is taking place, the offset
of the

Image

origin from the hotspot at the instant of the
triggering event, the

Transferable

subject data, and the

DragSourceListener

to use during the Drag and Drop
operation.

If

DragSourceContextPeer

is

null

NullPointerException

is thrown.

If

DragGestureEvent

is

null

NullPointerException

is thrown.

If

Cursor

is

null

no exception is thrown and
the default drag cursor behavior is activated for this drag operation.

If

Image

is

null

no exception is thrown.

If

Image

is not

null

and the offset is

null NullPointerException

is thrown.

If

Transferable

is

null

NullPointerException

is thrown.

If

DragSourceListener

is

null

no exception
is thrown.

Method Detail

- getDragSource

```java
public
DragSource
getDragSource()
```

Returns the

DragSource

that instantiated this

DragSourceContext

.

**Returns:** the

DragSource

that
instantiated this

DragSourceContext

- getComponent

```java
public
Component
getComponent()
```

Returns the

Component

associated with this

DragSourceContext

.

**Returns:** the

Component

that started the drag

- getTrigger

```java
public
DragGestureEvent
getTrigger()
```

Returns the

DragGestureEvent

that initially triggered the drag.

**Returns:** the Event that triggered the drag

- getSourceActions

```java
public int getSourceActions()
```

Returns a bitwise mask of

DnDConstants

that
represent the set of drop actions supported by the drag source for the
drag operation associated with this

DragSourceContext

.

**Returns:** the drop actions supported by the drag source

- setCursor

```java
public void setCursor​(
Cursor
c)
```

Sets the custom cursor for this drag operation to the specified

Cursor

. If the specified

Cursor

is

null

, the default drag cursor behavior is
activated for this drag operation, otherwise it is deactivated.

**Parameters:** c

- the initial

Cursor

for this drag operation,
or

null

for the default cursor handling;
see

class
level documentation

for more details
on the cursor handling during drag and drop

- getCursor

```java
public
Cursor
getCursor()
```

Returns the current custom drag

Cursor

.

**Returns:** the current custom drag

Cursor

, if it was set
otherwise returns

null

.
**See Also:** setCursor(java.awt.Cursor)

- addDragSourceListener

```java
public void addDragSourceListener​(
DragSourceListener
dsl)
throws
TooManyListenersException
```

Add a

DragSourceListener

to this

DragSourceContext

if one has not already been added.
If a

DragSourceListener

already exists,
this method throws a

TooManyListenersException

.

**Parameters:** dsl

- the

DragSourceListener

to add.
Note that while

null

is not prohibited,
it is not acceptable as a parameter.
**Throws:** TooManyListenersException

- if
a

DragSourceListener

has already been added

- removeDragSourceListener

```java
public void removeDragSourceListener​(
DragSourceListener
dsl)
```

Removes the specified

DragSourceListener

from this

DragSourceContext

.

**Parameters:** dsl

- the

DragSourceListener

to remove;
note that while

null

is not prohibited,
it is not acceptable as a parameter

- transferablesFlavorsChanged

```java
public void transferablesFlavorsChanged()
```

Notifies the peer that the

Transferable

's

DataFlavor

s have changed.

- dragEnter

```java
public void dragEnter​(
DragSourceDragEvent
dsde)
```

Calls

dragEnter

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceDragEvent

.

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

Calls

dragOver

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceDragEvent

.

**Specified by:** dragOver

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

Calls

dragExit

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceEvent

.

**Specified by:** dragExit

in interface

DragSourceListener
**Parameters:** dse

- the

DragSourceEvent

- dropActionChanged

```java
public void dropActionChanged​(
DragSourceDragEvent
dsde)
```

Calls

dropActionChanged

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceDragEvent

.

**Specified by:** dropActionChanged

in interface

DragSourceListener
**Parameters:** dsde

- the

DragSourceDragEvent

- dragDropEnd

```java
public void dragDropEnd​(
DragSourceDropEvent
dsde)
```

Calls

dragDropEnd

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceDropEvent

.

**Specified by:** dragDropEnd

in interface

DragSourceListener
**Parameters:** dsde

- the

DragSourceDropEvent

- dragMouseMoved

```java
public void dragMouseMoved​(
DragSourceDragEvent
dsde)
```

Calls

dragMouseMoved

on the

DragSourceMotionListener

s registered with the

DragSource

associated with this

DragSourceContext

, and them passes the specified

DragSourceDragEvent

.

**Specified by:** dragMouseMoved

in interface

DragSourceMotionListener
**Parameters:** dsde

- the

DragSourceDragEvent
**Since:** 1.4

- getTransferable

```java
public
Transferable
getTransferable()
```

Returns the

Transferable

associated with
this

DragSourceContext

.

**Returns:** the

Transferable

- updateCurrentCursor

```java
protected void updateCurrentCursor​(int sourceAct,
int targetAct,
int status)
```

If the default drag cursor behavior is active, this method
sets the default drag cursor for the specified actions
supported by the drag source, the drop target action,
and status, otherwise this method does nothing.

**Parameters:** sourceAct

- the actions supported by the drag source
**Parameters:** targetAct

- the drop target action
**Parameters:** status

- one of the fields

DEFAULT

,

ENTER

,

OVER

,

CHANGED

---

#### Method Detail

getDragSource

```java
public
DragSource
getDragSource()
```

Returns the

DragSource

that instantiated this

DragSourceContext

.

**Returns:** the

DragSource

that
instantiated this

DragSourceContext

---

#### getDragSource

public

DragSource

getDragSource()

Returns the

DragSource

that instantiated this

DragSourceContext

.

getComponent

```java
public
Component
getComponent()
```

Returns the

Component

associated with this

DragSourceContext

.

**Returns:** the

Component

that started the drag

---

#### getComponent

public

Component

getComponent()

Returns the

Component

associated with this

DragSourceContext

.

getTrigger

```java
public
DragGestureEvent
getTrigger()
```

Returns the

DragGestureEvent

that initially triggered the drag.

**Returns:** the Event that triggered the drag

---

#### getTrigger

public

DragGestureEvent

getTrigger()

Returns the

DragGestureEvent

that initially triggered the drag.

getSourceActions

```java
public int getSourceActions()
```

Returns a bitwise mask of

DnDConstants

that
represent the set of drop actions supported by the drag source for the
drag operation associated with this

DragSourceContext

.

**Returns:** the drop actions supported by the drag source

---

#### getSourceActions

public int getSourceActions()

Returns a bitwise mask of

DnDConstants

that
represent the set of drop actions supported by the drag source for the
drag operation associated with this

DragSourceContext

.

setCursor

```java
public void setCursor​(
Cursor
c)
```

Sets the custom cursor for this drag operation to the specified

Cursor

. If the specified

Cursor

is

null

, the default drag cursor behavior is
activated for this drag operation, otherwise it is deactivated.

**Parameters:** c

- the initial

Cursor

for this drag operation,
or

null

for the default cursor handling;
see

class
level documentation

for more details
on the cursor handling during drag and drop

---

#### setCursor

public void setCursor​(

Cursor

c)

Sets the custom cursor for this drag operation to the specified

Cursor

. If the specified

Cursor

is

null

, the default drag cursor behavior is
activated for this drag operation, otherwise it is deactivated.

getCursor

```java
public
Cursor
getCursor()
```

Returns the current custom drag

Cursor

.

**Returns:** the current custom drag

Cursor

, if it was set
otherwise returns

null

.
**See Also:** setCursor(java.awt.Cursor)

---

#### getCursor

public

Cursor

getCursor()

Returns the current custom drag

Cursor

.

addDragSourceListener

```java
public void addDragSourceListener​(
DragSourceListener
dsl)
throws
TooManyListenersException
```

Add a

DragSourceListener

to this

DragSourceContext

if one has not already been added.
If a

DragSourceListener

already exists,
this method throws a

TooManyListenersException

.

**Parameters:** dsl

- the

DragSourceListener

to add.
Note that while

null

is not prohibited,
it is not acceptable as a parameter.
**Throws:** TooManyListenersException

- if
a

DragSourceListener

has already been added

---

#### addDragSourceListener

public void addDragSourceListener​(

DragSourceListener

dsl)
throws

TooManyListenersException

Add a

DragSourceListener

to this

DragSourceContext

if one has not already been added.
If a

DragSourceListener

already exists,
this method throws a

TooManyListenersException

.

removeDragSourceListener

```java
public void removeDragSourceListener​(
DragSourceListener
dsl)
```

Removes the specified

DragSourceListener

from this

DragSourceContext

.

**Parameters:** dsl

- the

DragSourceListener

to remove;
note that while

null

is not prohibited,
it is not acceptable as a parameter

---

#### removeDragSourceListener

public void removeDragSourceListener​(

DragSourceListener

dsl)

Removes the specified

DragSourceListener

from this

DragSourceContext

.

transferablesFlavorsChanged

```java
public void transferablesFlavorsChanged()
```

Notifies the peer that the

Transferable

's

DataFlavor

s have changed.

---

#### transferablesFlavorsChanged

public void transferablesFlavorsChanged()

Notifies the peer that the

Transferable

's

DataFlavor

s have changed.

dragEnter

```java
public void dragEnter​(
DragSourceDragEvent
dsde)
```

Calls

dragEnter

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceDragEvent

.

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

Calls

dragEnter

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceDragEvent

.

dragOver

```java
public void dragOver​(
DragSourceDragEvent
dsde)
```

Calls

dragOver

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceDragEvent

.

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

Calls

dragOver

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceDragEvent

.

dragExit

```java
public void dragExit​(
DragSourceEvent
dse)
```

Calls

dragExit

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceEvent

.

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

Calls

dragExit

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceEvent

.

dropActionChanged

```java
public void dropActionChanged​(
DragSourceDragEvent
dsde)
```

Calls

dropActionChanged

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceDragEvent

.

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

Calls

dropActionChanged

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceDragEvent

.

dragDropEnd

```java
public void dragDropEnd​(
DragSourceDropEvent
dsde)
```

Calls

dragDropEnd

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceDropEvent

.

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

Calls

dragDropEnd

on the

DragSourceListener

s registered with this

DragSourceContext

and with the associated

DragSource

, and passes them the specified

DragSourceDropEvent

.

dragMouseMoved

```java
public void dragMouseMoved​(
DragSourceDragEvent
dsde)
```

Calls

dragMouseMoved

on the

DragSourceMotionListener

s registered with the

DragSource

associated with this

DragSourceContext

, and them passes the specified

DragSourceDragEvent

.

**Specified by:** dragMouseMoved

in interface

DragSourceMotionListener
**Parameters:** dsde

- the

DragSourceDragEvent
**Since:** 1.4

---

#### dragMouseMoved

public void dragMouseMoved​(

DragSourceDragEvent

dsde)

Calls

dragMouseMoved

on the

DragSourceMotionListener

s registered with the

DragSource

associated with this

DragSourceContext

, and them passes the specified

DragSourceDragEvent

.

getTransferable

```java
public
Transferable
getTransferable()
```

Returns the

Transferable

associated with
this

DragSourceContext

.

**Returns:** the

Transferable

---

#### getTransferable

public

Transferable

getTransferable()

Returns the

Transferable

associated with
this

DragSourceContext

.

updateCurrentCursor

```java
protected void updateCurrentCursor​(int sourceAct,
int targetAct,
int status)
```

If the default drag cursor behavior is active, this method
sets the default drag cursor for the specified actions
supported by the drag source, the drop target action,
and status, otherwise this method does nothing.

**Parameters:** sourceAct

- the actions supported by the drag source
**Parameters:** targetAct

- the drop target action
**Parameters:** status

- one of the fields

DEFAULT

,

ENTER

,

OVER

,

CHANGED

---

#### updateCurrentCursor

protected void updateCurrentCursor​(int sourceAct,
int targetAct,
int status)

If the default drag cursor behavior is active, this method
sets the default drag cursor for the specified actions
supported by the drag source, the drop target action,
and status, otherwise this method does nothing.

---

