# Interface DocumentTraversal

**Source:** `java.xml\org\w3c\dom\traversal\DocumentTraversal.html`

### Class Description

```java
public interface
DocumentTraversal
```

DocumentTraversal

contains methods that create

NodeIterators

and

TreeWalkers

to traverse a
node and its children in document order (depth first, pre-order
traversal, which is equivalent to the order in which the start tags occur
in the text representation of the document). In DOMs which support the
Traversal feature,

DocumentTraversal

will be implemented by
the same objects that implement the Document interface.

See also the

Document Object Model (DOM) Level 2 Traversal and Range Specification

.

**Since:** 9, DOM Level 2

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### NodeIterator
createNodeIterator​(
Node
root,
int whatToShow,

NodeFilter
filter,
boolean entityReferenceExpansion)
throws
DOMException

Create a new

NodeIterator

over the subtree rooted at the
specified node.

**Parameters:**
- root

- The node which will be iterated together with its
children. The

NodeIterator

is initially positioned
just before this node. The

whatToShow

flags and the
filter, if any, are not considered when setting this position. The
root must not be

null

.
- whatToShow

- This flag specifies which node types may appear in
the logical view of the tree presented by the

NodeIterator

. See the description of

NodeFilter

for the set of possible

SHOW_

values.These flags can be combined using

OR

.
- filter

- The

NodeFilter

to be used with this

NodeIterator

, or

null

to indicate no
filter.
- entityReferenceExpansion

- The value of this flag determines
whether entity reference nodes are expanded.

**Returns:**
- The newly created

NodeIterator

.

**Throws:**
- DOMException

- NOT_SUPPORTED_ERR: Raised if the specified

root

is

null

.

---

#### TreeWalker
createTreeWalker​(
Node
root,
int whatToShow,

NodeFilter
filter,
boolean entityReferenceExpansion)
throws
DOMException

Create a new

TreeWalker

over the subtree rooted at the
specified node.

**Parameters:**
- root

- The node which will serve as the

root

for the

TreeWalker

. The

whatToShow

flags and the

NodeFilter

are not considered when setting this value;
any node type will be accepted as the

root

. The

currentNode

of the

TreeWalker

is
initialized to this node, whether or not it is visible. The

root

functions as a stopping point for traversal
methods that look upward in the document structure, such as

parentNode

and nextNode. The

root

must
not be

null

.
- whatToShow

- This flag specifies which node types may appear in
the logical view of the tree presented by the

TreeWalker

. See the description of

NodeFilter

for the set of possible

SHOW_

values.These flags can be combined using

OR

.
- filter

- The

NodeFilter

to be used with this

TreeWalker

, or

null

to indicate no filter.
- entityReferenceExpansion

- If this flag is false, the contents of

EntityReference

nodes are not presented in the logical
view.

**Returns:**
- The newly created

TreeWalker

.

**Throws:**
- DOMException

- NOT_SUPPORTED_ERR: Raised if the specified

root

is

null

.

---

### Additional Sections

#### Interface DocumentTraversal

```java
public interface
DocumentTraversal
```

DocumentTraversal

contains methods that create

NodeIterators

and

TreeWalkers

to traverse a
node and its children in document order (depth first, pre-order
traversal, which is equivalent to the order in which the start tags occur
in the text representation of the document). In DOMs which support the
Traversal feature,

DocumentTraversal

will be implemented by
the same objects that implement the Document interface.

See also the

Document Object Model (DOM) Level 2 Traversal and Range Specification

.

**Since:** 9, DOM Level 2

public interface

DocumentTraversal

DocumentTraversal

contains methods that create

NodeIterators

and

TreeWalkers

to traverse a
node and its children in document order (depth first, pre-order
traversal, which is equivalent to the order in which the start tags occur
in the text representation of the document). In DOMs which support the
Traversal feature,

DocumentTraversal

will be implemented by
the same objects that implement the Document interface.

See also the

Document Object Model (DOM) Level 2 Traversal and Range Specification

.

See also the

Document Object Model (DOM) Level 2 Traversal and Range Specification

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

NodeIterator

createNodeIterator

​(

Node

root,
int whatToShow,

NodeFilter

filter,
boolean entityReferenceExpansion)

Create a new

NodeIterator

over the subtree rooted at the
specified node.

TreeWalker

createTreeWalker

