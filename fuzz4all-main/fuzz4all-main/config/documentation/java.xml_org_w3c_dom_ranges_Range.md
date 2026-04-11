# Interface Range

**Source:** `java.xml\org\w3c\dom\ranges\Range.html`

### Class Description

```java
public interface
Range
```

See also the

Document Object Model (DOM) Level 2 Traversal and Range Specification

.

**Since:** 9, DOM Level 2

---

### Field Details

#### static final short START_TO_START

Compare start boundary-point of

sourceRange

to start
boundary-point of Range on which

compareBoundaryPoints

is invoked.

**See Also:**
- Constant Field Values

---

#### static final short START_TO_END

Compare start boundary-point of

sourceRange

to end
boundary-point of Range on which

compareBoundaryPoints

is invoked.

**See Also:**
- Constant Field Values

---

#### static final short END_TO_END

Compare end boundary-point of

sourceRange

to end
boundary-point of Range on which

compareBoundaryPoints

is invoked.

**See Also:**
- Constant Field Values

---

#### static final short END_TO_START

Compare end boundary-point of

sourceRange

to start
boundary-point of Range on which

compareBoundaryPoints

is invoked.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### Node
getStartContainer()
throws
DOMException

Node within which the Range begins

**Throws:**
- DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

---

#### int getStartOffset()
throws
DOMException

Offset within the starting node of the Range.

**Throws:**
- DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

---

#### Node
getEndContainer()
throws
DOMException

Node within which the Range ends

**Throws:**
- DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

---

#### int getEndOffset()
throws
DOMException

Offset within the ending node of the Range.

**Throws:**
- DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

---

#### boolean getCollapsed()
throws
DOMException

TRUE if the Range is collapsed

**Throws:**
- DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

---

#### Node
getCommonAncestorContainer()
throws
DOMException

The deepest common ancestor container of the Range's two
boundary-points.

**Throws:**
- DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

---

#### void setStart​(
Node
refNode,
int offset)
throws
RangeException
,

DOMException

Sets the attributes describing the start of the Range.

**Parameters:**
- refNode

- The

refNode

value. This parameter must be
different from

null

.
- offset

- The

startOffset

value.

**Throws:**
- RangeException

- INVALID_NODE_TYPE_ERR: Raised if

refNode

or an ancestor
of

refNode

is an Entity, Notation, or DocumentType
node.
- DOMException

- INDEX_SIZE_ERR: Raised if

offset

is negative or greater
than the number of child units in

refNode

. Child units
are 16-bit units if

refNode

is a type of CharacterData
node (e.g., a Text or Comment node) or a ProcessingInstruction
node. Child units are Nodes in all other cases.

INVALID_STATE_ERR: Raised if

detach()

has already
been invoked on this object.

WRONG_DOCUMENT_ERR: Raised if

refNode

was created
from a different document than the one that created this range.

---

#### void setEnd​(
Node
refNode,
int offset)
throws
RangeException
,

DOMException

Sets the attributes describing the end of a Range.

**Parameters:**
- refNode

- The

refNode

value. This parameter must be
different from

null

.
- offset

- The

endOffset

value.

**Throws:**
- RangeException

- INVALID_NODE_TYPE_ERR: Raised if

refNode

or an ancestor
of

refNode

is an Entity, Notation, or DocumentType
node.
- DOMException

- INDEX_SIZE_ERR: Raised if

offset

is negative or greater
than the number of child units in

refNode

. Child units
are 16-bit units if

refNode

is a type of CharacterData
node (e.g., a Text or Comment node) or a ProcessingInstruction
node. Child units are Nodes in all other cases.

INVALID_STATE_ERR: Raised if

detach()

has already
been invoked on this object.

WRONG_DOCUMENT_ERR: Raised if

refNode

was created
from a different document than the one that created this range.

---

#### void setStartBefore​(
Node
refNode)
throws
RangeException
,

DOMException

Sets the start position to be before a node

**Parameters:**
- refNode

- Range starts before

refNode

**Throws:**
- RangeException

- INVALID_NODE_TYPE_ERR: Raised if the root container of

refNode

is not an Attr, Document, or DocumentFragment
node or if

refNode

is a Document, DocumentFragment,
Attr, Entity, or Notation node.
- DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

WRONG_DOCUMENT_ERR: Raised if

refNode

was created
from a different document than the one that created this range.

---

#### void setStartAfter​(
Node
refNode)
throws
RangeException
,

DOMException

Sets the start position to be after a node

**Parameters:**
- refNode

- Range starts after

refNode

**Throws:**
- RangeException

- INVALID_NODE_TYPE_ERR: Raised if the root container of

refNode

is not an Attr, Document, or DocumentFragment
node or if

refNode

is a Document, DocumentFragment,
Attr, Entity, or Notation node.
- DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

WRONG_DOCUMENT_ERR: Raised if

refNode

was created
from a different document than the one that created this range.

---

#### void setEndBefore​(
Node
refNode)
throws
RangeException
,

DOMException

Sets the end position to be before a node.

**Parameters:**
- refNode

- Range ends before

refNode

**Throws:**
- RangeException

- INVALID_NODE_TYPE_ERR: Raised if the root container of

refNode

is not an Attr, Document, or DocumentFragment
node or if

refNode

is a Document, DocumentFragment,
Attr, Entity, or Notation node.
- DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

WRONG_DOCUMENT_ERR: Raised if

refNode

was created
from a different document than the one that created this range.

---

#### void setEndAfter​(
Node
refNode)
throws
RangeException
,

DOMException

Sets the end of a Range to be after a node

**Parameters:**
- refNode

- Range ends after

refNode

.

**Throws:**
- RangeException

- INVALID_NODE_TYPE_ERR: Raised if the root container of

refNode

is not an Attr, Document or DocumentFragment
node or if

refNode

is a Document, DocumentFragment,
Attr, Entity, or Notation node.
- DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

WRONG_DOCUMENT_ERR: Raised if

refNode

was created
from a different document than the one that created this range.

---

#### void collapse​(boolean toStart)
throws
DOMException

Collapse a Range onto one of its boundary-points

**Parameters:**
- toStart

- If TRUE, collapses the Range onto its start; if FALSE,
collapses it onto its end.

**Throws:**
- DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

---

#### void selectNode​(
Node
refNode)
throws
RangeException
,

DOMException

Select a node and its contents

**Parameters:**
- refNode

- The node to select.

**Throws:**
- RangeException

- INVALID_NODE_TYPE_ERR: Raised if an ancestor of

refNode

is an Entity, Notation or DocumentType node or if

refNode

is a Document, DocumentFragment, Attr, Entity,
or Notation node.
- DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

WRONG_DOCUMENT_ERR: Raised if

refNode

was created
from a different document than the one that created this range.

---

#### void selectNodeContents​(
Node
refNode)
throws
RangeException
,

DOMException

Select the contents within a node

**Parameters:**
- refNode

- Node to select from

**Throws:**
- RangeException

- INVALID_NODE_TYPE_ERR: Raised if

refNode

or an ancestor
of

refNode

is an Entity, Notation or DocumentType node.
- DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

WRONG_DOCUMENT_ERR: Raised if

refNode

was created
from a different document than the one that created this range.

---

#### short compareBoundaryPoints​(short how,

Range
sourceRange)
throws
DOMException

Compare the boundary-points of two Ranges in a document.

**Parameters:**
- how

- A code representing the type of comparison, as defined
above.
- sourceRange

- The

Range

on which this current

Range

