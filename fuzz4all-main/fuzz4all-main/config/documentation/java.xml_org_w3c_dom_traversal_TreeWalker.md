# Interface TreeWalker

**Source:** `java.xml\org\w3c\dom\traversal\TreeWalker.html`

### Class Description

```java
public interface
TreeWalker
```

TreeWalker

objects are used to navigate a document tree or
subtree using the view of the document defined by their

whatToShow

flags and filter (if any). Any function which
performs navigation using a

TreeWalker

will automatically
support any view defined by a

TreeWalker

.

Omitting nodes from the logical view of a subtree can result in a
structure that is substantially different from the same subtree in the
complete, unfiltered document. Nodes that are siblings in the

TreeWalker

view may be children of different, widely
separated nodes in the original view. For instance, consider a

NodeFilter

that skips all nodes except for Text nodes and
the root node of a document. In the logical view that results, all text
nodes will be siblings and appear as direct children of the root node, no
matter how deeply nested the structure of the original document.

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

#### Node
getRoot()

The

root

node of the

TreeWalker

, as specified
when it was created.

---

#### int getWhatToShow()

This attribute determines which node types are presented via the

TreeWalker

. The available set of constants is defined in
the

NodeFilter

interface. Nodes not accepted by

whatToShow

will be skipped, but their children may still
be considered. Note that this skip takes precedence over the filter,
if any.

---

#### NodeFilter
getFilter()

The filter used to screen nodes.

---

#### boolean getExpandEntityReferences()

The value of this flag determines whether the children of entity
reference nodes are visible to the

TreeWalker

. If false,
these children and their descendants will be rejected. Note that
this rejection takes precedence over

whatToShow

and the
filter, if any.

To produce a view of the document that has entity references
expanded and does not expose the entity reference node itself, use
the

whatToShow

flags to hide the entity reference node
and set

expandEntityReferences

to true when creating the

TreeWalker

. To produce a view of the document that has
entity reference nodes but no entity expansion, use the

whatToShow

flags to show the entity reference node and
set

expandEntityReferences

to false.

---

#### Node
getCurrentNode()

The node at which the

TreeWalker

is currently positioned.

Alterations to the DOM tree may cause the current node to no longer
be accepted by the

TreeWalker

's associated filter.

currentNode

may also be explicitly set to any node,
whether or not it is within the subtree specified by the

root

node or would be accepted by the filter and

whatToShow

flags. Further traversal occurs relative to

currentNode

even if it is not part of the current view,
by applying the filters in the requested direction; if no traversal
is possible,

currentNode

is not changed.

---

#### void setCurrentNode​(
Node
currentNode)
throws
DOMException

The node at which the

TreeWalker

is currently positioned.

Alterations to the DOM tree may cause the current node to no longer
be accepted by the

TreeWalker

's associated filter.

currentNode

may also be explicitly set to any node,
whether or not it is within the subtree specified by the

root

node or would be accepted by the filter and

whatToShow

flags. Further traversal occurs relative to

currentNode

even if it is not part of the current view,
by applying the filters in the requested direction; if no traversal
is possible,

currentNode

is not changed.

**Throws:**
- DOMException

- NOT_SUPPORTED_ERR: Raised if an attempt is made to set

currentNode

to

null

.

---

#### Node
parentNode()

Moves to and returns the closest visible ancestor node of the current
node. If the search for

parentNode

attempts to step
upward from the

TreeWalker

's

root

node, or
if it fails to find a visible ancestor node, this method retains the
current position and returns

null

.

**Returns:**
- The new parent node, or

null

if the current node
has no parent in the

TreeWalker

's logical view.

---

#### Node
firstChild()

Moves the

TreeWalker

to the first visible child of the
current node, and returns the new node. If the current node has no
visible children, returns

null

, and retains the current
node.

**Returns:**
- The new node, or

null

if the current node has no
visible children in the

TreeWalker

's logical view.

---

#### Node
lastChild()

Moves the

TreeWalker

to the last visible child of the
current node, and returns the new node. If the current node has no
visible children, returns

null

, and retains the current
node.

**Returns:**
- The new node, or

null

if the current node has no
children in the

TreeWalker

's logical view.

---

#### Node
previousSibling()

