# Class DOMSource

**Source:** `java.xml\javax\xml\transform\dom\DOMSource.html`

### Class Description

```java
public class
DOMSource

extends
Object

implements
Source
```

Acts as a holder for a transformation Source tree in the
form of a Document Object Model (DOM) tree.

Note that XSLT requires namespace support. Attempting to transform a DOM
that was not contructed with a namespace-aware parser may result in errors.
Parsers can be made namespace aware by calling

DocumentBuilderFactory.setNamespaceAware(boolean awareness)

.

**All Implemented Interfaces:** Source

---

### Field Details

#### public static final
String
FEATURE

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the Transformer supports Source input of this type.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public DOMSource()

Zero-argument default constructor. If this constructor is used, and
no DOM source is set using

setNode(Node node)

, then the

Transformer

will
create an empty source

Document

using

DocumentBuilder.newDocument()

.

**See Also:**
- Transformer.transform(Source xmlSource, Result outputTarget)

---

#### public DOMSource​(
Node
n)

Create a new input source with a DOM node. The operation
will be applied to the subtree rooted at this node. In XSLT,
a "/" pattern still means the root of the tree (not the subtree),
and the evaluation of global variables and parameters is done
from the root node also.

**Parameters:**
- n

- The DOM node that will contain the Source tree.

---

#### public DOMSource​(
Node
node,

String
systemID)

Create a new input source with a DOM node, and with the
system ID also passed in as the base URI.

**Parameters:**
- node

- The DOM node that will contain the Source tree.
- systemID

- Specifies the base URI associated with node.

---

### Method Details

#### public void setNode​(
Node
node)

Set the node that will represents a Source DOM tree.

**Parameters:**
- node

- The node that is to be transformed.

---

#### public
Node
getNode()

Get the node that represents a Source DOM tree.

**Returns:**
- The node that is to be transformed.

---

#### public void setSystemId​(
String
systemID)

Set the base ID (URL or system ID) from where URLs
will be resolved.

**Specified by:**
- setSystemId

in interface

Source

**Parameters:**
- systemID

- Base URL for this DOM tree.

---

#### public
String
getSystemId()

Get the base ID (URL or system ID) from where URLs
will be resolved.

**Specified by:**
- getSystemId

in interface

Source

**Returns:**
- Base URL for this DOM tree.

---

#### public boolean isEmpty()

Indicates whether the

DOMSource

object is empty. Empty is
defined as follows:

- if the system identifier and node are

null

;
- if the system identifier is null, and the

node

has no child nodes.

**Specified by:**
- isEmpty

in interface

Source

**Returns:**
- true if the

DOMSource

object is empty, false otherwise

---

### Additional Sections

#### Class DOMSource

java.lang.Object

- javax.xml.transform.dom.DOMSource

javax.xml.transform.dom.DOMSource

**All Implemented Interfaces:** Source

```java
public class
DOMSource

extends
Object

implements
Source
```

Acts as a holder for a transformation Source tree in the
form of a Document Object Model (DOM) tree.

Note that XSLT requires namespace support. Attempting to transform a DOM
that was not contructed with a namespace-aware parser may result in errors.
Parsers can be made namespace aware by calling

DocumentBuilderFactory.setNamespaceAware(boolean awareness)

.

**Since:** 1.4
**See Also:** Document Object Model (DOM) Level 2 Specification

public class

DOMSource

extends

Object

implements

Source

Acts as a holder for a transformation Source tree in the
form of a Document Object Model (DOM) tree.

Note that XSLT requires namespace support. Attempting to transform a DOM
that was not contructed with a namespace-aware parser may result in errors.
Parsers can be made namespace aware by calling

DocumentBuilderFactory.setNamespaceAware(boolean awareness)

.

Acts as a holder for a transformation Source tree in the
form of a Document Object Model (DOM) tree.

Note that XSLT requires namespace support. Attempting to transform a DOM
that was not contructed with a namespace-aware parser may result in errors.
Parsers can be made namespace aware by calling

DocumentBuilderFactory.setNamespaceAware(boolean awareness)

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

returns true when passed this value as an argument,
the Transformer supports Source input of this type.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DOMSource

()

Zero-argument default constructor.

DOMSource

​(

Node

n)

Create a new input source with a DOM node.

DOMSource

​(

Node

node,

String

systemID)

Create a new input source with a DOM node, and with the
system ID also passed in as the base URI.

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

Get the node that represents a Source DOM tree.

String

getSystemId

()

Get the base ID (URL or system ID) from where URLs
will be resolved.

boolean

isEmpty

()

Indicates whether the

DOMSource

object is empty.

void

setNode

​(

Node

node)

Set the node that will represents a Source DOM tree.

void

setSystemId

​(

String

systemID)

Set the base ID (URL or system ID) from where URLs
will be resolved.

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

