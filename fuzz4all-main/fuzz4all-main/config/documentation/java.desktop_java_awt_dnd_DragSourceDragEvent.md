# Class DragSourceDragEvent

**Source:** `java.desktop\java\awt\dnd\DragSourceDragEvent.html`

### Class Description

```java
public class
DragSourceDragEvent

extends
DragSourceEvent
```

The

DragSourceDragEvent

is
delivered from the

DragSourceContextPeer

,
via the

DragSourceContext

, to the

DragSourceListener

registered with that

DragSourceContext

and with its associated

DragSource

.

The

DragSourceDragEvent

reports the

target drop action

and the

user drop action

that reflect the current state of
the drag operation.

Target drop action

is one of

DnDConstants

that represents
the drop action selected by the current drop target if this drop action is
supported by the drag source or

DnDConstants.ACTION_NONE

if this
drop action is not supported by the drag source.

User drop action

depends on the drop actions supported by the drag
source and the drop action selected by the user. The user can select a drop
action by pressing modifier keys during the drag operation:

```java
Ctrl + Shift -> ACTION_LINK
Ctrl -> ACTION_COPY
Shift -> ACTION_MOVE
```

If the user selects a drop action, the

user drop action

is one of

DnDConstants

that represents the selected drop action if this
drop action is supported by the drag source or

DnDConstants.ACTION_NONE

if this drop action is not supported
by the drag source.

If the user doesn't select a drop action, the set of

DnDConstants

that represents the set of drop actions supported
by the drag source is searched for

DnDConstants.ACTION_MOVE

,
then for

DnDConstants.ACTION_COPY

, then for

DnDConstants.ACTION_LINK

and the

user drop action

is the
first constant found. If no constant is found the

user drop action

is

DnDConstants.ACTION_NONE

.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public DragSourceDragEvent​(
DragSourceContext
dsc,
int dropAction,
int action,
int modifiers)

Constructs a

DragSourceDragEvent

.
This class is typically
instantiated by the

DragSourceContextPeer

rather than directly
by client code.
The coordinates for this

DragSourceDragEvent

are not specified, so

getLocation

will return

null

for this event.

The arguments

dropAction

and

action

should
be one of

DnDConstants

that represents a single action.
The argument

modifiers

should be either a bitwise mask
of old

java.awt.event.InputEvent.*_MASK

constants or a
bitwise mask of extended

java.awt.event.InputEvent.*_DOWN_MASK

constants.
This constructor does not throw any exception for invalid

dropAction

,

action

and

modifiers

.

**Parameters:**
- dsc

- the

DragSourceContext

that is to manage
notifications for this event.
- dropAction

- the user drop action.
- action

- the target drop action.
- modifiers

- the modifier keys down during event (shift, ctrl,
alt, meta)
Either extended _DOWN_MASK or old _MASK modifiers
should be used, but both models should not be mixed
in one event. Use of the extended modifiers is
preferred.

**Throws:**
- IllegalArgumentException

- if

dsc

is

null

.

**See Also:**
- InputEvent

,

DragSourceEvent.getLocation()

---

#### public DragSourceDragEvent​(
DragSourceContext
dsc,
int dropAction,
int action,
int modifiers,
int x,
int y)

Constructs a

DragSourceDragEvent

given the specified

DragSourceContext

, user drop action, target drop action,
modifiers and coordinates.

The arguments

dropAction

and

action

should
be one of

DnDConstants

that represents a single action.
The argument

modifiers

should be either a bitwise mask
of old

java.awt.event.InputEvent.*_MASK

constants or a
bitwise mask of extended

java.awt.event.InputEvent.*_DOWN_MASK

constants.
This constructor does not throw any exception for invalid

dropAction

,

action

and

modifiers

.

**Parameters:**
- dsc

- the

DragSourceContext

associated with this
event.
- dropAction

- the user drop action.
- action

- the target drop action.
- modifiers

- the modifier keys down during event (shift, ctrl,
alt, meta)
Either extended _DOWN_MASK or old _MASK modifiers
should be used, but both models should not be mixed
in one event. Use of the extended modifiers is
preferred.
- x

- the horizontal coordinate for the cursor location
- y

- the vertical coordinate for the cursor location

**Throws:**
- IllegalArgumentException

- if

dsc

is

null

.

**See Also:**
- InputEvent

**Since:**
- 1.4

---

### Method Details