Moves the

TreeWalker

to the previous sibling of the
current node, and returns the new node. If the current node has no
visible previous sibling, returns

null

, and retains the
current node.

**Returns:**
- The new node, or

null

if the current node has no
previous sibling. in the

TreeWalker

's logical view.

---

#### Node
nextSibling()

Moves the

TreeWalker

to the next sibling of the current
node, and returns the new node. If the current node has no visible
next sibling, returns

null

, and retains the current node.

**Returns:**
- The new node, or

null

if the current node has no
next sibling. in the

TreeWalker

's logical view.

---

#### Node
previousNode()

Moves the

TreeWalker

to the previous visible node in
document order relative to the current node, and returns the new
node. If the current node has no previous node, or if the search for

previousNode

attempts to step upward from the

TreeWalker

's

root

node, returns

null

, and retains the current node.

**Returns:**
- The new node, or

null

if the current node has no
previous node in the

TreeWalker

's logical view.

---

#### Node
nextNode()

Moves the

TreeWalker

to the next visible node in document
order relative to the current node, and returns the new node. If the
current node has no next node, or if the search for nextNode attempts
to step upward from the

TreeWalker

's

root

node, returns

null

, and retains the current node.

**Returns:**
- The new node, or

null

if the current node has no
next node in the

TreeWalker

's logical view.

---

### Additional Sections

#### Interface TreeWalker

```java
public interface
TreeWalker
```

TreeWalker

objects are used to navigate a document tree or
subtree using the view of the document defined by their

whatToShow

flags and filter (if any). Any function which
performs navigation using a

TreeWalker

will automatically
support any view defined by a

TreeWalker

.

Omitting nodes from the logical view of a subtree can result in a
structure that is substantially different from the same subtree in the
complete, unfiltered document. Nodes that are siblings in the

TreeWalker

view may be children of different, widely
separated nodes in the original view. For instance, consider a

NodeFilter

that skips all nodes except for Text nodes and
the root node of a document. In the logical view that results, all text
nodes will be siblings and appear as direct children of the root node, no
matter how deeply nested the structure of the original document.

See also the

Document Object Model (DOM) Level 2 Traversal and Range Specification

.

**Since:** 9, DOM Level 2

public interface

TreeWalker

TreeWalker

objects are used to navigate a document tree or
subtree using the view of the document defined by their

whatToShow

flags and filter (if any). Any function which
performs navigation using a

TreeWalker

will automatically
support any view defined by a

TreeWalker

.

Omitting nodes from the logical view of a subtree can result in a
structure that is substantially different from the same subtree in the
complete, unfiltered document. Nodes that are siblings in the

TreeWalker

view may be children of different, widely
separated nodes in the original view. For instance, consider a

NodeFilter

that skips all nodes except for Text nodes and
the root node of a document. In the logical view that results, all text
nodes will be siblings and appear as direct children of the root node, no
matter how deeply nested the structure of the original document.

See also the

Document Object Model (DOM) Level 2 Traversal and Range Specification

.

Omitting nodes from the logical view of a subtree can result in a
structure that is substantially different from the same subtree in the
complete, unfiltered document. Nodes that are siblings in the

TreeWalker

view may be children of different, widely
separated nodes in the original view. For instance, consider a

NodeFilter

that skips all nodes except for Text nodes and
the root node of a document. In the logical view that results, all text
nodes will be siblings and appear as direct children of the root node, no
matter how deeply nested the structure of the original document.

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

Node

firstChild

()

Moves the

TreeWalker

to the first visible child of the
current node, and returns the new node.

Node

getCurrentNode

()

The node at which the

TreeWalker

is currently positioned.

boolean

getExpandEntityReferences

()

The value of this flag determines whether the children of entity
reference nodes are visible to the

TreeWalker

.

NodeFilter

getFilter

()

The filter used to screen nodes.

Node

getRoot

()

The

root

node of the

TreeWalker

, as specified
when it was created.

int

getWhatToShow

()

This attribute determines which node types are presented via the

TreeWalker

.

Node

lastChild

()

Moves the

TreeWalker

to the last visible child of the
current node, and returns the new node.

Node

nextNode

()

Moves the

TreeWalker

to the next visible node in document
order relative to the current node, and returns the new node.

