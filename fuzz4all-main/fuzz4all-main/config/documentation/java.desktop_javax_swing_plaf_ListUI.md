# Class ListUI

**Source:** `java.desktop\javax\swing\plaf\ListUI.html`

### Class Description

```java
public abstract class
ListUI

extends
ComponentUI
```

The

JList

pluggable look and feel delegate.

**Direct Known Subclasses:** BasicListUI

,

MultiListUI

---

### Field Details

*No entries found.*

### Constructor Details

#### public ListUI()

*No description found.*

---

### Method Details

#### public abstract int locationToIndex​(
JList
<?> list,

Point
location)

Returns the cell index in the specified

JList

closest to the
given location in the list's coordinate system. To determine if the
cell actually contains the specified location, compare the point against
the cell's bounds, as provided by

getCellBounds

.
This method returns

-1

if the list's model is empty.

**Parameters:**
- list

- the list
- location

- the coordinates of the point

**Returns:**
- the cell index closest to the given location, or

-1

**Throws:**
- NullPointerException

- if

location

is null

---

#### public abstract
Point
indexToLocation​(
JList
<?> list,
int index)

Returns the origin in the given

JList

, of the specified item,
in the list's coordinate system.
Returns

null

if the index isn't valid.

**Parameters:**
- list

- the list
- index

- the cell index

**Returns:**
- the origin of the cell, or

null

---

#### public abstract
Rectangle
getCellBounds​(
JList
<?> list,
int index1,
int index2)

Returns the bounding rectangle, in the given list's coordinate system,
for the range of cells specified by the two indices.
The indices can be supplied in any order.

If the smaller index is outside the list's range of cells, this method
returns

null

. If the smaller index is valid, but the larger
index is outside the list's range, the bounds of just the first index
is returned. Otherwise, the bounds of the valid range is returned.

**Parameters:**
- list

- the list
- index1

- the first index in the range
- index2

- the second index in the range

**Returns:**
- the bounding rectangle for the range of cells, or

null

---

### Additional Sections

#### Class ListUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.ListUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.ListUI

javax.swing.plaf.ListUI

**Direct Known Subclasses:** BasicListUI

,

MultiListUI

```java
public abstract class
ListUI

extends
ComponentUI
```

The

JList

pluggable look and feel delegate.

public abstract class

ListUI

extends

ComponentUI

The

JList

pluggable look and feel delegate.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ListUI

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

Rectangle

getCellBounds

​(

JList

<?> list,
int index1,
int index2)

Returns the bounding rectangle, in the given list's coordinate system,
for the range of cells specified by the two indices.

abstract

Point

indexToLocation

​(

JList

<?> list,
int index)

Returns the origin in the given

JList

, of the specified item,
in the list's coordinate system.

abstract int

locationToIndex

​(

JList

<?> list,

Point

location)

Returns the cell index in the specified

JList

closest to the
given location in the list's coordinate system.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

createUI

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getBaseline

,

getBaselineResizeBehavior

,

getMaximumSize

,

getMinimumSize

,

getPreferredSize

,

installUI

,

paint

,

uninstallUI

,

update

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

ListUI

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

Rectangle

getCellBounds

​(

JList

<?> list,
int index1,
int index2)

Returns the bounding rectangle, in the given list's coordinate system,
for the range of cells specified by the two indices.

abstract

Point

indexToLocation

​(

JList

<?> list,
int index)

Returns the origin in the given

JList

, of the specified item,
in the list's coordinate system.

abstract int

locationToIndex

​(

JList

<?> list,

Point

location)

Returns the cell index in the specified

JList

closest to the
given location in the list's coordinate system.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

createUI

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getBaseline

,

getBaselineResizeBehavior

,

getMaximumSize

,

getMinimumSize

,

getPreferredSize

,

installUI

,

paint

,

uninstallUI

,

update

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Returns the bounding rectangle, in the given list's coordinate system,
for the range of cells specified by the two indices.

Returns the origin in the given

JList

, of the specified item,
in the list's coordinate system.

Returns the cell index in the specified

JList

closest to the
given location in the list's coordinate system.

Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

createUI

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getBaseline

,

getBaselineResizeBehavior

,

getMaximumSize

,

getMinimumSize

,

getPreferredSize

,

installUI

,

paint

,

uninstallUI

,

update

---

#### Methods declared in class javax.swing.plaf. ComponentUI

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

- ListUI

```java
public ListUI()
```

============ METHOD DETAIL ==========

- Method Detail

- locationToIndex

```java
public abstract int locationToIndex​(
JList
<?> list,

Point
location)
```

Returns the cell index in the specified

JList

closest to the
given location in the list's coordinate system. To determine if the
cell actually contains the specified location, compare the point against
the cell's bounds, as provided by

getCellBounds

.
This method returns

-1

if the list's model is empty.

**Parameters:** list

- the list
**Parameters:** location

- the coordinates of the point
**Returns:** the cell index closest to the given location, or

-1
**Throws:** NullPointerException

- if

location

is null

- indexToLocation

```java
public abstract
Point
indexToLocation​(
JList
<?> list,
int index)
```

Returns the origin in the given

JList

, of the specified item,
in the list's coordinate system.
Returns

null

if the index isn't valid.

**Parameters:** list

