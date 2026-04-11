# Interface XPathResult

**Source:** `jdk.xml.dom\org\w3c\dom\xpath\XPathResult.html`

### Class Description

```java
public interface
XPathResult
```

The

XPathResult

interface represents the result of the
evaluation of an XPath 1.0 expression within the context of a particular
node. Since evaluation of an XPath expression can result in various
result types, this object makes it possible to discover and manipulate
the type and value of the result.

See also the

Document Object Model (DOM) Level 3 XPath Specification

.

---

### Field Details

#### static final short ANY_TYPE

This code does not represent a specific type. An evaluation of an XPath
expression will never produce this type. If this type is requested,
then the evaluation returns whatever type naturally results from
evaluation of the expression.

If the natural result is a node set when

ANY_TYPE

was
requested, then

UNORDERED_NODE_ITERATOR_TYPE

is always
the resulting type. Any other representation of a node set must be
explicitly requested.

**See Also:**
- Constant Field Values

---

#### static final short NUMBER_TYPE

The result is a number as defined by . Document modification does not
invalidate the number, but may mean that reevaluation would not yield
the same number.

**See Also:**
- Constant Field Values

---

#### static final short STRING_TYPE

The result is a string as defined by . Document modification does not
invalidate the string, but may mean that the string no longer
corresponds to the current document.

**See Also:**
- Constant Field Values

---

#### static final short BOOLEAN_TYPE

The result is a boolean as defined by . Document modification does not
invalidate the boolean, but may mean that reevaluation would not
yield the same boolean.

**See Also:**
- Constant Field Values

---

#### static final short UNORDERED_NODE_ITERATOR_TYPE

The result is a node set as defined by that will be accessed
iteratively, which may not produce nodes in a particular order.
Document modification invalidates the iteration.

This is the default type returned if the result is a node set and

ANY_TYPE

is requested.

**See Also:**
- Constant Field Values

---

#### static final short ORDERED_NODE_ITERATOR_TYPE

The result is a node set as defined by that will be accessed
iteratively, which will produce document-ordered nodes. Document
modification invalidates the iteration.

**See Also:**
- Constant Field Values

---

#### static final short UNORDERED_NODE_SNAPSHOT_TYPE

The result is a node set as defined by that will be accessed as a
snapshot list of nodes that may not be in a particular order.
Document modification does not invalidate the snapshot but may mean
that reevaluation would not yield the same snapshot and nodes in the
snapshot may have been altered, moved, or removed from the document.

**See Also:**
- Constant Field Values

---

#### static final short ORDERED_NODE_SNAPSHOT_TYPE

The result is a node set as defined by that will be accessed as a
snapshot list of nodes that will be in original document order.
Document modification does not invalidate the snapshot but may mean
that reevaluation would not yield the same snapshot and nodes in the
snapshot may have been altered, moved, or removed from the document.

**See Also:**
- Constant Field Values

---

#### static final short ANY_UNORDERED_NODE_TYPE

The result is a node set as defined by and will be accessed as a
single node, which may be

null

if the node set is empty.
Document modification does not invalidate the node, but may mean that
the result node no longer corresponds to the current document. This
is a convenience that permits optimization since the implementation
can stop once any node in the in the resulting set has been found.

If there are more than one node in the actual result, the single
node returned might not be the first in document order.

**See Also:**
- Constant Field Values

---

#### static final short FIRST_ORDERED_NODE_TYPE

The result is a node set as defined by and will be accessed as a
single node, which may be

null

if the node set is empty.
Document modification does not invalidate the node, but may mean that
the result node no longer corresponds to the current document. This
is a convenience that permits optimization since the implementation
can stop once the first node in document order of the resulting set
has been found.

If there are more than one node in the actual result, the single
node returned will be the first in document order.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### short getResultType()

A code representing the type of this result, as defined by the type
constants.

---

#### double getNumberValue()
throws
XPathException

The value of this number result. If the native double type of the DOM
binding does not directly support the exact IEEE 754 result of the
XPath expression, then it is up to the definition of the binding
binding to specify how the XPath number is converted to the native
binding number.

**Throws:**
- XPathException

- TYPE_ERR: raised if

resultType

is not

NUMBER_TYPE

.

---

#### String
getStringValue()
throws
XPathException

The value of this string result.

**Throws:**
- XPathException

- TYPE_ERR: raised if

resultType

is not

STRING_TYPE

.

---

#### boolean getBooleanValue()
throws
XPathException

The value of this boolean result.

**Throws:**
- XPathException

- TYPE_ERR: raised if

resultType

is not

BOOLEAN_TYPE

.

---

#### Node
getSingleNodeValue()
throws
XPathException

The value of this single node result, which may be

null

.

**Throws:**
- XPathException

