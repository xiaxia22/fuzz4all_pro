# Interface TreeNode

**Source:** `java.desktop\javax\swing\tree\TreeNode.html`

### Class Description

```java
public interface
TreeNode
```

Defines the requirements for an object that can be used as a
tree node in a JTree.

Implementations of

TreeNode

that override

equals

will typically need to override

hashCode

as well. Refer
to

TreeModel

for more information.

For further information and examples of using tree nodes,
see

How to Use Tree Nodes

in

The Java Tutorial.

**All Known Subinterfaces:** MutableTreeNode

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### TreeNode
getChildAt​(int childIndex)

Returns the child

TreeNode

at index

childIndex

.

**Parameters:**
- childIndex

- index of child

**Returns:**
- the child node at given index

---

#### int getChildCount()

Returns the number of children

TreeNode

s the receiver
contains.

**Returns:**
- the number of children the receiver contains

---

#### TreeNode
getParent()

Returns the parent

TreeNode

of the receiver.

**Returns:**
- the parent of the receiver

---

#### int getIndex​(
TreeNode
node)

Returns the index of

node

in the receivers children.
If the receiver does not contain

node

, -1 will be
returned.

**Parameters:**
- node

- node to be loked for

**Returns:**
- index of specified node

---

#### boolean getAllowsChildren()

Returns true if the receiver allows children.

**Returns:**
- whether the receiver allows children

---

#### boolean isLeaf()

Returns true if the receiver is a leaf.

**Returns:**
- whether the receiver is a leaf

---

#### Enumeration
<? extends
TreeNode
> children()

Returns the children of the receiver as an

Enumeration

.

**Returns:**
- the children of the receiver as an

Enumeration

---

### Additional Sections

#### Interface TreeNode

**All Known Subinterfaces:** MutableTreeNode

**All Known Implementing Classes:** AbstractDocument.AbstractElement

,

AbstractDocument.BranchElement

,

AbstractDocument.LeafElement

,

DefaultMutableTreeNode

,

DefaultStyledDocument.SectionElement

,

HTMLDocument.BlockElement

,

HTMLDocument.RunElement

,

JTree.DynamicUtilTreeNode

```java
public interface
TreeNode
```

Defines the requirements for an object that can be used as a
tree node in a JTree.

Implementations of

TreeNode

that override

equals

will typically need to override

hashCode

as well. Refer
to

TreeModel

for more information.

For further information and examples of using tree nodes,
see

How to Use Tree Nodes

in

The Java Tutorial.

public interface

TreeNode

Defines the requirements for an object that can be used as a
tree node in a JTree.

Implementations of

TreeNode

that override

equals

will typically need to override

hashCode

as well. Refer
to

TreeModel

for more information.

For further information and examples of using tree nodes,
see

How to Use Tree Nodes

in

The Java Tutorial.

Implementations of

TreeNode

that override

equals

will typically need to override

hashCode

as well. Refer
to

TreeModel

for more information.

For further information and examples of using tree nodes,
see

How to Use Tree Nodes

in

The Java Tutorial.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Enumeration

<? extends

TreeNode

>

children

()

Returns the children of the receiver as an

Enumeration

.

boolean

getAllowsChildren

()

Returns true if the receiver allows children.

TreeNode

getChildAt

​(int childIndex)

Returns the child

TreeNode

at index

childIndex

.

int

getChildCount

()

Returns the number of children

TreeNode

s the receiver
contains.

int

getIndex

​(

TreeNode

node)

Returns the index of

node

in the receivers children.

TreeNode

getParent

()

Returns the parent

TreeNode

of the receiver.

boolean

isLeaf

()

Returns true if the receiver is a leaf.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Enumeration

<? extends

TreeNode

>

children

()

Returns the children of the receiver as an

Enumeration

.

boolean

getAllowsChildren

()

Returns true if the receiver allows children.

TreeNode

getChildAt

​(int childIndex)

Returns the child

TreeNode

at index

childIndex

.

int

getChildCount

()

Returns the number of children

TreeNode

s the receiver
contains.

int

getIndex

​(

TreeNode

node)

Returns the index of

node

in the receivers children.

TreeNode

getParent

()

Returns the parent

TreeNode

of the receiver.

boolean

isLeaf

()

Returns true if the receiver is a leaf.

---

#### Method Summary

Returns the children of the receiver as an

Enumeration

.

Returns true if the receiver allows children.

Returns the child

TreeNode

at index

childIndex

.

Returns the number of children

TreeNode

s the receiver
contains.

Returns the index of

node

in the receivers children.

Returns the parent

TreeNode

of the receiver.

