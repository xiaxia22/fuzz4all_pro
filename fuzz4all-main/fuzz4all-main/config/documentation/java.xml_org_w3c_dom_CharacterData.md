# Interface CharacterData

**Source:** `java.xml\org\w3c\dom\CharacterData.html`

### Class Description

```java
public interface
CharacterData

extends
Node
```

The

CharacterData

interface extends Node with a set of
attributes and methods for accessing character data in the DOM. For
clarity this set is defined here rather than on each object that uses
these attributes and methods. No DOM objects correspond directly to

CharacterData

, though

Text

and others do
inherit the interface from it. All

offsets

in this interface
start from

0

.

As explained in the

DOMString

interface, text strings in
the DOM are represented in UTF-16, i.e. as a sequence of 16-bit units. In
the following, the term 16-bit units is used whenever necessary to
indicate that indexing on CharacterData is done in 16-bit units.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

**All Superinterfaces:** Node

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getData()
throws
DOMException

The character data of the node that implements this interface. The DOM
implementation may not put arbitrary limits on the amount of data
that may be stored in a

CharacterData

node. However,
implementation limits may mean that the entirety of a node's data may
not fit into a single

DOMString

. In such cases, the user
may call

substringData

to retrieve the data in
appropriately sized pieces.

**Throws:**
- DOMException

- DOMSTRING_SIZE_ERR: Raised when it would return more characters than
fit in a

DOMString

variable on the implementation
platform.

---

#### void setData​(
String
data)
throws
DOMException

The character data of the node that implements this interface. The DOM
implementation may not put arbitrary limits on the amount of data
that may be stored in a

CharacterData

node. However,
implementation limits may mean that the entirety of a node's data may
not fit into a single

DOMString

. In such cases, the user
may call

substringData

to retrieve the data in
appropriately sized pieces.

**Throws:**
- DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised when the node is readonly.

---

#### int getLength()

The number of 16-bit units that are available through

data

and the

substringData

method below. This may have the
value zero, i.e.,

CharacterData

nodes may be empty.

---

#### String
substringData​(int offset,
int count)
throws
DOMException

Extracts a range of data from the node.

**Parameters:**
- offset

- Start offset of substring to extract.
- count

- The number of 16-bit units to extract.

**Returns:**
- The specified substring. If the sum of

offset

and

count

exceeds the

length

, then all 16-bit
units to the end of the data are returned.

**Throws:**
- DOMException

- INDEX_SIZE_ERR: Raised if the specified

offset

is
negative or greater than the number of 16-bit units in

data

, or if the specified

count

is
negative.

DOMSTRING_SIZE_ERR: Raised if the specified range of text does
not fit into a

DOMString

.

---

#### void appendData​(
String
arg)
throws
DOMException

Append the string to the end of the character data of the node. Upon
success,

data

provides access to the concatenation of

data

and the

DOMString

specified.

**Parameters:**
- arg

- The

DOMString

to append.

**Throws:**
- DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised if this node is readonly.

---

#### void insertData​(int offset,

String
arg)
throws
DOMException

Insert a string at the specified 16-bit unit offset.

**Parameters:**
- offset

- The character offset at which to insert.
- arg

- The

DOMString

to insert.

**Throws:**
- DOMException

- INDEX_SIZE_ERR: Raised if the specified

offset

is
negative or greater than the number of 16-bit units in

data

.

NO_MODIFICATION_ALLOWED_ERR: Raised if this node is readonly.

---

#### void deleteData​(int offset,
int count)
throws
DOMException

Remove a range of 16-bit units from the node. Upon success,

data

and

length

reflect the change.

**Parameters:**
- offset

- The offset from which to start removing.
- count

- The number of 16-bit units to delete. If the sum of

offset

and

count

exceeds

length

then all 16-bit units from

offset

to the end of the data are deleted.

**Throws:**
- DOMException

- INDEX_SIZE_ERR: Raised if the specified

offset

is
negative or greater than the number of 16-bit units in

data

, or if the specified

count

is
negative.

NO_MODIFICATION_ALLOWED_ERR: Raised if this node is readonly.

---

#### void replaceData​(int offset,
int count,

String
arg)
throws
DOMException

Replace the characters starting at the specified 16-bit unit offset
with the specified string.

**Parameters:**
- offset

- The offset from which to start replacing.
- count

- The number of 16-bit units to replace. If the sum of

offset

and

count

exceeds

length

