# Class DOMResult

**Source:** `java.xml\javax\xml\transform\dom\DOMResult.html`

### Class Description

```java
public class
DOMResult

extends
Object

implements
Result
```

Acts as a holder for a transformation result tree
in the form of a Document Object Model (DOM) tree.

If no output DOM source is set, the transformation will create
a Document node as the holder for the result of the transformation,
which may be retrieved with

getNode()

.

**All Implemented Interfaces:** Result

---

### Field Details

#### public static final
String
FEATURE

If

TransformerFactory.getFeature(java.lang.String)

returns

true

when passed this value as an argument,
the

Transformer

supports

Result

output of this type.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public DOMResult()

Zero-argument default constructor.

node

,

siblingNode

and

systemId

will be set to

null

.

---

#### public DOMResult​(
Node
node)

Use a DOM node to create a new output target.

In practice, the node should be
a

Document

node,
a

DocumentFragment

node, or
a

Element

node.
In other words, a node that accepts children.

siblingNode

and

systemId

will be set to

null

.

**Parameters:**
- node

- The DOM node that will contain the result tree.

---

#### public DOMResult​(
Node
node,

String
systemId)

Use a DOM node to create a new output target with the specified System ID.

In practice, the node should be
a

Document

node,
a

DocumentFragment

node, or
a

Element

node.
In other words, a node that accepts children.

siblingNode

will be set to

null

.

**Parameters:**
- node

- The DOM node that will contain the result tree.
- systemId

- The system identifier which may be used in association with this node.

---

#### public DOMResult​(
Node
node,

Node
nextSibling)

Use a DOM node to create a new output target specifying
the child node where the result nodes should be inserted before.

In practice,

node

and

nextSibling

should be
a

Document

node,
a

DocumentFragment

node, or
a

Element

node.
In other words, a node that accepts children.

Use

nextSibling

to specify the child node
where the result nodes should be inserted before.
If

nextSibling

is not a sibling of

node

,
then an

IllegalArgumentException

is thrown.
If

node

is

null

and

nextSibling

is not

null

,
then an

IllegalArgumentException

is thrown.
If

nextSibling

is

null

,
then the behavior is the same as calling

DOMResult(Node node)

,
i.e. append the result nodes as the last child of the specified

node

.

systemId

will be set to

null

.

**Parameters:**
- node

- The DOM node that will contain the result tree.
- nextSibling

- The child node where the result nodes should be inserted before.

**Throws:**
- IllegalArgumentException

- If

nextSibling

is not a sibling of

node

or

node

is

null

and

nextSibling

is not

null

.

**Since:**
- 1.5

---

#### public DOMResult​(
Node
node,

Node
nextSibling,

String
systemId)

Use a DOM node to create a new output target specifying the child
node where the result nodes should be inserted before and
the specified System ID.

In practice,

node

and

nextSibling

should be
a

Document

node,
a

DocumentFragment

node, or a

Element

node.
In other words, a node that accepts children.

Use

nextSibling

to specify the child node
where the result nodes should be inserted before.
If

nextSibling

is not a sibling of

node

,
then an

IllegalArgumentException

is thrown.
If

node

is

null

and

nextSibling

is not

null

,
then an

IllegalArgumentException

is thrown.
If

nextSibling

is

null

,
then the behavior is the same as calling

DOMResult(Node node, String systemId)

,
i.e. append the result nodes as the last child of the specified
node and use the specified System ID.

**Parameters:**
- node

- The DOM node that will contain the result tree.
- nextSibling

- The child node where the result nodes should be inserted before.
- systemId

- The system identifier which may be used in association with this node.

**Throws:**
- IllegalArgumentException

- If

nextSibling

is not a
sibling of

node

or

node

is

null

and

nextSibling

is not

null

.

**Since:**
- 1.5

---

### Method Details

#### public void setNode​(
Node
node)

Set the node that will contain the result DOM tree.

In practice, the node should be
a

Document

node,
a

DocumentFragment

node, or
a

Element

node.
In other words, a node that accepts children.

An

IllegalStateException

is thrown if

nextSibling

is not

null

and

node

is not a parent of

nextSibling

.
An

IllegalStateException

is thrown if

node

is

null

and

nextSibling

is not

null

.

**Parameters:**
- node

- The node to which the transformation will be appended.

**Throws:**
- IllegalStateException

- If

nextSibling

is not

null

and

nextSibling

is not a child of

node

or

node

is

null

and

nextSibling

is not

null

.

---

#### public
Node
getNode()

Get the node that will contain the result DOM tree.

If no node was set via

DOMResult(Node node)

,

DOMResult(Node node, String systeId)

,

DOMResult(Node node, Node nextSibling)

,

DOMResult(Node node, Node nextSibling, String systemId)

or

setNode(Node node)

,
then the node will be set by the transformation, and may be obtained from this method once the transformation is complete.
Calling this method before the transformation will return

null

.

**Returns:**
- The node to which the transformation will be appended.

---

#### public void setNextSibling​(
Node
nextSibling)

Set the child node before which the result nodes will be inserted.

