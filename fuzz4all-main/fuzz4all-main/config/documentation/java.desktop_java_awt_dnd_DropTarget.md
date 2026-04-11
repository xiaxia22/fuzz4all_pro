# Class DropTarget

**Source:** `java.desktop\java\awt\dnd\DropTarget.html`

### Class Description

```java
public class
DropTarget

extends
Object

implements
DropTargetListener
,
Serializable
```

The

DropTarget

is associated
with a

Component

when that

Component

wishes
to accept drops during Drag and Drop operations.

Each

DropTarget

is associated with a

FlavorMap

.
The default

FlavorMap

hereafter designates the

FlavorMap

returned by

SystemFlavorMap.getDefaultFlavorMap()

.

**All Implemented Interfaces:** DropTargetListener

,

Serializable

,

EventListener

---

### Field Details

*No entries found.*

### Constructor Details

#### public DropTarget​(
Component
c,
int ops,

DropTargetListener
dtl,
boolean act,

FlavorMap
fm)
throws
HeadlessException

Creates a new DropTarget given the

Component

to associate itself with, an

int

representing
the default acceptable action(s) to
support, a

DropTargetListener

to handle event processing, a

boolean

indicating
if the

DropTarget

is currently accepting drops, and
a

FlavorMap

to use (or null for the default

FlavorMap

).

The Component will receive drops only if it is enabled.

**Parameters:**
- c

- The

Component

with which this

DropTarget

is associated
- ops

- The default acceptable actions for this

DropTarget
- dtl

- The

DropTargetListener

for this

DropTarget
- act

- Is the

DropTarget

accepting drops.
- fm

- The

FlavorMap

to use, or null for the default

FlavorMap

**Throws:**
- HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true

**See Also:**
- GraphicsEnvironment.isHeadless()

---

#### public DropTarget​(
Component
c,
int ops,

DropTargetListener
dtl,
boolean act)
throws
HeadlessException

Creates a

DropTarget

given the

Component

to associate itself with, an

int

representing
the default acceptable action(s)
to support, a

DropTargetListener

to handle event processing, and a

boolean

indicating
if the

DropTarget

is currently accepting drops.

The Component will receive drops only if it is enabled.

**Parameters:**
- c

- The

Component

with which this

DropTarget

is associated
- ops

- The default acceptable actions for this

DropTarget
- dtl

- The

DropTargetListener

for this

DropTarget
- act

- Is the

DropTarget

accepting drops.

**Throws:**
- HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true

**See Also:**
- GraphicsEnvironment.isHeadless()

---

#### public DropTarget()
throws
HeadlessException

Creates a

DropTarget

.

**Throws:**
- HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true

**See Also:**
- GraphicsEnvironment.isHeadless()

---

#### public DropTarget​(
Component
c,

DropTargetListener
dtl)
throws
HeadlessException

Creates a

DropTarget

given the

Component

to associate itself with, and the

DropTargetListener

to handle event processing.

The Component will receive drops only if it is enabled.

**Parameters:**
- c

- The

Component

with which this

DropTarget

is associated
- dtl

- The

DropTargetListener

for this

DropTarget

**Throws:**
- HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true

**See Also:**
- GraphicsEnvironment.isHeadless()

---

#### public DropTarget​(
Component
c,
int ops,

DropTargetListener
dtl)
throws
HeadlessException

Creates a

DropTarget

given the

Component

to associate itself with, an

int

representing
the default acceptable action(s) to support, and a

DropTargetListener

to handle event processing.

The Component will receive drops only if it is enabled.

**Parameters:**
- c

- The

Component

with which this

DropTarget

is associated
- ops

- The default acceptable actions for this

DropTarget
- dtl

- The

DropTargetListener

for this

DropTarget

**Throws:**
- HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true

**See Also:**
- GraphicsEnvironment.isHeadless()

---

### Method Details

#### public void setComponent​(
Component
c)

Note: this interface is required to permit the safe association
of a DropTarget with a Component in one of two ways, either:

component.setDropTarget(droptarget);

or

droptarget.setComponent(component);

The Component will receive drops only if it is enabled.

**Parameters:**
- c

- The new

Component

this

DropTarget

is to be associated with.

---

#### public
Component
getComponent()

Gets the

Component

associated
with this

DropTarget

.

**Returns:**
- the current

Component

---

#### public void setDefaultActions​(int ops)

Sets the default acceptable actions for this

DropTarget

**Parameters:**
- ops

- the default actions

**See Also:**
- DnDConstants

---

#### public int getDefaultActions()

Gets an

int

representing the
current action(s) supported by this

DropTarget

.

**Returns:**
- the current default actions

---

#### public void setActive​(boolean isActive)

Sets the DropTarget active if

true

,
inactive if

false

.

**Parameters:**
- isActive

- sets the

DropTarget

(in)active.

---

#### public boolean isActive()

Reports whether or not
this

DropTarget

is currently active (ready to accept drops).

**Returns:**
- true

if active,

false

if not

---

#### public void addDropTargetListener​(
DropTargetListener
dtl)
throws
TooManyListenersException

Adds a new

DropTargetListener

(UNICAST SOURCE).

**Parameters:**
- dtl

- The new

DropTargetListener

**Throws:**
- TooManyListenersException

- if a

DropTargetListener

is already added to this

DropTarget

.

---

#### public void removeDropTargetListener​(
DropTargetListener
dtl)

Removes the current

DropTargetListener

(UNICAST SOURCE).

**Parameters:**
- dtl

- the DropTargetListener to deregister.

---

#### public void dragEnter​(
DropTargetDragEvent
dtde)

Calls

dragEnter

on the registered

DropTargetListener

and passes it
the specified

DropTargetDragEvent

.
Has no effect if this

DropTarget

is not active.

**Specified by:**
- dragEnter

in interface

DropTargetListener

**Parameters:**
- dtde

- the

DropTargetDragEvent

**Throws:**
- NullPointerException

- if this

DropTarget

is active and

dtde

is

null

**See Also:**
- isActive()

---

#### public void dragOver​(
DropTargetDragEvent
dtde)

Calls

dragOver

on the registered

DropTargetListener

and passes it
the specified

DropTargetDragEvent

.
Has no effect if this

DropTarget

is not active.

**Specified by:**
- dragOver

in interface

DropTargetListener

**Parameters:**
- dtde

- the

DropTargetDragEvent

**Throws:**
- NullPointerException

- if this

DropTarget

is active and

dtde

is

null

**See Also:**
- isActive()

---

#### public void dropActionChanged​(
DropTargetDragEvent
dtde)

Calls

dropActionChanged

on the registered

DropTargetListener

and passes it
the specified

DropTargetDragEvent

.
Has no effect if this

DropTarget

is not active.

**Specified by:**
- dropActionChanged

in interface

DropTargetListener

**Parameters:**
- dtde

- the

DropTargetDragEvent

**Throws:**
- NullPointerException

- if this

DropTarget

is active and

dtde

is

null

**See Also:**
- isActive()

---

#### public void dragExit​(
DropTargetEvent
dte)

Calls

dragExit

on the registered

DropTargetListener

and passes it
the specified

DropTargetEvent

.
Has no effect if this

DropTarget

is not active.

This method itself does not throw any exception
for null parameter but for exceptions thrown by
the respective method of the listener.

**Specified by:**
- dragExit

in interface

DropTargetListener

**Parameters:**
- dte

- the

DropTargetEvent

**See Also:**
- isActive()

---

#### public void drop​(
DropTargetDropEvent
dtde)

Calls

drop

on the registered

DropTargetListener

and passes it
the specified

