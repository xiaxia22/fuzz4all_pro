# Class DOMValidateContext

**Source:** `java.xml.crypto\javax\xml\crypto\dsig\dom\DOMValidateContext.html`

### Class Description

```java
public class
DOMValidateContext

extends
DOMCryptoContext

implements
XMLValidateContext
```

A DOM-specific

XMLValidateContext

. This class contains additional
methods to specify the location in a DOM tree where an

XMLSignature

is to be unmarshalled and validated from.

Note that the behavior of an unmarshalled

XMLSignature

is undefined if the contents of the underlying DOM tree are modified by the
caller after the

XMLSignature

is created.

Also, note that

DOMValidateContext

instances can contain
information and state specific to the XML signature structure it is
used with. The results are unpredictable if a

DOMValidateContext

is used with different signature structures
(for example, you should not use the same

DOMValidateContext

instance to validate two different

XMLSignature

objects).

**All Implemented Interfaces:** XMLValidateContext

,

XMLCryptoContext

---

### Field Details

*No entries found.*

### Constructor Details

#### public DOMValidateContext​(
KeySelector
ks,

Node
node)

Creates a

DOMValidateContext

containing the specified key
selector and node.

**Parameters:**
- ks

- a key selector for finding a validation key
- node

- the node

**Throws:**
- NullPointerException

- if

ks

or

node

is

null

---

#### public DOMValidateContext​(
Key
validatingKey,

Node
node)

Creates a

DOMValidateContext

containing the specified key
and node. The validating key will be stored in a

singleton KeySelector

that
is returned when the

getKeySelector

method is called.

**Parameters:**
- validatingKey

- the validating key
- node

- the node

**Throws:**
- NullPointerException

- if

validatingKey

or

node

is

null

---

### Method Details

#### public void setNode​(
Node
node)

Sets the node.

**Parameters:**
- node

- the node

**Throws:**
- NullPointerException

- if

node

is

null

**See Also:**
- getNode()

---

#### public
Node
getNode()

Returns the node.

**Returns:**
- the node (never

null

)

**See Also:**
- setNode(Node)

---

### Additional Sections

#### Class DOMValidateContext

java.lang.Object

- javax.xml.crypto.dom.DOMCryptoContext
- - javax.xml.crypto.dsig.dom.DOMValidateContext

javax.xml.crypto.dom.DOMCryptoContext

- javax.xml.crypto.dsig.dom.DOMValidateContext

javax.xml.crypto.dsig.dom.DOMValidateContext

**All Implemented Interfaces:** XMLValidateContext

,

XMLCryptoContext

```java
public class
DOMValidateContext

extends
DOMCryptoContext

implements
XMLValidateContext
```

A DOM-specific

XMLValidateContext

. This class contains additional
methods to specify the location in a DOM tree where an

XMLSignature

is to be unmarshalled and validated from.

Note that the behavior of an unmarshalled

XMLSignature

is undefined if the contents of the underlying DOM tree are modified by the
caller after the

XMLSignature

is created.

Also, note that

DOMValidateContext

instances can contain
information and state specific to the XML signature structure it is
used with. The results are unpredictable if a

DOMValidateContext

is used with different signature structures
(for example, you should not use the same

DOMValidateContext

instance to validate two different

XMLSignature

objects).

**Implementation Note:** The JDK implementation supports a secure validation mode which can be
enabled by setting the

org.jcp.xml.dsig.secureValidation

property
to

Boolean.TRUE

(see the

setProperty

method).
When enabled, validation of XML signatures are subject to stricter checking
of algorithms and other constraints as specified by the

jdk.xml.dsig.secureValidationPolicy

security property.
The mode can be disabled by setting the property to

Boolean.FALSE

.
The mode can also be enabled or disabled by setting the
org.jcp.xml.dsig.secureValidation system property to "true" or "false".
Any other value for the system property is also treated as "false".
If the system property is set, it supersedes the

DOMValidateContext

property value. The secure validation mode is
enabled by default if you are running code with a SecurityManager, otherwise
it is disabled by default.
**Since:** 1.6
**See Also:** XMLSignatureFactory.unmarshalXMLSignature(XMLValidateContext)

public class

DOMValidateContext

extends

DOMCryptoContext

implements

XMLValidateContext

