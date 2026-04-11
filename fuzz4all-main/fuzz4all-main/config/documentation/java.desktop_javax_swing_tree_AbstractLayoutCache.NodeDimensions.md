# Class AbstractLayoutCache.NodeDimensions

**Source:** `java.desktop\javax\swing\tree\AbstractLayoutCache.NodeDimensions.html`

### Class Description

```java
public abstract static class
AbstractLayoutCache.NodeDimensions

extends
Object
```

Used by

AbstractLayoutCache

to determine the size
and x origin of a particular node.

**Direct Known Subclasses:** BasicTreeUI.NodeDimensionsHandler

---

### Field Details

*No entries found.*

### Constructor Details

#### public NodeDimensions()

*No description found.*

---

### Method Details

#### public abstract
Rectangle
getNodeDimensions​(
Object
value,
int row,
int depth,
boolean expanded,

Rectangle
bounds)

Returns, by reference in bounds, the size and x origin to
place value at. The calling method is responsible for determining
the Y location. If bounds is

null

, a newly created

Rectangle

should be returned,
otherwise the value should be placed in bounds and returned.

**Parameters:**
- value

- the

value

to be represented
- row

- row being queried
- depth

- the depth of the row
- expanded

- true if row is expanded, false otherwise
- bounds

- a

Rectangle

containing the size needed
to represent

value

**Returns:**
- a

Rectangle

containing the node dimensions,
or

null

if node has no dimension

---

### Additional Sections

#### Class AbstractLayoutCache.NodeDimensions

java.lang.Object

- javax.swing.tree.AbstractLayoutCache.NodeDimensions

javax.swing.tree.AbstractLayoutCache.NodeDimensions

**Direct Known Subclasses:** BasicTreeUI.NodeDimensionsHandler

**Enclosing class:** AbstractLayoutCache

```java
public abstract static class
AbstractLayoutCache.NodeDimensions

extends
Object
```

Used by

AbstractLayoutCache

to determine the size
and x origin of a particular node.

public abstract static class

AbstractLayoutCache.NodeDimensions

extends

Object

Used by

AbstractLayoutCache

to determine the size
and x origin of a particular node.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

NodeDimensions

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

getNodeDimensions

​(

Object

value,
int row,
int depth,
boolean expanded,

Rectangle

bounds)

Returns, by reference in bounds, the size and x origin to
place value at.

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

NodeDimensions

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

getNodeDimensions

​(

Object

value,
int row,
int depth,
boolean expanded,

Rectangle

bounds)

Returns, by reference in bounds, the size and x origin to
place value at.

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

Returns, by reference in bounds, the size and x origin to
place value at.

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

- NodeDimensions

```java
public NodeDimensions()
```

============ METHOD DETAIL ==========

- Method Detail

- getNodeDimensions

```java
public abstract
Rectangle
getNodeDimensions​(
Object
value,
int row,
int depth,
boolean expanded,

Rectangle
bounds)
```

Returns, by reference in bounds, the size and x origin to
place value at. The calling method is responsible for determining
the Y location. If bounds is

null

, a newly created

Rectangle

should be returned,
otherwise the value should be placed in bounds and returned.

**Parameters:** value

- the

value

to be represented
**Parameters:** row

- row being queried
**Parameters:** depth

- the depth of the row
**Parameters:** expanded

- true if row is expanded, false otherwise
**Parameters:** bounds

- a

Rectangle

containing the size needed
to represent

value
**Returns:** a

Rectangle

containing the node dimensions,
or

null

if node has no dimension

Constructor Detail

- NodeDimensions

```java
public NodeDimensions()
```

---

#### Constructor Detail

NodeDimensions

```java
public NodeDimensions()
```

---

#### NodeDimensions

public NodeDimensions()

Method Detail

- getNodeDimensions

```java
public abstract
Rectangle
getNodeDimensions​(
Object
value,
int row,
int depth,
boolean expanded,

Rectangle
bounds)
```

Returns, by reference in bounds, the size and x origin to
place value at. The calling method is responsible for determining
the Y location. If bounds is

null

, a newly created

Rectangle

should be returned,
otherwise the value should be placed in bounds and returned.

**Parameters:** value

- the

value

to be represented
**Parameters:** row

- row being queried
**Parameters:** depth

- the depth of the row
**Parameters:** expanded

- true if row is expanded, false otherwise
**Parameters:** bounds

- a

Rectangle

containing the size needed
to represent

value
**Returns:** a

Rectangle

containing the node dimensions,
or

null

if node has no dimension

---

#### Method Detail

getNodeDimensions

```java
public abstract
Rectangle
getNodeDimensions​(
Object
value,
int row,
int depth,
boolean expanded,

Rectangle
bounds)
```

Returns, by reference in bounds, the size and x origin to
place value at. The calling method is responsible for determining
the Y location. If bounds is

null

, a newly created

Rectangle

should be returned,
otherwise the value should be placed in bounds and returned.

**Parameters:** value

- the

value

to be represented
**Parameters:** row

- row being queried
**Parameters:** depth

- the depth of the row
**Parameters:** expanded

- true if row is expanded, false otherwise
**Parameters:** bounds

- a

Rectangle

containing the size needed
to represent

value
**Returns:** a

Rectangle

containing the node dimensions,
or

null

if node has no dimension

---

#### getNodeDimensions

public abstract

Rectangle

getNodeDimensions​(

Object

value,
int row,
int depth,
boolean expanded,

Rectangle

bounds)

Returns, by reference in bounds, the size and x origin to
place value at. The calling method is responsible for determining
the Y location. If bounds is

null

, a newly created

Rectangle

should be returned,
otherwise the value should be placed in bounds and returned.

---