DropTargetDropEvent

if this

DropTarget

is active.

**Specified by:**
- drop

in interface

DropTargetListener

**Parameters:**
- dtde

- the

DropTargetDropEvent

**Throws:**
- NullPointerException

- if

dtde

is null
and at least one of the following is true: this

DropTarget

is not active, or there is
no a

DropTargetListener

registered.

**See Also:**
- isActive()

---

#### public
FlavorMap
getFlavorMap()

Gets the

FlavorMap

associated with this

DropTarget

.
If no

FlavorMap

has been set for this

DropTarget

, it is associated with the default

FlavorMap

.

**Returns:**
- the FlavorMap for this DropTarget

---

#### public void setFlavorMap​(
FlavorMap
fm)

Sets the

FlavorMap

associated
with this

DropTarget

.

**Parameters:**
- fm

- the new

FlavorMap

, or null to
associate the default FlavorMap with this DropTarget.

---

#### public void addNotify()

Notify the DropTarget that it has been associated with a Component

This method is usually called from java.awt.Component.addNotify() of
the Component associated with this DropTarget to notify the DropTarget
that a ComponentPeer has been associated with that Component.

Calling this method, other than to notify this DropTarget of the
association of the ComponentPeer with the Component may result in
a malfunction of the DnD system.

---

#### public void removeNotify()

Notify the DropTarget that it has been disassociated from a Component

This method is usually called from java.awt.Component.removeNotify() of
the Component associated with this DropTarget to notify the DropTarget
that a ComponentPeer has been disassociated with that Component.

Calling this method, other than to notify this DropTarget of the
disassociation of the ComponentPeer from the Component may result in
a malfunction of the DnD system.

---

#### public
DropTargetContext
getDropTargetContext()

Gets the

DropTargetContext

associated
with this

DropTarget

.

**Returns:**
- the

DropTargetContext

associated with this

DropTarget

.

---

#### protected
DropTargetContext
createDropTargetContext()

Creates the DropTargetContext associated with this DropTarget.
Subclasses may override this method to instantiate their own
DropTargetContext subclass.

This call is typically *only* called by the platform's
DropTargetContextPeer as a drag operation encounters this
DropTarget. Accessing the Context while no Drag is current
has undefined results.

**Returns:**
- the DropTargetContext associated with this DropTarget

---

#### protected
DropTarget.DropTargetAutoScroller
createDropTargetAutoScroller​(
Component
c,

Point
p)

create an embedded autoscroller

**Parameters:**
- c

- the

Component
- p

- the

Point

**Returns:**
- an embedded autoscroller

---

#### protected void initializeAutoscrolling​(
Point
p)

initialize autoscrolling

**Parameters:**
- p

- the

Point

---

#### protected void updateAutoscroll​(
Point
dragCursorLocn)

update autoscrolling with current cursor location

**Parameters:**
- dragCursorLocn

- the

Point

---

#### protected void clearAutoscroll()

clear autoscrolling

---

### Additional Sections

#### Class DropTarget

java.lang.Object

- java.awt.dnd.DropTarget

java.awt.dnd.DropTarget

**All Implemented Interfaces:** DropTargetListener

,

Serializable

,

EventListener

```java
public class
DropTarget

extends
Object

implements
DropTargetListener
,
Serializable
```

The

DropTarget

is associated
with a

Component

when that

Component

wishes
to accept drops during Drag and Drop operations.

Each

DropTarget

is associated with a

FlavorMap

.
The default

FlavorMap

hereafter designates the

FlavorMap

returned by

SystemFlavorMap.getDefaultFlavorMap()

.

**Since:** 1.2
**See Also:** Serialized Form

public class

DropTarget

extends

Object

implements

DropTargetListener

,

Serializable

The

DropTarget

is associated
with a

Component

when that

Component

wishes
to accept drops during Drag and Drop operations.

Each

DropTarget

is associated with a

FlavorMap

.
The default

FlavorMap

hereafter designates the

FlavorMap

returned by

SystemFlavorMap.getDefaultFlavorMap()

.

Each

DropTarget

is associated with a

FlavorMap

.
The default

FlavorMap

hereafter designates the

FlavorMap

returned by

SystemFlavorMap.getDefaultFlavorMap()

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected static class

DropTarget.DropTargetAutoScroller

this protected nested class implements autoscrolling

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DropTarget

()

Creates a

DropTarget

.

DropTarget

​(

Component

c,
int ops,

DropTargetListener

dtl)

Creates a

DropTarget

given the

Component

to associate itself with, an

int

representing
the default acceptable action(s) to support, and a

DropTargetListener

to handle event processing.

DropTarget

​(

Component

c,
int ops,

DropTargetListener

dtl,
boolean act)

Creates a

DropTarget

given the

Component

to associate itself with, an

int

representing
the default acceptable action(s)
to support, a

DropTargetListener

to handle event processing, and a

boolean

indicating
if the

DropTarget

is currently accepting drops.

DropTarget

​(

Component

c,
int ops,

DropTargetListener

dtl,
boolean act,

FlavorMap

fm)

Creates a new DropTarget given the

Component

to associate itself with, an

int

representing
the default acceptable action(s) to
support, a

DropTargetListener

to handle event processing, a

boolean

indicating
if the

DropTarget

is currently accepting drops, and
a

FlavorMap

to use (or null for the default

FlavorMap

).

DropTarget

​(

Component

c,

DropTargetListener

dtl)

Creates a

DropTarget

given the

Component

to associate itself with, and the

DropTargetListener

to handle event processing.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addDropTargetListener

​(

DropTargetListener

dtl)

Adds a new

DropTargetListener

(UNICAST SOURCE).

void

addNotify

()

Notify the DropTarget that it has been associated with a Component

This method is usually called from java.awt.Component.addNotify() of
the Component associated with this DropTarget to notify the DropTarget
that a ComponentPeer has been associated with that Component.

protected void

clearAutoscroll

()

clear autoscrolling

protected

DropTarget.DropTargetAutoScroller

createDropTargetAutoScroller

​(

Component

c,

Point

p)

create an embedded autoscroller

protected

DropTargetContext

createDropTargetContext

()

Creates the DropTargetContext associated with this DropTarget.

void

dragEnter

​(

DropTargetDragEvent

dtde)

Calls

dragEnter

on the registered

DropTargetListener

and passes it
the specified

DropTargetDragEvent

.

void

dragExit

​(

DropTargetEvent

dte)

Calls

dragExit

on the registered

DropTargetListener

and passes it
the specified

DropTargetEvent

.

void

dragOver

​(

DropTargetDragEvent

dtde)

Calls

dragOver

on the registered

DropTargetListener

and passes it
the specified

DropTargetDragEvent

.

void

drop

​(

DropTargetDropEvent

dtde)

Calls

drop

on the registered

DropTargetListener

and passes it
the specified

DropTargetDropEvent

if this

DropTarget

is active.

void

dropActionChanged

​(

DropTargetDragEvent

dtde)

Calls

dropActionChanged

on the registered

DropTargetListener

and passes it
the specified

DropTargetDragEvent

.

Component

getComponent

()

Gets the

Component

associated
with this

DropTarget

.

int

getDefaultActions

()

Gets an

int

representing the
current action(s) supported by this

DropTarget

.

DropTargetContext

getDropTargetContext

()

Gets the

DropTargetContext

associated
with this

DropTarget

.

FlavorMap

getFlavorMap

()

Gets the

FlavorMap

associated with this

DropTarget

.

protected void

initializeAutoscrolling

​(

Point

p)

initialize autoscrolling

boolean

isActive

()

