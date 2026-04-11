# Class AbstractUndoableEdit

**Source:** `java.desktop\javax\swing\undo\AbstractUndoableEdit.html`

### Class Description

```java
public class
AbstractUndoableEdit

extends
Object

implements
UndoableEdit
,
Serializable
```

An abstract implementation of

UndoableEdit

,
implementing simple responses to all boolean methods in
that interface.

**All Implemented Interfaces:** Serializable

,

UndoableEdit

---

### Field Details

#### protected static final
String
UndoName

String returned by

getUndoPresentationName

;
as of Java 2 platform v1.3.1 this field is no longer used. This value
is now localized and comes from the defaults table with key

AbstractUndoableEdit.undoText

.

**See Also:**
- UIDefaults

,

Constant Field Values

---

#### protected static final
String
RedoName

String returned by

getRedoPresentationName

;
as of Java 2 platform v1.3.1 this field is no longer used. This value
is now localized and comes from the defaults table with key

AbstractUndoableEdit.redoText

.

**See Also:**
- UIDefaults

,

Constant Field Values

---

### Constructor Details

#### public AbstractUndoableEdit()

Creates an

AbstractUndoableEdit

which defaults

hasBeenDone

and

alive

to

true

.

---

### Method Details

#### public void die()

Sets

alive

to false. Note that this
is a one way operation; dead edits cannot be resurrected.
Sending

undo

or

redo

to
a dead edit results in an exception being thrown.

Typically an edit is killed when it is consolidated by
another edit's

addEdit

or

replaceEdit

method, or when it is dequeued from an

UndoManager

.

**Specified by:**
- die

in interface

UndoableEdit

**See Also:**
- CompoundEdit.die()

---

#### public void undo()
throws
CannotUndoException

Throws

CannotUndoException

if

canUndo

returns

false

. Sets

hasBeenDone

to

false

. Subclasses should override to undo the
operation represented by this edit. Override should begin with
a call to super.

**Specified by:**
- undo

in interface

UndoableEdit

**Throws:**
- CannotUndoException

- if

canUndo

returns

false

**See Also:**
- canUndo()

---

#### public boolean canUndo()

Returns true if this edit is

alive

and

hasBeenDone

is

true

.

**Specified by:**
- canUndo

in interface

UndoableEdit

**Returns:**
- true if this edit is

alive

and

hasBeenDone

is

true

**See Also:**
- die()

,

undo()

,

redo()

---

#### public void redo()
throws
CannotRedoException

Throws

CannotRedoException

if

canRedo

returns false. Sets

hasBeenDone

to

true

.
Subclasses should override to redo the operation represented by
this edit. Override should begin with a call to super.

**Specified by:**
- redo

in interface

UndoableEdit

**Throws:**
- CannotRedoException

- if

canRedo

returns

false

**See Also:**
- canRedo()

---

#### public boolean canRedo()

Returns

true

if this edit is

alive

and

hasBeenDone

is

false

.

**Specified by:**
- canRedo

in interface

UndoableEdit

**Returns:**
- true

if this edit is

alive

and

hasBeenDone

is

false

**See Also:**
- die()

,

undo()

,

redo()

---

#### public boolean addEdit​(
UndoableEdit
anEdit)

This default implementation returns false.

**Specified by:**
- addEdit

in interface

UndoableEdit

**Parameters:**
- anEdit

- the edit to be added

**Returns:**
- false

**See Also:**
- UndoableEdit.addEdit(javax.swing.undo.UndoableEdit)

---

#### public boolean replaceEdit​(
UndoableEdit
anEdit)

This default implementation returns false.

**Specified by:**
- replaceEdit

in interface

UndoableEdit

**Parameters:**
- anEdit

- the edit to replace

**Returns:**
- false

**See Also:**
- UndoableEdit.replaceEdit(javax.swing.undo.UndoableEdit)

---

#### public boolean isSignificant()

This default implementation returns true.

**Specified by:**
- isSignificant

in interface

UndoableEdit

**Returns:**
- true

**See Also:**
- UndoableEdit.isSignificant()

---

#### public
String
getPresentationName()

This default implementation returns "". Used by

getUndoPresentationName

and

getRedoPresentationName

