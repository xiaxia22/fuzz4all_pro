# Class DragGestureEvent

**Source:** `java.desktop\java\awt\dnd\DragGestureEvent.html`

### Class Description

```java
public class
DragGestureEvent

extends
EventObject
```

A

DragGestureEvent

is passed
to

DragGestureListener

's
dragGestureRecognized() method
when a particular

DragGestureRecognizer

detects that a
platform dependent drag initiating gesture has occurred
on the

Component

that it is tracking.

The

action

field of any

DragGestureEvent

instance should take one of the following
values:

- DnDConstants.ACTION_COPY

DnDConstants.ACTION_MOVE

DnDConstants.ACTION_LINK

Assigning the value different from listed above will cause an unspecified behavior.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public DragGestureEvent​(
DragGestureRecognizer
dgr,
int act,

Point
ori,

List
<? extends
InputEvent
> evs)

Constructs a

DragGestureEvent

object given by the

DragGestureRecognizer

instance firing this event,
an

act

parameter representing
the user's preferred action, an

ori

parameter
indicating the origin of the drag, and a

List

of
events that comprise the gesture(

evs

parameter).

**Parameters:**
- dgr

- The

DragGestureRecognizer

firing this event
- act

- The user's preferred action.
For information on allowable values, see
the class description for

DragGestureEvent
- ori

- The origin of the drag
- evs

- The

List

of events that comprise the gesture

**Throws:**
- IllegalArgumentException

- if any parameter equals

null
- IllegalArgumentException

- if the act parameter does not comply with
the values given in the class
description for

DragGestureEvent

**See Also:**
- DnDConstants

---

### Method Details

#### public
DragGestureRecognizer
getSourceAsDragGestureRecognizer()

Returns the source as a

DragGestureRecognizer

.

**Returns:**
- the source as a

DragGestureRecognizer

---

#### public
Component
getComponent()

Returns the

Component

associated
with this

DragGestureEvent

.

**Returns:**
- the Component

---

#### public
DragSource
getDragSource()

Returns the

DragSource

.

**Returns:**
- the

DragSource

---

#### public
Point
getDragOrigin()

Returns a

Point

in the coordinates
of the

Component

over which the drag originated.

**Returns:**
- the Point where the drag originated in Component coords.

---

#### public
Iterator
<
InputEvent
> iterator()

Returns an

Iterator

for the events
comprising the gesture.

**Returns:**
- an Iterator for the events comprising the gesture

---

#### public
Object
[] toArray()

Returns an

Object

array of the
events comprising the drag gesture.

**Returns:**
- an array of the events comprising the gesture

---

#### public
Object
[] toArray​(
Object
[] array)

Returns an array of the events comprising the drag gesture.

**Parameters:**
- array

- the array of

EventObject

sub(types)

**Returns:**
- an array of the events comprising the gesture

---

#### public int getDragAction()

Returns an

int

representing the
action selected by the user.

**Returns:**
- the action selected by the user

---

#### public
InputEvent
getTriggerEvent()

Returns the initial event that triggered the gesture.

**Returns:**
- the first "triggering" event in the sequence of the gesture

---

#### public void startDrag​(
Cursor
dragCursor,

Transferable
transferable)
throws
InvalidDnDOperationException

Starts the drag operation given the

Cursor

for this drag
operation and the

Transferable

representing the source data
for this drag operation.

If a

null Cursor

is specified no exception will
be thrown and default drag cursors will be used instead.

If a

null Transferable

is specified

NullPointerException

will be thrown.

**Parameters:**
- dragCursor

- The initial

Cursor

for this drag operation
or

null

for the default cursor handling;
see

DragSourceContext

for more details on the cursor handling mechanism
during drag and drop
- transferable

- The

Transferable

representing the source
data for this drag operation.

**Throws:**
- InvalidDnDOperationException

- if the Drag and Drop
system is unable to initiate a drag operation, or if the user
attempts to start a drag while an existing drag operation is
still executing.
- NullPointerException

