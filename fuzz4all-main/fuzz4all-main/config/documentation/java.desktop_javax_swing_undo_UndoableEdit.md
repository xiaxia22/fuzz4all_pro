# Interface UndoableEdit

**Source:** `java.desktop\javax\swing\undo\UndoableEdit.html`

### Class Description

```java
public interface
UndoableEdit
```

An

UndoableEdit

represents an edit. The edit may
be undone, or if already undone the edit may be redone.

UndoableEdit

is designed to be used with the

UndoManager

. As

UndoableEdit

s are generated
by an

UndoableEditListener

they are typically added to
the

UndoManager

. When an

UndoableEdit

is added to an

UndoManager

the following occurs (assuming

end

has not been called on the

UndoManager

):

- If the

UndoManager

contains edits it will call

addEdit

on the current edit passing in the new edit
as the argument. If

addEdit

returns true the
new edit is assumed to have been incorporated into the current edit and
the new edit will not be added to the list of current edits.
Edits can use

addEdit

as a way for smaller edits to
be incorporated into a larger edit and treated as a single edit.

If

addEdit

returns false

replaceEdit

is called on the new edit with the current edit passed in as the
argument. This is the inverse of

addEdit

—
if the new edit returns true from

replaceEdit

, the new
edit replaces the current edit.

The

UndoManager

makes use of

isSignificant

to determine how many edits should be
undone or redone. The

UndoManager

will undo or redo
all insignificant edits (

isSignificant

returns false)
between the current edit and the last or
next significant edit.

addEdit

and

replaceEdit

can be used to treat multiple edits as
a single edit, returning false from

isSignificant

allows for treating can be used to
have many smaller edits undone or redone at once. Similar functionality
can also be done using the

addEdit

method.

**All Known Implementing Classes:** AbstractDocument.DefaultDocumentEvent

,

AbstractDocument.ElementEdit

,

AbstractUndoableEdit

,

CompoundEdit

,

DefaultStyledDocument.AttributeUndoableEdit

,

StateEdit

,

UndoManager

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void undo()
throws
CannotUndoException

Undo the edit.

**Throws:**
- CannotUndoException

- if this edit can not be undone

---

#### boolean canUndo()

Returns true if this edit may be undone.

**Returns:**
- true if this edit may be undone

---

#### void redo()
throws
CannotRedoException

Re-applies the edit.

**Throws:**
- CannotRedoException

- if this edit can not be redone

---

#### boolean canRedo()

Returns true if this edit may be redone.

**Returns:**
- true if this edit may be redone

---

#### void die()

Informs the edit that it should no longer be used. Once an

UndoableEdit

has been marked as dead it can no longer
be undone or redone.

This is a useful hook for cleaning up state no longer
needed once undoing or redoing is impossible--for example,
deleting file resources used by objects that can no longer be
undeleted.

UndoManager

calls this before it dequeues edits.

Note that this is a one-way operation. There is no "un-die"
method.

**See Also:**
- CompoundEdit.die()

---

#### boolean addEdit​(
UndoableEdit
anEdit)

Adds an

UndoableEdit

to this

UndoableEdit

.
This method can be used to coalesce smaller edits into a larger
compound edit. For example, text editors typically allow
undo operations to apply to words or sentences. The text
editor may choose to generate edits on each key event, but allow
those edits to be coalesced into a more user-friendly unit, such as
a word. In this case, the

UndoableEdit

would
override

addEdit

to return true when the edits may
be coalesced.

A return value of true indicates

anEdit

was incorporated
into this edit. A return value of false indicates

anEdit

may not be incorporated into this edit.

Typically the receiver is already in the queue of a

UndoManager

(or other

UndoableEditListener

),
and is being given a chance to incorporate

anEdit

rather than letting it be added to the queue in turn.

If true is returned, from now on

anEdit

must return
false from

canUndo

and

canRedo

,
and must throw the appropriate exception on

undo

or

redo

.

**Parameters:**
- anEdit

- the edit to be added

**Returns:**
- true if

anEdit

may be incorporated into this
edit

---

#### boolean replaceEdit​(
UndoableEdit
anEdit)

Returns true if this

UndoableEdit

should replace

anEdit

. This method is used by

CompoundEdit

and the

UndoManager

; it is called if

anEdit

