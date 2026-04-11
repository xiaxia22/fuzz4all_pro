# Class DragGestureRecognizer

**Source:** `java.desktop\java\awt\dnd\DragGestureRecognizer.html`

### Class Description

```java
public abstract class
DragGestureRecognizer

extends
Object

implements
Serializable
```

The

DragGestureRecognizer

is an
abstract base class for the specification
of a platform-dependent listener that can be associated with a particular

Component

in order to
identify platform-dependent drag initiating gestures.

The appropriate

DragGestureRecognizer

subclass instance is obtained from the

DragSource

associated with
a particular

Component

, or from the

Toolkit

object via its

createDragGestureRecognizer()

method.

Once the

DragGestureRecognizer

is associated with a particular

Component

it will register the appropriate listener interfaces on that

Component

in order to track the input events delivered to the

Component

.

Once the

DragGestureRecognizer

identifies a sequence of events
on the

Component

as a drag initiating gesture, it will notify
its unicast

DragGestureListener

by
invoking its

gestureRecognized()

method.

When a concrete

DragGestureRecognizer

instance detects a drag initiating
gesture on the

Component

it is associated with,
it fires a

DragGestureEvent

to
the

DragGestureListener

registered on
its unicast event source for

DragGestureListener

events. This

DragGestureListener

is responsible
for causing the associated

DragSource

to start the Drag and Drop operation (if
appropriate).

**All Implemented Interfaces:** Serializable

---

### Field Details

#### protected
DragSource
dragSource

The

DragSource

associated with this

DragGestureRecognizer

.

---

#### protected
Component
component

The

Component

associated with this

DragGestureRecognizer

.

---

#### protected transient
DragGestureListener
dragGestureListener

The

DragGestureListener

associated with this

DragGestureRecognizer

.

---

#### protected int sourceActions

An

int

representing
the type(s) of action(s) used
in this Drag and Drop operation.

---

#### protected
ArrayList
<
InputEvent
> events

The list of events (in order) that
the

DragGestureRecognizer

"recognized" as a "gesture" that triggers a drag.

---

### Constructor Details

#### protected DragGestureRecognizer​(
DragSource
ds,

Component
c,
int sa,

DragGestureListener
dgl)

Construct a new

DragGestureRecognizer

given the

DragSource

to be used
in this Drag and Drop operation, the

Component

this

DragGestureRecognizer

should "observe"
for drag initiating gestures, the action(s) supported
for this Drag and Drop operation, and the

DragGestureListener

to notify
once a drag initiating gesture has been detected.

**Parameters:**
- ds

- the

DragSource

this

DragGestureRecognizer

will use to process the Drag and Drop operation
- c

- the

Component

this

DragGestureRecognizer

should "observe" the event stream to,
in order to detect a drag initiating gesture.
If this value is

null

, the

DragGestureRecognizer

is not associated with any

Component

.
- sa

- the set (logical OR) of the

DnDConstants

that this Drag and Drop operation will support
- dgl

- the

DragGestureRecognizer

to notify when a drag gesture is detected

**Throws:**
- IllegalArgumentException

- if ds is

null

.

---

#### protected DragGestureRecognizer​(
DragSource
ds,

Component
c,
int sa)

Construct a new

DragGestureRecognizer

given the

DragSource

to be used in this
Drag and Drop
operation, the

Component

this

DragGestureRecognizer

should "observe"
for drag initiating gestures, and the action(s)
supported for this Drag and Drop operation.

**Parameters:**
- ds

- the

DragSource

this

DragGestureRecognizer

will use to
process the Drag and Drop operation
- c

- the

Component

this

DragGestureRecognizer

should "observe" the event
stream to, in order to detect a drag initiating gesture.
If this value is

null

, the

DragGestureRecognizer

is not associated with any

Component

.
- sa

- the set (logical OR) of the

DnDConstants

that this Drag and Drop operation will support

**Throws:**
- IllegalArgumentException

- if ds is

null

.

---

#### protected DragGestureRecognizer​(
DragSource
ds,

Component
c)

Construct a new

DragGestureRecognizer

given the

DragSource

to be used
in this Drag and Drop operation, and
the

Component

this

DragGestureRecognizer

should "observe" for drag initiating gestures.

**Parameters:**
- ds

- the

DragSource

this

DragGestureRecognizer

will use to process the Drag and Drop operation
- c

- the

Component

this

DragGestureRecognizer

should "observe" the event stream to,
in order to detect a drag initiating gesture.
If this value is

null

,
the

DragGestureRecognizer

is not associated with any

Component

.

**Throws:**
- IllegalArgumentException

- if ds is

null

.

---

#### protected DragGestureRecognizer​(
DragSource
ds)

Construct a new

DragGestureRecognizer

given the

DragSource

to be used in this
Drag and Drop operation.

**Parameters:**
- ds

- the

DragSource

this

DragGestureRecognizer

will
use to process the Drag and Drop operation

**Throws:**
- IllegalArgumentException

- if ds is

null

.

---

### Method Details

#### protected abstract void registerListeners()

register this DragGestureRecognizer's Listeners with the Component

subclasses must override this method

---

#### protected abstract void unregisterListeners()

unregister this DragGestureRecognizer's Listeners with the Component

subclasses must override this method

---

#### public
DragSource
getDragSource()

This method returns the

DragSource

this

DragGestureRecognizer

will use in order to process the Drag and Drop
operation.

**Returns:**
- the DragSource

---

#### public
Component
getComponent()

This method returns the

Component

that is to be "observed" by the

DragGestureRecognizer

for drag initiating gestures.

**Returns:**
- The Component this DragGestureRecognizer
is associated with

---

#### public void setComponent​(
Component
c)

set the Component that the DragGestureRecognizer is associated with

registerListeners() and unregisterListeners() are called as a side
effect as appropriate.

**Parameters:**
- c

- The

Component

or

null

---

#### public int getSourceActions()

This method returns an int representing the
type of action(s) this Drag and Drop
operation will support.

**Returns:**
- the currently permitted source action(s)

---

#### public void setSourceActions​(int actions)

This method sets the permitted source drag action(s)
for this Drag and Drop operation.

