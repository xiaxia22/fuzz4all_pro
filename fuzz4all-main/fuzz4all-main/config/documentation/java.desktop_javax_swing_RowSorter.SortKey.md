# Class RowSorter.SortKey

**Source:** `java.desktop\javax\swing\RowSorter.SortKey.html`

### Class Description

```java
public static class
RowSorter.SortKey

extends
Object
```

SortKey describes the sort order for a particular column. The
column index is in terms of the underlying model, which may differ
from that of the view.

**Enclosing class:** RowSorter

<

M

>

---

### Field Details

*No entries found.*

### Constructor Details

#### public SortKey​(int column,

SortOrder
sortOrder)

Creates a

SortKey

for the specified column with
the specified sort order.

**Parameters:**
- column

- index of the column, in terms of the model
- sortOrder

- the sorter order

**Throws:**
- IllegalArgumentException

- if

sortOrder

is

null

---

### Method Details

#### public final int getColumn()

Returns the index of the column.

**Returns:**
- index of column

---

#### public final
SortOrder
getSortOrder()

Returns the sort order of the column.

**Returns:**
- the sort order of the column

---

#### public int hashCode()

Returns the hash code for this

SortKey

.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- hash code

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public boolean equals​(
Object
o)

Returns true if this object equals the specified object.
If the specified object is a

SortKey

and
references the same column and sort order, the two objects
are equal.

**Overrides:**
- equals

in class

Object

**Parameters:**
- o

- the object to compare to

**Returns:**
- true if

o

is equal to this

SortKey

**See Also:**
- Object.hashCode()

,

HashMap

---

### Additional Sections

#### Class RowSorter.SortKey

java.lang.Object

- javax.swing.RowSorter.SortKey

javax.swing.RowSorter.SortKey

**Enclosing class:** RowSorter

<

M

>

```java
public static class
RowSorter.SortKey

extends
Object
```

SortKey describes the sort order for a particular column. The
column index is in terms of the underlying model, which may differ
from that of the view.

**Since:** 1.6

public static class

RowSorter.SortKey

extends

Object

SortKey describes the sort order for a particular column. The
column index is in terms of the underlying model, which may differ
from that of the view.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SortKey

​(int column,

SortOrder

sortOrder)

Creates a

SortKey

for the specified column with
the specified sort order.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

o)

Returns true if this object equals the specified object.

int

getColumn

()

Returns the index of the column.

SortOrder

getSortOrder

()

Returns the sort order of the column.

int

hashCode

()

Returns the hash code for this

SortKey

.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

SortKey

​(int column,

SortOrder

sortOrder)

Creates a

SortKey

for the specified column with
the specified sort order.

---

#### Constructor Summary

Creates a

SortKey

for the specified column with
the specified sort order.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

o)

Returns true if this object equals the specified object.

int

getColumn

()

Returns the index of the column.

SortOrder

getSortOrder

()

Returns the sort order of the column.

int

hashCode

()

Returns the hash code for this

SortKey

.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Returns true if this object equals the specified object.

Returns the index of the column.

Returns the sort order of the column.

Returns the hash code for this

SortKey

.

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

toString

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

- SortKey

```java
public SortKey​(int column,

SortOrder
sortOrder)
```

Creates a

SortKey

for the specified column with
the specified sort order.

**Parameters:** column

- index of the column, in terms of the model
**Parameters:** sortOrder

- the sorter order
**Throws:** IllegalArgumentException

- if

sortOrder

is

null

============ METHOD DETAIL ==========

- Method Detail

- getColumn

```java
public final int getColumn()
```

Returns the index of the column.

**Returns:** index of column

- getSortOrder

```java
public final
SortOrder
getSortOrder()
```

Returns the sort order of the column.

**Returns:** the sort order of the column

- hashCode

```java
public int hashCode()
```

Returns the hash code for this

SortKey

.

**Overrides:** hashCode

in class

Object
**Returns:** hash code
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
o)
```

Returns true if this object equals the specified object.
If the specified object is a

SortKey

and
references the same column and sort order, the two objects
are equal.

**Overrides:** equals

in class

Object
**Parameters:** o

- the object to compare to
**Returns:** true if

o

is equal to this

SortKey
**See Also:** Object.hashCode()

,

HashMap

Constructor Detail

- SortKey

```java
public SortKey​(int column,

SortOrder
sortOrder)
```

Creates a

SortKey

for the specified column with
the specified sort order.

**Parameters:** column

- index of the column, in terms of the model
**Parameters:** sortOrder

- the sorter order
**Throws:** IllegalArgumentException

- if

sortOrder

is

null

---

#### Constructor Detail

SortKey

```java
public SortKey​(int column,

SortOrder
sortOrder)
```

Creates a

SortKey

for the specified column with
the specified sort order.

**Parameters:** column

- index of the column, in terms of the model
**Parameters:** sortOrder

- the sorter order
**Throws:** IllegalArgumentException

- if

sortOrder

is

null

---

#### SortKey

public SortKey​(int column,

SortOrder

sortOrder)

Creates a

SortKey

for the specified column with
the specified sort order.

Method Detail

- getColumn

```java
public final int getColumn()
```

Returns the index of the column.

**Returns:** index of column

- getSortOrder

```java
public final
SortOrder
getSortOrder()
```

Returns the sort order of the column.

**Returns:** the sort order of the column

- hashCode

```java
public int hashCode()
```

Returns the hash code for this

SortKey

.

**Overrides:** hashCode

in class

Object
**Returns:** hash code
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
o)
```

Returns true if this object equals the specified object.
If the specified object is a

SortKey

and
references the same column and sort order, the two objects
are equal.

**Overrides:** equals

in class

Object
**Parameters:** o

- the object to compare to
**Returns:** true if

o

is equal to this

SortKey
**See Also:** Object.hashCode()

,

HashMap

---

#### Method Detail

getColumn

```java
public final int getColumn()
```

Returns the index of the column.

**Returns:** index of column

---

#### getColumn

public final int getColumn()

Returns the index of the column.

getSortOrder

```java
public final
SortOrder
getSortOrder()
```

Returns the sort order of the column.

**Returns:** the sort order of the column

---

#### getSortOrder

public final

SortOrder

getSortOrder()

Returns the sort order of the column.

hashCode

```java
public int hashCode()
```

Returns the hash code for this

SortKey

.

**Overrides:** hashCode

in class

Object
**Returns:** hash code
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code for this

SortKey

.

equals

```java
public boolean equals​(
Object
o)
```

Returns true if this object equals the specified object.
If the specified object is a

SortKey

and
references the same column and sort order, the two objects
are equal.

**Overrides:** equals

in class

Object
**Parameters:** o

- the object to compare to
**Returns:** true if

o

is equal to this

SortKey
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

o)

Returns true if this object equals the specified object.
If the specified object is a

SortKey

and
references the same column and sort order, the two objects
are equal.

---

