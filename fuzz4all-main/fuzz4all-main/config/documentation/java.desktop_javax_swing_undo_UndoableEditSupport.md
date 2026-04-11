# Class UndoableEditSupport

**Source:** `java.desktop\javax\swing\undo\UndoableEditSupport.html`

### Class Description

```java
public class
UndoableEditSupport

extends
Object
```

A support class used for managing

UndoableEdit

listeners.

---

### Field Details

#### protected int updateLevel

The update level.

---

#### protected
CompoundEdit
compoundEdit

The compound edit.

---

#### protected
Vector
<
UndoableEditListener
> listeners

The list of listeners.

---

#### protected
Object
realSource

The real source.

---

### Constructor Details

#### public UndoableEditSupport()

Constructs an

UndoableEditSupport

object.

---

#### public UndoableEditSupport​(
Object
r)

Constructs an

UndoableEditSupport

object.

**Parameters:**
- r

- an

Object

---

### Method Details

#### public void addUndoableEditListener​(
UndoableEditListener
l)

Registers an

UndoableEditListener

.
The listener is notified whenever an edit occurs which can be undone.

**Parameters:**
- l

- an

UndoableEditListener

object

**See Also:**
- removeUndoableEditListener(javax.swing.event.UndoableEditListener)

---

#### public void removeUndoableEditListener​(
UndoableEditListener
l)

Removes an

UndoableEditListener

.

**Parameters:**
- l

- the

UndoableEditListener

object to be removed

**See Also:**
- addUndoableEditListener(javax.swing.event.UndoableEditListener)

---

#### public
UndoableEditListener
[] getUndoableEditListeners()

Returns an array of all the

UndoableEditListener

s added
to this UndoableEditSupport with addUndoableEditListener().

**Returns:**
- all of the

UndoableEditListener

s added or an empty
array if no listeners have been added

**Since:**
- 1.4

---

#### protected void _postEdit​(
UndoableEdit
e)

Called only from

postEdit

and

endUpdate

. Calls

undoableEditHappened

in all listeners. No synchronization
is performed here, since the two calling methods are synchronized.

**Parameters:**
- e

- edit to be verified

---

#### public void postEdit​(
UndoableEdit
e)

DEADLOCK WARNING: Calling this method may call

undoableEditHappened

in all listeners.
It is unwise to call this method from one of its listeners.

**Parameters:**
- e

- edit to be posted

---

#### public int getUpdateLevel()

Returns the update level value.

**Returns:**
- an integer representing the update level

---

#### public void beginUpdate()

*No description found.*

---

#### protected
CompoundEdit
createCompoundEdit()

Called only from

beginUpdate

.
Exposed here for subclasses' use.

**Returns:**
- new created

CompoundEdit

object

---

#### public void endUpdate()

DEADLOCK WARNING: Calling this method may call

undoableEditHappened

in all listeners.
It is unwise to call this method from one of its listeners.

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
- a

String

representation of this object

---

### Additional Sections

#### Class UndoableEditSupport

java.lang.Object

- javax.swing.undo.UndoableEditSupport

javax.swing.undo.UndoableEditSupport

```java
public class
UndoableEditSupport

extends
Object
```

A support class used for managing

UndoableEdit

listeners.

public class

UndoableEditSupport

extends

Object

A support class used for managing

UndoableEdit

listeners.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

CompoundEdit

compoundEdit

The compound edit.

protected

Vector

<

UndoableEditListener

>

listeners

The list of listeners.

protected

Object

realSource

The real source.

protected int

updateLevel

The update level.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

UndoableEditSupport

()

Constructs an

UndoableEditSupport

object.

UndoableEditSupport

​(

Object

r)

Constructs an

UndoableEditSupport

object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

_postEdit

​(

UndoableEdit

e)

Called only from

postEdit

and

endUpdate

.

void

addUndoableEditListener

​(

UndoableEditListener

l)

Registers an

UndoableEditListener

.

void

beginUpdate

()

protected

CompoundEdit

createCompoundEdit

()

Called only from

beginUpdate

.

void

endUpdate

()

DEADLOCK WARNING: Calling this method may call

undoableEditHappened

in all listeners.

UndoableEditListener

[]

getUndoableEditListeners

()

Returns an array of all the

UndoableEditListener

