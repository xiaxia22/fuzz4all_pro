# Class TableColumnModelEvent

**Source:** `java.desktop\javax\swing\event\TableColumnModelEvent.html`

### Class Description

```java
public class
TableColumnModelEvent

extends
EventObject
```

TableColumnModelEvent

is used to notify listeners that a table
column model has changed, such as a column was added, removed, or
moved.

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

#### protected int fromIndex

The index of the column from where it was moved or removed

---

#### protected int toIndex

The index of the column to where it was moved or added

---

### Constructor Details

#### public TableColumnModelEvent​(
TableColumnModel
source,
int from,
int to)

Constructs a

TableColumnModelEvent

object.

**Parameters:**
- source

- the

TableColumnModel

that originated the event
- from

- an int specifying the index from where the column was
moved or removed
- to

- an int specifying the index to where the column was
moved or added

**See Also:**
- getFromIndex()

,

getToIndex()

---

### Method Details

#### public int getFromIndex()

Returns the fromIndex. Valid for removed or moved events

**Returns:**
- int value for index from which the column was moved or removed

---

#### public int getToIndex()

Returns the toIndex. Valid for add and moved events

**Returns:**
- int value of column's new index

---

### Additional Sections

#### Class TableColumnModelEvent

java.lang.Object

- java.util.EventObject
- - javax.swing.event.TableColumnModelEvent

java.util.EventObject

- javax.swing.event.TableColumnModelEvent

javax.swing.event.TableColumnModelEvent

**All Implemented Interfaces:** Serializable

```java
public class
TableColumnModelEvent

extends
EventObject
```

TableColumnModelEvent

is used to notify listeners that a table
column model has changed, such as a column was added, removed, or
moved.

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

**See Also:** TableColumnModelListener

,

Serialized Form

public class

TableColumnModelEvent

extends

EventObject

TableColumnModelEvent

is used to notify listeners that a table
column model has changed, such as a column was added, removed, or
moved.

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

Fields

Modifier and Type

Field

Description

protected int

fromIndex

The index of the column from where it was moved or removed

protected int

toIndex

The index of the column to where it was moved or added

- Fields declared in class java.util.

EventObject

source

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TableColumnModelEvent

​(

TableColumnModel

source,
int from,
int to)

Constructs a

TableColumnModelEvent

object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getFromIndex

()

Returns the fromIndex.

int

getToIndex

()

Returns the toIndex.

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

protected int

fromIndex

The index of the column from where it was moved or removed

protected int

toIndex

The index of the column to where it was moved or added

- Fields declared in class java.util.

EventObject

source

---

#### Field Summary

The index of the column from where it was moved or removed

The index of the column to where it was moved or added

Fields declared in class java.util.

EventObject

source

---

#### Fields declared in class java.util. EventObject

Constructor Summary

Constructors

Constructor

Description

TableColumnModelEvent

​(

TableColumnModel

source,
int from,
int to)

Constructs a

TableColumnModelEvent

object.

---

#### Constructor Summary

Constructs a

TableColumnModelEvent

object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getFromIndex

()

Returns the fromIndex.

int

getToIndex

()

Returns the toIndex.

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

Returns the fromIndex.

Returns the toIndex.

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

- fromIndex

```java
protected int fromIndex
```

The index of the column from where it was moved or removed

- toIndex

```java
protected int toIndex
```

The index of the column to where it was moved or added

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- TableColumnModelEvent

```java
public TableColumnModelEvent​(
TableColumnModel
source,
int from,
int to)
```

Constructs a

TableColumnModelEvent

object.

**Parameters:** source

- the

TableColumnModel

that originated the event
**Parameters:** from

- an int specifying the index from where the column was
moved or removed
**Parameters:** to

- an int specifying the index to where the column was
moved or added
**See Also:** getFromIndex()

,

getToIndex()

============ METHOD DETAIL ==========

- Method Detail

- getFromIndex

```java
public int getFromIndex()
```

Returns the fromIndex. Valid for removed or moved events

**Returns:** int value for index from which the column was moved or removed

- getToIndex

```java
public int getToIndex()
```

Returns the toIndex. Valid for add and moved events

**Returns:** int value of column's new index

Field Detail

- fromIndex

```java
protected int fromIndex
```

The index of the column from where it was moved or removed

- toIndex

```java
protected int toIndex
```

The index of the column to where it was moved or added

---

#### Field Detail

fromIndex

```java
protected int fromIndex
```

The index of the column from where it was moved or removed

---

#### fromIndex

protected int fromIndex

The index of the column from where it was moved or removed

toIndex

```java
protected int toIndex
```

The index of the column to where it was moved or added

---

#### toIndex

protected int toIndex

The index of the column to where it was moved or added

Constructor Detail

- TableColumnModelEvent

```java
public TableColumnModelEvent​(
TableColumnModel
source,
int from,
int to)
```

Constructs a

TableColumnModelEvent

object.

**Parameters:** source

- the

TableColumnModel

that originated the event
**Parameters:** from

- an int specifying the index from where the column was
moved or removed
**Parameters:** to

- an int specifying the index to where the column was
moved or added
**See Also:** getFromIndex()

,

getToIndex()

---

#### Constructor Detail

TableColumnModelEvent

```java
public TableColumnModelEvent​(
TableColumnModel
source,
int from,
int to)
```

Constructs a

TableColumnModelEvent

object.

**Parameters:** source

- the

TableColumnModel

that originated the event
**Parameters:** from

- an int specifying the index from where the column was
moved or removed
**Parameters:** to

- an int specifying the index to where the column was
moved or added
**See Also:** getFromIndex()

,

getToIndex()

---

#### TableColumnModelEvent

public TableColumnModelEvent​(

TableColumnModel

source,
int from,
int to)

Constructs a

TableColumnModelEvent

object.

Method Detail

- getFromIndex

```java
public int getFromIndex()
```

Returns the fromIndex. Valid for removed or moved events

**Returns:** int value for index from which the column was moved or removed

- getToIndex

```java
public int getToIndex()
```

Returns the toIndex. Valid for add and moved events

**Returns:** int value of column's new index

---

#### Method Detail

getFromIndex

```java
public int getFromIndex()
```

Returns the fromIndex. Valid for removed or moved events

**Returns:** int value for index from which the column was moved or removed

---

#### getFromIndex

public int getFromIndex()

Returns the fromIndex. Valid for removed or moved events

getToIndex

```java
public int getToIndex()
```

Returns the toIndex. Valid for add and moved events

**Returns:** int value of column's new index

---

#### getToIndex

public int getToIndex()

Returns the toIndex. Valid for add and moved events

---