​(

Node

root,
int whatToShow,

NodeFilter

filter,
boolean entityReferenceExpansion)

Create a new

TreeWalker

over the subtree rooted at the
specified node.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

NodeIterator

createNodeIterator

​(

Node

root,
int whatToShow,

NodeFilter

filter,
boolean entityReferenceExpansion)

Create a new

NodeIterator

over the subtree rooted at the
specified node.

TreeWalker

createTreeWalker

​(

Node

root,
int whatToShow,

NodeFilter

filter,
boolean entityReferenceExpansion)

Create a new

TreeWalker

over the subtree rooted at the
specified node.

---

#### Method Summary

Create a new

NodeIterator

over the subtree rooted at the
specified node.

Create a new

TreeWalker

over the subtree rooted at the
specified node.

============ METHOD DETAIL ==========

- Method Detail

- createNodeIterator

```java
NodeIterator
createNodeIterator​(
Node
root,
int whatToShow,

NodeFilter
filter,
boolean entityReferenceExpansion)
throws
DOMException
```

Create a new

NodeIterator

over the subtree rooted at the
specified node.

**Parameters:** root

- The node which will be iterated together with its
children. The

NodeIterator

is initially positioned
just before this node. The

whatToShow

flags and the
filter, if any, are not considered when setting this position. The
root must not be

null

.
**Parameters:** whatToShow

- This flag specifies which node types may appear in
the logical view of the tree presented by the

NodeIterator

. See the description of

NodeFilter

for the set of possible

SHOW_

values.These flags can be combined using

OR

.
**Parameters:** filter

- The

NodeFilter

to be used with this

NodeIterator

, or

null

to indicate no
filter.
**Parameters:** entityReferenceExpansion

- The value of this flag determines
whether entity reference nodes are expanded.
**Returns:** The newly created

NodeIterator

.
**Throws:** DOMException

- NOT_SUPPORTED_ERR: Raised if the specified

root

is

null

.

- createTreeWalker

```java
TreeWalker
createTreeWalker​(
Node
root,
int whatToShow,

NodeFilter
filter,
boolean entityReferenceExpansion)
throws
DOMException
```

Create a new

TreeWalker

over the subtree rooted at the
specified node.

**Parameters:** root

- The node which will serve as the

root

for the

TreeWalker

. The

whatToShow

flags and the

NodeFilter

are not considered when setting this value;
any node type will be accepted as the

root

. The

currentNode

of the

TreeWalker

is
initialized to this node, whether or not it is visible. The

root

functions as a stopping point for traversal
methods that look upward in the document structure, such as

parentNode

and nextNode. The

root

must
not be

null

.
**Parameters:** whatToShow

- This flag specifies which node types may appear in
the logical view of the tree presented by the

TreeWalker

. See the description of

NodeFilter

for the set of possible

SHOW_

values.These flags can be combined using

OR

.
**Parameters:** filter

- The

NodeFilter

to be used with this

TreeWalker

, or

null

to indicate no filter.
**Parameters:** entityReferenceExpansion

- If this flag is false, the contents of

EntityReference

nodes are not presented in the logical
view.
**Returns:** The newly created

TreeWalker

.
**Throws:** DOMException

- NOT_SUPPORTED_ERR: Raised if the specified

root

is

null

.

Method Detail

- createNodeIterator

```java
NodeIterator
createNodeIterator​(
Node
root,
int whatToShow,

NodeFilter
filter,
boolean entityReferenceExpansion)
throws
DOMException
```

Create a new

NodeIterator

over the subtree rooted at the
specified node.

**Parameters:** root

- The node which will be iterated together with its
children. The

NodeIterator

is initially positioned
just before this node. The

whatToShow

flags and the
filter, if any, are not considered when setting this position. The
root must not be

null

.
**Parameters:** whatToShow

- This flag specifies which node types may appear in
the logical view of the tree presented by the

NodeIterator

. See the description of

NodeFilter

for the set of possible

SHOW_

values.These flags can be combined using

OR

.
**Parameters:** filter

- The

NodeFilter

to be used with this

NodeIterator

, or

null

to indicate no
filter.
**Parameters:** entityReferenceExpansion

- The value of this flag determines
whether entity reference nodes are expanded.
**Returns:** The newly created

NodeIterator

.
**Throws:** DOMException

- NOT_SUPPORTED_ERR: Raised if the specified