could not be added to the current edit
(

addEdit

returns false).

This method provides a way for an edit to replace an existing edit.

This message is the opposite of addEdit--anEdit has typically
already been queued in an

UndoManager

(or other
UndoableEditListener), and the receiver is being given a chance
to take its place.

If true is returned, from now on anEdit must return false from
canUndo() and canRedo(), and must throw the appropriate
exception on undo() or redo().

**Parameters:**
- anEdit

- the edit that replaces the current edit

**Returns:**
- true if this edit should replace

anEdit

---

#### boolean isSignificant()

Returns true if this edit is considered significant. A significant
edit is typically an edit that should be presented to the user, perhaps
on a menu item or tooltip. The

UndoManager

will undo,
or redo, all insignificant edits to the next significant edit.

**Returns:**
- true if this edit is significant

---

#### String
getPresentationName()

Returns a localized, human-readable description of this edit, suitable
for use in a change log, for example.

**Returns:**
- description of this edit

---

#### String
getUndoPresentationName()

Returns a localized, human-readable description of the undoable form of
this edit, suitable for use as an Undo menu item, for example.
This is typically derived from

getPresentationName

.

**Returns:**
- a description of the undoable form of this edit

---

#### String
getRedoPresentationName()

Returns a localized, human-readable description of the redoable form of
this edit, suitable for use as a Redo menu item, for example. This is
typically derived from

getPresentationName

.

**Returns:**
- a description of the redoable form of this edit

---

### Additional Sections

#### Interface UndoableEdit

**All Known Implementing Classes:** AbstractDocument.DefaultDocumentEvent

,

AbstractDocument.ElementEdit

,

AbstractUndoableEdit

,

CompoundEdit

,

DefaultStyledDocument.AttributeUndoableEdit

,

StateEdit

,

UndoManager

```java
public interface
UndoableEdit
```

An

UndoableEdit

represents an edit. The edit may
be undone, or if already undone the edit may be redone.

UndoableEdit

is designed to be used with the

UndoManager

. As

UndoableEdit

s are generated
by an

UndoableEditListener

they are typically added to
the

UndoManager

. When an

UndoableEdit

is added to an

UndoManager

the following occurs (assuming

end

has not been called on the

UndoManager

):

- If the

UndoManager

contains edits it will call

addEdit

on the current edit passing in the new edit
as the argument. If

addEdit

returns true the
new edit is assumed to have been incorporated into the current edit and
the new edit will not be added to the list of current edits.
Edits can use

addEdit

as a way for smaller edits to
be incorporated into a larger edit and treated as a single edit.

If

addEdit

returns false

replaceEdit

is called on the new edit with the current edit passed in as the
argument. This is the inverse of

addEdit

—
if the new edit returns true from

replaceEdit

, the new
edit replaces the current edit.

The

UndoManager

makes use of

isSignificant

to determine how many edits should be
undone or redone. The

UndoManager

will undo or redo
all insignificant edits (

isSignificant

returns false)
between the current edit and the last or
next significant edit.

addEdit

and

replaceEdit

can be used to treat multiple edits as
a single edit, returning false from

isSignificant

allows for treating can be used to
have many smaller edits undone or redone at once. Similar functionality
can also be done using the

addEdit

method.

public interface

UndoableEdit

An

UndoableEdit

represents an edit. The edit may
be undone, or if already undone the edit may be redone.

UndoableEdit

is designed to be used with the

UndoManager

. As

UndoableEdit

s are generated
by an

UndoableEditListener

they are typically added to
the

UndoManager

. When an

UndoableEdit

is added to an

UndoManager

the following occurs (assuming

end

has not been called on the

UndoManager

):

- If the

UndoManager

contains edits it will call

addEdit

on the current edit passing in the new edit
as the argument. If

addEdit

returns true the
new edit is assumed to have been incorporated into the current edit and
the new edit will not be added to the list of current edits.
Edits can use

addEdit

as a way for smaller edits to
be incorporated into a larger edit and treated as a single edit.

If

addEdit

returns false

replaceEdit

is called on the new edit with the current edit passed in as the
argument. This is the inverse of

addEdit

—
if the new edit returns true from

replaceEdit

, the new
edit replaces the current edit.

The

UndoManager

makes use of

isSignificant