- TYPE_ERR: raised if

resultType

is not

ANY_UNORDERED_NODE_TYPE

or

FIRST_ORDERED_NODE_TYPE

.

---

#### boolean getInvalidIteratorState()

Signifies that the iterator has become invalid. True if

resultType

is

UNORDERED_NODE_ITERATOR_TYPE

or

ORDERED_NODE_ITERATOR_TYPE

and the document has been
modified since this result was returned.

---

#### int getSnapshotLength()
throws
XPathException

The number of nodes in the result snapshot. Valid values for
snapshotItem indices are

0

to

snapshotLength-1

inclusive.

**Throws:**
- XPathException

- TYPE_ERR: raised if

resultType

is not

UNORDERED_NODE_SNAPSHOT_TYPE

or

ORDERED_NODE_SNAPSHOT_TYPE

.

---

#### Node
iterateNext()
throws
XPathException
,

DOMException

Iterates and returns the next node from the node set or

null

if there are no more nodes.

**Returns:**
- Returns the next node.

**Throws:**
- XPathException

- TYPE_ERR: raised if

resultType

is not

UNORDERED_NODE_ITERATOR_TYPE

or

ORDERED_NODE_ITERATOR_TYPE

.
- DOMException

- INVALID_STATE_ERR: The document has been mutated since the result was
returned.

---

#### Node
snapshotItem​(int index)
throws
XPathException

Returns the

index

th item in the snapshot collection. If

index

is greater than or equal to the number of nodes in
the list, this method returns

null

. Unlike the iterator
result, the snapshot does not become invalid, but may not correspond
to the current document if it is mutated.

**Parameters:**
- index

- Index into the snapshot collection.

**Returns:**
- The node at the

index

th position in the

NodeList

, or

null

if that is not a valid
index.

**Throws:**
- XPathException

- TYPE_ERR: raised if

resultType

is not

UNORDERED_NODE_SNAPSHOT_TYPE

or

ORDERED_NODE_SNAPSHOT_TYPE

.

---

### Additional Sections

#### Interface XPathResult

```java
public interface
XPathResult
```

The

XPathResult

interface represents the result of the
evaluation of an XPath 1.0 expression within the context of a particular
node. Since evaluation of an XPath expression can result in various
result types, this object makes it possible to discover and manipulate
the type and value of the result.

See also the

Document Object Model (DOM) Level 3 XPath Specification

.

public interface

XPathResult

The

XPathResult

interface represents the result of the
evaluation of an XPath 1.0 expression within the context of a particular
node. Since evaluation of an XPath expression can result in various
result types, this object makes it possible to discover and manipulate
the type and value of the result.

See also the

Document Object Model (DOM) Level 3 XPath Specification

.

See also the

Document Object Model (DOM) Level 3 XPath Specification

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static short

ANY_TYPE

This code does not represent a specific type.

static short

ANY_UNORDERED_NODE_TYPE

The result is a node set as defined by and will be accessed as a
single node, which may be

null

if the node set is empty.

static short

BOOLEAN_TYPE

The result is a boolean as defined by .

static short

FIRST_ORDERED_NODE_TYPE

The result is a node set as defined by and will be accessed as a
single node, which may be

null

if the node set is empty.

static short

NUMBER_TYPE

The result is a number as defined by .

static short

ORDERED_NODE_ITERATOR_TYPE

The result is a node set as defined by that will be accessed
iteratively, which will produce document-ordered nodes.

static short

ORDERED_NODE_SNAPSHOT_TYPE

The result is a node set as defined by that will be accessed as a
snapshot list of nodes that will be in original document order.

static short

STRING_TYPE

The result is a string as defined by .

static short

UNORDERED_NODE_ITERATOR_TYPE

The result is a node set as defined by that will be accessed
iteratively, which may not produce nodes in a particular order.

static short

UNORDERED_NODE_SNAPSHOT_TYPE

The result is a node set as defined by that will be accessed as a
snapshot list of nodes that may not be in a particular order.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

getBooleanValue

()

The value of this boolean result.

boolean

getInvalidIteratorState

()

Signifies that the iterator has become invalid.

double

getNumberValue

()

The value of this number result.

short

getResultType

()

A code representing the type of this result, as defined by the type
constants.

Node

getSingleNodeValue

()

The value of this single node result, which may be

null

.

int

getSnapshotLength

()

The number of nodes in the result snapshot.

String

getStringValue

()

The value of this string result.

Node

iterateNext

()

Iterates and returns the next node from the node set or

null

if there are no more nodes.

Node

snapshotItem

​(int index)

Returns the

index

th item in the snapshot collection.

Field Summary

Fields

Modifier and Type

Field

Description

static short

ANY_TYPE

This code does not represent a specific type.

static short

