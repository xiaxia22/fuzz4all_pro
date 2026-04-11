# Class DOMStructure

**Source:** `java.xml.crypto\javax\xml\crypto\dom\DOMStructure.html`

### Class Description

```java
public class
DOMStructure

extends
Object

implements
XMLStructure
```

A DOM-specific

XMLStructure

. The purpose of this class is to
allow a DOM node to be used to represent extensible content (any elements
or mixed content) in XML Signature structures.

If a sequence of nodes is needed, the node contained in the

DOMStructure

is the first node of the sequence and successive
nodes can be accessed by invoking

Node.getNextSibling()

.

If the owner document of the

DOMStructure

is different than
the target document of an

XMLSignature

, the

XMLSignature.sign(XMLSignContext)

method imports the node into the
target document before generating the signature.

**All Implemented Interfaces:** XMLStructure

---

### Field Details

*No entries found.*

### Constructor Details

#### public DOMStructure​(
Node
node)

Creates a

DOMStructure

containing the specified node.

**Parameters:**
- node

- the node

**Throws:**
- NullPointerException

- if

node

is

null

---

### Method Details

#### public
Node
getNode()

Returns the node contained in this

DOMStructure

.

**Returns:**
- the node

---

#### public boolean isFeatureSupported​(
String
feature)

Description copied from interface:

XMLStructure

**Specified by:**
- isFeatureSupported

in interface

XMLStructure

**Parameters:**
- feature

- the feature name (as an absolute URI)

**Returns:**
- true

if the specified feature is supported,

false

otherwise

**Throws:**
- NullPointerException

- if

feature

is

null

---

### Additional Sections

#### Class DOMStructure

java.lang.Object

- javax.xml.crypto.dom.DOMStructure

javax.xml.crypto.dom.DOMStructure

**All Implemented Interfaces:** XMLStructure

```java
public class
DOMStructure

extends
Object

implements
XMLStructure
```

A DOM-specific

XMLStructure

. The purpose of this class is to
allow a DOM node to be used to represent extensible content (any elements
or mixed content) in XML Signature structures.

If a sequence of nodes is needed, the node contained in the

DOMStructure

is the first node of the sequence and successive
nodes can be accessed by invoking

Node.getNextSibling()

.

If the owner document of the

DOMStructure

is different than
the target document of an

XMLSignature

, the

XMLSignature.sign(XMLSignContext)

method imports the node into the
target document before generating the signature.

**Since:** 1.6

public class

DOMStructure

extends

Object

implements

XMLStructure

A DOM-specific

XMLStructure

. The purpose of this class is to
allow a DOM node to be used to represent extensible content (any elements
or mixed content) in XML Signature structures.

If a sequence of nodes is needed, the node contained in the

DOMStructure

is the first node of the sequence and successive
nodes can be accessed by invoking

Node.getNextSibling()

.

If the owner document of the

DOMStructure

is different than
the target document of an

XMLSignature

, the

XMLSignature.sign(XMLSignContext)

method imports the node into the
target document before generating the signature.

If a sequence of nodes is needed, the node contained in the

DOMStructure

is the first node of the sequence and successive
nodes can be accessed by invoking

Node.getNextSibling()

.

If the owner document of the

DOMStructure

is different than
the target document of an

XMLSignature

, the

XMLSignature.sign(XMLSignContext)

method imports the node into the
target document before generating the signature.

If the owner document of the

DOMStructure

is different than
the target document of an

XMLSignature

, the

XMLSignature.sign(XMLSignContext)

method imports the node into the
target document before generating the signature.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DOMStructure

​(

Node

node)

Creates a

DOMStructure

containing the specified node.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Node

getNode

()

Returns the node contained in this

DOMStructure

.

boolean

isFeatureSupported

​(

String

feature)

Indicates whether a specified feature is supported.

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

Constructor Summary

Constructors

Constructor

Description

DOMStructure

​(

Node

node)

Creates a

DOMStructure

containing the specified node.

---

#### Constructor Summary

Creates a

DOMStructure

containing the specified node.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Node

getNode

()

Returns the node contained in this

DOMStructure

.

boolean

isFeatureSupported

​(

String

feature)

Indicates whether a specified feature is supported.

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

Returns the node contained in this

DOMStructure

.

Indicates whether a specified feature is supported.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DOMStructure

```java
public DOMStructure​(
Node
node)
```

Creates a

DOMStructure

containing the specified node.

**Parameters:** node

- the node
**Throws:** NullPointerException

- if

node

is

null

============ METHOD DETAIL ==========

- Method Detail

- getNode

```java
public
Node
getNode()
```

Returns the node contained in this

DOMStructure

.

**Returns:** the node

- isFeatureSupported

```java
public boolean isFeatureSupported​(
String
feature)
```

Description copied from interface:

XMLStructure

Indicates whether a specified feature is supported.

**Specified by:** isFeatureSupported

in interface

XMLStructure
**Parameters:** feature

- the feature name (as an absolute URI)
**Returns:** true

if the specified feature is supported,

false

otherwise
**Throws:** NullPointerException

- if

feature

is

null

Constructor Detail

- DOMStructure

```java
public DOMStructure​(
Node
node)
```

Creates a

DOMStructure

containing the specified node.

**Parameters:** node

- the node
**Throws:** NullPointerException

- if

node

is

null

---

#### Constructor Detail

DOMStructure

```java
public DOMStructure​(
Node
node)
```

Creates a

DOMStructure

containing the specified node.

**Parameters:** node

- the node
**Throws:** NullPointerException

- if

node

is

null

---

#### DOMStructure

public DOMStructure​(

Node

node)

Creates a

DOMStructure

containing the specified node.

Method Detail

- getNode

```java
public
Node
getNode()
```

Returns the node contained in this

DOMStructure

.

**Returns:** the node

- isFeatureSupported

```java
public boolean isFeatureSupported​(
String
feature)
```

Description copied from interface:

XMLStructure

Indicates whether a specified feature is supported.

**Specified by:** isFeatureSupported

in interface

XMLStructure
**Parameters:** feature

- the feature name (as an absolute URI)
**Returns:** true

if the specified feature is supported,

false

otherwise
**Throws:** NullPointerException

- if

feature

is

null

---

#### Method Detail

getNode

```java
public
Node
getNode()
```

Returns the node contained in this

DOMStructure

.

**Returns:** the node

---

#### getNode

public

Node

getNode()

Returns the node contained in this

DOMStructure

.

isFeatureSupported

```java
public boolean isFeatureSupported​(
String
feature)
```

Description copied from interface:

XMLStructure

Indicates whether a specified feature is supported.

**Specified by:** isFeatureSupported

in interface

XMLStructure
**Parameters:** feature

- the feature name (as an absolute URI)
**Returns:** true

if the specified feature is supported,

false

otherwise
**Throws:** NullPointerException

- if

feature

is

null

---

#### isFeatureSupported

public boolean isFeatureSupported​(

String

feature)

Description copied from interface:

XMLStructure

Indicates whether a specified feature is supported.

---

