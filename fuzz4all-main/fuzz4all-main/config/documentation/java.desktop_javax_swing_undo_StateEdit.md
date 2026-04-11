# Class StateEdit

**Source:** `java.desktop\javax\swing\undo\StateEdit.html`

### Class Description

```java
public class
StateEdit

extends
AbstractUndoableEdit
```

StateEdit is a general edit for objects that change state.
Objects being edited must conform to the StateEditable interface.

This edit class works by asking an object to store it's state in
Hashtables before and after editing occurs. Upon undo or redo the
object is told to restore it's state from these Hashtables.

A state edit is used as follows:

```java
// Create the edit during the "before" state of the object
StateEdit newEdit = new StateEdit(myObject);
// Modify the object
myObject.someStateModifyingMethod();
// "end" the edit when you are done modifying the object
newEdit.end();
```

Note that when a StateEdit ends, it removes redundant state from
the Hashtables - A state Hashtable is not guaranteed to contain all
keys/values placed into it when the state is stored!

**All Implemented Interfaces:** Serializable

,

UndoableEdit

---

### Field Details

#### protected static final
String
RCSID

Obsolete RCS version identity.

**See Also:**
- Constant Field Values

---

#### protected
StateEditable
object

The object being edited

---

#### protected
Hashtable
<
Object
,​
Object
> preState

The state information prior to the edit

---

#### protected
Hashtable
<
Object
,​
Object
> postState

The state information after the edit

---

#### protected
String
undoRedoName

The undo/redo presentation name

---

### Constructor Details

#### public StateEdit​(
StateEditable
anObject)

Create and return a new StateEdit.

**Parameters:**
- anObject

- The object to watch for changing state

**See Also:**
- StateEdit

---

#### public StateEdit​(
StateEditable
anObject,

String
name)

Create and return a new StateEdit with a presentation name.

**Parameters:**
- anObject

- The object to watch for changing state
- name

- The presentation name to be used for this edit

**See Also:**
- StateEdit

---

### Method Details

#### protected void init​(
StateEditable
anObject,

String
name)

Initialize the state edit.

**Parameters:**
- anObject

- The object to watch for changing state
- name

- The presentation name to be used for this edit

---

#### public void end()

Gets the post-edit state of the StateEditable object and
ends the edit.

---

#### public void undo()

Tells the edited object to apply the state prior to the edit

**Specified by:**
- undo

in interface

UndoableEdit

**Overrides:**
- undo

in class

AbstractUndoableEdit

**See Also:**
- AbstractUndoableEdit.canUndo()

---

#### public void redo()

Tells the edited object to apply the state after the edit

**Specified by:**
- redo

in interface

UndoableEdit

**Overrides:**
- redo

in class

AbstractUndoableEdit

**See Also:**
- AbstractUndoableEdit.canRedo()

---

#### public
String
getPresentationName()

Gets the presentation name for this edit

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

#### protected void removeRedundantState()

Remove redundant key/values in state hashtables.

---

### Additional Sections

#### Class StateEdit

java.lang.Object

- javax.swing.undo.AbstractUndoableEdit
- - javax.swing.undo.StateEdit

javax.swing.undo.AbstractUndoableEdit

- javax.swing.undo.StateEdit

javax.swing.undo.StateEdit

**All Implemented Interfaces:** Serializable

,

UndoableEdit

```java
public class
StateEdit

extends
AbstractUndoableEdit
```

StateEdit is a general edit for objects that change state.
Objects being edited must conform to the StateEditable interface.

This edit class works by asking an object to store it's state in
Hashtables before and after editing occurs. Upon undo or redo the
object is told to restore it's state from these Hashtables.

A state edit is used as follows:

```java
// Create the edit during the "before" state of the object
StateEdit newEdit = new StateEdit(myObject);
// Modify the object
myObject.someStateModifyingMethod();
// "end" the edit when you are done modifying the object
newEdit.end();
```

Note that when a StateEdit ends, it removes redundant state from
the Hashtables - A state Hashtable is not guaranteed to contain all
keys/values placed into it when the state is stored!

**See Also:** StateEditable

,

Serialized Form

public class

StateEdit

extends

AbstractUndoableEdit

StateEdit is a general edit for objects that change state.
Objects being edited must conform to the StateEditable interface.

This edit class works by asking an object to store it's state in
Hashtables before and after editing occurs. Upon undo or redo the
object is told to restore it's state from these Hashtables.

A state edit is used as follows:

```java
// Create the edit during the "before" state of the object
StateEdit newEdit = new StateEdit(myObject);
// Modify the object
myObject.someStateModifyingMethod();
// "end" the edit when you are done modifying the object
newEdit.end();
```

Note that when a StateEdit ends, it removes redundant state from
the Hashtables - A state Hashtable is not guaranteed to contain all
keys/values placed into it when the state is stored!

StateEdit is a general edit for objects that change state.
Objects being edited must conform to the StateEditable interface.

This edit class works by asking an object to store it's state in
Hashtables before and after editing occurs. Upon undo or redo the
object is told to restore it's state from these Hashtables.