to determine how many edits should be
undone or redone. The

UndoManager

will undo or redo
all insignificant edits (

isSignificant

returns false)
between the current edit and the last or
next significant edit.

addEdit

and

replaceEdit

can be used to treat multiple edits as
a single edit, returning false from

isSignificant

allows for treating can be used to
have many smaller edits undone or redone at once. Similar functionality
can also be done using the

addEdit

method.

UndoableEdit

is designed to be used with the

UndoManager

. As

UndoableEdit

s are generated
by an

UndoableEditListener

they are typically added to
the

UndoManager

. When an

UndoableEdit

is added to an

UndoManager

the following occurs (assuming

end

has not been called on the

UndoManager

):

- If the

UndoManager

contains edits it will call

addEdit

on the current edit passing in the new edit
as the argument. If

addEdit

returns true the
new edit is assumed to have been incorporated into the current edit and
the new edit will not be added to the list of current edits.
Edits can use

addEdit

as a way for smaller edits to
be incorporated into a larger edit and treated as a single edit.

If

addEdit

returns false

replaceEdit

is called on the new edit with the current edit passed in as the
argument. This is the inverse of

addEdit

—
if the new edit returns true from

replaceEdit

, the new
edit replaces the current edit.

The

UndoManager

makes use of

isSignificant

to determine how many edits should be
undone or redone. The

UndoManager

will undo or redo
all insignificant edits (

isSignificant

returns false)
between the current edit and the last or
next significant edit.

addEdit

and

replaceEdit

can be used to treat multiple edits as
a single edit, returning false from

isSignificant

allows for treating can be used to
have many smaller edits undone or redone at once. Similar functionality
can also be done using the

addEdit

method.

If the

UndoManager

contains edits it will call

addEdit

on the current edit passing in the new edit
as the argument. If

addEdit

returns true the
new edit is assumed to have been incorporated into the current edit and
the new edit will not be added to the list of current edits.
Edits can use

addEdit

as a way for smaller edits to
be incorporated into a larger edit and treated as a single edit.

If

addEdit

returns false

replaceEdit

is called on the new edit with the current edit passed in as the
argument. This is the inverse of

addEdit

—
if the new edit returns true from

replaceEdit

, the new
edit replaces the current edit.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

addEdit

​(

UndoableEdit

anEdit)

Adds an

UndoableEdit

to this

UndoableEdit

.

boolean

canRedo

()

Returns true if this edit may be redone.

boolean

canUndo

()

Returns true if this edit may be undone.

void

die

()

Informs the edit that it should no longer be used.

String

getPresentationName

()

Returns a localized, human-readable description of this edit, suitable
for use in a change log, for example.

String

getRedoPresentationName

()

Returns a localized, human-readable description of the redoable form of
this edit, suitable for use as a Redo menu item, for example.

String

getUndoPresentationName

()

Returns a localized, human-readable description of the undoable form of
this edit, suitable for use as an Undo menu item, for example.

boolean

isSignificant

()

Returns true if this edit is considered significant.

void

redo

()

Re-applies the edit.

boolean

replaceEdit

​(

UndoableEdit

anEdit)

Returns true if this

UndoableEdit

should replace

anEdit

.

void

undo

()

Undo the edit.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

addEdit

​(

UndoableEdit

anEdit)

Adds an

UndoableEdit

to this

UndoableEdit

.

boolean

canRedo

()

Returns true if this edit may be redone.

boolean

canUndo

()

Returns true if this edit may be undone.

void

die

()

Informs the edit that it should no longer be used.

String

getPresentationName

()

Returns a localized, human-readable description of this edit, suitable
for use in a change log, for example.

String

getRedoPresentationName

()

Returns a localized, human-readable description of the redoable form of
this edit, suitable for use as a Redo menu item, for example.

String

getUndoPresentationName

()

Returns a localized, human-readable description of the undoable form of
this edit, suitable for use as an Undo menu item, for example.

boolean

isSignificant

()

Returns true if this edit is considered significant.

void

redo

()

Re-applies the edit.

boolean

replaceEdit

​(

UndoableEdit

anEdit)

Returns true if this

UndoableEdit

should replace

anEdit

.

void

undo

()

Undo the edit.

---

#### Method Summary

Adds an

UndoableEdit

to this

UndoableEdit

