# Class DropTargetDropEvent

**Source:** `java.desktop\java\awt\dnd\DropTargetDropEvent.html`

### Class Description

```java
public class
DropTargetDropEvent

extends
DropTargetEvent
```

The

DropTargetDropEvent

is delivered
via the

DropTargetListener

drop() method.

The

DropTargetDropEvent

reports the

source drop actions

and the

user drop action

that reflect the current state of the
drag-and-drop operation.

Source drop actions

is a bitwise mask of

DnDConstants

that represents the set of drop actions supported by the drag source for
this drag-and-drop operation.

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

#### public DropTargetDropEvent​(
DropTargetContext
dtc,

Point
cursorLocn,
int dropAction,
int srcActions)

Construct a

DropTargetDropEvent

given
the

DropTargetContext

for this operation,
the location of the drag

Cursor

's
hotspot in the

Component

's coordinates,
the currently
selected user drop action, and the current set of
actions supported by the source.
By default, this constructor
assumes that the target is not in the same virtual machine as
the source; that is,

isLocalTransfer()

will
return

false

.

**Parameters:**
- dtc

- The

DropTargetContext

for this operation
- cursorLocn

- The location of the "Drag" Cursor's
hotspot in

Component

coordinates
- dropAction

- the user drop action.
- srcActions

- the source drop actions.

**Throws:**
- NullPointerException

- if cursorLocn is

null
- IllegalArgumentException

- if dropAction is not one of

DnDConstants

.
- IllegalArgumentException

- if srcActions is not a bitwise mask of

DnDConstants

.
- IllegalArgumentException

- if dtc is

null

.

---

#### public DropTargetDropEvent​(
DropTargetContext
dtc,

Point
cursorLocn,
int dropAction,
int srcActions,
boolean isLocal)

Construct a

DropTargetEvent

given the

DropTargetContext

for this operation,
the location of the drag

Cursor

's hotspot
in the

Component

's
coordinates, the currently selected user drop action,
the current set of actions supported by the source,
and a

boolean

indicating if the source is in the same JVM
as the target.

**Parameters:**
- dtc

- The DropTargetContext for this operation
- cursorLocn

- The location of the "Drag" Cursor's
hotspot in Component's coordinates
- dropAction

- the user drop action.
- srcActions

- the source drop actions.
- isLocal

- True if the source is in the same JVM as the target

**Throws:**
- NullPointerException

- if cursorLocn is

null
- IllegalArgumentException

- if dropAction is not one of

DnDConstants

.
- IllegalArgumentException

- if srcActions is not a bitwise mask of

DnDConstants

.
- IllegalArgumentException

- if dtc is

null

.

---

### Method Details

#### public
Point
getLocation()

This method returns a

Point

indicating the

Cursor

's current
location in the

Component

's coordinates.

**Returns:**
- the current

Cursor

location in Component's coords.

---

#### public
DataFlavor
[] getCurrentDataFlavors()

This method returns the current DataFlavors.

**Returns:**
- current DataFlavors

---

#### public
List
<
DataFlavor
> getCurrentDataFlavorsAsList()

This method returns the currently available

DataFlavor

s as a

java.util.List

.

**Returns:**
- the currently available DataFlavors as a java.util.List

---

#### public boolean isDataFlavorSupported​(
DataFlavor
df)

This method returns a

boolean

indicating if the
specified

DataFlavor

is available
from the source.

**Parameters:**
- df

- the

DataFlavor

to test

**Returns:**
- if the DataFlavor specified is available from the source

---

#### public int getSourceActions()

This method returns the source drop actions.

**Returns:**
- the source drop actions.

---

#### public int getDropAction()

This method returns the user drop action.

**Returns:**
- the user drop actions.

---

#### public
Transferable
getTransferable()

This method returns the

Transferable

object
associated with the drop.

**Returns:**
- the

Transferable

associated with the drop

---

#### public void acceptDrop​(int dropAction)