Node

nextSibling

()

Moves the

TreeWalker

to the next sibling of the current
node, and returns the new node.

Node

parentNode

()

Moves to and returns the closest visible ancestor node of the current
node.

Node

previousNode

()

Moves the

TreeWalker

to the previous visible node in
document order relative to the current node, and returns the new
node.

Node

previousSibling

()

Moves the

TreeWalker

to the previous sibling of the
current node, and returns the new node.

void

setCurrentNode

​(

Node

currentNode)

The node at which the

TreeWalker

is currently positioned.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Node

firstChild

()

Moves the

TreeWalker

to the first visible child of the
current node, and returns the new node.

Node

getCurrentNode

()

The node at which the

TreeWalker

is currently positioned.

boolean

getExpandEntityReferences

()

The value of this flag determines whether the children of entity
reference nodes are visible to the

TreeWalker

.

NodeFilter

getFilter

()

The filter used to screen nodes.

Node

getRoot

()

The

root

node of the

TreeWalker

, as specified
when it was created.

int

getWhatToShow

()

This attribute determines which node types are presented via the

TreeWalker

.

Node

lastChild

()

Moves the

TreeWalker

to the last visible child of the
current node, and returns the new node.

Node

nextNode

()

Moves the

TreeWalker

to the next visible node in document
order relative to the current node, and returns the new node.

Node

nextSibling

()

Moves the

TreeWalker

to the next sibling of the current
node, and returns the new node.

Node

parentNode

()

Moves to and returns the closest visible ancestor node of the current
node.

Node

previousNode

()

Moves the

TreeWalker

to the previous visible node in
document order relative to the current node, and returns the new
node.

Node

previousSibling

()

Moves the

TreeWalker

to the previous sibling of the
current node, and returns the new node.

void

setCurrentNode

​(

Node

currentNode)

The node at which the

TreeWalker

is currently positioned.

---

#### Method Summary

Moves the

TreeWalker

to the first visible child of the
current node, and returns the new node.

The node at which the

TreeWalker

is currently positioned.

The value of this flag determines whether the children of entity
reference nodes are visible to the

TreeWalker

.

The filter used to screen nodes.

The

root

node of the

TreeWalker

, as specified
when it was created.

This attribute determines which node types are presented via the

TreeWalker

.

Moves the

TreeWalker

to the last visible child of the
current node, and returns the new node.

Moves the

TreeWalker

to the next visible node in document
order relative to the current node, and returns the new node.

Moves the

TreeWalker

to the next sibling of the current
node, and returns the new node.

Moves to and returns the closest visible ancestor node of the current
node.

Moves the

TreeWalker

to the previous visible node in
document order relative to the current node, and returns the new
node.

Moves the

TreeWalker

to the previous sibling of the
current node, and returns the new node.

============ METHOD DETAIL ==========

- Method Detail

- getRoot

```java
Node
getRoot()
```

The

root

node of the

TreeWalker

, as specified
when it was created.

- getWhatToShow

```java
int getWhatToShow()
```

This attribute determines which node types are presented via the

TreeWalker

. The available set of constants is defined in
the

NodeFilter

interface. Nodes not accepted by

whatToShow

will be skipped, but their children may still
be considered. Note that this skip takes precedence over the filter,
if any.

- getFilter

```java
NodeFilter
getFilter()
```

The filter used to screen nodes.

- getExpandEntityReferences

```java
boolean getExpandEntityReferences()
```

The value of this flag determines whether the children of entity
reference nodes are visible to the

TreeWalker

. If false,
these children and their descendants will be rejected. Note that
this rejection takes precedence over

whatToShow

and the
filter, if any.

To produce a view of the document that has entity references
expanded and does not expose the entity reference node itself, use
the

whatToShow

flags to hide the entity reference node
and set

expandEntityReferences

to true when creating the

TreeWalker

. To produce a view of the document that has
entity reference nodes but no entity expansion, use the

whatToShow

flags to show the entity reference node and
set

expandEntityReferences

to false.

- getCurrentNode

```java
Node
getCurrentNode()
```

The node at which the

TreeWalker

is currently positioned.

Alterations to the DOM tree may cause the current node to no longer
be accepted by the

