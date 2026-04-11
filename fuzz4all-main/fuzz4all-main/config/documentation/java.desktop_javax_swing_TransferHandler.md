# Class TransferHandler

**Source:** `java.desktop\javax\swing\TransferHandler.html`

### Class Description

```java
public class
TransferHandler

extends
Object

implements
Serializable
```

This class is used to handle the transfer of a

Transferable

to and from Swing components. The

Transferable

is used to
represent data that is exchanged via a cut, copy, or paste
to/from a clipboard. It is also used in drag-and-drop operations
to represent a drag from a component, and a drop to a component.
Swing provides functionality that automatically supports cut, copy,
and paste keyboard bindings that use the functionality provided by
an implementation of this class. Swing also provides functionality
that automatically supports drag and drop that uses the functionality
provided by an implementation of this class. The Swing developer can
concentrate on specifying the semantics of a transfer primarily by setting
the

transferHandler

property on a Swing component.

This class is implemented to provide a default behavior of transferring
a component property simply by specifying the name of the property in
the constructor. For example, to transfer the foreground color from
one component to another either via the clipboard or a drag and drop operation
a

TransferHandler

can be constructed with the string "foreground". The
built in support will use the color returned by

getForeground

as the source
of the transfer, and

setForeground

for the target of a transfer.

Please see

How to Use Drag and Drop and Data Transfer

,
a section in

The Java Tutorial

, for more information.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public static final int NONE

An

int

representing no transfer action.

**See Also:**
- Constant Field Values

---

#### public static final int COPY

An

int

representing a "copy" transfer action.
This value is used when data is copied to a clipboard
or copied elsewhere in a drag and drop operation.

**See Also:**
- Constant Field Values

---

#### public static final int MOVE

An

int

representing a "move" transfer action.
This value is used when data is moved to a clipboard (i.e. a cut)
or moved elsewhere in a drag and drop operation.

**See Also:**
- Constant Field Values

---

#### public static final int COPY_OR_MOVE

An

int

representing a source action capability of either
"copy" or "move".

**See Also:**
- Constant Field Values

---

#### public static final int LINK

An

int

representing a "link" transfer action.
This value is used to specify that data should be linked in a drag
and drop operation.

**See Also:**
- DnDConstants.ACTION_LINK

,

Constant Field Values

**Since:**
- 1.6

---

### Constructor Details

#### public TransferHandler​(
String
property)

Constructs a transfer handler that can transfer a Java Bean property
from one component to another via the clipboard or a drag and drop
operation.

**Parameters:**
- property

- the name of the property to transfer; this can
be

null

if there is no property associated with the transfer
handler (a subclass that performs some other kind of transfer, for example)

---

#### protected TransferHandler()

Convenience constructor for subclasses.

---

### Method Details

#### public static
Action
getCutAction()

Returns an

Action

that performs cut operations to the
clipboard. When performed, this action operates on the

JComponent

source of the

ActionEvent

by invoking

exportToClipboard

,
with a

MOVE

action, on the component's

TransferHandler

.

**Returns:**
- an

Action

for performing cuts to the clipboard

---

#### public static
Action
getCopyAction()

Returns an

Action

that performs copy operations to the
clipboard. When performed, this action operates on the

JComponent

source of the

ActionEvent

by invoking

exportToClipboard

,
with a

COPY

action, on the component's

TransferHandler

.

**Returns:**
- an

Action

for performing copies to the clipboard

---

#### public static
Action
getPasteAction()

Returns an

Action

that performs paste operations from the
clipboard. When performed, this action operates on the

JComponent

source of the

ActionEvent

by invoking

importData

,
with the clipboard contents, on the component's

TransferHandler

.

**Returns:**
- an

Action

for performing pastes from the clipboard

---

#### public void setDragImage​(
Image
img)

Sets the drag image parameter. The image has to be prepared
for rendering by the moment of the call. The image is stored
by reference because of some performance reasons.

**Parameters:**
- img

- an image to drag

---

#### public
Image
getDragImage()

Returns the drag image. If there is no image to drag,
the returned value is

null

.

**Returns:**
- the reference to the drag image

---

#### public void setDragImageOffset​(
Point
p)

Sets an anchor offset for the image to drag.
It can not be

null

.

**Parameters:**
- p

- a

Point

object that corresponds
to coordinates of an anchor offset of the image
relative to the upper left corner of the image

---

#### public
Point
getDragImageOffset()

Returns an anchor offset for the image to drag.

**Returns:**
- a

Point

object that corresponds
to coordinates of an anchor offset of the image
relative to the upper left corner of the image.
The point

(0,0)

returns by default.

---

#### public void exportAsDrag​(
JComponent
comp,

InputEvent
e,
int action)

Causes the Swing drag support to be initiated. This is called by
the various UI implementations in the

javax.swing.plaf.basic

package if the dragEnabled property is set on the component.
This can be called by custom UI
implementations to use the Swing drag support. This method can also be called
by a Swing extension written as a subclass of

JComponent

to take advantage of the Swing drag support.

The transfer

will not necessarily

have been completed at the
return of this call (i.e. the call does not block waiting for the drop).
The transfer will take place through the Swing implementation of the

java.awt.dnd

mechanism, requiring no further effort
from the developer. The

exportDone

method will be called
when the transfer has completed.

**Parameters:**
- comp

- the component holding the data to be transferred;
provided to enable sharing of

TransferHandler

s
- e

- the event that triggered the transfer
- action

- the transfer action initially requested;
either

COPY

,

MOVE

or

LINK

;
the DnD system may change the action used during the
course of the drag operation

---

#### public void exportToClipboard​(
JComponent
comp,

Clipboard
clip,
int action)
throws
IllegalStateException

Causes a transfer from the given component to the
given clipboard. This method is called by the default cut and
copy actions registered in a component's action map.

The transfer will take place using the

java.awt.datatransfer

mechanism, requiring no further effort from the developer. Any data
transfer

will

be complete and the

exportDone

method will be called with the action that occurred, before this method
returns. Should the clipboard be unavailable when attempting to place
data on it, the

IllegalStateException

thrown by

Clipboard.setContents(Transferable, ClipboardOwner)

will
be propagated through this method. However,

exportDone

will first be called with an action
of

NONE

for consistency.

**Parameters:**
- comp

- the component holding the data to be transferred;
provided to enable sharing of

TransferHandler

s
- clip

- the clipboard to transfer the data into
- action

- the transfer action requested; this should
be a value of either

COPY

or

MOVE

;
the operation performed is the intersection of the transfer
capabilities given by getSourceActions and the requested action;
the intersection may result in an action of

NONE

if the requested action isn't supported

**Throws:**
- IllegalStateException

- if the clipboard is currently unavailable

**See Also:**
- Clipboard.setContents(Transferable, ClipboardOwner)

---

#### public boolean importData​(
TransferHandler.TransferSupport
support)

Causes a transfer to occur from a clipboard or a drag and
drop operation. The

Transferable

to be
imported and the component to transfer to are contained
within the

TransferSupport

.

While the drag and drop implementation calls

canImport

to determine the suitability of a transfer before calling this
method, the implementation of paste does not. As such, it cannot
be assumed that the transfer is acceptable upon a call to
this method for paste. It is recommended that

canImport

be
explicitly called to cover this case.

Note: The

TransferSupport

object passed to this method
is only valid for the duration of the method call. It is undefined
what values it may contain after this method returns.

**Parameters:**
- support

- the object containing the details of
the transfer, not

null

.

**Returns:**
- true if the data was inserted into the component,
false otherwise

**Throws:**
- NullPointerException

- if

support

is

null

**See Also:**
- canImport(TransferHandler.TransferSupport)

**Since:**
- 1.6

---

#### public boolean importData​(
JComponent
comp,

Transferable
t)

Causes a transfer to a component from a clipboard or a
DND drop operation. The

Transferable

represents
the data to be imported into the component.

Note: Swing now calls the newer version of

importData

that takes a

TransferSupport

, which in turn calls this
method (if the component in the

TransferSupport

is a

JComponent

). Developers are encouraged to call and override the
newer version as it provides more information (and is the only
version that supports use with a

TransferHandler

set directly
on a

JFrame

or other non-

JComponent

).

**Parameters:**
- comp

- the component to receive the transfer;
provided to enable sharing of

TransferHandler

s
- t

- the data to import

**Returns:**
- true if the data was inserted into the component, false otherwise

**See Also:**
- importData(TransferHandler.TransferSupport)

---

#### public boolean canImport​(
TransferHandler.TransferSupport
support)

This method is called repeatedly during a drag and drop operation
to allow the developer to configure properties of, and to return
the acceptability of transfers; with a return value of

true

indicating that the transfer represented by the given

TransferSupport

(which contains all of the details of the
transfer) is acceptable at the current time, and a value of

false

rejecting the transfer.

For those components that automatically display a drop location during
drag and drop, accepting the transfer, by default, tells them to show
the drop location. This can be changed by calling

setShowDropLocation

on the

TransferSupport

.

By default, when the transfer is accepted, the chosen drop action is that
picked by the user via their drag gesture. The developer can override
this and choose a different action, from the supported source
actions, by calling

setDropAction

on the

TransferSupport

.

