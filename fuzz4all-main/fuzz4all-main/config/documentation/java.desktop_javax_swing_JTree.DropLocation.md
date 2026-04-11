# Class JTree.DropLocation

**Source:** `java.desktop\javax\swing\JTree.DropLocation.html`

### Class Description

```java
public static final class
JTree.DropLocation

extends
TransferHandler.DropLocation
```

A subclass of

TransferHandler.DropLocation

representing
a drop location for a

JTree

.

**Enclosing class:** JTree

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public int getChildIndex()

Returns the index where the dropped data should be inserted
with respect to the path returned by

getPath()

.

For drop modes

DropMode.USE_SELECTION

and

DropMode.ON

, this index is unimportant (and it will
always be

-1

) as the only interesting data is the
path over which the drop operation occurred.

For drop mode

DropMode.INSERT

, this index
indicates the index at which the data should be inserted into
the parent path represented by

getPath()

.

-1

indicates that the drop occurred over the
parent itself, and in most cases should be treated as inserting
into either the beginning or the end of the parent's list of
children.

For

DropMode.ON_OR_INSERT

, this value will be
an insert index, as described above, or

-1

if
the drop occurred over the path itself.

**Returns:**
- the child index

**See Also:**
- getPath()

---

#### public
TreePath
getPath()

Returns the path where dropped data should be placed in the
tree.

Interpretation of this value depends on the drop mode set on the
component. If the drop mode is

DropMode.USE_SELECTION

or

DropMode.ON

, the return value is the path in the
tree over which the data has been (or will be) dropped.

null

indicates that the drop is over empty space,
not associated with a particular path.

If the drop mode is

DropMode.INSERT

, the return value
refers to the path that should become the parent of the new data,
in which case

getChildIndex()

indicates where the
new item should be inserted into this parent path. A

null

path indicates that no parent path has been
determined, which can happen for multiple reasons:

- The tree has no model

There is no root in the tree

The root is collapsed

The root is a leaf node

It is up to the developer to decide if and how they wish to handle
the

null

case.

If the drop mode is

DropMode.ON_OR_INSERT

,

getChildIndex

can be used to determine whether the
drop is on top of the path itself (

-1

) or the index
at which it should be inserted into the path (values other than

-1

).

**Returns:**
- the drop path

**See Also:**
- getChildIndex()

---

#### public
String
toString()

Returns a string representation of this drop location.
This method is intended to be used for debugging purposes,
and the content and format of the returned string may vary
between implementations.

**Overrides:**
- toString

in class

TransferHandler.DropLocation

**Returns:**
- a string representation of this drop location

---

### Additional Sections

#### Class JTree.DropLocation

java.lang.Object

- javax.swing.TransferHandler.DropLocation
- - javax.swing.JTree.DropLocation

javax.swing.TransferHandler.DropLocation

- javax.swing.JTree.DropLocation

javax.swing.JTree.DropLocation

**Enclosing class:** JTree

```java
public static final class
JTree.DropLocation

extends
TransferHandler.DropLocation
```

A subclass of

TransferHandler.DropLocation

representing
a drop location for a

JTree

.

**Since:** 1.6
**See Also:** JTree.getDropLocation()

public static final class

JTree.DropLocation

extends

TransferHandler.DropLocation

A subclass of

TransferHandler.DropLocation

representing
a drop location for a

JTree

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

getChildIndex

()

Returns the index where the dropped data should be inserted
with respect to the path returned by

getPath()

.

TreePath

getPath

()

Returns the path where dropped data should be placed in the
tree.

String

toString

()

Returns a string representation of this drop location.

- Methods declared in class javax.swing.

TransferHandler.DropLocation

getDropPoint

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

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getChildIndex

()

Returns the index where the dropped data should be inserted
with respect to the path returned by

getPath()

.

TreePath

getPath

()

Returns the path where dropped data should be placed in the
tree.

String

toString

()

Returns a string representation of this drop location.