to
construct the strings they return. Subclasses should override to
return an appropriate description of the operation this edit
represents.

**Specified by:**
- getPresentationName

in interface

UndoableEdit

**Returns:**
- the empty string ""

**See Also:**
- getUndoPresentationName()

,

getRedoPresentationName()

---

#### public
String
getUndoPresentationName()

Retreives the value from the defaults table with key

AbstractUndoableEdit.undoText

and returns
that value followed by a space, followed by

getPresentationName

.
If

getPresentationName

returns "",
then the defaults value is returned alone.

**Specified by:**
- getUndoPresentationName

in interface

UndoableEdit

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
- getPresentationName()

---

#### public
String
getRedoPresentationName()

Retreives the value from the defaults table with key

AbstractUndoableEdit.redoText

and returns
that value followed by a space, followed by

getPresentationName

.
If

getPresentationName

returns "",
then the defaults value is returned alone.

**Specified by:**
- getRedoPresentationName

in interface

UndoableEdit

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
- getPresentationName()

---

#### public
String
toString()

Returns a string that displays and identifies this
object's properties.

**Overrides:**
- toString

in class

Object

**Returns:**
- a String representation of this object

---

### Additional Sections

#### Class AbstractUndoableEdit

java.lang.Object

- javax.swing.undo.AbstractUndoableEdit

javax.swing.undo.AbstractUndoableEdit

**All Implemented Interfaces:** Serializable

,

UndoableEdit

**Direct Known Subclasses:** AbstractDocument.ElementEdit

,

CompoundEdit

,

DefaultStyledDocument.AttributeUndoableEdit

,

StateEdit

```java
public class
AbstractUndoableEdit

extends
Object

implements
UndoableEdit
,
Serializable
```

An abstract implementation of

UndoableEdit

,
implementing simple responses to all boolean methods in
that interface.

**See Also:** Serialized Form

public class

AbstractUndoableEdit

extends

Object

implements

UndoableEdit

,

Serializable

An abstract implementation of

UndoableEdit

,
implementing simple responses to all boolean methods in
that interface.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected static

String

RedoName

String returned by

getRedoPresentationName

;
as of Java 2 platform v1.3.1 this field is no longer used.

protected static

String

UndoName

String returned by

getUndoPresentationName

;
as of Java 2 platform v1.3.1 this field is no longer used.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AbstractUndoableEdit

()

Creates an

AbstractUndoableEdit

which defaults

hasBeenDone

and

alive

to

true

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

This default implementation returns false.

boolean

canRedo

()

Returns

true

if this edit is

alive

and

hasBeenDone

is

false

.

boolean

canUndo

()

Returns true if this edit is

alive

and

hasBeenDone

is

true

.

void

die

()

Sets

alive

to false.

String

getPresentationName

()

This default implementation returns "".

String

getRedoPresentationName

()

Retreives the value from the defaults table with key

AbstractUndoableEdit.redoText

and returns
that value followed by a space, followed by

getPresentationName

.

String

getUndoPresentationName

()

Retreives the value from the defaults table with key

AbstractUndoableEdit.undoText

and returns
that value followed by a space, followed by

getPresentationName

.

boolean

isSignificant

()

This default implementation returns true.

void

redo

()

Throws

CannotRedoException

if

canRedo

returns false.

boolean

replaceEdit

​(

UndoableEdit

anEdit)

This default implementation returns false.

String

toString

()

Returns a string that displays and identifies this
object's properties.

void

undo

()

Throws

CannotUndoException

if

canUndo

returns

false

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

protected static

String

RedoName

String returned by

getRedoPresentationName

;
as of Java 2 platform v1.3.1 this field is no longer used.

protected static

String

UndoName

String returned by

getUndoPresentationName

;
as of Java 2 platform v1.3.1 this field is no longer used.

---

#### Field Summary

String returned by

getRedoPresentationName

;
as of Java 2 platform v1.3.1 this field is no longer used.

String returned by

getUndoPresentationName

;
as of Java 2 platform v1.3.1 this field is no longer used.

Constructor Summary

Constructors

Constructor

Description

AbstractUndoableEdit

()

Creates an

AbstractUndoableEdit

which defaults

hasBeenDone

and

alive

to

true

.

---

#### Constructor Summary