On every call to

canImport

, the

TransferSupport

contains
fresh state. As such, any properties set on it must be set on every
call. Upon a drop,

canImport

is called one final time before
calling into

importData

. Any state set on the

TransferSupport

during that last call will be available in

importData

.

This method is not called internally in response to paste operations.
As such, it is recommended that implementations of

importData

explicitly call this method for such cases and that this method
be prepared to return the suitability of paste operations as well.

Note: The

TransferSupport

object passed to this method
is only valid for the duration of the method call. It is undefined
what values it may contain after this method returns.

**Parameters:**
- support

- the object containing the details of
the transfer, not

null

.

**Returns:**
- true

if the import can happen,

false

otherwise

**Throws:**
- NullPointerException

- if

support

is

null

**See Also:**
- importData(TransferHandler.TransferSupport)

,

TransferHandler.TransferSupport.setShowDropLocation(boolean)

,

TransferHandler.TransferSupport.setDropAction(int)

**Since:**
- 1.6

---

#### public boolean canImport​(
JComponent
comp,

DataFlavor
[] transferFlavors)

Indicates whether a component will accept an import of the given
set of data flavors prior to actually attempting to import it.

Note: Swing now calls the newer version of

canImport

that takes a

TransferSupport

, which in turn calls this
method (only if the component in the

TransferSupport

is a

JComponent

). Developers are encouraged to call and override the
newer version as it provides more information (and is the only
version that supports use with a

TransferHandler

set directly
on a

JFrame

or other non-

JComponent

).

**Parameters:**
- comp

- the component to receive the transfer;
provided to enable sharing of

TransferHandler

s
- transferFlavors

- the data formats available

**Returns:**
- true if the data can be inserted into the component, false otherwise

**See Also:**
- canImport(TransferHandler.TransferSupport)

---

#### public int getSourceActions​(
JComponent
c)

Returns the type of transfer actions supported by the source;
any bitwise-OR combination of

COPY

,

MOVE

and

LINK

.

Some models are not mutable, so a transfer operation of

MOVE

should not be advertised in that case. Returning

NONE

disables transfers from the component.

**Parameters:**
- c

- the component holding the data to be transferred;
provided to enable sharing of

TransferHandler

s

**Returns:**
- COPY

if the transfer property can be found,
otherwise returns

NONE

---

#### public
Icon
getVisualRepresentation​(
Transferable
t)

Returns an object that establishes the look of a transfer. This is
useful for both providing feedback while performing a drag operation and for
representing the transfer in a clipboard implementation that has a visual
appearance. The implementation of the

Icon

interface should
not alter the graphics clip or alpha level.
The icon implementation need not be rectangular or paint all of the
bounding rectangle and logic that calls the icons paint method should
not assume the all bits are painted.

null

is a valid return value
for this method and indicates there is no visual representation provided.
In that case, the calling logic is free to represent the
transferable however it wants.

The default Swing logic will not do an alpha blended drag animation if
the return is

null

.

**Parameters:**
- t

- the data to be transferred; this value is expected to have been
created by the

createTransferable

method

**Returns:**
- null

, indicating
there is no default visual representation

---

#### protected
Transferable
createTransferable​(
JComponent
c)

Creates a

Transferable

to use as the source for
a data transfer. Returns the representation of the data to
be transferred, or

null

if the component's
property is

null

**Parameters:**
- c

- the component holding the data to be transferred;
provided to enable sharing of

TransferHandler

s

**Returns:**
- the representation of the data to be transferred, or

null

if the property associated with

c

is

null

---

#### protected void exportDone​(
JComponent
source,

Transferable
data,
int action)

Invoked after data has been exported. This method should remove
the data that was transferred if the action was

MOVE

.

This method is implemented to do nothing since

MOVE

is not a supported action of this implementation
(

getSourceActions

does not include

MOVE

).

**Parameters:**
- source

- the component that was the source of the data
- data

- The data that was transferred or possibly null
if the action is

NONE

.
- action

- the actual action that was performed

---

### Additional Sections

#### Class TransferHandler

java.lang.Object

- javax.swing.TransferHandler

javax.swing.TransferHandler

**All Implemented Interfaces:** Serializable

```java
public class
TransferHandler

extends
Object

implements
Serializable
```

This class is used to handle the transfer of a

Transferable

to and from Swing components. The

Transferable

is used to
represent data that is exchanged via a cut, copy, or paste
to/from a clipboard. It is also used in drag-and-drop operations
to represent a drag from a component, and a drop to a component.
Swing provides functionality that automatically supports cut, copy,
and paste keyboard bindings that use the functionality provided by
an implementation of this class. Swing also provides functionality
that automatically supports drag and drop that uses the functionality
provided by an implementation of this class. The Swing developer can
concentrate on specifying the semantics of a transfer primarily by setting
the

transferHandler

property on a Swing component.

This class is implemented to provide a default behavior of transferring
a component property simply by specifying the name of the property in
the constructor. For example, to transfer the foreground color from
one component to another either via the clipboard or a drag and drop operation
a

TransferHandler

can be constructed with the string "foreground". The
built in support will use the color returned by

getForeground

as the source
of the transfer, and

setForeground

for the target of a transfer.

Please see

How to Use Drag and Drop and Data Transfer

,
a section in

The Java Tutorial

, for more information.

**Since:** 1.4
**See Also:** Serialized Form

public class

TransferHandler

extends

Object

implements

Serializable

This class is used to handle the transfer of a

Transferable

to and from Swing components. The

Transferable

is used to
represent data that is exchanged via a cut, copy, or paste
to/from a clipboard. It is also used in drag-and-drop operations
to represent a drag from a component, and a drop to a component.
Swing provides functionality that automatically supports cut, copy,
and paste keyboard bindings that use the functionality provided by
an implementation of this class. Swing also provides functionality
that automatically supports drag and drop that uses the functionality
provided by an implementation of this class. The Swing developer can
concentrate on specifying the semantics of a transfer primarily by setting
the

transferHandler

property on a Swing component.

This class is implemented to provide a default behavior of transferring
a component property simply by specifying the name of the property in
the constructor. For example, to transfer the foreground color from
one component to another either via the clipboard or a drag and drop operation
a

TransferHandler

can be constructed with the string "foreground". The
built in support will use the color returned by

getForeground

as the source
of the transfer, and

setForeground

for the target of a transfer.

Please see

How to Use Drag and Drop and Data Transfer

,
a section in

The Java Tutorial

, for more information.

This class is implemented to provide a default behavior of transferring
a component property simply by specifying the name of the property in
the constructor. For example, to transfer the foreground color from
one component to another either via the clipboard or a drag and drop operation
a

TransferHandler

can be constructed with the string "foreground". The
built in support will use the color returned by

getForeground

as the source
of the transfer, and

setForeground

for the target of a transfer.

Please see

How to Use Drag and Drop and Data Transfer

,
a section in

The Java Tutorial

, for more information.

Please see

How to Use Drag and Drop and Data Transfer

,
a section in

The Java Tutorial

, for more information.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

TransferHandler.DropLocation

Represents a location where dropped data should be inserted.

static class

TransferHandler.TransferSupport

This class encapsulates all relevant details of a clipboard
or drag and drop transfer, and also allows for customizing
aspects of the drag and drop experience.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

COPY

An

int

representing a "copy" transfer action.

static int

COPY_OR_MOVE

An

int

representing a source action capability of either
"copy" or "move".

static int

LINK

An

int

representing a "link" transfer action.

static int

MOVE

An

int

representing a "move" transfer action.

static int

NONE

An

int

representing no transfer action.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

TransferHandler

()

Convenience constructor for subclasses.

TransferHandler

​(

String

property)

Constructs a transfer handler that can transfer a Java Bean property
from one component to another via the clipboard or a drag and drop
operation.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

canImport

​(

JComponent

comp,

DataFlavor

[] transferFlavors)

Indicates whether a component will accept an import of the given
set of data flavors prior to actually attempting to import it.

boolean

canImport

​(

TransferHandler.TransferSupport

support)

This method is called repeatedly during a drag and drop operation
to allow the developer to configure properties of, and to return
the acceptability of transfers; with a return value of

true

indicating that the transfer represented by the given

TransferSupport

(which contains all of the details of the
transfer) is acceptable at the current time, and a value of

false

rejecting the transfer.

protected

Transferable

createTransferable

​(

JComponent

c)

Creates a

Transferable

to use as the source for
a data transfer.

void

exportAsDrag

​(

JComponent

comp,

InputEvent

e,
int action)

Causes the Swing drag support to be initiated.

protected void

exportDone

​(

JComponent

source,

Transferable

data,
int action)

Invoked after data has been exported.

void

exportToClipboard

​(

JComponent

comp,

Clipboard

clip,
int action)

Causes a transfer from the given component to the
given clipboard.

static

Action

getCopyAction

()

Returns an

Action

that performs copy operations to the
clipboard.

static

Action

getCutAction

()

Returns an

Action

that performs cut operations to the
clipboard.

Image

getDragImage

()

Returns the drag image.

Point

getDragImageOffset

()

Returns an anchor offset for the image to drag.

static

Action

getPasteAction

()

Returns an

Action

that performs paste operations from the
clipboard.