, then all 16-bit units to the end of the data
are replaced; (i.e., the effect is the same as a

remove

method call with the same range, followed by an

append

method invocation).
- arg

- The

DOMString

with which the range must be
replaced.

**Throws:**
- DOMException

- INDEX_SIZE_ERR: Raised if the specified

offset

is
negative or greater than the number of 16-bit units in

data

, or if the specified

count

is
negative.

NO_MODIFICATION_ALLOWED_ERR: Raised if this node is readonly.

---

### Additional Sections

#### Interface CharacterData

**All Superinterfaces:** Node

**All Known Subinterfaces:** CDATASection

,

Comment

,

Text

```java
public interface
CharacterData

extends
Node
```

The

CharacterData

interface extends Node with a set of
attributes and methods for accessing character data in the DOM. For
clarity this set is defined here rather than on each object that uses
these attributes and methods. No DOM objects correspond directly to

CharacterData

, though

Text

and others do
inherit the interface from it. All

offsets

in this interface
start from

0

.

As explained in the

DOMString

interface, text strings in
the DOM are represented in UTF-16, i.e. as a sequence of 16-bit units. In
the following, the term 16-bit units is used whenever necessary to
indicate that indexing on CharacterData is done in 16-bit units.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

public interface

CharacterData

extends

Node

The

CharacterData

interface extends Node with a set of
attributes and methods for accessing character data in the DOM. For
clarity this set is defined here rather than on each object that uses
these attributes and methods. No DOM objects correspond directly to

CharacterData

, though

Text

and others do
inherit the interface from it. All

offsets

in this interface
start from

0

.

As explained in the

DOMString

interface, text strings in
the DOM are represented in UTF-16, i.e. as a sequence of 16-bit units. In
the following, the term 16-bit units is used whenever necessary to
indicate that indexing on CharacterData is done in 16-bit units.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

As explained in the

DOMString

interface, text strings in
the DOM are represented in UTF-16, i.e. as a sequence of 16-bit units. In
the following, the term 16-bit units is used whenever necessary to
indicate that indexing on CharacterData is done in 16-bit units.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface org.w3c.dom.

Node

ATTRIBUTE_NODE

,

CDATA_SECTION_NODE

,

COMMENT_NODE

,

DOCUMENT_FRAGMENT_NODE

,

DOCUMENT_NODE

,

DOCUMENT_POSITION_CONTAINED_BY

,

DOCUMENT_POSITION_CONTAINS

,

DOCUMENT_POSITION_DISCONNECTED

,

DOCUMENT_POSITION_FOLLOWING

,

DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC

,

DOCUMENT_POSITION_PRECEDING

,

DOCUMENT_TYPE_NODE

,

ELEMENT_NODE

,

ENTITY_NODE

,

ENTITY_REFERENCE_NODE

,

NOTATION_NODE

,

PROCESSING_INSTRUCTION_NODE

,

TEXT_NODE

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

appendData

​(

String

arg)

Append the string to the end of the character data of the node.

void

deleteData

​(int offset,
int count)

Remove a range of 16-bit units from the node.

String

getData

()

The character data of the node that implements this interface.

int

getLength

()

The number of 16-bit units that are available through

data

and the

substringData

method below.

void

insertData

​(int offset,

String

arg)

Insert a string at the specified 16-bit unit offset.

void

replaceData

​(int offset,
int count,

String

arg)

Replace the characters starting at the specified 16-bit unit offset
with the specified string.

void

setData

​(

String

data)

The character data of the node that implements this interface.

String

substringData

​(int offset,
int count)

Extracts a range of data from the node.

- Methods declared in interface org.w3c.dom.

Node

appendChild

,

cloneNode

,

compareDocumentPosition

,

getAttributes

,

getBaseURI

,

getChildNodes

,

getFeature

,

getFirstChild

,

getLastChild

,

getLocalName

,

getNamespaceURI

,

getNextSibling

,

getNodeName

,

getNodeType

,

getNodeValue

,

getOwnerDocument

,

getParentNode

,

getPrefix

,

getPreviousSibling

,

getTextContent

,

getUserData

,

hasAttributes

,

hasChildNodes

,

insertBefore

,

isDefaultNamespace

,

isEqualNode

,

isSameNode

,

isSupported

,

lookupNamespaceURI

,

lookupPrefix

,

normalize

,

removeChild

,

replaceChild

,

setNodeValue

,

setPrefix

,

setTextContent

,

setUserData

Field Summary

- Fields declared in interface org.w3c.dom.

