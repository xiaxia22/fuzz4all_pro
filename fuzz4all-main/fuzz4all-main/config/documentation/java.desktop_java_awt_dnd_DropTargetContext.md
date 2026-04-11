# Class DropTargetContext

**Source:** `java.desktop\java\awt\dnd\DropTargetContext.html`

### Class Description

```java
public class
DropTargetContext

extends
Object

implements
Serializable
```

A

DropTargetContext

is created
whenever the logical cursor associated
with a Drag and Drop operation coincides with the visible geometry of
a

Component

associated with a

DropTarget

.
The

DropTargetContext

provides
the mechanism for a potential receiver
of a drop operation to both provide the end user with the appropriate
drag under feedback, but also to effect the subsequent data transfer
if appropriate.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
DropTarget
getDropTarget()

This method returns the

DropTarget

associated with this

DropTargetContext

.

**Returns:**
- the

DropTarget

associated with this

DropTargetContext

---

#### public
Component
getComponent()

This method returns the

Component

associated with
this

DropTargetContext

.

**Returns:**
- the Component associated with this Context

---

#### protected void setTargetActions​(int actions)

This method sets the current actions acceptable to
this

DropTarget

.

**Parameters:**
- actions

- an

int

representing the supported action(s)

---

#### protected int getTargetActions()

This method returns an

int

representing the
current actions this

DropTarget

will accept.

**Returns:**
- the current actions acceptable to this

DropTarget

---

#### public void dropComplete​(boolean success)
throws
InvalidDnDOperationException

This method signals that the drop is completed and
if it was successful or not.

**Parameters:**
- success

- true for success, false if not

**Throws:**
- InvalidDnDOperationException

- if a drop is not outstanding/extant

---

#### protected void acceptDrag​(int dragOperation)

accept the Drag.

**Parameters:**
- dragOperation

- the supported action(s)

---

#### protected void rejectDrag()

reject the Drag.

---

#### protected void acceptDrop​(int dropOperation)

called to signal that the drop is acceptable
using the specified operation.
must be called during DropTargetListener.drop method invocation.

**Parameters:**
- dropOperation

- the supported action(s)

---

#### protected void rejectDrop()

called to signal that the drop is unacceptable.
must be called during DropTargetListener.drop method invocation.

---

#### protected
DataFlavor
[] getCurrentDataFlavors()

get the available DataFlavors of the

Transferable

operand of this operation.

**Returns:**
- a

DataFlavor[]

containing the
supported

DataFlavor

s of the

Transferable

operand.

---

#### protected
List
<
DataFlavor
> getCurrentDataFlavorsAsList()

This method returns a the currently available DataFlavors
of the

Transferable

operand
as a

java.util.List

.

**Returns:**
- the currently available
DataFlavors as a

java.util.List

---

#### protected boolean isDataFlavorSupported​(
DataFlavor
df)

This method returns a

boolean

indicating if the given

DataFlavor

is
supported by this

DropTargetContext

.

**Parameters:**
- df

- the

DataFlavor

**Returns:**
- if the

DataFlavor

specified is supported

---

#### protected
Transferable
getTransferable()
throws
InvalidDnDOperationException

get the Transferable (proxy) operand of this operation

**Returns:**
- the

Transferable

**Throws:**
- InvalidDnDOperationException

- if a drag is not outstanding/extant

---

#### protected
Transferable
createTransferableProxy​(
Transferable
t,
boolean local)

Creates a TransferableProxy to proxy for the specified
Transferable.

**Parameters:**
- t

- the

Transferable

to be proxied
- local

-

true

if

t

represents
the result of a local drag-n-drop operation.

**Returns:**
- the new

TransferableProxy

instance.

---

### Additional Sections

#### Class DropTargetContext

java.lang.Object

- java.awt.dnd.DropTargetContext

java.awt.dnd.DropTargetContext

**All Implemented Interfaces:** Serializable

```java
public class
DropTargetContext

extends
Object

implements
Serializable
```

A

DropTargetContext

is created
whenever the logical cursor associated
with a Drag and Drop operation coincides with the visible geometry of
a

Component

associated with a

DropTarget

.
The

DropTargetContext