accept the drop, using the specified action.

**Parameters:**
- dropAction

- the specified action

---

#### public void rejectDrop()

reject the Drop.

---

#### public void dropComplete​(boolean success)

This method notifies the

DragSource

that the drop transfer(s) are completed.

**Parameters:**
- success

- a

boolean

indicating that the drop transfer(s) are completed.

---

#### public boolean isLocalTransfer()

This method returns an

int

indicating if
the source is in the same JVM as the target.

**Returns:**
- if the Source is in the same JVM

---

### Additional Sections

#### Class DropTargetDropEvent

java.lang.Object

- java.util.EventObject
- - java.awt.dnd.DropTargetEvent
- - java.awt.dnd.DropTargetDropEvent

java.util.EventObject

- java.awt.dnd.DropTargetEvent
- - java.awt.dnd.DropTargetDropEvent

java.awt.dnd.DropTargetEvent

- java.awt.dnd.DropTargetDropEvent

java.awt.dnd.DropTargetDropEvent

**All Implemented Interfaces:** Serializable

```java
public class
DropTargetDropEvent

extends
DropTargetEvent
```

The

DropTargetDropEvent

is delivered
via the

DropTargetListener

drop() method.

The

DropTargetDropEvent

reports the

source drop actions

and the

user drop action

that reflect the current state of the
drag-and-drop operation.

Source drop actions

is a bitwise mask of

DnDConstants

that represents the set of drop actions supported by the drag source for
this drag-and-drop operation.

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

DropTargetDropEvent

extends

DropTargetEvent

The

DropTargetDropEvent

is delivered
via the

DropTargetListener

drop() method.

The

DropTargetDropEvent

reports the

source drop actions

and the

user drop action

that reflect the current state of the
drag-and-drop operation.

Source drop actions

is a bitwise mask of

DnDConstants

that represents the set of drop actions supported by the drag source for
this drag-and-drop operation.

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

DropTargetDropEvent

reports the

source drop actions

and the

user drop action

that reflect the current state of the
drag-and-drop operation.

Source drop actions

is a bitwise mask of

DnDConstants

that represents the set of drop actions supported by the drag source for
this drag-and-drop operation.

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

Source drop actions

is a bitwise mask of

DnDConstants

that represents the set of drop actions supported by the drag source for
this drag-and-drop operation.

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

- Fields declared in class java.awt.dnd.

DropTargetEvent

context

- Fields declared in class java.util.

EventObject

source

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DropTargetDropEvent

​(

DropTargetContext

dtc,

Point

cursorLocn,
int dropAction,
int srcActions)

Construct a

DropTargetDropEvent

given
the

DropTargetContext

for this operation,
the location of the drag

Cursor

's
hotspot in the

Component

's coordinates,
the currently
selected user drop action, and the current set of
actions supported by the source.

DropTargetDropEvent

​(

DropTargetContext

dtc,

Point

cursorLocn,
int dropAction,
int srcActions,
boolean isLocal)

Construct a

DropTargetEvent

given the

DropTargetContext

for this operation,
the location of the drag

Cursor

's hotspot
in the

Component

's
coordinates, the currently selected user drop action,
the current set of actions supported by the source,
and a

boolean

indicating if the source is in the same JVM
as the target.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

acceptDrop

​(int dropAction)

accept the drop, using the specified action.

void

dropComplete

​(boolean success)

This method notifies the

DragSource

that the drop transfer(s) are completed.

DataFlavor

[]

getCurrentDataFlavors

()

This method returns the current DataFlavors.

List

<

DataFlavor

>

getCurrentDataFlavorsAsList

()

This method returns the currently available

DataFlavor

s as a

java.util.List

.

int

getDropAction

()

This method returns the user drop action.

Point

getLocation

()

This method returns a

Point

indicating the

Cursor

's current
location in the

Component

's coordinates.

int

getSourceActions

()

This method returns the source drop actions.

Transferable