**Parameters:**
- actions

- the permitted source drag action(s)

---

#### public
InputEvent
getTriggerEvent()

This method returns the first event in the
series of events that initiated
the Drag and Drop operation.

**Returns:**
- the initial event that triggered the drag gesture

---

#### public void resetRecognizer()

Reset the Recognizer, if its currently recognizing a gesture, ignore
it.

---

#### public void addDragGestureListener​(
DragGestureListener
dgl)
throws
TooManyListenersException

Register a new

DragGestureListener

.

**Parameters:**
- dgl

- the

DragGestureListener

to register
with this

DragGestureRecognizer

.

**Throws:**
- TooManyListenersException

- if a

DragGestureListener

has already been added.

---

#### public void removeDragGestureListener​(
DragGestureListener
dgl)

unregister the current DragGestureListener

**Parameters:**
- dgl

- the

DragGestureListener

to unregister
from this

DragGestureRecognizer

**Throws:**
- IllegalArgumentException

- if
dgl is not (equal to) the currently registered

DragGestureListener

.

---

#### protected void fireDragGestureRecognized​(int dragAction,

Point
p)

Notify the DragGestureListener that a Drag and Drop initiating
gesture has occurred. Then reset the state of the Recognizer.

**Parameters:**
- dragAction

- The action initially selected by the users gesture
- p

- The point (in Component coords) where the gesture originated

---

#### protected void appendEvent​(
InputEvent
awtie)

Listeners registered on the Component by this Recognizer shall record
all Events that are recognized as part of the series of Events that go
to comprise a Drag and Drop initiating gesture via this API.

This method is used by a

DragGestureRecognizer

implementation to add an

InputEvent

subclass (that it believes is one in a series
of events that comprise a Drag and Drop operation)
to the array of events that this

DragGestureRecognizer

maintains internally.

**Parameters:**
- awtie

- the

InputEvent

to add to this

DragGestureRecognizer

's
internal array of events. Note that

null

is not a valid value, and will be ignored.

---

### Additional Sections

#### Class DragGestureRecognizer

java.lang.Object

- java.awt.dnd.DragGestureRecognizer

java.awt.dnd.DragGestureRecognizer

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** MouseDragGestureRecognizer

```java
public abstract class
DragGestureRecognizer

extends
Object

implements
Serializable
```

The

DragGestureRecognizer

is an
abstract base class for the specification
of a platform-dependent listener that can be associated with a particular

Component

in order to
identify platform-dependent drag initiating gestures.

The appropriate

DragGestureRecognizer

subclass instance is obtained from the

DragSource

associated with
a particular

Component

, or from the

Toolkit

object via its

createDragGestureRecognizer()

method.

Once the

DragGestureRecognizer

is associated with a particular

Component

it will register the appropriate listener interfaces on that

Component

in order to track the input events delivered to the

Component

.

Once the

DragGestureRecognizer

identifies a sequence of events
on the

Component

as a drag initiating gesture, it will notify
its unicast

DragGestureListener

by
invoking its

gestureRecognized()

method.

When a concrete

DragGestureRecognizer

instance detects a drag initiating
gesture on the

Component

it is associated with,
it fires a

DragGestureEvent

to
the

DragGestureListener

registered on
its unicast event source for

DragGestureListener

events. This

DragGestureListener

is responsible
for causing the associated

DragSource

to start the Drag and Drop operation (if
appropriate).

**See Also:** DragGestureListener

,

DragGestureEvent

,

DragSource

,

Serialized Form

public abstract class

DragGestureRecognizer

extends

Object

implements

Serializable

The

DragGestureRecognizer

is an
abstract base class for the specification
of a platform-dependent listener that can be associated with a particular

Component

in order to
identify platform-dependent drag initiating gestures.

The appropriate

DragGestureRecognizer

subclass instance is obtained from the

DragSource

associated with
a particular

Component

, or from the

Toolkit

object via its

createDragGestureRecognizer()

method.

Once the

DragGestureRecognizer

is associated with a particular

Component

it will register the appropriate listener interfaces on that

Component

in order to track the input events delivered to the

Component

.

Once the

DragGestureRecognizer

identifies a sequence of events
on the

Component

as a drag initiating gesture, it will notify
its unicast

DragGestureListener

by
invoking its

gestureRecognized()

method.

When a concrete

DragGestureRecognizer

instance detects a drag initiating
gesture on the

Component

it is associated with,
it fires a

DragGestureEvent

to
the

DragGestureListener

registered on
its unicast event source for

DragGestureListener

events. This

DragGestureListener

is responsible
for causing the associated

DragSource

to start the Drag and Drop operation (if
appropriate).

The appropriate

DragGestureRecognizer

subclass instance is obtained from the

DragSource

associated with
a particular

Component

, or from the

Toolkit

object via its

createDragGestureRecognizer()

method.

Once the

DragGestureRecognizer

is associated with a particular

Component

it will register the appropriate listener interfaces on that

Component

in order to track the input events delivered to the

Component

.

Once the

DragGestureRecognizer

identifies a sequence of events
on the

Component

as a drag initiating gesture, it will notify
its unicast

DragGestureListener

by
invoking its

gestureRecognized()

method.

When a concrete

DragGestureRecognizer

instance detects a drag initiating
gesture on the

Component

it is associated with,
it fires a

DragGestureEvent

to
the

DragGestureListener

registered on
its unicast event source for

DragGestureListener

events. This

DragGestureListener

is responsible
for causing the associated

DragSource

to start the Drag and Drop operation (if
appropriate).

Once the

DragGestureRecognizer

is associated with a particular

Component

it will register the appropriate listener interfaces on that

Component

in order to track the input events delivered to the

Component

.

Once the

DragGestureRecognizer

identifies a sequence of events
on the

Component

as a drag initiating gesture, it will notify
its unicast

DragGestureListener

by
invoking its

gestureRecognized()

method.

When a concrete

DragGestureRecognizer

instance detects a drag initiating
gesture on the

Component

it is associated with,
it fires a

DragGestureEvent

to
the

DragGestureListener

registered on
its unicast event source for