#### public int getTargetActions()

This method returns the target drop action.

**Returns:**
- the target drop action.

---

#### public int getGestureModifiers()

This method returns an

int

representing
the current state of the input device modifiers
associated with the user's gesture. Typically these
would be mouse buttons or keyboard modifiers.

If the

modifiers

passed to the constructor
are invalid, this method returns them unchanged.

**Returns:**
- the current state of the input device modifiers

---

#### public int getGestureModifiersEx()

This method returns an

int

representing
the current state of the input device extended modifiers
associated with the user's gesture.
See

InputEvent.getModifiersEx()

If the

modifiers

passed to the constructor
are invalid, this method returns them unchanged.

**Returns:**
- the current state of the input device extended modifiers

**Since:**
- 1.4

---

#### public int getUserAction()

This method returns the user drop action.

**Returns:**
- the user drop action.

---

#### public int getDropAction()

This method returns the logical intersection of
the target drop action and the set of drop actions supported by
the drag source.

**Returns:**
- the logical intersection of the target drop action and
the set of drop actions supported by the drag source.

---

### Additional Sections

#### Class DragSourceDragEvent

java.lang.Object

- java.util.EventObject
- - java.awt.dnd.DragSourceEvent
- - java.awt.dnd.DragSourceDragEvent

java.util.EventObject

- java.awt.dnd.DragSourceEvent
- - java.awt.dnd.DragSourceDragEvent

java.awt.dnd.DragSourceEvent

- java.awt.dnd.DragSourceDragEvent

java.awt.dnd.DragSourceDragEvent

**All Implemented Interfaces:** Serializable

```java
public class
DragSourceDragEvent

extends
DragSourceEvent
```

The

DragSourceDragEvent

is
delivered from the

DragSourceContextPeer

,
via the

DragSourceContext

, to the

DragSourceListener

registered with that

DragSourceContext

and with its associated

DragSource

.

The

DragSourceDragEvent

reports the

target drop action

and the

user drop action

that reflect the current state of
the drag operation.

Target drop action

is one of

DnDConstants

that represents
the drop action selected by the current drop target if this drop action is
supported by the drag source or

DnDConstants.ACTION_NONE

if this
drop action is not supported by the drag source.

User drop action

depends on the drop actions supported by the drag
source and the drop action selected by the user. The user can select a drop
action by pressing modifier keys during the drag operation:

```java
Ctrl + Shift -> ACTION_LINK
Ctrl -> ACTION_COPY
Shift -> ACTION_MOVE
```

If the user selects a drop action, the

user drop action

is one of

DnDConstants

that represents the selected drop action if this
drop action is supported by the drag source or

DnDConstants.ACTION_NONE

if this drop action is not supported
by the drag source.

If the user doesn't select a drop action, the set of

DnDConstants

that represents the set of drop actions supported
by the drag source is searched for

DnDConstants.ACTION_MOVE

,
then for

DnDConstants.ACTION_COPY

, then for

DnDConstants.ACTION_LINK

and the

user drop action

is the
first constant found. If no constant is found the

user drop action

is

DnDConstants.ACTION_NONE

.

**Since:** 1.2
**See Also:** Serialized Form

public class

DragSourceDragEvent

extends

DragSourceEvent

The

DragSourceDragEvent

is
delivered from the

DragSourceContextPeer

,
via the

DragSourceContext

, to the

DragSourceListener

registered with that

DragSourceContext

and with its associated

DragSource

.

The

DragSourceDragEvent

reports the

target drop action

and the

user drop action

that reflect the current state of
the drag operation.

Target drop action

is one of

DnDConstants

that represents
the drop action selected by the current drop target if this drop action is
supported by the drag source or

DnDConstants.ACTION_NONE

if this
drop action is not supported by the drag source.

User drop action

depends on the drop actions supported by the drag
source and the drop action selected by the user. The user can select a drop
action by pressing modifier keys during the drag operation:

```java
Ctrl + Shift -> ACTION_LINK
Ctrl -> ACTION_COPY
Shift -> ACTION_MOVE
```

If the user selects a drop action, the

user drop action

is one of

DnDConstants

that represents the selected drop action if this
drop action is supported by the drag source or

DnDConstants.ACTION_NONE

if this drop action is not supported
by the drag source.

If the user doesn't select a drop action, the set of

DnDConstants

that represents the set of drop actions supported
by the drag source is searched for