getTransferable

()

This method returns the

Transferable

object
associated with the drop.

boolean

isDataFlavorSupported

​(

DataFlavor

df)

This method returns a

boolean

indicating if the
specified

DataFlavor

is available
from the source.

boolean

isLocalTransfer

()

This method returns an

int

indicating if
the source is in the same JVM as the target.

void

rejectDrop

()

reject the Drop.

- Methods declared in class java.awt.dnd.

DropTargetEvent

getDropTargetContext

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

- Fields declared in class java.awt.dnd.

DropTargetEvent

context

- Fields declared in class java.util.

EventObject

source

---

#### Field Summary

Fields declared in class java.awt.dnd.

DropTargetEvent

context

---

#### Fields declared in class java.awt.dnd. DropTargetEvent

Fields declared in class java.util.

EventObject

source

---

#### Fields declared in class java.util. EventObject

Constructor Summary

Constructors

Constructor

Description

DropTargetDropEvent

​(

DropTargetContext

dtc,

Point

cursorLocn,
int dropAction,
int srcActions)

Construct a

DropTargetDropEvent

given
the

DropTargetContext

for this operation,
the location of the drag

Cursor

's
hotspot in the

Component

's coordinates,
the currently
selected user drop action, and the current set of
actions supported by the source.

DropTargetDropEvent

​(

DropTargetContext

dtc,

Point

cursorLocn,
int dropAction,
int srcActions,
boolean isLocal)

Construct a

DropTargetEvent

given the

DropTargetContext

for this operation,
the location of the drag

Cursor

's hotspot
in the

Component

's
coordinates, the currently selected user drop action,
the current set of actions supported by the source,
and a

boolean

indicating if the source is in the same JVM
as the target.

---

#### Constructor Summary

Construct a

DropTargetDropEvent

given
the

DropTargetContext

for this operation,
the location of the drag

Cursor

's
hotspot in the

Component

's coordinates,
the currently
selected user drop action, and the current set of
actions supported by the source.

Construct a

DropTargetEvent

given the

DropTargetContext

for this operation,
the location of the drag

Cursor

's hotspot
in the

Component

's
coordinates, the currently selected user drop action,
the current set of actions supported by the source,
and a

boolean

indicating if the source is in the same JVM
as the target.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

acceptDrop

​(int dropAction)

accept the drop, using the specified action.

void

dropComplete

​(boolean success)

This method notifies the

DragSource

that the drop transfer(s) are completed.

DataFlavor

[]

getCurrentDataFlavors

()

This method returns the current DataFlavors.

List

<

DataFlavor

>

getCurrentDataFlavorsAsList

()

This method returns the currently available

DataFlavor

s as a

java.util.List

.

int

getDropAction

()

This method returns the user drop action.

Point

getLocation

()

This method returns a

Point

indicating the

Cursor

's current
location in the

Component

's coordinates.

int

getSourceActions

()

This method returns the source drop actions.

Transferable

getTransferable

()

This method returns the

Transferable

object
associated with the drop.

boolean

isDataFlavorSupported

​(

DataFlavor

df)

This method returns a

boolean

indicating if the
specified

DataFlavor

is available
from the source.

boolean

isLocalTransfer

()

This method returns an

int

indicating if
the source is in the same JVM as the target.

void

rejectDrop

()

reject the Drop.

- Methods declared in class java.awt.dnd.

DropTargetEvent

getDropTargetContext

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

accept the drop, using the specified action.

This method notifies the

DragSource

that the drop transfer(s) are completed.

This method returns the current DataFlavors.

This method returns the currently available

DataFlavor

s as a

java.util.List

.

This method returns the user drop action.

This method returns a

Point

indicating the

Cursor

's current
location in the

Component

's coordinates.

This method returns the source drop actions.

This method returns the

Transferable

object
associated with the drop.

This method returns a

boolean

indicating if the
specified

DataFlavor

is available
from the source.