Use

nextSibling

to specify the child node
before which the result nodes should be inserted.
If

nextSibling

is not a descendant of

node

,
then an

IllegalArgumentException

is thrown.
If

node

is

null

and

nextSibling

is not

null

,
then an

IllegalStateException

is thrown.
If

nextSibling

is

null

,
then the behavior is the same as calling

DOMResult(Node node)

,
i.e. append the result nodes as the last child of the specified

node

.

**Parameters:**
- nextSibling

- The child node before which the result nodes will be inserted.

**Throws:**
- IllegalArgumentException

- If

nextSibling

is not a
descendant of

node

.
- IllegalStateException

- If

node

is

null

and

nextSibling

is not

null

.

**Since:**
- 1.5

---

#### public
Node
getNextSibling()

Get the child node before which the result nodes will be inserted.

If no node was set via

DOMResult(Node node, Node nextSibling)

,

DOMResult(Node node, Node nextSibling, String systemId)

or

setNextSibling(Node nextSibling)

,
then

null

will be returned.

**Returns:**
- The child node before which the result nodes will be inserted.

**Since:**
- 1.5

---

#### public void setSystemId​(
String
systemId)

Set the systemId that may be used in association with the node.

**Specified by:**
- setSystemId

in interface

Result

**Parameters:**
- systemId

- The system identifier as a URI string.

---

#### public
String
getSystemId()

Get the System Identifier.

If no System ID was set via

DOMResult(Node node, String systemId)

,

DOMResult(Node node, Node nextSibling, String systemId)

or

setSystemId(String systemId)

,
then

null

will be returned.

**Specified by:**
- getSystemId

in interface

Result

**Returns:**
- The system identifier.

---

### Additional Sections

#### Class DOMResult

java.lang.Object

- javax.xml.transform.dom.DOMResult

javax.xml.transform.dom.DOMResult

**All Implemented Interfaces:** Result

```java
public class
DOMResult

extends
Object

implements
Result
```

Acts as a holder for a transformation result tree
in the form of a Document Object Model (DOM) tree.

If no output DOM source is set, the transformation will create
a Document node as the holder for the result of the transformation,
which may be retrieved with

getNode()

.

**Since:** 1.4

public class

DOMResult

extends

Object

implements

Result

Acts as a holder for a transformation result tree
in the form of a Document Object Model (DOM) tree.

If no output DOM source is set, the transformation will create
a Document node as the holder for the result of the transformation,
which may be retrieved with

getNode()

.

If no output DOM source is set, the transformation will create
a Document node as the holder for the result of the transformation,
which may be retrieved with

getNode()

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

FEATURE

If

TransformerFactory.getFeature(java.lang.String)

returns

true

when passed this value as an argument,
the

Transformer

supports

Result

output of this type.

- Fields declared in interface javax.xml.transform.

Result

PI_DISABLE_OUTPUT_ESCAPING

,

PI_ENABLE_OUTPUT_ESCAPING

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DOMResult

()

Zero-argument default constructor.

DOMResult

​(

Node

node)

Use a DOM node to create a new output target.

DOMResult

​(

Node

node,

String

systemId)

Use a DOM node to create a new output target with the specified System ID.

DOMResult

​(

Node

node,

Node

nextSibling)

Use a DOM node to create a new output target specifying
the child node where the result nodes should be inserted before.

DOMResult

​(

Node

node,

Node

nextSibling,

String

systemId)

Use a DOM node to create a new output target specifying the child
node where the result nodes should be inserted before and
the specified System ID.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Node

getNextSibling

()

Get the child node before which the result nodes will be inserted.

Node

getNode

()

Get the node that will contain the result DOM tree.

String

getSystemId

()

Get the System Identifier.

void

setNextSibling

​(

Node

nextSibling)

Set the child node before which the result nodes will be inserted.

void

setNode

​(

Node

node)

Set the node that will contain the result DOM tree.

void

setSystemId

​(

String

systemId)

Set the systemId that may be used in association with the node.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Field Summary

Fields

Modifier and Type

Field

Description

static

String

FEATURE

If

TransformerFactory.getFeature(java.lang.String)

returns

true

when passed this value as an argument,
the

Transformer

supports

Result

output of this type.

- Fields declared in interface javax.xml.transform.

Result

PI_DISABLE_OUTPUT_ESCAPING

,

PI_ENABLE_OUTPUT_ESCAPING

---

#### Field Summary

If

TransformerFactory.getFeature(java.lang.String)

returns

true

when passed this value as an argument,
the

Transformer

supports

Result

output of this type.

Fields declared in interface javax.xml.transform.

Result

PI_DISABLE_OUTPUT_ESCAPING

,

PI_ENABLE_OUTPUT_ESCAPING

---

#### Fields declared in interface javax.xml.transform. Result

Constructor Summary

Constructors

Constructor

Description

DOMResult

()

Zero-argument default constructor.

DOMResult

​(

Node

node)

Use a DOM node to create a new output target.

DOMResult

​(

Node

node,

String

systemId)