ANY_UNORDERED_NODE_TYPE

The result is a node set as defined by and will be accessed as a
single node, which may be

null

if the node set is empty.

static short

BOOLEAN_TYPE

The result is a boolean as defined by .

static short

FIRST_ORDERED_NODE_TYPE

The result is a node set as defined by and will be accessed as a
single node, which may be

null

if the node set is empty.

static short

NUMBER_TYPE

The result is a number as defined by .

static short

ORDERED_NODE_ITERATOR_TYPE

The result is a node set as defined by that will be accessed
iteratively, which will produce document-ordered nodes.

static short

ORDERED_NODE_SNAPSHOT_TYPE

The result is a node set as defined by that will be accessed as a
snapshot list of nodes that will be in original document order.

static short

STRING_TYPE

The result is a string as defined by .

static short

UNORDERED_NODE_ITERATOR_TYPE

The result is a node set as defined by that will be accessed
iteratively, which may not produce nodes in a particular order.

static short

UNORDERED_NODE_SNAPSHOT_TYPE

The result is a node set as defined by that will be accessed as a
snapshot list of nodes that may not be in a particular order.

---

#### Field Summary

This code does not represent a specific type.

The result is a node set as defined by and will be accessed as a
single node, which may be

null

if the node set is empty.

The result is a boolean as defined by .

The result is a number as defined by .

The result is a node set as defined by that will be accessed
iteratively, which will produce document-ordered nodes.

The result is a node set as defined by that will be accessed as a
snapshot list of nodes that will be in original document order.

The result is a string as defined by .

The result is a node set as defined by that will be accessed
iteratively, which may not produce nodes in a particular order.

The result is a node set as defined by that will be accessed as a
snapshot list of nodes that may not be in a particular order.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

getBooleanValue

()

The value of this boolean result.

boolean

getInvalidIteratorState

()

Signifies that the iterator has become invalid.

double

getNumberValue

()

The value of this number result.

short

getResultType

()

A code representing the type of this result, as defined by the type
constants.

Node

getSingleNodeValue

()

The value of this single node result, which may be

null

.

int

getSnapshotLength

()

The number of nodes in the result snapshot.

String

getStringValue

()

The value of this string result.

Node

iterateNext

()

Iterates and returns the next node from the node set or

null

if there are no more nodes.

Node

snapshotItem

​(int index)

Returns the

index

th item in the snapshot collection.

---

#### Method Summary

The value of this boolean result.

Signifies that the iterator has become invalid.

The value of this number result.

A code representing the type of this result, as defined by the type
constants.

The value of this single node result, which may be

null

.

The number of nodes in the result snapshot.

The value of this string result.

Iterates and returns the next node from the node set or

null

if there are no more nodes.

Returns the

index

th item in the snapshot collection.

============ FIELD DETAIL ===========

- Field Detail

- ANY_TYPE

```java
static final short ANY_TYPE
```

This code does not represent a specific type. An evaluation of an XPath
expression will never produce this type. If this type is requested,
then the evaluation returns whatever type naturally results from
evaluation of the expression.

If the natural result is a node set when

ANY_TYPE

was
requested, then

UNORDERED_NODE_ITERATOR_TYPE

is always
the resulting type. Any other representation of a node set must be
explicitly requested.

**See Also:** Constant Field Values

- NUMBER_TYPE

```java
static final short NUMBER_TYPE
```

The result is a number as defined by . Document modification does not
invalidate the number, but may mean that reevaluation would not yield
the same number.

**See Also:** Constant Field Values

- STRING_TYPE

```java
static final short STRING_TYPE
```

The result is a string as defined by . Document modification does not
invalidate the string, but may mean that the string no longer
corresponds to the current document.

**See Also:** Constant Field Values

- BOOLEAN_TYPE

```java
static final short BOOLEAN_TYPE
```

The result is a boolean as defined by . Document modification does not
invalidate the boolean, but may mean that reevaluation would not
yield the same boolean.

**See Also:** Constant Field Values

- UNORDERED_NODE_ITERATOR_TYPE

```java
static final short UNORDERED_NODE_ITERATOR_TYPE
```

The result is a node set as defined by that will be accessed
iteratively, which may not produce nodes in a particular order.
Document modification invalidates the iteration.

This is the default type returned if the result is a node set and

ANY_TYPE

is requested.

**See Also:** Constant Field Values

- ORDERED_NODE_ITERATOR_TYPE

```java
static final short ORDERED_NODE_ITERATOR_TYPE
```

The result is a node set as defined by that will be accessed
iteratively, which will produce document-ordered nodes. Document
modification invalidates the iteration.

**See Also:** Constant Field Values

- UNORDERED_NODE_SNAPSHOT_TYPE