- Methods declared in class javax.swing.

TransferHandler.DropLocation

getDropPoint

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

Returns the index where the dropped data should be inserted
with respect to the path returned by

getPath()

.

Returns the path where dropped data should be placed in the
tree.

Returns a string representation of this drop location.

Methods declared in class javax.swing.

TransferHandler.DropLocation

getDropPoint

---

#### Methods declared in class javax.swing. TransferHandler.DropLocation

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

============ METHOD DETAIL ==========

- Method Detail

- getChildIndex

```java
public int getChildIndex()
```

Returns the index where the dropped data should be inserted
with respect to the path returned by

getPath()

.

For drop modes

DropMode.USE_SELECTION

and

DropMode.ON

, this index is unimportant (and it will
always be

-1

) as the only interesting data is the
path over which the drop operation occurred.

For drop mode

DropMode.INSERT

, this index
indicates the index at which the data should be inserted into
the parent path represented by

getPath()

.

-1

indicates that the drop occurred over the
parent itself, and in most cases should be treated as inserting
into either the beginning or the end of the parent's list of
children.

For

DropMode.ON_OR_INSERT

, this value will be
an insert index, as described above, or

-1

if
the drop occurred over the path itself.

**Returns:** the child index
**See Also:** getPath()

- getPath

```java
public
TreePath
getPath()
```

Returns the path where dropped data should be placed in the
tree.

Interpretation of this value depends on the drop mode set on the
component. If the drop mode is

DropMode.USE_SELECTION

or

DropMode.ON

, the return value is the path in the
tree over which the data has been (or will be) dropped.

null

indicates that the drop is over empty space,
not associated with a particular path.

If the drop mode is

DropMode.INSERT

, the return value
refers to the path that should become the parent of the new data,
in which case

getChildIndex()

indicates where the
new item should be inserted into this parent path. A

null

path indicates that no parent path has been
determined, which can happen for multiple reasons:

- The tree has no model

There is no root in the tree

The root is collapsed

The root is a leaf node

It is up to the developer to decide if and how they wish to handle
the

null

case.

If the drop mode is

DropMode.ON_OR_INSERT

,

getChildIndex

can be used to determine whether the
drop is on top of the path itself (

-1

) or the index
at which it should be inserted into the path (values other than

-1

).

**Returns:** the drop path
**See Also:** getChildIndex()

- toString

```java
public
String
toString()
```

Returns a string representation of this drop location.
This method is intended to be used for debugging purposes,
and the content and format of the returned string may vary
between implementations.

**Overrides:** toString

in class

TransferHandler.DropLocation
**Returns:** a string representation of this drop location

Method Detail

- getChildIndex

```java
public int getChildIndex()
```

Returns the index where the dropped data should be inserted
with respect to the path returned by

getPath()

.

For drop modes

DropMode.USE_SELECTION

and

DropMode.ON

, this index is unimportant (and it will
always be

-1

) as the only interesting data is the
path over which the drop operation occurred.

For drop mode

DropMode.INSERT

, this index
indicates the index at which the data should be inserted into
the parent path represented by

getPath()

.

-1

indicates that the drop occurred over the
parent itself, and in most cases should be treated as inserting
into either the beginning or the end of the parent's list of
children.

For

DropMode.ON_OR_INSERT

, this value will be
an insert index, as described above, or

-1

if
the drop occurred over the path itself.

**Returns:** the child index
**See Also:** getPath()

- getPath

```java
public
TreePath
getPath()
```

Returns the path where dropped data should be placed in the
tree.

Interpretation of this value depends on the drop mode set on the
component. If the drop mode is

DropMode.USE_SELECTION

or

DropMode.ON

, the return value is the path in the
tree over which the data has been (or will be) dropped.

null

indicates that the drop is over empty space,
not associated with a particular path.

If the drop mode is

DropMode.INSERT

, the return value
refers to the path that should become the parent of the new data,
in which case

