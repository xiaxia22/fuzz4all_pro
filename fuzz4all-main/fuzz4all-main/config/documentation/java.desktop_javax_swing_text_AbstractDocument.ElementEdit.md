# Class AbstractDocument.ElementEdit

**Source:** `java.desktop\javax\swing\text\AbstractDocument.ElementEdit.html`

### Class Description

```java
public static class
AbstractDocument.ElementEdit

extends
AbstractUndoableEdit

implements
DocumentEvent.ElementChange
```

An implementation of ElementChange that can be added to the document
event.

**All Implemented Interfaces:** Serializable

,

DocumentEvent.ElementChange

,

UndoableEdit

---

### Field Details

*No entries found.*

### Constructor Details

#### public ElementEdit​(
Element
e,
int index,

Element
[] removed,

Element
[] added)

Constructs an edit record. This does not modify the element
so it can safely be used to

catch up

a view to the
current model state for views that just attached to a model.

**Parameters:**
- e

- the element
- index

- the index into the model >= 0
- removed

- a set of elements that were removed
- added

- a set of elements that were added

---

### Method Details

#### public
Element
getElement()

Returns the underlying element.

**Specified by:**
- getElement

in interface

DocumentEvent.ElementChange

**Returns:**
- the element

---

#### public int getIndex()

Returns the index into the list of elements.

**Specified by:**
- getIndex

in interface

DocumentEvent.ElementChange

**Returns:**
- the index >= 0

---

#### public
Element
[] getChildrenRemoved()

Gets a list of children that were removed.

**Specified by:**
- getChildrenRemoved

in interface

DocumentEvent.ElementChange

**Returns:**
- the list

---

#### public
Element
[] getChildrenAdded()

Gets a list of children that were added.

**Specified by:**
- getChildrenAdded

in interface

DocumentEvent.ElementChange

**Returns:**
- the list

---

#### public void redo()
throws
CannotRedoException

Redoes a change.

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

- if the change cannot be redone

**See Also:**
- AbstractUndoableEdit.canRedo()

---

#### public void undo()
throws
CannotUndoException

Undoes a change.

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

- if the change cannot be undone

**See Also:**
- AbstractUndoableEdit.canUndo()

---

### Additional Sections

#### Class AbstractDocument.ElementEdit

java.lang.Object

- javax.swing.undo.AbstractUndoableEdit
- - javax.swing.text.AbstractDocument.ElementEdit

javax.swing.undo.AbstractUndoableEdit

- javax.swing.text.AbstractDocument.ElementEdit

javax.swing.text.AbstractDocument.ElementEdit

**All Implemented Interfaces:** Serializable

,

DocumentEvent.ElementChange

,

UndoableEdit

**Enclosing class:** AbstractDocument

```java
public static class
AbstractDocument.ElementEdit

extends
AbstractUndoableEdit

implements
DocumentEvent.ElementChange
```

An implementation of ElementChange that can be added to the document
event.

**See Also:** Serialized Form

public static class

AbstractDocument.ElementEdit

extends

AbstractUndoableEdit

implements

DocumentEvent.ElementChange

An implementation of ElementChange that can be added to the document
event.

=========== FIELD SUMMARY ===========

- Field Summary

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

ElementEdit

​(

Element

e,
int index,

Element

[] removed,

Element

[] added)

Constructs an edit record.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Element

[]

getChildrenAdded

()

Gets a list of children that were added.

Element

[]

getChildrenRemoved

()

Gets a list of children that were removed.

Element

getElement

()

Returns the underlying element.

int

getIndex

()

Returns the index into the list of elements.

void

redo

()

Redoes a change.

void

undo

()

Undoes a change.

- Methods declared in class javax.swing.undo.

AbstractUndoableEdit

addEdit

,

canRedo

,

canUndo

,

die

,

getPresentationName

,

getRedoPresentationName

,

getUndoPresentationName

,

isSignificant

,

replaceEdit

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

- Fields declared in class javax.swing.undo.