Creates an

AbstractUndoableEdit

which defaults

hasBeenDone

and

alive

to

true

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

This default implementation returns false.

boolean

canRedo

()

Returns

true

if this edit is

alive

and

hasBeenDone

is

false

.

boolean

canUndo

()

Returns true if this edit is

alive

and

hasBeenDone

is

true

.

void

die

()

Sets

alive

to false.

String

getPresentationName

()

This default implementation returns "".

String

getRedoPresentationName

()

Retreives the value from the defaults table with key

AbstractUndoableEdit.redoText

and returns
that value followed by a space, followed by

getPresentationName

.

String

getUndoPresentationName

()

Retreives the value from the defaults table with key

AbstractUndoableEdit.undoText

and returns
that value followed by a space, followed by

getPresentationName

.

boolean

isSignificant

()

This default implementation returns true.

void

redo

()

Throws

CannotRedoException

if

canRedo

returns false.

boolean

replaceEdit

​(

UndoableEdit

anEdit)

This default implementation returns false.

String

toString

()

Returns a string that displays and identifies this
object's properties.

void

undo

()

Throws

CannotUndoException

if

canUndo

returns

false

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

wait

,

wait

,

wait

---

#### Method Summary

This default implementation returns false.

Returns

true

if this edit is

alive

and

hasBeenDone

is

false

.

Returns true if this edit is

alive

and

hasBeenDone

is

true

.

Sets

alive

to false.

This default implementation returns "".

Retreives the value from the defaults table with key

AbstractUndoableEdit.redoText

and returns
that value followed by a space, followed by

getPresentationName

.

Retreives the value from the defaults table with key

AbstractUndoableEdit.undoText

and returns
that value followed by a space, followed by

getPresentationName

.

This default implementation returns true.

Throws

CannotRedoException

if

canRedo

returns false.

Returns a string that displays and identifies this
object's properties.

Throws

CannotUndoException

if

canUndo

returns

false

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- UndoName

```java
protected static final
String
UndoName
```

String returned by

getUndoPresentationName

;
as of Java 2 platform v1.3.1 this field is no longer used. This value
is now localized and comes from the defaults table with key

AbstractUndoableEdit.undoText

.

**See Also:** UIDefaults

,

Constant Field Values

- RedoName

```java
protected static final
String
RedoName
```

String returned by

getRedoPresentationName

;
as of Java 2 platform v1.3.1 this field is no longer used. This value
is now localized and comes from the defaults table with key

AbstractUndoableEdit.redoText

.

**See Also:** UIDefaults

,

Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AbstractUndoableEdit

```java
public AbstractUndoableEdit()
```

Creates an

AbstractUndoableEdit

which defaults

hasBeenDone

and

alive

to

true

.

============ METHOD DETAIL ==========

- Method Detail

- die

```java
public void die()
```

Sets

alive

to false. Note that this
is a one way operation; dead edits cannot be resurrected.
Sending

undo

or

redo

to
a dead edit results in an exception being thrown.

Typically an edit is killed when it is consolidated by
another edit's

addEdit

or

replaceEdit

method, or when it is dequeued from an

UndoManager

.

**Specified by:** die

in interface

UndoableEdit
**See Also:** CompoundEdit.die()

- undo

```java
public void undo()
throws
CannotUndoException
```

Throws

CannotUndoException

if

canUndo

returns

false

. Sets

hasBeenDone

to

false

. Subclasses should override to undo the
operation represented by this edit. Override should begin with
a call to super.

**Specified by:** undo

in interface

UndoableEdit
**Throws:** CannotUndoException

- if

canUndo

returns

false
**See Also:** canUndo()

- canUndo

```java
public boolean canUndo()
```

Returns true if this edit is

alive

and

hasBeenDone

is

true

.

**Specified by:** canUndo

in interface

UndoableEdit
**Returns:** true if this edit is

alive

and

hasBeenDone

is

true
**See Also:** die()

,

undo()

,

redo()

- redo

```java
public void redo()
throws
CannotRedoException
```

Throws

CannotRedoException

if

canRedo

returns false. Sets

hasBeenDone

to

true

.
Subclasses should override to redo the operation represented by
this edit. Override should begin with a call to super.