- if the

Transferable

is

null

**Since:**
- 1.4

---

#### public void startDrag​(
Cursor
dragCursor,

Transferable
transferable,

DragSourceListener
dsl)
throws
InvalidDnDOperationException

Starts the drag given the initial

Cursor

to display,
the

Transferable

object,
and the

DragSourceListener

to use.

**Parameters:**
- dragCursor

- The initial

Cursor

for this drag operation
or

null

for the default cursor handling;
see

DragSourceContext

for more details on the cursor handling mechanism
during drag and drop
- transferable

- The source's Transferable
- dsl

- The source's DragSourceListener

**Throws:**
- InvalidDnDOperationException

- if
the Drag and Drop system is unable to
initiate a drag operation, or if the user
attempts to start a drag while an existing
drag operation is still executing.

---

#### public void startDrag​(
Cursor
dragCursor,

Image
dragImage,

Point
imageOffset,

Transferable
transferable,

DragSourceListener
dsl)
throws
InvalidDnDOperationException

Start the drag given the initial

Cursor

to display,
a drag

Image

, the offset of
the

Image

,
the

Transferable

object, and
the

DragSourceListener

to use.

**Parameters:**
- dragCursor

- The initial

Cursor

for this drag operation
or

null

for the default cursor handling;
see

DragSourceContext

for more details on the cursor handling mechanism
during drag and drop
- dragImage

- The source's dragImage
- imageOffset

- The dragImage's offset
- transferable

- The source's Transferable
- dsl

- The source's DragSourceListener

**Throws:**
- InvalidDnDOperationException

- if
the Drag and Drop system is unable to
initiate a drag operation, or if the user
attempts to start a drag while an existing
drag operation is still executing.

---

### Additional Sections

#### Class DragGestureEvent

java.lang.Object

- java.util.EventObject
- - java.awt.dnd.DragGestureEvent

java.util.EventObject

- java.awt.dnd.DragGestureEvent

java.awt.dnd.DragGestureEvent

**All Implemented Interfaces:** Serializable

```java
public class
DragGestureEvent

extends
EventObject
```

A

DragGestureEvent

is passed
to

DragGestureListener

's
dragGestureRecognized() method
when a particular

DragGestureRecognizer

detects that a
platform dependent drag initiating gesture has occurred
on the

Component

that it is tracking.

The

action

field of any

DragGestureEvent

instance should take one of the following
values:

- DnDConstants.ACTION_COPY

DnDConstants.ACTION_MOVE

DnDConstants.ACTION_LINK

Assigning the value different from listed above will cause an unspecified behavior.

**See Also:** DragGestureRecognizer

,

DragGestureListener

,

DragSource

,

DnDConstants

,

Serialized Form

public class

DragGestureEvent

extends

EventObject

A

DragGestureEvent

is passed
to

DragGestureListener

's
dragGestureRecognized() method
when a particular

DragGestureRecognizer

detects that a
platform dependent drag initiating gesture has occurred
on the

Component

that it is tracking.

The

action

field of any

DragGestureEvent

instance should take one of the following
values:

- DnDConstants.ACTION_COPY

DnDConstants.ACTION_MOVE

DnDConstants.ACTION_LINK

Assigning the value different from listed above will cause an unspecified behavior.

DnDConstants.ACTION_COPY

DnDConstants.ACTION_MOVE

DnDConstants.ACTION_LINK

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.util.

EventObject

source

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DragGestureEvent

​(

DragGestureRecognizer

dgr,
int act,

Point

ori,

List

<? extends

InputEvent

> evs)

Constructs a

DragGestureEvent

object given by the

DragGestureRecognizer

instance firing this event,
an

act

parameter representing
the user's preferred action, an

ori

parameter
indicating the origin of the drag, and a

List

of
events that comprise the gesture(

evs

parameter).

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Component

getComponent

()

Returns the

Component

associated
with this

DragGestureEvent

.

int

getDragAction

()

Returns an

int

representing the
action selected by the user.

