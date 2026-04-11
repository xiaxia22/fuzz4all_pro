# Interface NodeFilter

**Source:** `java.xml\org\w3c\dom\traversal\NodeFilter.html`

### Class Description

```java
public interface
NodeFilter
```

Filters are objects that know how to "filter out" nodes. If a

NodeIterator

or

TreeWalker

is given a

NodeFilter

, it applies the filter before it returns the next
node. If the filter says to accept the node, the traversal logic returns
it; otherwise, traversal looks for the next node and pretends that the
node that was rejected was not there.

The DOM does not provide any filters.

NodeFilter

is just an
interface that users can implement to provide their own filters.

NodeFilters

do not need to know how to traverse from node
to node, nor do they need to know anything about the data structure that
is being traversed. This makes it very easy to write filters, since the
only thing they have to know how to do is evaluate a single node. One
filter may be used with a number of different kinds of traversals,
encouraging code reuse.

See also the

Document Object Model (DOM) Level 2 Traversal and Range Specification

.

**All Known Subinterfaces:** LSSerializerFilter

---

### Field Details

#### static final short FILTER_ACCEPT

Accept the node. Navigation methods defined for

NodeIterator

or

TreeWalker

will return this
node.

**See Also:**
- Constant Field Values

---

#### static final short FILTER_REJECT

Reject the node. Navigation methods defined for

NodeIterator

or

TreeWalker

will not return
this node. For

TreeWalker

, the children of this node
will also be rejected.

NodeIterators

treat this as a
synonym for

FILTER_SKIP

.

**See Also:**
- Constant Field Values

---

#### static final short FILTER_SKIP

Skip this single node. Navigation methods defined for

NodeIterator

or

TreeWalker

will not return
this node. For both

NodeIterator

and

TreeWalker

, the children of this node will still be
considered.

**See Also:**
- Constant Field Values

---

#### static final int SHOW_ALL

Show all

Nodes

.

**See Also:**
- Constant Field Values

---

#### static final int SHOW_ELEMENT

Show

Element

nodes.

**See Also:**
- Constant Field Values

---

#### static final int SHOW_ATTRIBUTE

Show

Attr

nodes. This is meaningful only when creating an

NodeIterator

or

TreeWalker

with an
attribute node as its

root

; in this case, it means that
the attribute node will appear in the first position of the iteration
or traversal. Since attributes are never children of other nodes,
they do not appear when traversing over the document tree.

**See Also:**
- Constant Field Values

---

#### static final int SHOW_TEXT

Show

Text

nodes.

**See Also:**
- Constant Field Values

---

#### static final int SHOW_CDATA_SECTION

Show

CDATASection

nodes.

**See Also:**
- Constant Field Values

---

#### static final int SHOW_ENTITY_REFERENCE

Show

EntityReference

nodes.

**See Also:**
- Constant Field Values

---

#### static final int SHOW_ENTITY

Show

Entity

nodes. This is meaningful only when creating
an

NodeIterator

or

TreeWalker

with an

Entity

node as its

root

; in this case, it
means that the

Entity

node will appear in the first
position of the traversal. Since entities are not part of the
document tree, they do not appear when traversing over the document
tree.

**See Also:**
- Constant Field Values

---

#### static final int SHOW_PROCESSING_INSTRUCTION

Show

ProcessingInstruction

nodes.

**See Also:**
- Constant Field Values

---

#### static final int SHOW_COMMENT

Show

Comment

nodes.

**See Also:**
- Constant Field Values

---

#### static final int SHOW_DOCUMENT

Show

Document

nodes.

**See Also:**
- Constant Field Values

---

#### static final int SHOW_DOCUMENT_TYPE

Show

DocumentType

nodes.

**See Also:**
- Constant Field Values

---

#### static final int SHOW_DOCUMENT_FRAGMENT

Show

DocumentFragment

nodes.

**See Also:**
- Constant Field Values

---

#### static final int SHOW_NOTATION

Show

Notation

nodes. This is meaningful only when creating
an

NodeIterator

or

TreeWalker

with a

Notation

node as its

root

; in this case, it
means that the

Notation

node will appear in the first
position of the traversal. Since notations are not part of the
document tree, they do not appear when traversing over the document
tree.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### short acceptNode​(
Node
n)

Test whether a specified node is visible in the logical view of a

TreeWalker

or

NodeIterator

. This function
will be called by the implementation of

TreeWalker

and

NodeIterator