```java
static final short UNORDERED_NODE_SNAPSHOT_TYPE
```

The result is a node set as defined by that will be accessed as a
snapshot list of nodes that may not be in a particular order.
Document modification does not invalidate the snapshot but may mean
that reevaluation would not yield the same snapshot and nodes in the
snapshot may have been altered, moved, or removed from the document.

**See Also:** Constant Field Values

- ORDERED_NODE_SNAPSHOT_TYPE

```java
static final short ORDERED_NODE_SNAPSHOT_TYPE
```

The result is a node set as defined by that will be accessed as a
snapshot list of nodes that will be in original document order.
Document modification does not invalidate the snapshot but may mean
that reevaluation would not yield the same snapshot and nodes in the
snapshot may have been altered, moved, or removed from the document.

**See Also:** Constant Field Values

- ANY_UNORDERED_NODE_TYPE

```java
static final short ANY_UNORDERED_NODE_TYPE
```

The result is a node set as defined by and will be accessed as a
single node, which may be

null

if the node set is empty.
Document modification does not invalidate the node, but may mean that
the result node no longer corresponds to the current document. This
is a convenience that permits optimization since the implementation
can stop once any node in the in the resulting set has been found.

If there are more than one node in the actual result, the single
node returned might not be the first in document order.

**See Also:** Constant Field Values

- FIRST_ORDERED_NODE_TYPE

```java
static final short FIRST_ORDERED_NODE_TYPE
```

The result is a node set as defined by and will be accessed as a
single node, which may be

null

if the node set is empty.
Document modification does not invalidate the node, but may mean that
the result node no longer corresponds to the current document. This
is a convenience that permits optimization since the implementation
can stop once the first node in document order of the resulting set
has been found.

If there are more than one node in the actual result, the single
node returned will be the first in document order.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getResultType

```java
short getResultType()
```

A code representing the type of this result, as defined by the type
constants.

- getNumberValue

```java
double getNumberValue()
throws
XPathException
```

The value of this number result. If the native double type of the DOM
binding does not directly support the exact IEEE 754 result of the
XPath expression, then it is up to the definition of the binding
binding to specify how the XPath number is converted to the native
binding number.

**Throws:** XPathException

- TYPE_ERR: raised if

resultType

is not

NUMBER_TYPE

.

- getStringValue

```java
String
getStringValue()
throws
XPathException
```

The value of this string result.

**Throws:** XPathException

- TYPE_ERR: raised if

resultType

is not

STRING_TYPE

.

- getBooleanValue

```java
boolean getBooleanValue()
throws
XPathException
```

The value of this boolean result.

**Throws:** XPathException

- TYPE_ERR: raised if

resultType

is not

BOOLEAN_TYPE

.

- getSingleNodeValue

```java
Node
getSingleNodeValue()
throws
XPathException
```

The value of this single node result, which may be

null

.

**Throws:** XPathException

- TYPE_ERR: raised if

resultType

is not

ANY_UNORDERED_NODE_TYPE

or

FIRST_ORDERED_NODE_TYPE

.

- getInvalidIteratorState

```java
boolean getInvalidIteratorState()
```

Signifies that the iterator has become invalid. True if

resultType

is

UNORDERED_NODE_ITERATOR_TYPE

or

ORDERED_NODE_ITERATOR_TYPE

and the document has been
modified since this result was returned.

- getSnapshotLength

```java
int getSnapshotLength()
throws
XPathException
```

The number of nodes in the result snapshot. Valid values for
snapshotItem indices are

0

to

snapshotLength-1

inclusive.

**Throws:** XPathException

- TYPE_ERR: raised if

resultType

is not

UNORDERED_NODE_SNAPSHOT_TYPE

or

ORDERED_NODE_SNAPSHOT_TYPE

.

- iterateNext

```java
Node
iterateNext()
throws
XPathException
,

DOMException
```

Iterates and returns the next node from the node set or

null

if there are no more nodes.

**Returns:** Returns the next node.
**Throws:** XPathException

- TYPE_ERR: raised if

resultType

is not

UNORDERED_NODE_ITERATOR_TYPE

or

ORDERED_NODE_ITERATOR_TYPE

.
**Throws:** DOMException

- INVALID_STATE_ERR: The document has been mutated since the result was
returned.

- snapshotItem

```java
Node
snapshotItem​(int index)
throws
XPathException
```

Returns the

index

th item in the snapshot collection. If

index

is greater than or equal to the number of nodes in
the list, this method returns

null

. Unlike the iterator
result, the snapshot does not become invalid, but may not correspond
to the current document if it is mutated.

**Parameters:** index

- Index into the snapshot collection.
**Returns:** The node at the

index

th position in the

NodeList

, or

null

if that is not a valid
index.
**Throws:** XPathException