Point

getDragOrigin

()

Returns a

Point

in the coordinates
of the

Component

over which the drag originated.

DragSource

getDragSource

()

Returns the

DragSource

.

DragGestureRecognizer

getSourceAsDragGestureRecognizer

()

Returns the source as a

DragGestureRecognizer

.

InputEvent

getTriggerEvent

()

Returns the initial event that triggered the gesture.

Iterator

<

InputEvent

>

iterator

()

Returns an

Iterator

for the events
comprising the gesture.

void

startDrag

​(

Cursor

dragCursor,

Transferable

transferable)

Starts the drag operation given the

Cursor

for this drag
operation and the

Transferable

representing the source data
for this drag operation.

void

startDrag

​(

Cursor

dragCursor,

Transferable

transferable,

DragSourceListener

dsl)

Starts the drag given the initial

Cursor

to display,
the

Transferable

object,
and the

DragSourceListener

to use.

void

startDrag

​(

Cursor

dragCursor,

Image

dragImage,

Point

imageOffset,

Transferable

transferable,

DragSourceListener

dsl)

Start the drag given the initial

Cursor

to display,
a drag

Image

, the offset of
the

Image

,
the

Transferable

object, and
the

DragSourceListener

to use.

Object

[]

toArray

()

Returns an

Object

array of the
events comprising the drag gesture.

Object

[]

toArray

​(

Object

[] array)

Returns an array of the events comprising the drag gesture.

- Methods declared in class java.util.

EventObject

getSource

,

toString

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

wait

,

wait

,

wait

Field Summary

- Fields declared in class java.util.

EventObject

source

---

#### Field Summary

Fields declared in class java.util.

EventObject

source

---

#### Fields declared in class java.util. EventObject

Constructor Summary

Constructors

Constructor

Description

DragGestureEvent

​(

DragGestureRecognizer

dgr,
int act,

Point

ori,

List

<? extends

InputEvent

> evs)

Constructs a

DragGestureEvent

object given by the

DragGestureRecognizer

instance firing this event,
an

act

parameter representing
the user's preferred action, an

ori

parameter
indicating the origin of the drag, and a

List

of
events that comprise the gesture(

evs

parameter).

---

#### Constructor Summary

Constructs a

DragGestureEvent

object given by the

DragGestureRecognizer

instance firing this event,
an

act

parameter representing
the user's preferred action, an

ori

parameter
indicating the origin of the drag, and a

List

of
events that comprise the gesture(

evs

parameter).

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Component

getComponent

()

Returns the

Component

associated
with this

DragGestureEvent

.

int

getDragAction

()

Returns an

int

representing the
action selected by the user.

Point

getDragOrigin

()

Returns a

Point

in the coordinates
of the

Component

over which the drag originated.

DragSource

getDragSource

()

Returns the

DragSource

.

DragGestureRecognizer

getSourceAsDragGestureRecognizer

()

Returns the source as a

DragGestureRecognizer

.

InputEvent

getTriggerEvent

()

Returns the initial event that triggered the gesture.

Iterator

<

InputEvent

>

iterator

()

Returns an

Iterator

for the events
comprising the gesture.

void

startDrag

​(

Cursor

dragCursor,

Transferable

transferable)

Starts the drag operation given the

Cursor

for this drag
operation and the

Transferable

representing the source data
for this drag operation.

void

startDrag

​(

Cursor

dragCursor,

Transferable

transferable,

DragSourceListener

dsl)

Starts the drag given the initial

Cursor

to display,
the

Transferable

object,
and the

DragSourceListener

to use.

void

startDrag

​(

Cursor

dragCursor,

Image

dragImage,

Point

imageOffset,

Transferable

transferable,

DragSourceListener

dsl)

Start the drag given the initial

Cursor

to display,
a drag

Image

, the offset of
the

Image

,
the

Transferable

object, and
the

DragSourceListener

to use.

Object

[]

toArray

()

Returns an

Object

array of the
events comprising the drag gesture.