- the list
**Parameters:** index

- the cell index
**Returns:** the origin of the cell, or

null

- getCellBounds

```java
public abstract
Rectangle
getCellBounds​(
JList
<?> list,
int index1,
int index2)
```

Returns the bounding rectangle, in the given list's coordinate system,
for the range of cells specified by the two indices.
The indices can be supplied in any order.

If the smaller index is outside the list's range of cells, this method
returns

null

. If the smaller index is valid, but the larger
index is outside the list's range, the bounds of just the first index
is returned. Otherwise, the bounds of the valid range is returned.

**Parameters:** list

- the list
**Parameters:** index1

- the first index in the range
**Parameters:** index2

- the second index in the range
**Returns:** the bounding rectangle for the range of cells, or

null

Constructor Detail

- ListUI

```java
public ListUI()
```

---

#### Constructor Detail

ListUI

```java
public ListUI()
```

---

#### ListUI

public ListUI()

Method Detail

- locationToIndex

```java
public abstract int locationToIndex​(
JList
<?> list,

Point
location)
```

Returns the cell index in the specified

JList

closest to the
given location in the list's coordinate system. To determine if the
cell actually contains the specified location, compare the point against
the cell's bounds, as provided by

getCellBounds

.
This method returns

-1

if the list's model is empty.

**Parameters:** list

- the list
**Parameters:** location

- the coordinates of the point
**Returns:** the cell index closest to the given location, or

-1
**Throws:** NullPointerException

- if

location

is null

- indexToLocation

```java
public abstract
Point
indexToLocation​(
JList
<?> list,
int index)
```

Returns the origin in the given

JList

, of the specified item,
in the list's coordinate system.
Returns

null

if the index isn't valid.

**Parameters:** list

- the list
**Parameters:** index

- the cell index
**Returns:** the origin of the cell, or

null

- getCellBounds

```java
public abstract
Rectangle
getCellBounds​(
JList
<?> list,
int index1,
int index2)
```

Returns the bounding rectangle, in the given list's coordinate system,
for the range of cells specified by the two indices.
The indices can be supplied in any order.

If the smaller index is outside the list's range of cells, this method
returns

null

. If the smaller index is valid, but the larger
index is outside the list's range, the bounds of just the first index
is returned. Otherwise, the bounds of the valid range is returned.

**Parameters:** list

- the list
**Parameters:** index1

- the first index in the range
**Parameters:** index2

- the second index in the range
**Returns:** the bounding rectangle for the range of cells, or

null

---

#### Method Detail

locationToIndex

```java
public abstract int locationToIndex​(
JList
<?> list,

Point
location)
```

Returns the cell index in the specified

JList

closest to the
given location in the list's coordinate system. To determine if the
cell actually contains the specified location, compare the point against
the cell's bounds, as provided by

getCellBounds

.
This method returns

-1

if the list's model is empty.

**Parameters:** list

- the list
**Parameters:** location

- the coordinates of the point
**Returns:** the cell index closest to the given location, or

-1
**Throws:** NullPointerException

- if

location

is null

---

#### locationToIndex

public abstract int locationToIndex​(

JList

<?> list,

Point

location)

Returns the cell index in the specified

JList

closest to the
given location in the list's coordinate system. To determine if the
cell actually contains the specified location, compare the point against
the cell's bounds, as provided by

getCellBounds

.
This method returns

-1

if the list's model is empty.

indexToLocation

```java
public abstract
Point
indexToLocation​(
JList
<?> list,
int index)
```

Returns the origin in the given

JList

, of the specified item,
in the list's coordinate system.
Returns

null

if the index isn't valid.

**Parameters:** list

- the list
**Parameters:** index

- the cell index
**Returns:** the origin of the cell, or

null

---

#### indexToLocation

public abstract

Point

indexToLocation​(

JList

<?> list,
int index)

Returns the origin in the given

JList

, of the specified item,
in the list's coordinate system.
Returns

null

if the index isn't valid.

getCellBounds

```java
public abstract
Rectangle
getCellBounds​(
JList
<?> list,
int index1,
int index2)
```

Returns the bounding rectangle, in the given list's coordinate system,
for the range of cells specified by the two indices.
The indices can be supplied in any order.

If the smaller index is outside the list's range of cells, this method
returns

null

. If the smaller index is valid, but the larger
index is outside the list's range, the bounds of just the first index
is returned. Otherwise, the bounds of the valid range is returned.

**Parameters:** list

- the list
**Parameters:** index1

- the first index in the range
**Parameters:** index2

- the second index in the range
**Returns:** the bounding rectangle for the range of cells, or

null

---

#### getCellBounds

public abstract

Rectangle

getCellBounds​(

JList

<?> list,
int index1,
int index2)

Returns the bounding rectangle, in the given list's coordinate system,
for the range of cells specified by the two indices.
The indices can be supplied in any order.

If the smaller index is outside the list's range of cells, this method
returns

null

. If the smaller index is valid, but the larger
index is outside the list's range, the bounds of just the first index
is returned. Otherwise, the bounds of the valid range is returned.

If the smaller index is outside the list's range of cells, this method
returns

null

. If the smaller index is valid, but the larger
index is outside the list's range, the bounds of just the first index
is returned. Otherwise, the bounds of the valid range is returned.

---

