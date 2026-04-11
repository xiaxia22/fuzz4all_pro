# Interface LSParserFilter

**Source:** `java.xml\org\w3c\dom\ls\LSParserFilter.html`

### Class Description

```java
public interface
LSParserFilter
```

LSParserFilter

s provide applications the ability to examine
nodes as they are being constructed while parsing. As each node is
examined, it may be modified or removed, or the entire parse may be
terminated early.

At the time any of the filter methods are called by the parser, the
owner Document and DOMImplementation objects exist and are accessible.
The document element is never passed to the

LSParserFilter

methods, i.e. it is not possible to filter out the document element.

Document

,

DocumentType

,

Notation

,

Entity

, and

Attr

nodes are never passed to the

acceptNode

method on the filter. The child nodes of an

EntityReference

node are passed to the filter if the parameter
"

entities

"
is set to

false

. Note that, as described by the parameter
"

entities

",
unexpanded entity reference nodes are never discarded and are always
passed to the filter.

All validity checking while parsing a document occurs on the source
document as it appears on the input stream, not on the DOM document as it
is built in memory. With filters, the document in memory may be a subset
of the document on the stream, and its validity may have been affected by
the filtering.

All default attributes must be present on elements when the elements
are passed to the filter methods. All other default content must be
passed to the filter methods.

DOM applications must not raise exceptions in a filter. The effect of
throwing exceptions from a filter is DOM implementation dependent.

See also the

Document Object Model (DOM) Level 3 Load and Save Specification

.

**Since:** 1.5

---

### Field Details

#### static final short FILTER_ACCEPT

Accept the node.

**See Also:**
- Constant Field Values

---

#### static final short FILTER_REJECT

Reject the node and its children.

**See Also:**
- Constant Field Values

---

#### static final short FILTER_SKIP

Skip this single node. The children of this node will still be
considered.

**See Also:**
- Constant Field Values

---

#### static final short FILTER_INTERRUPT

Interrupt the normal processing of the document.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### short startElement​(
Element
elementArg)

The parser will call this method after each

Element

start
tag has been scanned, but before the remainder of the

Element

is processed. The intent is to allow the
element, including any children, to be efficiently skipped. Note that
only element nodes are passed to the

startElement

function.

The element node passed to

startElement

for filtering
will include all of the Element's attributes, but none of the
children nodes. The Element may not yet be in place in the document
being constructed (it may not have a parent node.)

A

startElement

filter function may access or change
the attributes for the Element. Changing Namespace declarations will
have no effect on namespace resolution by the parser.

For efficiency, the Element node passed to the filter may not be
the same one as is actually placed in the tree if the node is
accepted. And the actual node (node object identity) may be reused
during the process of reading in and filtering a document.

**Parameters:**
- elementArg

- The newly encountered element. At the time this
method is called, the element is incomplete - it will have its
attributes, but no children.

**Returns:**
- - FILTER_ACCEPT

if the

Element

should
be included in the DOM document being built.
- FILTER_REJECT

if the

Element

and all of
its children should be rejected.
- FILTER_SKIP

if the

Element

should be skipped. All of its children are
inserted in place of the skipped

Element

node.
- FILTER_INTERRUPT

if the filter wants to stop the
processing of the document. Interrupting the processing of the
document does no longer guarantee that the resulting DOM tree is
XML well-formed. The

Element

is rejected.

Returning
any other values will result in unspecified behavior.

---

#### short acceptNode​(
Node
nodeArg)

This method will be called by the parser at the completion of the
parsing of each node. The node and all of its descendants will exist
and be complete. The parent node will also exist, although it may be
incomplete, i.e. it may have additional children that have not yet
been parsed. Attribute nodes are never passed to this function.

From within this method, the new node may be freely modified -
children may be added or removed, text nodes modified, etc. The state
of the rest of the document outside this node is not defined, and the
affect of any attempt to navigate to, or to modify any other part of
the document is undefined.

For validating parsers, the checks are made on the original
document, before any modification by the filter. No validity checks
are made on any document modifications made by the filter.