Object

[]

toArray

​(

Object

[] array)

Returns an array of the events comprising the drag gesture.

- Methods declared in class java.util.

EventObject

getSource

,

toString

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

wait

,

wait

,

wait

---

#### Method Summary

Returns the

Component

associated
with this

DragGestureEvent

.

Returns an

int

representing the
action selected by the user.

Returns a

Point

in the coordinates
of the

Component

over which the drag originated.

Returns the

DragSource

.

Returns the source as a

DragGestureRecognizer

.

Returns the initial event that triggered the gesture.

Returns an

Iterator

for the events
comprising the gesture.

Starts the drag operation given the

Cursor

for this drag
operation and the

Transferable

representing the source data
for this drag operation.

Starts the drag given the initial

Cursor

to display,
the

Transferable

object,
and the

DragSourceListener

to use.

Start the drag given the initial

Cursor

to display,
a drag

Image

, the offset of
the

Image

,
the

Transferable

object, and
the

DragSourceListener

to use.

Returns an

Object

array of the
events comprising the drag gesture.

Returns an array of the events comprising the drag gesture.

Methods declared in class java.util.

EventObject

getSource

,

toString

---

#### Methods declared in class java.util. EventObject

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DragGestureEvent

```java
public DragGestureEvent​(
DragGestureRecognizer
dgr,
int act,

Point
ori,

List
<? extends
InputEvent
> evs)
```

Constructs a

DragGestureEvent

object given by the

DragGestureRecognizer

instance firing this event,
an

act

parameter representing
the user's preferred action, an

ori

parameter
indicating the origin of the drag, and a

List

of
events that comprise the gesture(

evs

parameter).

**Parameters:** dgr

- The

DragGestureRecognizer

firing this event
**Parameters:** act

- The user's preferred action.
For information on allowable values, see
the class description for

DragGestureEvent
**Parameters:** ori

- The origin of the drag
**Parameters:** evs

- The

List

of events that comprise the gesture
**Throws:** IllegalArgumentException

- if any parameter equals

null
**Throws:** IllegalArgumentException

- if the act parameter does not comply with
the values given in the class
description for

DragGestureEvent
**See Also:** DnDConstants

============ METHOD DETAIL ==========

- Method Detail

- getSourceAsDragGestureRecognizer

```java
public
DragGestureRecognizer
getSourceAsDragGestureRecognizer()
```

Returns the source as a

DragGestureRecognizer

.

**Returns:** the source as a

DragGestureRecognizer

- getComponent

```java
public
Component
getComponent()
```

Returns the

Component

associated
with this

DragGestureEvent

.

**Returns:** the Component

- getDragSource

```java
public
DragSource
getDragSource()
```

Returns the

DragSource

.

**Returns:** the

DragSource

- getDragOrigin

```java
public
Point
getDragOrigin()
```

Returns a

Point

in the coordinates
of the

Component

over which the drag originated.

**Returns:** the Point where the drag originated in Component coords.

- iterator

```java
public
Iterator
<
InputEvent
> iterator()
```

Returns an

Iterator

for the events
comprising the gesture.

**Returns:** an Iterator for the events comprising the gesture

- toArray

```java
public
Object
[] toArray()
```

Returns an

Object

array of the
events comprising the drag gesture.

**Returns:** an array of the events comprising the gesture

- toArray

```java
public
Object
[] toArray​(
Object
[] array)
```

Returns an array of the events comprising the drag gesture.

**Parameters:** array

- the array of

EventObject

sub(types)
**Returns:** an array of the events comprising the gesture

- getDragAction

```java
public int getDragAction()
```

Returns an

int

representing the
action selected by the user.

**Returns:** the action selected by the user

- getTriggerEvent

```java
public
InputEvent
getTriggerEvent()
```

Returns the initial event that triggered the gesture.

**Returns:** the first "triggering" event in the sequence of the gesture

- startDrag

```java
public void startDrag​(
Cursor
dragCursor,

Transferable
transferable)
throws
InvalidDnDOperationException
```