Node

ATTRIBUTE_NODE

,

CDATA_SECTION_NODE

,

COMMENT_NODE

,

DOCUMENT_FRAGMENT_NODE

,

DOCUMENT_NODE

,

DOCUMENT_POSITION_CONTAINED_BY

,

DOCUMENT_POSITION_CONTAINS

,

DOCUMENT_POSITION_DISCONNECTED

,

DOCUMENT_POSITION_FOLLOWING

,

DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC

,

DOCUMENT_POSITION_PRECEDING

,

DOCUMENT_TYPE_NODE

,

ELEMENT_NODE

,

ENTITY_NODE

,

ENTITY_REFERENCE_NODE

,

NOTATION_NODE

,

PROCESSING_INSTRUCTION_NODE

,

TEXT_NODE

---

#### Field Summary

Fields declared in interface org.w3c.dom.

Node

ATTRIBUTE_NODE

,

CDATA_SECTION_NODE

,

COMMENT_NODE

,

DOCUMENT_FRAGMENT_NODE

,

DOCUMENT_NODE

,

DOCUMENT_POSITION_CONTAINED_BY

,

DOCUMENT_POSITION_CONTAINS

,

DOCUMENT_POSITION_DISCONNECTED

,

DOCUMENT_POSITION_FOLLOWING

,

DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC

,

DOCUMENT_POSITION_PRECEDING

,

DOCUMENT_TYPE_NODE

,

ELEMENT_NODE

,

ENTITY_NODE

,

ENTITY_REFERENCE_NODE

,

NOTATION_NODE

,

PROCESSING_INSTRUCTION_NODE

,

TEXT_NODE

---

#### Fields declared in interface org.w3c.dom. Node

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

appendData

​(

String

arg)

Append the string to the end of the character data of the node.

void

deleteData

​(int offset,
int count)

Remove a range of 16-bit units from the node.

String

getData

()

The character data of the node that implements this interface.

int

getLength

()

The number of 16-bit units that are available through

data

and the

substringData

method below.

void

insertData

​(int offset,

String

arg)

Insert a string at the specified 16-bit unit offset.

void

replaceData

​(int offset,
int count,

String

arg)

Replace the characters starting at the specified 16-bit unit offset
with the specified string.

void

setData

​(

String

data)

The character data of the node that implements this interface.

String

substringData

​(int offset,
int count)

Extracts a range of data from the node.

- Methods declared in interface org.w3c.dom.

Node

appendChild

,

cloneNode

,

compareDocumentPosition

,

getAttributes

,

getBaseURI

,

getChildNodes

,

getFeature

,

getFirstChild

,

getLastChild

,

getLocalName

,

getNamespaceURI

,

getNextSibling

,

getNodeName

,

getNodeType

,

getNodeValue

,

getOwnerDocument

,

getParentNode

,

getPrefix

,

getPreviousSibling

,

getTextContent

,

getUserData

,

hasAttributes

,

hasChildNodes

,

insertBefore

,

isDefaultNamespace

,

isEqualNode

,

isSameNode

,

isSupported

,

lookupNamespaceURI

,

lookupPrefix

,

normalize

,

removeChild

,

replaceChild

,

setNodeValue

,

setPrefix

,

setTextContent

,

setUserData

---

#### Method Summary

Append the string to the end of the character data of the node.

Remove a range of 16-bit units from the node.

The character data of the node that implements this interface.

The number of 16-bit units that are available through

data

and the

substringData

method below.

Insert a string at the specified 16-bit unit offset.

Replace the characters starting at the specified 16-bit unit offset
with the specified string.

Extracts a range of data from the node.

Methods declared in interface org.w3c.dom.

Node

appendChild

,

cloneNode

,

compareDocumentPosition

,

getAttributes

,

getBaseURI

,

getChildNodes

,

getFeature

,

getFirstChild

,

getLastChild

,

getLocalName

,

getNamespaceURI

,

getNextSibling

,

getNodeName

,

getNodeType

,

getNodeValue

,

getOwnerDocument

,

getParentNode

,

getPrefix

,

getPreviousSibling

,

getTextContent

,

getUserData

,

hasAttributes

,

hasChildNodes

,

insertBefore

,

isDefaultNamespace

,

isEqualNode

,

isSameNode

,

isSupported

,

lookupNamespaceURI

,

lookupPrefix

,

normalize

,

removeChild

,

replaceChild

,

setNodeValue

,

setPrefix