- TYPE_ERR: raised if

resultType

is not

UNORDERED_NODE_SNAPSHOT_TYPE

or

ORDERED_NODE_SNAPSHOT_TYPE

.

Field Detail

- ANY_TYPE

```java
static final short ANY_TYPE
```

This code does not represent a specific type. An evaluation of an XPath
expression will never produce this type. If this type is requested,
then the evaluation returns whatever type naturally results from
evaluation of the expression.

If the natural result is a node set when

ANY_TYPE

was
requested, then

UNORDERED_NODE_ITERATOR_TYPE

is always
the resulting type. Any other representation of a node set must be
explicitly requested.

**See Also:** Constant Field Values

- NUMBER_TYPE

```java
static final short NUMBER_TYPE
```

The result is a number as defined by . Document modification does not
invalidate the number, but may mean that reevaluation would not yield
the same number.

**See Also:** Constant Field Values

- STRING_TYPE

```java
static final short STRING_TYPE
```

The result is a string as defined by . Document modification does not
invalidate the string, but may mean that the string no longer
corresponds to the current document.

**See Also:** Constant Field Values

- BOOLEAN_TYPE

```java
static final short BOOLEAN_TYPE
```

The result is a boolean as defined by . Document modification does not
invalidate the boolean, but may mean that reevaluation would not
yield the same boolean.

**See Also:** Constant Field Values

- UNORDERED_NODE_ITERATOR_TYPE

```java
static final short UNORDERED_NODE_ITERATOR_TYPE
```

The result is a node set as defined by that will be accessed
iteratively, which may not produce nodes in a particular order.
Document modification invalidates the iteration.

This is the default type returned if the result is a node set and

ANY_TYPE

is requested.

**See Also:** Constant Field Values

- ORDERED_NODE_ITERATOR_TYPE

```java
static final short ORDERED_NODE_ITERATOR_TYPE
```

The result is a node set as defined by that will be accessed
iteratively, which will produce document-ordered nodes. Document
modification invalidates the iteration.

**See Also:** Constant Field Values

- UNORDERED_NODE_SNAPSHOT_TYPE

```java
static final short UNORDERED_NODE_SNAPSHOT_TYPE
```

The result is a node set as defined by that will be accessed as a
snapshot list of nodes that may not be in a particular order.
Document modification does not invalidate the snapshot but may mean
that reevaluation would not yield the same snapshot and nodes in the
snapshot may have been altered, moved, or removed from the document.

**See Also:** Constant Field Values

- ORDERED_NODE_SNAPSHOT_TYPE

```java
static final short ORDERED_NODE_SNAPSHOT_TYPE
```

The result is a node set as defined by that will be accessed as a
snapshot list of nodes that will be in original document order.
Document modification does not invalidate the snapshot but may mean
that reevaluation would not yield the same snapshot and nodes in the
snapshot may have been altered, moved, or removed from the document.

**See Also:** Constant Field Values

- ANY_UNORDERED_NODE_TYPE

```java
static final short ANY_UNORDERED_NODE_TYPE
```

The result is a node set as defined by and will be accessed as a
single node, which may be

null

if the node set is empty.
Document modification does not invalidate the node, but may mean that
the result node no longer corresponds to the current document. This
is a convenience that permits optimization since the implementation
can stop once any node in the in the resulting set has been found.

If there are more than one node in the actual result, the single
node returned might not be the first in document order.

**See Also:** Constant Field Values

- FIRST_ORDERED_NODE_TYPE

```java
static final short FIRST_ORDERED_NODE_TYPE
```

The result is a node set as defined by and will be accessed as a
single node, which may be

null

if the node set is empty.
Document modification does not invalidate the node, but may mean that
the result node no longer corresponds to the current document. This
is a convenience that permits optimization since the implementation
can stop once the first node in document order of the resulting set
has been found.

If there are more than one node in the actual result, the single
node returned will be the first in document order.

**See Also:** Constant Field Values

---

#### Field Detail

ANY_TYPE

```java
static final short ANY_TYPE
```

This code does not represent a specific type. An evaluation of an XPath
expression will never produce this type. If this type is requested,
then the evaluation returns whatever type naturally results from
evaluation of the expression.

If the natural result is a node set when

ANY_TYPE

was
requested, then

UNORDERED_NODE_ITERATOR_TYPE

is always
the resulting type. Any other representation of a node set must be
explicitly requested.

**See Also:** Constant Field Values

---

#### ANY_TYPE

static final short ANY_TYPE

This code does not represent a specific type. An evaluation of an XPath
expression will never produce this type. If this type is requested,
then the evaluation returns whatever type naturally results from
evaluation of the expression.

If the natural result is a node set when

ANY_TYPE

was
requested, then

UNORDERED_NODE_ITERATOR_TYPE