AbstractUndoableEdit

RedoName

,

UndoName

---

#### Field Summary

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

ElementEdit

​(

Element

e,
int index,

Element

[] removed,

Element

[] added)

Constructs an edit record.

---

#### Constructor Summary

Constructs an edit record.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Element

[]

getChildrenAdded

()

Gets a list of children that were added.

Element

[]

getChildrenRemoved

()

Gets a list of children that were removed.

Element

getElement

()

Returns the underlying element.

int

getIndex

()

Returns the index into the list of elements.

void

redo

()

Redoes a change.

void

undo

()

Undoes a change.

- Methods declared in class javax.swing.undo.

AbstractUndoableEdit

addEdit

,

canRedo

,

canUndo

,

die

,

getPresentationName

,

getRedoPresentationName

,

getUndoPresentationName

,

isSignificant

,

replaceEdit

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

Gets a list of children that were added.

Gets a list of children that were removed.

Returns the underlying element.

Returns the index into the list of elements.

Redoes a change.

Undoes a change.

Methods declared in class javax.swing.undo.

AbstractUndoableEdit

addEdit

,

canRedo

,

canUndo

,

die

,

getPresentationName

,

getRedoPresentationName

,

getUndoPresentationName

,

isSignificant

,

replaceEdit

,

toString

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ElementEdit

```java
public ElementEdit​(
Element
e,
int index,

Element
[] removed,

Element
[] added)
```

Constructs an edit record. This does not modify the element
so it can safely be used to

catch up

a view to the
current model state for views that just attached to a model.

**Parameters:** e

- the element
**Parameters:** index

- the index into the model >= 0
**Parameters:** removed

- a set of elements that were removed
**Parameters:** added

- a set of elements that were added

============ METHOD DETAIL ==========

- Method Detail

- getElement

```java
public
Element
getElement()
```

Returns the underlying element.

**Specified by:** getElement

in interface

DocumentEvent.ElementChange
**Returns:** the element

- getIndex

```java
public int getIndex()
```

Returns the index into the list of elements.

**Specified by:** getIndex

in interface

DocumentEvent.ElementChange
**Returns:** the index >= 0

- getChildrenRemoved

```java
public
Element
[] getChildrenRemoved()
```

Gets a list of children that were removed.

**Specified by:** getChildrenRemoved

in interface

DocumentEvent.ElementChange
**Returns:** the list

- getChildrenAdded

```java
public
Element
[] getChildrenAdded()
```

Gets a list of children that were added.

**Specified by:** getChildrenAdded

in interface

DocumentEvent.ElementChange
**Returns:** the list

- redo

```java
public void redo()
throws
CannotRedoException
```

Redoes a change.

**Specified by:** redo

in interface

UndoableEdit
**Overrides:** redo

in class

AbstractUndoableEdit
**Throws:** CannotRedoException

- if the change cannot be redone
**See Also:** AbstractUndoableEdit.canRedo()

- undo

```java
public void undo()
throws
CannotUndoException
```

Undoes a change.

**Specified by:** undo

in interface

UndoableEdit
**Overrides:** undo

in class

AbstractUndoableEdit
**Throws:** CannotUndoException

- if the change cannot be undone
**See Also:** AbstractUndoableEdit.canUndo()

Constructor Detail

- ElementEdit

```java
public ElementEdit​(
Element
e,
int index,

Element
[] removed,

Element
[] added)
```

Constructs an edit record. This does not modify the element
so it can safely be used to

catch up

a view to the
current model state for views that just attached to a model.

**Parameters:** e

- the element
**Parameters:** index

- the index into the model >= 0
**Parameters:** removed

- a set of elements that were removed
**Parameters:** added

- a set of elements that were added

---

#### Constructor Detail

ElementEdit

```java
public ElementEdit​(
Element
e,
int index,

Element
[] removed,

Element
[] added)
```

Constructs an edit record. This does not modify the element
so it can safely be used to

catch up