.

Returns true if this edit may be redone.

Returns true if this edit may be undone.

Informs the edit that it should no longer be used.

Returns a localized, human-readable description of this edit, suitable
for use in a change log, for example.

Returns a localized, human-readable description of the redoable form of
this edit, suitable for use as a Redo menu item, for example.

Returns a localized, human-readable description of the undoable form of
this edit, suitable for use as an Undo menu item, for example.

Returns true if this edit is considered significant.

Re-applies the edit.

Returns true if this

UndoableEdit

should replace

anEdit

.

Undo the edit.

============ METHOD DETAIL ==========

- Method Detail

- undo

```java
void undo()
throws
CannotUndoException
```

Undo the edit.

**Throws:** CannotUndoException

- if this edit can not be undone

- canUndo

```java
boolean canUndo()
```

Returns true if this edit may be undone.

**Returns:** true if this edit may be undone

- redo

```java
void redo()
throws
CannotRedoException
```

Re-applies the edit.

**Throws:** CannotRedoException

- if this edit can not be redone

- canRedo

```java
boolean canRedo()
```

Returns true if this edit may be redone.

**Returns:** true if this edit may be redone

- die

```java
void die()
```

Informs the edit that it should no longer be used. Once an

UndoableEdit

has been marked as dead it can no longer
be undone or redone.

This is a useful hook for cleaning up state no longer
needed once undoing or redoing is impossible--for example,
deleting file resources used by objects that can no longer be
undeleted.

UndoManager

calls this before it dequeues edits.

Note that this is a one-way operation. There is no "un-die"
method.

**See Also:** CompoundEdit.die()

- addEdit

```java
boolean addEdit​(
UndoableEdit
anEdit)
```

Adds an

UndoableEdit

to this

UndoableEdit

.
This method can be used to coalesce smaller edits into a larger
compound edit. For example, text editors typically allow
undo operations to apply to words or sentences. The text
editor may choose to generate edits on each key event, but allow
those edits to be coalesced into a more user-friendly unit, such as
a word. In this case, the

UndoableEdit

would
override

addEdit

to return true when the edits may
be coalesced.

A return value of true indicates

anEdit

was incorporated
into this edit. A return value of false indicates

anEdit

may not be incorporated into this edit.

Typically the receiver is already in the queue of a

UndoManager

(or other

UndoableEditListener

),
and is being given a chance to incorporate

anEdit

rather than letting it be added to the queue in turn.

If true is returned, from now on

anEdit

must return
false from

canUndo

and

canRedo

,
and must throw the appropriate exception on

undo

or

redo

.

**Parameters:** anEdit

- the edit to be added
**Returns:** true if

anEdit

may be incorporated into this
edit

- replaceEdit

```java
boolean replaceEdit​(
UndoableEdit
anEdit)
```

Returns true if this

UndoableEdit

should replace

anEdit

. This method is used by

CompoundEdit

and the

UndoManager

; it is called if

anEdit

could not be added to the current edit
(

addEdit

returns false).

This method provides a way for an edit to replace an existing edit.

This message is the opposite of addEdit--anEdit has typically
already been queued in an

UndoManager

(or other
UndoableEditListener), and the receiver is being given a chance
to take its place.

If true is returned, from now on anEdit must return false from
canUndo() and canRedo(), and must throw the appropriate
exception on undo() or redo().

**Parameters:** anEdit

- the edit that replaces the current edit
**Returns:** true if this edit should replace

anEdit

- isSignificant

```java
boolean isSignificant()
```

Returns true if this edit is considered significant. A significant
edit is typically an edit that should be presented to the user, perhaps
on a menu item or tooltip. The

UndoManager

will undo,
or redo, all insignificant edits to the next significant edit.

**Returns:** true if this edit is significant

- getPresentationName

```java
String
getPresentationName()
```

Returns a localized, human-readable description of this edit, suitable
for use in a change log, for example.

**Returns:** description of this edit

- getUndoPresentationName

```java
String
getUndoPresentationName()
```

Returns a localized, human-readable description of the undoable form of
this edit, suitable for use as an Undo menu item, for example.
This is typically derived from

getPresentationName

.

**Returns:** a description of the undoable form of this edit

- getRedoPresentationName

```java
String
getRedoPresentationName()
```