,

setTextContent

,

setUserData

---

#### Methods declared in interface org.w3c.dom. Node

============ METHOD DETAIL ==========

- Method Detail

- getData

```java
String
getData()
throws
DOMException
```

The character data of the node that implements this interface. The DOM
implementation may not put arbitrary limits on the amount of data
that may be stored in a

CharacterData

node. However,
implementation limits may mean that the entirety of a node's data may
not fit into a single

DOMString

. In such cases, the user
may call

substringData

to retrieve the data in
appropriately sized pieces.

**Throws:** DOMException

- DOMSTRING_SIZE_ERR: Raised when it would return more characters than
fit in a

DOMString

variable on the implementation
platform.

- setData

```java
void setData​(
String
data)
throws
DOMException
```

The character data of the node that implements this interface. The DOM
implementation may not put arbitrary limits on the amount of data
that may be stored in a

CharacterData

node. However,
implementation limits may mean that the entirety of a node's data may
not fit into a single

DOMString

. In such cases, the user
may call

substringData

to retrieve the data in
appropriately sized pieces.

**Throws:** DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised when the node is readonly.

- getLength

```java
int getLength()
```

The number of 16-bit units that are available through

data

and the

substringData

method below. This may have the
value zero, i.e.,

CharacterData

nodes may be empty.

- substringData

```java
String
substringData​(int offset,
int count)
throws
DOMException
```

Extracts a range of data from the node.

**Parameters:** offset

- Start offset of substring to extract.
**Parameters:** count

- The number of 16-bit units to extract.
**Returns:** The specified substring. If the sum of

offset

and

count

exceeds the

length

, then all 16-bit
units to the end of the data are returned.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if the specified

offset

is
negative or greater than the number of 16-bit units in

data

, or if the specified

count

is
negative.

DOMSTRING_SIZE_ERR: Raised if the specified range of text does
not fit into a

DOMString

.

- appendData

```java
void appendData​(
String
arg)
throws
DOMException
```

Append the string to the end of the character data of the node. Upon
success,

data

provides access to the concatenation of

data

and the

DOMString

specified.

**Parameters:** arg

- The

DOMString

to append.
**Throws:** DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised if this node is readonly.

- insertData

```java
void insertData​(int offset,

String
arg)
throws
DOMException
```

Insert a string at the specified 16-bit unit offset.

**Parameters:** offset

- The character offset at which to insert.
**Parameters:** arg

- The

DOMString

to insert.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if the specified

offset

is
negative or greater than the number of 16-bit units in

data

.

NO_MODIFICATION_ALLOWED_ERR: Raised if this node is readonly.

- deleteData

```java
void deleteData​(int offset,
int count)
throws
DOMException
```

Remove a range of 16-bit units from the node. Upon success,

data

and

length

reflect the change.

**Parameters:** offset

- The offset from which to start removing.
**Parameters:** count

- The number of 16-bit units to delete. If the sum of

offset

and

count

exceeds

length

then all 16-bit units from

offset

to the end of the data are deleted.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if the specified

offset

is
negative or greater than the number of 16-bit units in

data

, or if the specified

count

is
negative.

NO_MODIFICATION_ALLOWED_ERR: Raised if this node is readonly.

- replaceData

```java
void replaceData​(int offset,
int count,

String
arg)
throws
DOMException
```

Replace the characters starting at the specified 16-bit unit offset
with the specified string.

**Parameters:** offset

- The offset from which to start replacing.
**Parameters:** count

- The number of 16-bit units to replace. If the sum of

offset

and

count

exceeds

length

, then all 16-bit units to the end of the data
are replaced; (i.e., the effect is the same as a

remove

method call with the same range, followed by an

append

method invocation).
**Parameters:** arg

- The

DOMString

with which the range must be
replaced.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if the specified

offset

is
negative or greater than the number of 16-bit units in

data

, or if the specified

count

is
negative.

NO_MODIFICATION_ALLOWED_ERR: Raised if this node is readonly.

Method Detail

- getData

```java
String
getData()
throws
DOMException
```

The character data of the node that implements this interface. The DOM
implementation may not put arbitrary limits on the amount of data
that may be stored in a

CharacterData

node. However,
implementation limits may mean that the entirety of a node's data may
not fit into a single

DOMString

. In such cases, the user
may call

substringData

to retrieve the data in
appropriately sized pieces.

**Throws:** DOMException

- DOMSTRING_SIZE_ERR: Raised when it would return more characters than
fit in a