provides
the mechanism for a potential receiver
of a drop operation to both provide the end user with the appropriate
drag under feedback, but also to effect the subsequent data transfer
if appropriate.

**Since:** 1.2
**See Also:** Serialized Form

public class

DropTargetContext

extends

Object

implements

Serializable

A

DropTargetContext

is created
whenever the logical cursor associated
with a Drag and Drop operation coincides with the visible geometry of
a

Component

associated with a

DropTarget

.
The

DropTargetContext

provides
the mechanism for a potential receiver
of a drop operation to both provide the end user with the appropriate
drag under feedback, but also to effect the subsequent data transfer
if appropriate.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

DropTargetContext.TransferableProxy

TransferableProxy

is a helper inner class that implements

Transferable

interface and serves as a proxy for another

Transferable

object which represents data transfer for
a particular drag-n-drop operation.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

acceptDrag

​(int dragOperation)

accept the Drag.

protected void

acceptDrop

​(int dropOperation)

called to signal that the drop is acceptable
using the specified operation.

protected

Transferable

createTransferableProxy

​(

Transferable

t,
boolean local)

Creates a TransferableProxy to proxy for the specified
Transferable.

void

dropComplete

​(boolean success)

This method signals that the drop is completed and
if it was successful or not.

Component

getComponent

()

This method returns the

Component

associated with
this

DropTargetContext

.

protected

DataFlavor

[]

getCurrentDataFlavors

()

get the available DataFlavors of the

Transferable

operand of this operation.

protected

List

<

DataFlavor

>

getCurrentDataFlavorsAsList

()

This method returns a the currently available DataFlavors
of the

Transferable

operand
as a

java.util.List

.

DropTarget

getDropTarget

()

This method returns the

DropTarget

associated with this

DropTargetContext

.

protected int

getTargetActions

()

This method returns an

int

representing the
current actions this

DropTarget

will accept.

protected

Transferable

getTransferable

()

get the Transferable (proxy) operand of this operation

protected boolean

isDataFlavorSupported

​(

DataFlavor

df)

This method returns a

boolean

indicating if the given

DataFlavor

is
supported by this

DropTargetContext

.

protected void

rejectDrag

()

reject the Drag.

protected void

rejectDrop

()

called to signal that the drop is unacceptable.

protected void

setTargetActions

​(int actions)

This method sets the current actions acceptable to
this

DropTarget

.

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

protected class

DropTargetContext.TransferableProxy

TransferableProxy

is a helper inner class that implements

Transferable

interface and serves as a proxy for another

Transferable

object which represents data transfer for
a particular drag-n-drop operation.

---

#### Nested Class Summary

TransferableProxy

is a helper inner class that implements

Transferable

interface and serves as a proxy for another

Transferable

object which represents data transfer for
a particular drag-n-drop operation.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

acceptDrag

​(int dragOperation)

accept the Drag.

protected void

acceptDrop

​(int dropOperation)

called to signal that the drop is acceptable
using the specified operation.

protected

Transferable

createTransferableProxy

​(

Transferable

t,
boolean local)

Creates a TransferableProxy to proxy for the specified
Transferable.

void

dropComplete

​(boolean success)

This method signals that the drop is completed and
if it was successful or not.

Component

getComponent

()

This method returns the

Component

associated with
this

DropTargetContext

.

protected

DataFlavor

[]

getCurrentDataFlavors

()

get the available DataFlavors of the

Transferable

operand of this operation.

protected

List

<

DataFlavor

>

getCurrentDataFlavorsAsList

()

This method returns a the currently available DataFlavors
of the

Transferable

operand
as a

java.util.List

.

DropTarget

getDropTarget

()

This method returns the

DropTarget

associated with this

DropTargetContext

.

protected int

getTargetActions

()

This method returns an

int

representing the
current actions this

DropTarget

will accept.

protected

Transferable

getTransferable

()

get the Transferable (proxy) operand of this operation

protected boolean

isDataFlavorSupported

​(

DataFlavor

df)

This method returns a

boolean

indicating if the given

DataFlavor

is
supported by this

DropTargetContext

.

protected void

rejectDrag

()

reject the Drag.

protected void

rejectDrop

()

called to signal that the drop is unacceptable.

protected void

setTargetActions

​(int actions)

This method sets the current actions acceptable to
this