is compared to.

**Returns:**
- -1, 0 or 1 depending on whether the corresponding
boundary-point of the Range is respectively before, equal to, or
after the corresponding boundary-point of

sourceRange

.

**Throws:**
- DOMException

- WRONG_DOCUMENT_ERR: Raised if the two Ranges are not in the same
Document or DocumentFragment.

INVALID_STATE_ERR: Raised if

detach()

has already
been invoked on this object.

---

#### void deleteContents()
throws
DOMException

Removes the contents of a Range from the containing document or
document fragment without returning a reference to the removed
content.

**Throws:**
- DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised if any portion of the content of
the Range is read-only or any of the nodes that contain any of the
content of the Range are read-only.

INVALID_STATE_ERR: Raised if

detach()

has already
been invoked on this object.

---

#### DocumentFragment
extractContents()
throws
DOMException

Moves the contents of a Range from the containing document or document
fragment to a new DocumentFragment.

**Returns:**
- A DocumentFragment containing the extracted contents.

**Throws:**
- DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised if any portion of the content of
the Range is read-only or any of the nodes which contain any of the
content of the Range are read-only.

HIERARCHY_REQUEST_ERR: Raised if a DocumentType node would be
extracted into the new DocumentFragment.

INVALID_STATE_ERR: Raised if

detach()

has already
been invoked on this object.

---

#### DocumentFragment
cloneContents()
throws
DOMException

Duplicates the contents of a Range

**Returns:**
- A DocumentFragment that contains content equivalent to this
Range.

**Throws:**
- DOMException

- HIERARCHY_REQUEST_ERR: Raised if a DocumentType node would be
extracted into the new DocumentFragment.

INVALID_STATE_ERR: Raised if

detach()

has already
been invoked on this object.

---

#### void insertNode​(
Node
newNode)
throws
DOMException
,

RangeException

Inserts a node into the Document or DocumentFragment at the start of
the Range. If the container is a Text node, this will be split at the
start of the Range (as if the Text node's splitText method was
performed at the insertion point) and the insertion will occur
between the two resulting Text nodes. Adjacent Text nodes will not be
automatically merged. If the node to be inserted is a
DocumentFragment node, the children will be inserted rather than the
DocumentFragment node itself.

**Parameters:**
- newNode

- The node to insert at the start of the Range

**Throws:**
- DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised if an ancestor container of the
start of the Range is read-only.

WRONG_DOCUMENT_ERR: Raised if

newNode

and the
container of the start of the Range were not created from the same
document.

HIERARCHY_REQUEST_ERR: Raised if the container of the start of
the Range is of a type that does not allow children of the type of

newNode

or if

newNode

is an ancestor of
the container.

INVALID_STATE_ERR: Raised if

detach()

has already
been invoked on this object.
- RangeException

- INVALID_NODE_TYPE_ERR: Raised if

newNode

is an Attr,
Entity, Notation, or Document node.

---

#### void surroundContents​(
Node
newParent)
throws
DOMException
,

RangeException

Reparents the contents of the Range to the given node and inserts the
node at the position of the start of the Range.

**Parameters:**
- newParent

- The node to surround the contents with.

**Throws:**
- DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised if an ancestor container of
either boundary-point of the Range is read-only.

WRONG_DOCUMENT_ERR: Raised if

newParent

and the
container of the start of the Range were not created from the same
document.

HIERARCHY_REQUEST_ERR: Raised if the container of the start of
the Range is of a type that does not allow children of the type of

newParent

or if

newParent

is an ancestor
of the container or if

node

would end up with a child
node of a type not allowed by the type of

node

.

INVALID_STATE_ERR: Raised if

detach()

has already
been invoked on this object.
- RangeException

- BAD_BOUNDARYPOINTS_ERR: Raised if the Range partially selects a
non-text node.

INVALID_NODE_TYPE_ERR: Raised if

node

is an Attr,
Entity, DocumentType, Notation, Document, or DocumentFragment node.

---

#### Range
cloneRange()
throws
DOMException

Produces a new Range whose boundary-points are equal to the
boundary-points of the Range.

**Returns:**
- The duplicated Range.

**Throws:**
- DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

---

#### String
toString()
throws
DOMException

Returns the contents of a Range as a string. This string contains only
the data characters, not any markup.

**Overrides:**
- toString

in class

Object

**Returns:**
- The contents of the Range.

**Throws:**
- DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

---

#### void detach()
throws
DOMException

Called to indicate that the Range is no longer in use and that the
implementation may relinquish any resources associated with this
Range. Subsequent calls to any methods or attribute getters on this
Range will result in a

DOMException

being thrown with an
error code of

INVALID_STATE_ERR

.

**Throws:**
- DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

---

### Additional Sections

#### Interface Range

```java
public interface
Range
```

See also the

Document Object Model (DOM) Level 2 Traversal and Range Specification

.

**Since:** 9, DOM Level 2

public interface

Range

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

END_TO_END

Compare end boundary-point of

sourceRange

to end
boundary-point of Range on which

compareBoundaryPoints

is invoked.

static short

END_TO_START

Compare end boundary-point of

sourceRange

to start
boundary-point of Range on which

compareBoundaryPoints

is invoked.

static short

START_TO_END

Compare start boundary-point of

sourceRange

to end
boundary-point of Range on which

compareBoundaryPoints

is invoked.

static short

START_TO_START

Compare start boundary-point of

sourceRange

to start
boundary-point of Range on which

compareBoundaryPoints

is invoked.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

DocumentFragment

cloneContents

()

Duplicates the contents of a Range

Range

cloneRange

()

Produces a new Range whose boundary-points are equal to the
boundary-points of the Range.

void

collapse

​(boolean toStart)

Collapse a Range onto one of its boundary-points

short

compareBoundaryPoints

​(short how,

Range

sourceRange)

Compare the boundary-points of two Ranges in a document.

void

deleteContents

()

Removes the contents of a Range from the containing document or
document fragment without returning a reference to the removed
content.

void

detach

()

Called to indicate that the Range is no longer in use and that the
implementation may relinquish any resources associated with this
Range.

DocumentFragment

extractContents

()

Moves the contents of a Range from the containing document or document
fragment to a new DocumentFragment.

boolean

getCollapsed

()

TRUE if the Range is collapsed

Node

getCommonAncestorContainer

()

The deepest common ancestor container of the Range's two
boundary-points.

Node

getEndContainer

()

Node within which the Range ends

int

getEndOffset

()

Offset within the ending node of the Range.

Node

getStartContainer

()

Node within which the Range begins

int

getStartOffset

()

Offset within the starting node of the Range.

void

insertNode

​(

Node

newNode)

Inserts a node into the Document or DocumentFragment at the start of
the Range.

void

selectNode

​(

Node

refNode)

Select a node and its contents

void

selectNodeContents

​(

Node

refNode)

Select the contents within a node

void

setEnd

​(

Node

refNode,
int offset)

Sets the attributes describing the end of a Range.

void

setEndAfter

​(

Node

refNode)

Sets the end of a Range to be after a node

void

setEndBefore

​(

Node

refNode)

Sets the end position to be before a node.

void

setStart

​(

Node

refNode,
int offset)

Sets the attributes describing the start of the Range.

void

setStartAfter

​(

Node

refNode)

Sets the start position to be after a node

void

setStartBefore

​(

Node

refNode)

Sets the start position to be before a node

void

surroundContents

​(

Node

newParent)

Reparents the contents of the Range to the given node and inserts the
node at the position of the start of the Range.