; it is not normally called directly from
user code. (Though you could do so if you wanted to use the same
filter to guide your own application logic.)

**Parameters:**
- n

- The node to check to see if it passes the filter or not.

**Returns:**
- A constant to determine whether the node is accepted,
rejected, or skipped, as defined above.

---

### Additional Sections

#### Interface NodeFilter

**All Known Subinterfaces:** LSSerializerFilter

```java
public interface
NodeFilter
```

Filters are objects that know how to "filter out" nodes. If a

NodeIterator

or

TreeWalker

is given a

NodeFilter

, it applies the filter before it returns the next
node. If the filter says to accept the node, the traversal logic returns
it; otherwise, traversal looks for the next node and pretends that the
node that was rejected was not there.

The DOM does not provide any filters.

NodeFilter

is just an
interface that users can implement to provide their own filters.

NodeFilters

do not need to know how to traverse from node
to node, nor do they need to know anything about the data structure that
is being traversed. This makes it very easy to write filters, since the
only thing they have to know how to do is evaluate a single node. One
filter may be used with a number of different kinds of traversals,
encouraging code reuse.

See also the

Document Object Model (DOM) Level 2 Traversal and Range Specification

.

**Since:** 9, DOM Level 2

public interface

NodeFilter

Filters are objects that know how to "filter out" nodes. If a

NodeIterator

or

TreeWalker

is given a

NodeFilter

, it applies the filter before it returns the next
node. If the filter says to accept the node, the traversal logic returns
it; otherwise, traversal looks for the next node and pretends that the
node that was rejected was not there.

The DOM does not provide any filters.

NodeFilter

is just an
interface that users can implement to provide their own filters.

NodeFilters

do not need to know how to traverse from node
to node, nor do they need to know anything about the data structure that
is being traversed. This makes it very easy to write filters, since the
only thing they have to know how to do is evaluate a single node. One
filter may be used with a number of different kinds of traversals,
encouraging code reuse.

See also the

Document Object Model (DOM) Level 2 Traversal and Range Specification

.

The DOM does not provide any filters.

NodeFilter

is just an
interface that users can implement to provide their own filters.

NodeFilters

do not need to know how to traverse from node
to node, nor do they need to know anything about the data structure that
is being traversed. This makes it very easy to write filters, since the
only thing they have to know how to do is evaluate a single node. One
filter may be used with a number of different kinds of traversals,
encouraging code reuse.

See also the

Document Object Model (DOM) Level 2 Traversal and Range Specification

.

NodeFilters

do not need to know how to traverse from node
to node, nor do they need to know anything about the data structure that
is being traversed. This makes it very easy to write filters, since the
only thing they have to know how to do is evaluate a single node. One
filter may be used with a number of different kinds of traversals,
encouraging code reuse.

See also the

Document Object Model (DOM) Level 2 Traversal and Range Specification

.

See also the

Document Object Model (DOM) Level 2 Traversal and Range Specification

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static short

FILTER_ACCEPT

Accept the node.

static short

FILTER_REJECT

Reject the node.

static short

FILTER_SKIP

Skip this single node.

static int

SHOW_ALL

Show all

Nodes

.

static int

SHOW_ATTRIBUTE

Show

Attr

nodes.

static int

SHOW_CDATA_SECTION

Show

CDATASection

nodes.

static int

SHOW_COMMENT

Show

Comment

nodes.

static int

SHOW_DOCUMENT

Show

Document

nodes.

static int

SHOW_DOCUMENT_FRAGMENT

Show

DocumentFragment

nodes.

static int

SHOW_DOCUMENT_TYPE

Show

DocumentType

nodes.

static int

SHOW_ELEMENT

Show

Element

nodes.

static int

SHOW_ENTITY

Show

Entity

nodes.

static int

SHOW_ENTITY_REFERENCE

Show

EntityReference

nodes.

static int

SHOW_NOTATION

Show

Notation

nodes.

static int

SHOW_PROCESSING_INSTRUCTION

Show

ProcessingInstruction

nodes.

static int

SHOW_TEXT

Show

Text

nodes.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

short

acceptNode

​(

Node

n)

Test whether a specified node is visible in the logical view of a

TreeWalker

or

NodeIterator

.

Field Summary

Fields

Modifier and Type

Field

Description

static short

FILTER_ACCEPT

Accept the node.

static short

FILTER_REJECT

Reject the node.

static short

FILTER_SKIP

Skip this single node.

static int

SHOW_ALL

Show all

Nodes

.

static int

