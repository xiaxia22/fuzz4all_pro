# Class DropTargetDragEvent

**Source:** `java.desktop\java\awt\dnd\DropTargetDragEvent.html`

### Class Description

```java
public class
DropTargetDragEvent

extends
DropTargetEvent
```

The

DropTargetDragEvent

is delivered to a

DropTargetListener

via its
dragEnter() and dragOver() methods.

The

DropTargetDragEvent

reports the

source drop actions

and the

user drop action

that reflect the current state of
the drag operation.

Source drop actions

is a bitwise mask of

DnDConstants

that represents the set of drop actions supported by the drag source for
this drag operation.

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

#### public DropTargetDragEvent​(
DropTargetContext
dtc,

Point
cursorLocn,
int dropAction,
int srcActions)

Construct a

DropTargetDragEvent

given the

DropTargetContext

for this operation,
the location of the "Drag"

Cursor

's hotspot
in the

Component

's coordinates, the
user drop action, and the source drop actions.

**Parameters:**
- dtc

- The DropTargetContext for this operation
- cursorLocn

- The location of the "Drag" Cursor's
hotspot in Component coordinates
- dropAction

- The user drop action
- srcActions

- The source drop actions

**Throws:**
- NullPointerException

- if cursorLocn is null
- IllegalArgumentException

- if dropAction is not one of

DnDConstants

.
- IllegalArgumentException

- if srcActions is not
a bitwise mask of

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
location within the

Component'

s
coordinates.

**Returns:**
- the current cursor location in

Component

's coords.

---

#### public
DataFlavor
[] getCurrentDataFlavors()

This method returns the current

DataFlavor

s from the

DropTargetContext

.

**Returns:**
- current DataFlavors from the DropTargetContext

---

#### public
List
<
DataFlavor
> getCurrentDataFlavorsAsList()

This method returns the current

DataFlavor

s
as a

java.util.List

**Returns:**
- a

java.util.List

of the Current

DataFlavor

s

---

#### public boolean isDataFlavorSupported​(
DataFlavor
df)

This method returns a

boolean

indicating
if the specified

DataFlavor

is supported.

**Parameters:**
- df

- the

DataFlavor

to test

**Returns:**
- if a particular DataFlavor is supported

---

#### public int getSourceActions()

This method returns the source drop actions.

**Returns:**
- the source drop actions

---

#### public int getDropAction()

This method returns the user drop action.

**Returns:**
- the user drop action

---

#### public
Transferable
getTransferable()

This method returns the Transferable object that represents
the data associated with the current drag operation.

**Returns:**
- the Transferable associated with the drag operation

**Throws:**
- InvalidDnDOperationException

- if the data associated with the drag
operation is not available

**Since:**
- 1.5

---

#### public void acceptDrag​(int dragOperation)

Accepts the drag.

This method should be called from a

DropTargetListeners dragEnter

,

dragOver

, and

dropActionChanged

methods if the implementation wishes to accept an operation
from the srcActions other than the one selected by
the user as represented by the

dropAction

.

**Parameters:**
- dragOperation

- the operation accepted by the target

---

#### public void rejectDrag()

Rejects the drag as a result of examining either the

dropAction

or the available

DataFlavor

types.

---

### Additional Sections

#### Class DropTargetDragEvent

java.lang.Object

- java.util.EventObject
- - java.awt.dnd.DropTargetEvent
- - java.awt.dnd.DropTargetDragEvent

java.util.EventObject

- java.awt.dnd.DropTargetEvent
- - java.awt.dnd.DropTargetDragEvent

java.awt.dnd.DropTargetEvent

- java.awt.dnd.DropTargetDragEvent

java.awt.dnd.DropTargetDragEvent

**All Implemented Interfaces:** Serializable

```java
public class
DropTargetDragEvent

extends
DropTargetEvent
```

The

DropTargetDragEvent

is delivered to a

DropTargetListener

via its
dragEnter() and dragOver() methods.

The

DropTargetDragEvent

reports the

source drop actions

and the

user drop action

that reflect the current state of
the drag operation.

Source drop actions

is a bitwise mask of

DnDConstants

that represents the set of drop actions supported by the drag source for
this drag operation.

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

DropTargetDragEvent

extends

DropTargetEvent

The

DropTargetDragEvent

is delivered to a

DropTargetListener

via its
dragEnter() and dragOver() methods.

The

DropTargetDragEvent

reports the

source drop actions

and the

user drop action

that reflect the current state of
the drag operation.

Source drop actions

is a bitwise mask of

DnDConstants