String

toString

()

Returns the contents of a Range as a string.

Field Summary

Fields

Modifier and Type

Field

Description

static short

END_TO_END

Compare end boundary-point of

sourceRange

to end
boundary-point of Range on which

compareBoundaryPoints

is invoked.

static short

END_TO_START

Compare end boundary-point of

sourceRange

to start
boundary-point of Range on which

compareBoundaryPoints

is invoked.

static short

START_TO_END

Compare start boundary-point of

sourceRange

to end
boundary-point of Range on which

compareBoundaryPoints

is invoked.

static short

START_TO_START

Compare start boundary-point of

sourceRange

to start
boundary-point of Range on which

compareBoundaryPoints

is invoked.

---

#### Field Summary

Compare end boundary-point of

sourceRange

to end
boundary-point of Range on which

compareBoundaryPoints

is invoked.

Compare end boundary-point of

sourceRange

to start
boundary-point of Range on which

compareBoundaryPoints

is invoked.

Compare start boundary-point of

sourceRange

to end
boundary-point of Range on which

compareBoundaryPoints

is invoked.

Compare start boundary-point of

sourceRange

to start
boundary-point of Range on which

compareBoundaryPoints

is invoked.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

DocumentFragment

cloneContents

()

Duplicates the contents of a Range

Range

cloneRange

()

Produces a new Range whose boundary-points are equal to the
boundary-points of the Range.

void

collapse

​(boolean toStart)

Collapse a Range onto one of its boundary-points

short

compareBoundaryPoints

​(short how,

Range

sourceRange)

Compare the boundary-points of two Ranges in a document.

void

deleteContents

()

Removes the contents of a Range from the containing document or
document fragment without returning a reference to the removed
content.

void

detach

()

Called to indicate that the Range is no longer in use and that the
implementation may relinquish any resources associated with this
Range.

DocumentFragment

extractContents

()

Moves the contents of a Range from the containing document or document
fragment to a new DocumentFragment.

boolean

getCollapsed

()

TRUE if the Range is collapsed

Node

getCommonAncestorContainer

()

The deepest common ancestor container of the Range's two
boundary-points.

Node

getEndContainer

()

Node within which the Range ends

int

getEndOffset

()

Offset within the ending node of the Range.

Node

getStartContainer

()

Node within which the Range begins

int

getStartOffset

()

Offset within the starting node of the Range.

void

insertNode

​(

Node

newNode)

Inserts a node into the Document or DocumentFragment at the start of
the Range.

void

selectNode

​(

Node

refNode)

Select a node and its contents

void

selectNodeContents

​(

Node

refNode)

Select the contents within a node

void

setEnd

​(

Node

refNode,
int offset)

Sets the attributes describing the end of a Range.

void

setEndAfter

​(

Node

refNode)

Sets the end of a Range to be after a node

void

setEndBefore

​(

Node

refNode)

Sets the end position to be before a node.

void

setStart

​(

Node

refNode,
int offset)

Sets the attributes describing the start of the Range.

void

setStartAfter

​(

Node

refNode)

Sets the start position to be after a node

void

setStartBefore

​(

Node

refNode)

Sets the start position to be before a node

void

surroundContents

​(

Node

newParent)

Reparents the contents of the Range to the given node and inserts the
node at the position of the start of the Range.

String

toString

()

Returns the contents of a Range as a string.

---

#### Method Summary

Duplicates the contents of a Range

Produces a new Range whose boundary-points are equal to the
boundary-points of the Range.

Collapse a Range onto one of its boundary-points

Compare the boundary-points of two Ranges in a document.

Removes the contents of a Range from the containing document or
document fragment without returning a reference to the removed
content.

Called to indicate that the Range is no longer in use and that the
implementation may relinquish any resources associated with this
Range.

Moves the contents of a Range from the containing document or document
fragment to a new DocumentFragment.

TRUE if the Range is collapsed

The deepest common ancestor container of the Range's two
boundary-points.

Node within which the Range ends

Offset within the ending node of the Range.

Node within which the Range begins

Offset within the starting node of the Range.

Inserts a node into the Document or DocumentFragment at the start of
the Range.

Select a node and its contents

Select the contents within a node

Sets the attributes describing the end of a Range.

Sets the end of a Range to be after a node

Sets the end position to be before a node.

Sets the attributes describing the start of the Range.

Sets the start position to be after a node

Sets the start position to be before a node

Reparents the contents of the Range to the given node and inserts the
node at the position of the start of the Range.

Returns the contents of a Range as a string.

============ FIELD DETAIL ===========

- Field Detail

- START_TO_START

```java
static final short START_TO_START
```

Compare start boundary-point of

sourceRange

to start
boundary-point of Range on which

compareBoundaryPoints

is invoked.

**See Also:** Constant Field Values

- START_TO_END

```java
static final short START_TO_END
```

Compare start boundary-point of

sourceRange

to end
boundary-point of Range on which

compareBoundaryPoints

is invoked.

**See Also:** Constant Field Values

- END_TO_END

```java
static final short END_TO_END
```

Compare end boundary-point of

sourceRange

to end
boundary-point of Range on which

compareBoundaryPoints

is invoked.

**See Also:** Constant Field Values

- END_TO_START

```java
static final short END_TO_START
```

Compare end boundary-point of

sourceRange

to start
boundary-point of Range on which

compareBoundaryPoints

is invoked.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getStartContainer

```java
Node
getStartContainer()
throws
DOMException
```

Node within which the Range begins

**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

- getStartOffset

```java
int getStartOffset()
throws
DOMException
```

Offset within the starting node of the Range.

**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

- getEndContainer

```java
Node
getEndContainer()
throws
DOMException
```

Node within which the Range ends

**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

- getEndOffset

```java
int getEndOffset()
throws
DOMException
```

Offset within the ending node of the Range.

**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

- getCollapsed

```java
boolean getCollapsed()
throws
DOMException
```

TRUE if the Range is collapsed

**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

- getCommonAncestorContainer

```java
Node
getCommonAncestorContainer()
throws
DOMException
```

The deepest common ancestor container of the Range's two
boundary-points.

**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

- setStart

```java
void setStart​(
Node
refNode,
int offset)
throws
RangeException
,

DOMException
```

Sets the attributes describing the start of the Range.

**Parameters:** refNode

- The

refNode

value. This parameter must be
different from

null

.
**Parameters:** offset

- The

startOffset

value.
**Throws:** RangeException

- INVALID_NODE_TYPE_ERR: Raised if

refNode

or an ancestor
of

refNode

is an Entity, Notation, or DocumentType
node.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if

offset

is negative or greater
than the number of child units in

refNode

. Child units
are 16-bit units if

refNode

is a type of CharacterData
node (e.g., a Text or Comment node) or a ProcessingInstruction
node. Child units are Nodes in all other cases.

INVALID_STATE_ERR: Raised if

detach()

has already
been invoked on this object.

WRONG_DOCUMENT_ERR: Raised if

refNode

was created
from a different document than the one that created this range.

- setEnd

```java
void setEnd​(
Node
refNode,
int offset)
throws
RangeException
,

DOMException
```

Sets the attributes describing the end of a Range.

**Parameters:** refNode

- The

refNode

value. This parameter must be
different from

null

.
**Parameters:** offset

- The

endOffset

value.
**Throws:** RangeException

- INVALID_NODE_TYPE_ERR: Raised if

refNode

or an ancestor
of

refNode

