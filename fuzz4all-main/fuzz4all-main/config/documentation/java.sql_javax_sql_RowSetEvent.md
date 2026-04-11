# Class RowSetEvent

**Source:** `java.sql\javax\sql\RowSetEvent.html`

### Class Description

```java
public class
RowSetEvent

extends
EventObject
```

An

Event

object generated when an event occurs to a

RowSet

object. A

RowSetEvent

object is
generated when a single row in a rowset is changed, the whole rowset
is changed, or the rowset cursor moves.

When an event occurs on a

RowSet

object, one of the

RowSetListener

methods will be sent to all registered
listeners to notify them of the event. An

Event

object
is supplied to the

RowSetListener

method so that the
listener can use it to find out which

RowSet

object is
the source of the event.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public RowSetEvent​(
RowSet
source)

Constructs a

RowSetEvent

object initialized with the
given

RowSet

object.

**Parameters:**
- source

- the

RowSet

object whose data has changed or
whose cursor has moved

**Throws:**
- IllegalArgumentException

- if

source

is null.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class RowSetEvent

java.lang.Object

- java.util.EventObject
- - javax.sql.RowSetEvent

java.util.EventObject

- javax.sql.RowSetEvent

javax.sql.RowSetEvent

**All Implemented Interfaces:** Serializable

```java
public class
RowSetEvent

extends
EventObject
```

An

Event

object generated when an event occurs to a

RowSet

object. A

RowSetEvent

object is
generated when a single row in a rowset is changed, the whole rowset
is changed, or the rowset cursor moves.

When an event occurs on a

RowSet

object, one of the

RowSetListener

methods will be sent to all registered
listeners to notify them of the event. An

Event

object
is supplied to the

RowSetListener

method so that the
listener can use it to find out which

RowSet

object is
the source of the event.

**Since:** 1.4
**See Also:** Serialized Form

public class

RowSetEvent

extends

EventObject

An

Event

object generated when an event occurs to a

RowSet

object. A

RowSetEvent

object is
generated when a single row in a rowset is changed, the whole rowset
is changed, or the rowset cursor moves.

When an event occurs on a

RowSet

object, one of the

RowSetListener

methods will be sent to all registered
listeners to notify them of the event. An

Event

object
is supplied to the

RowSetListener

method so that the
listener can use it to find out which

RowSet

object is
the source of the event.

When an event occurs on a

RowSet

object, one of the

RowSetListener

methods will be sent to all registered
listeners to notify them of the event. An

Event

object
is supplied to the

RowSetListener

method so that the
listener can use it to find out which

RowSet

object is
the source of the event.

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

RowSetEvent

​(

RowSet

source)

Constructs a

RowSetEvent

object initialized with the
given

RowSet

object.

========== METHOD SUMMARY ===========

- Method Summary

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

RowSetEvent

​(

RowSet

source)

Constructs a

RowSetEvent

object initialized with the
given

RowSet

object.

---

#### Constructor Summary

Constructs a

RowSetEvent

object initialized with the
given

RowSet

object.

Method Summary

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

- RowSetEvent

```java
public RowSetEvent​(
RowSet
source)
```

Constructs a

RowSetEvent

object initialized with the
given

RowSet

object.

**Parameters:** source

- the

RowSet

object whose data has changed or
whose cursor has moved
**Throws:** IllegalArgumentException

- if

source

is null.

Constructor Detail

- RowSetEvent

```java
public RowSetEvent​(
RowSet
source)
```

Constructs a

RowSetEvent

object initialized with the
given

RowSet

object.

**Parameters:** source

- the

RowSet

object whose data has changed or
whose cursor has moved
**Throws:** IllegalArgumentException

- if

source

is null.

---

#### Constructor Detail

RowSetEvent

```java
public RowSetEvent​(
RowSet
source)
```

Constructs a

RowSetEvent

object initialized with the
given

RowSet

object.

**Parameters:** source

- the

RowSet

object whose data has changed or
whose cursor has moved
**Throws:** IllegalArgumentException

- if

source

is null.

---

#### RowSetEvent

public RowSetEvent​(

RowSet

source)

Constructs a

RowSetEvent

object initialized with the
given

RowSet

object.

---