DragGestureListener

events. This

DragGestureListener

is responsible
for causing the associated

DragSource

to start the Drag and Drop operation (if
appropriate).

Once the

DragGestureRecognizer

identifies a sequence of events
on the

Component

as a drag initiating gesture, it will notify
its unicast

DragGestureListener

by
invoking its

gestureRecognized()

method.

When a concrete

DragGestureRecognizer

instance detects a drag initiating
gesture on the

Component

it is associated with,
it fires a

DragGestureEvent

to
the

DragGestureListener

registered on
its unicast event source for

DragGestureListener

events. This

DragGestureListener

is responsible
for causing the associated

DragSource

to start the Drag and Drop operation (if
appropriate).

When a concrete

DragGestureRecognizer

instance detects a drag initiating
gesture on the

Component

it is associated with,
it fires a

DragGestureEvent

to
the

DragGestureListener

registered on
its unicast event source for

DragGestureListener

events. This

DragGestureListener

is responsible
for causing the associated

DragSource

to start the Drag and Drop operation (if
appropriate).

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Component

component

The

Component

associated with this

DragGestureRecognizer

.

protected

DragGestureListener

dragGestureListener

The

DragGestureListener

associated with this

DragGestureRecognizer

.

protected

DragSource

dragSource

The

DragSource

associated with this

DragGestureRecognizer

.

protected

ArrayList

<

InputEvent

>

events

The list of events (in order) that
the

DragGestureRecognizer

"recognized" as a "gesture" that triggers a drag.

protected int

sourceActions

An

int

representing
the type(s) of action(s) used
in this Drag and Drop operation.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

DragGestureRecognizer

​(

DragSource

ds)

Construct a new

DragGestureRecognizer

given the

DragSource

to be used in this
Drag and Drop operation.

protected

DragGestureRecognizer

​(

DragSource

ds,

Component

c)

Construct a new

DragGestureRecognizer

given the

DragSource

to be used
in this Drag and Drop operation, and
the

Component

this

DragGestureRecognizer

should "observe" for drag initiating gestures.

protected

DragGestureRecognizer

​(

DragSource

ds,

Component

c,
int sa)

Construct a new

DragGestureRecognizer

given the

DragSource

to be used in this
Drag and Drop
operation, the

Component

this

DragGestureRecognizer

should "observe"
for drag initiating gestures, and the action(s)
supported for this Drag and Drop operation.

protected

DragGestureRecognizer

​(

DragSource

ds,

Component

c,
int sa,

DragGestureListener

dgl)

Construct a new

DragGestureRecognizer

given the

DragSource

to be used
in this Drag and Drop operation, the

Component

this

DragGestureRecognizer

should "observe"
for drag initiating gestures, the action(s) supported
for this Drag and Drop operation, and the

DragGestureListener

to notify
once a drag initiating gesture has been detected.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

void

addDragGestureListener

​(

DragGestureListener

dgl)

Register a new

DragGestureListener

.

protected void

appendEvent

​(

InputEvent

awtie)

Listeners registered on the Component by this Recognizer shall record
all Events that are recognized as part of the series of Events that go
to comprise a Drag and Drop initiating gesture via this API.

protected void

fireDragGestureRecognized

​(int dragAction,

Point

p)

Notify the DragGestureListener that a Drag and Drop initiating
gesture has occurred.

Component

getComponent

()

This method returns the

Component

that is to be "observed" by the

DragGestureRecognizer

for drag initiating gestures.

DragSource

getDragSource

()

This method returns the

DragSource

this

DragGestureRecognizer

will use in order to process the Drag and Drop
operation.

int

getSourceActions

()

This method returns an int representing the
type of action(s) this Drag and Drop
operation will support.

InputEvent

getTriggerEvent

()

This method returns the first event in the
series of events that initiated
the Drag and Drop operation.

protected abstract void

registerListeners

()

register this DragGestureRecognizer's Listeners with the Component

subclasses must override this method

void

removeDragGestureListener

​(

DragGestureListener

dgl)

unregister the current DragGestureListener

void

resetRecognizer

()

Reset the Recognizer, if its currently recognizing a gesture, ignore
it.

void

setComponent

​(

Component

c)

set the Component that the DragGestureRecognizer is associated with

registerListeners() and unregisterListeners() are called as a side
effect as appropriate.

void

setSourceActions

​(int actions)

This method sets the permitted source drag action(s)
for this Drag and Drop operation.

protected abstract void

unregisterListeners

()

unregister this DragGestureRecognizer's Listeners with the Component

subclasses must override this method

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

protected

Component

component

The

Component

associated with this

DragGestureRecognizer

.

protected

DragGestureListener

dragGestureListener

The

DragGestureListener

associated with this

DragGestureRecognizer

.

protected

DragSource

dragSource

The

DragSource

associated with this

DragGestureRecognizer

.

protected

ArrayList

<

InputEvent

>

events

The list of events (in order) that
the

DragGestureRecognizer

"recognized" as a "gesture" that triggers a drag.

protected int

sourceActions

An

int

representing
the type(s) of action(s) used
in this Drag and Drop operation.

---

#### Field Summary

The

Component

associated with this

DragGestureRecognizer

.

The

DragGestureListener

associated with this

DragGestureRecognizer

.

The

DragSource

associated with this

DragGestureRecognizer

.

The list of events (in order) that
the

DragGestureRecognizer

"recognized" as a "gesture" that triggers a drag.

An

int

representing
the type(s) of action(s) used
in this Drag and Drop operation.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

DragGestureRecognizer

​(

DragSource

ds)

Construct a new

DragGestureRecognizer

given the

DragSource

to be used in this
Drag and Drop operation.

protected

DragGestureRecognizer

​(

DragSource

ds,

Component

c)

Construct a new

DragGestureRecognizer

given the

DragSource

to be used
in this Drag and Drop operation, and
the

Component

this

DragGestureRecognizer

should "observe" for drag initiating gestures.

protected

DragGestureRecognizer

​(

DragSource

ds,

Component

c,
int sa)

Construct a new

DragGestureRecognizer

given the

DragSource