DnDConstants.ACTION_MOVE

,
then for

DnDConstants.ACTION_COPY

, then for

DnDConstants.ACTION_LINK

and the

user drop action

is the
first constant found. If no constant is found the

user drop action

is

DnDConstants.ACTION_NONE

.

The

DragSourceDragEvent

reports the

target drop action

and the

user drop action

that reflect the current state of
the drag operation.

Target drop action

is one of

DnDConstants

that represents
the drop action selected by the current drop target if this drop action is
supported by the drag source or

DnDConstants.ACTION_NONE

if this
drop action is not supported by the drag source.

User drop action

depends on the drop actions supported by the drag
source and the drop action selected by the user. The user can select a drop
action by pressing modifier keys during the drag operation:

```java
Ctrl + Shift -> ACTION_LINK
Ctrl -> ACTION_COPY
Shift -> ACTION_MOVE
```

If the user selects a drop action, the

user drop action

is one of

DnDConstants

that represents the selected drop action if this
drop action is supported by the drag source or

DnDConstants.ACTION_NONE

if this drop action is not supported
by the drag source.

If the user doesn't select a drop action, the set of

DnDConstants

that represents the set of drop actions supported
by the drag source is searched for

DnDConstants.ACTION_MOVE

,
then for

DnDConstants.ACTION_COPY

, then for

DnDConstants.ACTION_LINK

and the

user drop action

is the
first constant found. If no constant is found the

user drop action

is

DnDConstants.ACTION_NONE

.

Target drop action

is one of

DnDConstants

that represents
the drop action selected by the current drop target if this drop action is
supported by the drag source or

DnDConstants.ACTION_NONE

if this
drop action is not supported by the drag source.

User drop action

depends on the drop actions supported by the drag
source and the drop action selected by the user. The user can select a drop
action by pressing modifier keys during the drag operation:

```java
Ctrl + Shift -> ACTION_LINK
Ctrl -> ACTION_COPY
Shift -> ACTION_MOVE
```

If the user selects a drop action, the

user drop action

is one of

DnDConstants

that represents the selected drop action if this
drop action is supported by the drag source or

DnDConstants.ACTION_NONE

if this drop action is not supported
by the drag source.

If the user doesn't select a drop action, the set of

DnDConstants

that represents the set of drop actions supported
by the drag source is searched for

DnDConstants.ACTION_MOVE

,
then for

DnDConstants.ACTION_COPY

, then for

DnDConstants.ACTION_LINK

and the

user drop action

is the
first constant found. If no constant is found the

user drop action

is

DnDConstants.ACTION_NONE

.

User drop action

depends on the drop actions supported by the drag
source and the drop action selected by the user. The user can select a drop
action by pressing modifier keys during the drag operation:

```java
Ctrl + Shift -> ACTION_LINK
Ctrl -> ACTION_COPY
Shift -> ACTION_MOVE
```

If the user selects a drop action, the

user drop action

is one of

DnDConstants

that represents the selected drop action if this
drop action is supported by the drag source or

DnDConstants.ACTION_NONE

if this drop action is not supported
by the drag source.

If the user doesn't select a drop action, the set of

DnDConstants

that represents the set of drop actions supported
by the drag source is searched for

DnDConstants.ACTION_MOVE

,
then for

DnDConstants.ACTION_COPY

, then for

DnDConstants.ACTION_LINK

and the

user drop action

is the
first constant found. If no constant is found the

user drop action

is

DnDConstants.ACTION_NONE

.

Ctrl + Shift -> ACTION_LINK
Ctrl -> ACTION_COPY
Shift -> ACTION_MOVE

If the user doesn't select a drop action, the set of

DnDConstants

that represents the set of drop actions supported
by the drag source is searched for

DnDConstants.ACTION_MOVE

,
then for

DnDConstants.ACTION_COPY

, then for

DnDConstants.ACTION_LINK

and the

user drop action

is the
first constant found. If no constant is found the

user drop action

is

DnDConstants.ACTION_NONE

.

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

DragSourceDragEvent

​(

DragSourceContext

dsc,
int dropAction,
int action,
int modifiers)

Constructs a

DragSourceDragEvent

.

DragSourceDragEvent

​(

DragSourceContext

dsc,
int dropAction,
int action,
int modifiers,
int x,
int y)

Constructs a

DragSourceDragEvent

given the specified

DragSourceContext