TreeWalker

's associated filter.

currentNode

may also be explicitly set to any node,
whether or not it is within the subtree specified by the

root

node or would be accepted by the filter and

whatToShow

flags. Further traversal occurs relative to

currentNode

even if it is not part of the current view,
by applying the filters in the requested direction; if no traversal
is possible,

currentNode

is not changed.

- setCurrentNode

```java
void setCurrentNode​(
Node
currentNode)
throws
DOMException
```

The node at which the

TreeWalker

is currently positioned.

Alterations to the DOM tree may cause the current node to no longer
be accepted by the

TreeWalker

's associated filter.

currentNode

may also be explicitly set to any node,
whether or not it is within the subtree specified by the

root

node or would be accepted by the filter and

whatToShow

flags. Further traversal occurs relative to

currentNode

even if it is not part of the current view,
by applying the filters in the requested direction; if no traversal
is possible,

currentNode

is not changed.

**Throws:** DOMException

- NOT_SUPPORTED_ERR: Raised if an attempt is made to set

currentNode

to

null

.

- parentNode

```java
Node
parentNode()
```

Moves to and returns the closest visible ancestor node of the current
node. If the search for

parentNode

attempts to step
upward from the

TreeWalker

's

root

node, or
if it fails to find a visible ancestor node, this method retains the
current position and returns

null

.

**Returns:** The new parent node, or

null

if the current node
has no parent in the

TreeWalker

's logical view.

- firstChild

```java
Node
firstChild()
```

Moves the

TreeWalker

to the first visible child of the
current node, and returns the new node. If the current node has no
visible children, returns

null

, and retains the current
node.

**Returns:** The new node, or

null

if the current node has no
visible children in the

TreeWalker

's logical view.

- lastChild

```java
Node
lastChild()
```

Moves the

TreeWalker

to the last visible child of the
current node, and returns the new node. If the current node has no
visible children, returns

null

, and retains the current
node.

**Returns:** The new node, or

null

if the current node has no
children in the

TreeWalker

's logical view.

- previousSibling

```java
Node
previousSibling()
```

Moves the

TreeWalker

to the previous sibling of the
current node, and returns the new node. If the current node has no
visible previous sibling, returns

null

, and retains the
current node.

**Returns:** The new node, or

null

if the current node has no
previous sibling. in the

TreeWalker

's logical view.

- nextSibling

```java
Node
nextSibling()
```

Moves the

TreeWalker

to the next sibling of the current
node, and returns the new node. If the current node has no visible
next sibling, returns

null

, and retains the current node.

**Returns:** The new node, or

null

if the current node has no
next sibling. in the

TreeWalker

's logical view.

- previousNode

```java
Node
previousNode()
```

Moves the

TreeWalker

to the previous visible node in
document order relative to the current node, and returns the new
node. If the current node has no previous node, or if the search for

previousNode

attempts to step upward from the

TreeWalker

's

root

node, returns

null

, and retains the current node.

**Returns:** The new node, or

null

if the current node has no
previous node in the

TreeWalker

's logical view.

- nextNode

```java
Node
nextNode()
```

Moves the

TreeWalker

to the next visible node in document
order relative to the current node, and returns the new node. If the
current node has no next node, or if the search for nextNode attempts
to step upward from the

TreeWalker

's

root

node, returns

null

, and retains the current node.

**Returns:** The new node, or

null

if the current node has no
next node in the

TreeWalker

's logical view.

Method Detail

- getRoot

```java
Node
getRoot()
```

The

root

node of the

TreeWalker

, as specified
when it was created.

- getWhatToShow

```java
int getWhatToShow()
```

This attribute determines which node types are presented via the

TreeWalker

. The available set of constants is defined in
the

NodeFilter

interface. Nodes not accepted by

whatToShow

will be skipped, but their children may still
be considered. Note that this skip takes precedence over the filter,
if any.

- getFilter

```java
NodeFilter
getFilter()
```

The filter used to screen nodes.

- getExpandEntityReferences

```java
boolean getExpandEntityReferences()
```

The value of this flag determines whether the children of entity
reference nodes are visible to the

TreeWalker

. If false,
these children and their descendants will be rejected. Note that
this rejection takes precedence over

whatToShow