to be used in this
Drag and Drop
operation, the

Component

this

DragGestureRecognizer

should "observe"
for drag initiating gestures, and the action(s)
supported for this Drag and Drop operation.

protected

DragGestureRecognizer

​(

DragSource

ds,

Component

c,
int sa,

DragGestureListener

dgl)

Construct a new

DragGestureRecognizer

given the

DragSource

to be used
in this Drag and Drop operation, the

Component

this

DragGestureRecognizer

should "observe"
for drag initiating gestures, the action(s) supported
for this Drag and Drop operation, and the

DragGestureListener

to notify
once a drag initiating gesture has been detected.

---

#### Constructor Summary

Construct a new

DragGestureRecognizer

given the

DragSource

to be used in this
Drag and Drop operation.

Construct a new

DragGestureRecognizer

given the

DragSource

to be used
in this Drag and Drop operation, and
the

Component

this

DragGestureRecognizer

should "observe" for drag initiating gestures.

Construct a new

DragGestureRecognizer

given the

DragSource

to be used in this
Drag and Drop
operation, the

Component

this

DragGestureRecognizer

should "observe"
for drag initiating gestures, and the action(s)
supported for this Drag and Drop operation.

Construct a new

DragGestureRecognizer

given the

DragSource

to be used
in this Drag and Drop operation, the

Component

this

DragGestureRecognizer

should "observe"
for drag initiating gestures, the action(s) supported
for this Drag and Drop operation, and the

DragGestureListener

to notify
once a drag initiating gesture has been detected.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

void

addDragGestureListener

​(

DragGestureListener

dgl)

Register a new

DragGestureListener

.

protected void

appendEvent

​(

InputEvent

awtie)

Listeners registered on the Component by this Recognizer shall record
all Events that are recognized as part of the series of Events that go
to comprise a Drag and Drop initiating gesture via this API.

protected void

fireDragGestureRecognized

​(int dragAction,

Point

p)

Notify the DragGestureListener that a Drag and Drop initiating
gesture has occurred.

Component

getComponent

()

This method returns the

Component

that is to be "observed" by the

DragGestureRecognizer

for drag initiating gestures.

DragSource

getDragSource

()

This method returns the

DragSource

this

DragGestureRecognizer

will use in order to process the Drag and Drop
operation.

int

getSourceActions

()

This method returns an int representing the
type of action(s) this Drag and Drop
operation will support.

InputEvent

getTriggerEvent

()

This method returns the first event in the
series of events that initiated
the Drag and Drop operation.

protected abstract void

registerListeners

()

register this DragGestureRecognizer's Listeners with the Component

subclasses must override this method

void

removeDragGestureListener

​(

DragGestureListener

dgl)

unregister the current DragGestureListener

void

resetRecognizer

()

Reset the Recognizer, if its currently recognizing a gesture, ignore
it.

void

setComponent

​(

Component

c)

set the Component that the DragGestureRecognizer is associated with

registerListeners() and unregisterListeners() are called as a side
effect as appropriate.

void

setSourceActions

​(int actions)

This method sets the permitted source drag action(s)
for this Drag and Drop operation.

protected abstract void

unregisterListeners

()

unregister this DragGestureRecognizer's Listeners with the Component

subclasses must override this method

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

Register a new

DragGestureListener

.

Listeners registered on the Component by this Recognizer shall record
all Events that are recognized as part of the series of Events that go
to comprise a Drag and Drop initiating gesture via this API.

Notify the DragGestureListener that a Drag and Drop initiating
gesture has occurred.

This method returns the

Component

that is to be "observed" by the

DragGestureRecognizer

for drag initiating gestures.

This method returns the

DragSource

this

DragGestureRecognizer

will use in order to process the Drag and Drop
operation.

This method returns an int representing the
type of action(s) this Drag and Drop
operation will support.

This method returns the first event in the
series of events that initiated
the Drag and Drop operation.

register this DragGestureRecognizer's Listeners with the Component

subclasses must override this method

unregister the current DragGestureListener

Reset the Recognizer, if its currently recognizing a gesture, ignore
it.

set the Component that the DragGestureRecognizer is associated with

registerListeners() and unregisterListeners() are called as a side
effect as appropriate.

This method sets the permitted source drag action(s)
for this Drag and Drop operation.

unregister this DragGestureRecognizer's Listeners with the Component

subclasses must override this method

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

- dragSource

```java
protected
DragSource
dragSource
```

The

DragSource

associated with this

DragGestureRecognizer

.

- component

```java
protected
Component
component
```

The

Component

associated with this

DragGestureRecognizer

.

- dragGestureListener

```java
protected transient
DragGestureListener
dragGestureListener
```

The

DragGestureListener

associated with this

DragGestureRecognizer

.

- sourceActions

```java
protected int sourceActions
```

An

int

representing
the type(s) of action(s) used
in this Drag and Drop operation.

- events

```java
protected
ArrayList
<
InputEvent
> events
```

The list of events (in order) that
the

DragGestureRecognizer

"recognized" as a "gesture" that triggers a drag.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DragGestureRecognizer

```java
protected DragGestureRecognizer​(
DragSource
ds,

Component
c,
int sa,

DragGestureListener
dgl)
```

Construct a new

DragGestureRecognizer

given the

DragSource

to be used
in this Drag and Drop operation, the

Component

this

DragGestureRecognizer

should "observe"
for drag initiating gestures, the action(s) supported
for this Drag and Drop operation, and the

DragGestureListener

to notify
once a drag initiating gesture has been detected.

**Parameters:** ds

- the

DragSource

this

DragGestureRecognizer

will use to process the Drag and Drop operation
**Parameters:** c

- the

Component

this

DragGestureRecognizer

should "observe" the event stream to,
in order to detect a drag initiating gesture.
If this value is

null

, the

DragGestureRecognizer

is not associated with any

Component

.
**Parameters:** sa

- the set (logical OR) of the

DnDConstants

that this Drag and Drop operation will support
**Parameters:** dgl

- the

DragGestureRecognizer

to notify when a drag gesture is detected
**Throws:** IllegalArgumentException

- if ds is

null

.