Reports whether or not
this

DropTarget

is currently active (ready to accept drops).

void

removeDropTargetListener

​(

DropTargetListener

dtl)

Removes the current

DropTargetListener

(UNICAST SOURCE).

void

removeNotify

()

Notify the DropTarget that it has been disassociated from a Component

This method is usually called from java.awt.Component.removeNotify() of
the Component associated with this DropTarget to notify the DropTarget
that a ComponentPeer has been disassociated with that Component.

void

setActive

​(boolean isActive)

Sets the DropTarget active if

true

,
inactive if

false

.

void

setComponent

​(

Component

c)

Note: this interface is required to permit the safe association
of a DropTarget with a Component in one of two ways, either:

component.setDropTarget(droptarget);

or

droptarget.setComponent(component);

void

setDefaultActions

​(int ops)

Sets the default acceptable actions for this

DropTarget

void

setFlavorMap

​(

FlavorMap

fm)

Sets the

FlavorMap

associated
with this

DropTarget

.

protected void

updateAutoscroll

​(

Point

dragCursorLocn)

update autoscrolling with current cursor location

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected static class

DropTarget.DropTargetAutoScroller

this protected nested class implements autoscrolling

---

#### Nested Class Summary

this protected nested class implements autoscrolling

Constructor Summary

Constructors

Constructor

Description

DropTarget

()

Creates a

DropTarget

.

DropTarget

​(

Component

c,
int ops,

DropTargetListener

dtl)

Creates a

DropTarget

given the

Component

to associate itself with, an

int

representing
the default acceptable action(s) to support, and a

DropTargetListener

to handle event processing.

DropTarget

​(

Component

c,
int ops,

DropTargetListener

dtl,
boolean act)

Creates a

DropTarget

given the

Component

to associate itself with, an

int

representing
the default acceptable action(s)
to support, a

DropTargetListener

to handle event processing, and a

boolean

indicating
if the

DropTarget

is currently accepting drops.

DropTarget

​(

Component

c,
int ops,

DropTargetListener

dtl,
boolean act,

FlavorMap

fm)

Creates a new DropTarget given the

Component

to associate itself with, an

int

representing
the default acceptable action(s) to
support, a

DropTargetListener

to handle event processing, a

boolean

indicating
if the

DropTarget

is currently accepting drops, and
a

FlavorMap

to use (or null for the default

FlavorMap

).

DropTarget

​(

Component

c,

DropTargetListener

dtl)

Creates a

DropTarget

given the

Component

to associate itself with, and the

DropTargetListener

to handle event processing.

---

#### Constructor Summary

Creates a

DropTarget

.

Creates a

DropTarget

given the

Component

to associate itself with, an

int

representing
the default acceptable action(s) to support, and a

DropTargetListener

to handle event processing.

Creates a

DropTarget

given the

Component

to associate itself with, an

int

representing
the default acceptable action(s)
to support, a

DropTargetListener

to handle event processing, and a

boolean

indicating
if the

DropTarget

is currently accepting drops.

Creates a new DropTarget given the

Component

to associate itself with, an

int

representing
the default acceptable action(s) to
support, a

DropTargetListener

to handle event processing, a

boolean

indicating
if the

DropTarget

is currently accepting drops, and
a

FlavorMap

to use (or null for the default

FlavorMap

).

Creates a

DropTarget

given the

Component

to associate itself with, and the

DropTargetListener

to handle event processing.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addDropTargetListener

​(

DropTargetListener

dtl)

Adds a new

DropTargetListener

(UNICAST SOURCE).

void

addNotify

()

Notify the DropTarget that it has been associated with a Component

This method is usually called from java.awt.Component.addNotify() of
the Component associated with this DropTarget to notify the DropTarget
that a ComponentPeer has been associated with that Component.

protected void

clearAutoscroll

()

clear autoscrolling

protected

DropTarget.DropTargetAutoScroller

createDropTargetAutoScroller

​(

Component

c,

Point

p)

create an embedded autoscroller

protected

DropTargetContext

createDropTargetContext

()

Creates the DropTargetContext associated with this DropTarget.

void

dragEnter

​(

DropTargetDragEvent

dtde)

Calls

dragEnter

on the registered

DropTargetListener

and passes it
the specified

DropTargetDragEvent

.

void

dragExit

​(

DropTargetEvent

dte)

Calls

dragExit

on the registered

DropTargetListener

and passes it
the specified

DropTargetEvent

.

void

dragOver

​(

DropTargetDragEvent

dtde)

Calls

dragOver

on the registered

DropTargetListener

and passes it
the specified

DropTargetDragEvent

.

void

drop

​(

DropTargetDropEvent

dtde)

Calls

drop

on the registered

DropTargetListener

and passes it
the specified

DropTargetDropEvent

if this

DropTarget

is active.

void

dropActionChanged

​(

DropTargetDragEvent

dtde)

Calls

dropActionChanged

on the registered

DropTargetListener

and passes it
the specified

DropTargetDragEvent

.

Component

getComponent

()

Gets the

Component

associated
with this

DropTarget

.

int

getDefaultActions

()

Gets an

int

representing the
current action(s) supported by this

DropTarget

.

DropTargetContext

getDropTargetContext

()

Gets the

DropTargetContext

associated
with this

DropTarget

.

FlavorMap

getFlavorMap

()

Gets the

FlavorMap

associated with this

DropTarget

.

protected void

initializeAutoscrolling

​(

Point

p)

initialize autoscrolling

boolean

isActive

()

Reports whether or not
this

DropTarget

is currently active (ready to accept drops).

void

removeDropTargetListener

​(

DropTargetListener

dtl)

Removes the current

DropTargetListener

(UNICAST SOURCE).

void

removeNotify

()

Notify the DropTarget that it has been disassociated from a Component

This method is usually called from java.awt.Component.removeNotify() of
the Component associated with this DropTarget to notify the DropTarget
that a ComponentPeer has been disassociated with that Component.

void

setActive

​(boolean isActive)

Sets the DropTarget active if

true

,
inactive if

false

.

void

setComponent

​(

Component

c)

Note: this interface is required to permit the safe association
of a DropTarget with a Component in one of two ways, either:

component.setDropTarget(droptarget);

or

droptarget.setComponent(component);

void

setDefaultActions

​(int ops)

Sets the default acceptable actions for this

DropTarget

void

setFlavorMap

​(

FlavorMap

fm)

Sets the

FlavorMap

associated
with this

DropTarget

.

protected void

updateAutoscroll

​(

Point

dragCursorLocn)

update autoscrolling with current cursor location

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

Adds a new

DropTargetListener

(UNICAST SOURCE).

Notify the DropTarget that it has been associated with a Component

This method is usually called from java.awt.Component.addNotify() of
the Component associated with this DropTarget to notify the DropTarget
that a ComponentPeer has been associated with that Component.

clear autoscrolling

create an embedded autoscroller

Creates the DropTargetContext associated with this DropTarget.

Calls

dragEnter

on the registered

DropTargetListener

and passes it
the specified

DropTargetDragEvent

.

Calls

dragExit

on the registered

DropTargetListener

and passes it
the specified

DropTargetEvent

.

Calls

dragOver

on the registered

DropTargetListener

and passes it
the specified

DropTargetDragEvent

.

Calls

drop

on the registered

DropTargetListener

and passes it
the specified

DropTargetDropEvent

if this

DropTarget

is active.

Calls

dropActionChanged

on the registered

DropTargetListener

and passes it
the specified

DropTargetDragEvent

.

Gets the

Component

associated
with this

DropTarget

.

Gets an

int

representing the
current action(s) supported by this