This method returns an

int

indicating if
the source is in the same JVM as the target.

reject the Drop.

Methods declared in class java.awt.dnd.

DropTargetEvent

getDropTargetContext

---

#### Methods declared in class java.awt.dnd. DropTargetEvent

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

- DropTargetDropEvent

```java
public DropTargetDropEvent​(
DropTargetContext
dtc,

Point
cursorLocn,
int dropAction,
int srcActions)
```

Construct a

DropTargetDropEvent

given
the

DropTargetContext

for this operation,
the location of the drag

Cursor

's
hotspot in the

Component

's coordinates,
the currently
selected user drop action, and the current set of
actions supported by the source.
By default, this constructor
assumes that the target is not in the same virtual machine as
the source; that is,

isLocalTransfer()

will
return

false

.

**Parameters:** dtc

- The

DropTargetContext

for this operation
**Parameters:** cursorLocn

- The location of the "Drag" Cursor's
hotspot in

Component

coordinates
**Parameters:** dropAction

- the user drop action.
**Parameters:** srcActions

- the source drop actions.
**Throws:** NullPointerException

- if cursorLocn is

null
**Throws:** IllegalArgumentException

- if dropAction is not one of

DnDConstants

.
**Throws:** IllegalArgumentException

- if srcActions is not a bitwise mask of

DnDConstants

.
**Throws:** IllegalArgumentException

- if dtc is

null

.

- DropTargetDropEvent

```java
public DropTargetDropEvent​(
DropTargetContext
dtc,

Point
cursorLocn,
int dropAction,
int srcActions,
boolean isLocal)
```

Construct a

DropTargetEvent

given the

DropTargetContext

for this operation,
the location of the drag

Cursor

's hotspot
in the

Component

's
coordinates, the currently selected user drop action,
the current set of actions supported by the source,
and a

boolean

indicating if the source is in the same JVM
as the target.

**Parameters:** dtc

- The DropTargetContext for this operation
**Parameters:** cursorLocn

- The location of the "Drag" Cursor's
hotspot in Component's coordinates
**Parameters:** dropAction

- the user drop action.
**Parameters:** srcActions

- the source drop actions.
**Parameters:** isLocal

- True if the source is in the same JVM as the target
**Throws:** NullPointerException

- if cursorLocn is

null
**Throws:** IllegalArgumentException

- if dropAction is not one of

DnDConstants

.
**Throws:** IllegalArgumentException

- if srcActions is not a bitwise mask of

DnDConstants

.
**Throws:** IllegalArgumentException

- if dtc is

null

.

============ METHOD DETAIL ==========

- Method Detail

- getLocation

```java
public
Point
getLocation()
```

This method returns a

Point

indicating the

Cursor

's current
location in the

Component

's coordinates.

**Returns:** the current

Cursor

location in Component's coords.

- getCurrentDataFlavors

```java
public
DataFlavor
[] getCurrentDataFlavors()
```

This method returns the current DataFlavors.

**Returns:** current DataFlavors

- getCurrentDataFlavorsAsList

```java
public
List
<
DataFlavor
> getCurrentDataFlavorsAsList()
```

This method returns the currently available

DataFlavor

s as a

java.util.List

.

**Returns:** the currently available DataFlavors as a java.util.List

- isDataFlavorSupported

```java
public boolean isDataFlavorSupported​(
DataFlavor
df)
```

This method returns a

boolean

indicating if the
specified

DataFlavor

is available
from the source.

**Parameters:** df

- the

DataFlavor

to test
**Returns:** if the DataFlavor specified is available from the source

- getSourceActions

```java
public int getSourceActions()
```

This method returns the source drop actions.

**Returns:** the source drop actions.

- getDropAction

```java
public int getDropAction()
```

This method returns the user drop action.

**Returns:** the user drop actions.

- getTransferable

```java
public
Transferable
getTransferable()
```

This method returns the

Transferable

object
associated with the drop.