that represents the set of drop actions supported by the drag source for
this drag operation.

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

DropTargetDragEvent

reports the

source drop actions

and the

user drop action

that reflect the current state of
the drag operation.

Source drop actions

is a bitwise mask of

DnDConstants

that represents the set of drop actions supported by the drag source for
this drag operation.

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
this drag operation.

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

DropTargetDragEvent

​(

DropTargetContext

dtc,

Point

cursorLocn,
int dropAction,
int srcActions)

Construct a

DropTargetDragEvent

given the

DropTargetContext

for this operation,
the location of the "Drag"

Cursor

's hotspot
in the

Component

's coordinates, the
user drop action, and the source drop actions.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

acceptDrag

​(int dragOperation)

Accepts the drag.

DataFlavor

[]

getCurrentDataFlavors

()

This method returns the current

DataFlavor

s from the

DropTargetContext

.

List

<

DataFlavor

>

getCurrentDataFlavorsAsList

()

This method returns the current

DataFlavor

s
as a

java.util.List

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
location within the

Component'

s
coordinates.

int

getSourceActions

()

This method returns the source drop actions.

Transferable

getTransferable

()

This method returns the Transferable object that represents
the data associated with the current drag operation.

boolean

isDataFlavorSupported

​(

DataFlavor

df)

This method returns a

boolean

indicating
if the specified

DataFlavor

is supported.

void

rejectDrag

()

Rejects the drag as a result of examining either the

dropAction

or the available

DataFlavor

types.

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

DropTargetDragEvent

​(

DropTargetContext

dtc,

Point

cursorLocn,
int dropAction,
int srcActions)

Construct a

DropTargetDragEvent

given the

DropTargetContext

for this operation,
the location of the "Drag"

Cursor

's hotspot
in the

Component

's coordinates, the
user drop action, and the source drop actions.

---

#### Constructor Summary

Construct a

DropTargetDragEvent

given the

DropTargetContext

for this operation,
the location of the "Drag"

Cursor

's hotspot
in the

Component

's coordinates, the
user drop action, and the source drop actions.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

acceptDrag

​(int dragOperation)

Accepts the drag.

DataFlavor

[]

getCurrentDataFlavors

()

This method returns the current

DataFlavor

s from the

DropTargetContext

.

List

<

DataFlavor

>

getCurrentDataFlavorsAsList

()

This method returns the current

DataFlavor

s
as a

java.util.List

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
location within the

Component'

s
coordinates.

int

getSourceActions

()

This method returns the source drop actions.

Transferable

getTransferable

()

This method returns the Transferable object that represents
the data associated with the current drag operation.

boolean

isDataFlavorSupported

​(

DataFlavor

df)

This method returns a

boolean

indicating
if the specified

DataFlavor

is supported.

void

rejectDrag

()

Rejects the drag as a result of examining either the

dropAction

or the available

DataFlavor

types.

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

Accepts the drag.

This method returns the current

DataFlavor

s from the

DropTargetContext

.

This method returns the current

DataFlavor

s
as a

java.util.List

This method returns the user drop action.

This method returns a

Point

indicating the

Cursor

's current
location within the

Component'

s
coordinates.

This method returns the source drop actions.

This method returns the Transferable object that represents
the data associated with the current drag operation.

This method returns a

boolean

indicating
if the specified

DataFlavor

is supported.

Rejects the drag as a result of examining either the

dropAction

or the available

DataFlavor

types.

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

- DropTargetDragEvent

```java
public DropTargetDragEvent​(
DropTargetContext
dtc,

Point
cursorLocn,
int dropAction,
int srcActions)
```

Construct a

DropTargetDragEvent

given the

DropTargetContext

for this operation,
the location of the "Drag"

Cursor

's hotspot
in the

Component

's coordinates, the
user drop action, and the source drop actions.

**Parameters:** dtc

- The DropTargetContext for this operation
**Parameters:** cursorLocn

- The location of the "Drag" Cursor's
hotspot in Component coordinates
**Parameters:** dropAction

- The user drop action
**Parameters:** srcActions

- The source drop actions
**Throws:** NullPointerException

- if cursorLocn is null
**Throws:** IllegalArgumentException

- if dropAction is not one of

DnDConstants

.
**Throws:** IllegalArgumentException

- if srcActions is not
a bitwise mask of

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
location within the

Component'

s
coordinates.

**Returns:** the current cursor location in

Component

's coords.

- getCurrentDataFlavors

```java
public
DataFlavor
[] getCurrentDataFlavors()
```

This method returns the current

DataFlavor

s from the

DropTargetContext

.

