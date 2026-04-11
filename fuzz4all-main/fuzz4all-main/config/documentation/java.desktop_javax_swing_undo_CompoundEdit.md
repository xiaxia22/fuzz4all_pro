# Class CompoundEdit

**Source:** `java.desktop\javax\swing\undo\CompoundEdit.html`

### Class Description

```java
public class
CompoundEdit

extends
AbstractUndoableEdit
```

A concrete subclass of AbstractUndoableEdit, used to assemble little
UndoableEdits into great big ones.

**All Implemented Interfaces:** Serializable

,

UndoableEdit

---

### Field Details

#### protected
Vector
<
UndoableEdit
> edits

The collection of

UndoableEdit

s
undone/redone en masse by this

CompoundEdit

.

---

### Constructor Details

#### public CompoundEdit()

Constructs a

CompoundEdit

.

---

### Method Details

#### public void undo()
throws
CannotUndoException

Sends

undo

to all contained

UndoableEdits

in the reverse of
the order in which they were added.

**Specified by:**
- undo

in interface

UndoableEdit

**Overrides:**
- undo

in class

AbstractUndoableEdit

**Throws:**
- CannotUndoException

- if

canUndo

returns

false

**See Also:**
- AbstractUndoableEdit.canUndo()

---

#### public void redo()
throws
CannotRedoException

Sends

redo

to all contained

UndoableEdit

s in the order in
which they were added.

**Specified by:**
- redo

in interface

UndoableEdit

**Overrides:**
- redo

in class

AbstractUndoableEdit

**Throws:**
- CannotRedoException

- if

canRedo

returns

false

**See Also:**
- AbstractUndoableEdit.canRedo()

---

#### protected
UndoableEdit
lastEdit()

Returns the last

UndoableEdit

in

edits

, or

null

if

edits

is empty.

**Returns:**
- the last

UndoableEdit

in

edits

,
or

null

if

edits

is empty.

---

#### public void die()

Sends

die

to each subedit,
in the reverse of the order that they were added.

**Specified by:**
- die

in interface

UndoableEdit

**Overrides:**
- die

in class

AbstractUndoableEdit

**See Also:**
- die()

---

#### public boolean addEdit​(
UndoableEdit
anEdit)

If this edit is

inProgress

,
accepts

anEdit

and returns true.

The last edit added to this

CompoundEdit

is given a chance to

addEdit(anEdit)

.
If it refuses (returns false),

anEdit

is
given a chance to

replaceEdit

the last edit.
If

anEdit

returns false here,
it is added to

edits

.

**Specified by:**
- addEdit

in interface

UndoableEdit

**Overrides:**
- addEdit

in class

AbstractUndoableEdit

**Parameters:**
- anEdit

- the edit to be added

**Returns:**
- true if the edit is

inProgress

;
otherwise returns false

**See Also:**
- UndoableEdit.addEdit(javax.swing.undo.UndoableEdit)

---

#### public void end()

Sets

inProgress

to false.

**See Also:**
- canUndo()

,

canRedo()

---

#### public boolean canUndo()

Returns false if

isInProgress

or if super
returns false.

**Specified by:**
- canUndo

in interface

UndoableEdit

**Overrides:**
- canUndo

in class

AbstractUndoableEdit

**Returns:**
- true if this edit is

alive

and

hasBeenDone

is

true

**See Also:**
- isInProgress()

---

#### public boolean canRedo()

Returns false if

isInProgress

or if super
returns false.

**Specified by:**
- canRedo

in interface

UndoableEdit

**Overrides:**
- canRedo

in class

AbstractUndoableEdit

**Returns:**
- true

if this edit is

alive

and

hasBeenDone

is

false

**See Also:**
- isInProgress()

---

#### public boolean isInProgress()

Returns true if this edit is in progress--that is, it has not
received end. This generally means that edits are still being
added to it.

**Returns:**
- whether this edit is in progress

**See Also:**
- end()

---

#### public boolean isSignificant()

Returns true if any of the