DOMString

variable on the implementation
platform.

- setData

```java
void setData​(
String
data)
throws
DOMException
```

The character data of the node that implements this interface. The DOM
implementation may not put arbitrary limits on the amount of data
that may be stored in a

CharacterData

node. However,
implementation limits may mean that the entirety of a node's data may
not fit into a single

DOMString

. In such cases, the user
may call

substringData

to retrieve the data in
appropriately sized pieces.

**Throws:** DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised when the node is readonly.

- getLength

```java
int getLength()
```

The number of 16-bit units that are available through

data

and the

substringData

method below. This may have the
value zero, i.e.,

CharacterData

nodes may be empty.

- substringData

```java
String
substringData​(int offset,
int count)
throws
DOMException
```

Extracts a range of data from the node.

**Parameters:** offset

- Start offset of substring to extract.
**Parameters:** count

- The number of 16-bit units to extract.
**Returns:** The specified substring. If the sum of

offset

and

count

exceeds the

length

, then all 16-bit
units to the end of the data are returned.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if the specified

offset

is
negative or greater than the number of 16-bit units in

data

, or if the specified

count

is
negative.

DOMSTRING_SIZE_ERR: Raised if the specified range of text does
not fit into a

DOMString

.

- appendData

```java
void appendData​(
String
arg)
throws
DOMException
```

Append the string to the end of the character data of the node. Upon
success,

data

provides access to the concatenation of

data

and the

DOMString

specified.

**Parameters:** arg

- The

DOMString

to append.
**Throws:** DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised if this node is readonly.

- insertData

```java
void insertData​(int offset,

String
arg)
throws
DOMException
```

Insert a string at the specified 16-bit unit offset.

**Parameters:** offset

- The character offset at which to insert.
**Parameters:** arg

- The

DOMString

to insert.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if the specified

offset

is
negative or greater than the number of 16-bit units in

data

.

NO_MODIFICATION_ALLOWED_ERR: Raised if this node is readonly.

- deleteData

```java
void deleteData​(int offset,
int count)
throws
DOMException
```

Remove a range of 16-bit units from the node. Upon success,

data

and

length

reflect the change.

**Parameters:** offset

- The offset from which to start removing.
**Parameters:** count

- The number of 16-bit units to delete. If the sum of

offset

and

count

exceeds

length

then all 16-bit units from

offset

to the end of the data are deleted.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if the specified

offset

is
negative or greater than the number of 16-bit units in

data

, or if the specified

count

is
negative.

NO_MODIFICATION_ALLOWED_ERR: Raised if this node is readonly.

- replaceData

```java
void replaceData​(int offset,
int count,

String
arg)
throws
DOMException
```

Replace the characters starting at the specified 16-bit unit offset
with the specified string.

**Parameters:** offset

- The offset from which to start replacing.
**Parameters:** count

- The number of 16-bit units to replace. If the sum of

offset

and

count

exceeds

length

, then all 16-bit units to the end of the data
are replaced; (i.e., the effect is the same as a

remove

method call with the same range, followed by an

append

method invocation).
**Parameters:** arg

- The

DOMString

with which the range must be
replaced.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if the specified

offset

is
negative or greater than the number of 16-bit units in

data

, or if the specified

count

is
negative.

NO_MODIFICATION_ALLOWED_ERR: Raised if this node is readonly.

---

#### Method Detail

getData

```java
String
getData()
throws
DOMException
```

The character data of the node that implements this interface. The DOM
implementation may not put arbitrary limits on the amount of data
that may be stored in a

CharacterData

node. However,
implementation limits may mean that the entirety of a node's data may
not fit into a single

DOMString

. In such cases, the user
may call

substringData

to retrieve the data in
appropriately sized pieces.

**Throws:** DOMException

- DOMSTRING_SIZE_ERR: Raised when it would return more characters than
fit in a

DOMString

variable on the implementation
platform.

---

#### getData

String

getData()
throws

DOMException

The character data of the node that implements this interface. The DOM
implementation may not put arbitrary limits on the amount of data
that may be stored in a

CharacterData

node. However,
implementation limits may mean that the entirety of a node's data may
not fit into a single

DOMString

. In such cases, the user
may call

substringData

to retrieve the data in
appropriately sized pieces.

setData

```java
void setData​(
String
data)
throws
DOMException
```

The character data of the node that implements this interface. The DOM
implementation may not put arbitrary limits on the amount of data
that may be stored in a