Returns a localized, human-readable description of the redoable form of
this edit, suitable for use as a Redo menu item, for example. This is
typically derived from

getPresentationName

.

**Returns:** a description of the redoable form of this edit

Method Detail

- undo

```java
void undo()
throws
CannotUndoException
```

Undo the edit.

**Throws:** CannotUndoException

- if this edit can not be undone

- canUndo

```java
boolean canUndo()
```

Returns true if this edit may be undone.

**Returns:** true if this edit may be undone

- redo

```java
void redo()
throws
CannotRedoException
```

Re-applies the edit.

**Throws:** CannotRedoException

- if this edit can not be redone

- canRedo

```java
boolean canRedo()
```

Returns true if this edit may be redone.

**Returns:** true if this edit may be redone

- die

```java
void die()
```

Informs the edit that it should no longer be used. Once an

UndoableEdit

has been marked as dead it can no longer
be undone or redone.

This is a useful hook for cleaning up state no longer
needed once undoing or redoing is impossible--for example,
deleting file resources used by objects that can no longer be
undeleted.

UndoManager

calls this before it dequeues edits.

Note that this is a one-way operation. There is no "un-die"
method.

**See Also:** CompoundEdit.die()

- addEdit

```java
boolean addEdit​(
UndoableEdit
anEdit)
```

Adds an

UndoableEdit

to this

UndoableEdit

.
This method can be used to coalesce smaller edits into a larger
compound edit. For example, text editors typically allow
undo operations to apply to words or sentences. The text
editor may choose to generate edits on each key event, but allow
those edits to be coalesced into a more user-friendly unit, such as
a word. In this case, the

UndoableEdit

would
override

addEdit

to return true when the edits may
be coalesced.

A return value of true indicates

anEdit

was incorporated
into this edit. A return value of false indicates

anEdit

may not be incorporated into this edit.

Typically the receiver is already in the queue of a

UndoManager

(or other

UndoableEditListener

),
and is being given a chance to incorporate

anEdit

rather than letting it be added to the queue in turn.

If true is returned, from now on

anEdit

must return
false from

canUndo

and

canRedo

,
and must throw the appropriate exception on

undo

or

redo

.

**Parameters:** anEdit

- the edit to be added
**Returns:** true if

anEdit

may be incorporated into this
edit

- replaceEdit

```java
boolean replaceEdit​(
UndoableEdit
anEdit)
```

Returns true if this

UndoableEdit

should replace

anEdit

. This method is used by

CompoundEdit

and the

UndoManager

; it is called if

anEdit

could not be added to the current edit
(

addEdit

returns false).

This method provides a way for an edit to replace an existing edit.

This message is the opposite of addEdit--anEdit has typically
already been queued in an

UndoManager

(or other
UndoableEditListener), and the receiver is being given a chance
to take its place.

If true is returned, from now on anEdit must return false from
canUndo() and canRedo(), and must throw the appropriate
exception on undo() or redo().

**Parameters:** anEdit

- the edit that replaces the current edit
**Returns:** true if this edit should replace

anEdit

- isSignificant

```java
boolean isSignificant()
```

Returns true if this edit is considered significant. A significant
edit is typically an edit that should be presented to the user, perhaps
on a menu item or tooltip. The

UndoManager

will undo,
or redo, all insignificant edits to the next significant edit.

**Returns:** true if this edit is significant

- getPresentationName

```java
String
getPresentationName()
```

Returns a localized, human-readable description of this edit, suitable
for use in a change log, for example.

**Returns:** description of this edit

- getUndoPresentationName

```java
String
getUndoPresentationName()
```

Returns a localized, human-readable description of the undoable form of
this edit, suitable for use as an Undo menu item, for example.
This is typically derived from

getPresentationName

.

**Returns:** a description of the undoable form of this edit

- getRedoPresentationName

```java
String
getRedoPresentationName()
```

Returns a localized, human-readable description of the redoable form of
this edit, suitable for use as a Redo menu item, for example. This is
typically derived from

getPresentationName

.

**Returns:** a description of the redoable form of this edit

---

#### Method Detail

undo

```java
void undo()
throws
CannotUndoException
```

Undo the edit.

**Throws:** CannotUndoException

- if this edit can not be undone

---

#### undo

void undo()
throws