**Returns:** the

Transferable

associated with the drop

- acceptDrop

```java
public void acceptDrop​(int dropAction)
```

accept the drop, using the specified action.

**Parameters:** dropAction

- the specified action

- rejectDrop

```java
public void rejectDrop()
```

reject the Drop.

- dropComplete

```java
public void dropComplete​(boolean success)
```

This method notifies the

DragSource

that the drop transfer(s) are completed.

**Parameters:** success

- a

boolean

indicating that the drop transfer(s) are completed.

- isLocalTransfer

```java
public boolean isLocalTransfer()
```

This method returns an

int

indicating if
the source is in the same JVM as the target.

**Returns:** if the Source is in the same JVM

Constructor Detail

- DropTargetDropEvent

```java
public DropTargetDropEvent​(
DropTargetContext
dtc,

Point
cursorLocn,
int dropAction,
int srcActions)
```

Construct a

DropTargetDropEvent

given
the

DropTargetContext

for this operation,
the location of the drag

Cursor

's
hotspot in the

Component

's coordinates,
the currently
selected user drop action, and the current set of
actions supported by the source.
By default, this constructor
assumes that the target is not in the same virtual machine as
the source; that is,

isLocalTransfer()

will
return

false

.

**Parameters:** dtc

- The

DropTargetContext

for this operation
**Parameters:** cursorLocn

- The location of the "Drag" Cursor's
hotspot in

Component

coordinates
**Parameters:** dropAction

- the user drop action.
**Parameters:** srcActions

- the source drop actions.
**Throws:** NullPointerException

- if cursorLocn is

null
**Throws:** IllegalArgumentException

- if dropAction is not one of

DnDConstants

.
**Throws:** IllegalArgumentException

- if srcActions is not a bitwise mask of

DnDConstants

.
**Throws:** IllegalArgumentException

- if dtc is

null

.

- DropTargetDropEvent

```java
public DropTargetDropEvent​(
DropTargetContext
dtc,

Point
cursorLocn,
int dropAction,
int srcActions,
boolean isLocal)
```

Construct a

DropTargetEvent

given the

DropTargetContext

for this operation,
the location of the drag

Cursor

's hotspot
in the

Component

's
coordinates, the currently selected user drop action,
the current set of actions supported by the source,
and a

boolean

indicating if the source is in the same JVM
as the target.

**Parameters:** dtc

- The DropTargetContext for this operation
**Parameters:** cursorLocn

- The location of the "Drag" Cursor's
hotspot in Component's coordinates
**Parameters:** dropAction

- the user drop action.
**Parameters:** srcActions

- the source drop actions.
**Parameters:** isLocal

- True if the source is in the same JVM as the target
**Throws:** NullPointerException

- if cursorLocn is

null
**Throws:** IllegalArgumentException

- if dropAction is not one of

DnDConstants

.
**Throws:** IllegalArgumentException

- if srcActions is not a bitwise mask of

DnDConstants

.
**Throws:** IllegalArgumentException

- if dtc is

null

.

---

#### Constructor Detail

DropTargetDropEvent

```java
public DropTargetDropEvent​(
DropTargetContext
dtc,

Point
cursorLocn,
int dropAction,
int srcActions)
```

Construct a

DropTargetDropEvent

given
the

DropTargetContext

for this operation,
the location of the drag

Cursor

's
hotspot in the

Component

's coordinates,
the currently
selected user drop action, and the current set of
actions supported by the source.
By default, this constructor
assumes that the target is not in the same virtual machine as
the source; that is,

isLocalTransfer()

will
return

false

.

**Parameters:** dtc

- The

DropTargetContext

for this operation
**Parameters:** cursorLocn

- The location of the "Drag" Cursor's
hotspot in

Component

coordinates
**Parameters:** dropAction

- the user drop action.
**Parameters:** srcActions

- the source drop actions.
**Throws:** NullPointerException

- if cursorLocn is