// Create the edit during the "before" state of the object
StateEdit newEdit = new StateEdit(myObject);
// Modify the object
myObject.someStateModifyingMethod();
// "end" the edit when you are done modifying the object
newEdit.end();

Note that when a StateEdit ends, it removes redundant state from
the Hashtables - A state Hashtable is not guaranteed to contain all
keys/values placed into it when the state is stored!

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

StateEditable

object

The object being edited

protected

Hashtable

<

Object

,​

Object

>

postState

The state information after the edit

protected

Hashtable

<

Object

,​

Object

>

preState

The state information prior to the edit

protected static

String

RCSID

Obsolete RCS version identity.

protected

String

undoRedoName

The undo/redo presentation name

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

StateEdit

​(

StateEditable

anObject)

Create and return a new StateEdit.

StateEdit

​(

StateEditable

anObject,

String

name)

Create and return a new StateEdit with a presentation name.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

end

()

Gets the post-edit state of the StateEditable object and
ends the edit.

String

getPresentationName

()

Gets the presentation name for this edit

protected void

init

​(

StateEditable

anObject,

String

name)

Initialize the state edit.

void

redo

()

Tells the edited object to apply the state after the edit

protected void

removeRedundantState

()

Remove redundant key/values in state hashtables.

void

undo

()

Tells the edited object to apply the state prior to the edit

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

StateEditable

object

The object being edited

protected

Hashtable

<

Object

,​

Object

>

postState

The state information after the edit

protected

Hashtable

<

Object

,​

Object

>

preState

The state information prior to the edit

protected static

String

RCSID

Obsolete RCS version identity.

protected

String

undoRedoName

The undo/redo presentation name

- Fields declared in class javax.swing.undo.

AbstractUndoableEdit

RedoName

,

UndoName

---

#### Field Summary

The object being edited

The state information after the edit

The state information prior to the edit

Obsolete RCS version identity.

The undo/redo presentation name

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

StateEdit

​(

StateEditable

anObject)

Create and return a new StateEdit.

StateEdit

​(

StateEditable

anObject,

String

name)

Create and return a new StateEdit with a presentation name.

---

#### Constructor Summary

Create and return a new StateEdit.

Create and return a new StateEdit with a presentation name.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

end

()

Gets the post-edit state of the StateEditable object and
ends the edit.

String

getPresentationName

()

Gets the presentation name for this edit

protected void

init

​(

StateEditable

anObject,

String

name)

Initialize the state edit.

void

redo

()

Tells the edited object to apply the state after the edit

protected void

removeRedundantState

()

Remove redundant key/values in state hashtables.

void

undo

()

Tells the edited object to apply the state prior to the edit

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

Gets the post-edit state of the StateEditable object and
ends the edit.

Gets the presentation name for this edit

Initialize the state edit.

Tells the edited object to apply the state after the edit

Remove redundant key/values in state hashtables.

Tells the edited object to apply the state prior to the edit

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

- RCSID

```java
protected static final
String
RCSID
```

Obsolete RCS version identity.

**See Also:** Constant Field Values

- object

```java
protected
StateEditable
object
```

The object being edited

- preState

```java
protected
Hashtable
<
Object
,​
Object
> preState
```

The state information prior to the edit

- postState

```java
protected
Hashtable
<
Object
,​
Object
> postState
```

The state information after the edit

- undoRedoName

```java
protected
String
undoRedoName
```

The undo/redo presentation name

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- StateEdit

```java
public StateEdit​(
StateEditable
anObject)
```

Create and return a new StateEdit.

**Parameters:** anObject

- The object to watch for changing state
**See Also:** StateEdit

- StateEdit

```java
public StateEdit​(
StateEditable
anObject,

String
name)
```

Create and return a new StateEdit with a presentation name.

**Parameters:** anObject

- The object to watch for changing state
**Parameters:** name

- The presentation name to be used for this edit
**See Also:** StateEdit

============ METHOD DETAIL ==========

- Method Detail

- init

```java
protected void init​(
StateEditable
anObject,

String
name)
```

Initialize the state edit.

**Parameters:** anObject

- The object to watch for changing state
**Parameters:** name

- The presentation name to be used for this edit

- end

```java
public void end()
```

Gets the post-edit state of the StateEditable object and
ends the edit.

- undo

```java
public void undo()
```

Tells the edited object to apply the state prior to the edit

**Specified by:** undo

in interface

UndoableEdit
**Overrides:** undo

in class

AbstractUndoableEdit
**See Also:** AbstractUndoableEdit.canUndo()

- redo

```java
public void redo()
```

Tells the edited object to apply the state after the edit

**Specified by:** redo

in interface

UndoableEdit
**Overrides:** redo

in class

AbstractUndoableEdit
**See Also:** AbstractUndoableEdit.canRedo()

- getPresentationName

```java
public
String
getPresentationName()
```

Gets the presentation name for this edit

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

- removeRedundantState

```java
protected void removeRedundantState()
```

Remove redundant key/values in state hashtables.

Field Detail

- RCSID

```java
protected static final
String
RCSID
```

Obsolete RCS version identity.

**See Also:** Constant Field Values

- object

```java
protected
StateEditable
object
```