**Specified by:** redo

in interface

UndoableEdit
**Throws:** CannotRedoException

- if

canRedo

returns

false
**See Also:** canRedo()

- canRedo

```java
public boolean canRedo()
```

Returns

true

if this edit is

alive

and

hasBeenDone

is

false

.

**Specified by:** canRedo

in interface

UndoableEdit
**Returns:** true

if this edit is

alive

and

hasBeenDone

is

false
**See Also:** die()

,

undo()

,

redo()

- addEdit

```java
public boolean addEdit​(
UndoableEdit
anEdit)
```

This default implementation returns false.

**Specified by:** addEdit

in interface

UndoableEdit
**Parameters:** anEdit

- the edit to be added
**Returns:** false
**See Also:** UndoableEdit.addEdit(javax.swing.undo.UndoableEdit)

- replaceEdit

```java
public boolean replaceEdit​(
UndoableEdit
anEdit)
```

This default implementation returns false.

**Specified by:** replaceEdit

in interface

UndoableEdit
**Parameters:** anEdit

- the edit to replace
**Returns:** false
**See Also:** UndoableEdit.replaceEdit(javax.swing.undo.UndoableEdit)

- isSignificant

```java
public boolean isSignificant()
```

This default implementation returns true.

**Specified by:** isSignificant

in interface

UndoableEdit
**Returns:** true
**See Also:** UndoableEdit.isSignificant()

- getPresentationName

```java
public
String
getPresentationName()
```

This default implementation returns "". Used by

getUndoPresentationName

and

getRedoPresentationName

to
construct the strings they return. Subclasses should override to
return an appropriate description of the operation this edit
represents.

**Specified by:** getPresentationName

in interface

UndoableEdit
**Returns:** the empty string ""
**See Also:** getUndoPresentationName()

,

getRedoPresentationName()

- getUndoPresentationName

```java
public
String
getUndoPresentationName()
```

Retreives the value from the defaults table with key

AbstractUndoableEdit.undoText

and returns
that value followed by a space, followed by

getPresentationName

.
If

getPresentationName

returns "",
then the defaults value is returned alone.

**Specified by:** getUndoPresentationName

in interface

UndoableEdit
**Returns:** the value from the defaults table with key

AbstractUndoableEdit.undoText

, followed
by a space, followed by

getPresentationName

unless

getPresentationName

is "" in which
case, the defaults value is returned alone.
**See Also:** getPresentationName()

- getRedoPresentationName

```java
public
String
getRedoPresentationName()
```

Retreives the value from the defaults table with key

AbstractUndoableEdit.redoText

and returns
that value followed by a space, followed by

getPresentationName

.
If

getPresentationName

returns "",
then the defaults value is returned alone.

**Specified by:** getRedoPresentationName

in interface

UndoableEdit
**Returns:** the value from the defaults table with key

AbstractUndoableEdit.redoText

, followed
by a space, followed by

getPresentationName

unless

getPresentationName

is "" in which
case, the defaults value is returned alone.
**See Also:** getPresentationName()

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

Object
**Returns:** a String representation of this object

Field Detail

- UndoName

```java
protected static final
String
UndoName
```

String returned by

getUndoPresentationName

;
as of Java 2 platform v1.3.1 this field is no longer used. This value
is now localized and comes from the defaults table with key

AbstractUndoableEdit.undoText

.

**See Also:** UIDefaults

,

Constant Field Values

- RedoName

```java
protected static final
String
RedoName
```

String returned by

getRedoPresentationName

;
as of Java 2 platform v1.3.1 this field is no longer used. This value
is now localized and comes from the defaults table with key

AbstractUndoableEdit.redoText

.

**See Also:** UIDefaults

,

Constant Field Values

---

#### Field Detail

UndoName

```java
protected static final
String
UndoName
```

String returned by

getUndoPresentationName

;
as of Java 2 platform v1.3.1 this field is no longer used. This value
is now localized and comes from the defaults table with key

AbstractUndoableEdit.undoText

.

**See Also:** UIDefaults

,

Constant Field Values

---

#### UndoName

protected static final

String

UndoName

String returned by

getUndoPresentationName

;
as of Java 2 platform v1.3.1 this field is no longer used. This value
is now localized and comes from the defaults table with key