returns true when passed this value as an argument,
the Transformer supports Source input of this type.

---

#### Field Summary

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the Transformer supports Source input of this type.

Constructor Summary

Constructors

Constructor

Description

DOMSource

()

Zero-argument default constructor.

DOMSource

​(

Node

n)

Create a new input source with a DOM node.

DOMSource

​(

Node

node,

String

systemID)

Create a new input source with a DOM node, and with the
system ID also passed in as the base URI.

---

#### Constructor Summary

Zero-argument default constructor.

Create a new input source with a DOM node.

Create a new input source with a DOM node, and with the
system ID also passed in as the base URI.

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

Get the node that represents a Source DOM tree.

String

getSystemId

()

Get the base ID (URL or system ID) from where URLs
will be resolved.

boolean

isEmpty

()

Indicates whether the

DOMSource

object is empty.

void

setNode

​(

Node

node)

Set the node that will represents a Source DOM tree.

void

setSystemId

​(

String

systemID)

Set the base ID (URL or system ID) from where URLs
will be resolved.

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

Get the node that represents a Source DOM tree.

Get the base ID (URL or system ID) from where URLs
will be resolved.

Indicates whether the

DOMSource

object is empty.

Set the node that will represents a Source DOM tree.

Set the base ID (URL or system ID) from where URLs
will be resolved.

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

returns true when passed this value as an argument,
the Transformer supports Source input of this type.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DOMSource

```java
public DOMSource()
```

Zero-argument default constructor. If this constructor is used, and
no DOM source is set using

setNode(Node node)

, then the

Transformer

will
create an empty source

Document

using

DocumentBuilder.newDocument()

.

**See Also:** Transformer.transform(Source xmlSource, Result outputTarget)

- DOMSource

```java
public DOMSource​(
Node
n)
```

Create a new input source with a DOM node. The operation
will be applied to the subtree rooted at this node. In XSLT,
a "/" pattern still means the root of the tree (not the subtree),
and the evaluation of global variables and parameters is done
from the root node also.

**Parameters:** n

- The DOM node that will contain the Source tree.

- DOMSource

```java
public DOMSource​(
Node
node,

String
systemID)
```

Create a new input source with a DOM node, and with the
system ID also passed in as the base URI.

**Parameters:** node

- The DOM node that will contain the Source tree.
**Parameters:** systemID

- Specifies the base URI associated with node.

============ METHOD DETAIL ==========

- Method Detail

- setNode

```java
public void setNode​(
Node
node)
```

Set the node that will represents a Source DOM tree.

**Parameters:** node

- The node that is to be transformed.

- getNode

```java
public
Node
getNode()
```

Get the node that represents a Source DOM tree.

**Returns:** The node that is to be transformed.

- setSystemId

```java
public void setSystemId​(
String
systemID)
```

Set the base ID (URL or system ID) from where URLs
will be resolved.

**Specified by:** setSystemId

in interface

Source
**Parameters:** systemID

- Base URL for this DOM tree.

- getSystemId

```java
public
String
getSystemId()
```

Get the base ID (URL or system ID) from where URLs
will be resolved.

**Specified by:** getSystemId

in interface

Source
**Returns:** Base URL for this DOM tree.

- isEmpty

```java
public boolean isEmpty()
```

Indicates whether the

DOMSource

object is empty. Empty is
defined as follows:

- if the system identifier and node are

null

;
- if the system identifier is null, and the

node

has no child nodes.

**Specified by:** isEmpty

in interface

Source
**Returns:** true if the

DOMSource

object is empty, false otherwise

Field Detail

- FEATURE

```java
public static final
String
FEATURE
```

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the Transformer supports Source input of this type.

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

returns true when passed this value as an argument,
the Transformer supports Source input of this type.

**See Also:** Constant Field Values

---

#### FEATURE

public static final

String

FEATURE

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the Transformer supports Source input of this type.

Constructor Detail

- DOMSource

```java
public DOMSource()
```

Zero-argument default constructor. If this constructor is used, and
no DOM source is set using

setNode(Node node)

, then the

Transformer

will
create an empty source

Document

using

DocumentBuilder.newDocument()

.

**See Also:** Transformer.transform(Source xmlSource, Result outputTarget)

- DOMSource

```java
public DOMSource​(
Node
n)
```

Create a new input source with a DOM node. The operation
will be applied to the subtree rooted at this node. In XSLT,
a "/" pattern still means the root of the tree (not the subtree),
and the evaluation of global variables and parameters is done
from the root node also.

**Parameters:** n

- The DOM node that will contain the Source tree.

- DOMSource

```java
public DOMSource​(
Node
node,

String
systemID)
```

Create a new input source with a DOM node, and with the
system ID also passed in as the base URI.

**Parameters:** node