**Returns:** current DataFlavors from the DropTargetContext

- getCurrentDataFlavorsAsList

```java
public
List
<
DataFlavor
> getCurrentDataFlavorsAsList()
```

This method returns the current

DataFlavor

s
as a

java.util.List

**Returns:** a

java.util.List

of the Current

DataFlavor

s

- isDataFlavorSupported

```java
public boolean isDataFlavorSupported​(
DataFlavor
df)
```

This method returns a

boolean

indicating
if the specified

DataFlavor

is supported.

**Parameters:** df

- the

DataFlavor

to test
**Returns:** if a particular DataFlavor is supported

- getSourceActions

```java
public int getSourceActions()
```

This method returns the source drop actions.

**Returns:** the source drop actions

- getDropAction

```java
public int getDropAction()
```

This method returns the user drop action.

**Returns:** the user drop action

- getTransferable

```java
public
Transferable
getTransferable()
```

This method returns the Transferable object that represents
the data associated with the current drag operation.

**Returns:** the Transferable associated with the drag operation
**Throws:** InvalidDnDOperationException

- if the data associated with the drag
operation is not available
**Since:** 1.5

- acceptDrag

```java
public void acceptDrag​(int dragOperation)
```

Accepts the drag.

This method should be called from a

DropTargetListeners dragEnter

,

dragOver

, and

dropActionChanged

methods if the implementation wishes to accept an operation
from the srcActions other than the one selected by
the user as represented by the

dropAction

.

**Parameters:** dragOperation

- the operation accepted by the target

- rejectDrag

```java
public void rejectDrag()
```

Rejects the drag as a result of examining either the

dropAction

or the available

DataFlavor

types.

Constructor Detail

- DropTargetDragEvent

```java
public DropTargetDragEvent​(
DropTargetContext
dtc,

Point
cursorLocn,
int dropAction,
int srcActions)
```

Construct a

DropTargetDragEvent

given the

DropTargetContext

for this operation,
the location of the "Drag"

Cursor

's hotspot
in the

Component

's coordinates, the
user drop action, and the source drop actions.

**Parameters:** dtc

- The DropTargetContext for this operation
**Parameters:** cursorLocn

- The location of the "Drag" Cursor's
hotspot in Component coordinates
**Parameters:** dropAction

- The user drop action
**Parameters:** srcActions

- The source drop actions
**Throws:** NullPointerException

- if cursorLocn is null
**Throws:** IllegalArgumentException

- if dropAction is not one of

DnDConstants

.
**Throws:** IllegalArgumentException

- if srcActions is not
a bitwise mask of

DnDConstants

.
**Throws:** IllegalArgumentException

- if dtc is

null

.

---

#### Constructor Detail

DropTargetDragEvent

```java
public DropTargetDragEvent​(
DropTargetContext
dtc,

Point
cursorLocn,
int dropAction,
int srcActions)
```

Construct a

DropTargetDragEvent

given the

DropTargetContext

for this operation,
the location of the "Drag"

Cursor

's hotspot
in the

Component

's coordinates, the
user drop action, and the source drop actions.

**Parameters:** dtc

- The DropTargetContext for this operation
**Parameters:** cursorLocn

- The location of the "Drag" Cursor's
hotspot in Component coordinates
**Parameters:** dropAction

- The user drop action
**Parameters:** srcActions

- The source drop actions
**Throws:** NullPointerException

- if cursorLocn is null
**Throws:** IllegalArgumentException

- if dropAction is not one of

DnDConstants

.
**Throws:** IllegalArgumentException

- if srcActions is not
a bitwise mask of

DnDConstants

.
**Throws:** IllegalArgumentException

- if dtc is

null

.

---

#### DropTargetDragEvent

public DropTargetDragEvent​(

DropTargetContext

dtc,

Point

cursorLocn,
int dropAction,
int srcActions)

Construct a

DropTargetDragEvent

given the

DropTargetContext

for this operation,
the location of the "Drag"

Cursor

's hotspot
in the

Component

's coordinates, the
user drop action, and the source drop actions.

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
location within the

Component'

s
coordinates.

**Returns:** the current cursor location in

Component

's coords.

- getCurrentDataFlavors

```java
public
DataFlavor
[] getCurrentDataFlavors()
```

This method returns the current

DataFlavor

s from the

DropTargetContext

.

**Returns:** current DataFlavors from the DropTargetContext

- getCurrentDataFlavorsAsList

```java
public
List
<
DataFlavor
> getCurrentDataFlavorsAsList()
```

This method returns the current

DataFlavor

s
as a

