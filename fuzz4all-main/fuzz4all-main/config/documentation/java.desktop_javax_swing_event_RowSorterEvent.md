# Class RowSorterEvent

**Source:** `java.desktop\javax\swing\event\RowSorterEvent.html`

### Class Description

```java
public class
RowSorterEvent

extends
EventObject
```

RowSorterEvent

provides notification of changes to
a

RowSorter

. Two types of notification are possible:

- Type.SORT_ORDER_CHANGED

: indicates the sort order has
changed. This is typically followed by a notification of:

Type.SORTED

: indicates the contents of the model have
been transformed in some way. For example, the contents may have
been sorted or filtered.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public RowSorterEvent​(
RowSorter
<?> source)

Creates a

RowSorterEvent

of type

SORT_ORDER_CHANGED

.

**Parameters:**
- source

- the source of the change

**Throws:**
- IllegalArgumentException

- if

source

is

null

---

#### public RowSorterEvent​(
RowSorter
<?> source,

RowSorterEvent.Type
type,
int[] previousRowIndexToModel)

Creates a

RowSorterEvent

.

**Parameters:**
- source

- the source of the change
- type

- the type of event
- previousRowIndexToModel

- the mapping from model indices to
view indices prior to the sort, may be

null

**Throws:**
- IllegalArgumentException

- if source or

type

is

null

---

### Method Details

#### public
RowSorter
<?> getSource()

Returns the source of the event as a

RowSorter

.

**Overrides:**
- getSource

in class

EventObject

**Returns:**
- the source of the event as a

RowSorter

---

#### public
RowSorterEvent.Type
getType()

Returns the type of event.

**Returns:**
- the type of event

---

#### public int convertPreviousRowIndexToModel​(int index)

Returns the location of

index

in terms of the
model prior to the sort. This method is only useful for events
of type

SORTED

. This method will return -1 if the
index is not valid, or the locations prior to the sort have not
been provided.

**Parameters:**
- index

- the index in terms of the view

**Returns:**
- the index in terms of the model prior to the sort, or -1 if
the location is not valid or the mapping was not provided.

---

#### public int getPreviousRowCount()

Returns the number of rows before the sort. This method is only
useful for events of type

SORTED

and if the
last locations have not been provided will return 0.

**Returns:**
- the number of rows in terms of the view prior to the sort

---

### Additional Sections

#### Class RowSorterEvent

java.lang.Object

- java.util.EventObject
- - javax.swing.event.RowSorterEvent

java.util.EventObject

- javax.swing.event.RowSorterEvent

javax.swing.event.RowSorterEvent

**All Implemented Interfaces:** Serializable

```java
public class
RowSorterEvent

extends
EventObject
```

RowSorterEvent

provides notification of changes to
a

RowSorter

. Two types of notification are possible:

- Type.SORT_ORDER_CHANGED

: indicates the sort order has
changed. This is typically followed by a notification of:

Type.SORTED

: indicates the contents of the model have
been transformed in some way. For example, the contents may have
been sorted or filtered.

**Since:** 1.6
**See Also:** RowSorter

,

Serialized Form

public class

RowSorterEvent

extends

EventObject

RowSorterEvent

provides notification of changes to
a

RowSorter

. Two types of notification are possible:

- Type.SORT_ORDER_CHANGED

: indicates the sort order has
changed. This is typically followed by a notification of:

Type.SORTED

: indicates the contents of the model have
been transformed in some way. For example, the contents may have
been sorted or filtered.

Type.SORT_ORDER_CHANGED

: indicates the sort order has
changed. This is typically followed by a notification of:

Type.SORTED

: indicates the contents of the model have
been transformed in some way. For example, the contents may have
been sorted or filtered.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

RowSorterEvent.Type

Enumeration of the types of

RowSorterEvent

s.

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

RowSorterEvent

​(

RowSorter

<?> source)

Creates a

RowSorterEvent

of type

SORT_ORDER_CHANGED

.

RowSorterEvent

​(

RowSorter

<?> source,

RowSorterEvent.Type

type,
int[] previousRowIndexToModel)

Creates a

RowSorterEvent

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