int

getSourceActions

​(

JComponent

c)

Returns the type of transfer actions supported by the source;
any bitwise-OR combination of

COPY

,

MOVE

and

LINK

.

Icon

getVisualRepresentation

​(

Transferable

t)

Returns an object that establishes the look of a transfer.

boolean

importData

​(

JComponent

comp,

Transferable

t)

Causes a transfer to a component from a clipboard or a
DND drop operation.

boolean

importData

​(

TransferHandler.TransferSupport

support)

Causes a transfer to occur from a clipboard or a drag and
drop operation.

void

setDragImage

​(

Image

img)

Sets the drag image parameter.

void

setDragImageOffset

​(

Point

p)

Sets an anchor offset for the image to drag.

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

static class

TransferHandler.DropLocation

Represents a location where dropped data should be inserted.

static class

TransferHandler.TransferSupport

This class encapsulates all relevant details of a clipboard
or drag and drop transfer, and also allows for customizing
aspects of the drag and drop experience.

---

#### Nested Class Summary

Represents a location where dropped data should be inserted.

This class encapsulates all relevant details of a clipboard
or drag and drop transfer, and also allows for customizing
aspects of the drag and drop experience.

Field Summary

Fields

Modifier and Type

Field

Description

static int

COPY

An

int

representing a "copy" transfer action.

static int

COPY_OR_MOVE

An

int

representing a source action capability of either
"copy" or "move".

static int

LINK

An

int

representing a "link" transfer action.

static int

MOVE

An

int

representing a "move" transfer action.

static int

NONE

An

int

representing no transfer action.

---

#### Field Summary

An

int

representing a "copy" transfer action.

An

int

representing a source action capability of either
"copy" or "move".

An

int

representing a "link" transfer action.

An

int

representing a "move" transfer action.

An

int

representing no transfer action.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

TransferHandler

()

Convenience constructor for subclasses.

TransferHandler

​(

String

property)

Constructs a transfer handler that can transfer a Java Bean property
from one component to another via the clipboard or a drag and drop
operation.

---

#### Constructor Summary

Convenience constructor for subclasses.

Constructs a transfer handler that can transfer a Java Bean property
from one component to another via the clipboard or a drag and drop
operation.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

canImport

​(

JComponent

comp,

DataFlavor

[] transferFlavors)

Indicates whether a component will accept an import of the given
set of data flavors prior to actually attempting to import it.

boolean

canImport

​(

TransferHandler.TransferSupport

support)

This method is called repeatedly during a drag and drop operation
to allow the developer to configure properties of, and to return
the acceptability of transfers; with a return value of

true

indicating that the transfer represented by the given

TransferSupport

(which contains all of the details of the
transfer) is acceptable at the current time, and a value of

false

rejecting the transfer.

protected

Transferable

createTransferable

​(

JComponent

c)

Creates a

Transferable

to use as the source for
a data transfer.

void

exportAsDrag

​(

JComponent

comp,

InputEvent

e,
int action)

Causes the Swing drag support to be initiated.

protected void

exportDone

​(

JComponent

source,

Transferable

data,
int action)

Invoked after data has been exported.

void

exportToClipboard

​(

JComponent

comp,

Clipboard

clip,
int action)

Causes a transfer from the given component to the
given clipboard.

static

Action

getCopyAction

()

Returns an

Action

that performs copy operations to the
clipboard.

static

Action

getCutAction

()

Returns an

Action

that performs cut operations to the
clipboard.

Image

getDragImage

()

Returns the drag image.

Point

getDragImageOffset

()

Returns an anchor offset for the image to drag.

static

Action

getPasteAction

()

Returns an

Action

that performs paste operations from the
clipboard.

int

getSourceActions

​(

JComponent

c)

Returns the type of transfer actions supported by the source;
any bitwise-OR combination of

COPY

,

MOVE

and

LINK

.

Icon

getVisualRepresentation

​(

Transferable

t)

Returns an object that establishes the look of a transfer.

boolean

importData

​(

JComponent

comp,

Transferable

t)

Causes a transfer to a component from a clipboard or a
DND drop operation.

boolean

importData

​(

TransferHandler.TransferSupport

support)

Causes a transfer to occur from a clipboard or a drag and
drop operation.

void

setDragImage

​(

Image

img)

Sets the drag image parameter.

void

setDragImageOffset

​(

Point

p)

Sets an anchor offset for the image to drag.

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

Indicates whether a component will accept an import of the given
set of data flavors prior to actually attempting to import it.

This method is called repeatedly during a drag and drop operation
to allow the developer to configure properties of, and to return
the acceptability of transfers; with a return value of

true

indicating that the transfer represented by the given

TransferSupport

(which contains all of the details of the
transfer) is acceptable at the current time, and a value of

false

rejecting the transfer.

Creates a

Transferable

to use as the source for
a data transfer.

Causes the Swing drag support to be initiated.

Invoked after data has been exported.

Causes a transfer from the given component to the
given clipboard.

Returns an

Action

that performs copy operations to the
clipboard.

Returns an

Action

that performs cut operations to the
clipboard.

Returns the drag image.

Returns an anchor offset for the image to drag.

Returns an

Action

that performs paste operations from the
clipboard.

Returns the type of transfer actions supported by the source;
any bitwise-OR combination of

COPY

,

MOVE

and

LINK

.

Returns an object that establishes the look of a transfer.

Causes a transfer to a component from a clipboard or a
DND drop operation.

Causes a transfer to occur from a clipboard or a drag and
drop operation.

Sets the drag image parameter.

Sets an anchor offset for the image to drag.

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

- NONE

```java
public static final int NONE
```

An

int

representing no transfer action.

**See Also:** Constant Field Values

- COPY

```java
public static final int COPY
```

An

int

representing a "copy" transfer action.
This value is used when data is copied to a clipboard
or copied elsewhere in a drag and drop operation.

**See Also:** Constant Field Values

- MOVE

```java
public static final int MOVE
```

An

int

representing a "move" transfer action.
This value is used when data is moved to a clipboard (i.e. a cut)
or moved elsewhere in a drag and drop operation.

**See Also:** Constant Field Values

- COPY_OR_MOVE

```java
public static final int COPY_OR_MOVE
```

An

int

representing a source action capability of either
"copy" or "move".

**See Also:** Constant Field Values

- LINK

```java
public static final int LINK
```

An

int

representing a "link" transfer action.
This value is used to specify that data should be linked in a drag
and drop operation.

**Since:** 1.6
**See Also:** DnDConstants.ACTION_LINK

,

Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- TransferHandler

```java
public TransferHandler​(
String
property)
```

Constructs a transfer handler that can transfer a Java Bean property
from one component to another via the clipboard or a drag and drop
operation.

**Parameters:** property

- the name of the property to transfer; this can
be

null

if there is no property associated with the transfer
handler (a subclass that performs some other kind of transfer, for example)

- TransferHandler

```java
protected TransferHandler()
```

Convenience constructor for subclasses.

============ METHOD DETAIL ==========

- Method Detail

- getCutAction

```java
public static
Action
getCutAction()
```

Returns an

Action

that performs cut operations to the
clipboard. When performed, this action operates on the

JComponent

source of the

ActionEvent

by invoking

exportToClipboard

,
with a

MOVE

action, on the component's

TransferHandler

.

**Returns:** an

Action

for performing cuts to the clipboard

- getCopyAction

```java
public static
Action
getCopyAction()
```

Returns an

Action

that performs copy operations to the
clipboard. When performed, this action operates on the

JComponent

source of the

ActionEvent

by invoking

exportToClipboard

,
with a

COPY

action, on the component's

TransferHandler

.

**Returns:** an

Action

for performing copies to the clipboard

- getPasteAction

```java
public static
Action
getPasteAction()
```

Returns an

Action

that performs paste operations from the
clipboard. When performed, this action operates on the

JComponent

source of the

ActionEvent

by invoking

importData

,
with the clipboard contents, on the component's

TransferHandler

.

**Returns:** an

Action

for performing pastes from the clipboard

- setDragImage

```java
public void setDragImage​(
Image
img)
```

Sets the drag image parameter. The image has to be prepared
for rendering by the moment of the call. The image is stored
by reference because of some performance reasons.

**Parameters:** img

- an image to drag

- getDragImage

```java
public
Image
getDragImage()
```

Returns the drag image. If there is no image to drag,
the returned value is

null

.

**Returns:** the reference to the drag image

- setDragImageOffset

```java
public void setDragImageOffset​(
Point
p)
```

Sets an anchor offset for the image to drag.
It can not be

null

.

**Parameters:** p

- a

Point

object that corresponds
to coordinates of an anchor offset of the image
relative to the upper left corner of the image

- getDragImageOffset

```java
public
Point
getDragImageOffset()
```

Returns an anchor offset for the image to drag.

**Returns:** a

Point

object that corresponds
to coordinates of an anchor offset of the image
relative to the upper left corner of the image.
The point

(0,0)

returns by default.

- exportAsDrag

```java
public void exportAsDrag​(
JComponent
comp,

InputEvent
e,
int action)
```

Causes the Swing drag support to be initiated. This is called by
the various UI implementations in the

javax.swing.plaf.basic