UndoableEdit

s
in

edits

do.
Returns false if they all return false.

**Specified by:**
- isSignificant

in interface

UndoableEdit

**Overrides:**
- isSignificant

in class

AbstractUndoableEdit

**Returns:**
- true

**See Also:**
- UndoableEdit.isSignificant()

---

#### public
String
getPresentationName()

Returns

getPresentationName

from the
last

UndoableEdit

added to

edits

. If

edits

is empty,
calls super.

**Specified by:**
- getPresentationName

in interface

UndoableEdit

**Overrides:**
- getPresentationName

in class

AbstractUndoableEdit

**Returns:**
- the empty string ""

**See Also:**
- AbstractUndoableEdit.getUndoPresentationName()

,

AbstractUndoableEdit.getRedoPresentationName()

---

#### public
String
getUndoPresentationName()

Returns

getUndoPresentationName

from the last

UndoableEdit

added to

edits

.
If

edits

is empty, calls super.

**Specified by:**
- getUndoPresentationName

in interface

UndoableEdit

**Overrides:**
- getUndoPresentationName

in class

AbstractUndoableEdit

**Returns:**
- the value from the defaults table with key

AbstractUndoableEdit.undoText

, followed
by a space, followed by

getPresentationName

unless

getPresentationName

is "" in which
case, the defaults value is returned alone.

**See Also:**
- AbstractUndoableEdit.getPresentationName()

---

#### public
String
getRedoPresentationName()

Returns

getRedoPresentationName

from the last

UndoableEdit

added to

edits

.
If

edits

is empty, calls super.

**Specified by:**
- getRedoPresentationName

in interface

UndoableEdit

**Overrides:**
- getRedoPresentationName

in class

AbstractUndoableEdit

**Returns:**
- the value from the defaults table with key

AbstractUndoableEdit.redoText

, followed
by a space, followed by

getPresentationName

unless

getPresentationName

is "" in which
case, the defaults value is returned alone.

**See Also:**
- AbstractUndoableEdit.getPresentationName()

---

#### public
String
toString()

Returns a string that displays and identifies this
object's properties.

**Overrides:**
- toString

in class

AbstractUndoableEdit

**Returns:**
- a String representation of this object

---

### Additional Sections

#### Class CompoundEdit

java.lang.Object

- javax.swing.undo.AbstractUndoableEdit
- - javax.swing.undo.CompoundEdit

javax.swing.undo.AbstractUndoableEdit

- javax.swing.undo.CompoundEdit

javax.swing.undo.CompoundEdit

**All Implemented Interfaces:** Serializable

,

UndoableEdit

**Direct Known Subclasses:** AbstractDocument.DefaultDocumentEvent

,

UndoManager

```java
public class
CompoundEdit

extends
AbstractUndoableEdit
```

A concrete subclass of AbstractUndoableEdit, used to assemble little
UndoableEdits into great big ones.

**See Also:** Serialized Form

public class

CompoundEdit

extends

AbstractUndoableEdit

A concrete subclass of AbstractUndoableEdit, used to assemble little
UndoableEdits into great big ones.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Vector

<

UndoableEdit

>

edits

The collection of

UndoableEdit

s
undone/redone en masse by this

CompoundEdit

.

- Fields declared in class javax.swing.undo.

AbstractUndoableEdit

RedoName

,

UndoName

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CompoundEdit

()

Constructs a

CompoundEdit

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

addEdit

​(

UndoableEdit

anEdit)

If this edit is

inProgress

,
accepts

anEdit

and returns true.

boolean

canRedo

()

Returns false if

isInProgress

or if super
returns false.

boolean

canUndo

()

Returns false if

isInProgress

or if super
returns false.

void

die

()

Sends

die

to each subedit,
in the reverse of the order that they were added.

void

end

()

Sets

inProgress

to false.

String

getPresentationName

()

Returns

getPresentationName

from the
last

UndoableEdit

added to

edits

.

String

getRedoPresentationName

()

Returns

getRedoPresentationName