SHOW_ATTRIBUTE

Show

Attr

nodes.

static int

SHOW_CDATA_SECTION

Show

CDATASection

nodes.

static int

SHOW_COMMENT

Show

Comment

nodes.

static int

SHOW_DOCUMENT

Show

Document

nodes.

static int

SHOW_DOCUMENT_FRAGMENT

Show

DocumentFragment

nodes.

static int

SHOW_DOCUMENT_TYPE

Show

DocumentType

nodes.

static int

SHOW_ELEMENT

Show

Element

nodes.

static int

SHOW_ENTITY

Show

Entity

nodes.

static int

SHOW_ENTITY_REFERENCE

Show

EntityReference

nodes.

static int

SHOW_NOTATION

Show

Notation

nodes.

static int

SHOW_PROCESSING_INSTRUCTION

Show

ProcessingInstruction

nodes.

static int

SHOW_TEXT

Show

Text

nodes.

---

#### Field Summary

Accept the node.

Reject the node.

Skip this single node.

Show all

Nodes

.

Show

Attr

nodes.

Show

CDATASection

nodes.

Show

Comment

nodes.

Show

Document

nodes.

Show

DocumentFragment

nodes.

Show

DocumentType

nodes.

Show

Element

nodes.

Show

Entity

nodes.

Show

EntityReference

nodes.

Show

Notation

nodes.

Show

ProcessingInstruction

nodes.

Show

Text

nodes.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

short

acceptNode

​(

Node

n)

Test whether a specified node is visible in the logical view of a

TreeWalker

or

NodeIterator

.

---

#### Method Summary

Test whether a specified node is visible in the logical view of a

TreeWalker

or

NodeIterator

.

============ FIELD DETAIL ===========

- Field Detail

- FILTER_ACCEPT

```java
static final short FILTER_ACCEPT
```

Accept the node. Navigation methods defined for

NodeIterator

or

TreeWalker

will return this
node.

**See Also:** Constant Field Values

- FILTER_REJECT

```java
static final short FILTER_REJECT
```

Reject the node. Navigation methods defined for

NodeIterator

or

TreeWalker

will not return
this node. For

TreeWalker

, the children of this node
will also be rejected.

NodeIterators

treat this as a
synonym for

FILTER_SKIP

.

**See Also:** Constant Field Values

- FILTER_SKIP

```java
static final short FILTER_SKIP
```

Skip this single node. Navigation methods defined for

NodeIterator

or

TreeWalker

will not return
this node. For both

NodeIterator

and

TreeWalker

, the children of this node will still be
considered.

**See Also:** Constant Field Values

- SHOW_ALL

```java
static final int SHOW_ALL
```

Show all

Nodes

.

**See Also:** Constant Field Values

- SHOW_ELEMENT

```java
static final int SHOW_ELEMENT
```

Show

Element

nodes.

**See Also:** Constant Field Values

- SHOW_ATTRIBUTE

```java
static final int SHOW_ATTRIBUTE
```

Show

Attr

nodes. This is meaningful only when creating an

NodeIterator

or

TreeWalker

with an
attribute node as its

root

; in this case, it means that
the attribute node will appear in the first position of the iteration
or traversal. Since attributes are never children of other nodes,
they do not appear when traversing over the document tree.

**See Also:** Constant Field Values

- SHOW_TEXT

```java
static final int SHOW_TEXT
```

Show

Text

nodes.

**See Also:** Constant Field Values

- SHOW_CDATA_SECTION

```java
static final int SHOW_CDATA_SECTION
```

Show

CDATASection

nodes.

**See Also:** Constant Field Values

- SHOW_ENTITY_REFERENCE

```java
static final int SHOW_ENTITY_REFERENCE
```

Show

EntityReference

nodes.

**See Also:** Constant Field Values

- SHOW_ENTITY

```java
static final int SHOW_ENTITY
```

Show

Entity

nodes. This is meaningful only when creating
an

NodeIterator

or

TreeWalker

with an

Entity

node as its

root

; in this case, it
means that the

Entity

node will appear in the first
position of the traversal. Since entities are not part of the
document tree, they do not appear when traversing over the document
tree.

**See Also:** Constant Field Values

- SHOW_PROCESSING_INSTRUCTION

```java
static final int SHOW_PROCESSING_INSTRUCTION
```

Show

ProcessingInstruction

nodes.

**See Also:** Constant Field Values

- SHOW_COMMENT

```java
static final int SHOW_COMMENT
```

Show