CannotUndoException

Undo the edit.

canUndo

```java
boolean canUndo()
```

Returns true if this edit may be undone.

**Returns:** true if this edit may be undone

---

#### canUndo

boolean canUndo()

Returns true if this edit may be undone.

redo

```java
void redo()
throws
CannotRedoException
```

Re-applies the edit.

**Throws:** CannotRedoException

- if this edit can not be redone

---

#### redo

void redo()
throws

CannotRedoException

Re-applies the edit.

canRedo

```java
boolean canRedo()
```

Returns true if this edit may be redone.

**Returns:** true if this edit may be redone

---

#### canRedo

boolean canRedo()

Returns true if this edit may be redone.

die

```java
void die()
```

Informs the edit that it should no longer be used. Once an

UndoableEdit

has been marked as dead it can no longer
be undone or redone.

This is a useful hook for cleaning up state no longer
needed once undoing or redoing is impossible--for example,
deleting file resources used by objects that can no longer be
undeleted.

UndoManager

calls this before it dequeues edits.

Note that this is a one-way operation. There is no "un-die"
method.

**See Also:** CompoundEdit.die()

---

#### die

void die()

Informs the edit that it should no longer be used. Once an

UndoableEdit

has been marked as dead it can no longer
be undone or redone.

This is a useful hook for cleaning up state no longer
needed once undoing or redoing is impossible--for example,
deleting file resources used by objects that can no longer be
undeleted.

UndoManager

calls this before it dequeues edits.

Note that this is a one-way operation. There is no "un-die"
method.

This is a useful hook for cleaning up state no longer
needed once undoing or redoing is impossible--for example,
deleting file resources used by objects that can no longer be
undeleted.

UndoManager

calls this before it dequeues edits.

Note that this is a one-way operation. There is no "un-die"
method.

Note that this is a one-way operation. There is no "un-die"
method.

addEdit

```java
boolean addEdit​(
UndoableEdit
anEdit)
```

Adds an

UndoableEdit

to this

UndoableEdit

.
This method can be used to coalesce smaller edits into a larger
compound edit. For example, text editors typically allow
undo operations to apply to words or sentences. The text
editor may choose to generate edits on each key event, but allow
those edits to be coalesced into a more user-friendly unit, such as
a word. In this case, the

UndoableEdit

would
override

addEdit

to return true when the edits may
be coalesced.

A return value of true indicates

anEdit

was incorporated
into this edit. A return value of false indicates

anEdit

may not be incorporated into this edit.

Typically the receiver is already in the queue of a

UndoManager

(or other

UndoableEditListener

),
and is being given a chance to incorporate

anEdit

rather than letting it be added to the queue in turn.

If true is returned, from now on

anEdit

must return
false from

canUndo

and

canRedo

,
and must throw the appropriate exception on

undo

or

redo

.

**Parameters:** anEdit

- the edit to be added
**Returns:** true if

anEdit

may be incorporated into this
edit

---

#### addEdit

boolean addEdit​(

UndoableEdit

anEdit)

Adds an

UndoableEdit

to this

UndoableEdit

.
This method can be used to coalesce smaller edits into a larger
compound edit. For example, text editors typically allow
undo operations to apply to words or sentences. The text
editor may choose to generate edits on each key event, but allow
those edits to be coalesced into a more user-friendly unit, such as
a word. In this case, the

UndoableEdit

would
override

addEdit

to return true when the edits may
be coalesced.

A return value of true indicates

anEdit

was incorporated
into this edit. A return value of false indicates

anEdit

may not be incorporated into this edit.

Typically the receiver is already in the queue of a

UndoManager

(or other

UndoableEditListener

),
and is being given a chance to incorporate

anEdit

rather than letting it be added to the queue in turn.

If true is returned, from now on

anEdit

must return
false from

canUndo

and

canRedo

,
and must throw the appropriate exception on

undo

or

redo

.

A return value of true indicates

anEdit

was incorporated
into this edit. A return value of false indicates

anEdit

may not be incorporated into this edit.

Typically the receiver is already in the queue of a

UndoManager

(or other

UndoableEditListener

),
and is being given a chance to incorporate

anEdit

rather than letting it be added to the queue in turn.

If true is returned, from now on

anEdit

must return
false from

canUndo

and