If this new node is rejected, the parser might reuse the new node
and any of its descendants.

**Parameters:**
- nodeArg

- The newly constructed element. At the time this method
is called, the element is complete - it has all of its children
(and their children, recursively) and attributes, and is attached
as a child to its parent.

**Returns:**
- - FILTER_ACCEPT

if this

Node

should
be included in the DOM document being built.
- FILTER_REJECT

if the

Node

and all of its
children should be rejected.
- FILTER_SKIP

if the

Node

should be skipped and the

Node

should be replaced by all the children of the

Node

.
- FILTER_INTERRUPT

if the filter wants to stop the
processing of the document. Interrupting the processing of the
document does no longer guarantee that the resulting DOM tree is
XML well-formed. The

Node

is accepted and will be the
last completely parsed node.

---

#### int getWhatToShow()

Tells the

LSParser

what types of nodes to show to the
method

LSParserFilter.acceptNode

. If a node is not shown
to the filter using this attribute, it is automatically included in
the DOM document being built. See

NodeFilter

for
definition of the constants. The constants

SHOW_ATTRIBUTE

,

SHOW_DOCUMENT

,

SHOW_DOCUMENT_TYPE

,

SHOW_NOTATION

,

SHOW_ENTITY

, and

SHOW_DOCUMENT_FRAGMENT

are meaningless here. Those nodes
will never be passed to

LSParserFilter.acceptNode

.

The constants used here are defined in
[

DOM Level 2 Traversal and Range

].

---

### Additional Sections

#### Interface LSParserFilter

```java
public interface
LSParserFilter
```

LSParserFilter

s provide applications the ability to examine
nodes as they are being constructed while parsing. As each node is
examined, it may be modified or removed, or the entire parse may be
terminated early.

At the time any of the filter methods are called by the parser, the
owner Document and DOMImplementation objects exist and are accessible.
The document element is never passed to the

LSParserFilter

methods, i.e. it is not possible to filter out the document element.

Document

,

DocumentType

,

Notation

,

Entity

, and

Attr

nodes are never passed to the

acceptNode

method on the filter. The child nodes of an

EntityReference

node are passed to the filter if the parameter
"

entities

"
is set to

false

. Note that, as described by the parameter
"

entities

",
unexpanded entity reference nodes are never discarded and are always
passed to the filter.

All validity checking while parsing a document occurs on the source
document as it appears on the input stream, not on the DOM document as it
is built in memory. With filters, the document in memory may be a subset
of the document on the stream, and its validity may have been affected by
the filtering.

All default attributes must be present on elements when the elements
are passed to the filter methods. All other default content must be
passed to the filter methods.

DOM applications must not raise exceptions in a filter. The effect of
throwing exceptions from a filter is DOM implementation dependent.

See also the

Document Object Model (DOM) Level 3 Load and Save Specification

.

**Since:** 1.5

public interface

LSParserFilter

LSParserFilter

s provide applications the ability to examine
nodes as they are being constructed while parsing. As each node is
examined, it may be modified or removed, or the entire parse may be
terminated early.

At the time any of the filter methods are called by the parser, the
owner Document and DOMImplementation objects exist and are accessible.
The document element is never passed to the

LSParserFilter

methods, i.e. it is not possible to filter out the document element.

Document

,

DocumentType

,

Notation

,

Entity

, and

Attr

nodes are never passed to the

acceptNode

method on the filter. The child nodes of an

EntityReference

node are passed to the filter if the parameter
"

entities

"
is set to

false

. Note that, as described by the parameter
"

entities

",
unexpanded entity reference nodes are never discarded and are always
passed to the filter.

All validity checking while parsing a document occurs on the source
document as it appears on the input stream, not on the DOM document as it
is built in memory. With filters, the document in memory may be a subset
of the document on the stream, and its validity may have been affected by
the filtering.

All default attributes must be present on elements when the elements
are passed to the filter methods. All other default content must be
passed to the filter methods.

DOM applications must not raise exceptions in a filter. The effect of
throwing exceptions from a filter is DOM implementation dependent.