DropTarget

.

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

accept the Drag.

called to signal that the drop is acceptable
using the specified operation.

Creates a TransferableProxy to proxy for the specified
Transferable.

This method signals that the drop is completed and
if it was successful or not.

This method returns the

Component

associated with
this

DropTargetContext

.

get the available DataFlavors of the

Transferable

operand of this operation.

This method returns a the currently available DataFlavors
of the

Transferable

operand
as a

java.util.List

.

This method returns the

DropTarget

associated with this

DropTargetContext

.

This method returns an

int

representing the
current actions this

DropTarget

will accept.

get the Transferable (proxy) operand of this operation

This method returns a

boolean

indicating if the given

DataFlavor

is
supported by this

DropTargetContext

.

reject the Drag.

called to signal that the drop is unacceptable.

This method sets the current actions acceptable to
this

DropTarget

.

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

============ METHOD DETAIL ==========

- Method Detail

- getDropTarget

```java
public
DropTarget
getDropTarget()
```

This method returns the

DropTarget

associated with this

DropTargetContext

.

**Returns:** the

DropTarget

associated with this

DropTargetContext

- getComponent

```java
public
Component
getComponent()
```

This method returns the

Component

associated with
this

DropTargetContext

.

**Returns:** the Component associated with this Context

- setTargetActions

```java
protected void setTargetActions​(int actions)
```

This method sets the current actions acceptable to
this

DropTarget

.

**Parameters:** actions

- an

int

representing the supported action(s)

- getTargetActions

```java
protected int getTargetActions()
```

This method returns an

int

representing the
current actions this

DropTarget

will accept.

**Returns:** the current actions acceptable to this

DropTarget

- dropComplete

```java
public void dropComplete​(boolean success)
throws
InvalidDnDOperationException
```

This method signals that the drop is completed and
if it was successful or not.

**Parameters:** success

- true for success, false if not
**Throws:** InvalidDnDOperationException

- if a drop is not outstanding/extant

- acceptDrag

```java
protected void acceptDrag​(int dragOperation)
```

accept the Drag.

**Parameters:** dragOperation

- the supported action(s)

- rejectDrag

```java
protected void rejectDrag()
```

reject the Drag.

- acceptDrop

```java
protected void acceptDrop​(int dropOperation)
```

called to signal that the drop is acceptable
using the specified operation.
must be called during DropTargetListener.drop method invocation.

**Parameters:** dropOperation

- the supported action(s)

- rejectDrop

```java
protected void rejectDrop()
```

called to signal that the drop is unacceptable.
must be called during DropTargetListener.drop method invocation.

- getCurrentDataFlavors

```java
protected
DataFlavor
[] getCurrentDataFlavors()
```

get the available DataFlavors of the

Transferable

operand of this operation.

**Returns:** a

DataFlavor[]

containing the
supported

DataFlavor

s of the

Transferable

operand.

- getCurrentDataFlavorsAsList

```java
protected
List
<
DataFlavor
> getCurrentDataFlavorsAsList()
```

This method returns a the currently available DataFlavors
of the

Transferable

operand
as a

java.util.List

.

**Returns:** the currently available
DataFlavors as a

java.util.List

- isDataFlavorSupported

```java
protected boolean isDataFlavorSupported​(
DataFlavor
df)
```

This method returns a

boolean

indicating if the given

DataFlavor

is
supported by this

DropTargetContext

.

**Parameters:** df

- the

DataFlavor
**Returns:** if the

DataFlavor

specified is supported

- getTransferable

```java
protected
Transferable
getTransferable()
throws
InvalidDnDOperationException
```

get the Transferable (proxy) operand of this operation

**Returns:** the

Transferable
**Throws:** InvalidDnDOperationException

- if a drag is not outstanding/extant

- createTransferableProxy

```java
protected
Transferable
createTransferableProxy​(
Transferable
t,
boolean local)
```

Creates a TransferableProxy to proxy for the specified
Transferable.

**Parameters:** t

- the

Transferable

to be proxied
**Parameters:** local

-

true

if

t

represents
the result of a local drag-n-drop operation.
**Returns:** the new

TransferableProxy

instance.

Method Detail

- getDropTarget

```java
public
DropTarget
getDropTarget()
```