, user drop action, target drop action,
modifiers and coordinates.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getDropAction

()

This method returns the logical intersection of
the target drop action and the set of drop actions supported by
the drag source.

int

getGestureModifiers

()

This method returns an

int

representing
the current state of the input device modifiers
associated with the user's gesture.

int

getGestureModifiersEx

()

This method returns an

int

representing
the current state of the input device extended modifiers
associated with the user's gesture.

int

getTargetActions

()

This method returns the target drop action.

int

getUserAction

()

This method returns the user drop action.

- Methods declared in class java.awt.dnd.

DragSourceEvent

getDragSourceContext

,

getLocation

,

getX

,

getY

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

DragSourceDragEvent

​(

DragSourceContext

dsc,
int dropAction,
int action,
int modifiers)

Constructs a

DragSourceDragEvent

.

DragSourceDragEvent

​(

DragSourceContext

dsc,
int dropAction,
int action,
int modifiers,
int x,
int y)

Constructs a

DragSourceDragEvent

given the specified

DragSourceContext

, user drop action, target drop action,
modifiers and coordinates.

---

#### Constructor Summary

Constructs a

DragSourceDragEvent

.

Constructs a

DragSourceDragEvent

given the specified

DragSourceContext

, user drop action, target drop action,
modifiers and coordinates.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getDropAction

()

This method returns the logical intersection of
the target drop action and the set of drop actions supported by
the drag source.

int

getGestureModifiers

()

This method returns an

int

representing
the current state of the input device modifiers
associated with the user's gesture.

int

getGestureModifiersEx

()

This method returns an

int

representing
the current state of the input device extended modifiers
associated with the user's gesture.

int

getTargetActions

()

This method returns the target drop action.

int

getUserAction

()

This method returns the user drop action.

- Methods declared in class java.awt.dnd.

DragSourceEvent

getDragSourceContext

,

getLocation

,

getX

,

getY

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

This method returns the logical intersection of
the target drop action and the set of drop actions supported by
the drag source.

This method returns an

int

representing
the current state of the input device modifiers
associated with the user's gesture.

This method returns an

int

representing
the current state of the input device extended modifiers
associated with the user's gesture.

This method returns the target drop action.

This method returns the user drop action.

Methods declared in class java.awt.dnd.

DragSourceEvent

getDragSourceContext

,

getLocation

,

getX

,

getY

---

#### Methods declared in class java.awt.dnd. DragSourceEvent

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

- DragSourceDragEvent

```java
public DragSourceDragEvent​(
DragSourceContext
dsc,
int dropAction,
int action,
int modifiers)
```

Constructs a

DragSourceDragEvent

.
This class is typically
instantiated by the

DragSourceContextPeer

rather than directly
by client code.
The coordinates for this

DragSourceDragEvent

are not specified, so

getLocation

will return

null

for this event.

The arguments

dropAction

and

action

should
be one of

DnDConstants

that represents a single action.
The argument

modifiers

should be either a bitwise mask
of old

java.awt.event.InputEvent.*_MASK

constants or a
bitwise mask of extended

java.awt.event.InputEvent.*_DOWN_MASK

constants.
This constructor does not throw any exception for invalid

dropAction

,

action

and

modifiers

.

**Parameters:** dsc

- the

DragSourceContext

that is to manage
notifications for this event.
**Parameters:** dropAction

- the user drop action.
**Parameters:** action

- the target drop action.
**Parameters:** modifiers

- the modifier keys down during event (shift, ctrl,
alt, meta)
Either extended _DOWN_MASK or old _MASK modifiers
should be used, but both models should not be mixed
in one event. Use of the extended modifiers is
preferred.
**Throws:** IllegalArgumentException

- if

dsc

is

null

.
**See Also:** InputEvent

,

DragSourceEvent.getLocation()

- DragSourceDragEvent

```java
public DragSourceDragEvent​(
DragSourceContext
dsc,
int dropAction,
int action,
int modifiers,
int x,
int y)
```

Constructs a

DragSourceDragEvent

given the specified

DragSourceContext

, user drop action, target drop action,
modifiers and coordinates.

The arguments

dropAction

and

action

should
be one of

DnDConstants

that represents a single action.
The argument

modifiers

should be either a bitwise mask
of old

java.awt.event.InputEvent.*_MASK

constants or a
bitwise mask of extended

java.awt.event.InputEvent.*_DOWN_MASK