package if the dragEnabled property is set on the component.
This can be called by custom UI
implementations to use the Swing drag support. This method can also be called
by a Swing extension written as a subclass of

JComponent

to take advantage of the Swing drag support.

The transfer

will not necessarily

have been completed at the
return of this call (i.e. the call does not block waiting for the drop).
The transfer will take place through the Swing implementation of the

java.awt.dnd

mechanism, requiring no further effort
from the developer. The

exportDone

method will be called
when the transfer has completed.

**Parameters:** comp

- the component holding the data to be transferred;
provided to enable sharing of

TransferHandler

s
**Parameters:** e

- the event that triggered the transfer
**Parameters:** action

- the transfer action initially requested;
either

COPY

,

MOVE

or

LINK

;
the DnD system may change the action used during the
course of the drag operation

- exportToClipboard

```java
public void exportToClipboard​(
JComponent
comp,

Clipboard
clip,
int action)
throws
IllegalStateException
```

Causes a transfer from the given component to the
given clipboard. This method is called by the default cut and
copy actions registered in a component's action map.

The transfer will take place using the

java.awt.datatransfer

mechanism, requiring no further effort from the developer. Any data
transfer

will

be complete and the

exportDone

method will be called with the action that occurred, before this method
returns. Should the clipboard be unavailable when attempting to place
data on it, the

IllegalStateException

thrown by

Clipboard.setContents(Transferable, ClipboardOwner)

will
be propagated through this method. However,

exportDone

will first be called with an action
of

NONE

for consistency.

**Parameters:** comp

- the component holding the data to be transferred;
provided to enable sharing of

TransferHandler

s
**Parameters:** clip

- the clipboard to transfer the data into
**Parameters:** action

- the transfer action requested; this should
be a value of either

COPY

or

MOVE

;
the operation performed is the intersection of the transfer
capabilities given by getSourceActions and the requested action;
the intersection may result in an action of

NONE

if the requested action isn't supported
**Throws:** IllegalStateException

- if the clipboard is currently unavailable
**See Also:** Clipboard.setContents(Transferable, ClipboardOwner)

- importData

```java
public boolean importData​(
TransferHandler.TransferSupport
support)
```

Causes a transfer to occur from a clipboard or a drag and
drop operation. The

Transferable

to be
imported and the component to transfer to are contained
within the

TransferSupport

.

While the drag and drop implementation calls

canImport

to determine the suitability of a transfer before calling this
method, the implementation of paste does not. As such, it cannot
be assumed that the transfer is acceptable upon a call to
this method for paste. It is recommended that

canImport

be
explicitly called to cover this case.

Note: The

TransferSupport

object passed to this method
is only valid for the duration of the method call. It is undefined
what values it may contain after this method returns.

**Parameters:** support

- the object containing the details of
the transfer, not

null

.
**Returns:** true if the data was inserted into the component,
false otherwise
**Throws:** NullPointerException

- if

support

is

null
**Since:** 1.6
**See Also:** canImport(TransferHandler.TransferSupport)

- importData

```java
public boolean importData​(
JComponent
comp,

Transferable
t)
```

Causes a transfer to a component from a clipboard or a
DND drop operation. The

Transferable

represents
the data to be imported into the component.

Note: Swing now calls the newer version of

importData

that takes a

TransferSupport

, which in turn calls this
method (if the component in the

TransferSupport

is a

JComponent

). Developers are encouraged to call and override the
newer version as it provides more information (and is the only
version that supports use with a

TransferHandler

set directly
on a

JFrame

or other non-

JComponent

).

**Parameters:** comp

- the component to receive the transfer;
provided to enable sharing of

TransferHandler

s
**Parameters:** t

- the data to import
**Returns:** true if the data was inserted into the component, false otherwise
**See Also:** importData(TransferHandler.TransferSupport)

- canImport

```java
public boolean canImport​(
TransferHandler.TransferSupport
support)
```

This method is called repeatedly during a drag and drop operation
to allow the developer to configure properties of, and to return
the acceptability of transfers; with a return value of

true

indicating that the transfer represented by the given

TransferSupport

(which contains all of the details of the
transfer) is acceptable at the current time, and a value of

false

rejecting the transfer.

For those components that automatically display a drop location during
drag and drop, accepting the transfer, by default, tells them to show
the drop location. This can be changed by calling

setShowDropLocation

on the

TransferSupport

.

By default, when the transfer is accepted, the chosen drop action is that
picked by the user via their drag gesture. The developer can override
this and choose a different action, from the supported source
actions, by calling

setDropAction

on the

TransferSupport

.

On every call to

canImport

, the

TransferSupport

contains
fresh state. As such, any properties set on it must be set on every
call. Upon a drop,

canImport

is called one final time before
calling into

importData

. Any state set on the

TransferSupport

during that last call will be available in

importData

.

This method is not called internally in response to paste operations.
As such, it is recommended that implementations of

importData

explicitly call this method for such cases and that this method
be prepared to return the suitability of paste operations as well.

Note: The

TransferSupport

object passed to this method
is only valid for the duration of the method call. It is undefined
what values it may contain after this method returns.

**Parameters:** support

- the object containing the details of
the transfer, not

null

.
**Returns:** true

if the import can happen,

false

otherwise
**Throws:** NullPointerException

- if

support

is

null
**Since:** 1.6
**See Also:** importData(TransferHandler.TransferSupport)

,

TransferHandler.TransferSupport.setShowDropLocation(boolean)

,

TransferHandler.TransferSupport.setDropAction(int)

- canImport

```java
public boolean canImport​(
JComponent
comp,

DataFlavor
[] transferFlavors)
```

Indicates whether a component will accept an import of the given
set of data flavors prior to actually attempting to import it.

Note: Swing now calls the newer version of

canImport

that takes a

TransferSupport

, which in turn calls this
method (only if the component in the

TransferSupport

is a

JComponent

). Developers are encouraged to call and override the
newer version as it provides more information (and is the only
version that supports use with a

TransferHandler

set directly
on a

JFrame

or other non-

JComponent

).

**Parameters:** comp

- the component to receive the transfer;
provided to enable sharing of

TransferHandler

s
**Parameters:** transferFlavors

- the data formats available
**Returns:** true if the data can be inserted into the component, false otherwise
**See Also:** canImport(TransferHandler.TransferSupport)

- getSourceActions

```java
public int getSourceActions​(
JComponent
c)
```

Returns the type of transfer actions supported by the source;
any bitwise-OR combination of

COPY

,

MOVE

and

LINK

.

Some models are not mutable, so a transfer operation of

MOVE

should not be advertised in that case. Returning

NONE

disables transfers from the component.

**Parameters:** c

- the component holding the data to be transferred;
provided to enable sharing of

TransferHandler

s
**Returns:** COPY

if the transfer property can be found,
otherwise returns

NONE

- getVisualRepresentation

```java
public
Icon
getVisualRepresentation​(
Transferable
t)
```

Returns an object that establishes the look of a transfer. This is
useful for both providing feedback while performing a drag operation and for
representing the transfer in a clipboard implementation that has a visual
appearance. The implementation of the

Icon

interface should
not alter the graphics clip or alpha level.
The icon implementation need not be rectangular or paint all of the
bounding rectangle and logic that calls the icons paint method should
not assume the all bits are painted.

null

is a valid return value
for this method and indicates there is no visual representation provided.
In that case, the calling logic is free to represent the
transferable however it wants.

The default Swing logic will not do an alpha blended drag animation if
the return is

null

.

**Parameters:** t

- the data to be transferred; this value is expected to have been
created by the

createTransferable

method
**Returns:** null

, indicating
there is no default visual representation

- createTransferable

```java
protected
Transferable
createTransferable​(
JComponent
c)
```

Creates a

Transferable

to use as the source for
a data transfer. Returns the representation of the data to
be transferred, or

null

if the component's
property is

null

**Parameters:** c

- the component holding the data to be transferred;
provided to enable sharing of

TransferHandler

s
**Returns:** the representation of the data to be transferred, or

null

if the property associated with

c

is

null

- exportDone

```java
protected void exportDone​(
JComponent
source,

Transferable
data,
int action)
```

Invoked after data has been exported. This method should remove
the data that was transferred if the action was

MOVE

.

This method is implemented to do nothing since

MOVE

is not a supported action of this implementation
(

getSourceActions

does not include

MOVE

).

**Parameters:** source

- the component that was the source of the data
**Parameters:** data

- The data that was transferred or possibly null
if the action is

NONE

.
**Parameters:** action

- the actual action that was performed

Field Detail

- NONE

```java
public static final int NONE
```

An

int

representing no transfer action.

**See Also:** Constant Field Values

- COPY

```java
public static final int COPY
```

An

int

representing a "copy" transfer action.
This value is used when data is copied to a clipboard
or copied elsewhere in a drag and drop operation.

**See Also:** Constant Field Values

- MOVE

```java
public static final int MOVE
```

An

int

representing a "move" transfer action.
This value is used when data is moved to a clipboard (i.e. a cut)
or moved elsewhere in a drag and drop operation.

**See Also:** Constant Field Values

- COPY_OR_MOVE

```java
public static final int COPY_OR_MOVE
```

An

int