from the last

UndoableEdit

added to

edits

.

String

getUndoPresentationName

()

Returns

getUndoPresentationName

from the last

UndoableEdit

added to

edits

.

boolean

isInProgress

()

Returns true if this edit is in progress--that is, it has not
received end.

boolean

isSignificant

()

Returns true if any of the

UndoableEdit

s
in

edits

do.

protected

UndoableEdit

lastEdit

()

Returns the last

UndoableEdit

in

edits

, or

null

if

edits

is empty.

void

redo

()

Sends

redo

to all contained

UndoableEdit

s in the order in
which they were added.

String

toString

()

Returns a string that displays and identifies this
object's properties.

void

undo

()

Sends

undo

to all contained

UndoableEdits

in the reverse of
the order in which they were added.

- Methods declared in class javax.swing.undo.

AbstractUndoableEdit

replaceEdit

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

Fields

Modifier and Type

Field

Description

protected

Vector

<

UndoableEdit

>

edits

The collection of

UndoableEdit

s
undone/redone en masse by this

CompoundEdit

.

- Fields declared in class javax.swing.undo.

AbstractUndoableEdit

RedoName

,

UndoName

---

#### Field Summary

The collection of

UndoableEdit

s
undone/redone en masse by this

CompoundEdit

.

Fields declared in class javax.swing.undo.

AbstractUndoableEdit

RedoName

,

UndoName

---

#### Fields declared in class javax.swing.undo. AbstractUndoableEdit

Constructor Summary

Constructors

Constructor

Description

CompoundEdit

()

Constructs a

CompoundEdit

.

---

#### Constructor Summary

Constructs a

CompoundEdit

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

addEdit

​(

UndoableEdit

anEdit)

If this edit is

inProgress

,
accepts

anEdit

and returns true.

boolean

canRedo

()

Returns false if

isInProgress

or if super
returns false.

boolean

canUndo

()

Returns false if

isInProgress

or if super
returns false.

void

die

()

Sends

die

to each subedit,
in the reverse of the order that they were added.

void

end

()

Sets

inProgress

to false.

String

getPresentationName

()

Returns

getPresentationName

from the
last

UndoableEdit

added to

edits

.

String

getRedoPresentationName

()

Returns

getRedoPresentationName

from the last

UndoableEdit

added to

edits

.

String

getUndoPresentationName

()

Returns

getUndoPresentationName

from the last

UndoableEdit

added to

edits

.

boolean

isInProgress

()

Returns true if this edit is in progress--that is, it has not
received end.

boolean

isSignificant

()

Returns true if any of the

UndoableEdit

s
in

edits

do.

protected

UndoableEdit

lastEdit

()

Returns the last

UndoableEdit

in

edits

, or

null

if

edits

is empty.

void

redo

()

Sends

redo

to all contained

UndoableEdit

s in the order in
which they were added.

String

toString

()

Returns a string that displays and identifies this
object's properties.

void

undo

()

Sends

undo

to all contained

UndoableEdits

in the reverse of
the order in which they were added.

- Methods declared in class javax.swing.undo.

AbstractUndoableEdit

replaceEdit

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

If this edit is

inProgress

,
accepts

anEdit

and returns true.

Returns false if

isInProgress

or if super
returns false.

Sends

die

to each subedit,
in the reverse of the order that they were added.

Sets

inProgress

to false.

Returns

getPresentationName

from the
last

UndoableEdit

added to

edits

.

Returns

getRedoPresentationName

from the last

UndoableEdit

added to

edits

.

Returns

getUndoPresentationName

from the last

UndoableEdit

added to

edits

.

Returns true if this edit is in progress--that is, it has not
received end.

Returns true if any of the

UndoableEdit

s
in

edits

do.

Returns the last

UndoableEdit

in

edits

, or

null

if

edits

is empty.

Sends

redo

to all contained

UndoableEdit

s in the order in
which they were added.

Returns a string that displays and identifies this
object's properties.

Sends

undo

to all contained

UndoableEdits

