# Class DropTargetAdapter

**Source:** `java.desktop\java\awt\dnd\DropTargetAdapter.html`

### Class Description

```java
public abstract class
DropTargetAdapter

extends
Object

implements
DropTargetListener
```

An abstract adapter class for receiving drop target events. The methods in
this class are empty. This class exists only as a convenience for creating
listener objects.

Extend this class to create a

DropTargetEvent

listener
and override the methods for the events of interest. (If you implement the

DropTargetListener

interface, you have to define all of
the methods in it. This abstract class defines a null implementation for
every method except

drop(DropTargetDropEvent)

, so you only have
to define methods for events you care about.) You must provide an
implementation for at least

drop(DropTargetDropEvent)

. This
method cannot have a null implementation because its specification requires
that you either accept or reject the drop, and, if accepted, indicate
whether the drop was successful.

Create a listener object using the extended class and then register it with
a

DropTarget

. When the drag enters, moves over, or exits
the operable part of the drop site for that

DropTarget

, when
the drop action changes, and when the drop occurs, the relevant method in
the listener object is invoked, and the

DropTargetEvent

is
passed to it.

The operable part of the drop site for the

DropTarget

is
the part of the associated

Component

's geometry that is not
obscured by an overlapping top-level window or by another

Component

higher in the Z-order that has an associated active

DropTarget

.

During the drag, the data associated with the current drag operation can be
retrieved by calling

getTransferable()

on

DropTargetDragEvent

instances passed to the listener's
methods.

Note that

getTransferable()

on the

DropTargetDragEvent

instance should only be called within the
respective listener's method and all the necessary data should be retrieved
from the returned

Transferable

before that method returns.

**All Implemented Interfaces:** DropTargetListener

,

EventListener

---

### Field Details

*No entries found.*

### Constructor Details

#### public DropTargetAdapter()

*No description found.*

---

### Method Details

#### public void dragEnter​(
DropTargetDragEvent
dtde)

Called while a drag operation is ongoing, when the mouse pointer enters
the operable part of the drop site for the

DropTarget

registered with this listener.

**Specified by:**
- dragEnter

in interface

DropTargetListener

**Parameters:**
- dtde

- the

DropTargetDragEvent

---

#### public void dragOver​(
DropTargetDragEvent
dtde)

Called when a drag operation is ongoing, while the mouse pointer is still
over the operable part of the drop site for the

DropTarget

registered with this listener.

**Specified by:**
- dragOver

in interface

DropTargetListener

**Parameters:**
- dtde

- the

DropTargetDragEvent

---

#### public void dropActionChanged​(
DropTargetDragEvent
dtde)

Called if the user has modified
the current drop gesture.

**Specified by:**
- dropActionChanged

in interface

DropTargetListener

**Parameters:**
- dtde

- the

DropTargetDragEvent

---

#### public void dragExit​(
DropTargetEvent
dte)

Called while a drag operation is ongoing, when the mouse pointer has
exited the operable part of the drop site for the

DropTarget

registered with this listener.

**Specified by:**
- dragExit

in interface

DropTargetListener

**Parameters:**
- dte

- the

DropTargetEvent

---

### Additional Sections

#### Class DropTargetAdapter

java.lang.Object

- java.awt.dnd.DropTargetAdapter

java.awt.dnd.DropTargetAdapter

**All Implemented Interfaces:** DropTargetListener

,

EventListener

```java
public abstract class
DropTargetAdapter

extends
Object

implements
DropTargetListener
```

An abstract adapter class for receiving drop target events. The methods in
this class are empty. This class exists only as a convenience for creating
listener objects.

Extend this class to create a

DropTargetEvent

listener
and override the methods for the events of interest. (If you implement the

DropTargetListener

interface, you have to define all of
the methods in it. This abstract class defines a null implementation for
every method except

drop(DropTargetDropEvent)

, so you only have
to define methods for events you care about.) You must provide an
implementation for at least

drop(DropTargetDropEvent)

. This
method cannot have a null implementation because its specification requires
that you either accept or reject the drop, and, if accepted, indicate
whether the drop was successful.

Create a listener object using the extended class and then register it with
a

DropTarget

. When the drag enters, moves over, or exits
the operable part of the drop site for that

DropTarget