constants.
This constructor does not throw any exception for invalid

dropAction

,

action

and

modifiers

.

**Parameters:** dsc

- the

DragSourceContext

associated with this
event.
**Parameters:** dropAction

- the user drop action.
**Parameters:** action

- the target drop action.
**Parameters:** modifiers

- the modifier keys down during event (shift, ctrl,
alt, meta)
Either extended _DOWN_MASK or old _MASK modifiers
should be used, but both models should not be mixed
in one event. Use of the extended modifiers is
preferred.
**Parameters:** x

- the horizontal coordinate for the cursor location
**Parameters:** y

- the vertical coordinate for the cursor location
**Throws:** IllegalArgumentException

- if

dsc

is

null

.
**Since:** 1.4
**See Also:** InputEvent

============ METHOD DETAIL ==========

- Method Detail

- getTargetActions

```java
public int getTargetActions()
```

This method returns the target drop action.

**Returns:** the target drop action.

- getGestureModifiers

```java
public int getGestureModifiers()
```

This method returns an

int

representing
the current state of the input device modifiers
associated with the user's gesture. Typically these
would be mouse buttons or keyboard modifiers.

If the

modifiers

passed to the constructor
are invalid, this method returns them unchanged.

**Returns:** the current state of the input device modifiers

- getGestureModifiersEx

```java
public int getGestureModifiersEx()
```

This method returns an

int

representing
the current state of the input device extended modifiers
associated with the user's gesture.
See

InputEvent.getModifiersEx()

If the

modifiers

passed to the constructor
are invalid, this method returns them unchanged.

**Returns:** the current state of the input device extended modifiers
**Since:** 1.4

- getUserAction

```java
public int getUserAction()
```

This method returns the user drop action.

**Returns:** the user drop action.

- getDropAction

```java
public int getDropAction()
```

This method returns the logical intersection of
the target drop action and the set of drop actions supported by
the drag source.

**Returns:** the logical intersection of the target drop action and
the set of drop actions supported by the drag source.

Constructor Detail

- DragSourceDragEvent

```java
public DragSourceDragEvent​(
DragSourceContext
dsc,
int dropAction,
int action,
int modifiers)
```

Constructs a

DragSourceDragEvent

.
This class is typically
instantiated by the

DragSourceContextPeer

rather than directly
by client code.
The coordinates for this

DragSourceDragEvent

are not specified, so

getLocation

will return

null

for this event.

The arguments

dropAction

and

action

should
be one of

DnDConstants

that represents a single action.
The argument

modifiers

should be either a bitwise mask
of old

java.awt.event.InputEvent.*_MASK

constants or a
bitwise mask of extended

java.awt.event.InputEvent.*_DOWN_MASK

constants.
This constructor does not throw any exception for invalid

dropAction

,

action

and

modifiers

.

**Parameters:** dsc

- the

DragSourceContext

that is to manage
notifications for this event.
**Parameters:** dropAction

- the user drop action.
**Parameters:** action

- the target drop action.
**Parameters:** modifiers

- the modifier keys down during event (shift, ctrl,
alt, meta)
Either extended _DOWN_MASK or old _MASK modifiers
should be used, but both models should not be mixed
in one event. Use of the extended modifiers is
preferred.
**Throws:** IllegalArgumentException

- if

dsc

is

null

.
**See Also:** InputEvent

,

DragSourceEvent.getLocation()

- DragSourceDragEvent

```java
public DragSourceDragEvent​(
DragSourceContext
dsc,
int dropAction,
int action,
int modifiers,
int x,
int y)
```

Constructs a

DragSourceDragEvent

given the specified

DragSourceContext

, user drop action, target drop action,
modifiers and coordinates.

The arguments

dropAction

and

action

should
be one of

DnDConstants

that represents a single action.
The argument

modifiers

should be either a bitwise mask
of old

java.awt.event.InputEvent.*_MASK

constants or a
bitwise mask of extended

java.awt.event.InputEvent.*_DOWN_MASK

constants.
This constructor does not throw any exception for invalid

dropAction

,

action

and

modifiers

.

**Parameters:** dsc

- the

DragSourceContext

associated with this
event.
**Parameters:** dropAction

- the user drop action.
**Parameters:** action

- the target drop action.
**Parameters:** modifiers