in the reverse of
the order in which they were added.

Methods declared in class javax.swing.undo.

AbstractUndoableEdit

replaceEdit

---

#### Methods declared in class javax.swing.undo. AbstractUndoableEdit

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

============ FIELD DETAIL ===========

- Field Detail

- edits

```java
protected
Vector
<
UndoableEdit
> edits
```

The collection of

UndoableEdit

s
undone/redone en masse by this

CompoundEdit

.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- CompoundEdit

```java
public CompoundEdit()
```

Constructs a

CompoundEdit

.

============ METHOD DETAIL ==========

- Method Detail

- undo

```java
public void undo()
throws
CannotUndoException
```

Sends

undo

to all contained

UndoableEdits

in the reverse of
the order in which they were added.

**Specified by:** undo

in interface

UndoableEdit
**Overrides:** undo

in class

AbstractUndoableEdit
**Throws:** CannotUndoException

- if

canUndo

returns

false
**See Also:** AbstractUndoableEdit.canUndo()

- redo

```java
public void redo()
throws
CannotRedoException
```

Sends

redo

to all contained

UndoableEdit

s in the order in
which they were added.

**Specified by:** redo

in interface

UndoableEdit
**Overrides:** redo

in class

AbstractUndoableEdit
**Throws:** CannotRedoException

- if

canRedo

returns

false
**See Also:** AbstractUndoableEdit.canRedo()

- lastEdit

```java
protected
UndoableEdit
lastEdit()
```

Returns the last

UndoableEdit

in

edits

, or

null

if

edits

is empty.

**Returns:** the last

UndoableEdit

in

edits

,
or

null

if

edits

is empty.

- die

```java
public void die()
```

Sends

die

to each subedit,
in the reverse of the order that they were added.

**Specified by:** die

in interface

UndoableEdit
**Overrides:** die

in class

AbstractUndoableEdit
**See Also:** die()

- addEdit

```java
public boolean addEdit​(
UndoableEdit
anEdit)
```

If this edit is

inProgress

,
accepts

anEdit

and returns true.

The last edit added to this

CompoundEdit

is given a chance to

addEdit(anEdit)

.
If it refuses (returns false),

anEdit

is
given a chance to

replaceEdit

the last edit.
If

anEdit

returns false here,
it is added to

edits

.

**Specified by:** addEdit

in interface

UndoableEdit
**Overrides:** addEdit

in class

AbstractUndoableEdit
**Parameters:** anEdit

- the edit to be added
**Returns:** true if the edit is

inProgress

;
otherwise returns false
**See Also:** UndoableEdit.addEdit(javax.swing.undo.UndoableEdit)

- end

```java
public void end()
```

Sets

inProgress

to false.

**See Also:** canUndo()

,

canRedo()

- canUndo

```java
public boolean canUndo()
```

Returns false if

isInProgress

or if super
returns false.

**Specified by:** canUndo

in interface

UndoableEdit
**Overrides:** canUndo

in class

AbstractUndoableEdit
**Returns:** true if this edit is

alive

and

hasBeenDone

is

true
**See Also:** isInProgress()

- canRedo

```java
public boolean canRedo()
```

Returns false if

isInProgress

or if super
returns false.

**Specified by:** canRedo

in interface

UndoableEdit
**Overrides:** canRedo

in class

AbstractUndoableEdit
**Returns:** true

if this edit is

alive

and

hasBeenDone

is

false
**See Also:** isInProgress()

- isInProgress

```java
public boolean isInProgress()
```

Returns true if this edit is in progress--that is, it has not
received end. This generally means that edits are still being
added to it.

**Returns:** whether this edit is in progress
**See Also:** end()

- isSignificant

```java
public boolean isSignificant()
```

Returns true if any of the

UndoableEdit

s
in

edits

do.
Returns false if they all return false.

**Specified by:** isSignificant

in interface

UndoableEdit
**Overrides:** isSignificant

in class

AbstractUndoableEdit
**Returns:** true
**See Also:** UndoableEdit.isSignificant()