, when
the drop action changes, and when the drop occurs, the relevant method in
the listener object is invoked, and the

DropTargetEvent

is
passed to it.

The operable part of the drop site for the

DropTarget

is
the part of the associated

Component

's geometry that is not
obscured by an overlapping top-level window or by another

Component

higher in the Z-order that has an associated active

DropTarget

.

During the drag, the data associated with the current drag operation can be
retrieved by calling

getTransferable()

on

DropTargetDragEvent

instances passed to the listener's
methods.

Note that

getTransferable()

on the

DropTargetDragEvent

instance should only be called within the
respective listener's method and all the necessary data should be retrieved
from the returned

Transferable

before that method returns.

**Since:** 1.4
**See Also:** DropTargetEvent

,

DropTargetListener

public abstract class

DropTargetAdapter

extends

Object

implements

DropTargetListener

An abstract adapter class for receiving drop target events. The methods in
this class are empty. This class exists only as a convenience for creating
listener objects.

Extend this class to create a

DropTargetEvent

listener
and override the methods for the events of interest. (If you implement the

DropTargetListener

interface, you have to define all of
the methods in it. This abstract class defines a null implementation for
every method except

drop(DropTargetDropEvent)

, so you only have
to define methods for events you care about.) You must provide an
implementation for at least

drop(DropTargetDropEvent)

. This
method cannot have a null implementation because its specification requires
that you either accept or reject the drop, and, if accepted, indicate
whether the drop was successful.

Create a listener object using the extended class and then register it with
a

DropTarget

. When the drag enters, moves over, or exits
the operable part of the drop site for that

DropTarget

, when
the drop action changes, and when the drop occurs, the relevant method in
the listener object is invoked, and the

DropTargetEvent

is
passed to it.

The operable part of the drop site for the

DropTarget

is
the part of the associated

Component

's geometry that is not
obscured by an overlapping top-level window or by another

Component

higher in the Z-order that has an associated active

DropTarget

.

During the drag, the data associated with the current drag operation can be
retrieved by calling

getTransferable()

on

DropTargetDragEvent

instances passed to the listener's
methods.

Note that

getTransferable()

on the

DropTargetDragEvent

instance should only be called within the
respective listener's method and all the necessary data should be retrieved
from the returned

Transferable

before that method returns.

Extend this class to create a

DropTargetEvent

listener
and override the methods for the events of interest. (If you implement the

DropTargetListener

interface, you have to define all of
the methods in it. This abstract class defines a null implementation for
every method except

drop(DropTargetDropEvent)

, so you only have
to define methods for events you care about.) You must provide an
implementation for at least

drop(DropTargetDropEvent)

. This
method cannot have a null implementation because its specification requires
that you either accept or reject the drop, and, if accepted, indicate
whether the drop was successful.

Create a listener object using the extended class and then register it with
a

DropTarget

. When the drag enters, moves over, or exits
the operable part of the drop site for that

DropTarget

, when
the drop action changes, and when the drop occurs, the relevant method in
the listener object is invoked, and the

DropTargetEvent

is
passed to it.

The operable part of the drop site for the

DropTarget

is
the part of the associated

Component

's geometry that is not
obscured by an overlapping top-level window or by another

Component

higher in the Z-order that has an associated active

DropTarget

.

During the drag, the data associated with the current drag operation can be
retrieved by calling

getTransferable()

on

DropTargetDragEvent

instances passed to the listener's
methods.

Note that

getTransferable()

on the

DropTargetDragEvent

instance should only be called within the
respective listener's method and all the necessary data should be retrieved
from the returned

Transferable

before that method returns.

Create a listener object using the extended class and then register it with
a

DropTarget

. When the drag enters, moves over, or exits
the operable part of the drop site for that

DropTarget

, when
the drop action changes, and when the drop occurs, the relevant method in
the listener object is invoked, and the

DropTargetEvent

is
passed to it.

The operable part of the drop site for the

DropTarget

is
the part of the associated

Component

's geometry that is not
obscured by an overlapping top-level window or by another

Component

higher in the Z-order that has an associated active

DropTarget

.

During the drag, the data associated with the current drag operation can be
retrieved by calling

getTransferable()

on

DropTargetDragEvent

instances passed to the listener's
methods.

Note that

getTransferable()

on the

DropTargetDragEvent