See also the

Document Object Model (DOM) Level 3 Load and Save Specification

.

At the time any of the filter methods are called by the parser, the
owner Document and DOMImplementation objects exist and are accessible.
The document element is never passed to the

LSParserFilter

methods, i.e. it is not possible to filter out the document element.

Document

,

DocumentType

,

Notation

,

Entity

, and

Attr

nodes are never passed to the

acceptNode

method on the filter. The child nodes of an

EntityReference

node are passed to the filter if the parameter
"

entities

"
is set to

false

. Note that, as described by the parameter
"

entities

",
unexpanded entity reference nodes are never discarded and are always
passed to the filter.

All validity checking while parsing a document occurs on the source
document as it appears on the input stream, not on the DOM document as it
is built in memory. With filters, the document in memory may be a subset
of the document on the stream, and its validity may have been affected by
the filtering.

All default attributes must be present on elements when the elements
are passed to the filter methods. All other default content must be
passed to the filter methods.

DOM applications must not raise exceptions in a filter. The effect of
throwing exceptions from a filter is DOM implementation dependent.

See also the

Document Object Model (DOM) Level 3 Load and Save Specification

.

All validity checking while parsing a document occurs on the source
document as it appears on the input stream, not on the DOM document as it
is built in memory. With filters, the document in memory may be a subset
of the document on the stream, and its validity may have been affected by
the filtering.

All default attributes must be present on elements when the elements
are passed to the filter methods. All other default content must be
passed to the filter methods.

DOM applications must not raise exceptions in a filter. The effect of
throwing exceptions from a filter is DOM implementation dependent.

See also the

Document Object Model (DOM) Level 3 Load and Save Specification

.

All default attributes must be present on elements when the elements
are passed to the filter methods. All other default content must be
passed to the filter methods.

DOM applications must not raise exceptions in a filter. The effect of
throwing exceptions from a filter is DOM implementation dependent.

See also the

Document Object Model (DOM) Level 3 Load and Save Specification

.

DOM applications must not raise exceptions in a filter. The effect of
throwing exceptions from a filter is DOM implementation dependent.

See also the

Document Object Model (DOM) Level 3 Load and Save Specification

.

See also the

Document Object Model (DOM) Level 3 Load and Save Specification

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

FILTER_INTERRUPT

Interrupt the normal processing of the document.

static short

FILTER_REJECT

Reject the node and its children.

static short

FILTER_SKIP

Skip this single node.

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

nodeArg)

This method will be called by the parser at the completion of the
parsing of each node.

int

getWhatToShow

()

Tells the

LSParser

what types of nodes to show to the
method

LSParserFilter.acceptNode

.

short

startElement

​(

Element

elementArg)

The parser will call this method after each

Element

start
tag has been scanned, but before the remainder of the

Element

is processed.

Field Summary

Fields

Modifier and Type

Field

Description

static short

FILTER_ACCEPT

Accept the node.

static short

FILTER_INTERRUPT

Interrupt the normal processing of the document.

static short

FILTER_REJECT

Reject the node and its children.

static short

FILTER_SKIP

Skip this single node.

---

#### Field Summary

Accept the node.

Interrupt the normal processing of the document.

Reject the node and its children.

Skip this single node.

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

nodeArg)

This method will be called by the parser at the completion of the
parsing of each node.

int

getWhatToShow

()

Tells the

LSParser

what types of nodes to show to the
method

LSParserFilter.acceptNode

.

short

startElement

​(

Element

elementArg)

The parser will call this method after each

Element

start
tag has been scanned, but before the remainder of the

Element

is processed.

---

#### Method Summary

This method will be called by the parser at the completion of the
parsing of each node.

Tells the

LSParser

what types of nodes to show to the
method

LSParserFilter.acceptNode

.

The parser will call this method after each

Element

start
tag has been scanned, but before the remainder of the

Element

is processed.

============ FIELD DETAIL ===========

- Field Detail

- FILTER_ACCEPT

```java
static final short FILTER_ACCEPT
```