and the
filter, if any.

To produce a view of the document that has entity references
expanded and does not expose the entity reference node itself, use
the

whatToShow

flags to hide the entity reference node
and set

expandEntityReferences

to true when creating the

TreeWalker

. To produce a view of the document that has
entity reference nodes but no entity expansion, use the

whatToShow

flags to show the entity reference node and
set

expandEntityReferences

to false.

- getCurrentNode

```java
Node
getCurrentNode()
```

The node at which the

TreeWalker

is currently positioned.

Alterations to the DOM tree may cause the current node to no longer
be accepted by the

TreeWalker

's associated filter.

currentNode

may also be explicitly set to any node,
whether or not it is within the subtree specified by the

root

node or would be accepted by the filter and

whatToShow

flags. Further traversal occurs relative to

currentNode

even if it is not part of the current view,
by applying the filters in the requested direction; if no traversal
is possible,

currentNode

is not changed.

- setCurrentNode

```java
void setCurrentNode​(
Node
currentNode)
throws
DOMException
```

The node at which the

TreeWalker

is currently positioned.

Alterations to the DOM tree may cause the current node to no longer
be accepted by the

TreeWalker

's associated filter.

currentNode

may also be explicitly set to any node,
whether or not it is within the subtree specified by the

root

node or would be accepted by the filter and

whatToShow

flags. Further traversal occurs relative to

currentNode

even if it is not part of the current view,
by applying the filters in the requested direction; if no traversal
is possible,

currentNode

is not changed.

**Throws:** DOMException

- NOT_SUPPORTED_ERR: Raised if an attempt is made to set

currentNode

to

null

.

- parentNode

```java
Node
parentNode()
```

Moves to and returns the closest visible ancestor node of the current
node. If the search for

parentNode

attempts to step
upward from the

TreeWalker

's

root

node, or
if it fails to find a visible ancestor node, this method retains the
current position and returns

null

.

**Returns:** The new parent node, or

null

if the current node
has no parent in the

TreeWalker

's logical view.

- firstChild

```java
Node
firstChild()
```

Moves the

TreeWalker

to the first visible child of the
current node, and returns the new node. If the current node has no
visible children, returns

null

, and retains the current
node.

**Returns:** The new node, or

null

if the current node has no
visible children in the

TreeWalker

's logical view.

- lastChild

```java
Node
lastChild()
```

Moves the

TreeWalker

to the last visible child of the
current node, and returns the new node. If the current node has no
visible children, returns

null

, and retains the current
node.

**Returns:** The new node, or

null

if the current node has no
children in the

TreeWalker

's logical view.

- previousSibling

```java
Node
previousSibling()
```

Moves the

TreeWalker

to the previous sibling of the
current node, and returns the new node. If the current node has no
visible previous sibling, returns

null

, and retains the
current node.

**Returns:** The new node, or

null

if the current node has no
previous sibling. in the

TreeWalker

's logical view.

- nextSibling

```java
Node
nextSibling()
```

Moves the

TreeWalker

to the next sibling of the current
node, and returns the new node. If the current node has no visible
next sibling, returns

null

, and retains the current node.

**Returns:** The new node, or

null

if the current node has no
next sibling. in the

TreeWalker

's logical view.

- previousNode

```java
Node
previousNode()
```

Moves the

TreeWalker

to the previous visible node in
document order relative to the current node, and returns the new
node. If the current node has no previous node, or if the search for

previousNode

attempts to step upward from the

TreeWalker

's

root

node, returns

null

, and retains the current node.

**Returns:** The new node, or

null

if the current node has no
previous node in the

TreeWalker

's logical view.

- nextNode

```java
Node
nextNode()
```

Moves the

TreeWalker

to the next visible node in document
order relative to the current node, and returns the new node. If the
current node has no next node, or if the search for nextNode attempts
to step upward from the

TreeWalker

's

root

node, returns

null

, and retains the current node.

**Returns:** The new node, or

null

if the current node has no
next node in the

TreeWalker

's logical view.

---

#### Method Detail

getRoot

```java
Node
getRoot()
```

The

root

node of the

TreeWalker

, as specified
when it was created.

---

#### getRoot

Node

getRoot()

The

root

node of the

TreeWalker