Use a DOM node to create a new output target with the specified System ID.

DOMResult

​(

Node

node,

Node

nextSibling)

Use a DOM node to create a new output target specifying
the child node where the result nodes should be inserted before.

DOMResult

​(

Node

node,

Node

nextSibling,

String

systemId)

Use a DOM node to create a new output target specifying the child
node where the result nodes should be inserted before and
the specified System ID.

---

#### Constructor Summary

Zero-argument default constructor.

Use a DOM node to create a new output target.

Use a DOM node to create a new output target with the specified System ID.

Use a DOM node to create a new output target specifying
the child node where the result nodes should be inserted before.

Use a DOM node to create a new output target specifying the child
node where the result nodes should be inserted before and
the specified System ID.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Node

getNextSibling

()

Get the child node before which the result nodes will be inserted.

Node

getNode

()

Get the node that will contain the result DOM tree.

String

getSystemId

()

Get the System Identifier.

void

setNextSibling

​(

Node

nextSibling)

Set the child node before which the result nodes will be inserted.

void

setNode

​(

Node

node)

Set the node that will contain the result DOM tree.

void

setSystemId

​(

String

systemId)

Set the systemId that may be used in association with the node.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Get the child node before which the result nodes will be inserted.

Get the node that will contain the result DOM tree.

Get the System Identifier.

Set the child node before which the result nodes will be inserted.

Set the node that will contain the result DOM tree.

Set the systemId that may be used in association with the node.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- FEATURE

```java
public static final
String
FEATURE
```

If

TransformerFactory.getFeature(java.lang.String)

returns

true

when passed this value as an argument,
the

Transformer

supports

Result

output of this type.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DOMResult

```java
public DOMResult()
```

Zero-argument default constructor.

node

,

siblingNode

and

systemId

will be set to

null

.

- DOMResult

```java
public DOMResult​(
Node
node)
```

Use a DOM node to create a new output target.

In practice, the node should be
a

Document

node,
a

DocumentFragment

node, or
a

Element

node.
In other words, a node that accepts children.

siblingNode

and

systemId

will be set to

null

.

**Parameters:** node

- The DOM node that will contain the result tree.

- DOMResult

```java
public DOMResult​(
Node
node,

String
systemId)
```

Use a DOM node to create a new output target with the specified System ID.

In practice, the node should be
a

Document

node,
a

DocumentFragment

node, or
a

Element

node.
In other words, a node that accepts children.

siblingNode

will be set to

null

.

**Parameters:** node

- The DOM node that will contain the result tree.
**Parameters:** systemId

- The system identifier which may be used in association with this node.

- DOMResult

```java
public DOMResult​(
Node
node,

Node
nextSibling)
```

Use a DOM node to create a new output target specifying
the child node where the result nodes should be inserted before.

In practice,

node

and

nextSibling

should be
a

Document

node,
a

DocumentFragment

node, or
a

Element

node.
In other words, a node that accepts children.

Use

nextSibling

to specify the child node
where the result nodes should be inserted before.
If

nextSibling

is not a sibling of

node

,
then an

IllegalArgumentException

is thrown.
If

node

is

null

and

nextSibling

is not

null

,
then an

IllegalArgumentException

is thrown.
If

nextSibling

is

null

,
then the behavior is the same as calling

DOMResult(Node node)

,
i.e. append the result nodes as the last child of the specified

node

.

systemId

will be set to

null

.

**Parameters:** node

- The DOM node that will contain the result tree.
**Parameters:** nextSibling

- The child node where the result nodes should be inserted before.
**Throws:** IllegalArgumentException

- If

nextSibling

is not a sibling of

node

or

node

is

null

and

nextSibling

is not

null

.
**Since:** 1.5

- DOMResult

```java
public DOMResult​(
Node
node,

Node
nextSibling,

String
systemId)
```

Use a DOM node to create a new output target specifying the child
node where the result nodes should be inserted before and
the specified System ID.

In practice,

node

and

nextSibling

should be
a

Document

node,
a

DocumentFragment

node, or a

Element

node.
In other words, a node that accepts children.

Use

nextSibling

to specify the child node
where the result nodes should be inserted before.
If

nextSibling

is not a sibling of

node

,
then an

IllegalArgumentException

is thrown.
If

node

is

null

and

nextSibling

is not

null

,
then an

IllegalArgumentException

is thrown.
If

nextSibling

is

null

,
then the behavior is the same as calling

DOMResult(Node node, String systemId)

,
i.e. append the result nodes as the last child of the specified
node and use the specified System ID.

**Parameters:** node

- The DOM node that will contain the result tree.
**Parameters:** nextSibling

- The child node where the result nodes should be inserted before.
**Parameters:** systemId

- The system identifier which may be used in association with this node.
**Throws:** IllegalArgumentException

- If

nextSibling

is not a
sibling of

node

or

node

is

null

and

nextSibling

is not

null

.
**Since:** 1.5

============ METHOD DETAIL ==========

- Method Detail

- setNode

```java
public void setNode​(
Node
node)
```

Set the node that will contain the result DOM tree.