AbstractUndoableEdit.undoText

.

RedoName

```java
protected static final
String
RedoName
```

String returned by

getRedoPresentationName

;
as of Java 2 platform v1.3.1 this field is no longer used. This value
is now localized and comes from the defaults table with key

AbstractUndoableEdit.redoText

.

**See Also:** UIDefaults

,

Constant Field Values

---

#### RedoName

protected static final

String

RedoName

String returned by

getRedoPresentationName

;
as of Java 2 platform v1.3.1 this field is no longer used. This value
is now localized and comes from the defaults table with key

AbstractUndoableEdit.redoText

.

Constructor Detail

- AbstractUndoableEdit

```java
public AbstractUndoableEdit()
```

Creates an

AbstractUndoableEdit

which defaults

hasBeenDone

and

alive

to

true

.

---

#### Constructor Detail

AbstractUndoableEdit

```java
public AbstractUndoableEdit()
```

Creates an

AbstractUndoableEdit

which defaults

hasBeenDone

and

alive

to

true

.

---

#### AbstractUndoableEdit

public AbstractUndoableEdit()

Creates an

AbstractUndoableEdit

which defaults

hasBeenDone

and

alive

to

true

.

Method Detail

- die

```java
public void die()
```

Sets

alive

to false. Note that this
is a one way operation; dead edits cannot be resurrected.
Sending

undo

or

redo

to
a dead edit results in an exception being thrown.

Typically an edit is killed when it is consolidated by
another edit's

addEdit

or

replaceEdit

method, or when it is dequeued from an

UndoManager

.

**Specified by:** die

in interface

UndoableEdit
**See Also:** CompoundEdit.die()

- undo

```java
public void undo()
throws
CannotUndoException
```

Throws

CannotUndoException

if

canUndo

returns

false

. Sets

hasBeenDone

to

false

. Subclasses should override to undo the
operation represented by this edit. Override should begin with
a call to super.

**Specified by:** undo

in interface

UndoableEdit
**Throws:** CannotUndoException

- if

canUndo

returns

false
**See Also:** canUndo()

- canUndo

```java
public boolean canUndo()
```

Returns true if this edit is

alive

and

hasBeenDone

is

true

.

**Specified by:** canUndo

in interface

UndoableEdit
**Returns:** true if this edit is

alive

and

hasBeenDone

is

true
**See Also:** die()

,

undo()

,

redo()

- redo

```java
public void redo()
throws
CannotRedoException
```

Throws

CannotRedoException

if

canRedo

returns false. Sets

hasBeenDone

to

true

.
Subclasses should override to redo the operation represented by
this edit. Override should begin with a call to super.

**Specified by:** redo

in interface

UndoableEdit
**Throws:** CannotRedoException

- if

canRedo

returns

false
**See Also:** canRedo()

- canRedo

```java
public boolean canRedo()
```

Returns

true

if this edit is

alive

and

hasBeenDone

is

false

.

**Specified by:** canRedo

in interface

UndoableEdit
**Returns:** true

if this edit is

alive

and

hasBeenDone

is

false
**See Also:** die()

,

undo()

,

redo()

- addEdit

```java
public boolean addEdit​(
UndoableEdit
anEdit)
```

This default implementation returns false.

**Specified by:** addEdit

in interface

UndoableEdit
**Parameters:** anEdit

- the edit to be added
**Returns:** false
**See Also:** UndoableEdit.addEdit(javax.swing.undo.UndoableEdit)

- replaceEdit

```java
public boolean replaceEdit​(
UndoableEdit
anEdit)
```

This default implementation returns false.

**Specified by:** replaceEdit

in interface

UndoableEdit
**Parameters:** anEdit

- the edit to replace
**Returns:** false
**See Also:** UndoableEdit.replaceEdit(javax.swing.undo.UndoableEdit)

- isSignificant

```java
public boolean isSignificant()
```

This default implementation returns true.

**Specified by:** isSignificant

in interface

UndoableEdit
**Returns:** true
**See Also:** UndoableEdit.isSignificant()

- getPresentationName

```java
public
String
getPresentationName()
```

This default implementation returns "". Used by

getUndoPresentationName

and

getRedoPresentationName