instance should only be called within the
respective listener's method and all the necessary data should be retrieved
from the returned

Transferable

before that method returns.

The operable part of the drop site for the

DropTarget

is
the part of the associated

Component

's geometry that is not
obscured by an overlapping top-level window or by another

Component

higher in the Z-order that has an associated active

DropTarget

.

During the drag, the data associated with the current drag operation can be
retrieved by calling

getTransferable()

on

DropTargetDragEvent

instances passed to the listener's
methods.

Note that

getTransferable()

on the

DropTargetDragEvent

instance should only be called within the
respective listener's method and all the necessary data should be retrieved
from the returned

Transferable

before that method returns.

During the drag, the data associated with the current drag operation can be
retrieved by calling

getTransferable()

on

DropTargetDragEvent

instances passed to the listener's
methods.

Note that

getTransferable()

on the

DropTargetDragEvent

instance should only be called within the
respective listener's method and all the necessary data should be retrieved
from the returned

Transferable

before that method returns.

Note that

getTransferable()

on the

DropTargetDragEvent

instance should only be called within the
respective listener's method and all the necessary data should be retrieved
from the returned

Transferable

before that method returns.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DropTargetAdapter

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

dragEnter

​(

DropTargetDragEvent

dtde)

Called while a drag operation is ongoing, when the mouse pointer enters
the operable part of the drop site for the

DropTarget

registered with this listener.

void

dragExit

​(

DropTargetEvent

dte)

Called while a drag operation is ongoing, when the mouse pointer has
exited the operable part of the drop site for the

DropTarget

registered with this listener.

void

dragOver

​(

DropTargetDragEvent

dtde)

Called when a drag operation is ongoing, while the mouse pointer is still
over the operable part of the drop site for the

DropTarget

registered with this listener.

void

dropActionChanged

​(

DropTargetDragEvent

dtde)

Called if the user has modified
the current drop gesture.

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

- Methods declared in interface java.awt.dnd.

DropTargetListener

drop

Constructor Summary

Constructors

Constructor

Description

DropTargetAdapter

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

dragEnter

​(

DropTargetDragEvent

dtde)

Called while a drag operation is ongoing, when the mouse pointer enters
the operable part of the drop site for the

DropTarget

registered with this listener.

void

dragExit

​(

DropTargetEvent

dte)

Called while a drag operation is ongoing, when the mouse pointer has
exited the operable part of the drop site for the

DropTarget

registered with this listener.

void

dragOver

​(

DropTargetDragEvent

dtde)

Called when a drag operation is ongoing, while the mouse pointer is still
over the operable part of the drop site for the

DropTarget

registered with this listener.

void

dropActionChanged

​(

DropTargetDragEvent

dtde)

Called if the user has modified
the current drop gesture.

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

- Methods declared in interface java.awt.dnd.

DropTargetListener

drop

---

#### Method Summary

Called while a drag operation is ongoing, when the mouse pointer enters
the operable part of the drop site for the

DropTarget

registered with this listener.

Called while a drag operation is ongoing, when the mouse pointer has
exited the operable part of the drop site for the

DropTarget

registered with this listener.

Called when a drag operation is ongoing, while the mouse pointer is still
over the operable part of the drop site for the

DropTarget

registered with this listener.

Called if the user has modified
the current drop gesture.

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

Methods declared in interface java.awt.dnd.

DropTargetListener

drop

---

#### Methods declared in interface java.awt.dnd. DropTargetListener

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DropTargetAdapter

```java
public DropTargetAdapter()
```

============ METHOD DETAIL ==========

- Method Detail

- dragEnter

```java
public void dragEnter​(
DropTargetDragEvent
dtde)
```

Called while a drag operation is ongoing, when the mouse pointer enters
the operable part of the drop site for the

DropTarget

registered with this listener.

**Specified by:** dragEnter

in interface

DropTargetListener
**Parameters:** dtde

- the

DropTargetDragEvent

- dragOver

```java
public void dragOver​(
DropTargetDragEvent
dtde)
```

Called when a drag operation is ongoing, while the mouse pointer is still
over the operable part of the drop site for the

DropTarget

registered with this listener.

**Specified by:** dragOver

in interface

DropTargetListener
**Parameters:** dtde

- the

DropTargetDragEvent

- dropActionChanged