DropTarget

.

Gets the

DropTargetContext

associated
with this

DropTarget

.

Gets the

FlavorMap

associated with this

DropTarget

.

initialize autoscrolling

Reports whether or not
this

DropTarget

is currently active (ready to accept drops).

Removes the current

DropTargetListener

(UNICAST SOURCE).

Notify the DropTarget that it has been disassociated from a Component

This method is usually called from java.awt.Component.removeNotify() of
the Component associated with this DropTarget to notify the DropTarget
that a ComponentPeer has been disassociated with that Component.

Sets the DropTarget active if

true

,
inactive if

false

.

Note: this interface is required to permit the safe association
of a DropTarget with a Component in one of two ways, either:

component.setDropTarget(droptarget);

or

droptarget.setComponent(component);

Sets the default acceptable actions for this

DropTarget

Sets the

FlavorMap

associated
with this

DropTarget

.

update autoscrolling with current cursor location

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

- DropTarget

```java
public DropTarget​(
Component
c,
int ops,

DropTargetListener
dtl,
boolean act,

FlavorMap
fm)
throws
HeadlessException
```

Creates a new DropTarget given the

Component

to associate itself with, an

int

representing
the default acceptable action(s) to
support, a

DropTargetListener

to handle event processing, a

boolean

indicating
if the

DropTarget

is currently accepting drops, and
a

FlavorMap

to use (or null for the default

FlavorMap

).

The Component will receive drops only if it is enabled.

**Parameters:** c

- The

Component

with which this

DropTarget

is associated
**Parameters:** ops

- The default acceptable actions for this

DropTarget
**Parameters:** dtl

- The

DropTargetListener

for this

DropTarget
**Parameters:** act

- Is the

DropTarget

accepting drops.
**Parameters:** fm

- The

FlavorMap

to use, or null for the default

FlavorMap
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true
**See Also:** GraphicsEnvironment.isHeadless()

- DropTarget

```java
public DropTarget​(
Component
c,
int ops,

DropTargetListener
dtl,
boolean act)
throws
HeadlessException
```

Creates a

DropTarget

given the

Component

to associate itself with, an

int

representing
the default acceptable action(s)
to support, a

DropTargetListener

to handle event processing, and a

boolean

indicating
if the

DropTarget

is currently accepting drops.

The Component will receive drops only if it is enabled.

**Parameters:** c

- The

Component

with which this

DropTarget

is associated
**Parameters:** ops

- The default acceptable actions for this

DropTarget
**Parameters:** dtl

- The

DropTargetListener

for this

DropTarget
**Parameters:** act

- Is the

DropTarget

accepting drops.
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true
**See Also:** GraphicsEnvironment.isHeadless()

- DropTarget

```java
public DropTarget()
throws
HeadlessException
```

Creates a

DropTarget

.

**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true
**See Also:** GraphicsEnvironment.isHeadless()

- DropTarget

```java
public DropTarget​(
Component
c,

DropTargetListener
dtl)
throws
HeadlessException
```

Creates a

DropTarget

given the

Component

to associate itself with, and the

DropTargetListener

to handle event processing.

The Component will receive drops only if it is enabled.

**Parameters:** c

- The

Component

with which this

DropTarget

is associated
**Parameters:** dtl

- The

DropTargetListener

for this

DropTarget
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true
**See Also:** GraphicsEnvironment.isHeadless()

- DropTarget

```java
public DropTarget​(
Component
c,
int ops,

DropTargetListener
dtl)
throws
HeadlessException
```

Creates a

DropTarget

given the

Component

to associate itself with, an

int

representing
the default acceptable action(s) to support, and a

DropTargetListener

to handle event processing.

The Component will receive drops only if it is enabled.

**Parameters:** c

- The

Component

with which this

DropTarget

is associated
**Parameters:** ops

- The default acceptable actions for this

DropTarget
**Parameters:** dtl

- The

DropTargetListener

for this

DropTarget
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true
**See Also:** GraphicsEnvironment.isHeadless()

============ METHOD DETAIL ==========

- Method Detail

- setComponent

```java
public void setComponent​(
Component
c)
```

Note: this interface is required to permit the safe association
of a DropTarget with a Component in one of two ways, either:

component.setDropTarget(droptarget);

or

droptarget.setComponent(component);

The Component will receive drops only if it is enabled.

**Parameters:** c

- The new

Component

this

DropTarget

is to be associated with.

- getComponent

```java
public
Component
getComponent()
```

Gets the

Component

associated
with this

DropTarget

.

**Returns:** the current

Component

- setDefaultActions

```java
public void setDefaultActions​(int ops)
```

Sets the default acceptable actions for this

DropTarget

**Parameters:** ops

- the default actions
**See Also:** DnDConstants

- getDefaultActions

```java
public int getDefaultActions()
```

Gets an

int

representing the
current action(s) supported by this

DropTarget

.

**Returns:** the current default actions

- setActive

```java
public void setActive​(boolean isActive)
```

Sets the DropTarget active if

true

,
inactive if

false

.

**Parameters:** isActive

- sets the

DropTarget

(in)active.

- isActive

```java
public boolean isActive()
```

Reports whether or not
this

DropTarget

is currently active (ready to accept drops).

**Returns:** true

if active,

false

if not

- addDropTargetListener

```java
public void addDropTargetListener​(
DropTargetListener
dtl)
throws
TooManyListenersException
```

Adds a new

DropTargetListener

(UNICAST SOURCE).

**Parameters:** dtl

- The new

DropTargetListener
**Throws:** TooManyListenersException

- if a

DropTargetListener

is already added to this

DropTarget

.

- removeDropTargetListener

```java
public void removeDropTargetListener​(
DropTargetListener
dtl)
```

Removes the current

DropTargetListener

(UNICAST SOURCE).

**Parameters:** dtl

- the DropTargetListener to deregister.

- dragEnter

```java
public void dragEnter​(
DropTargetDragEvent
dtde)
```

Calls

dragEnter

on the registered

DropTargetListener

and passes it
the specified

DropTargetDragEvent

.
Has no effect if this

DropTarget

is not active.

**Specified by:** dragEnter

in interface

DropTargetListener
**Parameters:** dtde

- the

DropTargetDragEvent
**Throws:** NullPointerException

- if this

DropTarget

is active and

dtde

is

null
**See Also:** isActive()

- dragOver

```java
public void dragOver​(
DropTargetDragEvent
dtde)
```

Calls

dragOver

on the registered

DropTargetListener

and passes it
the specified

DropTargetDragEvent

.
Has no effect if this

DropTarget

is not active.

**Specified by:** dragOver

in interface

DropTargetListener
**Parameters:** dtde

- the

DropTargetDragEvent
**Throws:** NullPointerException

- if this

DropTarget

is active and

dtde

is

null
**See Also:** isActive()

- dropActionChanged

```java
public void dropActionChanged​(
DropTargetDragEvent
dtde)
```

Calls

dropActionChanged

on the registered

DropTargetListener

and passes it
the specified

DropTargetDragEvent

.
Has no effect if this

DropTarget

is not active.

**Specified by:** dropActionChanged

in interface

DropTargetListener
**Parameters:** dtde

- the

DropTargetDragEvent
**Throws:** NullPointerException

- if this

DropTarget

is active and

dtde

is

null
**See Also:** isActive()

- dragExit

```java
public void dragExit​(
DropTargetEvent
dte)
```

Calls

dragExit

on the registered

DropTargetListener

and passes it
the specified

DropTargetEvent

.
Has no effect if this

DropTarget

is not active.