This method returns the

DropTarget

associated with this

DropTargetContext

.

**Returns:** the

DropTarget

associated with this

DropTargetContext

- getComponent

```java
public
Component
getComponent()
```

This method returns the

Component

associated with
this

DropTargetContext

.

**Returns:** the Component associated with this Context

- setTargetActions

```java
protected void setTargetActions​(int actions)
```

This method sets the current actions acceptable to
this

DropTarget

.

**Parameters:** actions

- an

int

representing the supported action(s)

- getTargetActions

```java
protected int getTargetActions()
```

This method returns an

int

representing the
current actions this

DropTarget

will accept.

**Returns:** the current actions acceptable to this

DropTarget

- dropComplete

```java
public void dropComplete​(boolean success)
throws
InvalidDnDOperationException
```

This method signals that the drop is completed and
if it was successful or not.

**Parameters:** success

- true for success, false if not
**Throws:** InvalidDnDOperationException

- if a drop is not outstanding/extant

- acceptDrag

```java
protected void acceptDrag​(int dragOperation)
```

accept the Drag.

**Parameters:** dragOperation

- the supported action(s)

- rejectDrag

```java
protected void rejectDrag()
```

reject the Drag.

- acceptDrop

```java
protected void acceptDrop​(int dropOperation)
```

called to signal that the drop is acceptable
using the specified operation.
must be called during DropTargetListener.drop method invocation.

**Parameters:** dropOperation

- the supported action(s)

- rejectDrop

```java
protected void rejectDrop()
```

called to signal that the drop is unacceptable.
must be called during DropTargetListener.drop method invocation.

- getCurrentDataFlavors

```java
protected
DataFlavor
[] getCurrentDataFlavors()
```

get the available DataFlavors of the

Transferable

operand of this operation.

**Returns:** a

DataFlavor[]

containing the
supported

DataFlavor

s of the

Transferable

operand.

- getCurrentDataFlavorsAsList

```java
protected
List
<
DataFlavor
> getCurrentDataFlavorsAsList()
```

This method returns a the currently available DataFlavors
of the

Transferable

operand
as a

java.util.List

.

**Returns:** the currently available
DataFlavors as a

java.util.List

- isDataFlavorSupported

```java
protected boolean isDataFlavorSupported​(
DataFlavor
df)
```

This method returns a

boolean

indicating if the given

DataFlavor

is
supported by this

DropTargetContext

.

**Parameters:** df

- the

DataFlavor
**Returns:** if the

DataFlavor

specified is supported

- getTransferable

```java
protected
Transferable
getTransferable()
throws
InvalidDnDOperationException
```

get the Transferable (proxy) operand of this operation

**Returns:** the

Transferable
**Throws:** InvalidDnDOperationException

- if a drag is not outstanding/extant

- createTransferableProxy

```java
protected
Transferable
createTransferableProxy​(
Transferable
t,
boolean local)
```

Creates a TransferableProxy to proxy for the specified
Transferable.

**Parameters:** t

- the

Transferable

to be proxied
**Parameters:** local

-

true

if

t

represents
the result of a local drag-n-drop operation.
**Returns:** the new

TransferableProxy

instance.

---

#### Method Detail

getDropTarget

```java
public
DropTarget
getDropTarget()
```

This method returns the

DropTarget

associated with this

DropTargetContext

.

**Returns:** the

DropTarget

associated with this

DropTargetContext

---

#### getDropTarget

public

DropTarget

getDropTarget()

This method returns the

DropTarget

associated with this

DropTargetContext

.

getComponent

```java
public
Component
getComponent()
```

This method returns the

Component

associated with
this

DropTargetContext

.

**Returns:** the Component associated with this Context

---

#### getComponent

public

Component

getComponent()

This method returns the

Component

associated with
this

DropTargetContext

.

setTargetActions

```java
protected void setTargetActions​(int actions)
```

This method sets the current actions acceptable to
this

DropTarget

.

**Parameters:** actions

- an

int

representing the supported action(s)

---

#### setTargetActions

protected void setTargetActions​(int actions)

This method sets the current actions acceptable to
this

DropTarget

.

getTargetActions

```java
protected int getTargetActions()
```

This method returns an

int

representing the
current actions this

DropTarget

will accept.