is an Entity, Notation, or DocumentType
node.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if

offset

is negative or greater
than the number of child units in

refNode

. Child units
are 16-bit units if

refNode

is a type of CharacterData
node (e.g., a Text or Comment node) or a ProcessingInstruction
node. Child units are Nodes in all other cases.

INVALID_STATE_ERR: Raised if

detach()

has already
been invoked on this object.

WRONG_DOCUMENT_ERR: Raised if

refNode

was created
from a different document than the one that created this range.

- setStartBefore

```java
void setStartBefore​(
Node
refNode)
throws
RangeException
,

DOMException
```

Sets the start position to be before a node

**Parameters:** refNode

- Range starts before

refNode
**Throws:** RangeException

- INVALID_NODE_TYPE_ERR: Raised if the root container of

refNode

is not an Attr, Document, or DocumentFragment
node or if

refNode

is a Document, DocumentFragment,
Attr, Entity, or Notation node.
**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

WRONG_DOCUMENT_ERR: Raised if

refNode

was created
from a different document than the one that created this range.

- setStartAfter

```java
void setStartAfter​(
Node
refNode)
throws
RangeException
,

DOMException
```

Sets the start position to be after a node

**Parameters:** refNode

- Range starts after

refNode
**Throws:** RangeException

- INVALID_NODE_TYPE_ERR: Raised if the root container of

refNode

is not an Attr, Document, or DocumentFragment
node or if

refNode

is a Document, DocumentFragment,
Attr, Entity, or Notation node.
**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

WRONG_DOCUMENT_ERR: Raised if

refNode

was created
from a different document than the one that created this range.

- setEndBefore

```java
void setEndBefore​(
Node
refNode)
throws
RangeException
,

DOMException
```

Sets the end position to be before a node.

**Parameters:** refNode

- Range ends before

refNode
**Throws:** RangeException

- INVALID_NODE_TYPE_ERR: Raised if the root container of

refNode

is not an Attr, Document, or DocumentFragment
node or if

refNode

is a Document, DocumentFragment,
Attr, Entity, or Notation node.
**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

WRONG_DOCUMENT_ERR: Raised if

refNode

was created
from a different document than the one that created this range.

- setEndAfter

```java
void setEndAfter​(
Node
refNode)
throws
RangeException
,

DOMException
```

Sets the end of a Range to be after a node

**Parameters:** refNode

- Range ends after

refNode

.
**Throws:** RangeException

- INVALID_NODE_TYPE_ERR: Raised if the root container of

refNode

is not an Attr, Document or DocumentFragment
node or if

refNode

is a Document, DocumentFragment,
Attr, Entity, or Notation node.
**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

WRONG_DOCUMENT_ERR: Raised if

refNode

was created
from a different document than the one that created this range.

- collapse

```java
void collapse​(boolean toStart)
throws
DOMException
```

Collapse a Range onto one of its boundary-points

**Parameters:** toStart

- If TRUE, collapses the Range onto its start; if FALSE,
collapses it onto its end.
**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

- selectNode

```java
void selectNode​(
Node
refNode)
throws
RangeException
,

DOMException
```

Select a node and its contents

**Parameters:** refNode

- The node to select.
**Throws:** RangeException

- INVALID_NODE_TYPE_ERR: Raised if an ancestor of

refNode

is an Entity, Notation or DocumentType node or if

refNode

is a Document, DocumentFragment, Attr, Entity,
or Notation node.
**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

WRONG_DOCUMENT_ERR: Raised if

refNode

was created
from a different document than the one that created this range.

- selectNodeContents

```java
void selectNodeContents​(
Node
refNode)
throws
RangeException
,

DOMException
```

Select the contents within a node

**Parameters:** refNode

- Node to select from
**Throws:** RangeException

- INVALID_NODE_TYPE_ERR: Raised if

refNode

or an ancestor
of

refNode

is an Entity, Notation or DocumentType node.
**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

WRONG_DOCUMENT_ERR: Raised if

refNode

was created
from a different document than the one that created this range.

- compareBoundaryPoints

```java
short compareBoundaryPoints​(short how,

Range
sourceRange)
throws
DOMException
```

Compare the boundary-points of two Ranges in a document.

**Parameters:** how

- A code representing the type of comparison, as defined
above.
**Parameters:** sourceRange

- The

Range

on which this current

Range

is compared to.
**Returns:** -1, 0 or 1 depending on whether the corresponding
boundary-point of the Range is respectively before, equal to, or
after the corresponding boundary-point of

sourceRange

.
**Throws:** DOMException

- WRONG_DOCUMENT_ERR: Raised if the two Ranges are not in the same
Document or DocumentFragment.

INVALID_STATE_ERR: Raised if

detach()

has already
been invoked on this object.

- deleteContents

```java
void deleteContents()
throws
DOMException
```

Removes the contents of a Range from the containing document or
document fragment without returning a reference to the removed
content.

**Throws:** DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised if any portion of the content of
the Range is read-only or any of the nodes that contain any of the
content of the Range are read-only.

INVALID_STATE_ERR: Raised if

detach()

has already
been invoked on this object.

- extractContents

```java
DocumentFragment
extractContents()
throws
DOMException
```

Moves the contents of a Range from the containing document or document
fragment to a new DocumentFragment.

**Returns:** A DocumentFragment containing the extracted contents.
**Throws:** DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised if any portion of the content of
the Range is read-only or any of the nodes which contain any of the
content of the Range are read-only.

HIERARCHY_REQUEST_ERR: Raised if a DocumentType node would be
extracted into the new DocumentFragment.

INVALID_STATE_ERR: Raised if

detach()

has already
been invoked on this object.

- cloneContents

```java
DocumentFragment
cloneContents()
throws
DOMException
```

Duplicates the contents of a Range

**Returns:** A DocumentFragment that contains content equivalent to this
Range.
**Throws:** DOMException

- HIERARCHY_REQUEST_ERR: Raised if a DocumentType node would be
extracted into the new DocumentFragment.

INVALID_STATE_ERR: Raised if

detach()

has already
been invoked on this object.

- insertNode

```java
void insertNode​(
Node
newNode)
throws
DOMException
,

RangeException
```

Inserts a node into the Document or DocumentFragment at the start of
the Range. If the container is a Text node, this will be split at the
start of the Range (as if the Text node's splitText method was
performed at the insertion point) and the insertion will occur
between the two resulting Text nodes. Adjacent Text nodes will not be
automatically merged. If the node to be inserted is a
DocumentFragment node, the children will be inserted rather than the
DocumentFragment node itself.

**Parameters:** newNode

- The node to insert at the start of the Range
**Throws:** DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised if an ancestor container of the
start of the Range is read-only.

WRONG_DOCUMENT_ERR: Raised if

newNode

and the
container of the start of the Range were not created from the same
document.

HIERARCHY_REQUEST_ERR: Raised if the container of the start of
the Range is of a type that does not allow children of the type of

newNode

or if

newNode

is an ancestor of
the container.

INVALID_STATE_ERR: Raised if

detach()

has already
been invoked on this object.
**Throws:** RangeException

- INVALID_NODE_TYPE_ERR: Raised if

newNode

is an Attr,
Entity, Notation, or Document node.

- surroundContents

```java
void surroundContents​(
Node
newParent)
throws
DOMException
,

RangeException
```

Reparents the contents of the Range to the given node and inserts the
node at the position of the start of the Range.

**Parameters:** newParent

- The node to surround the contents with.
**Throws:** DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised if an ancestor container of
either boundary-point of the Range is read-only.

