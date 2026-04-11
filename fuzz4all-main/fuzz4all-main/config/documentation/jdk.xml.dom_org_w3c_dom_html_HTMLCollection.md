# Interface HTMLCollection

**Source:** `jdk.xml.dom\org\w3c\dom\html\HTMLCollection.html`

### Class Description

```java
public interface
HTMLCollection
```

An

HTMLCollection

is a list of nodes. An individual node may
be accessed by either ordinal index or the node's

name

or

id

attributes. Note: Collections in the HTML DOM are assumed
to be live meaning that they are automatically updated when the
underlying document is changed.

See also the

Document Object Model (DOM) Level 2 Specification

.

**Since:** 1.4, DOM Level 2

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### int getLength()

This attribute specifies the length or size of the list.

---

#### Node
item​(int index)

This method retrieves a node specified by ordinal index. Nodes are
numbered in tree order (depth-first traversal order).

**Parameters:**
- index

- The index of the node to be fetched. The index origin is
0.

**Returns:**
- The

Node

at the corresponding position upon
success. A value of

null

is returned if the index is
out of range.

---

#### Node
namedItem​(
String
name)

This method retrieves a

Node

using a name. It first
searches for a

Node

with a matching

id

attribute. If it doesn't find one, it then searches for a

Node

with a matching

name

attribute, but
only on those elements that are allowed a name attribute.

**Parameters:**
- name

- The name of the

Node

to be fetched.

**Returns:**
- The

Node

with a

name

or

id

attribute whose value corresponds to the specified
string. Upon failure (e.g., no node with this name exists), returns

null

.

---

### Additional Sections

#### Interface HTMLCollection

```java
public interface
HTMLCollection
```

An

HTMLCollection

is a list of nodes. An individual node may
be accessed by either ordinal index or the node's

name

or

id

attributes. Note: Collections in the HTML DOM are assumed
to be live meaning that they are automatically updated when the
underlying document is changed.

See also the

Document Object Model (DOM) Level 2 Specification

.

**Since:** 1.4, DOM Level 2

public interface

HTMLCollection

An

HTMLCollection

is a list of nodes. An individual node may
be accessed by either ordinal index or the node's

name

or

id

attributes. Note: Collections in the HTML DOM are assumed
to be live meaning that they are automatically updated when the
underlying document is changed.

See also the

Document Object Model (DOM) Level 2 Specification

.

See also the

Document Object Model (DOM) Level 2 Specification

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

This attribute specifies the length or size of the list.

Node

item

​(int index)

This method retrieves a node specified by ordinal index.

Node

namedItem

​(

String

name)

This method retrieves a

Node

using a name.

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

This attribute specifies the length or size of the list.

Node

item

​(int index)

This method retrieves a node specified by ordinal index.

Node

namedItem

​(

String

name)

This method retrieves a

Node

using a name.

---

#### Method Summary

This attribute specifies the length or size of the list.

This method retrieves a node specified by ordinal index.

This method retrieves a

Node

using a name.

============ METHOD DETAIL ==========

- Method Detail

- getLength

```java
int getLength()
```

This attribute specifies the length or size of the list.

- item

```java
Node
item​(int index)
```

This method retrieves a node specified by ordinal index. Nodes are
numbered in tree order (depth-first traversal order).

**Parameters:** index

- The index of the node to be fetched. The index origin is
0.
**Returns:** The

Node

at the corresponding position upon
success. A value of

null

is returned if the index is
out of range.

- namedItem

```java
Node
namedItem​(
String
name)
```

This method retrieves a

Node

using a name. It first
searches for a

Node

with a matching

id

attribute. If it doesn't find one, it then searches for a

Node

with a matching

name

attribute, but
only on those elements that are allowed a name attribute.

**Parameters:** name

- The name of the

Node

to be fetched.
**Returns:** The

Node

with a

name

or

id

attribute whose value corresponds to the specified
string. Upon failure (e.g., no node with this name exists), returns

null

.

Method Detail

- getLength

```java
int getLength()
```

This attribute specifies the length or size of the list.

- item

```java
Node
item​(int index)
```

This method retrieves a node specified by ordinal index. Nodes are
numbered in tree order (depth-first traversal order).

**Parameters:** index

- The index of the node to be fetched. The index origin is
0.
**Returns:** The

Node

at the corresponding position upon
success. A value of

null

is returned if the index is
out of range.

- namedItem

```java
Node
namedItem​(
String
name)
```

This method retrieves a

Node

using a name. It first
searches for a

Node

with a matching

id

attribute. If it doesn't find one, it then searches for a

Node

with a matching

name

attribute, but
only on those elements that are allowed a name attribute.

**Parameters:** name

- The name of the

Node

to be fetched.
**Returns:** The

Node

with a

name

or

id

attribute whose value corresponds to the specified
string. Upon failure (e.g., no node with this name exists), returns

null

.

---

#### Method Detail

getLength

```java
int getLength()
```

This attribute specifies the length or size of the list.

---

#### getLength

int getLength()

This attribute specifies the length or size of the list.

item

```java
Node
item​(int index)
```

This method retrieves a node specified by ordinal index. Nodes are
numbered in tree order (depth-first traversal order).

**Parameters:** index

- The index of the node to be fetched. The index origin is
0.
**Returns:** The

Node

at the corresponding position upon
success. A value of

null

is returned if the index is
out of range.

---

#### item

Node

item​(int index)

This method retrieves a node specified by ordinal index. Nodes are
numbered in tree order (depth-first traversal order).

namedItem

```java
Node
namedItem​(
String
name)
```

This method retrieves a

Node

using a name. It first
searches for a

Node

with a matching

id

attribute. If it doesn't find one, it then searches for a

Node

with a matching

name

attribute, but
only on those elements that are allowed a name attribute.

**Parameters:** name

- The name of the

Node

to be fetched.
**Returns:** The

Node

with a

name

or

id

attribute whose value corresponds to the specified
string. Upon failure (e.g., no node with this name exists), returns

null

.

---

#### namedItem

Node

namedItem​(

String

name)

This method retrieves a

Node

using a name. It first
searches for a

Node

with a matching

id

attribute. If it doesn't find one, it then searches for a

Node

with a matching

name

attribute, but
only on those elements that are allowed a name attribute.

---