- DragGestureRecognizer

```java
protected DragGestureRecognizer​(
DragSource
ds,

Component
c,
int sa)
```

Construct a new

DragGestureRecognizer

given the

DragSource

to be used in this
Drag and Drop
operation, the

Component

this

DragGestureRecognizer

should "observe"
for drag initiating gestures, and the action(s)
supported for this Drag and Drop operation.

**Parameters:** ds

- the

DragSource

this

DragGestureRecognizer

will use to
process the Drag and Drop operation
**Parameters:** c

- the

Component

this

DragGestureRecognizer

should "observe" the event
stream to, in order to detect a drag initiating gesture.
If this value is

null

, the

DragGestureRecognizer

is not associated with any

Component

.
**Parameters:** sa

- the set (logical OR) of the

DnDConstants

that this Drag and Drop operation will support
**Throws:** IllegalArgumentException

- if ds is

null

.

- DragGestureRecognizer

```java
protected DragGestureRecognizer​(
DragSource
ds,

Component
c)
```

Construct a new

DragGestureRecognizer

given the

DragSource

to be used
in this Drag and Drop operation, and
the

Component

this

DragGestureRecognizer

should "observe" for drag initiating gestures.

**Parameters:** ds

- the

DragSource

this

DragGestureRecognizer

will use to process the Drag and Drop operation
**Parameters:** c

- the

Component

this

DragGestureRecognizer

should "observe" the event stream to,
in order to detect a drag initiating gesture.
If this value is

null

,
the

DragGestureRecognizer

is not associated with any

Component

.
**Throws:** IllegalArgumentException

- if ds is

null

.

- DragGestureRecognizer

```java
protected DragGestureRecognizer​(
DragSource
ds)
```

Construct a new

DragGestureRecognizer

given the

DragSource

to be used in this
Drag and Drop operation.

**Parameters:** ds

- the

DragSource

this

DragGestureRecognizer

will
use to process the Drag and Drop operation
**Throws:** IllegalArgumentException

- if ds is

null

.

============ METHOD DETAIL ==========

- Method Detail

- registerListeners

```java
protected abstract void registerListeners()
```

register this DragGestureRecognizer's Listeners with the Component

subclasses must override this method

- unregisterListeners

```java
protected abstract void unregisterListeners()
```

unregister this DragGestureRecognizer's Listeners with the Component

subclasses must override this method

- getDragSource

```java
public
DragSource
getDragSource()
```

This method returns the

DragSource

this

DragGestureRecognizer

will use in order to process the Drag and Drop
operation.

**Returns:** the DragSource

- getComponent

```java
public
Component
getComponent()
```

This method returns the

Component

that is to be "observed" by the

DragGestureRecognizer

for drag initiating gestures.

**Returns:** The Component this DragGestureRecognizer
is associated with

- setComponent

```java
public void setComponent​(
Component
c)
```

set the Component that the DragGestureRecognizer is associated with

registerListeners() and unregisterListeners() are called as a side
effect as appropriate.

**Parameters:** c

- The

Component

or

null

- getSourceActions

```java
public int getSourceActions()
```

This method returns an int representing the
type of action(s) this Drag and Drop
operation will support.

**Returns:** the currently permitted source action(s)

- setSourceActions

```java
public void setSourceActions​(int actions)
```

This method sets the permitted source drag action(s)
for this Drag and Drop operation.

**Parameters:** actions

- the permitted source drag action(s)

- getTriggerEvent

```java
public
InputEvent
getTriggerEvent()
```

This method returns the first event in the
series of events that initiated
the Drag and Drop operation.

**Returns:** the initial event that triggered the drag gesture

- resetRecognizer

```java
public void resetRecognizer()
```

Reset the Recognizer, if its currently recognizing a gesture, ignore
it.

- addDragGestureListener

```java
public void addDragGestureListener​(
DragGestureListener
dgl)
throws
TooManyListenersException
```

Register a new

DragGestureListener

.

**Parameters:** dgl

- the

DragGestureListener

to register
with this

DragGestureRecognizer

.
**Throws:** TooManyListenersException

- if a

DragGestureListener

has already been added.

- removeDragGestureListener

```java
public void removeDragGestureListener​(
DragGestureListener
dgl)
```

unregister the current DragGestureListener

**Parameters:** dgl

- the

DragGestureListener

to unregister
from this

DragGestureRecognizer
**Throws:** IllegalArgumentException

- if
dgl is not (equal to) the currently registered

DragGestureListener

.

- fireDragGestureRecognized

```java
protected void fireDragGestureRecognized​(int dragAction,

Point
p)
```

Notify the DragGestureListener that a Drag and Drop initiating
gesture has occurred. Then reset the state of the Recognizer.

**Parameters:** dragAction

- The action initially selected by the users gesture
**Parameters:** p

- The point (in Component coords) where the gesture originated

- appendEvent

```java
protected void appendEvent​(
InputEvent
awtie)
```

Listeners registered on the Component by this Recognizer shall record
all Events that are recognized as part of the series of Events that go
to comprise a Drag and Drop initiating gesture via this API.

This method is used by a

DragGestureRecognizer

implementation to add an

InputEvent

subclass (that it believes is one in a series
of events that comprise a Drag and Drop operation)
to the array of events that this

DragGestureRecognizer

maintains internally.

**Parameters:** awtie

- the

InputEvent

to add to this

DragGestureRecognizer

's
internal array of events. Note that

null

is not a valid value, and will be ignored.

Field Detail

- dragSource

```java
protected
DragSource
dragSource
```

The

DragSource

associated with this

DragGestureRecognizer

.

- component

```java
protected
Component
component
```

The

Component

associated with this

DragGestureRecognizer

.

- dragGestureListener

```java
protected transient
DragGestureListener
dragGestureListener
```

The

DragGestureListener

associated with this

DragGestureRecognizer

.

- sourceActions

```java
protected int sourceActions
```

An

int

representing
the type(s) of action(s) used
in this Drag and Drop operation.

- events

```java
protected
ArrayList
<
InputEvent
> events
```

The list of events (in order) that
the

DragGestureRecognizer