getChildIndex()

indicates where the
new item should be inserted into this parent path. A

null

path indicates that no parent path has been
determined, which can happen for multiple reasons:

- The tree has no model

There is no root in the tree

The root is collapsed

The root is a leaf node

It is up to the developer to decide if and how they wish to handle
the

null

case.

If the drop mode is

DropMode.ON_OR_INSERT

,

getChildIndex

can be used to determine whether the
drop is on top of the path itself (

-1

) or the index
at which it should be inserted into the path (values other than

-1

).

**Returns:** the drop path
**See Also:** getChildIndex()

- toString

```java
public
String
toString()
```

Returns a string representation of this drop location.
This method is intended to be used for debugging purposes,
and the content and format of the returned string may vary
between implementations.

**Overrides:** toString

in class

TransferHandler.DropLocation
**Returns:** a string representation of this drop location

---

#### Method Detail

getChildIndex

```java
public int getChildIndex()
```

Returns the index where the dropped data should be inserted
with respect to the path returned by

getPath()

.

For drop modes

DropMode.USE_SELECTION

and

DropMode.ON

, this index is unimportant (and it will
always be

-1

) as the only interesting data is the
path over which the drop operation occurred.

For drop mode

DropMode.INSERT

, this index
indicates the index at which the data should be inserted into
the parent path represented by

getPath()

.

-1

indicates that the drop occurred over the
parent itself, and in most cases should be treated as inserting
into either the beginning or the end of the parent's list of
children.

For

DropMode.ON_OR_INSERT

, this value will be
an insert index, as described above, or

-1

if
the drop occurred over the path itself.

**Returns:** the child index
**See Also:** getPath()

---

#### getChildIndex

public int getChildIndex()

Returns the index where the dropped data should be inserted
with respect to the path returned by

getPath()

.

For drop modes

DropMode.USE_SELECTION

and

DropMode.ON

, this index is unimportant (and it will
always be

-1

) as the only interesting data is the
path over which the drop operation occurred.

For drop mode

DropMode.INSERT

, this index
indicates the index at which the data should be inserted into
the parent path represented by

getPath()

.

-1

indicates that the drop occurred over the
parent itself, and in most cases should be treated as inserting
into either the beginning or the end of the parent's list of
children.

For

DropMode.ON_OR_INSERT

, this value will be
an insert index, as described above, or

-1

if
the drop occurred over the path itself.

For drop modes

DropMode.USE_SELECTION

and

DropMode.ON

, this index is unimportant (and it will
always be

-1

) as the only interesting data is the
path over which the drop operation occurred.

For drop mode

DropMode.INSERT

, this index
indicates the index at which the data should be inserted into
the parent path represented by

getPath()

.

-1

indicates that the drop occurred over the
parent itself, and in most cases should be treated as inserting
into either the beginning or the end of the parent's list of
children.

For

DropMode.ON_OR_INSERT

, this value will be
an insert index, as described above, or

-1

if
the drop occurred over the path itself.

For drop mode

DropMode.INSERT

, this index
indicates the index at which the data should be inserted into
the parent path represented by

getPath()

.

-1

indicates that the drop occurred over the
parent itself, and in most cases should be treated as inserting
into either the beginning or the end of the parent's list of
children.

For

DropMode.ON_OR_INSERT

, this value will be
an insert index, as described above, or

-1

if
the drop occurred over the path itself.

For

DropMode.ON_OR_INSERT

, this value will be
an insert index, as described above, or

-1

if
the drop occurred over the path itself.

getPath

```java
public
TreePath
getPath()
```

Returns the path where dropped data should be placed in the
tree.

Interpretation of this value depends on the drop mode set on the
component. If the drop mode is

DropMode.USE_SELECTION

or

DropMode.ON

, the return value is the path in the
tree over which the data has been (or will be) dropped.

null

indicates that the drop is over empty space,
not associated with a particular path.

If the drop mode is

DropMode.INSERT