to
construct the strings they return. Subclasses should override to
return an appropriate description of the operation this edit
represents.

**Specified by:** getPresentationName

in interface

UndoableEdit
**Returns:** the empty string ""
**See Also:** getUndoPresentationName()

,

getRedoPresentationName()

- getUndoPresentationName

```java
public
String
getUndoPresentationName()
```

Retreives the value from the defaults table with key

AbstractUndoableEdit.undoText

and returns
that value followed by a space, followed by

getPresentationName

.
If

getPresentationName

returns "",
then the defaults value is returned alone.

**Specified by:** getUndoPresentationName

in interface

UndoableEdit
**Returns:** the value from the defaults table with key

AbstractUndoableEdit.undoText

, followed
by a space, followed by

getPresentationName

unless

getPresentationName

is "" in which
case, the defaults value is returned alone.
**See Also:** getPresentationName()

- getRedoPresentationName

```java
public
String
getRedoPresentationName()
```

Retreives the value from the defaults table with key

AbstractUndoableEdit.redoText

and returns
that value followed by a space, followed by

getPresentationName

.
If

getPresentationName

returns "",
then the defaults value is returned alone.

**Specified by:** getRedoPresentationName

in interface

UndoableEdit
**Returns:** the value from the defaults table with key

AbstractUndoableEdit.redoText

, followed
by a space, followed by

getPresentationName

unless

getPresentationName

is "" in which
case, the defaults value is returned alone.
**See Also:** getPresentationName()

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

Object
**Returns:** a String representation of this object

---

#### Method Detail

die

```java
public void die()
```

Sets

alive

to false. Note that this
is a one way operation; dead edits cannot be resurrected.
Sending

undo

or

redo

to
a dead edit results in an exception being thrown.

Typically an edit is killed when it is consolidated by
another edit's

addEdit

or

replaceEdit

method, or when it is dequeued from an

UndoManager

.

**Specified by:** die

in interface

UndoableEdit
**See Also:** CompoundEdit.die()

---

#### die

public void die()

Sets

alive

to false. Note that this
is a one way operation; dead edits cannot be resurrected.
Sending

undo

or

redo

to
a dead edit results in an exception being thrown.

Typically an edit is killed when it is consolidated by
another edit's

addEdit

or

replaceEdit

method, or when it is dequeued from an

UndoManager

.

Typically an edit is killed when it is consolidated by
another edit's

addEdit

or

replaceEdit

method, or when it is dequeued from an

UndoManager

.

undo

```java
public void undo()
throws
CannotUndoException
```

Throws

CannotUndoException

if

canUndo

returns

false

. Sets

hasBeenDone

to

false

. Subclasses should override to undo the
operation represented by this edit. Override should begin with
a call to super.

**Specified by:** undo

in interface

UndoableEdit
**Throws:** CannotUndoException

- if

canUndo

returns

false
**See Also:** canUndo()

---

#### undo

public void undo()
throws

CannotUndoException

Throws

CannotUndoException

if

canUndo

returns

false

. Sets

hasBeenDone

to

false

. Subclasses should override to undo the
operation represented by this edit. Override should begin with
a call to super.

canUndo

```java
public boolean canUndo()
```

Returns true if this edit is

alive

and

hasBeenDone

is

true

.

**Specified by:** canUndo

in interface

UndoableEdit
**Returns:** true if this edit is

alive

and

hasBeenDone

is

true
**See Also:** die()

,

undo()

,

redo()

---

#### canUndo

public boolean canUndo()

Returns true if this edit is

alive

and

hasBeenDone

is

true

.

redo

```java
public void redo()
throws
CannotRedoException
```

Throws

CannotRedoException

if

canRedo

returns false. Sets

hasBeenDone

to

true

.
Subclasses should override to redo the operation represented by
this edit. Override should begin with a call to super.

**Specified by:** redo

in interface

UndoableEdit
**Throws:** CannotRedoException

- if

canRedo

returns

false
**See Also:** canRedo()

---

#### redo

public void redo()
throws

CannotRedoException

Throws

CannotRedoException

if

canRedo

returns false. Sets

hasBeenDone

to

true

.
Subclasses should override to redo the operation represented by
this edit. Override should begin with a call to super.

canRedo