"recognized" as a "gesture" that triggers a drag.

---

#### Field Detail

dragSource

```java
protected
DragSource
dragSource
```

The

DragSource

associated with this

DragGestureRecognizer

.

---

#### dragSource

protected

DragSource

dragSource

The

DragSource

associated with this

DragGestureRecognizer

.

component

```java
protected
Component
component
```

The

Component

associated with this

DragGestureRecognizer

.

---

#### component

protected

Component

component

The

Component

associated with this

DragGestureRecognizer

.

dragGestureListener

```java
protected transient
DragGestureListener
dragGestureListener
```

The

DragGestureListener

associated with this

DragGestureRecognizer

.

---

#### dragGestureListener

protected transient

DragGestureListener

dragGestureListener

The

DragGestureListener

associated with this

DragGestureRecognizer

.

sourceActions

```java
protected int sourceActions
```

An

int

representing
the type(s) of action(s) used
in this Drag and Drop operation.

---

#### sourceActions

protected int sourceActions

An

int

representing
the type(s) of action(s) used
in this Drag and Drop operation.

events

```java
protected
ArrayList
<
InputEvent
> events
```

The list of events (in order) that
the

DragGestureRecognizer

"recognized" as a "gesture" that triggers a drag.

---

#### events

protected

ArrayList

<

InputEvent

> events

The list of events (in order) that
the

DragGestureRecognizer

"recognized" as a "gesture" that triggers a drag.

Constructor Detail

- DragGestureRecognizer

```java
protected DragGestureRecognizer​(
DragSource
ds,

Component
c,
int sa,

DragGestureListener
dgl)
```

Construct a new

DragGestureRecognizer

given the

DragSource

to be used
in this Drag and Drop operation, the

Component

this

DragGestureRecognizer

should "observe"
for drag initiating gestures, the action(s) supported
for this Drag and Drop operation, and the

DragGestureListener

to notify
once a drag initiating gesture has been detected.

**Parameters:** ds

- the

DragSource

this

DragGestureRecognizer

will use to process the Drag and Drop operation
**Parameters:** c

- the

Component

this

DragGestureRecognizer

should "observe" the event stream to,
in order to detect a drag initiating gesture.
If this value is

null

, the

DragGestureRecognizer

is not associated with any

Component

.
**Parameters:** sa

- the set (logical OR) of the

DnDConstants

that this Drag and Drop operation will support
**Parameters:** dgl

- the

DragGestureRecognizer

to notify when a drag gesture is detected
**Throws:** IllegalArgumentException

- if ds is

null

.

- DragGestureRecognizer

```java
protected DragGestureRecognizer​(
DragSource
ds,

Component
c,
int sa)
```

Construct a new

DragGestureRecognizer

given the

DragSource

to be used in this
Drag and Drop
operation, the

Component

this

DragGestureRecognizer

should "observe"
for drag initiating gestures, and the action(s)
supported for this Drag and Drop operation.

**Parameters:** ds

- the

DragSource

this

DragGestureRecognizer

will use to
process the Drag and Drop operation
**Parameters:** c

- the

Component

this

DragGestureRecognizer

should "observe" the event
stream to, in order to detect a drag initiating gesture.
If this value is

null

, the

DragGestureRecognizer

is not associated with any

Component

.
**Parameters:** sa

- the set (logical OR) of the

DnDConstants

that this Drag and Drop operation will support
**Throws:** IllegalArgumentException

- if ds is

null

.

- DragGestureRecognizer

```java
protected DragGestureRecognizer​(
DragSource
ds,

Component
c)
```

Construct a new

DragGestureRecognizer

given the

DragSource

to be used
in this Drag and Drop operation, and
the

Component

this

DragGestureRecognizer

should "observe" for drag initiating gestures.

**Parameters:** ds

- the

DragSource

this

DragGestureRecognizer

will use to process the Drag and Drop operation
**Parameters:** c

- the

Component

this

DragGestureRecognizer

should "observe" the event stream to,
in order to detect a drag initiating gesture.
If this value is

null

,
the

DragGestureRecognizer

is not associated with any

Component

.
**Throws:** IllegalArgumentException

- if ds is

null

.

- DragGestureRecognizer

```java
protected DragGestureRecognizer​(
DragSource
ds)
```

Construct a new

DragGestureRecognizer

given the

DragSource

to be used in this
Drag and Drop operation.

**Parameters:** ds

- the

DragSource

this

DragGestureRecognizer

will
use to process the Drag and Drop operation
**Throws:** IllegalArgumentException

- if ds is

null

.

---

#### Constructor Detail

DragGestureRecognizer

```java
protected DragGestureRecognizer​(
DragSource
ds,

Component
c,
int sa,

DragGestureListener
dgl)
```

Construct a new

DragGestureRecognizer

given the

DragSource

to be used
in this Drag and Drop operation, the

Component

this

DragGestureRecognizer

should "observe"
for drag initiating gestures, the action(s) supported
for this Drag and Drop operation, and the

DragGestureListener

to notify
once a drag initiating gesture has been detected.

**Parameters:** ds

- the

DragSource

this

DragGestureRecognizer

will use to process the Drag and Drop operation
**Parameters:** c

- the

Component

this

DragGestureRecognizer

should "observe" the event stream to,
in order to detect a drag initiating gesture.
If this value is

null

, the

DragGestureRecognizer

is not associated with any

Component

.
**Parameters:** sa

- the set (logical OR) of the

DnDConstants

that this Drag and Drop operation will support
**Parameters:** dgl

- the

DragGestureRecognizer

to notify when a drag gesture is detected
**Throws:** IllegalArgumentException

- if ds is

null

.

---

#### DragGestureRecognizer

protected DragGestureRecognizer​(

DragSource

ds,

Component

c,
int sa,

DragGestureListener

dgl)

Construct a new

DragGestureRecognizer

given the

DragSource

to be used
in this Drag and Drop operation, the

Component

this

DragGestureRecognizer

should "observe"
for drag initiating gestures, the action(s) supported
for this Drag and Drop operation, and the

DragGestureListener

to notify
once a drag initiating gesture has been detected.

DragGestureRecognizer