s added
to this UndoableEditSupport with addUndoableEditListener().

int

getUpdateLevel

()

Returns the update level value.

void

postEdit

​(

UndoableEdit

e)

DEADLOCK WARNING: Calling this method may call

undoableEditHappened

in all listeners.

void

removeUndoableEditListener

​(

UndoableEditListener

l)

Removes an

UndoableEditListener

.

String

toString

()

Returns a string that displays and identifies this
object's properties.

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

CompoundEdit

compoundEdit

The compound edit.

protected

Vector

<

UndoableEditListener

>

listeners

The list of listeners.

protected

Object

realSource

The real source.

protected int

updateLevel

The update level.

---

#### Field Summary

The compound edit.

The list of listeners.

The real source.

The update level.

Constructor Summary

Constructors

Constructor

Description

UndoableEditSupport

()

Constructs an

UndoableEditSupport

object.

UndoableEditSupport

​(

Object

r)

Constructs an

UndoableEditSupport

object.

---

#### Constructor Summary

Constructs an

UndoableEditSupport

object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

_postEdit

​(

UndoableEdit

e)

Called only from

postEdit

and

endUpdate

.

void

addUndoableEditListener

​(

UndoableEditListener

l)

Registers an

UndoableEditListener

.

void

beginUpdate

()

protected

CompoundEdit

createCompoundEdit

()

Called only from

beginUpdate

.

void

endUpdate

()

DEADLOCK WARNING: Calling this method may call

undoableEditHappened

in all listeners.

UndoableEditListener

[]

getUndoableEditListeners

()

Returns an array of all the

UndoableEditListener

s added
to this UndoableEditSupport with addUndoableEditListener().

int

getUpdateLevel

()

Returns the update level value.

void

postEdit

​(

UndoableEdit

e)

DEADLOCK WARNING: Calling this method may call

undoableEditHappened

in all listeners.

void

removeUndoableEditListener

​(

UndoableEditListener

l)

Removes an

UndoableEditListener

.

String

toString

()

Returns a string that displays and identifies this
object's properties.

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

Called only from

postEdit

and

endUpdate

.

Registers an

UndoableEditListener

.

Called only from

beginUpdate

.

DEADLOCK WARNING: Calling this method may call

undoableEditHappened

in all listeners.

Returns an array of all the

UndoableEditListener

s added
to this UndoableEditSupport with addUndoableEditListener().

Returns the update level value.

Removes an

UndoableEditListener

.

Returns a string that displays and identifies this
object's properties.

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

- updateLevel

```java
protected int updateLevel
```

The update level.

- compoundEdit

```java
protected
CompoundEdit
compoundEdit
```

The compound edit.

- listeners

```java
protected
Vector
<
UndoableEditListener
> listeners
```

The list of listeners.

- realSource

```java
protected
Object
realSource
```

The real source.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- UndoableEditSupport

```java
public UndoableEditSupport()
```

Constructs an

UndoableEditSupport

object.

- UndoableEditSupport

```java
public UndoableEditSupport​(
Object
r)
```

Constructs an

UndoableEditSupport

object.

**Parameters:** r

- an

Object

============ METHOD DETAIL ==========

- Method Detail

- addUndoableEditListener

```java
public void addUndoableEditListener​(
UndoableEditListener
l)
```

Registers an

UndoableEditListener

.
The listener is notified whenever an edit occurs which can be undone.

**Parameters:** l

- an

UndoableEditListener

object
**See Also:** removeUndoableEditListener(javax.swing.event.UndoableEditListener)

- removeUndoableEditListener

```java
public void removeUndoableEditListener​(
UndoableEditListener
l)
```

Removes an

UndoableEditListener

.

**Parameters:** l

- the

UndoableEditListener

object to be removed
**See Also:** addUndoableEditListener(javax.swing.event.UndoableEditListener)

- getUndoableEditListeners

```java
public
UndoableEditListener
[] getUndoableEditListeners()
```

Returns an array of all the

UndoableEditListener

s added
to this UndoableEditSupport with addUndoableEditListener().

**Returns:** all of the

UndoableEditListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- _postEdit

```java
protected void _postEdit​(
UndoableEdit
e)
```

Called only from

postEdit

and

endUpdate

. Calls

undoableEditHappened

in all listeners. No synchronization
is performed here, since the two calling methods are synchronized.

