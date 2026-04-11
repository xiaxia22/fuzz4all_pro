# Class UndoableEditEvent

**Source:** `java.desktop\javax\swing\event\UndoableEditEvent.html`

### Class Description

```java
public class
UndoableEditEvent

extends
EventObject
```

An event indicating that an operation which can be undone has occurred.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public UndoableEditEvent​(
Object
source,

UndoableEdit
edit)

Constructs an UndoableEditEvent object.

**Parameters:**
- source

- the Object that originated the event
(typically

this

)
- edit

- an UndoableEdit object

---

### Method Details

#### public
UndoableEdit
getEdit()

Returns the edit value.

**Returns:**
- the UndoableEdit object encapsulating the edit

---

### Additional Sections

#### Class UndoableEditEvent

java.lang.Object

- java.util.EventObject
- - javax.swing.event.UndoableEditEvent

java.util.EventObject

- javax.swing.event.UndoableEditEvent

javax.swing.event.UndoableEditEvent

**All Implemented Interfaces:** Serializable

```java
public class
UndoableEditEvent

extends
EventObject
```

An event indicating that an operation which can be undone has occurred.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**See Also:** Serialized Form

public class

UndoableEditEvent

extends

EventObject

An event indicating that an operation which can be undone has occurred.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.util.

EventObject

source

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

UndoableEditEvent

​(

Object

source,

UndoableEdit

edit)

Constructs an UndoableEditEvent object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

UndoableEdit

getEdit

()

Returns the edit value.

- Methods declared in class java.util.

EventObject

getSource

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

- Fields declared in class java.util.

EventObject

source

---

#### Field Summary

Fields declared in class java.util.

EventObject

source

---

#### Fields declared in class java.util. EventObject

Constructor Summary

Constructors

Constructor

Description

UndoableEditEvent

​(

Object

source,

UndoableEdit

edit)

Constructs an UndoableEditEvent object.

---

#### Constructor Summary

Constructs an UndoableEditEvent object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

UndoableEdit

getEdit

()

Returns the edit value.

- Methods declared in class java.util.

EventObject

getSource

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

Returns the edit value.

Methods declared in class java.util.

EventObject

getSource

,

toString

---

#### Methods declared in class java.util. EventObject

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

- UndoableEditEvent

```java
public UndoableEditEvent​(
Object
source,

UndoableEdit
edit)
```

Constructs an UndoableEditEvent object.

**Parameters:** source

- the Object that originated the event
(typically

this

)
**Parameters:** edit

- an UndoableEdit object

============ METHOD DETAIL ==========

- Method Detail

- getEdit

```java
public
UndoableEdit
getEdit()
```

Returns the edit value.

**Returns:** the UndoableEdit object encapsulating the edit

Constructor Detail

- UndoableEditEvent

```java
public UndoableEditEvent​(
Object
source,

UndoableEdit
edit)
```

Constructs an UndoableEditEvent object.

**Parameters:** source

- the Object that originated the event
(typically

this

)
**Parameters:** edit

- an UndoableEdit object

---

#### Constructor Detail

UndoableEditEvent

```java
public UndoableEditEvent​(
Object
source,

UndoableEdit
edit)
```

Constructs an UndoableEditEvent object.

**Parameters:** source

- the Object that originated the event
(typically

this

)
**Parameters:** edit

- an UndoableEdit object

---

#### UndoableEditEvent

public UndoableEditEvent​(

Object

source,

UndoableEdit

edit)

Constructs an UndoableEditEvent object.

Method Detail

- getEdit

```java
public
UndoableEdit
getEdit()
```

Returns the edit value.

**Returns:** the UndoableEdit object encapsulating the edit

---

#### Method Detail

getEdit

```java
public
UndoableEdit
getEdit()
```

Returns the edit value.

**Returns:** the UndoableEdit object encapsulating the edit

---

#### getEdit

public

UndoableEdit

getEdit()

Returns the edit value.

---