```java
public void dropActionChanged​(
DropTargetDragEvent
dtde)
```

Called if the user has modified
the current drop gesture.

**Specified by:** dropActionChanged

in interface

DropTargetListener
**Parameters:** dtde

- the

DropTargetDragEvent

- dragExit

```java
public void dragExit​(
DropTargetEvent
dte)
```

Called while a drag operation is ongoing, when the mouse pointer has
exited the operable part of the drop site for the

DropTarget

registered with this listener.

**Specified by:** dragExit

in interface

DropTargetListener
**Parameters:** dte

- the

DropTargetEvent

Constructor Detail

- DropTargetAdapter

```java
public DropTargetAdapter()
```

---

#### Constructor Detail

DropTargetAdapter

```java
public DropTargetAdapter()
```

---

#### DropTargetAdapter

public DropTargetAdapter()

Method Detail

- dragEnter

```java
public void dragEnter​(
DropTargetDragEvent
dtde)
```

Called while a drag operation is ongoing, when the mouse pointer enters
the operable part of the drop site for the

DropTarget

registered with this listener.

**Specified by:** dragEnter

in interface

DropTargetListener
**Parameters:** dtde

- the

DropTargetDragEvent

- dragOver

```java
public void dragOver​(
DropTargetDragEvent
dtde)
```

Called when a drag operation is ongoing, while the mouse pointer is still
over the operable part of the drop site for the

DropTarget

registered with this listener.

**Specified by:** dragOver

in interface

DropTargetListener
**Parameters:** dtde

- the

DropTargetDragEvent

- dropActionChanged

```java
public void dropActionChanged​(
DropTargetDragEvent
dtde)
```

Called if the user has modified
the current drop gesture.

**Specified by:** dropActionChanged

in interface

DropTargetListener
**Parameters:** dtde

- the

DropTargetDragEvent

- dragExit

```java
public void dragExit​(
DropTargetEvent
dte)
```

Called while a drag operation is ongoing, when the mouse pointer has
exited the operable part of the drop site for the

DropTarget

registered with this listener.

**Specified by:** dragExit

in interface

DropTargetListener
**Parameters:** dte

- the

DropTargetEvent

---

#### Method Detail

dragEnter

```java
public void dragEnter​(
DropTargetDragEvent
dtde)
```

Called while a drag operation is ongoing, when the mouse pointer enters
the operable part of the drop site for the

DropTarget

registered with this listener.

**Specified by:** dragEnter

in interface

DropTargetListener
**Parameters:** dtde

- the

DropTargetDragEvent

---

#### dragEnter

public void dragEnter​(

DropTargetDragEvent

dtde)

Called while a drag operation is ongoing, when the mouse pointer enters
the operable part of the drop site for the

DropTarget

registered with this listener.

dragOver

```java
public void dragOver​(
DropTargetDragEvent
dtde)
```

Called when a drag operation is ongoing, while the mouse pointer is still
over the operable part of the drop site for the

DropTarget

registered with this listener.

**Specified by:** dragOver

in interface

DropTargetListener
**Parameters:** dtde

- the

DropTargetDragEvent

---

#### dragOver

public void dragOver​(

DropTargetDragEvent

dtde)

Called when a drag operation is ongoing, while the mouse pointer is still
over the operable part of the drop site for the

DropTarget

registered with this listener.

dropActionChanged

```java
public void dropActionChanged​(
DropTargetDragEvent
dtde)
```

Called if the user has modified
the current drop gesture.

**Specified by:** dropActionChanged

in interface

DropTargetListener
**Parameters:** dtde

- the

DropTargetDragEvent

---

#### dropActionChanged

public void dropActionChanged​(

DropTargetDragEvent

dtde)

Called if the user has modified
the current drop gesture.

dragExit

```java
public void dragExit​(
DropTargetEvent
dte)
```

Called while a drag operation is ongoing, when the mouse pointer has
exited the operable part of the drop site for the

DropTarget

registered with this listener.

**Specified by:** dragExit

in interface

DropTargetListener
**Parameters:** dte

- the

DropTargetEvent

---

#### dragExit

public void dragExit​(

DropTargetEvent

dte)

Called while a drag operation is ongoing, when the mouse pointer has
exited the operable part of the drop site for the

DropTarget

registered with this listener.

---