**Parameters:** e

- edit to be verified

- postEdit

```java
public void postEdit​(
UndoableEdit
e)
```

DEADLOCK WARNING: Calling this method may call

undoableEditHappened

in all listeners.
It is unwise to call this method from one of its listeners.

**Parameters:** e

- edit to be posted

- getUpdateLevel

```java
public int getUpdateLevel()
```

Returns the update level value.

**Returns:** an integer representing the update level

- beginUpdate

```java
public void beginUpdate()
```

- createCompoundEdit

```java
protected
CompoundEdit
createCompoundEdit()
```

Called only from

beginUpdate

.
Exposed here for subclasses' use.

**Returns:** new created

CompoundEdit

object

- endUpdate

```java
public void endUpdate()
```

DEADLOCK WARNING: Calling this method may call

undoableEditHappened

in all listeners.
It is unwise to call this method from one of its listeners.

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
**Returns:** a

String

representation of this object

Field Detail

- updateLevel

```java
protected int updateLevel
```

The update level.

- compoundEdit

```java
protected
CompoundEdit
compoundEdit
```

The compound edit.

- listeners

```java
protected
Vector
<
UndoableEditListener
> listeners
```

The list of listeners.

- realSource

```java
protected
Object
realSource
```

The real source.

---

#### Field Detail

updateLevel

```java
protected int updateLevel
```

The update level.

---

#### updateLevel

protected int updateLevel

The update level.

compoundEdit

```java
protected
CompoundEdit
compoundEdit
```

The compound edit.

---

#### compoundEdit

protected

CompoundEdit

compoundEdit

The compound edit.

listeners

```java
protected
Vector
<
UndoableEditListener
> listeners
```

The list of listeners.

---

#### listeners

protected

Vector

<

UndoableEditListener

> listeners

The list of listeners.

realSource

```java
protected
Object
realSource
```

The real source.

---

#### realSource

protected

Object

realSource

The real source.

Constructor Detail

- UndoableEditSupport

```java
public UndoableEditSupport()
```

Constructs an

UndoableEditSupport

object.

- UndoableEditSupport

```java
public UndoableEditSupport​(
Object
r)
```

Constructs an

UndoableEditSupport

object.

**Parameters:** r

- an

Object

---

#### Constructor Detail

UndoableEditSupport

```java
public UndoableEditSupport()
```

Constructs an

UndoableEditSupport

object.

---

#### UndoableEditSupport

public UndoableEditSupport()

Constructs an

UndoableEditSupport

object.

UndoableEditSupport

```java
public UndoableEditSupport​(
Object
r)
```

Constructs an

UndoableEditSupport

object.

**Parameters:** r

- an

Object

---

#### UndoableEditSupport

public UndoableEditSupport​(

Object

r)

Constructs an

UndoableEditSupport

object.

Method Detail

- addUndoableEditListener

```java
public void addUndoableEditListener​(
UndoableEditListener
l)
```

Registers an

UndoableEditListener

.
The listener is notified whenever an edit occurs which can be undone.

**Parameters:** l

- an

UndoableEditListener

object
**See Also:** removeUndoableEditListener(javax.swing.event.UndoableEditListener)

- removeUndoableEditListener

```java
public void removeUndoableEditListener​(
UndoableEditListener
l)
```

Removes an

UndoableEditListener

.

**Parameters:** l

- the

UndoableEditListener

object to be removed
**See Also:** addUndoableEditListener(javax.swing.event.UndoableEditListener)

- getUndoableEditListeners

```java
public
UndoableEditListener
[] getUndoableEditListeners()
```

Returns an array of all the

UndoableEditListener

s added
to this UndoableEditSupport with addUndoableEditListener().

**Returns:** all of the

UndoableEditListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- _postEdit

```java
protected void _postEdit​(
UndoableEdit
e)
```

Called only from

postEdit

and

endUpdate

. Calls

undoableEditHappened

in all listeners. No synchronization
is performed here, since the two calling methods are synchronized.

**Parameters:** e

- edit to be verified

- postEdit

```java
public void postEdit​(
UndoableEdit
e)
```

DEADLOCK WARNING: Calling this method may call

undoableEditHappened

in all listeners.
It is unwise to call this method from one of its listeners.

**Parameters:** e

- edit to be posted