java.util.List

**Returns:** a

java.util.List

of the Current

DataFlavor

s

- isDataFlavorSupported

```java
public boolean isDataFlavorSupported​(
DataFlavor
df)
```

This method returns a

boolean

indicating
if the specified

DataFlavor

is supported.

**Parameters:** df

- the

DataFlavor

to test
**Returns:** if a particular DataFlavor is supported

- getSourceActions

```java
public int getSourceActions()
```

This method returns the source drop actions.

**Returns:** the source drop actions

- getDropAction

```java
public int getDropAction()
```

This method returns the user drop action.

**Returns:** the user drop action

- getTransferable

```java
public
Transferable
getTransferable()
```

This method returns the Transferable object that represents
the data associated with the current drag operation.

**Returns:** the Transferable associated with the drag operation
**Throws:** InvalidDnDOperationException

- if the data associated with the drag
operation is not available
**Since:** 1.5

- acceptDrag

```java
public void acceptDrag​(int dragOperation)
```

Accepts the drag.

This method should be called from a

DropTargetListeners dragEnter

,

dragOver

, and

dropActionChanged

methods if the implementation wishes to accept an operation
from the srcActions other than the one selected by
the user as represented by the

dropAction

.

**Parameters:** dragOperation

- the operation accepted by the target

- rejectDrag

```java
public void rejectDrag()
```

Rejects the drag as a result of examining either the

dropAction

or the available

DataFlavor

types.

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
location within the

Component'

s
coordinates.

**Returns:** the current cursor location in

Component

's coords.

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
location within the

Component'

s
coordinates.

getCurrentDataFlavors

```java
public
DataFlavor
[] getCurrentDataFlavors()
```

This method returns the current

DataFlavor

s from the

DropTargetContext

.

**Returns:** current DataFlavors from the DropTargetContext

---

#### getCurrentDataFlavors

public

DataFlavor

[] getCurrentDataFlavors()

This method returns the current

DataFlavor

s from the

DropTargetContext

.

getCurrentDataFlavorsAsList

```java
public
List
<
DataFlavor
> getCurrentDataFlavorsAsList()
```

This method returns the current

DataFlavor

s
as a

java.util.List

**Returns:** a

java.util.List

of the Current

DataFlavor

s

---

#### getCurrentDataFlavorsAsList

public

List

<

DataFlavor

> getCurrentDataFlavorsAsList()

This method returns the current

DataFlavor

s
as a

java.util.List

isDataFlavorSupported

```java
public boolean isDataFlavorSupported​(
DataFlavor
df)
```

This method returns a

boolean

indicating
if the specified

DataFlavor

is supported.

**Parameters:** df

- the

DataFlavor

to test
**Returns:** if a particular DataFlavor is supported

---

#### isDataFlavorSupported

public boolean isDataFlavorSupported​(

DataFlavor

df)

This method returns a

boolean

indicating
if the specified

DataFlavor

is supported.

getSourceActions

```java
public int getSourceActions()
```

This method returns the source drop actions.

**Returns:** the source drop actions

---

#### getSourceActions

public int getSourceActions()

This method returns the source drop actions.

getDropAction

```java
public int getDropAction()
```

This method returns the user drop action.

**Returns:** the user drop action

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

This method returns the Transferable object that represents
the data associated with the current drag operation.

**Returns:** the Transferable associated with the drag operation
**Throws:** InvalidDnDOperationException

- if the data associated with the drag
operation is not available
**Since:** 1.5

---

#### getTransferable

public

Transferable

getTransferable()

This method returns the Transferable object that represents
the data associated with the current drag operation.

acceptDrag

```java
public void acceptDrag​(int dragOperation)
```

Accepts the drag.

This method should be called from a

DropTargetListeners dragEnter

,

dragOver

, and

dropActionChanged

methods if the implementation wishes to accept an operation
from the srcActions other than the one selected by
the user as represented by the

dropAction

.

**Parameters:** dragOperation

- the operation accepted by the target

---

#### acceptDrag

public void acceptDrag​(int dragOperation)

Accepts the drag.

This method should be called from a

DropTargetListeners dragEnter

,

dragOver

, and

dropActionChanged

methods if the implementation wishes to accept an operation
from the srcActions other than the one selected by
the user as represented by the

dropAction

.

rejectDrag

```java
public void rejectDrag()
```

Rejects the drag as a result of examining either the

dropAction

or the available

DataFlavor

types.

---

#### rejectDrag

public void rejectDrag()

Rejects the drag as a result of examining either the

dropAction

or the available

DataFlavor

types.

---