Comment

nodes.

**See Also:** Constant Field Values

- SHOW_DOCUMENT

```java
static final int SHOW_DOCUMENT
```

Show

Document

nodes.

**See Also:** Constant Field Values

- SHOW_DOCUMENT_TYPE

```java
static final int SHOW_DOCUMENT_TYPE
```

Show

DocumentType

nodes.

**See Also:** Constant Field Values

- SHOW_DOCUMENT_FRAGMENT

```java
static final int SHOW_DOCUMENT_FRAGMENT
```

Show

DocumentFragment

nodes.

**See Also:** Constant Field Values

- SHOW_NOTATION

```java
static final int SHOW_NOTATION
```

Show

Notation

nodes. This is meaningful only when creating
an

NodeIterator

or

TreeWalker

with a

Notation

node as its

root

; in this case, it
means that the

Notation

node will appear in the first
position of the traversal. Since notations are not part of the
document tree, they do not appear when traversing over the document
tree.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- acceptNode

```java
short acceptNode​(
Node
n)
```

Test whether a specified node is visible in the logical view of a

TreeWalker

or

NodeIterator

. This function
will be called by the implementation of

TreeWalker

and

NodeIterator

; it is not normally called directly from
user code. (Though you could do so if you wanted to use the same
filter to guide your own application logic.)

**Parameters:** n

- The node to check to see if it passes the filter or not.
**Returns:** A constant to determine whether the node is accepted,
rejected, or skipped, as defined above.

Field Detail

- FILTER_ACCEPT

```java
static final short FILTER_ACCEPT
```

Accept the node. Navigation methods defined for

NodeIterator

or

TreeWalker

will return this
node.

**See Also:** Constant Field Values

- FILTER_REJECT

```java
static final short FILTER_REJECT
```

Reject the node. Navigation methods defined for

NodeIterator

or

TreeWalker

will not return
this node. For

TreeWalker

, the children of this node
will also be rejected.

NodeIterators

treat this as a
synonym for

FILTER_SKIP

.

**See Also:** Constant Field Values

- FILTER_SKIP

```java
static final short FILTER_SKIP
```

Skip this single node. Navigation methods defined for

NodeIterator

or

TreeWalker

will not return
this node. For both

NodeIterator

and

TreeWalker

, the children of this node will still be
considered.

**See Also:** Constant Field Values

- SHOW_ALL

```java
static final int SHOW_ALL
```

Show all

Nodes

.

**See Also:** Constant Field Values

- SHOW_ELEMENT

```java
static final int SHOW_ELEMENT
```

Show

Element

nodes.

**See Also:** Constant Field Values

- SHOW_ATTRIBUTE

```java
static final int SHOW_ATTRIBUTE
```

Show

Attr

nodes. This is meaningful only when creating an

NodeIterator

or

TreeWalker

with an
attribute node as its

root

; in this case, it means that
the attribute node will appear in the first position of the iteration
or traversal. Since attributes are never children of other nodes,
they do not appear when traversing over the document tree.

**See Also:** Constant Field Values

- SHOW_TEXT

```java
static final int SHOW_TEXT
```

Show

Text

nodes.

**See Also:** Constant Field Values

- SHOW_CDATA_SECTION

```java
static final int SHOW_CDATA_SECTION
```

Show

CDATASection

nodes.

**See Also:** Constant Field Values

- SHOW_ENTITY_REFERENCE

```java
static final int SHOW_ENTITY_REFERENCE
```

Show

EntityReference

nodes.

**See Also:** Constant Field Values

- SHOW_ENTITY

```java
static final int SHOW_ENTITY
```

Show

Entity

nodes. This is meaningful only when creating
an

NodeIterator

or

TreeWalker

with an

Entity

node as its

root

; in this case, it
means that the

Entity

node will appear in the first
position of the traversal. Since entities are not part of the
document tree, they do not appear when traversing over the document
tree.

**See Also:** Constant Field Values

- SHOW_PROCESSING_INSTRUCTION

```java
static final int SHOW_PROCESSING_INSTRUCTION
```

Show

ProcessingInstruction

nodes.

**See Also:** Constant Field Values

- SHOW_COMMENT

```java
static final int SHOW_COMMENT
```

Show

Comment

nodes.

**See Also:** Constant Field Values

- SHOW_DOCUMENT

```java
static final int SHOW_DOCUMENT
```

Show

Document

nodes.

**See Also:** Constant Field Values

- SHOW_DOCUMENT_TYPE

