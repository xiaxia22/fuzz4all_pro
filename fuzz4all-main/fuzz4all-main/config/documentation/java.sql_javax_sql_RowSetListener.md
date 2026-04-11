# Interface RowSetListener

**Source:** `java.sql\javax\sql\RowSetListener.html`

### Class Description

```java
public interface
RowSetListener

extends
EventListener
```

An interface that must be implemented by a
component that wants to be notified when a significant
event happens in the life of a

RowSet

object.
A component becomes a listener by being registered with a

RowSet

object via the method

RowSet.addRowSetListener

.
How a registered component implements this interface determines what it does
when it is notified of an event.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void rowSetChanged​(
RowSetEvent
event)

Notifies registered listeners that a

RowSet

object
in the given

RowSetEvent

object has changed its entire contents.

The source of the event can be retrieved with the method

event.getSource

.

**Parameters:**
- event

- a

RowSetEvent

object that contains
the

RowSet

object that is the source of the event

---

#### void rowChanged​(
RowSetEvent
event)

Notifies registered listeners that a

RowSet

object
has had a change in one of its rows.

The source of the event can be retrieved with the method

event.getSource

.

**Parameters:**
- event

- a

RowSetEvent

object that contains
the

RowSet

object that is the source of the event

---

#### void cursorMoved​(
RowSetEvent
event)

Notifies registered listeners that a

RowSet

object's
cursor has moved.

The source of the event can be retrieved with the method

event.getSource

.

**Parameters:**
- event

- a

RowSetEvent

object that contains
the

RowSet

object that is the source of the event

---

### Additional Sections

#### Interface RowSetListener

**All Superinterfaces:** EventListener

```java
public interface
RowSetListener

extends
EventListener
```

An interface that must be implemented by a
component that wants to be notified when a significant
event happens in the life of a

RowSet

object.
A component becomes a listener by being registered with a

RowSet

object via the method

RowSet.addRowSetListener

.
How a registered component implements this interface determines what it does
when it is notified of an event.

**Since:** 1.4

public interface

RowSetListener

extends

EventListener

An interface that must be implemented by a
component that wants to be notified when a significant
event happens in the life of a

RowSet

object.
A component becomes a listener by being registered with a

RowSet

object via the method

RowSet.addRowSetListener

.
How a registered component implements this interface determines what it does
when it is notified of an event.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

cursorMoved

​(

RowSetEvent

event)

Notifies registered listeners that a

RowSet

object's
cursor has moved.

void

rowChanged

​(

RowSetEvent

event)

Notifies registered listeners that a

RowSet

object
has had a change in one of its rows.

void

rowSetChanged

​(

RowSetEvent

event)

Notifies registered listeners that a

RowSet

object
in the given

RowSetEvent

object has changed its entire contents.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

cursorMoved

​(

RowSetEvent

event)

Notifies registered listeners that a

RowSet

object's
cursor has moved.

void

rowChanged

​(

RowSetEvent

event)

Notifies registered listeners that a

RowSet

object
has had a change in one of its rows.

void

rowSetChanged

​(

RowSetEvent

event)

Notifies registered listeners that a

RowSet

object
in the given

RowSetEvent

object has changed its entire contents.

---

#### Method Summary

Notifies registered listeners that a

RowSet

object's
cursor has moved.

Notifies registered listeners that a

RowSet

object
has had a change in one of its rows.

Notifies registered listeners that a

RowSet

object
in the given

RowSetEvent

object has changed its entire contents.

============ METHOD DETAIL ==========

- Method Detail

- rowSetChanged

```java
void rowSetChanged​(
RowSetEvent
event)
```

Notifies registered listeners that a

RowSet

object
in the given

RowSetEvent

object has changed its entire contents.

The source of the event can be retrieved with the method

event.getSource

.

**Parameters:** event

- a

RowSetEvent

object that contains
the

RowSet

object that is the source of the event

- rowChanged

```java
void rowChanged​(
RowSetEvent
event)
```

Notifies registered listeners that a

RowSet

object
has had a change in one of its rows.

The source of the event can be retrieved with the method

event.getSource

.

**Parameters:** event

- a

RowSetEvent

object that contains
the

RowSet

object that is the source of the event

- cursorMoved

```java
void cursorMoved​(
RowSetEvent
event)
```

Notifies registered listeners that a

RowSet

object's
cursor has moved.

The source of the event can be retrieved with the method

event.getSource

.

**Parameters:** event

- a

RowSetEvent

object that contains
the

RowSet

object that is the source of the event

Method Detail

- rowSetChanged

```java
void rowSetChanged​(
RowSetEvent
event)
```

Notifies registered listeners that a

RowSet

object
in the given

RowSetEvent

object has changed its entire contents.

The source of the event can be retrieved with the method

event.getSource

.

**Parameters:** event

- a

RowSetEvent

object that contains
the

RowSet

object that is the source of the event

- rowChanged

```java
void rowChanged​(
RowSetEvent
event)
```

Notifies registered listeners that a

RowSet

object
has had a change in one of its rows.

The source of the event can be retrieved with the method

event.getSource

.

**Parameters:** event

- a

RowSetEvent

object that contains
the

RowSet

object that is the source of the event

- cursorMoved

```java
void cursorMoved​(
RowSetEvent
event)
```

Notifies registered listeners that a

RowSet

object's
cursor has moved.

The source of the event can be retrieved with the method

event.getSource

.

**Parameters:** event

- a

RowSetEvent

object that contains
the

RowSet

object that is the source of the event

---

#### Method Detail

rowSetChanged

```java
void rowSetChanged​(
RowSetEvent
event)
```

Notifies registered listeners that a

RowSet

object
in the given

RowSetEvent

object has changed its entire contents.

The source of the event can be retrieved with the method

event.getSource

.

**Parameters:** event

- a

RowSetEvent

object that contains
the

RowSet

object that is the source of the event

---

#### rowSetChanged

void rowSetChanged​(

RowSetEvent

event)

Notifies registered listeners that a

RowSet

object
in the given

RowSetEvent

object has changed its entire contents.

The source of the event can be retrieved with the method

event.getSource

.

The source of the event can be retrieved with the method

event.getSource

.

rowChanged

```java
void rowChanged​(
RowSetEvent
event)
```

Notifies registered listeners that a

RowSet

object
has had a change in one of its rows.

The source of the event can be retrieved with the method

event.getSource

.

**Parameters:** event

- a

RowSetEvent

object that contains
the

RowSet

object that is the source of the event

---

#### rowChanged

void rowChanged​(

RowSetEvent

event)

Notifies registered listeners that a

RowSet

object
has had a change in one of its rows.

The source of the event can be retrieved with the method

event.getSource

.

The source of the event can be retrieved with the method

event.getSource

.

cursorMoved

```java
void cursorMoved​(
RowSetEvent
event)
```

Notifies registered listeners that a

RowSet

object's
cursor has moved.

The source of the event can be retrieved with the method

event.getSource

.

**Parameters:** event

- a

RowSetEvent

object that contains
the

RowSet

object that is the source of the event

---

#### cursorMoved

void cursorMoved​(

RowSetEvent

event)

Notifies registered listeners that a

RowSet

object's
cursor has moved.

The source of the event can be retrieved with the method

event.getSource

.

The source of the event can be retrieved with the method

event.getSource

.

---