In practice, the node should be
a

Document

node,
a

DocumentFragment

node, or
a

Element

node.
In other words, a node that accepts children.

An

IllegalStateException

is thrown if

nextSibling

is not

null

and

node

is not a parent of

nextSibling

.
An

IllegalStateException

is thrown if

node

is

null

and

nextSibling

is not

null

.

**Parameters:** node

- The node to which the transformation will be appended.
**Throws:** IllegalStateException

- If

nextSibling

is not

null

and

nextSibling

is not a child of

node

or

node

is

null

and

nextSibling

is not

null

.

- getNode

```java
public
Node
getNode()
```

Get the node that will contain the result DOM tree.

If no node was set via

DOMResult(Node node)

,

DOMResult(Node node, String systeId)

,

DOMResult(Node node, Node nextSibling)

,

DOMResult(Node node, Node nextSibling, String systemId)

or

setNode(Node node)

,
then the node will be set by the transformation, and may be obtained from this method once the transformation is complete.
Calling this method before the transformation will return

null

.

**Returns:** The node to which the transformation will be appended.

- setNextSibling

```java
public void setNextSibling​(
Node
nextSibling)
```

Set the child node before which the result nodes will be inserted.

Use

nextSibling

to specify the child node
before which the result nodes should be inserted.
If

nextSibling

is not a descendant of

node

,
then an

IllegalArgumentException

is thrown.
If

node

is

null

and

nextSibling

is not

null

,
then an

IllegalStateException

is thrown.
If

nextSibling

is

null

,
then the behavior is the same as calling

DOMResult(Node node)

,
i.e. append the result nodes as the last child of the specified

node

.

**Parameters:** nextSibling

- The child node before which the result nodes will be inserted.
**Throws:** IllegalArgumentException

- If

nextSibling

is not a
descendant of

node

.
**Throws:** IllegalStateException

- If

node

is

null

and

nextSibling

is not

null

.
**Since:** 1.5

- getNextSibling

```java
public
Node
getNextSibling()
```

Get the child node before which the result nodes will be inserted.

If no node was set via

DOMResult(Node node, Node nextSibling)

,

DOMResult(Node node, Node nextSibling, String systemId)

or

setNextSibling(Node nextSibling)

,
then

null

will be returned.

**Returns:** The child node before which the result nodes will be inserted.
**Since:** 1.5

- setSystemId

```java
public void setSystemId​(
String
systemId)
```

Set the systemId that may be used in association with the node.

**Specified by:** setSystemId

in interface

Result
**Parameters:** systemId

- The system identifier as a URI string.

- getSystemId

```java
public
String
getSystemId()
```

Get the System Identifier.

If no System ID was set via

DOMResult(Node node, String systemId)

,

DOMResult(Node node, Node nextSibling, String systemId)

or

setSystemId(String systemId)

,
then

null

will be returned.

**Specified by:** getSystemId

in interface

Result
**Returns:** The system identifier.

Field Detail

- FEATURE

```java
public static final
String
FEATURE
```

If

TransformerFactory.getFeature(java.lang.String)

returns

true

when passed this value as an argument,
the

Transformer

supports

Result

output of this type.

**See Also:** Constant Field Values

---

#### Field Detail

FEATURE

```java
public static final
String
FEATURE
```

If

TransformerFactory.getFeature(java.lang.String)

returns

true

when passed this value as an argument,
the

Transformer

supports

Result

output of this type.

**See Also:** Constant Field Values

---

#### FEATURE

public static final

String

FEATURE

If

TransformerFactory.getFeature(java.lang.String)

returns

true

when passed this value as an argument,
the

Transformer

supports

Result

output of this type.

Constructor Detail

- DOMResult

```java
public DOMResult()
```

Zero-argument default constructor.

node

,

siblingNode

and

systemId

will be set to

null

.

- DOMResult

```java
public DOMResult​(
Node
node)
```

Use a DOM node to create a new output target.

In practice, the node should be
a

Document

node,
a

DocumentFragment

node, or
a

Element

node.
In other words, a node that accepts children.

siblingNode

and

systemId

will be set to

null

.

**Parameters:** node

- The DOM node that will contain the result tree.

- DOMResult

```java
public DOMResult​(
Node
node,

String
systemId)
```

Use a DOM node to create a new output target with the specified System ID.

In practice, the node should be
a

Document

node,
a

DocumentFragment

node, or
a

Element

node.
In other words, a node that accepts children.

siblingNode

will be set to

null

.

**Parameters:** node

- The DOM node that will contain the result tree.
**Parameters:** systemId

- The system identifier which may be used in association with this node.

- DOMResult

```java
public DOMResult​(
Node
node,

Node
nextSibling)
```

Use a DOM node to create a new output target specifying
the child node where the result nodes should be inserted before.

In practice,

node

and

nextSibling

should be
a

Document

node,
a

DocumentFragment

node, or
a

Element

node.
In other words, a node that accepts children.

Use

nextSibling

to specify the child node
where the result nodes should be inserted before.
If

nextSibling