convertPreviousRowIndexToModel

​(int index)

Returns the location of

index

in terms of the
model prior to the sort.

int

getPreviousRowCount

()

Returns the number of rows before the sort.

RowSorter

<?>

getSource

()

Returns the source of the event as a

RowSorter

.

RowSorterEvent.Type

getType

()

Returns the type of event.

- Methods declared in class java.util.

EventObject

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

RowSorterEvent.Type

Enumeration of the types of

RowSorterEvent

s.

---

#### Nested Class Summary

Enumeration of the types of

RowSorterEvent

s.

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

RowSorterEvent

​(

RowSorter

<?> source)

Creates a

RowSorterEvent

of type

SORT_ORDER_CHANGED

.

RowSorterEvent

​(

RowSorter

<?> source,

RowSorterEvent.Type

type,
int[] previousRowIndexToModel)

Creates a

RowSorterEvent

.

---

#### Constructor Summary

Creates a

RowSorterEvent

of type

SORT_ORDER_CHANGED

.

Creates a

RowSorterEvent

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

convertPreviousRowIndexToModel

​(int index)

Returns the location of

index

in terms of the
model prior to the sort.

int

getPreviousRowCount

()

Returns the number of rows before the sort.

RowSorter

<?>

getSource

()

Returns the source of the event as a

RowSorter

.

RowSorterEvent.Type

getType

()

Returns the type of event.

- Methods declared in class java.util.

EventObject

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

Returns the location of

index

in terms of the
model prior to the sort.

Returns the number of rows before the sort.

Returns the source of the event as a

RowSorter

.

Returns the type of event.

Methods declared in class java.util.

EventObject

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

- RowSorterEvent

```java
public RowSorterEvent​(
RowSorter
<?> source)
```

Creates a

RowSorterEvent

of type

SORT_ORDER_CHANGED

.

**Parameters:** source

- the source of the change
**Throws:** IllegalArgumentException

- if

source

is

null

- RowSorterEvent

```java
public RowSorterEvent​(
RowSorter
<?> source,

RowSorterEvent.Type
type,
int[] previousRowIndexToModel)
```

Creates a

RowSorterEvent

.

**Parameters:** source

- the source of the change
**Parameters:** type

- the type of event
**Parameters:** previousRowIndexToModel

- the mapping from model indices to
view indices prior to the sort, may be

null
**Throws:** IllegalArgumentException

- if source or

type

is

null

============ METHOD DETAIL ==========

- Method Detail

- getSource

```java
public
RowSorter
<?> getSource()
```

Returns the source of the event as a

RowSorter

.

**Overrides:** getSource

in class

EventObject
**Returns:** the source of the event as a

RowSorter

- getType

```java
public
RowSorterEvent.Type
getType()
```

Returns the type of event.

**Returns:** the type of event

- convertPreviousRowIndexToModel

```java
public int convertPreviousRowIndexToModel​(int index)
```

Returns the location of

index

in terms of the
model prior to the sort. This method is only useful for events
of type

SORTED

. This method will return -1 if the
index is not valid, or the locations prior to the sort have not
been provided.

**Parameters:** index

- the index in terms of the view
**Returns:** the index in terms of the model prior to the sort, or -1 if
the location is not valid or the mapping was not provided.

- getPreviousRowCount

```java
public int getPreviousRowCount()
```

Returns the number of rows before the sort. This method is only
useful for events of type

SORTED

and if the
last locations have not been provided will return 0.

**Returns:** the number of rows in terms of the view prior to the sort

Constructor Detail

- RowSorterEvent

```java
public RowSorterEvent​(
RowSorter
<?> source)
```

Creates a

RowSorterEvent

of type

SORT_ORDER_CHANGED

.

**Parameters:** source

- the source of the change
**Throws:** IllegalArgumentException

- if

source

is

null

- RowSorterEvent

```java
public RowSorterEvent​(
RowSorter
<?> source,

RowSorterEvent.Type
type,
int[] previousRowIndexToModel)
```

Creates a

RowSorterEvent

.

**Parameters:** source

- the source of the change
**Parameters:** type

- the type of event
**Parameters:** previousRowIndexToModel