Accept the node.

**See Also:** Constant Field Values

- FILTER_REJECT

```java
static final short FILTER_REJECT
```

Reject the node and its children.

**See Also:** Constant Field Values

- FILTER_SKIP

```java
static final short FILTER_SKIP
```

Skip this single node. The children of this node will still be
considered.

**See Also:** Constant Field Values

- FILTER_INTERRUPT

```java
static final short FILTER_INTERRUPT
```

Interrupt the normal processing of the document.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- startElement

```java
short startElement​(
Element
elementArg)
```

The parser will call this method after each

Element

start
tag has been scanned, but before the remainder of the

Element

is processed. The intent is to allow the
element, including any children, to be efficiently skipped. Note that
only element nodes are passed to the

startElement

function.

The element node passed to

startElement

for filtering
will include all of the Element's attributes, but none of the
children nodes. The Element may not yet be in place in the document
being constructed (it may not have a parent node.)

A

startElement

filter function may access or change
the attributes for the Element. Changing Namespace declarations will
have no effect on namespace resolution by the parser.

For efficiency, the Element node passed to the filter may not be
the same one as is actually placed in the tree if the node is
accepted. And the actual node (node object identity) may be reused
during the process of reading in and filtering a document.

**Parameters:** elementArg

- The newly encountered element. At the time this
method is called, the element is incomplete - it will have its
attributes, but no children.
**Returns:** - FILTER_ACCEPT

if the

Element

should
be included in the DOM document being built.
- FILTER_REJECT

if the

Element

and all of
its children should be rejected.
- FILTER_SKIP

if the

Element

should be skipped. All of its children are
inserted in place of the skipped

Element

node.
- FILTER_INTERRUPT

if the filter wants to stop the
processing of the document. Interrupting the processing of the
document does no longer guarantee that the resulting DOM tree is
XML well-formed. The

Element

is rejected.

Returning
any other values will result in unspecified behavior.

- acceptNode

```java
short acceptNode​(
Node
nodeArg)
```

This method will be called by the parser at the completion of the
parsing of each node. The node and all of its descendants will exist
and be complete. The parent node will also exist, although it may be
incomplete, i.e. it may have additional children that have not yet
been parsed. Attribute nodes are never passed to this function.

From within this method, the new node may be freely modified -
children may be added or removed, text nodes modified, etc. The state
of the rest of the document outside this node is not defined, and the
affect of any attempt to navigate to, or to modify any other part of
the document is undefined.

For validating parsers, the checks are made on the original
document, before any modification by the filter. No validity checks
are made on any document modifications made by the filter.

If this new node is rejected, the parser might reuse the new node
and any of its descendants.

**Parameters:** nodeArg

- The newly constructed element. At the time this method
is called, the element is complete - it has all of its children
(and their children, recursively) and attributes, and is attached
as a child to its parent.
**Returns:** - FILTER_ACCEPT

if this

Node

should
be included in the DOM document being built.
- FILTER_REJECT

if the

Node

and all of its
children should be rejected.
- FILTER_SKIP

if the

Node

should be skipped and the

Node

should be replaced by all the children of the

Node

.
- FILTER_INTERRUPT

if the filter wants to stop the
processing of the document. Interrupting the processing of the
document does no longer guarantee that the resulting DOM tree is
XML well-formed. The

Node

is accepted and will be the
last completely parsed node.

- getWhatToShow

```java
int getWhatToShow()
```

Tells the

LSParser

what types of nodes to show to the
method

LSParserFilter.acceptNode

. If a node is not shown
to the filter using this attribute, it is automatically included in
the DOM document being built. See

NodeFilter

for
definition of the constants. The constants

SHOW_ATTRIBUTE

,

SHOW_DOCUMENT

,

SHOW_DOCUMENT_TYPE

,

SHOW_NOTATION

,

SHOW_ENTITY

, and

SHOW_DOCUMENT_FRAGMENT

are meaningless here. Those nodes
will never be passed to

LSParserFilter.acceptNode

.