WRONG_DOCUMENT_ERR: Raised if

newParent

and the
container of the start of the Range were not created from the same
document.

HIERARCHY_REQUEST_ERR: Raised if the container of the start of
the Range is of a type that does not allow children of the type of

newParent

or if

newParent

is an ancestor
of the container or if

node

would end up with a child
node of a type not allowed by the type of

node

.

INVALID_STATE_ERR: Raised if

detach()

has already
been invoked on this object.
**Throws:** RangeException

- BAD_BOUNDARYPOINTS_ERR: Raised if the Range partially selects a
non-text node.

INVALID_NODE_TYPE_ERR: Raised if

node

is an Attr,
Entity, DocumentType, Notation, Document, or DocumentFragment node.

- cloneRange

```java
Range
cloneRange()
throws
DOMException
```

Produces a new Range whose boundary-points are equal to the
boundary-points of the Range.

**Returns:** The duplicated Range.
**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

- toString

```java
String
toString()
throws
DOMException
```

Returns the contents of a Range as a string. This string contains only
the data characters, not any markup.

**Overrides:** toString

in class

Object
**Returns:** The contents of the Range.
**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

- detach

```java
void detach()
throws
DOMException
```

Called to indicate that the Range is no longer in use and that the
implementation may relinquish any resources associated with this
Range. Subsequent calls to any methods or attribute getters on this
Range will result in a

DOMException

being thrown with an
error code of

INVALID_STATE_ERR

.

**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

Field Detail

- START_TO_START

```java
static final short START_TO_START
```

Compare start boundary-point of

sourceRange

to start
boundary-point of Range on which

compareBoundaryPoints

is invoked.

**See Also:** Constant Field Values

- START_TO_END

```java
static final short START_TO_END
```

Compare start boundary-point of

sourceRange

to end
boundary-point of Range on which

compareBoundaryPoints

is invoked.

**See Also:** Constant Field Values

- END_TO_END

```java
static final short END_TO_END
```

Compare end boundary-point of

sourceRange

to end
boundary-point of Range on which

compareBoundaryPoints

is invoked.

**See Also:** Constant Field Values

- END_TO_START

```java
static final short END_TO_START
```

Compare end boundary-point of

sourceRange

to start
boundary-point of Range on which

compareBoundaryPoints

is invoked.

**See Also:** Constant Field Values

---

#### Field Detail

START_TO_START

```java
static final short START_TO_START
```

Compare start boundary-point of

sourceRange

to start
boundary-point of Range on which

compareBoundaryPoints

is invoked.

**See Also:** Constant Field Values

---

#### START_TO_START

static final short START_TO_START

Compare start boundary-point of

sourceRange

to start
boundary-point of Range on which

compareBoundaryPoints

is invoked.

START_TO_END

```java
static final short START_TO_END
```

Compare start boundary-point of

sourceRange

to end
boundary-point of Range on which

compareBoundaryPoints

is invoked.

**See Also:** Constant Field Values

---

#### START_TO_END

static final short START_TO_END

Compare start boundary-point of

sourceRange

to end
boundary-point of Range on which

compareBoundaryPoints

is invoked.

END_TO_END

```java
static final short END_TO_END
```

Compare end boundary-point of

sourceRange

to end
boundary-point of Range on which

compareBoundaryPoints

is invoked.

**See Also:** Constant Field Values

---

#### END_TO_END

static final short END_TO_END

Compare end boundary-point of

sourceRange

to end
boundary-point of Range on which

compareBoundaryPoints

is invoked.

END_TO_START

```java
static final short END_TO_START
```

Compare end boundary-point of

sourceRange

to start
boundary-point of Range on which

compareBoundaryPoints

is invoked.

**See Also:** Constant Field Values

---

#### END_TO_START

static final short END_TO_START

Compare end boundary-point of

sourceRange

to start
boundary-point of Range on which

compareBoundaryPoints

is invoked.

Method Detail

- getStartContainer

```java
Node
getStartContainer()
throws
DOMException
```

Node within which the Range begins

**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

- getStartOffset

```java
int getStartOffset()
throws
DOMException
```

Offset within the starting node of the Range.

**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

- getEndContainer

```java
Node
getEndContainer()
throws
DOMException
```

Node within which the Range ends

**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

- getEndOffset

```java
int getEndOffset()
throws
DOMException
```

Offset within the ending node of the Range.

**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

- getCollapsed

```java
boolean getCollapsed()
throws
DOMException
```

TRUE if the Range is collapsed

**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

- getCommonAncestorContainer

```java
Node
getCommonAncestorContainer()
throws
DOMException
```

The deepest common ancestor container of the Range's two
boundary-points.

**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

- setStart

```java
void setStart​(
Node
refNode,
int offset)
throws
RangeException
,

DOMException
```

Sets the attributes describing the start of the Range.

**Parameters:** refNode

- The

refNode

value. This parameter must be
different from

null

.
**Parameters:** offset

- The

startOffset

value.
**Throws:** RangeException

- INVALID_NODE_TYPE_ERR: Raised if

refNode

or an ancestor
of

refNode

is an Entity, Notation, or DocumentType
node.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if

offset

is negative or greater
than the number of child units in

refNode

. Child units
are 16-bit units if

refNode

is a type of CharacterData
node (e.g., a Text or Comment node) or a ProcessingInstruction
node. Child units are Nodes in all other cases.

INVALID_STATE_ERR: Raised if

detach()

has already
been invoked on this object.

WRONG_DOCUMENT_ERR: Raised if

refNode

was created
from a different document than the one that created this range.

- setEnd

```java
void setEnd​(
Node
refNode,
int offset)
throws
RangeException
,

DOMException
```

Sets the attributes describing the end of a Range.

**Parameters:** refNode

- The

refNode

value. This parameter must be
different from

null

.
**Parameters:** offset

- The

endOffset

value.
**Throws:** RangeException

- INVALID_NODE_TYPE_ERR: Raised if

refNode

or an ancestor
of

refNode

is an Entity, Notation, or DocumentType
node.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if

offset

is negative or greater
than the number of child units in

refNode

. Child units
are 16-bit units if

refNode

is a type of CharacterData
node (e.g., a Text or Comment node) or a ProcessingInstruction
node. Child units are Nodes in all other cases.

INVALID_STATE_ERR: Raised if

detach()

has already
been invoked on this object.

WRONG_DOCUMENT_ERR: Raised if

refNode

was created
from a different document than the one that created this range.

- setStartBefore

```java
void setStartBefore​(
Node
refNode)
throws
RangeException
,

DOMException
```

Sets the start position to be before a node

**Parameters:** refNode

- Range starts before

refNode
**Throws:** RangeException

- INVALID_NODE_TYPE_ERR: Raised if the root container of

refNode

is not an Attr, Document, or DocumentFragment
node or if

refNode

is a Document, DocumentFragment,
Attr, Entity, or Notation node.
**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

WRONG_DOCUMENT_ERR: Raised if

refNode

was created
from a different document than the one that created this range.

- setStartAfter

```java
void setStartAfter​(
Node
refNode)
throws
RangeException
,

DOMException
```

Sets the start position to be after a node

**Parameters:** refNode

- Range starts after

refNode
**Throws:** RangeException

- INVALID_NODE_TYPE_ERR: Raised if the root container of

refNode

is not an Attr, Document, or DocumentFragment
node or if

refNode

is a Document, DocumentFragment,
Attr, Entity, or Notation node.
**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