representing a source action capability of either
"copy" or "move".

**See Also:** Constant Field Values

- LINK

```java
public static final int LINK
```

An

int

representing a "link" transfer action.
This value is used to specify that data should be linked in a drag
and drop operation.

**Since:** 1.6
**See Also:** DnDConstants.ACTION_LINK

,

Constant Field Values

---

#### Field Detail

NONE

```java
public static final int NONE
```

An

int

representing no transfer action.

**See Also:** Constant Field Values

---

#### NONE

public static final int NONE

An

int

representing no transfer action.

COPY

```java
public static final int COPY
```

An

int

representing a "copy" transfer action.
This value is used when data is copied to a clipboard
or copied elsewhere in a drag and drop operation.

**See Also:** Constant Field Values

---

#### COPY

public static final int COPY

An

int

representing a "copy" transfer action.
This value is used when data is copied to a clipboard
or copied elsewhere in a drag and drop operation.

MOVE

```java
public static final int MOVE
```

An

int

representing a "move" transfer action.
This value is used when data is moved to a clipboard (i.e. a cut)
or moved elsewhere in a drag and drop operation.

**See Also:** Constant Field Values

---

#### MOVE

public static final int MOVE

An

int

representing a "move" transfer action.
This value is used when data is moved to a clipboard (i.e. a cut)
or moved elsewhere in a drag and drop operation.

COPY_OR_MOVE

```java
public static final int COPY_OR_MOVE
```

An

int

representing a source action capability of either
"copy" or "move".

**See Also:** Constant Field Values

---

#### COPY_OR_MOVE

public static final int COPY_OR_MOVE

An

int

representing a source action capability of either
"copy" or "move".

LINK

```java
public static final int LINK
```

An

int

representing a "link" transfer action.
This value is used to specify that data should be linked in a drag
and drop operation.

**Since:** 1.6
**See Also:** DnDConstants.ACTION_LINK

,

Constant Field Values

---

#### LINK

public static final int LINK

An

int

representing a "link" transfer action.
This value is used to specify that data should be linked in a drag
and drop operation.

Constructor Detail

- TransferHandler

```java
public TransferHandler​(
String
property)
```

Constructs a transfer handler that can transfer a Java Bean property
from one component to another via the clipboard or a drag and drop
operation.

**Parameters:** property

- the name of the property to transfer; this can
be

null

if there is no property associated with the transfer
handler (a subclass that performs some other kind of transfer, for example)

- TransferHandler

```java
protected TransferHandler()
```

Convenience constructor for subclasses.

---

#### Constructor Detail

TransferHandler

```java
public TransferHandler​(
String
property)
```

Constructs a transfer handler that can transfer a Java Bean property
from one component to another via the clipboard or a drag and drop
operation.

**Parameters:** property

- the name of the property to transfer; this can
be

null

if there is no property associated with the transfer
handler (a subclass that performs some other kind of transfer, for example)

---

#### TransferHandler

public TransferHandler​(

String

property)

Constructs a transfer handler that can transfer a Java Bean property
from one component to another via the clipboard or a drag and drop
operation.

TransferHandler

```java
protected TransferHandler()
```

Convenience constructor for subclasses.

---

#### TransferHandler

protected TransferHandler()

Convenience constructor for subclasses.

Method Detail

- getCutAction

```java
public static
Action
getCutAction()
```

Returns an

Action

that performs cut operations to the
clipboard. When performed, this action operates on the

JComponent

source of the

ActionEvent

by invoking

exportToClipboard

,
with a

MOVE

action, on the component's

TransferHandler

.

**Returns:** an

Action

for performing cuts to the clipboard

- getCopyAction

```java
public static
Action
getCopyAction()
```

Returns an

Action

that performs copy operations to the
clipboard. When performed, this action operates on the

JComponent

source of the

ActionEvent

by invoking

exportToClipboard

,
with a

COPY

action, on the component's

TransferHandler

.

**Returns:** an

Action

for performing copies to the clipboard

- getPasteAction

```java
public static
Action
getPasteAction()
```

Returns an

Action

that performs paste operations from the
clipboard. When performed, this action operates on the

JComponent

source of the

ActionEvent

by invoking

importData

,
with the clipboard contents, on the component's

TransferHandler

.

**Returns:** an

Action

for performing pastes from the clipboard

- setDragImage

```java
public void setDragImage​(
Image
img)
```

Sets the drag image parameter. The image has to be prepared
for rendering by the moment of the call. The image is stored
by reference because of some performance reasons.

**Parameters:** img

- an image to drag

- getDragImage

```java
public
Image
getDragImage()
```

Returns the drag image. If there is no image to drag,
the returned value is

null

.

**Returns:** the reference to the drag image

- setDragImageOffset

```java
public void setDragImageOffset​(
Point
p)
```

Sets an anchor offset for the image to drag.
It can not be

null

.

**Parameters:** p

- a

Point

object that corresponds
to coordinates of an anchor offset of the image
relative to the upper left corner of the image

- getDragImageOffset

```java
public
Point
getDragImageOffset()
```

Returns an anchor offset for the image to drag.

**Returns:** a

Point

object that corresponds
to coordinates of an anchor offset of the image
relative to the upper left corner of the image.
The point

(0,0)

returns by default.

- exportAsDrag

```java
public void exportAsDrag​(
JComponent
comp,

InputEvent
e,
int action)
```

Causes the Swing drag support to be initiated. This is called by
the various UI implementations in the

javax.swing.plaf.basic

package if the dragEnabled property is set on the component.
This can be called by custom UI
implementations to use the Swing drag support. This method can also be called
by a Swing extension written as a subclass of

JComponent

to take advantage of the Swing drag support.

The transfer

will not necessarily

have been completed at the
return of this call (i.e. the call does not block waiting for the drop).
The transfer will take place through the Swing implementation of the

java.awt.dnd

mechanism, requiring no further effort
from the developer. The

exportDone

method will be called
when the transfer has completed.

**Parameters:** comp

- the component holding the data to be transferred;
provided to enable sharing of

TransferHandler

s
**Parameters:** e

- the event that triggered the transfer
**Parameters:** action

- the transfer action initially requested;
either

COPY

,

MOVE

or

LINK

;
the DnD system may change the action used during the
course of the drag operation

- exportToClipboard

```java
public void exportToClipboard​(
JComponent
comp,

Clipboard
clip,
int action)
throws
IllegalStateException
```

Causes a transfer from the given component to the
given clipboard. This method is called by the default cut and
copy actions registered in a component's action map.

The transfer will take place using the

java.awt.datatransfer

mechanism, requiring no further effort from the developer. Any data
transfer

will

be complete and the

exportDone

method will be called with the action that occurred, before this method
returns. Should the clipboard be unavailable when attempting to place
data on it, the

IllegalStateException

thrown by

Clipboard.setContents(Transferable, ClipboardOwner)

will
be propagated through this method. However,

exportDone

will first be called with an action
of

NONE

for consistency.

**Parameters:** comp

- the component holding the data to be transferred;
provided to enable sharing of

TransferHandler

s
**Parameters:** clip

- the clipboard to transfer the data into
**Parameters:** action

- the transfer action requested; this should
be a value of either

COPY

or

MOVE

;
the operation performed is the intersection of the transfer
capabilities given by getSourceActions and the requested action;
the intersection may result in an action of

NONE

if the requested action isn't supported
**Throws:** IllegalStateException

- if the clipboard is currently unavailable
**See Also:** Clipboard.setContents(Transferable, ClipboardOwner)

- importData

```java
public boolean importData​(
TransferHandler.TransferSupport
support)
```

Causes a transfer to occur from a clipboard or a drag and
drop operation. The

Transferable

to be
imported and the component to transfer to are contained
within the

TransferSupport

.

While the drag and drop implementation calls

canImport

to determine the suitability of a transfer before calling this
method, the implementation of paste does not. As such, it cannot
be assumed that the transfer is acceptable upon a call to
this method for paste. It is recommended that

canImport

be
explicitly called to cover this case.

Note: The

TransferSupport

object passed to this method
is only valid for the duration of the method call. It is undefined
what values it may contain after this method returns.

**Parameters:** support

- the object containing the details of
the transfer, not

null

.
**Returns:** true if the data was inserted into the component,
false otherwise
**Throws:** NullPointerException

- if

support

is

null
**Since:** 1.6
**See Also:** canImport(TransferHandler.TransferSupport)

- importData

```java
public boolean importData​(
JComponent
comp,

Transferable
t)
```

Causes a transfer to a component from a clipboard or a
DND drop operation. The

Transferable

represents
the data to be imported into the component.

Note: Swing now calls the newer version of

importData

that takes a

TransferSupport

, which in turn calls this
method (if the component in the

TransferSupport

is a

JComponent

). Developers are encouraged to call and override the
newer version as it provides more information (and is the only
version that supports use with a

TransferHandler

set directly
on a

JFrame

or other non-

JComponent

).

**Parameters:** comp

- the component to receive the transfer;
provided to enable sharing of

TransferHandler

s
**Parameters:** t

- the data to import
**Returns:** true if the data was inserted into the component, false otherwise
**See Also:** importData(TransferHandler.TransferSupport)

- canImport