The constants used here are defined in
[

DOM Level 2 Traversal and Range

].

Field Detail

- FILTER_ACCEPT

```java
static final short FILTER_ACCEPT
```

Accept the node.

**See Also:** Constant Field Values

- FILTER_REJECT

```java
static final short FILTER_REJECT
```

Reject the node and its children.

**See Also:** Constant Field Values

- FILTER_SKIP

```java
static final short FILTER_SKIP
```

Skip this single node. The children of this node will still be
considered.

**See Also:** Constant Field Values

- FILTER_INTERRUPT

```java
static final short FILTER_INTERRUPT
```

Interrupt the normal processing of the document.

**See Also:** Constant Field Values

---

#### Field Detail

FILTER_ACCEPT

```java
static final short FILTER_ACCEPT
```

Accept the node.

**See Also:** Constant Field Values

---

#### FILTER_ACCEPT

static final short FILTER_ACCEPT

Accept the node.

FILTER_REJECT

```java
static final short FILTER_REJECT
```

Reject the node and its children.

**See Also:** Constant Field Values

---

#### FILTER_REJECT

static final short FILTER_REJECT

Reject the node and its children.

FILTER_SKIP

```java
static final short FILTER_SKIP
```

Skip this single node. The children of this node will still be
considered.

**See Also:** Constant Field Values

---

#### FILTER_SKIP

static final short FILTER_SKIP

Skip this single node. The children of this node will still be
considered.

FILTER_INTERRUPT

```java
static final short FILTER_INTERRUPT
```

Interrupt the normal processing of the document.

**See Also:** Constant Field Values

---

#### FILTER_INTERRUPT

static final short FILTER_INTERRUPT

Interrupt the normal processing of the document.

Method Detail

- startElement

```java
short startElement​(
Element
elementArg)
```

The parser will call this method after each

Element

start
tag has been scanned, but before the remainder of the

Element

is processed. The intent is to allow the
element, including any children, to be efficiently skipped. Note that
only element nodes are passed to the

startElement

function.

The element node passed to

startElement

for filtering
will include all of the Element's attributes, but none of the
children nodes. The Element may not yet be in place in the document
being constructed (it may not have a parent node.)

A

startElement

filter function may access or change
the attributes for the Element. Changing Namespace declarations will
have no effect on namespace resolution by the parser.

For efficiency, the Element node passed to the filter may not be
the same one as is actually placed in the tree if the node is
accepted. And the actual node (node object identity) may be reused
during the process of reading in and filtering a document.

**Parameters:** elementArg

- The newly encountered element. At the time this
method is called, the element is incomplete - it will have its
attributes, but no children.
**Returns:** - FILTER_ACCEPT

if the

Element

should
be included in the DOM document being built.
- FILTER_REJECT

if the

Element

and all of
its children should be rejected.
- FILTER_SKIP

if the

Element

should be skipped. All of its children are
inserted in place of the skipped

Element

node.
- FILTER_INTERRUPT

if the filter wants to stop the
processing of the document. Interrupting the processing of the
document does no longer guarantee that the resulting DOM tree is
XML well-formed. The

Element

is rejected.

Returning
any other values will result in unspecified behavior.

- acceptNode

```java
short acceptNode​(
Node
nodeArg)
```

This method will be called by the parser at the completion of the
parsing of each node. The node and all of its descendants will exist
and be complete. The parent node will also exist, although it may be
incomplete, i.e. it may have additional children that have not yet
been parsed. Attribute nodes are never passed to this function.

From within this method, the new node may be freely modified -
children may be added or removed, text nodes modified, etc. The state
of the rest of the document outside this node is not defined, and the
affect of any attempt to navigate to, or to modify any other part of
the document is undefined.

For validating parsers, the checks are made on the original
document, before any modification by the filter. No validity checks
are made on any document modifications made by the filter.

If this new node is rejected, the parser might reuse the new node
and any of its descendants.

**Parameters:** nodeArg

- The newly constructed element. At the time this method
is called, the element is complete - it has all of its children
(and their children, recursively) and attributes, and is attached
as a child to its parent.
**Returns:** - FILTER_ACCEPT