WRONG_DOCUMENT_ERR: Raised if

refNode

was created
from a different document than the one that created this range.

- setEndBefore

```java
void setEndBefore​(
Node
refNode)
throws
RangeException
,

DOMException
```

Sets the end position to be before a node.

**Parameters:** refNode

- Range ends before

refNode
**Throws:** RangeException

- INVALID_NODE_TYPE_ERR: Raised if the root container of

refNode

is not an Attr, Document, or DocumentFragment
node or if

refNode

is a Document, DocumentFragment,
Attr, Entity, or Notation node.
**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

WRONG_DOCUMENT_ERR: Raised if

refNode

was created
from a different document than the one that created this range.

- setEndAfter

```java
void setEndAfter​(
Node
refNode)
throws
RangeException
,

DOMException
```

Sets the end of a Range to be after a node

**Parameters:** refNode

- Range ends after

refNode

.
**Throws:** RangeException

- INVALID_NODE_TYPE_ERR: Raised if the root container of

refNode

is not an Attr, Document or DocumentFragment
node or if

refNode

is a Document, DocumentFragment,
Attr, Entity, or Notation node.
**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

WRONG_DOCUMENT_ERR: Raised if

refNode

was created
from a different document than the one that created this range.

- collapse

```java
void collapse​(boolean toStart)
throws
DOMException
```

Collapse a Range onto one of its boundary-points

**Parameters:** toStart

- If TRUE, collapses the Range onto its start; if FALSE,
collapses it onto its end.
**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

- selectNode

```java
void selectNode​(
Node
refNode)
throws
RangeException
,

DOMException
```

Select a node and its contents

**Parameters:** refNode

- The node to select.
**Throws:** RangeException

- INVALID_NODE_TYPE_ERR: Raised if an ancestor of

refNode

is an Entity, Notation or DocumentType node or if

refNode

is a Document, DocumentFragment, Attr, Entity,
or Notation node.
**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

WRONG_DOCUMENT_ERR: Raised if

refNode

was created
from a different document than the one that created this range.

- selectNodeContents

```java
void selectNodeContents​(
Node
refNode)
throws
RangeException
,

DOMException
```

Select the contents within a node

**Parameters:** refNode

- Node to select from
**Throws:** RangeException

- INVALID_NODE_TYPE_ERR: Raised if

refNode

or an ancestor
of

refNode

is an Entity, Notation or DocumentType node.
**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

WRONG_DOCUMENT_ERR: Raised if

refNode

was created
from a different document than the one that created this range.

- compareBoundaryPoints

```java
short compareBoundaryPoints​(short how,

Range
sourceRange)
throws
DOMException
```

Compare the boundary-points of two Ranges in a document.

**Parameters:** how

- A code representing the type of comparison, as defined
above.
**Parameters:** sourceRange

- The

Range

on which this current

Range

is compared to.
**Returns:** -1, 0 or 1 depending on whether the corresponding
boundary-point of the Range is respectively before, equal to, or
after the corresponding boundary-point of

sourceRange

.
**Throws:** DOMException

- WRONG_DOCUMENT_ERR: Raised if the two Ranges are not in the same
Document or DocumentFragment.

INVALID_STATE_ERR: Raised if

detach()

has already
been invoked on this object.

- deleteContents

```java
void deleteContents()
throws
DOMException
```

Removes the contents of a Range from the containing document or
document fragment without returning a reference to the removed
content.

**Throws:** DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised if any portion of the content of
the Range is read-only or any of the nodes that contain any of the
content of the Range are read-only.

INVALID_STATE_ERR: Raised if

detach()

has already
been invoked on this object.

- extractContents

```java
DocumentFragment
extractContents()
throws
DOMException
```

Moves the contents of a Range from the containing document or document
fragment to a new DocumentFragment.

**Returns:** A DocumentFragment containing the extracted contents.
**Throws:** DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised if any portion of the content of
the Range is read-only or any of the nodes which contain any of the
content of the Range are read-only.

HIERARCHY_REQUEST_ERR: Raised if a DocumentType node would be
extracted into the new DocumentFragment.

INVALID_STATE_ERR: Raised if

detach()

has already
been invoked on this object.

- cloneContents

```java
DocumentFragment
cloneContents()
throws
DOMException
```

Duplicates the contents of a Range

**Returns:** A DocumentFragment that contains content equivalent to this
Range.
**Throws:** DOMException

- HIERARCHY_REQUEST_ERR: Raised if a DocumentType node would be
extracted into the new DocumentFragment.

INVALID_STATE_ERR: Raised if

detach()

has already
been invoked on this object.

- insertNode

```java
void insertNode​(
Node
newNode)
throws
DOMException
,

RangeException
```

Inserts a node into the Document or DocumentFragment at the start of
the Range. If the container is a Text node, this will be split at the
start of the Range (as if the Text node's splitText method was
performed at the insertion point) and the insertion will occur
between the two resulting Text nodes. Adjacent Text nodes will not be
automatically merged. If the node to be inserted is a
DocumentFragment node, the children will be inserted rather than the
DocumentFragment node itself.

**Parameters:** newNode

- The node to insert at the start of the Range
**Throws:** DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised if an ancestor container of the
start of the Range is read-only.

WRONG_DOCUMENT_ERR: Raised if

newNode

and the
container of the start of the Range were not created from the same
document.

HIERARCHY_REQUEST_ERR: Raised if the container of the start of
the Range is of a type that does not allow children of the type of

newNode

or if

newNode

is an ancestor of
the container.

INVALID_STATE_ERR: Raised if

detach()

has already
been invoked on this object.
**Throws:** RangeException

- INVALID_NODE_TYPE_ERR: Raised if

newNode

is an Attr,
Entity, Notation, or Document node.

- surroundContents

```java
void surroundContents​(
Node
newParent)
throws
DOMException
,

RangeException
```

Reparents the contents of the Range to the given node and inserts the
node at the position of the start of the Range.

**Parameters:** newParent

- The node to surround the contents with.
**Throws:** DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised if an ancestor container of
either boundary-point of the Range is read-only.

WRONG_DOCUMENT_ERR: Raised if

newParent

and the
container of the start of the Range were not created from the same
document.

HIERARCHY_REQUEST_ERR: Raised if the container of the start of
the Range is of a type that does not allow children of the type of

newParent

or if

newParent

is an ancestor
of the container or if

node

would end up with a child
node of a type not allowed by the type of

node

.

INVALID_STATE_ERR: Raised if

detach()

has already
been invoked on this object.
**Throws:** RangeException

- BAD_BOUNDARYPOINTS_ERR: Raised if the Range partially selects a
non-text node.

INVALID_NODE_TYPE_ERR: Raised if

node

is an Attr,
Entity, DocumentType, Notation, Document, or DocumentFragment node.

- cloneRange

```java
Range
cloneRange()
throws
DOMException
```

Produces a new Range whose boundary-points are equal to the
boundary-points of the Range.

**Returns:** The duplicated Range.
**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

- toString

```java
String
toString()
throws
DOMException
```

Returns the contents of a Range as a string. This string contains only
the data characters, not any markup.

**Overrides:** toString

in class

Object
**Returns:** The contents of the Range.
**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

- detach

```java
void detach()
throws
DOMException
```

Called to indicate that the Range is no longer in use and that the
implementation may relinquish any resources associated with this
Range. Subsequent calls to any methods or attribute getters on this
Range will result in a

DOMException

being thrown with an
error code of