```java
public boolean canImport​(
TransferHandler.TransferSupport
support)
```

This method is called repeatedly during a drag and drop operation
to allow the developer to configure properties of, and to return
the acceptability of transfers; with a return value of

true

indicating that the transfer represented by the given

TransferSupport

(which contains all of the details of the
transfer) is acceptable at the current time, and a value of

false

rejecting the transfer.

For those components that automatically display a drop location during
drag and drop, accepting the transfer, by default, tells them to show
the drop location. This can be changed by calling

setShowDropLocation

on the

TransferSupport

.

By default, when the transfer is accepted, the chosen drop action is that
picked by the user via their drag gesture. The developer can override
this and choose a different action, from the supported source
actions, by calling

setDropAction

on the

TransferSupport

.

On every call to

canImport

, the

TransferSupport

contains
fresh state. As such, any properties set on it must be set on every
call. Upon a drop,

canImport

is called one final time before
calling into

importData

. Any state set on the

TransferSupport

during that last call will be available in

importData

.

This method is not called internally in response to paste operations.
As such, it is recommended that implementations of

importData

explicitly call this method for such cases and that this method
be prepared to return the suitability of paste operations as well.

Note: The

TransferSupport

object passed to this method
is only valid for the duration of the method call. It is undefined
what values it may contain after this method returns.

**Parameters:** support

- the object containing the details of
the transfer, not

null

.
**Returns:** true

if the import can happen,

false

otherwise
**Throws:** NullPointerException

- if

support

is

null
**Since:** 1.6
**See Also:** importData(TransferHandler.TransferSupport)

,

TransferHandler.TransferSupport.setShowDropLocation(boolean)

,

TransferHandler.TransferSupport.setDropAction(int)

- canImport

```java
public boolean canImport​(
JComponent
comp,

DataFlavor
[] transferFlavors)
```

Indicates whether a component will accept an import of the given
set of data flavors prior to actually attempting to import it.

Note: Swing now calls the newer version of

canImport

that takes a

TransferSupport

, which in turn calls this
method (only if the component in the

TransferSupport

is a

JComponent

). Developers are encouraged to call and override the
newer version as it provides more information (and is the only
version that supports use with a

TransferHandler

set directly
on a

JFrame

or other non-

JComponent

).

**Parameters:** comp

- the component to receive the transfer;
provided to enable sharing of

TransferHandler

s
**Parameters:** transferFlavors

- the data formats available
**Returns:** true if the data can be inserted into the component, false otherwise
**See Also:** canImport(TransferHandler.TransferSupport)

- getSourceActions

```java
public int getSourceActions​(
JComponent
c)
```

Returns the type of transfer actions supported by the source;
any bitwise-OR combination of

COPY

,

MOVE

and

LINK

.

Some models are not mutable, so a transfer operation of

MOVE

should not be advertised in that case. Returning

NONE

disables transfers from the component.

**Parameters:** c

- the component holding the data to be transferred;
provided to enable sharing of

TransferHandler

s
**Returns:** COPY

if the transfer property can be found,
otherwise returns

NONE

- getVisualRepresentation

```java
public
Icon
getVisualRepresentation​(
Transferable
t)
```

Returns an object that establishes the look of a transfer. This is
useful for both providing feedback while performing a drag operation and for
representing the transfer in a clipboard implementation that has a visual
appearance. The implementation of the

Icon

interface should
not alter the graphics clip or alpha level.
The icon implementation need not be rectangular or paint all of the
bounding rectangle and logic that calls the icons paint method should
not assume the all bits are painted.

null

is a valid return value
for this method and indicates there is no visual representation provided.
In that case, the calling logic is free to represent the
transferable however it wants.

The default Swing logic will not do an alpha blended drag animation if
the return is

null

.

**Parameters:** t

- the data to be transferred; this value is expected to have been
created by the

createTransferable

method
**Returns:** null

, indicating
there is no default visual representation

- createTransferable

```java
protected
Transferable
createTransferable​(
JComponent
c)
```

Creates a

Transferable

to use as the source for
a data transfer. Returns the representation of the data to
be transferred, or

null

if the component's
property is

null

**Parameters:** c

- the component holding the data to be transferred;
provided to enable sharing of

TransferHandler

s
**Returns:** the representation of the data to be transferred, or

null

if the property associated with

c

is

null

- exportDone

```java
protected void exportDone​(
JComponent
source,

Transferable
data,
int action)
```

Invoked after data has been exported. This method should remove
the data that was transferred if the action was

MOVE

.

This method is implemented to do nothing since

MOVE

is not a supported action of this implementation
(

getSourceActions

does not include

MOVE

).

**Parameters:** source

- the component that was the source of the data
**Parameters:** data

- The data that was transferred or possibly null
if the action is

NONE

.
**Parameters:** action

- the actual action that was performed

---

#### Method Detail

getCutAction

```java
public static
Action
getCutAction()
```

Returns an

Action

that performs cut operations to the
clipboard. When performed, this action operates on the

JComponent

source of the

ActionEvent

by invoking

exportToClipboard

,
with a

MOVE

action, on the component's

TransferHandler

.

**Returns:** an

Action

for performing cuts to the clipboard

---

#### getCutAction

public static

Action

getCutAction()

Returns an

Action

that performs cut operations to the
clipboard. When performed, this action operates on the

JComponent

source of the

ActionEvent

by invoking

exportToClipboard

,
with a

MOVE

action, on the component's

TransferHandler

.

getCopyAction

```java
public static
Action
getCopyAction()
```

Returns an

Action

that performs copy operations to the
clipboard. When performed, this action operates on the

JComponent

source of the

ActionEvent

by invoking

exportToClipboard

,
with a

COPY

action, on the component's

TransferHandler

.

**Returns:** an

Action

for performing copies to the clipboard

---

#### getCopyAction

public static

Action

getCopyAction()

Returns an

Action

that performs copy operations to the
clipboard. When performed, this action operates on the

JComponent

source of the

ActionEvent

by invoking

exportToClipboard

,
with a

COPY

action, on the component's

TransferHandler

.

getPasteAction

```java
public static
Action
getPasteAction()
```

Returns an

Action

that performs paste operations from the
clipboard. When performed, this action operates on the

JComponent

source of the

ActionEvent

by invoking

importData

,
with the clipboard contents, on the component's

TransferHandler

.

**Returns:** an

Action

for performing pastes from the clipboard

---

#### getPasteAction

public static

Action

getPasteAction()

Returns an

Action

that performs paste operations from the
clipboard. When performed, this action operates on the

JComponent

source of the

ActionEvent

by invoking

importData

,
with the clipboard contents, on the component's

TransferHandler

.

setDragImage

```java
public void setDragImage​(
Image
img)
```

Sets the drag image parameter. The image has to be prepared
for rendering by the moment of the call. The image is stored
by reference because of some performance reasons.

**Parameters:** img

- an image to drag

---

#### setDragImage

public void setDragImage​(

Image

img)

Sets the drag image parameter. The image has to be prepared
for rendering by the moment of the call. The image is stored
by reference because of some performance reasons.

getDragImage

```java
public
Image
getDragImage()
```

Returns the drag image. If there is no image to drag,
the returned value is

null

.

**Returns:** the reference to the drag image

---

#### getDragImage

public

Image

getDragImage()

Returns the drag image. If there is no image to drag,
the returned value is

null

.

setDragImageOffset

```java
public void setDragImageOffset​(
Point
p)
```

Sets an anchor offset for the image to drag.
It can not be

null

.

**Parameters:** p

- a

Point

object that corresponds
to coordinates of an anchor offset of the image
relative to the upper left corner of the image

---

#### setDragImageOffset

public void setDragImageOffset​(

Point

p)

Sets an anchor offset for the image to drag.
It can not be

null

.

getDragImageOffset

```java
public
Point
getDragImageOffset()
```

Returns an anchor offset for the image to drag.

**Returns:** a

Point

object that corresponds
to coordinates of an anchor offset of the image
relative to the upper left corner of the image.
The point

(0,0)

returns by default.

---

#### getDragImageOffset

public

Point

getDragImageOffset()

Returns an anchor offset for the image to drag.

exportAsDrag

```java
public void exportAsDrag​(
JComponent
comp,

InputEvent
e,
int action)
```

Causes the Swing drag support to be initiated. This is called by
the various UI implementations in the

javax.swing.plaf.basic

package if the dragEnabled property is set on the component.
This can be called by custom UI
implementations to use the Swing drag support. This method can also be called
by a Swing extension written as a subclass of

JComponent

to take advantage of the Swing drag support.

The transfer

will not necessarily

have been completed at the
return of this call (i.e. the call does not block waiting for the drop).
The transfer will take place through the Swing implementation of the

java.awt.dnd

mechanism, requiring no further effort
from the developer. The

exportDone

method will be called
when the transfer has completed.

**Parameters:** comp

- the component holding the data to be transferred;
provided to enable sharing of

TransferHandler

s
**Parameters:** e

- the event that triggered the transfer
**Parameters:** action

- the transfer action initially requested;
either

COPY

,

MOVE

or

LINK

;
the DnD system may change the action used during the
course of the drag operation

---

#### exportAsDrag