null
**Throws:** IllegalArgumentException

- if dropAction is not one of

DnDConstants

.
**Throws:** IllegalArgumentException

- if srcActions is not a bitwise mask of

DnDConstants

.
**Throws:** IllegalArgumentException

- if dtc is

null

.

---

#### DropTargetDropEvent

public DropTargetDropEvent​(

DropTargetContext

dtc,

Point

cursorLocn,
int dropAction,
int srcActions)

Construct a

DropTargetDropEvent

given
the

DropTargetContext

for this operation,
the location of the drag

Cursor

's
hotspot in the

Component

's coordinates,
the currently
selected user drop action, and the current set of
actions supported by the source.
By default, this constructor
assumes that the target is not in the same virtual machine as
the source; that is,

isLocalTransfer()

will
return

false

.

DropTargetDropEvent

```java
public DropTargetDropEvent​(
DropTargetContext
dtc,

Point
cursorLocn,
int dropAction,
int srcActions,
boolean isLocal)
```

Construct a

DropTargetEvent

given the

DropTargetContext

for this operation,
the location of the drag

Cursor

's hotspot
in the

Component

's
coordinates, the currently selected user drop action,
the current set of actions supported by the source,
and a

boolean

indicating if the source is in the same JVM
as the target.

**Parameters:** dtc

- The DropTargetContext for this operation
**Parameters:** cursorLocn

- The location of the "Drag" Cursor's
hotspot in Component's coordinates
**Parameters:** dropAction

- the user drop action.
**Parameters:** srcActions

- the source drop actions.
**Parameters:** isLocal

- True if the source is in the same JVM as the target
**Throws:** NullPointerException

- if cursorLocn is

null
**Throws:** IllegalArgumentException

- if dropAction is not one of

DnDConstants

.
**Throws:** IllegalArgumentException

- if srcActions is not a bitwise mask of

DnDConstants

.
**Throws:** IllegalArgumentException

- if dtc is

null

.

---

#### DropTargetDropEvent

public DropTargetDropEvent​(

DropTargetContext

dtc,

Point

cursorLocn,
int dropAction,
int srcActions,
boolean isLocal)

Construct a

DropTargetEvent

given the

DropTargetContext

for this operation,
the location of the drag

Cursor

's hotspot
in the

Component

's
coordinates, the currently selected user drop action,
the current set of actions supported by the source,
and a

boolean

indicating if the source is in the same JVM
as the target.

Method Detail

- getLocation

```java
public
Point
getLocation()
```

This method returns a

Point

indicating the

Cursor

's current
location in the

Component

's coordinates.

**Returns:** the current

Cursor

location in Component's coords.

- getCurrentDataFlavors

```java
public
DataFlavor
[] getCurrentDataFlavors()
```

This method returns the current DataFlavors.

**Returns:** current DataFlavors

- getCurrentDataFlavorsAsList

```java
public
List
<
DataFlavor
> getCurrentDataFlavorsAsList()
```

This method returns the currently available

DataFlavor

s as a

java.util.List

.

**Returns:** the currently available DataFlavors as a java.util.List

- isDataFlavorSupported

```java
public boolean isDataFlavorSupported​(
DataFlavor
df)
```

This method returns a

boolean

indicating if the
specified

DataFlavor

is available
from the source.

**Parameters:** df

- the

DataFlavor

to test
**Returns:** if the DataFlavor specified is available from the source

- getSourceActions

```java
public int getSourceActions()
```

This method returns the source drop actions.

**Returns:** the source drop actions.

- getDropAction

```java
public int getDropAction()
```

This method returns the user drop action.

**Returns:** the user drop actions.

- getTransferable

```java
public
Transferable
getTransferable()
```

This method returns the

Transferable

object
associated with the drop.

**Returns:** the

Transferable

associated with the drop

- acceptDrop

```java
public void acceptDrop​(int dropAction)
```

accept the drop, using the specified action.