is always
the resulting type. Any other representation of a node set must be
explicitly requested.

NUMBER_TYPE

```java
static final short NUMBER_TYPE
```

The result is a number as defined by . Document modification does not
invalidate the number, but may mean that reevaluation would not yield
the same number.

**See Also:** Constant Field Values

---

#### NUMBER_TYPE

static final short NUMBER_TYPE

The result is a number as defined by . Document modification does not
invalidate the number, but may mean that reevaluation would not yield
the same number.

STRING_TYPE

```java
static final short STRING_TYPE
```

The result is a string as defined by . Document modification does not
invalidate the string, but may mean that the string no longer
corresponds to the current document.

**See Also:** Constant Field Values

---

#### STRING_TYPE

static final short STRING_TYPE

The result is a string as defined by . Document modification does not
invalidate the string, but may mean that the string no longer
corresponds to the current document.

BOOLEAN_TYPE

```java
static final short BOOLEAN_TYPE
```

The result is a boolean as defined by . Document modification does not
invalidate the boolean, but may mean that reevaluation would not
yield the same boolean.

**See Also:** Constant Field Values

---

#### BOOLEAN_TYPE

static final short BOOLEAN_TYPE

The result is a boolean as defined by . Document modification does not
invalidate the boolean, but may mean that reevaluation would not
yield the same boolean.

UNORDERED_NODE_ITERATOR_TYPE

```java
static final short UNORDERED_NODE_ITERATOR_TYPE
```

The result is a node set as defined by that will be accessed
iteratively, which may not produce nodes in a particular order.
Document modification invalidates the iteration.

This is the default type returned if the result is a node set and

ANY_TYPE

is requested.

**See Also:** Constant Field Values

---

#### UNORDERED_NODE_ITERATOR_TYPE

static final short UNORDERED_NODE_ITERATOR_TYPE

The result is a node set as defined by that will be accessed
iteratively, which may not produce nodes in a particular order.
Document modification invalidates the iteration.

This is the default type returned if the result is a node set and

ANY_TYPE

is requested.

ORDERED_NODE_ITERATOR_TYPE

```java
static final short ORDERED_NODE_ITERATOR_TYPE
```

The result is a node set as defined by that will be accessed
iteratively, which will produce document-ordered nodes. Document
modification invalidates the iteration.

**See Also:** Constant Field Values

---

#### ORDERED_NODE_ITERATOR_TYPE

static final short ORDERED_NODE_ITERATOR_TYPE

The result is a node set as defined by that will be accessed
iteratively, which will produce document-ordered nodes. Document
modification invalidates the iteration.

UNORDERED_NODE_SNAPSHOT_TYPE

```java
static final short UNORDERED_NODE_SNAPSHOT_TYPE
```

The result is a node set as defined by that will be accessed as a
snapshot list of nodes that may not be in a particular order.
Document modification does not invalidate the snapshot but may mean
that reevaluation would not yield the same snapshot and nodes in the
snapshot may have been altered, moved, or removed from the document.

**See Also:** Constant Field Values

---

#### UNORDERED_NODE_SNAPSHOT_TYPE

static final short UNORDERED_NODE_SNAPSHOT_TYPE

The result is a node set as defined by that will be accessed as a
snapshot list of nodes that may not be in a particular order.
Document modification does not invalidate the snapshot but may mean
that reevaluation would not yield the same snapshot and nodes in the
snapshot may have been altered, moved, or removed from the document.

ORDERED_NODE_SNAPSHOT_TYPE

```java
static final short ORDERED_NODE_SNAPSHOT_TYPE
```

The result is a node set as defined by that will be accessed as a
snapshot list of nodes that will be in original document order.
Document modification does not invalidate the snapshot but may mean
that reevaluation would not yield the same snapshot and nodes in the
snapshot may have been altered, moved, or removed from the document.

**See Also:** Constant Field Values

---

#### ORDERED_NODE_SNAPSHOT_TYPE

static final short ORDERED_NODE_SNAPSHOT_TYPE

The result is a node set as defined by that will be accessed as a
snapshot list of nodes that will be in original document order.
Document modification does not invalidate the snapshot but may mean
that reevaluation would not yield the same snapshot and nodes in the
snapshot may have been altered, moved, or removed from the document.

ANY_UNORDERED_NODE_TYPE

```java
static final short ANY_UNORDERED_NODE_TYPE
```

The result is a node set as defined by and will be accessed as a
single node, which may be

null

if the node set is empty.
Document modification does not invalidate the node, but may mean that
the result node no longer corresponds to the current document. This
is a convenience that permits optimization since the implementation
can stop once any node in the in the resulting set has been found.

If there are more than one node in the actual result, the single
node returned might not be the first in document order.