- the modifier keys down during event (shift, ctrl,
alt, meta)
Either extended _DOWN_MASK or old _MASK modifiers
should be used, but both models should not be mixed
in one event. Use of the extended modifiers is
preferred.
**Parameters:** x

- the horizontal coordinate for the cursor location
**Parameters:** y

- the vertical coordinate for the cursor location
**Throws:** IllegalArgumentException

- if

dsc

is

null

.
**Since:** 1.4
**See Also:** InputEvent

---

#### Constructor Detail

DragSourceDragEvent

```java
public DragSourceDragEvent​(
DragSourceContext
dsc,
int dropAction,
int action,
int modifiers)
```

Constructs a

DragSourceDragEvent

.
This class is typically
instantiated by the

DragSourceContextPeer

rather than directly
by client code.
The coordinates for this

DragSourceDragEvent

are not specified, so

getLocation

will return

null

for this event.

The arguments

dropAction

and

action

should
be one of

DnDConstants

that represents a single action.
The argument

modifiers

should be either a bitwise mask
of old

java.awt.event.InputEvent.*_MASK

constants or a
bitwise mask of extended

java.awt.event.InputEvent.*_DOWN_MASK

constants.
This constructor does not throw any exception for invalid

dropAction

,

action

and

modifiers

.

**Parameters:** dsc

- the

DragSourceContext

that is to manage
notifications for this event.
**Parameters:** dropAction

- the user drop action.
**Parameters:** action

- the target drop action.
**Parameters:** modifiers

- the modifier keys down during event (shift, ctrl,
alt, meta)
Either extended _DOWN_MASK or old _MASK modifiers
should be used, but both models should not be mixed
in one event. Use of the extended modifiers is
preferred.
**Throws:** IllegalArgumentException

- if

dsc

is

null

.
**See Also:** InputEvent

,

DragSourceEvent.getLocation()

---

#### DragSourceDragEvent

public DragSourceDragEvent​(

DragSourceContext

dsc,
int dropAction,
int action,
int modifiers)

Constructs a

DragSourceDragEvent

.
This class is typically
instantiated by the

DragSourceContextPeer

rather than directly
by client code.
The coordinates for this

DragSourceDragEvent

are not specified, so

getLocation

will return

null

for this event.

The arguments

dropAction

and

action

should
be one of

DnDConstants

that represents a single action.
The argument

modifiers

should be either a bitwise mask
of old

java.awt.event.InputEvent.*_MASK

constants or a
bitwise mask of extended

java.awt.event.InputEvent.*_DOWN_MASK

constants.
This constructor does not throw any exception for invalid

dropAction

,

action

and

modifiers

.

The arguments

dropAction

and

action

should
be one of

DnDConstants

that represents a single action.
The argument

modifiers

should be either a bitwise mask
of old

java.awt.event.InputEvent.*_MASK

constants or a
bitwise mask of extended

java.awt.event.InputEvent.*_DOWN_MASK

constants.
This constructor does not throw any exception for invalid

dropAction

,

action

and

modifiers

.

DragSourceDragEvent

```java
public DragSourceDragEvent​(
DragSourceContext
dsc,
int dropAction,
int action,
int modifiers,
int x,
int y)
```

Constructs a

DragSourceDragEvent

given the specified

DragSourceContext

, user drop action, target drop action,
modifiers and coordinates.

The arguments

dropAction

and

action

should
be one of

DnDConstants

that represents a single action.
The argument

modifiers

should be either a bitwise mask
of old

java.awt.event.InputEvent.*_MASK

constants or a
bitwise mask of extended

java.awt.event.InputEvent.*_DOWN_MASK

constants.
This constructor does not throw any exception for invalid

dropAction

,

action

and

modifiers

.

**Parameters:** dsc

- the

DragSourceContext

associated with this
event.
**Parameters:** dropAction

- the user drop action.
**Parameters:** action

- the target drop action.
**Parameters:** modifiers

- the modifier keys down during event (shift, ctrl,
alt, meta)
Either extended _DOWN_MASK or old _MASK modifiers
should be used, but both models should not be mixed
in one event. Use of the extended modifiers is
preferred.
**Parameters:** x

- the horizontal coordinate for the cursor location
**Parameters:** y

- the vertical coordinate for the cursor location
**Throws:** IllegalArgumentException

- if

dsc

is

null

.
**Since:** 1.4
**See Also:** InputEvent

---

#### DragSourceDragEvent