public void exportAsDrag​(

JComponent

comp,

InputEvent

e,
int action)

Causes the Swing drag support to be initiated. This is called by
the various UI implementations in the

javax.swing.plaf.basic

package if the dragEnabled property is set on the component.
This can be called by custom UI
implementations to use the Swing drag support. This method can also be called
by a Swing extension written as a subclass of

JComponent

to take advantage of the Swing drag support.

The transfer

will not necessarily

have been completed at the
return of this call (i.e. the call does not block waiting for the drop).
The transfer will take place through the Swing implementation of the

java.awt.dnd

mechanism, requiring no further effort
from the developer. The

exportDone

method will be called
when the transfer has completed.

The transfer

will not necessarily

have been completed at the
return of this call (i.e. the call does not block waiting for the drop).
The transfer will take place through the Swing implementation of the

java.awt.dnd

mechanism, requiring no further effort
from the developer. The

exportDone

method will be called
when the transfer has completed.

exportToClipboard

```java
public void exportToClipboard​(
JComponent
comp,

Clipboard
clip,
int action)
throws
IllegalStateException
```

Causes a transfer from the given component to the
given clipboard. This method is called by the default cut and
copy actions registered in a component's action map.

The transfer will take place using the

java.awt.datatransfer

mechanism, requiring no further effort from the developer. Any data
transfer

will

be complete and the

exportDone

method will be called with the action that occurred, before this method
returns. Should the clipboard be unavailable when attempting to place
data on it, the

IllegalStateException

thrown by

Clipboard.setContents(Transferable, ClipboardOwner)

will
be propagated through this method. However,

exportDone

will first be called with an action
of

NONE

for consistency.

**Parameters:** comp

- the component holding the data to be transferred;
provided to enable sharing of

TransferHandler

s
**Parameters:** clip

- the clipboard to transfer the data into
**Parameters:** action

- the transfer action requested; this should
be a value of either

COPY

or

MOVE

;
the operation performed is the intersection of the transfer
capabilities given by getSourceActions and the requested action;
the intersection may result in an action of

NONE

if the requested action isn't supported
**Throws:** IllegalStateException

- if the clipboard is currently unavailable
**See Also:** Clipboard.setContents(Transferable, ClipboardOwner)

---

#### exportToClipboard

public void exportToClipboard​(

JComponent

comp,

Clipboard

clip,
int action)
throws

IllegalStateException

Causes a transfer from the given component to the
given clipboard. This method is called by the default cut and
copy actions registered in a component's action map.

The transfer will take place using the

java.awt.datatransfer

mechanism, requiring no further effort from the developer. Any data
transfer

will

be complete and the

exportDone

method will be called with the action that occurred, before this method
returns. Should the clipboard be unavailable when attempting to place
data on it, the

IllegalStateException

thrown by

Clipboard.setContents(Transferable, ClipboardOwner)

will
be propagated through this method. However,

exportDone

will first be called with an action
of

NONE

for consistency.

The transfer will take place using the

java.awt.datatransfer

mechanism, requiring no further effort from the developer. Any data
transfer

will

be complete and the

exportDone

method will be called with the action that occurred, before this method
returns. Should the clipboard be unavailable when attempting to place
data on it, the

IllegalStateException

thrown by

Clipboard.setContents(Transferable, ClipboardOwner)

will
be propagated through this method. However,

exportDone

will first be called with an action
of

NONE

for consistency.

importData

```java
public boolean importData​(
TransferHandler.TransferSupport
support)
```

Causes a transfer to occur from a clipboard or a drag and
drop operation. The

Transferable

to be
imported and the component to transfer to are contained
within the

TransferSupport

.

While the drag and drop implementation calls

canImport

to determine the suitability of a transfer before calling this
method, the implementation of paste does not. As such, it cannot
be assumed that the transfer is acceptable upon a call to
this method for paste. It is recommended that

canImport

be
explicitly called to cover this case.

Note: The

TransferSupport

object passed to this method
is only valid for the duration of the method call. It is undefined
what values it may contain after this method returns.

**Parameters:** support

- the object containing the details of
the transfer, not

null

.
**Returns:** true if the data was inserted into the component,
false otherwise
**Throws:** NullPointerException

- if

support

is

null
**Since:** 1.6
**See Also:** canImport(TransferHandler.TransferSupport)

---

#### importData

public boolean importData​(

TransferHandler.TransferSupport

support)

Causes a transfer to occur from a clipboard or a drag and
drop operation. The

Transferable

to be
imported and the component to transfer to are contained
within the

TransferSupport

.

While the drag and drop implementation calls

canImport

to determine the suitability of a transfer before calling this
method, the implementation of paste does not. As such, it cannot
be assumed that the transfer is acceptable upon a call to
this method for paste. It is recommended that

canImport

be
explicitly called to cover this case.

Note: The

TransferSupport

object passed to this method
is only valid for the duration of the method call. It is undefined
what values it may contain after this method returns.

While the drag and drop implementation calls

canImport

to determine the suitability of a transfer before calling this
method, the implementation of paste does not. As such, it cannot
be assumed that the transfer is acceptable upon a call to
this method for paste. It is recommended that

canImport

be
explicitly called to cover this case.

Note: The

TransferSupport

object passed to this method
is only valid for the duration of the method call. It is undefined
what values it may contain after this method returns.

Note: The

TransferSupport

object passed to this method
is only valid for the duration of the method call. It is undefined
what values it may contain after this method returns.

importData

```java
public boolean importData​(
JComponent
comp,

Transferable
t)
```

Causes a transfer to a component from a clipboard or a
DND drop operation. The

Transferable

represents
the data to be imported into the component.

Note: Swing now calls the newer version of

importData

that takes a

TransferSupport

, which in turn calls this
method (if the component in the

TransferSupport

is a

JComponent

). Developers are encouraged to call and override the
newer version as it provides more information (and is the only
version that supports use with a

TransferHandler

set directly
on a

JFrame

or other non-

JComponent

).

**Parameters:** comp

- the component to receive the transfer;
provided to enable sharing of

TransferHandler

s
**Parameters:** t

- the data to import
**Returns:** true if the data was inserted into the component, false otherwise
**See Also:** importData(TransferHandler.TransferSupport)

---

#### importData

public boolean importData​(

JComponent

comp,

Transferable

t)

Causes a transfer to a component from a clipboard or a
DND drop operation. The

Transferable

represents
the data to be imported into the component.

Note: Swing now calls the newer version of

importData

that takes a

TransferSupport

, which in turn calls this
method (if the component in the

TransferSupport

is a

JComponent

). Developers are encouraged to call and override the
newer version as it provides more information (and is the only
version that supports use with a

TransferHandler

set directly
on a

JFrame

or other non-

JComponent

).

Note: Swing now calls the newer version of

importData

that takes a

TransferSupport

, which in turn calls this
method (if the component in the

TransferSupport

is a

JComponent

). Developers are encouraged to call and override the
newer version as it provides more information (and is the only
version that supports use with a

TransferHandler

set directly
on a

JFrame

or other non-

JComponent

).

canImport

```java
public boolean canImport​(
TransferHandler.TransferSupport
support)
```

This method is called repeatedly during a drag and drop operation
to allow the developer to configure properties of, and to return
the acceptability of transfers; with a return value of

true

indicating that the transfer represented by the given

TransferSupport

(which contains all of the details of the
transfer) is acceptable at the current time, and a value of

false

rejecting the transfer.

For those components that automatically display a drop location during
drag and drop, accepting the transfer, by default, tells them to show
the drop location. This can be changed by calling

setShowDropLocation

on the

TransferSupport

.

By default, when the transfer is accepted, the chosen drop action is that
picked by the user via their drag gesture. The developer can override
this and choose a different action, from the supported source
actions, by calling

setDropAction

on the

TransferSupport

.

On every call to

canImport

, the

TransferSupport

contains
fresh state. As such, any properties set on it must be set on every
call. Upon a drop,

canImport

is called one final time before
calling into

importData

. Any state set on the

TransferSupport

during that last call will be available in

importData

.

This method is not called internally in response to paste operations.
As such, it is recommended that implementations of

importData

explicitly call this method for such cases and that this method
be prepared to return the suitability of paste operations as well.

Note: The

TransferSupport

object passed to this method
is only valid for the duration of the method call. It is undefined
what values it may contain after this method returns.

**Parameters:** support

- the object containing the details of
the transfer, not

null

.
**Returns:** true

if the import can happen,

false

otherwise
**Throws:** NullPointerException

- if

support

is

null
**Since:** 1.6
**See Also:** importData(TransferHandler.TransferSupport)

,

TransferHandler.TransferSupport.setShowDropLocation(boolean)

,

TransferHandler.TransferSupport.setDropAction(int)

---

#### canImport

public boolean canImport​(

TransferHandler.TransferSupport

support)

This method is called repeatedly during a drag and drop operation
to allow the developer to configure properties of, and to return
the acceptability of transfers; with a return value of

true

indicating that the transfer represented by the given

TransferSupport

(which contains all of the details of the
transfer) is acceptable at the current time, and a value of

false

rejecting the transfer.

For those components that automatically display a drop location during
drag and drop, accepting the transfer, by default, tells them to show
the drop location. This can be changed by calling