is not a sibling of

node

,
then an

IllegalArgumentException

is thrown.
If

node

is

null

and

nextSibling

is not

null

,
then an

IllegalArgumentException

is thrown.
If

nextSibling

is

null

,
then the behavior is the same as calling

DOMResult(Node node)

,
i.e. append the result nodes as the last child of the specified

node

.

systemId

will be set to

null

.

**Parameters:** node

- The DOM node that will contain the result tree.
**Parameters:** nextSibling

- The child node where the result nodes should be inserted before.
**Throws:** IllegalArgumentException

- If

nextSibling

is not a sibling of

node

or

node

is

null

and

nextSibling

is not

null

.
**Since:** 1.5

- DOMResult

```java
public DOMResult​(
Node
node,

Node
nextSibling,

String
systemId)
```

Use a DOM node to create a new output target specifying the child
node where the result nodes should be inserted before and
the specified System ID.

In practice,

node

and

nextSibling

should be
a

Document

node,
a

DocumentFragment

node, or a

Element

node.
In other words, a node that accepts children.

Use

nextSibling

to specify the child node
where the result nodes should be inserted before.
If

nextSibling

is not a sibling of

node

,
then an

IllegalArgumentException

is thrown.
If

node

is

null

and

nextSibling

is not

null

,
then an

IllegalArgumentException

is thrown.
If

nextSibling

is

null

,
then the behavior is the same as calling

DOMResult(Node node, String systemId)

,
i.e. append the result nodes as the last child of the specified
node and use the specified System ID.

**Parameters:** node

- The DOM node that will contain the result tree.
**Parameters:** nextSibling

- The child node where the result nodes should be inserted before.
**Parameters:** systemId

- The system identifier which may be used in association with this node.
**Throws:** IllegalArgumentException

- If

nextSibling

is not a
sibling of

node

or

node

is

null

and

nextSibling

is not

null

.
**Since:** 1.5

---

#### Constructor Detail

DOMResult

```java
public DOMResult()
```

Zero-argument default constructor.

node

,

siblingNode

and

systemId

will be set to

null

.

---

#### DOMResult

public DOMResult()

Zero-argument default constructor.

node

,

siblingNode

and

systemId

will be set to

null

.

node

,

siblingNode

and

systemId

will be set to

null

.

DOMResult

```java
public DOMResult​(
Node
node)
```

Use a DOM node to create a new output target.

In practice, the node should be
a

Document

node,
a

DocumentFragment

node, or
a

Element

node.
In other words, a node that accepts children.

siblingNode

and

systemId

will be set to

null

.

**Parameters:** node

- The DOM node that will contain the result tree.

---

#### DOMResult

public DOMResult​(

Node

node)

Use a DOM node to create a new output target.

In practice, the node should be
a

Document

node,
a

DocumentFragment

node, or
a

Element

node.
In other words, a node that accepts children.

siblingNode

and

systemId

will be set to

null

.

In practice, the node should be
a

Document

node,
a

DocumentFragment

node, or
a

Element

node.
In other words, a node that accepts children.

siblingNode

and

systemId

will be set to

null

.

siblingNode

and

systemId

will be set to

null

.

DOMResult

```java
public DOMResult​(
Node
node,

String
systemId)
```

Use a DOM node to create a new output target with the specified System ID.

In practice, the node should be
a

Document

node,
a

DocumentFragment

node, or
a

Element

node.
In other words, a node that accepts children.

siblingNode

will be set to

null

.

**Parameters:** node

- The DOM node that will contain the result tree.
**Parameters:** systemId

- The system identifier which may be used in association with this node.

---

#### DOMResult

public DOMResult​(

Node

node,

String

systemId)

Use a DOM node to create a new output target with the specified System ID.

In practice, the node should be
a

Document

node,
a

DocumentFragment

node, or
a

Element

node.
In other words, a node that accepts children.

siblingNode

will be set to

null

.

In practice, the node should be
a

Document

node,
a

DocumentFragment

node, or
a

Element

node.
In other words, a node that accepts children.

siblingNode

will be set to

null

.

siblingNode

will be set to

null

.

DOMResult

```java
public DOMResult​(
Node
node,

Node
nextSibling)
```

Use a DOM node to create a new output target specifying
the child node where the result nodes should be inserted before.

In practice,

node

and

nextSibling

should be
a

Document

node,
a

DocumentFragment

node, or
a

Element

node.
In other words, a node that accepts children.

Use

nextSibling

to specify the child node
where the result nodes should be inserted before.
If

nextSibling

is not a sibling of

node

,
then an

IllegalArgumentException

is thrown.
If

node

is

null

and

nextSibling

is not

null

,
then an

IllegalArgumentException

is thrown.
If

nextSibling

is

null

,
then the behavior is the same as calling

DOMResult(Node node)

,
i.e. append the result nodes as the last child of the specified

node

.

systemId

will be set to

null

.

**Parameters:** node

- The DOM node that will contain the result tree.
**Parameters:** nextSibling

- The child node where the result nodes should be inserted before.
**Throws:** IllegalArgumentException