Starts the drag operation given the

Cursor

for this drag
operation and the

Transferable

representing the source data
for this drag operation.

If a

null Cursor

is specified no exception will
be thrown and default drag cursors will be used instead.

If a

null Transferable

is specified

NullPointerException

will be thrown.

**Parameters:** dragCursor

- The initial

Cursor

for this drag operation
or

null

for the default cursor handling;
see

DragSourceContext

for more details on the cursor handling mechanism
during drag and drop
**Parameters:** transferable

- The

Transferable

representing the source
data for this drag operation.
**Throws:** InvalidDnDOperationException

- if the Drag and Drop
system is unable to initiate a drag operation, or if the user
attempts to start a drag while an existing drag operation is
still executing.
**Throws:** NullPointerException

- if the

Transferable

is

null
**Since:** 1.4

- startDrag

```java
public void startDrag​(
Cursor
dragCursor,

Transferable
transferable,

DragSourceListener
dsl)
throws
InvalidDnDOperationException
```

Starts the drag given the initial

Cursor

to display,
the

Transferable

object,
and the

DragSourceListener

to use.

**Parameters:** dragCursor

- The initial

Cursor

for this drag operation
or

null

for the default cursor handling;
see

DragSourceContext

for more details on the cursor handling mechanism
during drag and drop
**Parameters:** transferable

- The source's Transferable
**Parameters:** dsl

- The source's DragSourceListener
**Throws:** InvalidDnDOperationException

- if
the Drag and Drop system is unable to
initiate a drag operation, or if the user
attempts to start a drag while an existing
drag operation is still executing.

- startDrag

```java
public void startDrag​(
Cursor
dragCursor,

Image
dragImage,

Point
imageOffset,

Transferable
transferable,

DragSourceListener
dsl)
throws
InvalidDnDOperationException
```

Start the drag given the initial

Cursor

to display,
a drag

Image

, the offset of
the

Image

,
the

Transferable

object, and
the

DragSourceListener

to use.

**Parameters:** dragCursor

- The initial

Cursor

for this drag operation
or

null

for the default cursor handling;
see

DragSourceContext

for more details on the cursor handling mechanism
during drag and drop
**Parameters:** dragImage

- The source's dragImage
**Parameters:** imageOffset

- The dragImage's offset
**Parameters:** transferable

- The source's Transferable
**Parameters:** dsl

- The source's DragSourceListener
**Throws:** InvalidDnDOperationException

- if
the Drag and Drop system is unable to
initiate a drag operation, or if the user
attempts to start a drag while an existing
drag operation is still executing.

Constructor Detail

- DragGestureEvent

```java
public DragGestureEvent​(
DragGestureRecognizer
dgr,
int act,

Point
ori,

List
<? extends
InputEvent
> evs)
```

Constructs a

DragGestureEvent

object given by the

DragGestureRecognizer

instance firing this event,
an

act

parameter representing
the user's preferred action, an

ori

parameter
indicating the origin of the drag, and a

List

of
events that comprise the gesture(

evs

parameter).

**Parameters:** dgr

- The

DragGestureRecognizer

firing this event
**Parameters:** act

- The user's preferred action.
For information on allowable values, see
the class description for

DragGestureEvent
**Parameters:** ori

- The origin of the drag
**Parameters:** evs

- The

List

of events that comprise the gesture
**Throws:** IllegalArgumentException

- if any parameter equals

null
**Throws:** IllegalArgumentException

- if the act parameter does not comply with
the values given in the class
description for

DragGestureEvent
**See Also:** DnDConstants

---

#### Constructor Detail

DragGestureEvent

```java
public DragGestureEvent​(
DragGestureRecognizer
dgr,
int act,

Point
ori,

List
<? extends
InputEvent
> evs)
```

Constructs a

DragGestureEvent

object given by the

DragGestureRecognizer

instance firing this event,
an

act

parameter representing
the user's preferred action, an

ori

parameter
indicating the origin of the drag, and a