if this

Node

should
be included in the DOM document being built.
- FILTER_REJECT

if the

Node

and all of its
children should be rejected.
- FILTER_SKIP

if the

Node

should be skipped and the

Node

should be replaced by all the children of the

Node

.
- FILTER_INTERRUPT

if the filter wants to stop the
processing of the document. Interrupting the processing of the
document does no longer guarantee that the resulting DOM tree is
XML well-formed. The

Node

is accepted and will be the
last completely parsed node.

- getWhatToShow

```java
int getWhatToShow()
```

Tells the

LSParser

what types of nodes to show to the
method

LSParserFilter.acceptNode

. If a node is not shown
to the filter using this attribute, it is automatically included in
the DOM document being built. See

NodeFilter

for
definition of the constants. The constants

SHOW_ATTRIBUTE

,

SHOW_DOCUMENT

,

SHOW_DOCUMENT_TYPE

,

SHOW_NOTATION

,

SHOW_ENTITY

, and

SHOW_DOCUMENT_FRAGMENT

are meaningless here. Those nodes
will never be passed to

LSParserFilter.acceptNode

.

The constants used here are defined in
[

DOM Level 2 Traversal and Range

].

---

#### Method Detail

startElement

```java
short startElement​(
Element
elementArg)
```

The parser will call this method after each

Element

start
tag has been scanned, but before the remainder of the

Element

is processed. The intent is to allow the
element, including any children, to be efficiently skipped. Note that
only element nodes are passed to the

startElement

function.

The element node passed to

startElement

for filtering
will include all of the Element's attributes, but none of the
children nodes. The Element may not yet be in place in the document
being constructed (it may not have a parent node.)

A

startElement

filter function may access or change
the attributes for the Element. Changing Namespace declarations will
have no effect on namespace resolution by the parser.

For efficiency, the Element node passed to the filter may not be
the same one as is actually placed in the tree if the node is
accepted. And the actual node (node object identity) may be reused
during the process of reading in and filtering a document.

**Parameters:** elementArg

- The newly encountered element. At the time this
method is called, the element is incomplete - it will have its
attributes, but no children.
**Returns:** - FILTER_ACCEPT

if the

Element

should
be included in the DOM document being built.
- FILTER_REJECT

if the

Element

and all of
its children should be rejected.
- FILTER_SKIP

if the

Element

should be skipped. All of its children are
inserted in place of the skipped

Element

node.
- FILTER_INTERRUPT

if the filter wants to stop the
processing of the document. Interrupting the processing of the
document does no longer guarantee that the resulting DOM tree is
XML well-formed. The

Element

is rejected.

Returning
any other values will result in unspecified behavior.

---

#### startElement

short startElement​(

Element

elementArg)

The parser will call this method after each

Element

start
tag has been scanned, but before the remainder of the

Element

is processed. The intent is to allow the
element, including any children, to be efficiently skipped. Note that
only element nodes are passed to the

startElement

function.

The element node passed to

startElement

for filtering
will include all of the Element's attributes, but none of the
children nodes. The Element may not yet be in place in the document
being constructed (it may not have a parent node.)

A

startElement

filter function may access or change
the attributes for the Element. Changing Namespace declarations will
have no effect on namespace resolution by the parser.

For efficiency, the Element node passed to the filter may not be
the same one as is actually placed in the tree if the node is
accepted. And the actual node (node object identity) may be reused
during the process of reading in and filtering a document.

FILTER_ACCEPT

if the

Element

should
be included in the DOM document being built.

FILTER_REJECT

if the

Element

and all of
its children should be rejected.

FILTER_SKIP

if the

Element

should be skipped. All of its children are
inserted in place of the skipped

Element

node.

FILTER_INTERRUPT

if the filter wants to stop the
processing of the document. Interrupting the processing of the
document does no longer guarantee that the resulting DOM tree is
XML well-formed. The

Element

is rejected.

acceptNode

```java
short acceptNode​(
Node
nodeArg)
```