- If

nextSibling

is not a sibling of

node

or

node

is

null

and

nextSibling

is not

null

.
**Since:** 1.5

---

#### DOMResult

public DOMResult​(

Node

node,

Node

nextSibling)

Use a DOM node to create a new output target specifying
the child node where the result nodes should be inserted before.

In practice,

node

and

nextSibling

should be
a

Document

node,
a

DocumentFragment

node, or
a

Element

node.
In other words, a node that accepts children.

Use

nextSibling

to specify the child node
where the result nodes should be inserted before.
If

nextSibling

is not a sibling of

node

,
then an

IllegalArgumentException

is thrown.
If

node

is

null

and

nextSibling

is not

null

,
then an

IllegalArgumentException

is thrown.
If

nextSibling

is

null

,
then the behavior is the same as calling

DOMResult(Node node)

,
i.e. append the result nodes as the last child of the specified

node

.

systemId

will be set to

null

.

In practice,

node

and

nextSibling

should be
a

Document

node,
a

DocumentFragment

node, or
a

Element

node.
In other words, a node that accepts children.

Use

nextSibling

to specify the child node
where the result nodes should be inserted before.
If

nextSibling

is not a sibling of

node

,
then an

IllegalArgumentException

is thrown.
If

node

is

null

and

nextSibling

is not

null

,
then an

IllegalArgumentException

is thrown.
If

nextSibling

is

null

,
then the behavior is the same as calling

DOMResult(Node node)

,
i.e. append the result nodes as the last child of the specified

node

.

systemId

will be set to

null

.

Use

nextSibling

to specify the child node
where the result nodes should be inserted before.
If

nextSibling

is not a sibling of

node

,
then an

IllegalArgumentException

is thrown.
If

node

is

null

and

nextSibling

is not

null

,
then an

IllegalArgumentException

is thrown.
If

nextSibling

is

null

,
then the behavior is the same as calling

DOMResult(Node node)

,
i.e. append the result nodes as the last child of the specified

node

.

systemId

will be set to

null

.

systemId

will be set to

null

.

DOMResult

```java
public DOMResult​(
Node
node,

Node
nextSibling,

String
systemId)
```

Use a DOM node to create a new output target specifying the child
node where the result nodes should be inserted before and
the specified System ID.

In practice,

node

and

nextSibling

should be
a

Document

node,
a

DocumentFragment

node, or a

Element

node.
In other words, a node that accepts children.

Use

nextSibling

to specify the child node
where the result nodes should be inserted before.
If

nextSibling

is not a sibling of

node

,
then an

IllegalArgumentException

is thrown.
If

node

is

null

and

nextSibling

is not

null

,
then an

IllegalArgumentException

is thrown.
If

nextSibling

is

null

,
then the behavior is the same as calling

DOMResult(Node node, String systemId)

,
i.e. append the result nodes as the last child of the specified
node and use the specified System ID.

**Parameters:** node

- The DOM node that will contain the result tree.
**Parameters:** nextSibling

- The child node where the result nodes should be inserted before.
**Parameters:** systemId

- The system identifier which may be used in association with this node.
**Throws:** IllegalArgumentException

- If

nextSibling

is not a
sibling of

node

or

node

is

null

and

nextSibling

is not

null

.
**Since:** 1.5

---

#### DOMResult

public DOMResult​(

Node

node,

Node

nextSibling,

String

systemId)

Use a DOM node to create a new output target specifying the child
node where the result nodes should be inserted before and
the specified System ID.

In practice,

node

and

nextSibling

should be
a

Document

node,
a

DocumentFragment

node, or a

Element

node.
In other words, a node that accepts children.

Use

nextSibling

to specify the child node
where the result nodes should be inserted before.
If

nextSibling

is not a sibling of

node

,
then an

IllegalArgumentException

is thrown.
If

node

is

null

and

nextSibling

is not

null

,
then an

IllegalArgumentException

is thrown.
If

nextSibling

is

null

,
then the behavior is the same as calling

DOMResult(Node node, String systemId)

,
i.e. append the result nodes as the last child of the specified
node and use the specified System ID.

In practice,

node

and

nextSibling

should be
a

Document

node,
a

DocumentFragment

node, or a

Element

node.
In other words, a node that accepts children.

Use

nextSibling

to specify the child node
where the result nodes should be inserted before.
If

nextSibling

is not a sibling of

node

,
then an

IllegalArgumentException

is thrown.
If

node

is

null

and

nextSibling

is not

null

,
then an

IllegalArgumentException

is thrown.
If

nextSibling

is

null

,
then the behavior is the same as calling

DOMResult(Node node, String systemId)

,
i.e. append the result nodes as the last child of the specified
node and use the specified System ID.

Use

nextSibling

to specify the child node
where the result nodes should be inserted before.
If

nextSibling

is not a sibling of

node

,
then an

IllegalArgumentException

is thrown.
If

node

is

null

and

nextSibling

is not

null

,
then an

IllegalArgumentException

is thrown.
If

nextSibling

is

null