List

of
events that comprise the gesture(

evs

parameter).

**Parameters:** dgr

- The

DragGestureRecognizer

firing this event
**Parameters:** act

- The user's preferred action.
For information on allowable values, see
the class description for

DragGestureEvent
**Parameters:** ori

- The origin of the drag
**Parameters:** evs

- The

List

of events that comprise the gesture
**Throws:** IllegalArgumentException

- if any parameter equals

null
**Throws:** IllegalArgumentException

- if the act parameter does not comply with
the values given in the class
description for

DragGestureEvent
**See Also:** DnDConstants

---

#### DragGestureEvent

public DragGestureEvent​(

DragGestureRecognizer

dgr,
int act,

Point

ori,

List

<? extends

InputEvent

> evs)

Constructs a

DragGestureEvent

object given by the

DragGestureRecognizer

instance firing this event,
an

act

parameter representing
the user's preferred action, an

ori

parameter
indicating the origin of the drag, and a

List

of
events that comprise the gesture(

evs

parameter).

Method Detail

- getSourceAsDragGestureRecognizer

```java
public
DragGestureRecognizer
getSourceAsDragGestureRecognizer()
```

Returns the source as a

DragGestureRecognizer

.

**Returns:** the source as a

DragGestureRecognizer

- getComponent

```java
public
Component
getComponent()
```

Returns the

Component

associated
with this

DragGestureEvent

.

**Returns:** the Component

- getDragSource

```java
public
DragSource
getDragSource()
```

Returns the

DragSource

.

**Returns:** the

DragSource

- getDragOrigin

```java
public
Point
getDragOrigin()
```

Returns a

Point

in the coordinates
of the

Component

over which the drag originated.

**Returns:** the Point where the drag originated in Component coords.

- iterator

```java
public
Iterator
<
InputEvent
> iterator()
```

Returns an

Iterator

for the events
comprising the gesture.

**Returns:** an Iterator for the events comprising the gesture

- toArray

```java
public
Object
[] toArray()
```

Returns an

Object

array of the
events comprising the drag gesture.

**Returns:** an array of the events comprising the gesture

- toArray

```java
public
Object
[] toArray​(
Object
[] array)
```

Returns an array of the events comprising the drag gesture.

**Parameters:** array

- the array of

EventObject

sub(types)
**Returns:** an array of the events comprising the gesture

- getDragAction

```java
public int getDragAction()
```

Returns an

int

representing the
action selected by the user.

**Returns:** the action selected by the user

- getTriggerEvent

```java
public
InputEvent
getTriggerEvent()
```

Returns the initial event that triggered the gesture.

**Returns:** the first "triggering" event in the sequence of the gesture

- startDrag

```java
public void startDrag​(
Cursor
dragCursor,

Transferable
transferable)
throws
InvalidDnDOperationException
```

Starts the drag operation given the

Cursor

for this drag
operation and the

Transferable

representing the source data
for this drag operation.

If a

null Cursor

is specified no exception will
be thrown and default drag cursors will be used instead.

If a

null Transferable

is specified

NullPointerException

will be thrown.

**Parameters:** dragCursor

- The initial

Cursor

for this drag operation
or

null

for the default cursor handling;
see

DragSourceContext

for more details on the cursor handling mechanism
during drag and drop
**Parameters:** transferable

- The

Transferable

representing the source
data for this drag operation.
**Throws:** InvalidDnDOperationException

- if the Drag and Drop
system is unable to initiate a drag operation, or if the user
attempts to start a drag while an existing drag operation is
still executing.
**Throws:** NullPointerException

- if the

Transferable

is

null
**Since:** 1.4

- startDrag

```java
public void startDrag​(
Cursor
dragCursor,

Transferable
transferable,

DragSourceListener
dsl)
throws
InvalidDnDOperationException
```

Starts the drag given the initial

Cursor

to display,
the

Transferable

object,
and the

DragSourceListener

to use.

**Parameters:** dragCursor

- The initial