canRedo

,
and must throw the appropriate exception on

undo

or

redo

.

Typically the receiver is already in the queue of a

UndoManager

(or other

UndoableEditListener

),
and is being given a chance to incorporate

anEdit

rather than letting it be added to the queue in turn.

If true is returned, from now on

anEdit

must return
false from

canUndo

and

canRedo

,
and must throw the appropriate exception on

undo

or

redo

.

replaceEdit

```java
boolean replaceEdit​(
UndoableEdit
anEdit)
```

Returns true if this

UndoableEdit

should replace

anEdit

. This method is used by

CompoundEdit

and the

UndoManager

; it is called if

anEdit

could not be added to the current edit
(

addEdit

returns false).

This method provides a way for an edit to replace an existing edit.

This message is the opposite of addEdit--anEdit has typically
already been queued in an

UndoManager

(or other
UndoableEditListener), and the receiver is being given a chance
to take its place.

If true is returned, from now on anEdit must return false from
canUndo() and canRedo(), and must throw the appropriate
exception on undo() or redo().

**Parameters:** anEdit

- the edit that replaces the current edit
**Returns:** true if this edit should replace

anEdit

---

#### replaceEdit

boolean replaceEdit​(

UndoableEdit

anEdit)

Returns true if this

UndoableEdit

should replace

anEdit

. This method is used by

CompoundEdit

and the

UndoManager

; it is called if

anEdit

could not be added to the current edit
(

addEdit

returns false).

This method provides a way for an edit to replace an existing edit.

This message is the opposite of addEdit--anEdit has typically
already been queued in an

UndoManager

(or other
UndoableEditListener), and the receiver is being given a chance
to take its place.

If true is returned, from now on anEdit must return false from
canUndo() and canRedo(), and must throw the appropriate
exception on undo() or redo().

This method provides a way for an edit to replace an existing edit.

This message is the opposite of addEdit--anEdit has typically
already been queued in an

UndoManager

(or other
UndoableEditListener), and the receiver is being given a chance
to take its place.

If true is returned, from now on anEdit must return false from
canUndo() and canRedo(), and must throw the appropriate
exception on undo() or redo().

This message is the opposite of addEdit--anEdit has typically
already been queued in an

UndoManager

(or other
UndoableEditListener), and the receiver is being given a chance
to take its place.

If true is returned, from now on anEdit must return false from
canUndo() and canRedo(), and must throw the appropriate
exception on undo() or redo().

isSignificant

```java
boolean isSignificant()
```

Returns true if this edit is considered significant. A significant
edit is typically an edit that should be presented to the user, perhaps
on a menu item or tooltip. The

UndoManager

will undo,
or redo, all insignificant edits to the next significant edit.

**Returns:** true if this edit is significant

---

#### isSignificant

boolean isSignificant()

Returns true if this edit is considered significant. A significant
edit is typically an edit that should be presented to the user, perhaps
on a menu item or tooltip. The

UndoManager

will undo,
or redo, all insignificant edits to the next significant edit.

getPresentationName

```java
String
getPresentationName()
```

Returns a localized, human-readable description of this edit, suitable
for use in a change log, for example.

**Returns:** description of this edit

---

#### getPresentationName

String

getPresentationName()

Returns a localized, human-readable description of this edit, suitable
for use in a change log, for example.

getUndoPresentationName

```java
String
getUndoPresentationName()
```

Returns a localized, human-readable description of the undoable form of
this edit, suitable for use as an Undo menu item, for example.
This is typically derived from

getPresentationName

.

**Returns:** a description of the undoable form of this edit

---

#### getUndoPresentationName

String

getUndoPresentationName()

Returns a localized, human-readable description of the undoable form of
this edit, suitable for use as an Undo menu item, for example.
This is typically derived from

getPresentationName

.

getRedoPresentationName

```java
String
getRedoPresentationName()
```

Returns a localized, human-readable description of the redoable form of
this edit, suitable for use as a Redo menu item, for example. This is
typically derived from

getPresentationName

.

**Returns:** a description of the redoable form of this edit

---

#### getRedoPresentationName

String

getRedoPresentationName()

Returns a localized, human-readable description of the redoable form of
this edit, suitable for use as a Redo menu item, for example. This is
typically derived from

getPresentationName

.

---