The object being edited

- preState

```java
protected
Hashtable
<
Object
,​
Object
> preState
```

The state information prior to the edit

- postState

```java
protected
Hashtable
<
Object
,​
Object
> postState
```

The state information after the edit

- undoRedoName

```java
protected
String
undoRedoName
```

The undo/redo presentation name

---

#### Field Detail

RCSID

```java
protected static final
String
RCSID
```

Obsolete RCS version identity.

**See Also:** Constant Field Values

---

#### RCSID

protected static final

String

RCSID

Obsolete RCS version identity.

object

```java
protected
StateEditable
object
```

The object being edited

---

#### object

protected

StateEditable

object

The object being edited

preState

```java
protected
Hashtable
<
Object
,​
Object
> preState
```

The state information prior to the edit

---

#### preState

protected

Hashtable

<

Object

,​

Object

> preState

The state information prior to the edit

postState

```java
protected
Hashtable
<
Object
,​
Object
> postState
```

The state information after the edit

---

#### postState

protected

Hashtable

<

Object

,​

Object

> postState

The state information after the edit

undoRedoName

```java
protected
String
undoRedoName
```

The undo/redo presentation name

---

#### undoRedoName

protected

String

undoRedoName

The undo/redo presentation name

Constructor Detail

- StateEdit

```java
public StateEdit​(
StateEditable
anObject)
```

Create and return a new StateEdit.

**Parameters:** anObject

- The object to watch for changing state
**See Also:** StateEdit

- StateEdit

```java
public StateEdit​(
StateEditable
anObject,

String
name)
```

Create and return a new StateEdit with a presentation name.

**Parameters:** anObject

- The object to watch for changing state
**Parameters:** name

- The presentation name to be used for this edit
**See Also:** StateEdit

---

#### Constructor Detail

StateEdit

```java
public StateEdit​(
StateEditable
anObject)
```

Create and return a new StateEdit.

**Parameters:** anObject

- The object to watch for changing state
**See Also:** StateEdit

---

#### StateEdit

public StateEdit​(

StateEditable

anObject)

Create and return a new StateEdit.

StateEdit

```java
public StateEdit​(
StateEditable
anObject,

String
name)
```

Create and return a new StateEdit with a presentation name.

**Parameters:** anObject

- The object to watch for changing state
**Parameters:** name

- The presentation name to be used for this edit
**See Also:** StateEdit

---

#### StateEdit

public StateEdit​(

StateEditable

anObject,

String

name)

Create and return a new StateEdit with a presentation name.

Method Detail

- init

```java
protected void init​(
StateEditable
anObject,

String
name)
```

Initialize the state edit.

**Parameters:** anObject

- The object to watch for changing state
**Parameters:** name

- The presentation name to be used for this edit

- end

```java
public void end()
```

Gets the post-edit state of the StateEditable object and
ends the edit.

- undo

```java
public void undo()
```

Tells the edited object to apply the state prior to the edit

**Specified by:** undo

in interface

UndoableEdit
**Overrides:** undo

in class

AbstractUndoableEdit
**See Also:** AbstractUndoableEdit.canUndo()

- redo

```java
public void redo()
```

Tells the edited object to apply the state after the edit

**Specified by:** redo

in interface

UndoableEdit
**Overrides:** redo

in class

AbstractUndoableEdit
**See Also:** AbstractUndoableEdit.canRedo()

- getPresentationName

```java
public
String
getPresentationName()
```

Gets the presentation name for this edit

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

- removeRedundantState

```java
protected void removeRedundantState()
```

Remove redundant key/values in state hashtables.

---

#### Method Detail

init

```java
protected void init​(
StateEditable
anObject,

String
name)
```

Initialize the state edit.

**Parameters:** anObject

- The object to watch for changing state
**Parameters:** name

- The presentation name to be used for this edit

---

#### init

protected void init​(

StateEditable

anObject,

String

name)

Initialize the state edit.

end

```java
public void end()
```

Gets the post-edit state of the StateEditable object and
ends the edit.

---

#### end

public void end()

Gets the post-edit state of the StateEditable object and
ends the edit.

undo

```java
public void undo()
```

Tells the edited object to apply the state prior to the edit

**Specified by:** undo

in interface

UndoableEdit
**Overrides:** undo

in class

AbstractUndoableEdit
**See Also:** AbstractUndoableEdit.canUndo()

---

#### undo

public void undo()

Tells the edited object to apply the state prior to the edit

redo

```java
public void redo()
```

Tells the edited object to apply the state after the edit

**Specified by:** redo

in interface

UndoableEdit
**Overrides:** redo

in class

AbstractUndoableEdit
**See Also:** AbstractUndoableEdit.canRedo()

---

#### redo

public void redo()

Tells the edited object to apply the state after the edit

getPresentationName

```java
public
String
getPresentationName()
```

Gets the presentation name for this edit

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

Gets the presentation name for this edit

removeRedundantState

```java
protected void removeRedundantState()
```

Remove redundant key/values in state hashtables.

---

#### removeRedundantState

protected void removeRedundantState()

Remove redundant key/values in state hashtables.

---