Returns true if the receiver is a leaf.

============ METHOD DETAIL ==========

- Method Detail

- getChildAt

```java
TreeNode
getChildAt​(int childIndex)
```

Returns the child

TreeNode

at index

childIndex

.

**Parameters:** childIndex

- index of child
**Returns:** the child node at given index

- getChildCount

```java
int getChildCount()
```

Returns the number of children

TreeNode

s the receiver
contains.

**Returns:** the number of children the receiver contains

- getParent

```java
TreeNode
getParent()
```

Returns the parent

TreeNode

of the receiver.

**Returns:** the parent of the receiver

- getIndex

```java
int getIndex​(
TreeNode
node)
```

Returns the index of

node

in the receivers children.
If the receiver does not contain

node

, -1 will be
returned.

**Parameters:** node

- node to be loked for
**Returns:** index of specified node

- getAllowsChildren

```java
boolean getAllowsChildren()
```

Returns true if the receiver allows children.

**Returns:** whether the receiver allows children

- isLeaf

```java
boolean isLeaf()
```

Returns true if the receiver is a leaf.

**Returns:** whether the receiver is a leaf

- children

```java
Enumeration
<? extends
TreeNode
> children()
```

Returns the children of the receiver as an

Enumeration

.

**Returns:** the children of the receiver as an

Enumeration

Method Detail

- getChildAt

```java
TreeNode
getChildAt​(int childIndex)
```

Returns the child

TreeNode

at index

childIndex

.

**Parameters:** childIndex

- index of child
**Returns:** the child node at given index

- getChildCount

```java
int getChildCount()
```

Returns the number of children

TreeNode

s the receiver
contains.

**Returns:** the number of children the receiver contains

- getParent

```java
TreeNode
getParent()
```

Returns the parent

TreeNode

of the receiver.

**Returns:** the parent of the receiver

- getIndex

```java
int getIndex​(
TreeNode
node)
```

Returns the index of

node

in the receivers children.
If the receiver does not contain

node

, -1 will be
returned.

**Parameters:** node

- node to be loked for
**Returns:** index of specified node

- getAllowsChildren

```java
boolean getAllowsChildren()
```

Returns true if the receiver allows children.

**Returns:** whether the receiver allows children

- isLeaf

```java
boolean isLeaf()
```

Returns true if the receiver is a leaf.

**Returns:** whether the receiver is a leaf

- children

```java
Enumeration
<? extends
TreeNode
> children()
```

Returns the children of the receiver as an

Enumeration

.

**Returns:** the children of the receiver as an

Enumeration

---

#### Method Detail

getChildAt

```java
TreeNode
getChildAt​(int childIndex)
```

Returns the child

TreeNode

at index

childIndex

.

**Parameters:** childIndex

- index of child
**Returns:** the child node at given index

---

#### getChildAt

TreeNode

getChildAt​(int childIndex)

Returns the child

TreeNode

at index

childIndex

.

getChildCount

```java
int getChildCount()
```

Returns the number of children

TreeNode

s the receiver
contains.

**Returns:** the number of children the receiver contains

---

#### getChildCount

int getChildCount()

Returns the number of children

TreeNode

s the receiver
contains.

getParent

```java
TreeNode
getParent()
```

Returns the parent

TreeNode

of the receiver.

**Returns:** the parent of the receiver

---

#### getParent

TreeNode

getParent()

Returns the parent

TreeNode

of the receiver.

getIndex

```java
int getIndex​(
TreeNode
node)
```

Returns the index of

node

in the receivers children.
If the receiver does not contain

node

, -1 will be
returned.

**Parameters:** node

- node to be loked for
**Returns:** index of specified node

---

#### getIndex

int getIndex​(

TreeNode

node)

Returns the index of

node

in the receivers children.
If the receiver does not contain

node

, -1 will be
returned.

getAllowsChildren

```java
boolean getAllowsChildren()
```

Returns true if the receiver allows children.

**Returns:** whether the receiver allows children

---

#### getAllowsChildren

boolean getAllowsChildren()

Returns true if the receiver allows children.

isLeaf

```java
boolean isLeaf()
```

Returns true if the receiver is a leaf.

**Returns:** whether the receiver is a leaf

---

#### isLeaf

boolean isLeaf()

Returns true if the receiver is a leaf.

children

```java
Enumeration
<? extends
TreeNode
> children()
```

Returns the children of the receiver as an

Enumeration

.

**Returns:** the children of the receiver as an

Enumeration

---

#### children

Enumeration

<? extends

TreeNode

> children()

Returns the children of the receiver as an

Enumeration

.

---