public DragSourceDragEvent​(

DragSourceContext

dsc,
int dropAction,
int action,
int modifiers,
int x,
int y)

Constructs a

DragSourceDragEvent

given the specified

DragSourceContext

, user drop action, target drop action,
modifiers and coordinates.

The arguments

dropAction

and

action

should
be one of

DnDConstants

that represents a single action.
The argument

modifiers

should be either a bitwise mask
of old

java.awt.event.InputEvent.*_MASK

constants or a
bitwise mask of extended

java.awt.event.InputEvent.*_DOWN_MASK

constants.
This constructor does not throw any exception for invalid

dropAction

,

action

and

modifiers

.

The arguments

dropAction

and

action

should
be one of

DnDConstants

that represents a single action.
The argument

modifiers

should be either a bitwise mask
of old

java.awt.event.InputEvent.*_MASK

constants or a
bitwise mask of extended

java.awt.event.InputEvent.*_DOWN_MASK

constants.
This constructor does not throw any exception for invalid

dropAction

,

action

and

modifiers

.

Method Detail

- getTargetActions

```java
public int getTargetActions()
```

This method returns the target drop action.

**Returns:** the target drop action.

- getGestureModifiers

```java
public int getGestureModifiers()
```

This method returns an

int

representing
the current state of the input device modifiers
associated with the user's gesture. Typically these
would be mouse buttons or keyboard modifiers.

If the

modifiers

passed to the constructor
are invalid, this method returns them unchanged.

**Returns:** the current state of the input device modifiers

- getGestureModifiersEx

```java
public int getGestureModifiersEx()
```

This method returns an

int

representing
the current state of the input device extended modifiers
associated with the user's gesture.
See

InputEvent.getModifiersEx()

If the

modifiers

passed to the constructor
are invalid, this method returns them unchanged.

**Returns:** the current state of the input device extended modifiers
**Since:** 1.4

- getUserAction

```java
public int getUserAction()
```

This method returns the user drop action.

**Returns:** the user drop action.

- getDropAction

```java
public int getDropAction()
```

This method returns the logical intersection of
the target drop action and the set of drop actions supported by
the drag source.

**Returns:** the logical intersection of the target drop action and
the set of drop actions supported by the drag source.

---

#### Method Detail

getTargetActions

```java
public int getTargetActions()
```

This method returns the target drop action.

**Returns:** the target drop action.

---

#### getTargetActions

public int getTargetActions()

This method returns the target drop action.

getGestureModifiers

```java
public int getGestureModifiers()
```

This method returns an

int

representing
the current state of the input device modifiers
associated with the user's gesture. Typically these
would be mouse buttons or keyboard modifiers.

If the

modifiers

passed to the constructor
are invalid, this method returns them unchanged.

**Returns:** the current state of the input device modifiers

---

#### getGestureModifiers

public int getGestureModifiers()

This method returns an

int

representing
the current state of the input device modifiers
associated with the user's gesture. Typically these
would be mouse buttons or keyboard modifiers.

If the

modifiers

passed to the constructor
are invalid, this method returns them unchanged.

If the

modifiers

passed to the constructor
are invalid, this method returns them unchanged.

getGestureModifiersEx

```java
public int getGestureModifiersEx()
```

This method returns an

int

representing
the current state of the input device extended modifiers
associated with the user's gesture.
See

InputEvent.getModifiersEx()

If the

modifiers

passed to the constructor
are invalid, this method returns them unchanged.

**Returns:** the current state of the input device extended modifiers
**Since:** 1.4

---

#### getGestureModifiersEx

public int getGestureModifiersEx()

This method returns an

int

representing
the current state of the input device extended modifiers
associated with the user's gesture.
See

InputEvent.getModifiersEx()

If the

modifiers

passed to the constructor
are invalid, this method returns them unchanged.

If the

modifiers

passed to the constructor
are invalid, this method returns them unchanged.

getUserAction

```java
public int getUserAction()
```

This method returns the user drop action.

**Returns:** the user drop action.

---

#### getUserAction

public int getUserAction()

This method returns the user drop action.

getDropAction

```java
public int getDropAction()
```

This method returns the logical intersection of
the target drop action and the set of drop actions supported by
the drag source.

**Returns:** the logical intersection of the target drop action and
the set of drop actions supported by the drag source.

---

#### getDropAction

public int getDropAction()

This method returns the logical intersection of
the target drop action and the set of drop actions supported by
the drag source.

---