- getPresentationName

```java
public
String
getPresentationName()
```

Returns

getPresentationName

from the
last

UndoableEdit

added to

edits

. If

edits

is empty,
calls super.

**Specified by:** getPresentationName

in interface

UndoableEdit
**Overrides:** getPresentationName

in class

AbstractUndoableEdit
**Returns:** the empty string ""
**See Also:** AbstractUndoableEdit.getUndoPresentationName()

,

AbstractUndoableEdit.getRedoPresentationName()

- getUndoPresentationName

```java
public
String
getUndoPresentationName()
```

Returns

getUndoPresentationName

from the last

UndoableEdit

added to

edits

.
If

edits

is empty, calls super.

**Specified by:** getUndoPresentationName

in interface

UndoableEdit
**Overrides:** getUndoPresentationName

in class

AbstractUndoableEdit
**Returns:** the value from the defaults table with key

AbstractUndoableEdit.undoText

, followed
by a space, followed by

getPresentationName

unless

getPresentationName

is "" in which
case, the defaults value is returned alone.
**See Also:** AbstractUndoableEdit.getPresentationName()

- getRedoPresentationName

```java
public
String
getRedoPresentationName()
```

Returns

getRedoPresentationName

from the last

UndoableEdit

added to

edits

.
If

edits

is empty, calls super.

**Specified by:** getRedoPresentationName

in interface

UndoableEdit
**Overrides:** getRedoPresentationName

in class

AbstractUndoableEdit
**Returns:** the value from the defaults table with key

AbstractUndoableEdit.redoText

, followed
by a space, followed by

getPresentationName

unless

getPresentationName

is "" in which
case, the defaults value is returned alone.
**See Also:** AbstractUndoableEdit.getPresentationName()

- toString

```java
public
String
toString()
```

Returns a string that displays and identifies this
object's properties.

**Overrides:** toString

in class

AbstractUndoableEdit
**Returns:** a String representation of this object

Field Detail

- edits

```java
protected
Vector
<
UndoableEdit
> edits
```

The collection of

UndoableEdit

s
undone/redone en masse by this

CompoundEdit

.

---

#### Field Detail

edits

```java
protected
Vector
<
UndoableEdit
> edits
```

The collection of

UndoableEdit

s
undone/redone en masse by this

CompoundEdit

.

---

#### edits

protected

Vector

<

UndoableEdit

> edits

The collection of

UndoableEdit

s
undone/redone en masse by this

CompoundEdit

.

Constructor Detail

- CompoundEdit

```java
public CompoundEdit()
```

Constructs a

CompoundEdit

.

---

#### Constructor Detail

CompoundEdit

```java
public CompoundEdit()
```

Constructs a

CompoundEdit

.

---

#### CompoundEdit

public CompoundEdit()

Constructs a

CompoundEdit

.

Method Detail

- undo

```java
public void undo()
throws
CannotUndoException
```

Sends

undo

to all contained

UndoableEdits

in the reverse of
the order in which they were added.

**Specified by:** undo

in interface

UndoableEdit
**Overrides:** undo

in class

AbstractUndoableEdit
**Throws:** CannotUndoException

- if

canUndo

returns

false
**See Also:** AbstractUndoableEdit.canUndo()

- redo

```java
public void redo()
throws
CannotRedoException
```

Sends

redo

to all contained

UndoableEdit

s in the order in
which they were added.

**Specified by:** redo

in interface

UndoableEdit
**Overrides:** redo

in class

AbstractUndoableEdit
**Throws:** CannotRedoException

- if

canRedo

returns

false
**See Also:** AbstractUndoableEdit.canRedo()

- lastEdit

```java
protected
UndoableEdit
lastEdit()
```

Returns the last

UndoableEdit

in

edits

, or

null

if

edits

is empty.

**Returns:** the last

UndoableEdit

in

edits

,
or

null

if

edits

is empty.

- die

```java
public void die()
```

Sends

die

to each subedit,
in the reverse of the order that they were added.