, the return value
refers to the path that should become the parent of the new data,
in which case

getChildIndex()

indicates where the
new item should be inserted into this parent path. A

null

path indicates that no parent path has been
determined, which can happen for multiple reasons:

- The tree has no model

There is no root in the tree

The root is collapsed

The root is a leaf node

It is up to the developer to decide if and how they wish to handle
the

null

case.

If the drop mode is

DropMode.ON_OR_INSERT

,

getChildIndex

can be used to determine whether the
drop is on top of the path itself (

-1

) or the index
at which it should be inserted into the path (values other than

-1

).

**Returns:** the drop path
**See Also:** getChildIndex()

---

#### getPath

public

TreePath

getPath()

Returns the path where dropped data should be placed in the
tree.

Interpretation of this value depends on the drop mode set on the
component. If the drop mode is

DropMode.USE_SELECTION

or

DropMode.ON

, the return value is the path in the
tree over which the data has been (or will be) dropped.

null

indicates that the drop is over empty space,
not associated with a particular path.

If the drop mode is

DropMode.INSERT

, the return value
refers to the path that should become the parent of the new data,
in which case

getChildIndex()

indicates where the
new item should be inserted into this parent path. A

null

path indicates that no parent path has been
determined, which can happen for multiple reasons:

- The tree has no model

There is no root in the tree

The root is collapsed

The root is a leaf node

It is up to the developer to decide if and how they wish to handle
the

null

case.

If the drop mode is

DropMode.ON_OR_INSERT

,

getChildIndex

can be used to determine whether the
drop is on top of the path itself (

-1

) or the index
at which it should be inserted into the path (values other than

-1

).

Interpretation of this value depends on the drop mode set on the
component. If the drop mode is

DropMode.USE_SELECTION

or

DropMode.ON

, the return value is the path in the
tree over which the data has been (or will be) dropped.

null

indicates that the drop is over empty space,
not associated with a particular path.

If the drop mode is

DropMode.INSERT

, the return value
refers to the path that should become the parent of the new data,
in which case

getChildIndex()

indicates where the
new item should be inserted into this parent path. A

null

path indicates that no parent path has been
determined, which can happen for multiple reasons:

- The tree has no model

There is no root in the tree

The root is collapsed

The root is a leaf node

It is up to the developer to decide if and how they wish to handle
the

null

case.

If the drop mode is

DropMode.ON_OR_INSERT

,

getChildIndex

can be used to determine whether the
drop is on top of the path itself (

-1

) or the index
at which it should be inserted into the path (values other than

-1

).

If the drop mode is

DropMode.INSERT

, the return value
refers to the path that should become the parent of the new data,
in which case

getChildIndex()

indicates where the
new item should be inserted into this parent path. A

null

path indicates that no parent path has been
determined, which can happen for multiple reasons:

- The tree has no model

There is no root in the tree

The root is collapsed

The root is a leaf node

It is up to the developer to decide if and how they wish to handle
the

null

case.

If the drop mode is

DropMode.ON_OR_INSERT

,

getChildIndex

can be used to determine whether the
drop is on top of the path itself (

-1

) or the index
at which it should be inserted into the path (values other than

-1

).

The tree has no model

There is no root in the tree

The root is collapsed

The root is a leaf node

If the drop mode is

DropMode.ON_OR_INSERT

,

getChildIndex

can be used to determine whether the
drop is on top of the path itself (

-1

) or the index
at which it should be inserted into the path (values other than

-1

).

toString

```java
public
String
toString()
```

Returns a string representation of this drop location.
This method is intended to be used for debugging purposes,
and the content and format of the returned string may vary
between implementations.

**Overrides:** toString

in class

TransferHandler.DropLocation
**Returns:** a string representation of this drop location

---

#### toString

public

String

toString()

Returns a string representation of this drop location.
This method is intended to be used for debugging purposes,
and the content and format of the returned string may vary
between implementations.

---