```java
protected DragGestureRecognizer​(
DragSource
ds,

Component
c,
int sa)
```

Construct a new

DragGestureRecognizer

given the

DragSource

to be used in this
Drag and Drop
operation, the

Component

this

DragGestureRecognizer

should "observe"
for drag initiating gestures, and the action(s)
supported for this Drag and Drop operation.

**Parameters:** ds

- the

DragSource

this

DragGestureRecognizer

will use to
process the Drag and Drop operation
**Parameters:** c

- the

Component

this

DragGestureRecognizer

should "observe" the event
stream to, in order to detect a drag initiating gesture.
If this value is

null

, the

DragGestureRecognizer

is not associated with any

Component

.
**Parameters:** sa

- the set (logical OR) of the

DnDConstants

that this Drag and Drop operation will support
**Throws:** IllegalArgumentException

- if ds is

null

.

---

#### DragGestureRecognizer

protected DragGestureRecognizer​(

DragSource

ds,

Component

c,
int sa)

Construct a new

DragGestureRecognizer

given the

DragSource

to be used in this
Drag and Drop
operation, the

Component

this

DragGestureRecognizer

should "observe"
for drag initiating gestures, and the action(s)
supported for this Drag and Drop operation.

DragGestureRecognizer

```java
protected DragGestureRecognizer​(
DragSource
ds,

Component
c)
```

Construct a new

DragGestureRecognizer

given the

DragSource

to be used
in this Drag and Drop operation, and
the

Component

this

DragGestureRecognizer

should "observe" for drag initiating gestures.

**Parameters:** ds

- the

DragSource

this

DragGestureRecognizer

will use to process the Drag and Drop operation
**Parameters:** c

- the

Component

this

DragGestureRecognizer

should "observe" the event stream to,
in order to detect a drag initiating gesture.
If this value is

null

,
the

DragGestureRecognizer

is not associated with any

Component

.
**Throws:** IllegalArgumentException

- if ds is

null

.

---

#### DragGestureRecognizer

protected DragGestureRecognizer​(

DragSource

ds,

Component

c)

Construct a new

DragGestureRecognizer

given the

DragSource

to be used
in this Drag and Drop operation, and
the

Component

this

DragGestureRecognizer

should "observe" for drag initiating gestures.

DragGestureRecognizer

```java
protected DragGestureRecognizer​(
DragSource
ds)
```

Construct a new

DragGestureRecognizer

given the

DragSource

to be used in this
Drag and Drop operation.

**Parameters:** ds

- the

DragSource

this

DragGestureRecognizer

will
use to process the Drag and Drop operation
**Throws:** IllegalArgumentException

- if ds is

null

.

---

#### DragGestureRecognizer

protected DragGestureRecognizer​(

DragSource

ds)

Construct a new

DragGestureRecognizer

given the

DragSource

to be used in this
Drag and Drop operation.

Method Detail

- registerListeners

```java
protected abstract void registerListeners()
```

register this DragGestureRecognizer's Listeners with the Component

subclasses must override this method

- unregisterListeners

```java
protected abstract void unregisterListeners()
```

unregister this DragGestureRecognizer's Listeners with the Component

subclasses must override this method

- getDragSource

```java
public
DragSource
getDragSource()
```

This method returns the

DragSource

this

DragGestureRecognizer

will use in order to process the Drag and Drop
operation.

**Returns:** the DragSource

- getComponent

```java
public
Component
getComponent()
```

This method returns the

Component

that is to be "observed" by the

DragGestureRecognizer

for drag initiating gestures.

**Returns:** The Component this DragGestureRecognizer
is associated with

- setComponent

```java
public void setComponent​(
Component
c)
```

set the Component that the DragGestureRecognizer is associated with

registerListeners() and unregisterListeners() are called as a side
effect as appropriate.

**Parameters:** c

- The

Component

or

null

- getSourceActions

```java
public int getSourceActions()
```

This method returns an int representing the
type of action(s) this Drag and Drop
operation will support.

**Returns:** the currently permitted source action(s)

- setSourceActions

```java
public void setSourceActions​(int actions)
```

This method sets the permitted source drag action(s)
for this Drag and Drop operation.

**Parameters:** actions

- the permitted source drag action(s)

- getTriggerEvent

```java
public
InputEvent
getTriggerEvent()
```

This method returns the first event in the
series of events that initiated
the Drag and Drop operation.

**Returns:** the initial event that triggered the drag gesture

- resetRecognizer

```java
public void resetRecognizer()
```

Reset the Recognizer, if its currently recognizing a gesture, ignore
it.

- addDragGestureListener

```java
public void addDragGestureListener​(
DragGestureListener
dgl)
throws
TooManyListenersException
```

Register a new

DragGestureListener

.

**Parameters:** dgl

- the

DragGestureListener

to register
with this

DragGestureRecognizer

.
**Throws:** TooManyListenersException

- if a

DragGestureListener

has already been added.

- removeDragGestureListener

```java
public void removeDragGestureListener​(
DragGestureListener
dgl)
```

unregister the current DragGestureListener

**Parameters:** dgl

- the

DragGestureListener

to unregister
from this

DragGestureRecognizer
**Throws:** IllegalArgumentException

- if
dgl is not (equal to) the currently registered

DragGestureListener

.

- fireDragGestureRecognized

```java
protected void fireDragGestureRecognized​(int dragAction,

Point
p)
```

Notify the DragGestureListener that a Drag and Drop initiating
gesture has occurred. Then reset the state of the Recognizer.

**Parameters:** dragAction

- The action initially selected by the users gesture
**Parameters:** p

- The point (in Component coords) where the gesture originated

- appendEvent

```java
protected void appendEvent​(
InputEvent
awtie)
```

Listeners registered on the Component by this Recognizer shall record
all Events that are recognized as part of the series of Events that go
to comprise a Drag and Drop initiating gesture via this API.

This method is used by a

DragGestureRecognizer

implementation to add an

InputEvent

subclass (that it believes is one in a series
of events that comprise a Drag and Drop operation)
to the array of events that this

DragGestureRecognizer

maintains internally.

