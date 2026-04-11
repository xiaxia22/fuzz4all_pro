# Class DropTargetEvent

**Source:** `java.desktop\java\awt\dnd\DropTargetEvent.html`

### Class Description

```java
public class
DropTargetEvent

extends
EventObject
```

The

DropTargetEvent

is the base
class for both the

DropTargetDragEvent

and the

DropTargetDropEvent

.
It encapsulates the current state of the Drag and
Drop operations, in particular the current

DropTargetContext

.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### protected
DropTargetContext
context

The

DropTargetContext

associated with this

DropTargetEvent

.

---

### Constructor Details

#### public DropTargetEvent​(
DropTargetContext
dtc)

Construct a

DropTargetEvent

object with
the specified

DropTargetContext

.

**Parameters:**
- dtc

- The

DropTargetContext

**Throws:**
- NullPointerException

- if

dtc

equals

null

.

**See Also:**
- EventObject.getSource()

,

getDropTargetContext()

---

### Method Details

#### public
DropTargetContext
getDropTargetContext()

This method returns the

DropTargetContext

associated with this

DropTargetEvent

.

**Returns:**
- the

DropTargetContext

---

### Additional Sections

#### Class DropTargetEvent

java.lang.Object

- java.util.EventObject
- - java.awt.dnd.DropTargetEvent

java.util.EventObject

- java.awt.dnd.DropTargetEvent

java.awt.dnd.DropTargetEvent

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** DropTargetDragEvent

,

DropTargetDropEvent

```java
public class
DropTargetEvent

extends
EventObject
```

The

DropTargetEvent

is the base
class for both the

DropTargetDragEvent

and the

DropTargetDropEvent

.
It encapsulates the current state of the Drag and
Drop operations, in particular the current

DropTargetContext

.

**Since:** 1.2
**See Also:** Serialized Form

public class

DropTargetEvent

extends

EventObject

The

DropTargetEvent

is the base
class for both the

DropTargetDragEvent

and the

DropTargetDropEvent

.
It encapsulates the current state of the Drag and
Drop operations, in particular the current

DropTargetContext

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

DropTargetContext

context

The

DropTargetContext

associated with this

DropTargetEvent

.

- Fields declared in class java.util.

EventObject

source

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DropTargetEvent

​(

DropTargetContext

dtc)

Construct a

DropTargetEvent

object with
the specified

DropTargetContext

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

DropTargetContext

getDropTargetContext

()

This method returns the

DropTargetContext

associated with this

DropTargetEvent

.

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

Fields

Modifier and Type

Field

Description

protected

DropTargetContext

context

The

DropTargetContext

associated with this

DropTargetEvent

.

- Fields declared in class java.util.

EventObject

source

---

#### Field Summary

The

DropTargetContext

associated with this

DropTargetEvent

.

Fields declared in class java.util.

EventObject

source

---

#### Fields declared in class java.util. EventObject

Constructor Summary

Constructors

Constructor

Description

DropTargetEvent

​(

DropTargetContext

dtc)

Construct a

DropTargetEvent

object with
the specified

DropTargetContext

.

---

#### Constructor Summary

Construct a

DropTargetEvent

object with
the specified

DropTargetContext

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

DropTargetContext

getDropTargetContext

()

This method returns the

DropTargetContext

associated with this

DropTargetEvent

.

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

This method returns the

DropTargetContext

associated with this

DropTargetEvent

.

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

============ FIELD DETAIL ===========

- Field Detail

- context

```java
protected
DropTargetContext
context
```

The

DropTargetContext

associated with this

DropTargetEvent

.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DropTargetEvent

```java
public DropTargetEvent​(
DropTargetContext
dtc)
```

Construct a

DropTargetEvent

object with
the specified

DropTargetContext

.

**Parameters:** dtc

- The

DropTargetContext
**Throws:** NullPointerException

- if

dtc

equals

null

.
**See Also:** EventObject.getSource()

,

getDropTargetContext()

============ METHOD DETAIL ==========

- Method Detail

- getDropTargetContext

```java
public
DropTargetContext
getDropTargetContext()
```

This method returns the

DropTargetContext

associated with this

DropTargetEvent

.

**Returns:** the

DropTargetContext

Field Detail

- context

```java
protected
DropTargetContext
context
```

The

DropTargetContext

associated with this

DropTargetEvent

.

---

#### Field Detail

context

```java
protected
DropTargetContext
context
```

The

DropTargetContext

associated with this

DropTargetEvent

.

---

#### context

protected

DropTargetContext

context

The

DropTargetContext

associated with this

DropTargetEvent

.

Constructor Detail

- DropTargetEvent

```java
public DropTargetEvent​(
DropTargetContext
dtc)
```

Construct a

DropTargetEvent

object with
the specified

DropTargetContext

.

**Parameters:** dtc

- The

DropTargetContext
**Throws:** NullPointerException

- if

dtc

equals

null

.
**See Also:** EventObject.getSource()

,

getDropTargetContext()

---

#### Constructor Detail

DropTargetEvent

```java
public DropTargetEvent​(
DropTargetContext
dtc)
```

Construct a

DropTargetEvent

object with
the specified

DropTargetContext

.

**Parameters:** dtc

- The

DropTargetContext
**Throws:** NullPointerException

- if

dtc

equals

null

.
**See Also:** EventObject.getSource()

,

getDropTargetContext()

---

#### DropTargetEvent

public DropTargetEvent​(

DropTargetContext

dtc)

Construct a

DropTargetEvent

object with
the specified

DropTargetContext

.

Method Detail

- getDropTargetContext

```java
public
DropTargetContext
getDropTargetContext()
```

This method returns the

DropTargetContext

associated with this

DropTargetEvent

.

**Returns:** the

DropTargetContext

---

#### Method Detail

getDropTargetContext

```java
public
DropTargetContext
getDropTargetContext()
```

This method returns the

DropTargetContext

associated with this

DropTargetEvent

.

**Returns:** the

DropTargetContext

---

#### getDropTargetContext

public

DropTargetContext

getDropTargetContext()

This method returns the

DropTargetContext

associated with this

DropTargetEvent

.

---