This method itself does not throw any exception
for null parameter but for exceptions thrown by
the respective method of the listener.

**Specified by:** dragExit

in interface

DropTargetListener
**Parameters:** dte

- the

DropTargetEvent
**See Also:** isActive()

- drop

```java
public void drop​(
DropTargetDropEvent
dtde)
```

Calls

drop

on the registered

DropTargetListener

and passes it
the specified

DropTargetDropEvent

if this

DropTarget

is active.

**Specified by:** drop

in interface

DropTargetListener
**Parameters:** dtde

- the

DropTargetDropEvent
**Throws:** NullPointerException

- if

dtde

is null
and at least one of the following is true: this

DropTarget

is not active, or there is
no a

DropTargetListener

registered.
**See Also:** isActive()

- getFlavorMap

```java
public
FlavorMap
getFlavorMap()
```

Gets the

FlavorMap

associated with this

DropTarget

.
If no

FlavorMap

has been set for this

DropTarget

, it is associated with the default

FlavorMap

.

**Returns:** the FlavorMap for this DropTarget

- setFlavorMap

```java
public void setFlavorMap​(
FlavorMap
fm)
```

Sets the

FlavorMap

associated
with this

DropTarget

.

**Parameters:** fm

- the new

FlavorMap

, or null to
associate the default FlavorMap with this DropTarget.

- addNotify

```java
public void addNotify()
```

Notify the DropTarget that it has been associated with a Component

This method is usually called from java.awt.Component.addNotify() of
the Component associated with this DropTarget to notify the DropTarget
that a ComponentPeer has been associated with that Component.

Calling this method, other than to notify this DropTarget of the
association of the ComponentPeer with the Component may result in
a malfunction of the DnD system.

- removeNotify

```java
public void removeNotify()
```

Notify the DropTarget that it has been disassociated from a Component

This method is usually called from java.awt.Component.removeNotify() of
the Component associated with this DropTarget to notify the DropTarget
that a ComponentPeer has been disassociated with that Component.

Calling this method, other than to notify this DropTarget of the
disassociation of the ComponentPeer from the Component may result in
a malfunction of the DnD system.

- getDropTargetContext

```java
public
DropTargetContext
getDropTargetContext()
```

Gets the

DropTargetContext

associated
with this

DropTarget

.

**Returns:** the

DropTargetContext

associated with this

DropTarget

.

- createDropTargetContext

```java
protected
DropTargetContext
createDropTargetContext()
```

Creates the DropTargetContext associated with this DropTarget.
Subclasses may override this method to instantiate their own
DropTargetContext subclass.

This call is typically *only* called by the platform's
DropTargetContextPeer as a drag operation encounters this
DropTarget. Accessing the Context while no Drag is current
has undefined results.

**Returns:** the DropTargetContext associated with this DropTarget

- createDropTargetAutoScroller

```java
protected
DropTarget.DropTargetAutoScroller
createDropTargetAutoScroller​(
Component
c,

Point
p)
```

create an embedded autoscroller

**Parameters:** c

- the

Component
**Parameters:** p

- the

Point
**Returns:** an embedded autoscroller

- initializeAutoscrolling

```java
protected void initializeAutoscrolling​(
Point
p)
```

initialize autoscrolling

**Parameters:** p

- the

Point

- updateAutoscroll

```java
protected void updateAutoscroll​(
Point
dragCursorLocn)
```

update autoscrolling with current cursor location

**Parameters:** dragCursorLocn

- the

Point

- clearAutoscroll

```java
protected void clearAutoscroll()
```

clear autoscrolling

Constructor Detail

- DropTarget

```java
public DropTarget​(
Component
c,
int ops,

DropTargetListener
dtl,
boolean act,

FlavorMap
fm)
throws
HeadlessException
```

Creates a new DropTarget given the

Component

to associate itself with, an

int

representing
the default acceptable action(s) to
support, a

DropTargetListener

to handle event processing, a

boolean

indicating
if the

DropTarget

is currently accepting drops, and
a

FlavorMap

to use (or null for the default

FlavorMap

).

The Component will receive drops only if it is enabled.

**Parameters:** c

- The

Component

with which this

DropTarget

is associated
**Parameters:** ops

- The default acceptable actions for this

DropTarget
**Parameters:** dtl

- The

DropTargetListener

for this

DropTarget
**Parameters:** act

- Is the

DropTarget

accepting drops.
**Parameters:** fm

- The

FlavorMap

to use, or null for the default

FlavorMap
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true
**See Also:** GraphicsEnvironment.isHeadless()

- DropTarget

```java
public DropTarget​(
Component
c,
int ops,

DropTargetListener
dtl,
boolean act)
throws
HeadlessException
```

Creates a

DropTarget

given the

Component

to associate itself with, an

int

representing
the default acceptable action(s)
to support, a

DropTargetListener

to handle event processing, and a

boolean

indicating
if the

DropTarget

is currently accepting drops.

The Component will receive drops only if it is enabled.

**Parameters:** c

- The

Component

with which this

DropTarget

is associated
**Parameters:** ops

- The default acceptable actions for this

DropTarget
**Parameters:** dtl

- The

DropTargetListener

for this

DropTarget
**Parameters:** act

- Is the

DropTarget

accepting drops.
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true
**See Also:** GraphicsEnvironment.isHeadless()

- DropTarget

```java
public DropTarget()
throws
HeadlessException
```

Creates a

DropTarget

.

**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true
**See Also:** GraphicsEnvironment.isHeadless()

- DropTarget

```java
public DropTarget​(
Component
c,

DropTargetListener
dtl)
throws
HeadlessException
```

Creates a

DropTarget

given the

Component

to associate itself with, and the

DropTargetListener

to handle event processing.

The Component will receive drops only if it is enabled.

**Parameters:** c

- The

Component

with which this

DropTarget

is associated
**Parameters:** dtl

- The

DropTargetListener

for this

DropTarget
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true
**See Also:** GraphicsEnvironment.isHeadless()

- DropTarget

```java
public DropTarget​(
Component
c,
int ops,

DropTargetListener
dtl)
throws
HeadlessException
```

Creates a

DropTarget

given the

Component

to associate itself with, an

int

representing
the default acceptable action(s) to support, and a

DropTargetListener

to handle event processing.

The Component will receive drops only if it is enabled.

**Parameters:** c

- The

Component

with which this

DropTarget

is associated
**Parameters:** ops

- The default acceptable actions for this

DropTarget
**Parameters:** dtl

- The

DropTargetListener

for this

DropTarget
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true
**See Also:** GraphicsEnvironment.isHeadless()

---

#### Constructor Detail

DropTarget

```java
public DropTarget​(
Component
c,
int ops,

DropTargetListener
dtl,
boolean act,

FlavorMap
fm)
throws
HeadlessException
```

Creates a new DropTarget given the

Component

to associate itself with, an

int

representing
the default acceptable action(s) to
support, a

DropTargetListener

to handle event processing, a

boolean

indicating
if the

DropTarget

is currently accepting drops, and
a

FlavorMap

to use (or null for the default

FlavorMap

).

The Component will receive drops only if it is enabled.

**Parameters:** c

- The

Component

with which this

DropTarget

is associated
**Parameters:** ops

- The default acceptable actions for this

DropTarget
**Parameters:** dtl

- The

DropTargetListener

for this

DropTarget
**Parameters:** act

- Is the

DropTarget

accepting drops.
**Parameters:** fm

- The

FlavorMap

to use, or null for the default

FlavorMap
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true
**See Also:** GraphicsEnvironment.isHeadless()

---

#### DropTarget