setShowDropLocation

on the

TransferSupport

.

By default, when the transfer is accepted, the chosen drop action is that
picked by the user via their drag gesture. The developer can override
this and choose a different action, from the supported source
actions, by calling

setDropAction

on the

TransferSupport

.

On every call to

canImport

, the

TransferSupport

contains
fresh state. As such, any properties set on it must be set on every
call. Upon a drop,

canImport

is called one final time before
calling into

importData

. Any state set on the

TransferSupport

during that last call will be available in

importData

.

This method is not called internally in response to paste operations.
As such, it is recommended that implementations of

importData

explicitly call this method for such cases and that this method
be prepared to return the suitability of paste operations as well.

Note: The

TransferSupport

object passed to this method
is only valid for the duration of the method call. It is undefined
what values it may contain after this method returns.

For those components that automatically display a drop location during
drag and drop, accepting the transfer, by default, tells them to show
the drop location. This can be changed by calling

setShowDropLocation

on the

TransferSupport

.

By default, when the transfer is accepted, the chosen drop action is that
picked by the user via their drag gesture. The developer can override
this and choose a different action, from the supported source
actions, by calling

setDropAction

on the

TransferSupport

.

On every call to

canImport

, the

TransferSupport

contains
fresh state. As such, any properties set on it must be set on every
call. Upon a drop,

canImport

is called one final time before
calling into

importData

. Any state set on the

TransferSupport

during that last call will be available in

importData

.

This method is not called internally in response to paste operations.
As such, it is recommended that implementations of

importData

explicitly call this method for such cases and that this method
be prepared to return the suitability of paste operations as well.

Note: The

TransferSupport

object passed to this method
is only valid for the duration of the method call. It is undefined
what values it may contain after this method returns.

By default, when the transfer is accepted, the chosen drop action is that
picked by the user via their drag gesture. The developer can override
this and choose a different action, from the supported source
actions, by calling

setDropAction

on the

TransferSupport

.

On every call to

canImport

, the

TransferSupport

contains
fresh state. As such, any properties set on it must be set on every
call. Upon a drop,

canImport

is called one final time before
calling into

importData

. Any state set on the

TransferSupport

during that last call will be available in

importData

.

This method is not called internally in response to paste operations.
As such, it is recommended that implementations of

importData

explicitly call this method for such cases and that this method
be prepared to return the suitability of paste operations as well.

Note: The

TransferSupport

object passed to this method
is only valid for the duration of the method call. It is undefined
what values it may contain after this method returns.

On every call to

canImport

, the

TransferSupport

contains
fresh state. As such, any properties set on it must be set on every
call. Upon a drop,

canImport

is called one final time before
calling into

importData

. Any state set on the

TransferSupport

during that last call will be available in

importData

.

This method is not called internally in response to paste operations.
As such, it is recommended that implementations of

importData

explicitly call this method for such cases and that this method
be prepared to return the suitability of paste operations as well.

Note: The

TransferSupport

object passed to this method
is only valid for the duration of the method call. It is undefined
what values it may contain after this method returns.

This method is not called internally in response to paste operations.
As such, it is recommended that implementations of

importData

explicitly call this method for such cases and that this method
be prepared to return the suitability of paste operations as well.

Note: The

TransferSupport

object passed to this method
is only valid for the duration of the method call. It is undefined
what values it may contain after this method returns.

Note: The

TransferSupport

object passed to this method
is only valid for the duration of the method call. It is undefined
what values it may contain after this method returns.

canImport

```java
public boolean canImport​(
JComponent
comp,

DataFlavor
[] transferFlavors)
```

Indicates whether a component will accept an import of the given
set of data flavors prior to actually attempting to import it.

Note: Swing now calls the newer version of

canImport

that takes a

TransferSupport

, which in turn calls this
method (only if the component in the

TransferSupport

is a

JComponent

). Developers are encouraged to call and override the
newer version as it provides more information (and is the only
version that supports use with a

TransferHandler

set directly
on a

JFrame

or other non-

JComponent

).

**Parameters:** comp

- the component to receive the transfer;
provided to enable sharing of

TransferHandler

s
**Parameters:** transferFlavors

- the data formats available
**Returns:** true if the data can be inserted into the component, false otherwise
**See Also:** canImport(TransferHandler.TransferSupport)

---

#### canImport

public boolean canImport​(

JComponent

comp,

DataFlavor

[] transferFlavors)

Indicates whether a component will accept an import of the given
set of data flavors prior to actually attempting to import it.

Note: Swing now calls the newer version of

canImport

that takes a

TransferSupport

, which in turn calls this
method (only if the component in the

TransferSupport

is a

JComponent

). Developers are encouraged to call and override the
newer version as it provides more information (and is the only
version that supports use with a

TransferHandler

set directly
on a

JFrame

or other non-

JComponent

).

Note: Swing now calls the newer version of

canImport

that takes a

TransferSupport

, which in turn calls this
method (only if the component in the

TransferSupport

is a

JComponent

). Developers are encouraged to call and override the
newer version as it provides more information (and is the only
version that supports use with a

TransferHandler

set directly
on a

JFrame

or other non-

JComponent

).

getSourceActions

```java
public int getSourceActions​(
JComponent
c)
```

Returns the type of transfer actions supported by the source;
any bitwise-OR combination of

COPY

,

MOVE

and

LINK

.

Some models are not mutable, so a transfer operation of

MOVE

should not be advertised in that case. Returning

NONE

disables transfers from the component.

**Parameters:** c

- the component holding the data to be transferred;
provided to enable sharing of

TransferHandler

s
**Returns:** COPY

if the transfer property can be found,
otherwise returns

NONE

---

#### getSourceActions

public int getSourceActions​(

JComponent

c)

Returns the type of transfer actions supported by the source;
any bitwise-OR combination of

COPY

,

MOVE

and

LINK

.

Some models are not mutable, so a transfer operation of

MOVE

should not be advertised in that case. Returning

NONE

disables transfers from the component.

Some models are not mutable, so a transfer operation of

MOVE

should not be advertised in that case. Returning

NONE

disables transfers from the component.

getVisualRepresentation

```java
public
Icon
getVisualRepresentation​(
Transferable
t)
```

Returns an object that establishes the look of a transfer. This is
useful for both providing feedback while performing a drag operation and for
representing the transfer in a clipboard implementation that has a visual
appearance. The implementation of the

Icon

interface should
not alter the graphics clip or alpha level.
The icon implementation need not be rectangular or paint all of the
bounding rectangle and logic that calls the icons paint method should
not assume the all bits are painted.

null

is a valid return value
for this method and indicates there is no visual representation provided.
In that case, the calling logic is free to represent the
transferable however it wants.

The default Swing logic will not do an alpha blended drag animation if
the return is

null

.

**Parameters:** t

- the data to be transferred; this value is expected to have been
created by the

createTransferable

method
**Returns:** null

, indicating
there is no default visual representation

---

#### getVisualRepresentation

public

Icon

getVisualRepresentation​(

Transferable

t)

Returns an object that establishes the look of a transfer. This is
useful for both providing feedback while performing a drag operation and for
representing the transfer in a clipboard implementation that has a visual
appearance. The implementation of the

Icon

interface should
not alter the graphics clip or alpha level.
The icon implementation need not be rectangular or paint all of the
bounding rectangle and logic that calls the icons paint method should
not assume the all bits are painted.

null

is a valid return value
for this method and indicates there is no visual representation provided.
In that case, the calling logic is free to represent the
transferable however it wants.

The default Swing logic will not do an alpha blended drag animation if
the return is

null

.

The default Swing logic will not do an alpha blended drag animation if
the return is

null

.

createTransferable

```java
protected
Transferable
createTransferable​(
JComponent
c)
```

Creates a

Transferable

to use as the source for
a data transfer. Returns the representation of the data to
be transferred, or

null

if the component's
property is

null

**Parameters:** c

- the component holding the data to be transferred;
provided to enable sharing of

TransferHandler

s
**Returns:** the representation of the data to be transferred, or

null

if the property associated with

c

is

null

---

#### createTransferable

protected

Transferable

createTransferable​(

JComponent

c)

Creates a

Transferable

to use as the source for
a data transfer. Returns the representation of the data to
be transferred, or

null

if the component's
property is

null

exportDone

```java
protected void exportDone​(
JComponent
source,

Transferable
data,
int action)
```

Invoked after data has been exported. This method should remove
the data that was transferred if the action was

MOVE

.

This method is implemented to do nothing since

MOVE

is not a supported action of this implementation
(

getSourceActions

does not include

MOVE

).

**Parameters:** source

- the component that was the source of the data
**Parameters:** data

- The data that was transferred or possibly null
if the action is

NONE

.
**Parameters:** action

- the actual action that was performed

---

#### exportDone

protected void exportDone​(

JComponent

source,

Transferable

data,
int action)

Invoked after data has been exported. This method should remove
the data that was transferred if the action was

MOVE

.

This method is implemented to do nothing since

MOVE

is not a supported action of this implementation
(

getSourceActions

does not include

MOVE

).

This method is implemented to do nothing since

MOVE

is not a supported action of this implementation
(

getSourceActions

does not include

MOVE

).

---