- the mapping from model indices to
view indices prior to the sort, may be

null
**Throws:** IllegalArgumentException

- if source or

type

is

null

---

#### Constructor Detail

RowSorterEvent

```java
public RowSorterEvent​(
RowSorter
<?> source)
```

Creates a

RowSorterEvent

of type

SORT_ORDER_CHANGED

.

**Parameters:** source

- the source of the change
**Throws:** IllegalArgumentException

- if

source

is

null

---

#### RowSorterEvent

public RowSorterEvent​(

RowSorter

<?> source)

Creates a

RowSorterEvent

of type

SORT_ORDER_CHANGED

.

RowSorterEvent

```java
public RowSorterEvent​(
RowSorter
<?> source,

RowSorterEvent.Type
type,
int[] previousRowIndexToModel)
```

Creates a

RowSorterEvent

.

**Parameters:** source

- the source of the change
**Parameters:** type

- the type of event
**Parameters:** previousRowIndexToModel

- the mapping from model indices to
view indices prior to the sort, may be

null
**Throws:** IllegalArgumentException

- if source or

type

is

null

---

#### RowSorterEvent

public RowSorterEvent​(

RowSorter

<?> source,

RowSorterEvent.Type

type,
int[] previousRowIndexToModel)

Creates a

RowSorterEvent

.

Method Detail

- getSource

```java
public
RowSorter
<?> getSource()
```

Returns the source of the event as a

RowSorter

.

**Overrides:** getSource

in class

EventObject
**Returns:** the source of the event as a

RowSorter

- getType

```java
public
RowSorterEvent.Type
getType()
```

Returns the type of event.

**Returns:** the type of event

- convertPreviousRowIndexToModel

```java
public int convertPreviousRowIndexToModel​(int index)
```

Returns the location of

index

in terms of the
model prior to the sort. This method is only useful for events
of type

SORTED

. This method will return -1 if the
index is not valid, or the locations prior to the sort have not
been provided.

**Parameters:** index

- the index in terms of the view
**Returns:** the index in terms of the model prior to the sort, or -1 if
the location is not valid or the mapping was not provided.

- getPreviousRowCount

```java
public int getPreviousRowCount()
```

Returns the number of rows before the sort. This method is only
useful for events of type

SORTED

and if the
last locations have not been provided will return 0.

**Returns:** the number of rows in terms of the view prior to the sort

---

#### Method Detail

getSource

```java
public
RowSorter
<?> getSource()
```

Returns the source of the event as a

RowSorter

.

**Overrides:** getSource

in class

EventObject
**Returns:** the source of the event as a

RowSorter

---

#### getSource

public

RowSorter

<?> getSource()

Returns the source of the event as a

RowSorter

.

getType

```java
public
RowSorterEvent.Type
getType()
```

Returns the type of event.

**Returns:** the type of event

---

#### getType

public

RowSorterEvent.Type

getType()

Returns the type of event.

convertPreviousRowIndexToModel

```java
public int convertPreviousRowIndexToModel​(int index)
```

Returns the location of

index

in terms of the
model prior to the sort. This method is only useful for events
of type

SORTED

. This method will return -1 if the
index is not valid, or the locations prior to the sort have not
been provided.

**Parameters:** index

- the index in terms of the view
**Returns:** the index in terms of the model prior to the sort, or -1 if
the location is not valid or the mapping was not provided.

---

#### convertPreviousRowIndexToModel

public int convertPreviousRowIndexToModel​(int index)

Returns the location of

index

in terms of the
model prior to the sort. This method is only useful for events
of type

SORTED

. This method will return -1 if the
index is not valid, or the locations prior to the sort have not
been provided.

getPreviousRowCount

```java
public int getPreviousRowCount()
```

Returns the number of rows before the sort. This method is only
useful for events of type

SORTED

and if the
last locations have not been provided will return 0.

**Returns:** the number of rows in terms of the view prior to the sort

---

#### getPreviousRowCount

public int getPreviousRowCount()

Returns the number of rows before the sort. This method is only
useful for events of type

SORTED

and if the
last locations have not been provided will return 0.

---

