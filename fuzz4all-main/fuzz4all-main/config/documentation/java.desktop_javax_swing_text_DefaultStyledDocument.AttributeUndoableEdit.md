# Class DefaultStyledDocument.AttributeUndoableEdit

**Source:** `java.desktop\javax\swing\text\DefaultStyledDocument.AttributeUndoableEdit.html`

### Class Description

```java
public static class
DefaultStyledDocument.AttributeUndoableEdit

extends
AbstractUndoableEdit
```

An UndoableEdit used to remember AttributeSet changes to an
Element.

**All Implemented Interfaces:** Serializable

,

UndoableEdit

---

### Field Details

#### protected
AttributeSet
newAttributes

AttributeSet containing additional entries, must be non-mutable!

---

#### protected
AttributeSet
copy

Copy of the AttributeSet the Element contained.

---

#### protected boolean isReplacing

true if all the attributes in the element were removed first.

---

#### protected
Element
element

Affected Element.

---

### Constructor Details

#### public AttributeUndoableEdit​(
Element
element,

AttributeSet
newAttributes,
boolean isReplacing)

Constructs an

AttributeUndoableEdit

.

**Parameters:**
- element

- the element
- newAttributes

- the new attributes
- isReplacing

- true if all the attributes in the element were removed first.

---

### Method Details

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

#### Class DefaultStyledDocument.AttributeUndoableEdit

java.lang.Object

- javax.swing.undo.AbstractUndoableEdit
- - javax.swing.text.DefaultStyledDocument.AttributeUndoableEdit

javax.swing.undo.AbstractUndoableEdit

- javax.swing.text.DefaultStyledDocument.AttributeUndoableEdit

javax.swing.text.DefaultStyledDocument.AttributeUndoableEdit

**All Implemented Interfaces:** Serializable

,

UndoableEdit

**Enclosing class:** DefaultStyledDocument

```java
public static class
DefaultStyledDocument.AttributeUndoableEdit

extends
AbstractUndoableEdit
```

An UndoableEdit used to remember AttributeSet changes to an
Element.

**See Also:** Serialized Form

public static class

DefaultStyledDocument.AttributeUndoableEdit

extends

AbstractUndoableEdit

An UndoableEdit used to remember AttributeSet changes to an
Element.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

AttributeSet

copy

Copy of the AttributeSet the Element contained.

protected

Element

element

Affected Element.

protected boolean

isReplacing

true if all the attributes in the element were removed first.

protected

AttributeSet

newAttributes

AttributeSet containing additional entries, must be non-mutable!

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

AttributeUndoableEdit

​(

Element

element,

AttributeSet

newAttributes,
boolean isReplacing)

Constructs an

AttributeUndoableEdit

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

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

Fields

Modifier and Type

Field

Description

protected

AttributeSet

copy

Copy of the AttributeSet the Element contained.

protected

Element

element

Affected Element.

protected boolean

isReplacing

true if all the attributes in the element were removed first.

protected

AttributeSet

newAttributes

AttributeSet containing additional entries, must be non-mutable!

- Fields declared in class javax.swing.undo.

AbstractUndoableEdit

RedoName

,

UndoName

---

#### Field Summary

Copy of the AttributeSet the Element contained.

Affected Element.

true if all the attributes in the element were removed first.

AttributeSet containing additional entries, must be non-mutable!

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

AttributeUndoableEdit

​(

Element

element,

AttributeSet

newAttributes,
boolean isReplacing)

Constructs an

AttributeUndoableEdit

.

---

#### Constructor Summary

Constructs an

AttributeUndoableEdit

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

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

============ FIELD DETAIL ===========

- Field Detail

- newAttributes

```java
protected
AttributeSet
newAttributes
```

AttributeSet containing additional entries, must be non-mutable!

- copy

```java
protected
AttributeSet
copy
```

Copy of the AttributeSet the Element contained.

- isReplacing

```java
protected boolean isReplacing
```

true if all the attributes in the element were removed first.

- element

```java
protected
Element
element
```

Affected Element.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AttributeUndoableEdit

```java
public AttributeUndoableEdit​(
Element
element,

AttributeSet
newAttributes,
boolean isReplacing)
```

Constructs an

AttributeUndoableEdit

.

**Parameters:** element

- the element
**Parameters:** newAttributes

- the new attributes
**Parameters:** isReplacing

- true if all the attributes in the element were removed first.

============ METHOD DETAIL ==========

- Method Detail

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

Field Detail

- newAttributes

```java
protected
AttributeSet
newAttributes
```

AttributeSet containing additional entries, must be non-mutable!

- copy

```java
protected
AttributeSet
copy
```

Copy of the AttributeSet the Element contained.

- isReplacing

```java
protected boolean isReplacing
```

true if all the attributes in the element were removed first.

- element

```java
protected
Element
element
```

Affected Element.

---

#### Field Detail

newAttributes

```java
protected
AttributeSet
newAttributes
```

AttributeSet containing additional entries, must be non-mutable!

---

#### newAttributes

protected

AttributeSet

newAttributes

AttributeSet containing additional entries, must be non-mutable!

copy

```java
protected
AttributeSet
copy
```

Copy of the AttributeSet the Element contained.

---

#### copy

protected

AttributeSet

copy

Copy of the AttributeSet the Element contained.

isReplacing

```java
protected boolean isReplacing
```

true if all the attributes in the element were removed first.

---

#### isReplacing

protected boolean isReplacing

true if all the attributes in the element were removed first.

element

```java
protected
Element
element
```

Affected Element.

---

#### element

protected

Element

element

Affected Element.

Constructor Detail

- AttributeUndoableEdit

```java
public AttributeUndoableEdit​(
Element
element,

AttributeSet
newAttributes,
boolean isReplacing)
```

Constructs an

AttributeUndoableEdit

.

**Parameters:** element

- the element
**Parameters:** newAttributes

- the new attributes
**Parameters:** isReplacing

- true if all the attributes in the element were removed first.

---

#### Constructor Detail

AttributeUndoableEdit

```java
public AttributeUndoableEdit​(
Element
element,

AttributeSet
newAttributes,
boolean isReplacing)
```

Constructs an

AttributeUndoableEdit

.

**Parameters:** element

- the element
**Parameters:** newAttributes

- the new attributes
**Parameters:** isReplacing

- true if all the attributes in the element were removed first.

---

#### AttributeUndoableEdit

public AttributeUndoableEdit​(

Element

element,

AttributeSet

newAttributes,
boolean isReplacing)

Constructs an

AttributeUndoableEdit

.

Method Detail

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