A DOM-specific

XMLValidateContext

. This class contains additional
methods to specify the location in a DOM tree where an

XMLSignature

is to be unmarshalled and validated from.

Note that the behavior of an unmarshalled

XMLSignature

is undefined if the contents of the underlying DOM tree are modified by the
caller after the

XMLSignature

is created.

Also, note that

DOMValidateContext

instances can contain
information and state specific to the XML signature structure it is
used with. The results are unpredictable if a

DOMValidateContext

is used with different signature structures
(for example, you should not use the same

DOMValidateContext

instance to validate two different

XMLSignature

objects).

Note that the behavior of an unmarshalled

XMLSignature

is undefined if the contents of the underlying DOM tree are modified by the
caller after the

XMLSignature

is created.

Also, note that

DOMValidateContext

instances can contain
information and state specific to the XML signature structure it is
used with. The results are unpredictable if a

DOMValidateContext

is used with different signature structures
(for example, you should not use the same

DOMValidateContext

instance to validate two different

XMLSignature

objects).

Also, note that

DOMValidateContext

instances can contain
information and state specific to the XML signature structure it is
used with. The results are unpredictable if a

DOMValidateContext

is used with different signature structures
(for example, you should not use the same

DOMValidateContext

instance to validate two different

XMLSignature

objects).

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DOMValidateContext

​(

Key

validatingKey,

Node

node)

Creates a

DOMValidateContext

containing the specified key
and node.

DOMValidateContext

​(

KeySelector

ks,

Node

node)

Creates a

DOMValidateContext

containing the specified key
selector and node.

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

Returns the node.

void

setNode

​(

Node

node)

Sets the node.

- Methods declared in class javax.xml.crypto.dom.

DOMCryptoContext

get

,

getElementById

,

getNamespacePrefix

,

getProperty

,

iterator

,

put

,

putNamespacePrefix

,

setBaseURI

,

setIdAttributeNS

,

setProperty

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

- Methods declared in interface javax.xml.crypto.

XMLCryptoContext

get

,

getBaseURI

,

getDefaultNamespacePrefix

,

getKeySelector

,

getNamespacePrefix

,

getProperty

,

getURIDereferencer

,

put

,

putNamespacePrefix

,

setBaseURI

,

setDefaultNamespacePrefix

,

setKeySelector

,

setProperty

,

setURIDereferencer

Constructor Summary

Constructors

Constructor

Description

DOMValidateContext

​(

Key

validatingKey,

Node

node)

Creates a

DOMValidateContext

containing the specified key
and node.

DOMValidateContext

​(

KeySelector

ks,

Node

node)

Creates a

DOMValidateContext

containing the specified key
selector and node.

---

#### Constructor Summary

Creates a

DOMValidateContext

containing the specified key
and node.

Creates a

DOMValidateContext

containing the specified key
selector and node.

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

Returns the node.

void

setNode

​(

Node

node)

Sets the node.

- Methods declared in class javax.xml.crypto.dom.

DOMCryptoContext

get

,

getElementById

,

getNamespacePrefix

,

getProperty

,

iterator

,

put

,

putNamespacePrefix

,

setBaseURI

,

setIdAttributeNS

,

setProperty

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

- Methods declared in interface javax.xml.crypto.

XMLCryptoContext

get

,

getBaseURI

,

getDefaultNamespacePrefix

,

getKeySelector

,

getNamespacePrefix

,

getProperty

,

getURIDereferencer

,

put

,

putNamespacePrefix

,

setBaseURI

,

setDefaultNamespacePrefix

,

setKeySelector

,

setProperty

,

setURIDereferencer

---

#### Method Summary

Returns the node.

Sets the node.

Methods declared in class javax.xml.crypto.dom.

DOMCryptoContext

get

,

getElementById

,

getNamespacePrefix

,

getProperty

,

iterator

,

put

,

putNamespacePrefix

,

setBaseURI

,

setIdAttributeNS

,

setProperty

---

#### Methods declared in class javax.xml.crypto.dom. DOMCryptoContext

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

Methods declared in interface javax.xml.crypto.

XMLCryptoContext

get

,

getBaseURI

,

getDefaultNamespacePrefix

,

getKeySelector

,

getNamespacePrefix

,

getProperty

,

getURIDereferencer