**Specified by:** die

in interface

UndoableEdit
**Overrides:** die

in class

AbstractUndoableEdit
**See Also:** die()

- addEdit

```java
public boolean addEdit​(
UndoableEdit
anEdit)
```

If this edit is

inProgress

,
accepts

anEdit

and returns true.

The last edit added to this

CompoundEdit

is given a chance to

addEdit(anEdit)

.
If it refuses (returns false),

anEdit

is
given a chance to

replaceEdit

the last edit.
If

anEdit

returns false here,
it is added to

edits

.

**Specified by:** addEdit

in interface

UndoableEdit
**Overrides:** addEdit

in class

AbstractUndoableEdit
**Parameters:** anEdit

- the edit to be added
**Returns:** true if the edit is

inProgress

;
otherwise returns false
**See Also:** UndoableEdit.addEdit(javax.swing.undo.UndoableEdit)

- end

```java
public void end()
```

Sets

inProgress

to false.

**See Also:** canUndo()

,

canRedo()

- canUndo

```java
public boolean canUndo()
```

Returns false if

isInProgress

or if super
returns false.

**Specified by:** canUndo

in interface

UndoableEdit
**Overrides:** canUndo

in class

AbstractUndoableEdit
**Returns:** true if this edit is

alive

and

hasBeenDone

is

true
**See Also:** isInProgress()

- canRedo

```java
public boolean canRedo()
```

Returns false if

isInProgress

or if super
returns false.

**Specified by:** canRedo

in interface

UndoableEdit
**Overrides:** canRedo

in class

AbstractUndoableEdit
**Returns:** true

if this edit is

alive

and

hasBeenDone

is

false
**See Also:** isInProgress()

- isInProgress

```java
public boolean isInProgress()
```

Returns true if this edit is in progress--that is, it has not
received end. This generally means that edits are still being
added to it.

**Returns:** whether this edit is in progress
**See Also:** end()

- isSignificant

```java
public boolean isSignificant()
```

Returns true if any of the

UndoableEdit

s
in

edits

do.
Returns false if they all return false.

**Specified by:** isSignificant

in interface

UndoableEdit
**Overrides:** isSignificant

in class

AbstractUndoableEdit
**Returns:** true
**See Also:** UndoableEdit.isSignificant()

- getPresentationName

```java
public
String
getPresentationName()
```

Returns

getPresentationName

from the
last

UndoableEdit

added to

edits

. If

edits

is empty,
calls super.

**Specified by:** getPresentationName

in interface

UndoableEdit
**Overrides:** getPresentationName

in class

AbstractUndoableEdit
**Returns:** the empty string ""
**See Also:** AbstractUndoableEdit.getUndoPresentationName()

,

AbstractUndoableEdit.getRedoPresentationName()

- getUndoPresentationName

```java
public
String
getUndoPresentationName()
```

Returns

getUndoPresentationName

from the last

UndoableEdit

added to

edits

.
If

edits

is empty, calls super.

**Specified by:** getUndoPresentationName

in interface

UndoableEdit
**Overrides:** getUndoPresentationName

in class

AbstractUndoableEdit
**Returns:** the value from the defaults table with key

AbstractUndoableEdit.undoText

, followed
by a space, followed by

getPresentationName

unless

getPresentationName

is "" in which
case, the defaults value is returned alone.
**See Also:** AbstractUndoableEdit.getPresentationName()

- getRedoPresentationName

```java
public
String
getRedoPresentationName()
```

Returns

getRedoPresentationName

from the last

UndoableEdit

added to

edits

.
If

edits

is empty, calls super.

**Specified by:** getRedoPresentationName

in interface

UndoableEdit
**Overrides:** getRedoPresentationName

in class

AbstractUndoableEdit
**Returns:** the value from the defaults table with key

AbstractUndoableEdit.redoText

, followed
by a space, followed by

getPresentationName

unless

getPresentationName

is "" in which
case, the defaults value is returned alone.
**See Also:** AbstractUndoableEdit.getPresentationName()