, as specified
when it was created.

getWhatToShow

```java
int getWhatToShow()
```

This attribute determines which node types are presented via the

TreeWalker

. The available set of constants is defined in
the

NodeFilter

interface. Nodes not accepted by

whatToShow

will be skipped, but their children may still
be considered. Note that this skip takes precedence over the filter,
if any.

---

#### getWhatToShow

int getWhatToShow()

This attribute determines which node types are presented via the

TreeWalker

. The available set of constants is defined in
the

NodeFilter

interface. Nodes not accepted by

whatToShow

will be skipped, but their children may still
be considered. Note that this skip takes precedence over the filter,
if any.

getFilter

```java
NodeFilter
getFilter()
```

The filter used to screen nodes.

---

#### getFilter

NodeFilter

getFilter()

The filter used to screen nodes.

getExpandEntityReferences

```java
boolean getExpandEntityReferences()
```

The value of this flag determines whether the children of entity
reference nodes are visible to the

TreeWalker

. If false,
these children and their descendants will be rejected. Note that
this rejection takes precedence over

whatToShow

and the
filter, if any.

To produce a view of the document that has entity references
expanded and does not expose the entity reference node itself, use
the

whatToShow

flags to hide the entity reference node
and set

expandEntityReferences

to true when creating the

TreeWalker

. To produce a view of the document that has
entity reference nodes but no entity expansion, use the

whatToShow

flags to show the entity reference node and
set

expandEntityReferences

to false.

---

#### getExpandEntityReferences

boolean getExpandEntityReferences()

The value of this flag determines whether the children of entity
reference nodes are visible to the

TreeWalker

. If false,
these children and their descendants will be rejected. Note that
this rejection takes precedence over

whatToShow

and the
filter, if any.

To produce a view of the document that has entity references
expanded and does not expose the entity reference node itself, use
the

whatToShow

flags to hide the entity reference node
and set

expandEntityReferences

to true when creating the

TreeWalker

. To produce a view of the document that has
entity reference nodes but no entity expansion, use the

whatToShow

flags to show the entity reference node and
set

expandEntityReferences

to false.

getCurrentNode

```java
Node
getCurrentNode()
```

The node at which the

TreeWalker

is currently positioned.

Alterations to the DOM tree may cause the current node to no longer
be accepted by the

TreeWalker

's associated filter.

currentNode

may also be explicitly set to any node,
whether or not it is within the subtree specified by the

root

node or would be accepted by the filter and

whatToShow

flags. Further traversal occurs relative to

currentNode

even if it is not part of the current view,
by applying the filters in the requested direction; if no traversal
is possible,

currentNode

is not changed.

---

#### getCurrentNode

Node

getCurrentNode()

The node at which the

TreeWalker

is currently positioned.

Alterations to the DOM tree may cause the current node to no longer
be accepted by the

TreeWalker

's associated filter.

currentNode

may also be explicitly set to any node,
whether or not it is within the subtree specified by the

root

node or would be accepted by the filter and

whatToShow

flags. Further traversal occurs relative to

currentNode

even if it is not part of the current view,
by applying the filters in the requested direction; if no traversal
is possible,

currentNode

is not changed.

setCurrentNode

```java
void setCurrentNode​(
Node
currentNode)
throws
DOMException
```

The node at which the

TreeWalker

is currently positioned.

Alterations to the DOM tree may cause the current node to no longer
be accepted by the

TreeWalker

's associated filter.

currentNode

may also be explicitly set to any node,
whether or not it is within the subtree specified by the

root

node or would be accepted by the filter and

whatToShow

flags. Further traversal occurs relative to

currentNode

even if it is not part of the current view,
by applying the filters in the requested direction; if no traversal
is possible,

currentNode

is not changed.

**Throws:** DOMException

- NOT_SUPPORTED_ERR: Raised if an attempt is made to set

currentNode

to

null

.

---

#### setCurrentNode

void setCurrentNode​(

Node

currentNode)
throws

DOMException

The node at which the

TreeWalker

is currently positioned.

Alterations to the DOM tree may cause the current node to no longer
be accepted by the

TreeWalker

's associated filter.

currentNode

may also be explicitly set to any node,
whether or not it is within the subtree specified by the