,
then the behavior is the same as calling

DOMResult(Node node, String systemId)

,
i.e. append the result nodes as the last child of the specified
node and use the specified System ID.

Method Detail

- setNode

```java
public void setNode​(
Node
node)
```

Set the node that will contain the result DOM tree.

In practice, the node should be
a

Document

node,
a

DocumentFragment

node, or
a

Element

node.
In other words, a node that accepts children.

An

IllegalStateException

is thrown if

nextSibling

is not

null

and

node

is not a parent of

nextSibling

.
An

IllegalStateException

is thrown if

node

is

null

and

nextSibling

is not

null

.

**Parameters:** node

- The node to which the transformation will be appended.
**Throws:** IllegalStateException

- If

nextSibling

is not

null

and

nextSibling

is not a child of

node

or

node

is

null

and

nextSibling

is not

null

.

- getNode

```java
public
Node
getNode()
```

Get the node that will contain the result DOM tree.

If no node was set via

DOMResult(Node node)

,

DOMResult(Node node, String systeId)

,

DOMResult(Node node, Node nextSibling)

,

DOMResult(Node node, Node nextSibling, String systemId)

or

setNode(Node node)

,
then the node will be set by the transformation, and may be obtained from this method once the transformation is complete.
Calling this method before the transformation will return

null

.

**Returns:** The node to which the transformation will be appended.

- setNextSibling

```java
public void setNextSibling​(
Node
nextSibling)
```

Set the child node before which the result nodes will be inserted.

Use

nextSibling

to specify the child node
before which the result nodes should be inserted.
If

nextSibling

is not a descendant of

node

,
then an

IllegalArgumentException

is thrown.
If

node

is

null

and

nextSibling

is not

null

,
then an

IllegalStateException

is thrown.
If

nextSibling

is

null

,
then the behavior is the same as calling

DOMResult(Node node)

,
i.e. append the result nodes as the last child of the specified

node

.

**Parameters:** nextSibling

- The child node before which the result nodes will be inserted.
**Throws:** IllegalArgumentException

- If

nextSibling

is not a
descendant of

node

.
**Throws:** IllegalStateException

- If

node

is

null

and

nextSibling

is not

null

.
**Since:** 1.5

- getNextSibling

```java
public
Node
getNextSibling()
```

Get the child node before which the result nodes will be inserted.

If no node was set via

DOMResult(Node node, Node nextSibling)

,

DOMResult(Node node, Node nextSibling, String systemId)

or

setNextSibling(Node nextSibling)

,
then

null

will be returned.

**Returns:** The child node before which the result nodes will be inserted.
**Since:** 1.5

- setSystemId

```java
public void setSystemId​(
String
systemId)
```

Set the systemId that may be used in association with the node.

**Specified by:** setSystemId

in interface

Result
**Parameters:** systemId

- The system identifier as a URI string.

- getSystemId

```java
public
String
getSystemId()
```

Get the System Identifier.

If no System ID was set via

DOMResult(Node node, String systemId)

,

DOMResult(Node node, Node nextSibling, String systemId)

or

setSystemId(String systemId)

,
then

null

will be returned.

**Specified by:** getSystemId

in interface

Result
**Returns:** The system identifier.

---

#### Method Detail

setNode

```java
public void setNode​(
Node
node)
```

Set the node that will contain the result DOM tree.

In practice, the node should be
a

Document

node,
a

DocumentFragment

node, or
a

Element

node.
In other words, a node that accepts children.

An

IllegalStateException

is thrown if

nextSibling

is not

null

and

node

is not a parent of

nextSibling

.
An

IllegalStateException

is thrown if

node

is

null

and

nextSibling

is not

null

.

**Parameters:** node

- The node to which the transformation will be appended.
**Throws:** IllegalStateException

- If

nextSibling

is not

null

and

nextSibling

is not a child of

node

or

node

is

null

and

nextSibling

is not

null

.

---

#### setNode

public void setNode​(

Node

node)

Set the node that will contain the result DOM tree.

In practice, the node should be
a

Document

node,
a

DocumentFragment

node, or
a

Element

node.
In other words, a node that accepts children.

An

IllegalStateException

is thrown if

nextSibling

is not

null

and

node

is not a parent of

nextSibling

.
An

IllegalStateException

is thrown if

node

is

null

and

nextSibling

is not

null

.

In practice, the node should be
a

Document

node,
a

DocumentFragment

node, or
a

Element

node.
In other words, a node that accepts children.

An

IllegalStateException

is thrown if

nextSibling

is not

null

and

node

is not a parent of

nextSibling

.
An

IllegalStateException

is thrown if

node

is

null

and

nextSibling

is not

null

.

An

IllegalStateException

is thrown if

nextSibling

is not

null

and

node

is not a parent of

nextSibling

.
An

IllegalStateException

is thrown if

node

is

null

and

nextSibling

is not

null

.

getNode

```java
public
Node
getNode()
```

Get the node that will contain the result DOM tree.

If no node was set via

DOMResult(Node node)

,

DOMResult(Node node, String systeId)

,