a view to the
current model state for views that just attached to a model.

**Parameters:** e

- the element
**Parameters:** index

- the index into the model >= 0
**Parameters:** removed

- a set of elements that were removed
**Parameters:** added

- a set of elements that were added

---

#### ElementEdit

public ElementEdit​(

Element

e,
int index,

Element

[] removed,

Element

[] added)

Constructs an edit record. This does not modify the element
so it can safely be used to

catch up

a view to the
current model state for views that just attached to a model.

Method Detail

- getElement

```java
public
Element
getElement()
```

Returns the underlying element.

**Specified by:** getElement

in interface

DocumentEvent.ElementChange
**Returns:** the element

- getIndex

```java
public int getIndex()
```

Returns the index into the list of elements.

**Specified by:** getIndex

in interface

DocumentEvent.ElementChange
**Returns:** the index >= 0

- getChildrenRemoved

```java
public
Element
[] getChildrenRemoved()
```

Gets a list of children that were removed.

**Specified by:** getChildrenRemoved

in interface

DocumentEvent.ElementChange
**Returns:** the list

- getChildrenAdded

```java
public
Element
[] getChildrenAdded()
```

Gets a list of children that were added.

**Specified by:** getChildrenAdded

in interface

DocumentEvent.ElementChange
**Returns:** the list

- redo

```java
public void redo()
throws
CannotRedoException
```

Redoes a change.

**Specified by:** redo

in interface

UndoableEdit
**Overrides:** redo

in class

AbstractUndoableEdit
**Throws:** CannotRedoException

- if the change cannot be redone
**See Also:** AbstractUndoableEdit.canRedo()

- undo

```java
public void undo()
throws
CannotUndoException
```

Undoes a change.

**Specified by:** undo

in interface

UndoableEdit
**Overrides:** undo

in class

AbstractUndoableEdit
**Throws:** CannotUndoException

- if the change cannot be undone
**See Also:** AbstractUndoableEdit.canUndo()

---

#### Method Detail

getElement

```java
public
Element
getElement()
```

Returns the underlying element.

**Specified by:** getElement

in interface

DocumentEvent.ElementChange
**Returns:** the element

---

#### getElement

public

Element

getElement()

Returns the underlying element.

getIndex

```java
public int getIndex()
```

Returns the index into the list of elements.

**Specified by:** getIndex

in interface

DocumentEvent.ElementChange
**Returns:** the index >= 0

---

#### getIndex

public int getIndex()

Returns the index into the list of elements.

getChildrenRemoved

```java
public
Element
[] getChildrenRemoved()
```

Gets a list of children that were removed.

**Specified by:** getChildrenRemoved

in interface

DocumentEvent.ElementChange
**Returns:** the list

---

#### getChildrenRemoved

public

Element

[] getChildrenRemoved()

Gets a list of children that were removed.

getChildrenAdded

```java
public
Element
[] getChildrenAdded()
```

Gets a list of children that were added.

**Specified by:** getChildrenAdded

in interface

DocumentEvent.ElementChange
**Returns:** the list

---

#### getChildrenAdded

public

Element

[] getChildrenAdded()

Gets a list of children that were added.

redo

```java
public void redo()
throws
CannotRedoException
```

Redoes a change.

**Specified by:** redo

in interface

UndoableEdit
**Overrides:** redo

in class

AbstractUndoableEdit
**Throws:** CannotRedoException

- if the change cannot be redone
**See Also:** AbstractUndoableEdit.canRedo()

---

#### redo

public void redo()
throws

CannotRedoException

Redoes a change.

undo

```java
public void undo()
throws
CannotUndoException
```

Undoes a change.

**Specified by:** undo

in interface

UndoableEdit
**Overrides:** undo

in class

AbstractUndoableEdit
**Throws:** CannotUndoException

- if the change cannot be undone
**See Also:** AbstractUndoableEdit.canUndo()

---

#### undo

public void undo()
throws

CannotUndoException

Undoes a change.

---