```java
static final int SHOW_DOCUMENT_TYPE
```

Show

DocumentType

nodes.

**See Also:** Constant Field Values

- SHOW_DOCUMENT_FRAGMENT

```java
static final int SHOW_DOCUMENT_FRAGMENT
```

Show

DocumentFragment

nodes.

**See Also:** Constant Field Values

- SHOW_NOTATION

```java
static final int SHOW_NOTATION
```

Show

Notation

nodes. This is meaningful only when creating
an

NodeIterator

or

TreeWalker

with a

Notation

node as its

root

; in this case, it
means that the

Notation

node will appear in the first
position of the traversal. Since notations are not part of the
document tree, they do not appear when traversing over the document
tree.

**See Also:** Constant Field Values

---

#### Field Detail

FILTER_ACCEPT

```java
static final short FILTER_ACCEPT
```

Accept the node. Navigation methods defined for

NodeIterator

or

TreeWalker

will return this
node.

**See Also:** Constant Field Values

---

#### FILTER_ACCEPT

static final short FILTER_ACCEPT

Accept the node. Navigation methods defined for

NodeIterator

or

TreeWalker

will return this
node.

FILTER_REJECT

```java
static final short FILTER_REJECT
```

Reject the node. Navigation methods defined for

NodeIterator

or

TreeWalker

will not return
this node. For

TreeWalker

, the children of this node
will also be rejected.

NodeIterators

treat this as a
synonym for

FILTER_SKIP

.

**See Also:** Constant Field Values

---

#### FILTER_REJECT

static final short FILTER_REJECT

Reject the node. Navigation methods defined for

NodeIterator

or

TreeWalker

will not return
this node. For

TreeWalker

, the children of this node
will also be rejected.

NodeIterators

treat this as a
synonym for

FILTER_SKIP

.

FILTER_SKIP

```java
static final short FILTER_SKIP
```

Skip this single node. Navigation methods defined for

NodeIterator

or

TreeWalker

will not return
this node. For both

NodeIterator

and

TreeWalker

, the children of this node will still be
considered.

**See Also:** Constant Field Values

---

#### FILTER_SKIP

static final short FILTER_SKIP

Skip this single node. Navigation methods defined for

NodeIterator

or

TreeWalker

will not return
this node. For both

NodeIterator

and

TreeWalker

, the children of this node will still be
considered.

SHOW_ALL

```java
static final int SHOW_ALL
```

Show all

Nodes

.

**See Also:** Constant Field Values

---

#### SHOW_ALL

static final int SHOW_ALL

Show all

Nodes

.

SHOW_ELEMENT

```java
static final int SHOW_ELEMENT
```

Show

Element

nodes.

**See Also:** Constant Field Values

---

#### SHOW_ELEMENT

static final int SHOW_ELEMENT

Show

Element

nodes.

SHOW_ATTRIBUTE

```java
static final int SHOW_ATTRIBUTE
```

Show

Attr

nodes. This is meaningful only when creating an

NodeIterator

or

TreeWalker

with an
attribute node as its

root

; in this case, it means that
the attribute node will appear in the first position of the iteration
or traversal. Since attributes are never children of other nodes,
they do not appear when traversing over the document tree.

**See Also:** Constant Field Values

---

#### SHOW_ATTRIBUTE

static final int SHOW_ATTRIBUTE

Show

Attr

nodes. This is meaningful only when creating an

NodeIterator

or

TreeWalker

with an
attribute node as its

root

; in this case, it means that
the attribute node will appear in the first position of the iteration
or traversal. Since attributes are never children of other nodes,
they do not appear when traversing over the document tree.

SHOW_TEXT

```java
static final int SHOW_TEXT
```

Show

Text

nodes.

**See Also:** Constant Field Values

---

#### SHOW_TEXT

static final int SHOW_TEXT

Show

Text

nodes.

SHOW_CDATA_SECTION

```java
static final int SHOW_CDATA_SECTION
```

Show

CDATASection

nodes.

**See Also:** Constant Field Values

---

#### SHOW_CDATA_SECTION

static final int SHOW_CDATA_SECTION

Show

CDATASection

nodes.

SHOW_ENTITY_REFERENCE

```java
static final int SHOW_ENTITY_REFERENCE
```

Show

EntityReference

nodes.

**See Also:** Constant Field Values

---

#### SHOW_ENTITY_REFERENCE

static final int SHOW_ENTITY_REFERENCE

Show

EntityReference

nodes.