- The DOM node that will contain the Source tree.
**Parameters:** systemID

- Specifies the base URI associated with node.

---

#### Constructor Detail

DOMSource

```java
public DOMSource()
```

Zero-argument default constructor. If this constructor is used, and
no DOM source is set using

setNode(Node node)

, then the

Transformer

will
create an empty source

Document

using

DocumentBuilder.newDocument()

.

**See Also:** Transformer.transform(Source xmlSource, Result outputTarget)

---

#### DOMSource

public DOMSource()

Zero-argument default constructor. If this constructor is used, and
no DOM source is set using

setNode(Node node)

, then the

Transformer

will
create an empty source

Document

using

DocumentBuilder.newDocument()

.

DOMSource

```java
public DOMSource​(
Node
n)
```

Create a new input source with a DOM node. The operation
will be applied to the subtree rooted at this node. In XSLT,
a "/" pattern still means the root of the tree (not the subtree),
and the evaluation of global variables and parameters is done
from the root node also.

**Parameters:** n

- The DOM node that will contain the Source tree.

---

#### DOMSource

public DOMSource​(

Node

n)

Create a new input source with a DOM node. The operation
will be applied to the subtree rooted at this node. In XSLT,
a "/" pattern still means the root of the tree (not the subtree),
and the evaluation of global variables and parameters is done
from the root node also.

DOMSource

```java
public DOMSource​(
Node
node,

String
systemID)
```

Create a new input source with a DOM node, and with the
system ID also passed in as the base URI.

**Parameters:** node

- The DOM node that will contain the Source tree.
**Parameters:** systemID

- Specifies the base URI associated with node.

---

#### DOMSource

public DOMSource​(

Node

node,

String

systemID)

Create a new input source with a DOM node, and with the
system ID also passed in as the base URI.

Method Detail

- setNode

```java
public void setNode​(
Node
node)
```

Set the node that will represents a Source DOM tree.

**Parameters:** node

- The node that is to be transformed.

- getNode

```java
public
Node
getNode()
```

Get the node that represents a Source DOM tree.

**Returns:** The node that is to be transformed.

- setSystemId

```java
public void setSystemId​(
String
systemID)
```

Set the base ID (URL or system ID) from where URLs
will be resolved.

**Specified by:** setSystemId

in interface

Source
**Parameters:** systemID

- Base URL for this DOM tree.

- getSystemId

```java
public
String
getSystemId()
```

Get the base ID (URL or system ID) from where URLs
will be resolved.

**Specified by:** getSystemId

in interface

Source
**Returns:** Base URL for this DOM tree.

- isEmpty

```java
public boolean isEmpty()
```

Indicates whether the

DOMSource

object is empty. Empty is
defined as follows:

- if the system identifier and node are

null

;
- if the system identifier is null, and the

node

has no child nodes.

**Specified by:** isEmpty

in interface

Source
**Returns:** true if the

DOMSource

object is empty, false otherwise

---

#### Method Detail

setNode

```java
public void setNode​(
Node
node)
```

Set the node that will represents a Source DOM tree.

**Parameters:** node

- The node that is to be transformed.

---

#### setNode

public void setNode​(

Node

node)

Set the node that will represents a Source DOM tree.

getNode

```java
public
Node
getNode()
```

Get the node that represents a Source DOM tree.

**Returns:** The node that is to be transformed.

---

#### getNode

public

Node

getNode()

Get the node that represents a Source DOM tree.

setSystemId

```java
public void setSystemId​(
String
systemID)
```

Set the base ID (URL or system ID) from where URLs
will be resolved.

**Specified by:** setSystemId

in interface

Source
**Parameters:** systemID

- Base URL for this DOM tree.

---

#### setSystemId

public void setSystemId​(

String

systemID)

Set the base ID (URL or system ID) from where URLs
will be resolved.

getSystemId

```java
public
String
getSystemId()
```

Get the base ID (URL or system ID) from where URLs
will be resolved.

**Specified by:** getSystemId

in interface

Source
**Returns:** Base URL for this DOM tree.

---

#### getSystemId

public

String

getSystemId()

Get the base ID (URL or system ID) from where URLs
will be resolved.

isEmpty

```java
public boolean isEmpty()
```

Indicates whether the

DOMSource

object is empty. Empty is
defined as follows:

- if the system identifier and node are

null

;
- if the system identifier is null, and the

node

has no child nodes.

**Specified by:** isEmpty

in interface

Source
**Returns:** true if the

DOMSource

object is empty, false otherwise

---

#### isEmpty

public boolean isEmpty()

Indicates whether the

DOMSource

object is empty. Empty is
defined as follows:

- if the system identifier and node are

null

;
- if the system identifier is null, and the

node

has no child nodes.

if the system identifier and node are

null

;

if the system identifier is null, and the

node

has no child nodes.

---