public DropTarget​(

Component

c,
int ops,

DropTargetListener

dtl,
boolean act,

FlavorMap

fm)
throws

HeadlessException

Creates a new DropTarget given the

Component

to associate itself with, an

int

representing
the default acceptable action(s) to
support, a

DropTargetListener

to handle event processing, a

boolean

indicating
if the

DropTarget

is currently accepting drops, and
a

FlavorMap

to use (or null for the default

FlavorMap

).

The Component will receive drops only if it is enabled.

The Component will receive drops only if it is enabled.

DropTarget

```java
public DropTarget​(
Component
c,
int ops,

DropTargetListener
dtl,
boolean act)
throws
HeadlessException
```

Creates a

DropTarget

given the

Component

to associate itself with, an

int

representing
the default acceptable action(s)
to support, a

DropTargetListener

to handle event processing, and a

boolean

indicating
if the

DropTarget

is currently accepting drops.

The Component will receive drops only if it is enabled.

**Parameters:** c

- The

Component

with which this

DropTarget

is associated
**Parameters:** ops

- The default acceptable actions for this

DropTarget
**Parameters:** dtl

- The

DropTargetListener

for this

DropTarget
**Parameters:** act

- Is the

DropTarget

accepting drops.
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true
**See Also:** GraphicsEnvironment.isHeadless()

---

#### DropTarget

public DropTarget​(

Component

c,
int ops,

DropTargetListener

dtl,
boolean act)
throws

HeadlessException

Creates a

DropTarget

given the

Component

to associate itself with, an

int

representing
the default acceptable action(s)
to support, a

DropTargetListener

to handle event processing, and a

boolean

indicating
if the

DropTarget

is currently accepting drops.

The Component will receive drops only if it is enabled.

The Component will receive drops only if it is enabled.

DropTarget

```java
public DropTarget()
throws
HeadlessException
```

Creates a

DropTarget

.

**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true
**See Also:** GraphicsEnvironment.isHeadless()

---

#### DropTarget

public DropTarget()
throws

HeadlessException

Creates a

DropTarget

.

DropTarget

```java
public DropTarget​(
Component
c,

DropTargetListener
dtl)
throws
HeadlessException
```

Creates a

DropTarget

given the

Component

to associate itself with, and the

DropTargetListener

to handle event processing.

The Component will receive drops only if it is enabled.

**Parameters:** c

- The

Component

with which this

DropTarget

is associated
**Parameters:** dtl

- The

DropTargetListener

for this

DropTarget
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true
**See Also:** GraphicsEnvironment.isHeadless()

---

#### DropTarget

public DropTarget​(

Component

c,

DropTargetListener

dtl)
throws

HeadlessException

Creates a

DropTarget

given the

Component

to associate itself with, and the

DropTargetListener

to handle event processing.

The Component will receive drops only if it is enabled.

The Component will receive drops only if it is enabled.

DropTarget

```java
public DropTarget​(
Component
c,
int ops,

DropTargetListener
dtl)
throws
HeadlessException
```

Creates a

DropTarget

given the

Component

to associate itself with, an

int

representing
the default acceptable action(s) to support, and a

DropTargetListener

to handle event processing.

The Component will receive drops only if it is enabled.

**Parameters:** c

- The

Component

with which this

DropTarget

is associated
**Parameters:** ops

- The default acceptable actions for this

DropTarget
**Parameters:** dtl

- The

DropTargetListener

for this

DropTarget
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true
**See Also:** GraphicsEnvironment.isHeadless()

---

#### DropTarget

public DropTarget​(

Component

c,
int ops,

DropTargetListener

dtl)
throws

HeadlessException

Creates a

DropTarget

given the

Component

to associate itself with, an

int

representing
the default acceptable action(s) to support, and a

DropTargetListener

to handle event processing.

The Component will receive drops only if it is enabled.

The Component will receive drops only if it is enabled.

Method Detail

- setComponent

```java
public void setComponent​(
Component
c)
```

Note: this interface is required to permit the safe association
of a DropTarget with a Component in one of two ways, either:

component.setDropTarget(droptarget);

or

droptarget.setComponent(component);

The Component will receive drops only if it is enabled.

**Parameters:** c

- The new

Component

this

DropTarget

is to be associated with.

- getComponent

```java
public
Component
getComponent()
```

Gets the

Component

associated
with this

DropTarget

.

**Returns:** the current

Component

- setDefaultActions

```java
public void setDefaultActions​(int ops)
```

Sets the default acceptable actions for this

DropTarget

**Parameters:** ops

- the default actions
**See Also:** DnDConstants

- getDefaultActions

```java
public int getDefaultActions()
```

Gets an

int

representing the
current action(s) supported by this

DropTarget

.

**Returns:** the current default actions

- setActive

```java
public void setActive​(boolean isActive)
```

Sets the DropTarget active if

true

,
inactive if

false

.

**Parameters:** isActive

- sets the

DropTarget

(in)active.

- isActive

```java
public boolean isActive()
```

Reports whether or not
this

DropTarget

is currently active (ready to accept drops).

**Returns:** true

if active,

false

if not

- addDropTargetListener

```java
public void addDropTargetListener​(
DropTargetListener
dtl)
throws
TooManyListenersException
```

Adds a new

DropTargetListener

(UNICAST SOURCE).

**Parameters:** dtl

- The new

DropTargetListener
**Throws:** TooManyListenersException

- if a

DropTargetListener

is already added to this

DropTarget

.

- removeDropTargetListener

```java
public void removeDropTargetListener​(
DropTargetListener
dtl)
```

Removes the current

DropTargetListener

(UNICAST SOURCE).

**Parameters:** dtl

- the DropTargetListener to deregister.

- dragEnter

```java
public void dragEnter​(
DropTargetDragEvent
dtde)
```

Calls

dragEnter

on the registered

DropTargetListener

and passes it
the specified

DropTargetDragEvent

.
Has no effect if this

DropTarget

is not active.

**Specified by:** dragEnter

in interface

DropTargetListener
**Parameters:** dtde

- the

DropTargetDragEvent
**Throws:** NullPointerException

- if this

DropTarget

is active and

dtde

is

null
**See Also:** isActive()

- dragOver

```java
public void dragOver​(
DropTargetDragEvent
dtde)
```

Calls

dragOver

on the registered

DropTargetListener

and passes it
the specified

DropTargetDragEvent

.
Has no effect if this

DropTarget

is not active.

**Specified by:** dragOver

in interface

DropTargetListener
**Parameters:** dtde

- the

DropTargetDragEvent
**Throws:** NullPointerException

- if this

DropTarget

is active and

dtde

is

null
**See Also:** isActive()

- dropActionChanged

```java
public void dropActionChanged​(
DropTargetDragEvent
dtde)
```

Calls

dropActionChanged

on the registered

DropTargetListener

and passes it
the specified

DropTargetDragEvent

.
Has no effect if this

DropTarget

is not active.

**Specified by:** dropActionChanged

in interface

DropTargetListener
**Parameters:** dtde

- the

DropTargetDragEvent
**Throws:** NullPointerException

- if this

DropTarget

is active and

dtde

is

null
**See Also:** isActive()

- dragExit

```java
public void dragExit​(
DropTargetEvent
dte)
```

Calls

dragExit

on the registered

DropTargetListener

and passes it
the specified

DropTargetEvent

.
Has no effect if this

DropTarget

is not active.

This method itself does not throw any exception
for null parameter but for exceptions thrown by
the respective method of the listener.

**Specified by:** dragExit

in interface

DropTargetListener
**Parameters:** dte

- the

DropTargetEvent
**See Also:** isActive()