**Returns:** the current actions acceptable to this

DropTarget

---

#### getTargetActions

protected int getTargetActions()

This method returns an

int

representing the
current actions this

DropTarget

will accept.

dropComplete

```java
public void dropComplete​(boolean success)
throws
InvalidDnDOperationException
```

This method signals that the drop is completed and
if it was successful or not.

**Parameters:** success

- true for success, false if not
**Throws:** InvalidDnDOperationException

- if a drop is not outstanding/extant

---

#### dropComplete

public void dropComplete​(boolean success)
throws

InvalidDnDOperationException

This method signals that the drop is completed and
if it was successful or not.

acceptDrag

```java
protected void acceptDrag​(int dragOperation)
```

accept the Drag.

**Parameters:** dragOperation

- the supported action(s)

---

#### acceptDrag

protected void acceptDrag​(int dragOperation)

accept the Drag.

rejectDrag

```java
protected void rejectDrag()
```

reject the Drag.

---

#### rejectDrag

protected void rejectDrag()

reject the Drag.

acceptDrop

```java
protected void acceptDrop​(int dropOperation)
```

called to signal that the drop is acceptable
using the specified operation.
must be called during DropTargetListener.drop method invocation.

**Parameters:** dropOperation

- the supported action(s)

---

#### acceptDrop

protected void acceptDrop​(int dropOperation)

called to signal that the drop is acceptable
using the specified operation.
must be called during DropTargetListener.drop method invocation.

rejectDrop

```java
protected void rejectDrop()
```

called to signal that the drop is unacceptable.
must be called during DropTargetListener.drop method invocation.

---

#### rejectDrop

protected void rejectDrop()

called to signal that the drop is unacceptable.
must be called during DropTargetListener.drop method invocation.

getCurrentDataFlavors

```java
protected
DataFlavor
[] getCurrentDataFlavors()
```

get the available DataFlavors of the

Transferable

operand of this operation.

**Returns:** a

DataFlavor[]

containing the
supported

DataFlavor

s of the

Transferable

operand.

---

#### getCurrentDataFlavors

protected

DataFlavor

[] getCurrentDataFlavors()

get the available DataFlavors of the

Transferable

operand of this operation.

getCurrentDataFlavorsAsList

```java
protected
List
<
DataFlavor
> getCurrentDataFlavorsAsList()
```

This method returns a the currently available DataFlavors
of the

Transferable

operand
as a

java.util.List

.

**Returns:** the currently available
DataFlavors as a

java.util.List

---

#### getCurrentDataFlavorsAsList

protected

List

<

DataFlavor

> getCurrentDataFlavorsAsList()

This method returns a the currently available DataFlavors
of the

Transferable

operand
as a

java.util.List

.

isDataFlavorSupported

```java
protected boolean isDataFlavorSupported​(
DataFlavor
df)
```

This method returns a

boolean

indicating if the given

DataFlavor

is
supported by this

DropTargetContext

.

**Parameters:** df

- the

DataFlavor
**Returns:** if the

DataFlavor

specified is supported

---

#### isDataFlavorSupported

protected boolean isDataFlavorSupported​(

DataFlavor

df)

This method returns a

boolean

indicating if the given

DataFlavor

is
supported by this

DropTargetContext

.

getTransferable

```java
protected
Transferable
getTransferable()
throws
InvalidDnDOperationException
```

get the Transferable (proxy) operand of this operation

**Returns:** the

Transferable
**Throws:** InvalidDnDOperationException

- if a drag is not outstanding/extant

---

#### getTransferable

protected

Transferable

getTransferable()
throws

InvalidDnDOperationException

get the Transferable (proxy) operand of this operation

createTransferableProxy

```java
protected
Transferable
createTransferableProxy​(
Transferable
t,
boolean local)
```

Creates a TransferableProxy to proxy for the specified
Transferable.

**Parameters:** t

- the

Transferable

to be proxied
**Parameters:** local

-

true

if

t

represents
the result of a local drag-n-drop operation.
**Returns:** the new

TransferableProxy

instance.

---

#### createTransferableProxy

protected

Transferable

createTransferableProxy​(

Transferable

t,
boolean local)

Creates a TransferableProxy to proxy for the specified
Transferable.

---

