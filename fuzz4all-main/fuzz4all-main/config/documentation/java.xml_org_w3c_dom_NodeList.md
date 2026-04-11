# Interface NodeList

**Source:** `java.xml\org\w3c\dom\NodeList.html`

### Class Description

```java
public interface
NodeList
```

The

NodeList

interface provides the abstraction of an ordered
collection of nodes, without defining or constraining how this collection
is implemented.

NodeList

objects in the DOM are live.

The items in the

NodeList

are accessible via an integral
index, starting from 0.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

**All Known Implementing Classes:** IIOMetadataNode

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Node
item​(int index)

Returns the

index

th item in the collection. If

index

is greater than or equal to the number of nodes in
the list, this returns

null

.

**Parameters:**
- index

- Index into the collection.

**Returns:**
- The node at the

index

th position in the

NodeList

, or

null

if that is not a valid
index.

---

#### int getLength()

The number of nodes in the list. The range of valid child node indices
is 0 to

length-1

inclusive.

---

### Additional Sections

#### Interface NodeList

**All Known Implementing Classes:** IIOMetadataNode

```java
public interface
NodeList
```

The

NodeList

interface provides the abstraction of an ordered
collection of nodes, without defining or constraining how this collection
is implemented.

NodeList

objects in the DOM are live.

The items in the

NodeList

are accessible via an integral
index, starting from 0.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

public interface

NodeList

The

NodeList

interface provides the abstraction of an ordered
collection of nodes, without defining or constraining how this collection
is implemented.

NodeList

objects in the DOM are live.

The items in the

NodeList

are accessible via an integral
index, starting from 0.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

The items in the

NodeList

are accessible via an integral
index, starting from 0.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getLength

()

The number of nodes in the list.

Node

item

​(int index)

Returns the

index

th item in the collection.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getLength

()

The number of nodes in the list.

Node

item

​(int index)

Returns the

index

th item in the collection.

---

#### Method Summary

The number of nodes in the list.

Returns the

index

th item in the collection.

============ METHOD DETAIL ==========

- Method Detail

- item

```java
Node
item​(int index)
```

Returns the

index

th item in the collection. If

index

is greater than or equal to the number of nodes in
the list, this returns

null

.

**Parameters:** index

- Index into the collection.
**Returns:** The node at the

index

th position in the

NodeList

, or

null

if that is not a valid
index.

- getLength

```java
int getLength()
```

The number of nodes in the list. The range of valid child node indices
is 0 to

length-1

inclusive.

Method Detail

- item

```java
Node
item​(int index)
```

Returns the

index

th item in the collection. If

index

is greater than or equal to the number of nodes in
the list, this returns

null

.

**Parameters:** index

- Index into the collection.
**Returns:** The node at the

index

th position in the

NodeList

, or

null

if that is not a valid
index.

- getLength

```java
int getLength()
```

The number of nodes in the list. The range of valid child node indices
is 0 to

length-1

inclusive.

---

#### Method Detail

item

```java
Node
item​(int index)
```

Returns the

index

th item in the collection. If

index

is greater than or equal to the number of nodes in
the list, this returns

null

.

**Parameters:** index

- Index into the collection.
**Returns:** The node at the

index

th position in the

NodeList

, or

null

if that is not a valid
index.

---

#### item

Node

item​(int index)

Returns the

index

th item in the collection. If

index

is greater than or equal to the number of nodes in
the list, this returns

null

.

getLength

```java
int getLength()
```

The number of nodes in the list. The range of valid child node indices
is 0 to

length-1

inclusive.

---

#### getLength

int getLength()

The number of nodes in the list. The range of valid child node indices
is 0 to

length-1

inclusive.

---