- toString

```java
public
String
toString()
```

Returns a string that displays and identifies this
object's properties.

**Overrides:** toString

in class

AbstractUndoableEdit
**Returns:** a String representation of this object

---

#### Method Detail

undo

```java
public void undo()
throws
CannotUndoException
```

Sends

undo

to all contained

UndoableEdits

in the reverse of
the order in which they were added.

**Specified by:** undo

in interface

UndoableEdit
**Overrides:** undo

in class

AbstractUndoableEdit
**Throws:** CannotUndoException

- if

canUndo

returns

false
**See Also:** AbstractUndoableEdit.canUndo()

---

#### undo

public void undo()
throws

CannotUndoException

Sends

undo

to all contained

UndoableEdits

in the reverse of
the order in which they were added.

redo

```java
public void redo()
throws
CannotRedoException
```

Sends

redo

to all contained

UndoableEdit

s in the order in
which they were added.

**Specified by:** redo

in interface

UndoableEdit
**Overrides:** redo

in class

AbstractUndoableEdit
**Throws:** CannotRedoException

- if

canRedo

returns

false
**See Also:** AbstractUndoableEdit.canRedo()

---

#### redo

public void redo()
throws

CannotRedoException

Sends

redo

to all contained

UndoableEdit

s in the order in
which they were added.

lastEdit

```java
protected
UndoableEdit
lastEdit()
```

Returns the last

UndoableEdit

in

edits

, or

null

if

edits

is empty.

**Returns:** the last

UndoableEdit

in

edits

,
or

null

if

edits

is empty.

---

#### lastEdit

protected

UndoableEdit

lastEdit()

Returns the last

UndoableEdit

in

edits

, or

null

if

edits

is empty.

die

```java
public void die()
```

Sends

die

to each subedit,
in the reverse of the order that they were added.

**Specified by:** die

in interface

UndoableEdit
**Overrides:** die

in class

AbstractUndoableEdit
**See Also:** die()

---

#### die

public void die()

Sends

die

to each subedit,
in the reverse of the order that they were added.

addEdit

```java
public boolean addEdit​(
UndoableEdit
anEdit)
```

If this edit is

inProgress

,
accepts

anEdit

and returns true.

The last edit added to this

CompoundEdit

is given a chance to

addEdit(anEdit)

.
If it refuses (returns false),

anEdit

is
given a chance to

replaceEdit

the last edit.
If

anEdit

returns false here,
it is added to

edits

.

**Specified by:** addEdit

in interface

UndoableEdit
**Overrides:** addEdit

in class

AbstractUndoableEdit
**Parameters:** anEdit

- the edit to be added
**Returns:** true if the edit is

inProgress

;
otherwise returns false
**See Also:** UndoableEdit.addEdit(javax.swing.undo.UndoableEdit)

---

#### addEdit

public boolean addEdit​(

UndoableEdit

anEdit)

If this edit is

inProgress

,
accepts

anEdit

and returns true.

The last edit added to this

CompoundEdit

is given a chance to

addEdit(anEdit)

.
If it refuses (returns false),

anEdit

is
given a chance to

replaceEdit

the last edit.
If

anEdit

returns false here,
it is added to

edits

.

The last edit added to this

CompoundEdit

is given a chance to

addEdit(anEdit)

.
If it refuses (returns false),

anEdit

is
given a chance to

replaceEdit

the last edit.
If

anEdit

returns false here,
it is added to

edits

.

end

```java
public void end()
```

Sets

inProgress

to false.

**See Also:** canUndo()

,

canRedo()

---

#### end

public void end()

Sets

inProgress

to false.

canUndo

```java
public boolean canUndo()
```

Returns false if

isInProgress

or if super
returns false.

**Specified by:** canUndo

in interface

UndoableEdit
**Overrides:** canUndo

in class

AbstractUndoableEdit
**Returns:** true if this edit is

alive

and

hasBeenDone

is

true
**See Also:** isInProgress()

---