- getUpdateLevel

```java
public int getUpdateLevel()
```

Returns the update level value.

**Returns:** an integer representing the update level

- beginUpdate

```java
public void beginUpdate()
```

- createCompoundEdit

```java
protected
CompoundEdit
createCompoundEdit()
```

Called only from

beginUpdate

.
Exposed here for subclasses' use.

**Returns:** new created

CompoundEdit

object

- endUpdate

```java
public void endUpdate()
```

DEADLOCK WARNING: Calling this method may call

undoableEditHappened

in all listeners.
It is unwise to call this method from one of its listeners.

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
**Returns:** a

String

representation of this object

---

#### Method Detail

addUndoableEditListener

```java
public void addUndoableEditListener​(
UndoableEditListener
l)
```

Registers an

UndoableEditListener

.
The listener is notified whenever an edit occurs which can be undone.

**Parameters:** l

- an

UndoableEditListener

object
**See Also:** removeUndoableEditListener(javax.swing.event.UndoableEditListener)

---

#### addUndoableEditListener

public void addUndoableEditListener​(

UndoableEditListener

l)

Registers an

UndoableEditListener

.
The listener is notified whenever an edit occurs which can be undone.

removeUndoableEditListener

```java
public void removeUndoableEditListener​(
UndoableEditListener
l)
```

Removes an

UndoableEditListener

.

**Parameters:** l

- the

UndoableEditListener

object to be removed
**See Also:** addUndoableEditListener(javax.swing.event.UndoableEditListener)

---

#### removeUndoableEditListener

public void removeUndoableEditListener​(

UndoableEditListener

l)

Removes an

UndoableEditListener

.

getUndoableEditListeners

```java
public
UndoableEditListener
[] getUndoableEditListeners()
```

Returns an array of all the

UndoableEditListener

s added
to this UndoableEditSupport with addUndoableEditListener().

**Returns:** all of the

UndoableEditListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

---

#### getUndoableEditListeners

public

UndoableEditListener

[] getUndoableEditListeners()

Returns an array of all the

UndoableEditListener

s added
to this UndoableEditSupport with addUndoableEditListener().

_postEdit

```java
protected void _postEdit​(
UndoableEdit
e)
```

Called only from

postEdit

and

endUpdate

. Calls

undoableEditHappened

in all listeners. No synchronization
is performed here, since the two calling methods are synchronized.

**Parameters:** e

- edit to be verified

---

#### _postEdit

protected void _postEdit​(

UndoableEdit

e)

Called only from

postEdit

and

endUpdate

. Calls

undoableEditHappened

in all listeners. No synchronization
is performed here, since the two calling methods are synchronized.

postEdit

```java
public void postEdit​(
UndoableEdit
e)
```

DEADLOCK WARNING: Calling this method may call

undoableEditHappened

in all listeners.
It is unwise to call this method from one of its listeners.

**Parameters:** e

- edit to be posted

---

#### postEdit

public void postEdit​(

UndoableEdit

e)

DEADLOCK WARNING: Calling this method may call

undoableEditHappened

in all listeners.
It is unwise to call this method from one of its listeners.

getUpdateLevel

```java
public int getUpdateLevel()
```

Returns the update level value.

**Returns:** an integer representing the update level

---

#### getUpdateLevel

public int getUpdateLevel()

Returns the update level value.

beginUpdate

```java
public void beginUpdate()
```

---

#### beginUpdate

public void beginUpdate()

createCompoundEdit

```java
protected
CompoundEdit
createCompoundEdit()
```

Called only from

beginUpdate

.
Exposed here for subclasses' use.

**Returns:** new created

CompoundEdit

object

---

#### createCompoundEdit

protected

CompoundEdit

createCompoundEdit()

Called only from

beginUpdate

.
Exposed here for subclasses' use.

endUpdate

```java
public void endUpdate()
```

DEADLOCK WARNING: Calling this method may call

undoableEditHappened

in all listeners.
It is unwise to call this method from one of its listeners.

---

#### endUpdate

public void endUpdate()

DEADLOCK WARNING: Calling this method may call

undoableEditHappened

in all listeners.
It is unwise to call this method from one of its listeners.

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
**Returns:** a

String

representation of this object

---

#### toString

public

String

toString()

Returns a string that displays and identifies this
object's properties.

---