**See Also:** Constant Field Values

---

#### ANY_UNORDERED_NODE_TYPE

static final short ANY_UNORDERED_NODE_TYPE

The result is a node set as defined by and will be accessed as a
single node, which may be

null

if the node set is empty.
Document modification does not invalidate the node, but may mean that
the result node no longer corresponds to the current document. This
is a convenience that permits optimization since the implementation
can stop once any node in the in the resulting set has been found.

If there are more than one node in the actual result, the single
node returned might not be the first in document order.

FIRST_ORDERED_NODE_TYPE

```java
static final short FIRST_ORDERED_NODE_TYPE
```

The result is a node set as defined by and will be accessed as a
single node, which may be

null

if the node set is empty.
Document modification does not invalidate the node, but may mean that
the result node no longer corresponds to the current document. This
is a convenience that permits optimization since the implementation
can stop once the first node in document order of the resulting set
has been found.

If there are more than one node in the actual result, the single
node returned will be the first in document order.

**See Also:** Constant Field Values

---

#### FIRST_ORDERED_NODE_TYPE

static final short FIRST_ORDERED_NODE_TYPE

The result is a node set as defined by and will be accessed as a
single node, which may be

null

if the node set is empty.
Document modification does not invalidate the node, but may mean that
the result node no longer corresponds to the current document. This
is a convenience that permits optimization since the implementation
can stop once the first node in document order of the resulting set
has been found.

If there are more than one node in the actual result, the single
node returned will be the first in document order.

Method Detail

- getResultType

```java
short getResultType()
```

A code representing the type of this result, as defined by the type
constants.

- getNumberValue

```java
double getNumberValue()
throws
XPathException
```

The value of this number result. If the native double type of the DOM
binding does not directly support the exact IEEE 754 result of the
XPath expression, then it is up to the definition of the binding
binding to specify how the XPath number is converted to the native
binding number.

**Throws:** XPathException

- TYPE_ERR: raised if

resultType

is not

NUMBER_TYPE

.

- getStringValue

```java
String
getStringValue()
throws
XPathException
```

The value of this string result.

**Throws:** XPathException

- TYPE_ERR: raised if

resultType

is not

STRING_TYPE

.

- getBooleanValue

```java
boolean getBooleanValue()
throws
XPathException
```

The value of this boolean result.

**Throws:** XPathException

- TYPE_ERR: raised if

resultType

is not

BOOLEAN_TYPE

.

- getSingleNodeValue

```java
Node
getSingleNodeValue()
throws
XPathException
```

The value of this single node result, which may be

null

.

**Throws:** XPathException

- TYPE_ERR: raised if

resultType

is not

ANY_UNORDERED_NODE_TYPE

or

FIRST_ORDERED_NODE_TYPE

.

- getInvalidIteratorState

```java
boolean getInvalidIteratorState()
```

Signifies that the iterator has become invalid. True if

resultType

is

UNORDERED_NODE_ITERATOR_TYPE

or

ORDERED_NODE_ITERATOR_TYPE

and the document has been
modified since this result was returned.

- getSnapshotLength

```java
int getSnapshotLength()
throws
XPathException
```

The number of nodes in the result snapshot. Valid values for
snapshotItem indices are

0

to

snapshotLength-1

inclusive.

**Throws:** XPathException

- TYPE_ERR: raised if

resultType

is not

UNORDERED_NODE_SNAPSHOT_TYPE

or

ORDERED_NODE_SNAPSHOT_TYPE

.

- iterateNext

```java
Node
iterateNext()
throws
XPathException
,

DOMException
```

Iterates and returns the next node from the node set or

null

if there are no more nodes.

**Returns:** Returns the next node.
**Throws:** XPathException

- TYPE_ERR: raised if

resultType

is not

UNORDERED_NODE_ITERATOR_TYPE

or

ORDERED_NODE_ITERATOR_TYPE

.
**Throws:** DOMException

- INVALID_STATE_ERR: The document has been mutated since the result was
returned.

- snapshotItem

```java
Node
snapshotItem​(int index)
throws
XPathException
```

Returns the

index

th item in the snapshot collection. If

index

is greater than or equal to the number of nodes in
the list, this method returns

null

. Unlike the iterator
result, the snapshot does not become invalid, but may not correspond
to the current document if it is mutated.

**Parameters:** index

- Index into the snapshot collection.
**Returns:** The node at the

index

th position in the

NodeList

, or

null

if that is not a valid
index.
**Throws:** XPathException

- TYPE_ERR: raised if

resultType

is not

UNORDERED_NODE_SNAPSHOT_TYPE

or

ORDERED_NODE_SNAPSHOT_TYPE

.

---

#### Method Detail

getResultType

```java
short getResultType()
```