```java
public boolean canRedo()
```

Returns

true

if this edit is

alive

and

hasBeenDone

is

false

.

**Specified by:** canRedo

in interface

UndoableEdit
**Returns:** true

if this edit is

alive

and

hasBeenDone

is

false
**See Also:** die()

,

undo()

,

redo()

---

#### canRedo

public boolean canRedo()

Returns

true

if this edit is

alive

and

hasBeenDone

is

false

.

addEdit

```java
public boolean addEdit​(
UndoableEdit
anEdit)
```

This default implementation returns false.

**Specified by:** addEdit

in interface

UndoableEdit
**Parameters:** anEdit

- the edit to be added
**Returns:** false
**See Also:** UndoableEdit.addEdit(javax.swing.undo.UndoableEdit)

---

#### addEdit

public boolean addEdit​(

UndoableEdit

anEdit)

This default implementation returns false.

replaceEdit

```java
public boolean replaceEdit​(
UndoableEdit
anEdit)
```

This default implementation returns false.

**Specified by:** replaceEdit

in interface

UndoableEdit
**Parameters:** anEdit

- the edit to replace
**Returns:** false
**See Also:** UndoableEdit.replaceEdit(javax.swing.undo.UndoableEdit)

---

#### replaceEdit

public boolean replaceEdit​(

UndoableEdit

anEdit)

This default implementation returns false.

isSignificant

```java
public boolean isSignificant()
```

This default implementation returns true.

**Specified by:** isSignificant

in interface

UndoableEdit
**Returns:** true
**See Also:** UndoableEdit.isSignificant()

---

#### isSignificant

public boolean isSignificant()

This default implementation returns true.

getPresentationName

```java
public
String
getPresentationName()
```

This default implementation returns "". Used by

getUndoPresentationName

and

getRedoPresentationName

to
construct the strings they return. Subclasses should override to
return an appropriate description of the operation this edit
represents.

**Specified by:** getPresentationName

in interface

UndoableEdit
**Returns:** the empty string ""
**See Also:** getUndoPresentationName()

,

getRedoPresentationName()

---

#### getPresentationName

public

String

getPresentationName()

This default implementation returns "". Used by

getUndoPresentationName

and

getRedoPresentationName

to
construct the strings they return. Subclasses should override to
return an appropriate description of the operation this edit
represents.

getUndoPresentationName

```java
public
String
getUndoPresentationName()
```

Retreives the value from the defaults table with key

AbstractUndoableEdit.undoText

and returns
that value followed by a space, followed by

getPresentationName

.
If

getPresentationName

returns "",
then the defaults value is returned alone.

**Specified by:** getUndoPresentationName

in interface

UndoableEdit
**Returns:** the value from the defaults table with key

AbstractUndoableEdit.undoText

, followed
by a space, followed by

getPresentationName

unless

getPresentationName

is "" in which
case, the defaults value is returned alone.
**See Also:** getPresentationName()

---

#### getUndoPresentationName

public

String

getUndoPresentationName()

Retreives the value from the defaults table with key

AbstractUndoableEdit.undoText

and returns
that value followed by a space, followed by

getPresentationName

.
If

getPresentationName

returns "",
then the defaults value is returned alone.

getRedoPresentationName

```java
public
String
getRedoPresentationName()
```

Retreives the value from the defaults table with key

AbstractUndoableEdit.redoText

and returns
that value followed by a space, followed by

getPresentationName

.
If

getPresentationName

returns "",
then the defaults value is returned alone.

**Specified by:** getRedoPresentationName

in interface

UndoableEdit
**Returns:** the value from the defaults table with key

AbstractUndoableEdit.redoText

, followed
by a space, followed by

getPresentationName

unless

getPresentationName

is "" in which
case, the defaults value is returned alone.
**See Also:** getPresentationName()

---

#### getRedoPresentationName

public

String

getRedoPresentationName()

Retreives the value from the defaults table with key

AbstractUndoableEdit.redoText

and returns
that value followed by a space, followed by

getPresentationName

.
If

getPresentationName

returns "",
then the defaults value is returned alone.

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

Object
**Returns:** a String representation of this object

---

#### toString

public

String

toString()

Returns a string that displays and identifies this
object's properties.

---