This method will be called by the parser at the completion of the
parsing of each node. The node and all of its descendants will exist
and be complete. The parent node will also exist, although it may be
incomplete, i.e. it may have additional children that have not yet
been parsed. Attribute nodes are never passed to this function.

From within this method, the new node may be freely modified -
children may be added or removed, text nodes modified, etc. The state
of the rest of the document outside this node is not defined, and the
affect of any attempt to navigate to, or to modify any other part of
the document is undefined.

For validating parsers, the checks are made on the original
document, before any modification by the filter. No validity checks
are made on any document modifications made by the filter.

If this new node is rejected, the parser might reuse the new node
and any of its descendants.

**Parameters:** nodeArg

- The newly constructed element. At the time this method
is called, the element is complete - it has all of its children
(and their children, recursively) and attributes, and is attached
as a child to its parent.
**Returns:** - FILTER_ACCEPT

if this

Node

should
be included in the DOM document being built.
- FILTER_REJECT

if the

Node

and all of its
children should be rejected.
- FILTER_SKIP

if the

Node

should be skipped and the

Node

should be replaced by all the children of the

Node

.
- FILTER_INTERRUPT

if the filter wants to stop the
processing of the document. Interrupting the processing of the
document does no longer guarantee that the resulting DOM tree is
XML well-formed. The

Node

is accepted and will be the
last completely parsed node.

---

#### acceptNode

short acceptNode​(

Node

nodeArg)

This method will be called by the parser at the completion of the
parsing of each node. The node and all of its descendants will exist
and be complete. The parent node will also exist, although it may be
incomplete, i.e. it may have additional children that have not yet
been parsed. Attribute nodes are never passed to this function.

From within this method, the new node may be freely modified -
children may be added or removed, text nodes modified, etc. The state
of the rest of the document outside this node is not defined, and the
affect of any attempt to navigate to, or to modify any other part of
the document is undefined.

For validating parsers, the checks are made on the original
document, before any modification by the filter. No validity checks
are made on any document modifications made by the filter.

If this new node is rejected, the parser might reuse the new node
and any of its descendants.

FILTER_ACCEPT

if this

Node

should
be included in the DOM document being built.

FILTER_REJECT

if the

Node

and all of its
children should be rejected.

FILTER_SKIP

if the

Node

should be skipped and the

Node

should be replaced by all the children of the

Node

.

FILTER_INTERRUPT

if the filter wants to stop the
processing of the document. Interrupting the processing of the
document does no longer guarantee that the resulting DOM tree is
XML well-formed. The

Node

is accepted and will be the
last completely parsed node.

getWhatToShow

```java
int getWhatToShow()
```

Tells the

LSParser

what types of nodes to show to the
method

LSParserFilter.acceptNode

. If a node is not shown
to the filter using this attribute, it is automatically included in
the DOM document being built. See

NodeFilter

for
definition of the constants. The constants

SHOW_ATTRIBUTE

,

SHOW_DOCUMENT

,

SHOW_DOCUMENT_TYPE

,

SHOW_NOTATION

,

SHOW_ENTITY

, and

SHOW_DOCUMENT_FRAGMENT

are meaningless here. Those nodes
will never be passed to

LSParserFilter.acceptNode

.

The constants used here are defined in
[

DOM Level 2 Traversal and Range

].

---

#### getWhatToShow

int getWhatToShow()

Tells the

LSParser

what types of nodes to show to the
method

LSParserFilter.acceptNode

. If a node is not shown
to the filter using this attribute, it is automatically included in
the DOM document being built. See

NodeFilter

for
definition of the constants. The constants

SHOW_ATTRIBUTE

,

SHOW_DOCUMENT

,

SHOW_DOCUMENT_TYPE

,

SHOW_NOTATION

,

SHOW_ENTITY

, and

SHOW_DOCUMENT_FRAGMENT

are meaningless here. Those nodes
will never be passed to

LSParserFilter.acceptNode

.

The constants used here are defined in
[

DOM Level 2 Traversal and Range

].

---