A code representing the type of this result, as defined by the type
constants.

---

#### getResultType

short getResultType()

A code representing the type of this result, as defined by the type
constants.

getNumberValue

```java
double getNumberValue()
throws
XPathException
```

The value of this number result. If the native double type of the DOM
binding does not directly support the exact IEEE 754 result of the
XPath expression, then it is up to the definition of the binding
binding to specify how the XPath number is converted to the native
binding number.

**Throws:** XPathException

- TYPE_ERR: raised if

resultType

is not

NUMBER_TYPE

.

---

#### getNumberValue

double getNumberValue()
throws

XPathException

The value of this number result. If the native double type of the DOM
binding does not directly support the exact IEEE 754 result of the
XPath expression, then it is up to the definition of the binding
binding to specify how the XPath number is converted to the native
binding number.

getStringValue

```java
String
getStringValue()
throws
XPathException
```

The value of this string result.

**Throws:** XPathException

- TYPE_ERR: raised if

resultType

is not

STRING_TYPE

.

---

#### getStringValue

String

getStringValue()
throws

XPathException

The value of this string result.

getBooleanValue

```java
boolean getBooleanValue()
throws
XPathException
```

The value of this boolean result.

**Throws:** XPathException

- TYPE_ERR: raised if

resultType

is not

BOOLEAN_TYPE

.

---

#### getBooleanValue

boolean getBooleanValue()
throws

XPathException

The value of this boolean result.

getSingleNodeValue

```java
Node
getSingleNodeValue()
throws
XPathException
```

The value of this single node result, which may be

null

.

**Throws:** XPathException

- TYPE_ERR: raised if

resultType

is not

ANY_UNORDERED_NODE_TYPE

or

FIRST_ORDERED_NODE_TYPE

.

---

#### getSingleNodeValue

Node

getSingleNodeValue()
throws

XPathException

The value of this single node result, which may be

null

.

getInvalidIteratorState

```java
boolean getInvalidIteratorState()
```

Signifies that the iterator has become invalid. True if

resultType

is

UNORDERED_NODE_ITERATOR_TYPE

or

ORDERED_NODE_ITERATOR_TYPE

and the document has been
modified since this result was returned.

---

#### getInvalidIteratorState

boolean getInvalidIteratorState()

Signifies that the iterator has become invalid. True if

resultType

is

UNORDERED_NODE_ITERATOR_TYPE

or

ORDERED_NODE_ITERATOR_TYPE

and the document has been
modified since this result was returned.

getSnapshotLength

```java
int getSnapshotLength()
throws
XPathException
```

The number of nodes in the result snapshot. Valid values for
snapshotItem indices are

0

to

snapshotLength-1

inclusive.

**Throws:** XPathException

- TYPE_ERR: raised if

resultType

is not

UNORDERED_NODE_SNAPSHOT_TYPE

or

ORDERED_NODE_SNAPSHOT_TYPE

.

---

#### getSnapshotLength

int getSnapshotLength()
throws

XPathException

The number of nodes in the result snapshot. Valid values for
snapshotItem indices are

0

to

snapshotLength-1

inclusive.

iterateNext

```java
Node
iterateNext()
throws
XPathException
,

DOMException
```

Iterates and returns the next node from the node set or

null

if there are no more nodes.

**Returns:** Returns the next node.
**Throws:** XPathException

- TYPE_ERR: raised if

resultType

is not

UNORDERED_NODE_ITERATOR_TYPE

or

ORDERED_NODE_ITERATOR_TYPE

.
**Throws:** DOMException

- INVALID_STATE_ERR: The document has been mutated since the result was
returned.

---

#### iterateNext

Node

iterateNext()
throws

XPathException

,

DOMException

Iterates and returns the next node from the node set or

null

if there are no more nodes.

snapshotItem

```java
Node
snapshotItem​(int index)
throws
XPathException
```

Returns the

index

th item in the snapshot collection. If

index

is greater than or equal to the number of nodes in
the list, this method returns

null

. Unlike the iterator
result, the snapshot does not become invalid, but may not correspond
to the current document if it is mutated.

**Parameters:** index

- Index into the snapshot collection.
**Returns:** The node at the

index

th position in the

NodeList

, or

null

if that is not a valid
index.
**Throws:** XPathException

- TYPE_ERR: raised if

resultType

is not

UNORDERED_NODE_SNAPSHOT_TYPE

or

ORDERED_NODE_SNAPSHOT_TYPE

.

---

#### snapshotItem

Node

snapshotItem​(int index)
throws

XPathException

Returns the

index

th item in the snapshot collection. If

index

is greater than or equal to the number of nodes in
the list, this method returns

null

. Unlike the iterator
result, the snapshot does not become invalid, but may not correspond
to the current document if it is mutated.

---