INVALID_STATE_ERR

.

**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

---

#### Method Detail

getStartContainer

```java
Node
getStartContainer()
throws
DOMException
```

Node within which the Range begins

**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

---

#### getStartContainer

Node

getStartContainer()
throws

DOMException

Node within which the Range begins

getStartOffset

```java
int getStartOffset()
throws
DOMException
```

Offset within the starting node of the Range.

**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

---

#### getStartOffset

int getStartOffset()
throws

DOMException

Offset within the starting node of the Range.

getEndContainer

```java
Node
getEndContainer()
throws
DOMException
```

Node within which the Range ends

**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

---

#### getEndContainer

Node

getEndContainer()
throws

DOMException

Node within which the Range ends

getEndOffset

```java
int getEndOffset()
throws
DOMException
```

Offset within the ending node of the Range.

**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

---

#### getEndOffset

int getEndOffset()
throws

DOMException

Offset within the ending node of the Range.

getCollapsed

```java
boolean getCollapsed()
throws
DOMException
```

TRUE if the Range is collapsed

**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

---

#### getCollapsed

boolean getCollapsed()
throws

DOMException

TRUE if the Range is collapsed

getCommonAncestorContainer

```java
Node
getCommonAncestorContainer()
throws
DOMException
```

The deepest common ancestor container of the Range's two
boundary-points.

**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

---

#### getCommonAncestorContainer

Node

getCommonAncestorContainer()
throws

DOMException

The deepest common ancestor container of the Range's two
boundary-points.

setStart

```java
void setStart​(
Node
refNode,
int offset)
throws
RangeException
,

DOMException
```

Sets the attributes describing the start of the Range.

**Parameters:** refNode

- The

refNode

value. This parameter must be
different from

null

.
**Parameters:** offset

- The

startOffset

value.
**Throws:** RangeException

- INVALID_NODE_TYPE_ERR: Raised if

refNode

or an ancestor
of

refNode

is an Entity, Notation, or DocumentType
node.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if

offset

is negative or greater
than the number of child units in

refNode

. Child units
are 16-bit units if

refNode

is a type of CharacterData
node (e.g., a Text or Comment node) or a ProcessingInstruction
node. Child units are Nodes in all other cases.

INVALID_STATE_ERR: Raised if

detach()

has already
been invoked on this object.

WRONG_DOCUMENT_ERR: Raised if

refNode

was created
from a different document than the one that created this range.

---

#### setStart

void setStart​(

Node

refNode,
int offset)
throws

RangeException

,

DOMException

Sets the attributes describing the start of the Range.

setEnd

```java
void setEnd​(
Node
refNode,
int offset)
throws
RangeException
,

DOMException
```

Sets the attributes describing the end of a Range.

**Parameters:** refNode

- The

refNode

value. This parameter must be
different from

null

.
**Parameters:** offset

- The

endOffset

value.
**Throws:** RangeException

- INVALID_NODE_TYPE_ERR: Raised if

refNode

or an ancestor
of

refNode

is an Entity, Notation, or DocumentType
node.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if

offset

is negative or greater
than the number of child units in

refNode

. Child units
are 16-bit units if

refNode

is a type of CharacterData
node (e.g., a Text or Comment node) or a ProcessingInstruction
node. Child units are Nodes in all other cases.

INVALID_STATE_ERR: Raised if

detach()

has already
been invoked on this object.

WRONG_DOCUMENT_ERR: Raised if

refNode

was created
from a different document than the one that created this range.

---

#### setEnd

void setEnd​(

Node

refNode,
int offset)
throws

RangeException

,

DOMException

Sets the attributes describing the end of a Range.

setStartBefore

```java
void setStartBefore​(
Node
refNode)
throws
RangeException
,

DOMException
```

Sets the start position to be before a node

**Parameters:** refNode

- Range starts before

refNode
**Throws:** RangeException

- INVALID_NODE_TYPE_ERR: Raised if the root container of

refNode

is not an Attr, Document, or DocumentFragment
node or if

refNode

is a Document, DocumentFragment,
Attr, Entity, or Notation node.
**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

WRONG_DOCUMENT_ERR: Raised if

refNode

was created
from a different document than the one that created this range.

---

#### setStartBefore

void setStartBefore​(

Node

refNode)
throws

RangeException

,

DOMException

Sets the start position to be before a node

setStartAfter

```java
void setStartAfter​(
Node
refNode)
throws
RangeException
,

DOMException
```

Sets the start position to be after a node

**Parameters:** refNode

- Range starts after

refNode
**Throws:** RangeException

- INVALID_NODE_TYPE_ERR: Raised if the root container of

refNode

is not an Attr, Document, or DocumentFragment
node or if

refNode

is a Document, DocumentFragment,
Attr, Entity, or Notation node.
**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

WRONG_DOCUMENT_ERR: Raised if

refNode

was created
from a different document than the one that created this range.

---

#### setStartAfter

void setStartAfter​(

Node

refNode)
throws

RangeException

,

DOMException

Sets the start position to be after a node

setEndBefore

```java
void setEndBefore​(
Node
refNode)
throws
RangeException
,

DOMException
```

Sets the end position to be before a node.

**Parameters:** refNode

- Range ends before

refNode
**Throws:** RangeException

- INVALID_NODE_TYPE_ERR: Raised if the root container of

refNode

is not an Attr, Document, or DocumentFragment
node or if

refNode

is a Document, DocumentFragment,
Attr, Entity, or Notation node.
**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

WRONG_DOCUMENT_ERR: Raised if

refNode

was created
from a different document than the one that created this range.

---

#### setEndBefore

void setEndBefore​(

Node

refNode)
throws

RangeException

,

DOMException

Sets the end position to be before a node.

setEndAfter

```java
void setEndAfter​(
Node
refNode)
throws
RangeException
,

DOMException
```

Sets the end of a Range to be after a node

**Parameters:** refNode

- Range ends after

refNode

.
**Throws:** RangeException

- INVALID_NODE_TYPE_ERR: Raised if the root container of

refNode

is not an Attr, Document or DocumentFragment
node or if

refNode

is a Document, DocumentFragment,
Attr, Entity, or Notation node.
**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

WRONG_DOCUMENT_ERR: Raised if

refNode

was created
from a different document than the one that created this range.

---

#### setEndAfter

void setEndAfter​(

Node

refNode)
throws

RangeException

,

DOMException

Sets the end of a Range to be after a node

collapse

```java
void collapse​(boolean toStart)
throws
DOMException
```

Collapse a Range onto one of its boundary-points

**Parameters:** toStart

- If TRUE, collapses the Range onto its start; if FALSE,
collapses it onto its end.
**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

---

#### collapse

void collapse​(boolean toStart)
throws

DOMException

Collapse a Range onto one of its boundary-points

selectNode

```java
void selectNode​(
Node
refNode)
throws
RangeException
,

DOMException
```

Select a node and its contents

**Parameters:** refNode

- The node to select.
**Throws:** RangeException

- INVALID_NODE_TYPE_ERR: Raised if an ancestor of

refNode

is an Entity, Notation or DocumentType node or if

refNode

is a Document, DocumentFragment, Attr, Entity,
or Notation node.
**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

WRONG_DOCUMENT_ERR: Raised if

refNode

was created
from a different document than the one that created this range.

---

#### selectNode

void selectNode​(

Node

refNode)
throws

RangeException

,

DOMException

Select a node and its contents

selectNodeContents

```java
void selectNodeContents​(
Node
refNode)
throws
RangeException
,

DOMException
```