#### canUndo

public boolean canUndo()

Returns false if

isInProgress

or if super
returns false.

canRedo

```java
public boolean canRedo()
```

Returns false if

isInProgress

or if super
returns false.

**Specified by:** canRedo

in interface

UndoableEdit
**Overrides:** canRedo

in class

AbstractUndoableEdit
**Returns:** true

if this edit is

alive

and

hasBeenDone

is

false
**See Also:** isInProgress()

---

#### canRedo

public boolean canRedo()

Returns false if

isInProgress

or if super
returns false.

isInProgress

```java
public boolean isInProgress()
```

Returns true if this edit is in progress--that is, it has not
received end. This generally means that edits are still being
added to it.

**Returns:** whether this edit is in progress
**See Also:** end()

---

#### isInProgress

public boolean isInProgress()

Returns true if this edit is in progress--that is, it has not
received end. This generally means that edits are still being
added to it.

isSignificant

```java
public boolean isSignificant()
```

Returns true if any of the

UndoableEdit

s
in

edits

do.
Returns false if they all return false.

**Specified by:** isSignificant

in interface

UndoableEdit
**Overrides:** isSignificant

in class

AbstractUndoableEdit
**Returns:** true
**See Also:** UndoableEdit.isSignificant()

---

#### isSignificant

public boolean isSignificant()

Returns true if any of the

UndoableEdit

s
in

edits

do.
Returns false if they all return false.

getPresentationName

```java
public
String
getPresentationName()
```

Returns

getPresentationName

from the
last

UndoableEdit

added to

edits

. If

edits

is empty,
calls super.

**Specified by:** getPresentationName

in interface

UndoableEdit
**Overrides:** getPresentationName

in class

AbstractUndoableEdit
**Returns:** the empty string ""
**See Also:** AbstractUndoableEdit.getUndoPresentationName()

,

AbstractUndoableEdit.getRedoPresentationName()

---

#### getPresentationName

public

String

getPresentationName()

Returns

getPresentationName

from the
last

UndoableEdit

added to

edits

. If

edits

is empty,
calls super.

getUndoPresentationName

```java
public
String
getUndoPresentationName()
```

Returns

getUndoPresentationName

from the last

UndoableEdit

added to

edits

.
If

edits

is empty, calls super.

**Specified by:** getUndoPresentationName

in interface

UndoableEdit
**Overrides:** getUndoPresentationName

in class

AbstractUndoableEdit
**Returns:** the value from the defaults table with key

AbstractUndoableEdit.undoText

, followed
by a space, followed by

getPresentationName

unless

getPresentationName

is "" in which
case, the defaults value is returned alone.
**See Also:** AbstractUndoableEdit.getPresentationName()

---

#### getUndoPresentationName

public

String

getUndoPresentationName()

Returns

getUndoPresentationName

from the last

UndoableEdit

added to

edits

.
If

edits

is empty, calls super.

getRedoPresentationName

```java
public
String
getRedoPresentationName()
```

Returns

getRedoPresentationName

from the last

UndoableEdit

added to

edits

.
If

edits

is empty, calls super.

**Specified by:** getRedoPresentationName

in interface

UndoableEdit
**Overrides:** getRedoPresentationName

in class

AbstractUndoableEdit
**Returns:** the value from the defaults table with key

AbstractUndoableEdit.redoText

, followed
by a space, followed by

getPresentationName

unless

getPresentationName

is "" in which
case, the defaults value is returned alone.
**See Also:** AbstractUndoableEdit.getPresentationName()

---

#### getRedoPresentationName

public

String

getRedoPresentationName()

Returns

getRedoPresentationName

from the last

UndoableEdit

added to

edits

.
If

edits

is empty, calls super.

toString

```java
public
String
toString()
```

Returns a string that displays and identifies this
object's properties.

**Overrides:** toString

in class

AbstractUndoableEdit
**Returns:** a String representation of this object

---

#### toString

public

String

toString()

Returns a string that displays and identifies this
object's properties.

---