root

is

null

.

- createTreeWalker

```java
TreeWalker
createTreeWalker​(
Node
root,
int whatToShow,

NodeFilter
filter,
boolean entityReferenceExpansion)
throws
DOMException
```

Create a new

TreeWalker

over the subtree rooted at the
specified node.

**Parameters:** root

- The node which will serve as the

root

for the

TreeWalker

. The

whatToShow

flags and the

NodeFilter

are not considered when setting this value;
any node type will be accepted as the

root

. The

currentNode

of the

TreeWalker

is
initialized to this node, whether or not it is visible. The

root

functions as a stopping point for traversal
methods that look upward in the document structure, such as

parentNode

and nextNode. The

root

must
not be

null

.
**Parameters:** whatToShow

- This flag specifies which node types may appear in
the logical view of the tree presented by the

TreeWalker

. See the description of

NodeFilter

for the set of possible

SHOW_

values.These flags can be combined using

OR

.
**Parameters:** filter

- The

NodeFilter

to be used with this

TreeWalker

, or

null

to indicate no filter.
**Parameters:** entityReferenceExpansion

- If this flag is false, the contents of

EntityReference

nodes are not presented in the logical
view.
**Returns:** The newly created

TreeWalker

.
**Throws:** DOMException

- NOT_SUPPORTED_ERR: Raised if the specified

root

is

null

.

---

#### Method Detail

createNodeIterator

```java
NodeIterator
createNodeIterator​(
Node
root,
int whatToShow,

NodeFilter
filter,
boolean entityReferenceExpansion)
throws
DOMException
```

Create a new

NodeIterator

over the subtree rooted at the
specified node.

**Parameters:** root

- The node which will be iterated together with its
children. The

NodeIterator

is initially positioned
just before this node. The

whatToShow

flags and the
filter, if any, are not considered when setting this position. The
root must not be

null

.
**Parameters:** whatToShow

- This flag specifies which node types may appear in
the logical view of the tree presented by the

NodeIterator

. See the description of

NodeFilter

for the set of possible

SHOW_

values.These flags can be combined using

OR

.
**Parameters:** filter

- The

NodeFilter

to be used with this

NodeIterator

, or

null

to indicate no
filter.
**Parameters:** entityReferenceExpansion

- The value of this flag determines
whether entity reference nodes are expanded.
**Returns:** The newly created

NodeIterator

.
**Throws:** DOMException

- NOT_SUPPORTED_ERR: Raised if the specified

root

is

null

.

---

#### createNodeIterator

NodeIterator

createNodeIterator​(

Node

root,
int whatToShow,

NodeFilter

filter,
boolean entityReferenceExpansion)
throws

DOMException

Create a new

NodeIterator

over the subtree rooted at the
specified node.

createTreeWalker

```java
TreeWalker
createTreeWalker​(
Node
root,
int whatToShow,

NodeFilter
filter,
boolean entityReferenceExpansion)
throws
DOMException
```

Create a new

TreeWalker

over the subtree rooted at the
specified node.

**Parameters:** root

- The node which will serve as the

root

for the

TreeWalker

. The

whatToShow

flags and the

NodeFilter

are not considered when setting this value;
any node type will be accepted as the

root

. The

currentNode

of the

TreeWalker

is
initialized to this node, whether or not it is visible. The

root

functions as a stopping point for traversal
methods that look upward in the document structure, such as

parentNode

and nextNode. The

root

must
not be

null

.
**Parameters:** whatToShow

- This flag specifies which node types may appear in
the logical view of the tree presented by the

TreeWalker

. See the description of

NodeFilter

for the set of possible

SHOW_

values.These flags can be combined using

OR

.
**Parameters:** filter

- The

NodeFilter

to be used with this

TreeWalker

, or

null

to indicate no filter.
**Parameters:** entityReferenceExpansion

- If this flag is false, the contents of

EntityReference

nodes are not presented in the logical
view.
**Returns:** The newly created

TreeWalker

.
**Throws:** DOMException

- NOT_SUPPORTED_ERR: Raised if the specified

root

is

null

.

---

#### createTreeWalker

TreeWalker

createTreeWalker​(

Node

root,
int whatToShow,

NodeFilter

filter,
boolean entityReferenceExpansion)
throws

DOMException

Create a new

TreeWalker

over the subtree rooted at the
specified node.

---