- drop

```java
public void drop​(
DropTargetDropEvent
dtde)
```

Calls

drop

on the registered

DropTargetListener

and passes it
the specified

DropTargetDropEvent

if this

DropTarget

is active.

**Specified by:** drop

in interface

DropTargetListener
**Parameters:** dtde

- the

DropTargetDropEvent
**Throws:** NullPointerException

- if

dtde

is null
and at least one of the following is true: this

DropTarget

is not active, or there is
no a

DropTargetListener

registered.
**See Also:** isActive()

- getFlavorMap

```java
public
FlavorMap
getFlavorMap()
```

Gets the

FlavorMap

associated with this

DropTarget

.
If no

FlavorMap

has been set for this

DropTarget

, it is associated with the default

FlavorMap

.

**Returns:** the FlavorMap for this DropTarget

- setFlavorMap

```java
public void setFlavorMap​(
FlavorMap
fm)
```

Sets the

FlavorMap

associated
with this

DropTarget

.

**Parameters:** fm

- the new

FlavorMap

, or null to
associate the default FlavorMap with this DropTarget.

- addNotify

```java
public void addNotify()
```

Notify the DropTarget that it has been associated with a Component

This method is usually called from java.awt.Component.addNotify() of
the Component associated with this DropTarget to notify the DropTarget
that a ComponentPeer has been associated with that Component.

Calling this method, other than to notify this DropTarget of the
association of the ComponentPeer with the Component may result in
a malfunction of the DnD system.

- removeNotify

```java
public void removeNotify()
```

Notify the DropTarget that it has been disassociated from a Component

This method is usually called from java.awt.Component.removeNotify() of
the Component associated with this DropTarget to notify the DropTarget
that a ComponentPeer has been disassociated with that Component.

Calling this method, other than to notify this DropTarget of the
disassociation of the ComponentPeer from the Component may result in
a malfunction of the DnD system.

- getDropTargetContext

```java
public
DropTargetContext
getDropTargetContext()
```

Gets the

DropTargetContext

associated
with this

DropTarget

.

**Returns:** the

DropTargetContext

associated with this

DropTarget

.

- createDropTargetContext

```java
protected
DropTargetContext
createDropTargetContext()
```

Creates the DropTargetContext associated with this DropTarget.
Subclasses may override this method to instantiate their own
DropTargetContext subclass.

This call is typically *only* called by the platform's
DropTargetContextPeer as a drag operation encounters this
DropTarget. Accessing the Context while no Drag is current
has undefined results.

**Returns:** the DropTargetContext associated with this DropTarget

- createDropTargetAutoScroller

```java
protected
DropTarget.DropTargetAutoScroller
createDropTargetAutoScroller​(
Component
c,

Point
p)
```

create an embedded autoscroller

**Parameters:** c

- the

Component
**Parameters:** p

- the

Point
**Returns:** an embedded autoscroller

- initializeAutoscrolling

```java
protected void initializeAutoscrolling​(
Point
p)
```

initialize autoscrolling

**Parameters:** p

- the

Point

- updateAutoscroll

```java
protected void updateAutoscroll​(
Point
dragCursorLocn)
```

update autoscrolling with current cursor location

**Parameters:** dragCursorLocn

- the

Point

- clearAutoscroll

```java
protected void clearAutoscroll()
```

clear autoscrolling

---

#### Method Detail

setComponent

```java
public void setComponent​(
Component
c)
```

Note: this interface is required to permit the safe association
of a DropTarget with a Component in one of two ways, either:

component.setDropTarget(droptarget);

or

droptarget.setComponent(component);

The Component will receive drops only if it is enabled.

**Parameters:** c

- The new

Component

this

DropTarget

is to be associated with.

---

#### setComponent

public void setComponent​(

Component

c)

Note: this interface is required to permit the safe association
of a DropTarget with a Component in one of two ways, either:

component.setDropTarget(droptarget);

or

droptarget.setComponent(component);

The Component will receive drops only if it is enabled.

The Component will receive drops only if it is enabled.

getComponent

```java
public
Component
getComponent()
```

Gets the

Component

associated
with this

DropTarget

.

**Returns:** the current

Component

---

#### getComponent

public

Component

getComponent()

Gets the

Component

associated
with this

DropTarget

.

setDefaultActions

```java
public void setDefaultActions​(int ops)
```

Sets the default acceptable actions for this

DropTarget

**Parameters:** ops

- the default actions
**See Also:** DnDConstants

---

#### setDefaultActions

public void setDefaultActions​(int ops)

Sets the default acceptable actions for this

DropTarget

getDefaultActions

```java
public int getDefaultActions()
```

Gets an

int

representing the
current action(s) supported by this

DropTarget

.

**Returns:** the current default actions

---

#### getDefaultActions

public int getDefaultActions()

Gets an

int

representing the
current action(s) supported by this

DropTarget

.

setActive

```java
public void setActive​(boolean isActive)
```

Sets the DropTarget active if

true

,
inactive if

false

.

**Parameters:** isActive

- sets the

DropTarget

(in)active.

---

#### setActive

public void setActive​(boolean isActive)

Sets the DropTarget active if

true

,
inactive if

false

.

isActive

```java
public boolean isActive()
```

Reports whether or not
this

DropTarget

is currently active (ready to accept drops).

**Returns:** true

if active,

false

if not

---

#### isActive

public boolean isActive()

Reports whether or not
this

DropTarget

is currently active (ready to accept drops).

addDropTargetListener

```java
public void addDropTargetListener​(
DropTargetListener
dtl)
throws
TooManyListenersException
```

Adds a new

DropTargetListener

(UNICAST SOURCE).

**Parameters:** dtl

- The new

DropTargetListener
**Throws:** TooManyListenersException

- if a

DropTargetListener

is already added to this

DropTarget

.

---

#### addDropTargetListener

public void addDropTargetListener​(

DropTargetListener

dtl)
throws

TooManyListenersException

Adds a new

DropTargetListener

(UNICAST SOURCE).

removeDropTargetListener

```java
public void removeDropTargetListener​(
DropTargetListener
dtl)
```

Removes the current

DropTargetListener

(UNICAST SOURCE).

**Parameters:** dtl

- the DropTargetListener to deregister.

---

#### removeDropTargetListener

public void removeDropTargetListener​(

DropTargetListener

dtl)

Removes the current

DropTargetListener

(UNICAST SOURCE).

dragEnter

```java
public void dragEnter​(
DropTargetDragEvent
dtde)
```

Calls

dragEnter

on the registered

DropTargetListener

and passes it
the specified

DropTargetDragEvent

.
Has no effect if this

DropTarget

is not active.

**Specified by:** dragEnter

in interface

DropTargetListener
**Parameters:** dtde

- the

DropTargetDragEvent
**Throws:** NullPointerException

- if this

DropTarget

is active and

dtde

is

null
**See Also:** isActive()

---

#### dragEnter

public void dragEnter​(

DropTargetDragEvent

dtde)

Calls

dragEnter

on the registered

DropTargetListener

and passes it
the specified

DropTargetDragEvent

.
Has no effect if this

DropTarget

is not active.

dragOver

```java
public void dragOver​(
DropTargetDragEvent
dtde)
```

Calls

dragOver

on the registered

DropTargetListener

and passes it
the specified

DropTargetDragEvent

.
Has no effect if this

DropTarget

is not active.

**Specified by:** dragOver

in interface

DropTargetListener
**Parameters:** dtde

- the

DropTargetDragEvent
**Throws:** NullPointerException

- if this

DropTarget

is active and

dtde

is

null
**See Also:** isActive()