**Parameters:** dropAction

- the specified action

- rejectDrop

```java
public void rejectDrop()
```

reject the Drop.

- dropComplete

```java
public void dropComplete​(boolean success)
```

This method notifies the

DragSource

that the drop transfer(s) are completed.

**Parameters:** success

- a

boolean

indicating that the drop transfer(s) are completed.

- isLocalTransfer

```java
public boolean isLocalTransfer()
```

This method returns an

int

indicating if
the source is in the same JVM as the target.

**Returns:** if the Source is in the same JVM

---

#### Method Detail

getLocation

```java
public
Point
getLocation()
```

This method returns a

Point

indicating the

Cursor

's current
location in the

Component

's coordinates.

**Returns:** the current

Cursor

location in Component's coords.

---

#### getLocation

public

Point

getLocation()

This method returns a

Point

indicating the

Cursor

's current
location in the

Component

's coordinates.

getCurrentDataFlavors

```java
public
DataFlavor
[] getCurrentDataFlavors()
```

This method returns the current DataFlavors.

**Returns:** current DataFlavors

---

#### getCurrentDataFlavors

public

DataFlavor

[] getCurrentDataFlavors()

This method returns the current DataFlavors.

getCurrentDataFlavorsAsList

```java
public
List
<
DataFlavor
> getCurrentDataFlavorsAsList()
```

This method returns the currently available

DataFlavor

s as a

java.util.List

.

**Returns:** the currently available DataFlavors as a java.util.List

---

#### getCurrentDataFlavorsAsList

public

List

<

DataFlavor

> getCurrentDataFlavorsAsList()

This method returns the currently available

DataFlavor

s as a

java.util.List

.

isDataFlavorSupported

```java
public boolean isDataFlavorSupported​(
DataFlavor
df)
```

This method returns a

boolean

indicating if the
specified

DataFlavor

is available
from the source.

**Parameters:** df

- the

DataFlavor

to test
**Returns:** if the DataFlavor specified is available from the source

---

#### isDataFlavorSupported

public boolean isDataFlavorSupported​(

DataFlavor

df)

This method returns a

boolean

indicating if the
specified

DataFlavor

is available
from the source.

getSourceActions

```java
public int getSourceActions()
```

This method returns the source drop actions.

**Returns:** the source drop actions.

---

#### getSourceActions

public int getSourceActions()

This method returns the source drop actions.

getDropAction

```java
public int getDropAction()
```

This method returns the user drop action.

**Returns:** the user drop actions.

---

#### getDropAction

public int getDropAction()

This method returns the user drop action.

getTransferable

```java
public
Transferable
getTransferable()
```

This method returns the

Transferable

object
associated with the drop.

**Returns:** the

Transferable

associated with the drop

---

#### getTransferable

public

Transferable

getTransferable()

This method returns the

Transferable

object
associated with the drop.

acceptDrop

```java
public void acceptDrop​(int dropAction)
```

accept the drop, using the specified action.

**Parameters:** dropAction

- the specified action

---

#### acceptDrop

public void acceptDrop​(int dropAction)

accept the drop, using the specified action.

rejectDrop

```java
public void rejectDrop()
```

reject the Drop.

---

#### rejectDrop

public void rejectDrop()

reject the Drop.

dropComplete

```java
public void dropComplete​(boolean success)
```

This method notifies the

DragSource

that the drop transfer(s) are completed.

**Parameters:** success

- a

boolean

indicating that the drop transfer(s) are completed.

---

#### dropComplete

public void dropComplete​(boolean success)

This method notifies the

DragSource

that the drop transfer(s) are completed.

isLocalTransfer

```java
public boolean isLocalTransfer()
```

This method returns an

int

indicating if
the source is in the same JVM as the target.

**Returns:** if the Source is in the same JVM

---

#### isLocalTransfer

public boolean isLocalTransfer()

This method returns an

int

indicating if
the source is in the same JVM as the target.

---