CharacterData

node. However,
implementation limits may mean that the entirety of a node's data may
not fit into a single

DOMString

. In such cases, the user
may call

substringData

to retrieve the data in
appropriately sized pieces.

**Throws:** DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised when the node is readonly.

---

#### setData

void setData​(

String

data)
throws

DOMException

The character data of the node that implements this interface. The DOM
implementation may not put arbitrary limits on the amount of data
that may be stored in a

CharacterData

node. However,
implementation limits may mean that the entirety of a node's data may
not fit into a single

DOMString

. In such cases, the user
may call

substringData

to retrieve the data in
appropriately sized pieces.

getLength

```java
int getLength()
```

The number of 16-bit units that are available through

data

and the

substringData

method below. This may have the
value zero, i.e.,

CharacterData

nodes may be empty.

---

#### getLength

int getLength()

The number of 16-bit units that are available through

data

and the

substringData

method below. This may have the
value zero, i.e.,

CharacterData

nodes may be empty.

substringData

```java
String
substringData​(int offset,
int count)
throws
DOMException
```

Extracts a range of data from the node.

**Parameters:** offset

- Start offset of substring to extract.
**Parameters:** count

- The number of 16-bit units to extract.
**Returns:** The specified substring. If the sum of

offset

and

count

exceeds the

length

, then all 16-bit
units to the end of the data are returned.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if the specified

offset

is
negative or greater than the number of 16-bit units in

data

, or if the specified

count

is
negative.

DOMSTRING_SIZE_ERR: Raised if the specified range of text does
not fit into a

DOMString

.

---

#### substringData

String

substringData​(int offset,
int count)
throws

DOMException

Extracts a range of data from the node.

appendData

```java
void appendData​(
String
arg)
throws
DOMException
```

Append the string to the end of the character data of the node. Upon
success,

data

provides access to the concatenation of

data

and the

DOMString

specified.

**Parameters:** arg

- The

DOMString

to append.
**Throws:** DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised if this node is readonly.

---

#### appendData

void appendData​(

String

arg)
throws

DOMException

Append the string to the end of the character data of the node. Upon
success,

data

provides access to the concatenation of

data

and the

DOMString

specified.

insertData

```java
void insertData​(int offset,

String
arg)
throws
DOMException
```

Insert a string at the specified 16-bit unit offset.

**Parameters:** offset

- The character offset at which to insert.
**Parameters:** arg

- The

DOMString

to insert.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if the specified

offset

is
negative or greater than the number of 16-bit units in

data

.

NO_MODIFICATION_ALLOWED_ERR: Raised if this node is readonly.

---

#### insertData

void insertData​(int offset,

String

arg)
throws

DOMException

Insert a string at the specified 16-bit unit offset.

deleteData

```java
void deleteData​(int offset,
int count)
throws
DOMException
```

Remove a range of 16-bit units from the node. Upon success,

data

and

length

reflect the change.

**Parameters:** offset

- The offset from which to start removing.
**Parameters:** count

- The number of 16-bit units to delete. If the sum of

offset

and

count

exceeds

length

then all 16-bit units from

offset

to the end of the data are deleted.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if the specified

offset

is
negative or greater than the number of 16-bit units in

data

, or if the specified

count

is
negative.

NO_MODIFICATION_ALLOWED_ERR: Raised if this node is readonly.

---

#### deleteData

void deleteData​(int offset,
int count)
throws

DOMException

Remove a range of 16-bit units from the node. Upon success,

data

and

length

reflect the change.

replaceData

```java
void replaceData​(int offset,
int count,

String
arg)
throws
DOMException
```

Replace the characters starting at the specified 16-bit unit offset
with the specified string.

**Parameters:** offset

- The offset from which to start replacing.
**Parameters:** count

- The number of 16-bit units to replace. If the sum of

offset

and

count

exceeds

length

, then all 16-bit units to the end of the data
are replaced; (i.e., the effect is the same as a

remove

method call with the same range, followed by an

append

method invocation).
**Parameters:** arg

- The

DOMString

with which the range must be
replaced.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if the specified

offset

is
negative or greater than the number of 16-bit units in

data

, or if the specified

count

is
negative.

NO_MODIFICATION_ALLOWED_ERR: Raised if this node is readonly.

---

#### replaceData

void replaceData​(int offset,
int count,

String

arg)
throws

DOMException

Replace the characters starting at the specified 16-bit unit offset
with the specified string.

---