SHOW_ENTITY

```java
static final int SHOW_ENTITY
```

Show

Entity

nodes. This is meaningful only when creating
an

NodeIterator

or

TreeWalker

with an

Entity

node as its

root

; in this case, it
means that the

Entity

node will appear in the first
position of the traversal. Since entities are not part of the
document tree, they do not appear when traversing over the document
tree.

**See Also:** Constant Field Values

---

#### SHOW_ENTITY

static final int SHOW_ENTITY

Show

Entity

nodes. This is meaningful only when creating
an

NodeIterator

or

TreeWalker

with an

Entity

node as its

root

; in this case, it
means that the

Entity

node will appear in the first
position of the traversal. Since entities are not part of the
document tree, they do not appear when traversing over the document
tree.

SHOW_PROCESSING_INSTRUCTION

```java
static final int SHOW_PROCESSING_INSTRUCTION
```

Show

ProcessingInstruction

nodes.

**See Also:** Constant Field Values

---

#### SHOW_PROCESSING_INSTRUCTION

static final int SHOW_PROCESSING_INSTRUCTION

Show

ProcessingInstruction

nodes.

SHOW_COMMENT

```java
static final int SHOW_COMMENT
```

Show

Comment

nodes.

**See Also:** Constant Field Values

---

#### SHOW_COMMENT

static final int SHOW_COMMENT

Show

Comment

nodes.

SHOW_DOCUMENT

```java
static final int SHOW_DOCUMENT
```

Show

Document

nodes.

**See Also:** Constant Field Values

---

#### SHOW_DOCUMENT

static final int SHOW_DOCUMENT

Show

Document

nodes.

SHOW_DOCUMENT_TYPE

```java
static final int SHOW_DOCUMENT_TYPE
```

Show

DocumentType

nodes.

**See Also:** Constant Field Values

---

#### SHOW_DOCUMENT_TYPE

static final int SHOW_DOCUMENT_TYPE

Show

DocumentType

nodes.

SHOW_DOCUMENT_FRAGMENT

```java
static final int SHOW_DOCUMENT_FRAGMENT
```

Show

DocumentFragment

nodes.

**See Also:** Constant Field Values

---

#### SHOW_DOCUMENT_FRAGMENT

static final int SHOW_DOCUMENT_FRAGMENT

Show

DocumentFragment

nodes.

SHOW_NOTATION

```java
static final int SHOW_NOTATION
```

Show

Notation

nodes. This is meaningful only when creating
an

NodeIterator

or

TreeWalker

with a

Notation

node as its

root

; in this case, it
means that the

Notation

node will appear in the first
position of the traversal. Since notations are not part of the
document tree, they do not appear when traversing over the document
tree.

**See Also:** Constant Field Values

---

#### SHOW_NOTATION

static final int SHOW_NOTATION

Show

Notation

nodes. This is meaningful only when creating
an

NodeIterator

or

TreeWalker

with a

Notation

node as its

root

; in this case, it
means that the

Notation

node will appear in the first
position of the traversal. Since notations are not part of the
document tree, they do not appear when traversing over the document
tree.

Method Detail

- acceptNode

```java
short acceptNode​(
Node
n)
```

Test whether a specified node is visible in the logical view of a

TreeWalker

or

NodeIterator

. This function
will be called by the implementation of

TreeWalker

and

NodeIterator

; it is not normally called directly from
user code. (Though you could do so if you wanted to use the same
filter to guide your own application logic.)

**Parameters:** n

- The node to check to see if it passes the filter or not.
**Returns:** A constant to determine whether the node is accepted,
rejected, or skipped, as defined above.

---

#### Method Detail

acceptNode

```java
short acceptNode​(
Node
n)
```

Test whether a specified node is visible in the logical view of a

TreeWalker

or

NodeIterator

. This function
will be called by the implementation of

TreeWalker

and

NodeIterator

; it is not normally called directly from
user code. (Though you could do so if you wanted to use the same
filter to guide your own application logic.)

**Parameters:** n

- The node to check to see if it passes the filter or not.
**Returns:** A constant to determine whether the node is accepted,
rejected, or skipped, as defined above.

---

#### acceptNode

short acceptNode​(

Node

n)

Test whether a specified node is visible in the logical view of a

TreeWalker

or

NodeIterator

. This function
will be called by the implementation of

TreeWalker

and

NodeIterator

; it is not normally called directly from
user code. (Though you could do so if you wanted to use the same
filter to guide your own application logic.)

---