Cursor

for this drag operation
or

null

for the default cursor handling;
see

DragSourceContext

for more details on the cursor handling mechanism
during drag and drop
**Parameters:** transferable

- The source's Transferable
**Parameters:** dsl

- The source's DragSourceListener
**Throws:** InvalidDnDOperationException

- if
the Drag and Drop system is unable to
initiate a drag operation, or if the user
attempts to start a drag while an existing
drag operation is still executing.

- startDrag

```java
public void startDrag​(
Cursor
dragCursor,

Image
dragImage,

Point
imageOffset,

Transferable
transferable,

DragSourceListener
dsl)
throws
InvalidDnDOperationException
```

Start the drag given the initial

Cursor

to display,
a drag

Image

, the offset of
the

Image

,
the

Transferable

object, and
the

DragSourceListener

to use.

**Parameters:** dragCursor

- The initial

Cursor

for this drag operation
or

null

for the default cursor handling;
see

DragSourceContext

for more details on the cursor handling mechanism
during drag and drop
**Parameters:** dragImage

- The source's dragImage
**Parameters:** imageOffset

- The dragImage's offset
**Parameters:** transferable

- The source's Transferable
**Parameters:** dsl

- The source's DragSourceListener
**Throws:** InvalidDnDOperationException

- if
the Drag and Drop system is unable to
initiate a drag operation, or if the user
attempts to start a drag while an existing
drag operation is still executing.

---

#### Method Detail

getSourceAsDragGestureRecognizer

```java
public
DragGestureRecognizer
getSourceAsDragGestureRecognizer()
```

Returns the source as a

DragGestureRecognizer

.

**Returns:** the source as a

DragGestureRecognizer

---

#### getSourceAsDragGestureRecognizer

public

DragGestureRecognizer

getSourceAsDragGestureRecognizer()

Returns the source as a

DragGestureRecognizer

.

getComponent

```java
public
Component
getComponent()
```

Returns the

Component

associated
with this

DragGestureEvent

.

**Returns:** the Component

---

#### getComponent

public

Component

getComponent()

Returns the

Component

associated
with this

DragGestureEvent

.

getDragSource

```java
public
DragSource
getDragSource()
```

Returns the

DragSource

.

**Returns:** the

DragSource

---

#### getDragSource

public

DragSource

getDragSource()

Returns the

DragSource

.

getDragOrigin

```java
public
Point
getDragOrigin()
```

Returns a

Point

in the coordinates
of the

Component

over which the drag originated.

**Returns:** the Point where the drag originated in Component coords.

---

#### getDragOrigin

public

Point

getDragOrigin()

Returns a

Point

in the coordinates
of the

Component

over which the drag originated.

iterator

```java
public
Iterator
<
InputEvent
> iterator()
```

Returns an

Iterator

for the events
comprising the gesture.

**Returns:** an Iterator for the events comprising the gesture

---

#### iterator

public

Iterator

<

InputEvent

> iterator()

Returns an

Iterator

for the events
comprising the gesture.

toArray

```java
public
Object
[] toArray()
```

Returns an

Object

array of the
events comprising the drag gesture.

**Returns:** an array of the events comprising the gesture

---

#### toArray

public

Object

[] toArray()

Returns an

Object

array of the
events comprising the drag gesture.

toArray

```java
public
Object
[] toArray​(
Object
[] array)
```

Returns an array of the events comprising the drag gesture.

**Parameters:** array

- the array of

EventObject

sub(types)
**Returns:** an array of the events comprising the gesture

---

#### toArray

public

Object

[] toArray​(

Object

[] array)

Returns an array of the events comprising the drag gesture.

getDragAction

```java
public int getDragAction()
```

Returns an

int

representing the
action selected by the user.

**Returns:** the action selected by the user

---

#### getDragAction

public int getDragAction()

Returns an

int

representing the
action selected by the user.

getTriggerEvent

```java
public
InputEvent
getTriggerEvent()
```

Returns the initial event that triggered the gesture.