,

put

,

putNamespacePrefix

,

setBaseURI

,

setDefaultNamespacePrefix

,

setKeySelector

,

setProperty

,

setURIDereferencer

---

#### Methods declared in interface javax.xml.crypto. XMLCryptoContext

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DOMValidateContext

```java
public DOMValidateContext​(
KeySelector
ks,

Node
node)
```

Creates a

DOMValidateContext

containing the specified key
selector and node.

**Parameters:** ks

- a key selector for finding a validation key
**Parameters:** node

- the node
**Throws:** NullPointerException

- if

ks

or

node

is

null

- DOMValidateContext

```java
public DOMValidateContext​(
Key
validatingKey,

Node
node)
```

Creates a

DOMValidateContext

containing the specified key
and node. The validating key will be stored in a

singleton KeySelector

that
is returned when the

getKeySelector

method is called.

**Parameters:** validatingKey

- the validating key
**Parameters:** node

- the node
**Throws:** NullPointerException

- if

validatingKey

or

node

is

null

============ METHOD DETAIL ==========

- Method Detail

- setNode

```java
public void setNode​(
Node
node)
```

Sets the node.

**Parameters:** node

- the node
**Throws:** NullPointerException

- if

node

is

null
**See Also:** getNode()

- getNode

```java
public
Node
getNode()
```

Returns the node.

**Returns:** the node (never

null

)
**See Also:** setNode(Node)

Constructor Detail

- DOMValidateContext

```java
public DOMValidateContext​(
KeySelector
ks,

Node
node)
```

Creates a

DOMValidateContext

containing the specified key
selector and node.

**Parameters:** ks

- a key selector for finding a validation key
**Parameters:** node

- the node
**Throws:** NullPointerException

- if

ks

or

node

is

null

- DOMValidateContext

```java
public DOMValidateContext​(
Key
validatingKey,

Node
node)
```

Creates a

DOMValidateContext

containing the specified key
and node. The validating key will be stored in a

singleton KeySelector

that
is returned when the

getKeySelector

method is called.

**Parameters:** validatingKey

- the validating key
**Parameters:** node

- the node
**Throws:** NullPointerException

- if

validatingKey

or

node

is

null

---

#### Constructor Detail

DOMValidateContext

```java
public DOMValidateContext​(
KeySelector
ks,

Node
node)
```

Creates a

DOMValidateContext

containing the specified key
selector and node.

**Parameters:** ks

- a key selector for finding a validation key
**Parameters:** node

- the node
**Throws:** NullPointerException

- if

ks

or

node

is

null

---

#### DOMValidateContext

public DOMValidateContext​(

KeySelector

ks,

Node

node)

Creates a

DOMValidateContext

containing the specified key
selector and node.

DOMValidateContext

```java
public DOMValidateContext​(
Key
validatingKey,

Node
node)
```

Creates a

DOMValidateContext

containing the specified key
and node. The validating key will be stored in a

singleton KeySelector

that
is returned when the

getKeySelector

method is called.

**Parameters:** validatingKey

- the validating key
**Parameters:** node

- the node
**Throws:** NullPointerException

- if

validatingKey

or

node

is

null

---

#### DOMValidateContext

public DOMValidateContext​(

Key

validatingKey,

Node

node)

Creates a

DOMValidateContext

containing the specified key
and node. The validating key will be stored in a

singleton KeySelector

that
is returned when the

getKeySelector

method is called.

Method Detail

- setNode

```java
public void setNode​(
Node
node)
```

Sets the node.

**Parameters:** node

- the node
**Throws:** NullPointerException

- if

node

is

null
**See Also:** getNode()

- getNode

```java
public
Node
getNode()
```

Returns the node.

**Returns:** the node (never

null

)
**See Also:** setNode(Node)

---

#### Method Detail

setNode

```java
public void setNode​(
Node
node)
```

Sets the node.

**Parameters:** node

- the node
**Throws:** NullPointerException

- if

node

is

null
**See Also:** getNode()

---

#### setNode

public void setNode​(

Node

node)

Sets the node.

getNode

```java
public
Node
getNode()
```

Returns the node.

**Returns:** the node (never

null

)
**See Also:** setNode(Node)

---

#### getNode

public

Node

getNode()

Returns the node.

---

