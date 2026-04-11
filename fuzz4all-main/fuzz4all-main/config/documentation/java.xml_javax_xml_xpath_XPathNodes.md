# Interface XPathNodes

**Source:** `java.xml\javax\xml\xpath\XPathNodes.html`

### Class Description

```java
public interface
XPathNodes

extends
Iterable
<
Node
>
```

XPathNodes represents a set of nodes selected by a location path as specified
in

XML Path Language (XPath)
Version 1.0, 3.3 Node-sets

.

**All Superinterfaces:** Iterable

<

Node

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Iterator
<
Node
> iterator()

Returns an iterator of the Nodes.

**Specified by:**
- iterator

in interface

Iterable

<

Node

>

**Returns:**
- an Iterator.

---

#### int size()

Returns the number of items in the result

**Returns:**
- The number of items in the result

---

#### Node
get​(int index)
throws
XPathException

Returns a Node at the specified position

**Parameters:**
- index

- Index of the element to return.

**Returns:**
- The Node at the specified position.

**Throws:**
- XPathException

- If the index is out of range
(index < 0 || index >= size())

---

### Additional Sections

#### Interface XPathNodes

**All Superinterfaces:** Iterable

<

Node

>

```java
public interface
XPathNodes

extends
Iterable
<
Node
>
```

XPathNodes represents a set of nodes selected by a location path as specified
in

XML Path Language (XPath)
Version 1.0, 3.3 Node-sets

.

**Since:** 9

public interface

XPathNodes

extends

Iterable

<

Node

>

XPathNodes represents a set of nodes selected by a location path as specified
in

XML Path Language (XPath)
Version 1.0, 3.3 Node-sets

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Node

get

​(int index)

Returns a Node at the specified position

Iterator

<

Node

>

iterator

()

Returns an iterator of the Nodes.

int

size

()

Returns the number of items in the result

- Methods declared in interface java.lang.

Iterable

forEach

,

spliterator

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Node

get

​(int index)

Returns a Node at the specified position

Iterator

<

Node

>

iterator

()

Returns an iterator of the Nodes.

int

size

()

Returns the number of items in the result

- Methods declared in interface java.lang.

Iterable

forEach

,

spliterator

---

#### Method Summary

Returns a Node at the specified position

Returns an iterator of the Nodes.

Returns the number of items in the result

Methods declared in interface java.lang.

Iterable

forEach

,

spliterator

---

#### Methods declared in interface java.lang. Iterable

============ METHOD DETAIL ==========

- Method Detail

- iterator

```java
Iterator
<
Node
> iterator()
```

Returns an iterator of the Nodes.

**Specified by:** iterator

in interface

Iterable

<

Node

>
**Returns:** an Iterator.

- size

```java
int size()
```

Returns the number of items in the result

**Returns:** The number of items in the result

- get

```java
Node
get​(int index)
throws
XPathException
```

Returns a Node at the specified position

**Parameters:** index

- Index of the element to return.
**Returns:** The Node at the specified position.
**Throws:** XPathException

- If the index is out of range
(index < 0 || index >= size())

Method Detail

- iterator

```java
Iterator
<
Node
> iterator()
```

Returns an iterator of the Nodes.

**Specified by:** iterator

in interface

Iterable

<

Node

>
**Returns:** an Iterator.

- size

```java
int size()
```

Returns the number of items in the result

**Returns:** The number of items in the result

- get

```java
Node
get​(int index)
throws
XPathException
```

Returns a Node at the specified position

**Parameters:** index

- Index of the element to return.
**Returns:** The Node at the specified position.
**Throws:** XPathException

- If the index is out of range
(index < 0 || index >= size())

---

#### Method Detail

iterator

```java
Iterator
<
Node
> iterator()
```

Returns an iterator of the Nodes.

**Specified by:** iterator

in interface

Iterable

<

Node

>
**Returns:** an Iterator.

---

#### iterator

Iterator

<

Node

> iterator()

Returns an iterator of the Nodes.

size

```java
int size()
```

Returns the number of items in the result

**Returns:** The number of items in the result

---

#### size

int size()

Returns the number of items in the result

get

```java
Node
get​(int index)
throws
XPathException
```

Returns a Node at the specified position

**Parameters:** index

- Index of the element to return.
**Returns:** The Node at the specified position.
**Throws:** XPathException

- If the index is out of range
(index < 0 || index >= size())

---

#### get

Node

get​(int index)
throws

XPathException

Returns a Node at the specified position

---