Select the contents within a node

**Parameters:** refNode

- Node to select from
**Throws:** RangeException

- INVALID_NODE_TYPE_ERR: Raised if

refNode

or an ancestor
of

refNode

is an Entity, Notation or DocumentType node.
**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

WRONG_DOCUMENT_ERR: Raised if

refNode

was created
from a different document than the one that created this range.

---

#### selectNodeContents

void selectNodeContents​(

Node

refNode)
throws

RangeException

,

DOMException

Select the contents within a node

compareBoundaryPoints

```java
short compareBoundaryPoints​(short how,

Range
sourceRange)
throws
DOMException
```

Compare the boundary-points of two Ranges in a document.

**Parameters:** how

- A code representing the type of comparison, as defined
above.
**Parameters:** sourceRange

- The

Range

on which this current

Range

is compared to.
**Returns:** -1, 0 or 1 depending on whether the corresponding
boundary-point of the Range is respectively before, equal to, or
after the corresponding boundary-point of

sourceRange

.
**Throws:** DOMException

- WRONG_DOCUMENT_ERR: Raised if the two Ranges are not in the same
Document or DocumentFragment.

INVALID_STATE_ERR: Raised if

detach()

has already
been invoked on this object.

---

#### compareBoundaryPoints

short compareBoundaryPoints​(short how,

Range

sourceRange)
throws

DOMException

Compare the boundary-points of two Ranges in a document.

deleteContents

```java
void deleteContents()
throws
DOMException
```

Removes the contents of a Range from the containing document or
document fragment without returning a reference to the removed
content.

**Throws:** DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised if any portion of the content of
the Range is read-only or any of the nodes that contain any of the
content of the Range are read-only.

INVALID_STATE_ERR: Raised if

detach()

has already
been invoked on this object.

---

#### deleteContents

void deleteContents()
throws

DOMException

Removes the contents of a Range from the containing document or
document fragment without returning a reference to the removed
content.

extractContents

```java
DocumentFragment
extractContents()
throws
DOMException
```

Moves the contents of a Range from the containing document or document
fragment to a new DocumentFragment.

**Returns:** A DocumentFragment containing the extracted contents.
**Throws:** DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised if any portion of the content of
the Range is read-only or any of the nodes which contain any of the
content of the Range are read-only.

HIERARCHY_REQUEST_ERR: Raised if a DocumentType node would be
extracted into the new DocumentFragment.

INVALID_STATE_ERR: Raised if

detach()

has already
been invoked on this object.

---

#### extractContents

DocumentFragment

extractContents()
throws

DOMException

Moves the contents of a Range from the containing document or document
fragment to a new DocumentFragment.

cloneContents

```java
DocumentFragment
cloneContents()
throws
DOMException
```

Duplicates the contents of a Range

**Returns:** A DocumentFragment that contains content equivalent to this
Range.
**Throws:** DOMException

- HIERARCHY_REQUEST_ERR: Raised if a DocumentType node would be
extracted into the new DocumentFragment.

INVALID_STATE_ERR: Raised if

detach()

has already
been invoked on this object.

---

#### cloneContents

DocumentFragment

cloneContents()
throws

DOMException

Duplicates the contents of a Range

insertNode

```java
void insertNode​(
Node
newNode)
throws
DOMException
,

RangeException
```

Inserts a node into the Document or DocumentFragment at the start of
the Range. If the container is a Text node, this will be split at the
start of the Range (as if the Text node's splitText method was
performed at the insertion point) and the insertion will occur
between the two resulting Text nodes. Adjacent Text nodes will not be
automatically merged. If the node to be inserted is a
DocumentFragment node, the children will be inserted rather than the
DocumentFragment node itself.

**Parameters:** newNode

- The node to insert at the start of the Range
**Throws:** DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised if an ancestor container of the
start of the Range is read-only.

WRONG_DOCUMENT_ERR: Raised if

newNode

and the
container of the start of the Range were not created from the same
document.

HIERARCHY_REQUEST_ERR: Raised if the container of the start of
the Range is of a type that does not allow children of the type of

newNode

or if

newNode

is an ancestor of
the container.

INVALID_STATE_ERR: Raised if

detach()

has already
been invoked on this object.
**Throws:** RangeException

- INVALID_NODE_TYPE_ERR: Raised if

newNode

is an Attr,
Entity, Notation, or Document node.

---

#### insertNode

void insertNode​(

Node

newNode)
throws

DOMException

,

RangeException

Inserts a node into the Document or DocumentFragment at the start of
the Range. If the container is a Text node, this will be split at the
start of the Range (as if the Text node's splitText method was
performed at the insertion point) and the insertion will occur
between the two resulting Text nodes. Adjacent Text nodes will not be
automatically merged. If the node to be inserted is a
DocumentFragment node, the children will be inserted rather than the
DocumentFragment node itself.

surroundContents

```java
void surroundContents​(
Node
newParent)
throws
DOMException
,

RangeException
```

Reparents the contents of the Range to the given node and inserts the
node at the position of the start of the Range.

**Parameters:** newParent

- The node to surround the contents with.
**Throws:** DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised if an ancestor container of
either boundary-point of the Range is read-only.

WRONG_DOCUMENT_ERR: Raised if

newParent

and the
container of the start of the Range were not created from the same
document.

HIERARCHY_REQUEST_ERR: Raised if the container of the start of
the Range is of a type that does not allow children of the type of

newParent

or if

newParent

is an ancestor
of the container or if

node

would end up with a child
node of a type not allowed by the type of

node

.

INVALID_STATE_ERR: Raised if

detach()

has already
been invoked on this object.
**Throws:** RangeException

- BAD_BOUNDARYPOINTS_ERR: Raised if the Range partially selects a
non-text node.

INVALID_NODE_TYPE_ERR: Raised if

node

is an Attr,
Entity, DocumentType, Notation, Document, or DocumentFragment node.

---

#### surroundContents

void surroundContents​(

Node

newParent)
throws

DOMException

,

RangeException

Reparents the contents of the Range to the given node and inserts the
node at the position of the start of the Range.

cloneRange

```java
Range
cloneRange()
throws
DOMException
```

Produces a new Range whose boundary-points are equal to the
boundary-points of the Range.

**Returns:** The duplicated Range.
**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

---

#### cloneRange

Range

cloneRange()
throws

DOMException

Produces a new Range whose boundary-points are equal to the
boundary-points of the Range.

toString

```java
String
toString()
throws
DOMException
```

Returns the contents of a Range as a string. This string contains only
the data characters, not any markup.

**Overrides:** toString

in class

Object
**Returns:** The contents of the Range.
**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

---

#### toString

String

toString()
throws

DOMException

Returns the contents of a Range as a string. This string contains only
the data characters, not any markup.

detach

```java
void detach()
throws
DOMException
```

Called to indicate that the Range is no longer in use and that the
implementation may relinquish any resources associated with this
Range. Subsequent calls to any methods or attribute getters on this
Range will result in a

DOMException

being thrown with an
error code of

INVALID_STATE_ERR

.

**Throws:** DOMException

- INVALID_STATE_ERR: Raised if

detach()

has already been
invoked on this object.

---

#### detach

void detach()
throws

DOMException

Called to indicate that the Range is no longer in use and that the
implementation may relinquish any resources associated with this
Range. Subsequent calls to any methods or attribute getters on this
Range will result in a

DOMException

being thrown with an
error code of

INVALID_STATE_ERR

.

---