root

node or would be accepted by the filter and

whatToShow

flags. Further traversal occurs relative to

currentNode

even if it is not part of the current view,
by applying the filters in the requested direction; if no traversal
is possible,

currentNode

is not changed.

parentNode

```java
Node
parentNode()
```

Moves to and returns the closest visible ancestor node of the current
node. If the search for

parentNode

attempts to step
upward from the

TreeWalker

's

root

node, or
if it fails to find a visible ancestor node, this method retains the
current position and returns

null

.

**Returns:** The new parent node, or

null

if the current node
has no parent in the

TreeWalker

's logical view.

---

#### parentNode

Node

parentNode()

Moves to and returns the closest visible ancestor node of the current
node. If the search for

parentNode

attempts to step
upward from the

TreeWalker

's

root

node, or
if it fails to find a visible ancestor node, this method retains the
current position and returns

null

.

firstChild

```java
Node
firstChild()
```

Moves the

TreeWalker

to the first visible child of the
current node, and returns the new node. If the current node has no
visible children, returns

null

, and retains the current
node.

**Returns:** The new node, or

null

if the current node has no
visible children in the

TreeWalker

's logical view.

---

#### firstChild

Node

firstChild()

Moves the

TreeWalker

to the first visible child of the
current node, and returns the new node. If the current node has no
visible children, returns

null

, and retains the current
node.

lastChild

```java
Node
lastChild()
```

Moves the

TreeWalker

to the last visible child of the
current node, and returns the new node. If the current node has no
visible children, returns

null

, and retains the current
node.

**Returns:** The new node, or

null

if the current node has no
children in the

TreeWalker

's logical view.

---

#### lastChild

Node

lastChild()

Moves the

TreeWalker

to the last visible child of the
current node, and returns the new node. If the current node has no
visible children, returns

null

, and retains the current
node.

previousSibling

```java
Node
previousSibling()
```

Moves the

TreeWalker

to the previous sibling of the
current node, and returns the new node. If the current node has no
visible previous sibling, returns

null

, and retains the
current node.

**Returns:** The new node, or

null

if the current node has no
previous sibling. in the

TreeWalker

's logical view.

---

#### previousSibling

Node

previousSibling()

Moves the

TreeWalker

to the previous sibling of the
current node, and returns the new node. If the current node has no
visible previous sibling, returns

null

, and retains the
current node.

nextSibling

```java
Node
nextSibling()
```

Moves the

TreeWalker

to the next sibling of the current
node, and returns the new node. If the current node has no visible
next sibling, returns

null

, and retains the current node.

**Returns:** The new node, or

null

if the current node has no
next sibling. in the

TreeWalker

's logical view.

---

#### nextSibling

Node

nextSibling()

Moves the

TreeWalker

to the next sibling of the current
node, and returns the new node. If the current node has no visible
next sibling, returns

null

, and retains the current node.

previousNode

```java
Node
previousNode()
```

Moves the

TreeWalker

to the previous visible node in
document order relative to the current node, and returns the new
node. If the current node has no previous node, or if the search for

previousNode

attempts to step upward from the

TreeWalker

's

root

node, returns

null

, and retains the current node.

**Returns:** The new node, or

null

if the current node has no
previous node in the

TreeWalker

's logical view.

---

#### previousNode

Node

previousNode()

Moves the

TreeWalker

to the previous visible node in
document order relative to the current node, and returns the new
node. If the current node has no previous node, or if the search for

previousNode

attempts to step upward from the

TreeWalker

's

root

node, returns

null

, and retains the current node.

nextNode

```java
Node
nextNode()
```

Moves the

TreeWalker

to the next visible node in document
order relative to the current node, and returns the new node. If the
current node has no next node, or if the search for nextNode attempts
to step upward from the

TreeWalker

's

root

node, returns

null

, and retains the current node.

**Returns:** The new node, or

null

if the current node has no
next node in the

TreeWalker

's logical view.

---

#### nextNode

Node

nextNode()

Moves the

TreeWalker

to the next visible node in document
order relative to the current node, and returns the new node. If the
current node has no next node, or if the search for nextNode attempts
to step upward from the

TreeWalker

's

root

node, returns

null

, and retains the current node.

---