**Returns:** the first "triggering" event in the sequence of the gesture

---

#### getTriggerEvent

public

InputEvent

getTriggerEvent()

Returns the initial event that triggered the gesture.

startDrag

```java
public void startDrag​(
Cursor
dragCursor,

Transferable
transferable)
throws
InvalidDnDOperationException
```

Starts the drag operation given the

Cursor

for this drag
operation and the

Transferable

representing the source data
for this drag operation.

If a

null Cursor

is specified no exception will
be thrown and default drag cursors will be used instead.

If a

null Transferable

is specified

NullPointerException

will be thrown.

**Parameters:** dragCursor

- The initial

Cursor

for this drag operation
or

null

for the default cursor handling;
see

DragSourceContext

for more details on the cursor handling mechanism
during drag and drop
**Parameters:** transferable

- The

Transferable

representing the source
data for this drag operation.
**Throws:** InvalidDnDOperationException

- if the Drag and Drop
system is unable to initiate a drag operation, or if the user
attempts to start a drag while an existing drag operation is
still executing.
**Throws:** NullPointerException

- if the

Transferable

is

null
**Since:** 1.4

---

#### startDrag

public void startDrag​(

Cursor

dragCursor,

Transferable

transferable)
throws

InvalidDnDOperationException

Starts the drag operation given the

Cursor

for this drag
operation and the

Transferable

representing the source data
for this drag operation.

If a

null Cursor

is specified no exception will
be thrown and default drag cursors will be used instead.

If a

null Transferable

is specified

NullPointerException

will be thrown.

startDrag

```java
public void startDrag​(
Cursor
dragCursor,

Transferable
transferable,

DragSourceListener
dsl)
throws
InvalidDnDOperationException
```

Starts the drag given the initial

Cursor

to display,
the

Transferable

object,
and the

DragSourceListener

to use.

**Parameters:** dragCursor

- The initial

Cursor

for this drag operation
or

null

for the default cursor handling;
see

DragSourceContext

for more details on the cursor handling mechanism
during drag and drop
**Parameters:** transferable

- The source's Transferable
**Parameters:** dsl

- The source's DragSourceListener
**Throws:** InvalidDnDOperationException

- if
the Drag and Drop system is unable to
initiate a drag operation, or if the user
attempts to start a drag while an existing
drag operation is still executing.

---

#### startDrag

public void startDrag​(

Cursor

dragCursor,

Transferable

transferable,

DragSourceListener

dsl)
throws

InvalidDnDOperationException

Starts the drag given the initial

Cursor

to display,
the

Transferable

object,
and the

DragSourceListener

to use.

startDrag

```java
public void startDrag​(
Cursor
dragCursor,

Image
dragImage,

Point
imageOffset,

Transferable
transferable,

DragSourceListener
dsl)
throws
InvalidDnDOperationException
```

Start the drag given the initial

Cursor

to display,
a drag

Image

, the offset of
the

Image

,
the

Transferable

object, and
the

DragSourceListener

to use.

**Parameters:** dragCursor

- The initial

Cursor

for this drag operation
or

null

for the default cursor handling;
see

DragSourceContext

for more details on the cursor handling mechanism
during drag and drop
**Parameters:** dragImage

- The source's dragImage
**Parameters:** imageOffset

- The dragImage's offset
**Parameters:** transferable

- The source's Transferable
**Parameters:** dsl

- The source's DragSourceListener
**Throws:** InvalidDnDOperationException

- if
the Drag and Drop system is unable to
initiate a drag operation, or if the user
attempts to start a drag while an existing
drag operation is still executing.

---

#### startDrag

public void startDrag​(

Cursor

dragCursor,

Image

dragImage,

Point

imageOffset,

Transferable

transferable,

DragSourceListener

dsl)
throws

InvalidDnDOperationException

Start the drag given the initial

Cursor

to display,
a drag

Image

, the offset of
the

Image

,
the

Transferable

object, and
the

DragSourceListener

to use.

---