---

#### dragOver

public void dragOver​(

DropTargetDragEvent

dtde)

Calls

dragOver

on the registered

DropTargetListener

and passes it
the specified

DropTargetDragEvent

.
Has no effect if this

DropTarget

is not active.

dropActionChanged

```java
public void dropActionChanged​(
DropTargetDragEvent
dtde)
```

Calls

dropActionChanged

on the registered

DropTargetListener

and passes it
the specified

DropTargetDragEvent

.
Has no effect if this

DropTarget

is not active.

**Specified by:** dropActionChanged

in interface

DropTargetListener
**Parameters:** dtde

- the

DropTargetDragEvent
**Throws:** NullPointerException

- if this

DropTarget

is active and

dtde

is

null
**See Also:** isActive()

---

#### dropActionChanged

public void dropActionChanged​(

DropTargetDragEvent

dtde)

Calls

dropActionChanged

on the registered

DropTargetListener

and passes it
the specified

DropTargetDragEvent

.
Has no effect if this

DropTarget

is not active.

dragExit

```java
public void dragExit​(
DropTargetEvent
dte)
```

Calls

dragExit

on the registered

DropTargetListener

and passes it
the specified

DropTargetEvent

.
Has no effect if this

DropTarget

is not active.

This method itself does not throw any exception
for null parameter but for exceptions thrown by
the respective method of the listener.

**Specified by:** dragExit

in interface

DropTargetListener
**Parameters:** dte

- the

DropTargetEvent
**See Also:** isActive()

---

#### dragExit

public void dragExit​(

DropTargetEvent

dte)

Calls

dragExit

on the registered

DropTargetListener

and passes it
the specified

DropTargetEvent

.
Has no effect if this

DropTarget

is not active.

This method itself does not throw any exception
for null parameter but for exceptions thrown by
the respective method of the listener.

This method itself does not throw any exception
for null parameter but for exceptions thrown by
the respective method of the listener.

drop

```java
public void drop​(
DropTargetDropEvent
dtde)
```

Calls

drop

on the registered

DropTargetListener

and passes it
the specified

DropTargetDropEvent

if this

DropTarget

is active.

**Specified by:** drop

in interface

DropTargetListener
**Parameters:** dtde

- the

DropTargetDropEvent
**Throws:** NullPointerException

- if

dtde

is null
and at least one of the following is true: this

DropTarget

is not active, or there is
no a

DropTargetListener

registered.
**See Also:** isActive()

---

#### drop

public void drop​(

DropTargetDropEvent

dtde)

Calls

drop

on the registered

DropTargetListener

and passes it
the specified

DropTargetDropEvent

if this

DropTarget

is active.

getFlavorMap

```java
public
FlavorMap
getFlavorMap()
```

Gets the

FlavorMap

associated with this

DropTarget

.
If no

FlavorMap

has been set for this

DropTarget

, it is associated with the default

FlavorMap

.

**Returns:** the FlavorMap for this DropTarget

---

#### getFlavorMap

public

FlavorMap

getFlavorMap()

Gets the

FlavorMap

associated with this

DropTarget

.
If no

FlavorMap

has been set for this

DropTarget

, it is associated with the default

FlavorMap

.

setFlavorMap

```java
public void setFlavorMap​(
FlavorMap
fm)
```

Sets the

FlavorMap

associated
with this

DropTarget

.

**Parameters:** fm

- the new

FlavorMap

, or null to
associate the default FlavorMap with this DropTarget.

---

#### setFlavorMap

public void setFlavorMap​(

FlavorMap

fm)

Sets the

FlavorMap

associated
with this

DropTarget

.

addNotify

```java
public void addNotify()
```

Notify the DropTarget that it has been associated with a Component

This method is usually called from java.awt.Component.addNotify() of
the Component associated with this DropTarget to notify the DropTarget
that a ComponentPeer has been associated with that Component.

Calling this method, other than to notify this DropTarget of the
association of the ComponentPeer with the Component may result in
a malfunction of the DnD system.

---

#### addNotify

public void addNotify()

Notify the DropTarget that it has been associated with a Component

This method is usually called from java.awt.Component.addNotify() of
the Component associated with this DropTarget to notify the DropTarget
that a ComponentPeer has been associated with that Component.

Calling this method, other than to notify this DropTarget of the
association of the ComponentPeer with the Component may result in
a malfunction of the DnD system.

removeNotify

```java
public void removeNotify()
```

Notify the DropTarget that it has been disassociated from a Component

This method is usually called from java.awt.Component.removeNotify() of
the Component associated with this DropTarget to notify the DropTarget
that a ComponentPeer has been disassociated with that Component.

Calling this method, other than to notify this DropTarget of the
disassociation of the ComponentPeer from the Component may result in
a malfunction of the DnD system.

---

#### removeNotify

public void removeNotify()

Notify the DropTarget that it has been disassociated from a Component

This method is usually called from java.awt.Component.removeNotify() of
the Component associated with this DropTarget to notify the DropTarget
that a ComponentPeer has been disassociated with that Component.

Calling this method, other than to notify this DropTarget of the
disassociation of the ComponentPeer from the Component may result in
a malfunction of the DnD system.

getDropTargetContext

```java
public
DropTargetContext
getDropTargetContext()
```

Gets the

DropTargetContext

associated
with this

DropTarget

.

**Returns:** the

DropTargetContext

associated with this

DropTarget

.

---

#### getDropTargetContext

public

DropTargetContext

getDropTargetContext()

Gets the

DropTargetContext

associated
with this

DropTarget

.

createDropTargetContext

```java
protected
DropTargetContext
createDropTargetContext()
```

Creates the DropTargetContext associated with this DropTarget.
Subclasses may override this method to instantiate their own
DropTargetContext subclass.

This call is typically *only* called by the platform's
DropTargetContextPeer as a drag operation encounters this
DropTarget. Accessing the Context while no Drag is current
has undefined results.

**Returns:** the DropTargetContext associated with this DropTarget

---

#### createDropTargetContext

protected

DropTargetContext

createDropTargetContext()

Creates the DropTargetContext associated with this DropTarget.
Subclasses may override this method to instantiate their own
DropTargetContext subclass.

This call is typically *only* called by the platform's
DropTargetContextPeer as a drag operation encounters this
DropTarget. Accessing the Context while no Drag is current
has undefined results.

createDropTargetAutoScroller

```java
protected
DropTarget.DropTargetAutoScroller
createDropTargetAutoScroller​(
Component
c,

Point
p)
```

create an embedded autoscroller

**Parameters:** c

- the

Component
**Parameters:** p

- the

Point
**Returns:** an embedded autoscroller

---

#### createDropTargetAutoScroller

protected

DropTarget.DropTargetAutoScroller

createDropTargetAutoScroller​(

Component

c,

Point

p)

create an embedded autoscroller

initializeAutoscrolling

```java
protected void initializeAutoscrolling​(
Point
p)
```

initialize autoscrolling

**Parameters:** p

- the

Point

---

#### initializeAutoscrolling

protected void initializeAutoscrolling​(

Point

p)

initialize autoscrolling

updateAutoscroll

```java
protected void updateAutoscroll​(
Point
dragCursorLocn)
```

update autoscrolling with current cursor location

**Parameters:** dragCursorLocn

- the

Point

---

#### updateAutoscroll

protected void updateAutoscroll​(

Point

dragCursorLocn)

update autoscrolling with current cursor location

clearAutoscroll

```java
protected void clearAutoscroll()
```

clear autoscrolling

---

#### clearAutoscroll

protected void clearAutoscroll()

clear autoscrolling

---