**Parameters:** awtie

- the

InputEvent

to add to this

DragGestureRecognizer

's
internal array of events. Note that

null

is not a valid value, and will be ignored.

---

#### Method Detail

registerListeners

```java
protected abstract void registerListeners()
```

register this DragGestureRecognizer's Listeners with the Component

subclasses must override this method

---

#### registerListeners

protected abstract void registerListeners()

register this DragGestureRecognizer's Listeners with the Component

subclasses must override this method

unregisterListeners

```java
protected abstract void unregisterListeners()
```

unregister this DragGestureRecognizer's Listeners with the Component

subclasses must override this method

---

#### unregisterListeners

protected abstract void unregisterListeners()

unregister this DragGestureRecognizer's Listeners with the Component

subclasses must override this method

getDragSource

```java
public
DragSource
getDragSource()
```

This method returns the

DragSource

this

DragGestureRecognizer

will use in order to process the Drag and Drop
operation.

**Returns:** the DragSource

---

#### getDragSource

public

DragSource

getDragSource()

This method returns the

DragSource

this

DragGestureRecognizer

will use in order to process the Drag and Drop
operation.

getComponent

```java
public
Component
getComponent()
```

This method returns the

Component

that is to be "observed" by the

DragGestureRecognizer

for drag initiating gestures.

**Returns:** The Component this DragGestureRecognizer
is associated with

---

#### getComponent

public

Component

getComponent()

This method returns the

Component

that is to be "observed" by the

DragGestureRecognizer

for drag initiating gestures.

setComponent

```java
public void setComponent​(
Component
c)
```

set the Component that the DragGestureRecognizer is associated with

registerListeners() and unregisterListeners() are called as a side
effect as appropriate.

**Parameters:** c

- The

Component

or

null

---

#### setComponent

public void setComponent​(

Component

c)

set the Component that the DragGestureRecognizer is associated with

registerListeners() and unregisterListeners() are called as a side
effect as appropriate.

getSourceActions

```java
public int getSourceActions()
```

This method returns an int representing the
type of action(s) this Drag and Drop
operation will support.

**Returns:** the currently permitted source action(s)

---

#### getSourceActions

public int getSourceActions()

This method returns an int representing the
type of action(s) this Drag and Drop
operation will support.

setSourceActions

```java
public void setSourceActions​(int actions)
```

This method sets the permitted source drag action(s)
for this Drag and Drop operation.

**Parameters:** actions

- the permitted source drag action(s)

---

#### setSourceActions

public void setSourceActions​(int actions)

This method sets the permitted source drag action(s)
for this Drag and Drop operation.

getTriggerEvent

```java
public
InputEvent
getTriggerEvent()
```

This method returns the first event in the
series of events that initiated
the Drag and Drop operation.

**Returns:** the initial event that triggered the drag gesture

---

#### getTriggerEvent

public

InputEvent

getTriggerEvent()

This method returns the first event in the
series of events that initiated
the Drag and Drop operation.

resetRecognizer

```java
public void resetRecognizer()
```

Reset the Recognizer, if its currently recognizing a gesture, ignore
it.

---

#### resetRecognizer

public void resetRecognizer()

Reset the Recognizer, if its currently recognizing a gesture, ignore
it.

addDragGestureListener

```java
public void addDragGestureListener​(
DragGestureListener
dgl)
throws
TooManyListenersException
```

Register a new

DragGestureListener

.

**Parameters:** dgl

- the

DragGestureListener

to register
with this

DragGestureRecognizer

.
**Throws:** TooManyListenersException

- if a

DragGestureListener

has already been added.

---

#### addDragGestureListener

public void addDragGestureListener​(

DragGestureListener

dgl)
throws

TooManyListenersException

Register a new

DragGestureListener

.

removeDragGestureListener

```java
public void removeDragGestureListener​(
DragGestureListener
dgl)
```

unregister the current DragGestureListener

**Parameters:** dgl

- the

DragGestureListener

to unregister
from this

DragGestureRecognizer
**Throws:** IllegalArgumentException

- if
dgl is not (equal to) the currently registered

DragGestureListener

.

---

#### removeDragGestureListener

public void removeDragGestureListener​(

DragGestureListener

dgl)

unregister the current DragGestureListener

fireDragGestureRecognized

```java
protected void fireDragGestureRecognized​(int dragAction,

Point
p)
```

Notify the DragGestureListener that a Drag and Drop initiating
gesture has occurred. Then reset the state of the Recognizer.

**Parameters:** dragAction

- The action initially selected by the users gesture
**Parameters:** p

- The point (in Component coords) where the gesture originated

---

#### fireDragGestureRecognized

protected void fireDragGestureRecognized​(int dragAction,

Point

p)

Notify the DragGestureListener that a Drag and Drop initiating
gesture has occurred. Then reset the state of the Recognizer.

appendEvent

```java
protected void appendEvent​(
InputEvent
awtie)
```

Listeners registered on the Component by this Recognizer shall record
all Events that are recognized as part of the series of Events that go
to comprise a Drag and Drop initiating gesture via this API.

This method is used by a

DragGestureRecognizer

implementation to add an

InputEvent

subclass (that it believes is one in a series
of events that comprise a Drag and Drop operation)
to the array of events that this

DragGestureRecognizer

maintains internally.

**Parameters:** awtie

- the

InputEvent

to add to this

DragGestureRecognizer

's
internal array of events. Note that

null

is not a valid value, and will be ignored.

---

#### appendEvent

protected void appendEvent​(

InputEvent

awtie)

Listeners registered on the Component by this Recognizer shall record
all Events that are recognized as part of the series of Events that go
to comprise a Drag and Drop initiating gesture via this API.

This method is used by a

DragGestureRecognizer

implementation to add an

InputEvent

subclass (that it believes is one in a series
of events that comprise a Drag and Drop operation)
to the array of events that this

DragGestureRecognizer

maintains internally.

This method is used by a

DragGestureRecognizer

implementation to add an

InputEvent

subclass (that it believes is one in a series
of events that comprise a Drag and Drop operation)
to the array of events that this

DragGestureRecognizer

maintains internally.

---