DOMResult(Node node, Node nextSibling)

,

DOMResult(Node node, Node nextSibling, String systemId)

or

setNode(Node node)

,
then the node will be set by the transformation, and may be obtained from this method once the transformation is complete.
Calling this method before the transformation will return

null

.

**Returns:** The node to which the transformation will be appended.

---

#### getNode

public

Node

getNode()

Get the node that will contain the result DOM tree.

If no node was set via

DOMResult(Node node)

,

DOMResult(Node node, String systeId)

,

DOMResult(Node node, Node nextSibling)

,

DOMResult(Node node, Node nextSibling, String systemId)

or

setNode(Node node)

,
then the node will be set by the transformation, and may be obtained from this method once the transformation is complete.
Calling this method before the transformation will return

null

.

If no node was set via

DOMResult(Node node)

,

DOMResult(Node node, String systeId)

,

DOMResult(Node node, Node nextSibling)

,

DOMResult(Node node, Node nextSibling, String systemId)

or

setNode(Node node)

,
then the node will be set by the transformation, and may be obtained from this method once the transformation is complete.
Calling this method before the transformation will return

null

.

setNextSibling

```java
public void setNextSibling​(
Node
nextSibling)
```

Set the child node before which the result nodes will be inserted.

Use

nextSibling

to specify the child node
before which the result nodes should be inserted.
If

nextSibling

is not a descendant of

node

,
then an

IllegalArgumentException

is thrown.
If

node

is

null

and

nextSibling

is not

null

,
then an

IllegalStateException

is thrown.
If

nextSibling

is

null

,
then the behavior is the same as calling

DOMResult(Node node)

,
i.e. append the result nodes as the last child of the specified

node

.

**Parameters:** nextSibling

- The child node before which the result nodes will be inserted.
**Throws:** IllegalArgumentException

- If

nextSibling

is not a
descendant of

node

.
**Throws:** IllegalStateException

- If

node

is

null

and

nextSibling

is not

null

.
**Since:** 1.5

---

#### setNextSibling

public void setNextSibling​(

Node

nextSibling)

Set the child node before which the result nodes will be inserted.

Use

nextSibling

to specify the child node
before which the result nodes should be inserted.
If

nextSibling

is not a descendant of

node

,
then an

IllegalArgumentException

is thrown.
If

node

is

null

and

nextSibling

is not

null

,
then an

IllegalStateException

is thrown.
If

nextSibling

is

null

,
then the behavior is the same as calling

DOMResult(Node node)

,
i.e. append the result nodes as the last child of the specified

node

.

Use

nextSibling

to specify the child node
before which the result nodes should be inserted.
If

nextSibling

is not a descendant of

node

,
then an

IllegalArgumentException

is thrown.
If

node

is

null

and

nextSibling

is not

null

,
then an

IllegalStateException

is thrown.
If

nextSibling

is

null

,
then the behavior is the same as calling

DOMResult(Node node)

,
i.e. append the result nodes as the last child of the specified

node

.

getNextSibling

```java
public
Node
getNextSibling()
```

Get the child node before which the result nodes will be inserted.

If no node was set via

DOMResult(Node node, Node nextSibling)

,

DOMResult(Node node, Node nextSibling, String systemId)

or

setNextSibling(Node nextSibling)

,
then

null

will be returned.

**Returns:** The child node before which the result nodes will be inserted.
**Since:** 1.5

---

#### getNextSibling

public

Node

getNextSibling()

Get the child node before which the result nodes will be inserted.

If no node was set via

DOMResult(Node node, Node nextSibling)

,

DOMResult(Node node, Node nextSibling, String systemId)

or

setNextSibling(Node nextSibling)

,
then

null

will be returned.

If no node was set via

DOMResult(Node node, Node nextSibling)

,

DOMResult(Node node, Node nextSibling, String systemId)

or

setNextSibling(Node nextSibling)

,
then

null

will be returned.

setSystemId

```java
public void setSystemId​(
String
systemId)
```

Set the systemId that may be used in association with the node.

**Specified by:** setSystemId

in interface

Result
**Parameters:** systemId

- The system identifier as a URI string.

---

#### setSystemId

public void setSystemId​(

String

systemId)

Set the systemId that may be used in association with the node.

getSystemId

```java
public
String
getSystemId()
```

Get the System Identifier.

If no System ID was set via

DOMResult(Node node, String systemId)

,

DOMResult(Node node, Node nextSibling, String systemId)

or

setSystemId(String systemId)

,
then

null

will be returned.

**Specified by:** getSystemId

in interface

Result
**Returns:** The system identifier.

---

#### getSystemId

public

String

getSystemId()

Get the System Identifier.

If no System ID was set via

DOMResult(Node node, String systemId)

,

DOMResult(Node node, Node nextSibling, String systemId)

or

setSystemId(String systemId)

,
then

null

will be returned.

If no System ID was set via

DOMResult(Node node, String systemId)

,

DOMResult(Node node, Node nextSibling, String systemId)

or

setSystemId(String systemId)

,
then

null

will be returned.

---

