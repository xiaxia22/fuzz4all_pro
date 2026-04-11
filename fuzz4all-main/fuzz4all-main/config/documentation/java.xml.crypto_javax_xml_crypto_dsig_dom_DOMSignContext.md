# Class DOMSignContext

**Source:** `java.xml.crypto\javax\xml\crypto\dsig\dom\DOMSignContext.html`

### Class Description

```java
public class
DOMSignContext

extends
DOMCryptoContext

implements
XMLSignContext
```

A DOM-specific

XMLSignContext

. This class contains additional methods
to specify the location in a DOM tree where an

XMLSignature

object is to be marshalled when generating the signature.

Note that

DOMSignContext

instances can contain
information and state specific to the XML signature structure it is
used with. The results are unpredictable if a

DOMSignContext

is used with different signature structures
(for example, you should not use the same

DOMSignContext

instance to sign two different

XMLSignature

objects).

**All Implemented Interfaces:** XMLSignContext

,

XMLCryptoContext

---

### Field Details

*No entries found.*

### Constructor Details

#### public DOMSignContext​(
Key
signingKey,

Node
parent)

Creates a

DOMSignContext

with the specified signing key
and parent node. The signing key is stored in a

singleton KeySelector

that is
returned by the

getKeySelector

method.
The marshalled

XMLSignature

will be added as the last
child element of the specified parent node unless a next sibling node is
specified by invoking the

setNextSibling

method.

**Parameters:**
- signingKey

- the signing key
- parent

- the parent node

**Throws:**
- NullPointerException

- if

signingKey

or

parent

is

null

---

#### public DOMSignContext​(
Key
signingKey,

Node
parent,

Node
nextSibling)

Creates a

DOMSignContext

with the specified signing key,
parent and next sibling nodes. The signing key is stored in a

singleton KeySelector

that is
returned by the

getKeySelector

method.
The marshalled

XMLSignature

will be inserted as a child
element of the specified parent node and immediately before the
specified next sibling node.

**Parameters:**
- signingKey

- the signing key
- parent

- the parent node
- nextSibling

- the next sibling node

**Throws:**
- NullPointerException

- if

signingKey

,

parent

or

nextSibling

is

null

---

#### public DOMSignContext​(
KeySelector
ks,

Node
parent)

Creates a

DOMSignContext

with the specified key selector
and parent node. The marshalled

XMLSignature

will be added
as the last child element of the specified parent node unless a next
sibling node is specified by invoking the

setNextSibling

method.

**Parameters:**
- ks

- the key selector
- parent

- the parent node

**Throws:**
- NullPointerException

- if

ks

or

parent

is

null

---

#### public DOMSignContext​(
KeySelector
ks,

Node
parent,

Node
nextSibling)

Creates a

DOMSignContext

with the specified key selector,
parent and next sibling nodes. The marshalled

XMLSignature

will be inserted as a child element of the specified parent node and
immediately before the specified next sibling node.

**Parameters:**
- ks

- the key selector
- parent

- the parent node
- nextSibling

- the next sibling node

**Throws:**
- NullPointerException

- if

ks

,

parent

or

nextSibling

is

null

---

### Method Details

#### public void setParent​(
Node
parent)

Sets the parent node.

**Parameters:**
- parent

- the parent node. The marshalled

XMLSignature

will be added as a child element of this node.

**Throws:**
- NullPointerException

- if

parent

is

null

**See Also:**
- getParent()

---

#### public void setNextSibling​(
Node
nextSibling)

Sets the next sibling node.

**Parameters:**
- nextSibling

- the next sibling node. The marshalled

XMLSignature

will be inserted immediately before this
node. Specify

null

to remove the current setting.

**See Also:**
- getNextSibling()

---

#### public
Node
getParent()

Returns the parent node.

**Returns:**
- the parent node (never

null

)

**See Also:**
- setParent(Node)

---

#### public
Node
getNextSibling()

Returns the nextSibling node.

**Returns:**
- the nextSibling node, or

null

if not specified.

**See Also:**
- setNextSibling(Node)

---

### Additional Sections

#### Class DOMSignContext

java.lang.Object

- javax.xml.crypto.dom.DOMCryptoContext
- - javax.xml.crypto.dsig.dom.DOMSignContext

javax.xml.crypto.dom.DOMCryptoContext

- javax.xml.crypto.dsig.dom.DOMSignContext

javax.xml.crypto.dsig.dom.DOMSignContext

**All Implemented Interfaces:** XMLSignContext

,

XMLCryptoContext

```java
public class
DOMSignContext

extends
DOMCryptoContext

implements
XMLSignContext
```

A DOM-specific

XMLSignContext

. This class contains additional methods
to specify the location in a DOM tree where an

XMLSignature

object is to be marshalled when generating the signature.

Note that

DOMSignContext

instances can contain
information and state specific to the XML signature structure it is
used with. The results are unpredictable if a

DOMSignContext

is used with different signature structures
(for example, you should not use the same

DOMSignContext

instance to sign two different

XMLSignature

objects).

**Since:** 1.6

public class

DOMSignContext

extends

DOMCryptoContext

implements

XMLSignContext

A DOM-specific

XMLSignContext

. This class contains additional methods
to specify the location in a DOM tree where an

XMLSignature

object is to be marshalled when generating the signature.

Note that

DOMSignContext

instances can contain
information and state specific to the XML signature structure it is
used with. The results are unpredictable if a

DOMSignContext

is used with different signature structures
(for example, you should not use the same

DOMSignContext

instance to sign two different

XMLSignature

objects).

Note that

DOMSignContext

instances can contain
information and state specific to the XML signature structure it is
used with. The results are unpredictable if a

DOMSignContext

is used with different signature structures
(for example, you should not use the same

DOMSignContext

instance to sign two different

XMLSignature

objects).

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DOMSignContext

​(

Key

signingKey,

Node

parent)

Creates a

DOMSignContext

with the specified signing key
and parent node.

DOMSignContext

​(

Key

signingKey,

Node

parent,

Node

nextSibling)

Creates a

DOMSignContext

with the specified signing key,
parent and next sibling nodes.

DOMSignContext

​(

KeySelector

ks,

Node

parent)

Creates a

DOMSignContext

with the specified key selector
and parent node.

DOMSignContext

​(

KeySelector

ks,

Node

parent,

Node

nextSibling)

Creates a

DOMSignContext

with the specified key selector,
parent and next sibling nodes.

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

Returns the nextSibling node.

Node

getParent

()

Returns the parent node.

void

setNextSibling

​(

Node

nextSibling)

Sets the next sibling node.

void

setParent

​(

Node

parent)

Sets the parent node.

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

DOMSignContext

​(

Key

signingKey,

Node

parent)

Creates a

DOMSignContext

with the specified signing key
and parent node.

DOMSignContext

​(

Key

signingKey,

Node

parent,

Node

nextSibling)

Creates a

DOMSignContext

with the specified signing key,
parent and next sibling nodes.

DOMSignContext

​(

KeySelector

ks,

Node

parent)

Creates a

DOMSignContext

with the specified key selector
and parent node.

DOMSignContext

​(

KeySelector

ks,

Node

parent,

Node

nextSibling)

Creates a

DOMSignContext

with the specified key selector,
parent and next sibling nodes.

---

#### Constructor Summary

Creates a

DOMSignContext

with the specified signing key
and parent node.

Creates a

DOMSignContext

with the specified signing key,
parent and next sibling nodes.

Creates a

DOMSignContext

with the specified key selector
and parent node.

Creates a

DOMSignContext

with the specified key selector,
parent and next sibling nodes.

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

Returns the nextSibling node.

Node

getParent

()

Returns the parent node.

void

setNextSibling

​(

Node

nextSibling)

Sets the next sibling node.

void

setParent

​(

Node

parent)

Sets the parent node.

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

Returns the nextSibling node.

Returns the parent node.

Sets the next sibling node.

Sets the parent node.

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

- DOMSignContext

```java
public DOMSignContext​(
Key
signingKey,

Node
parent)
```

Creates a

DOMSignContext

with the specified signing key
and parent node. The signing key is stored in a

singleton KeySelector

that is
returned by the

getKeySelector

method.
The marshalled

XMLSignature

will be added as the last
child element of the specified parent node unless a next sibling node is
specified by invoking the

setNextSibling

method.

**Parameters:** signingKey

- the signing key
**Parameters:** parent

- the parent node
**Throws:** NullPointerException

- if

signingKey

or

parent

is

null

- DOMSignContext

```java
public DOMSignContext​(
Key
signingKey,

Node
parent,

Node
nextSibling)
```

Creates a

DOMSignContext

with the specified signing key,
parent and next sibling nodes. The signing key is stored in a

singleton KeySelector

that is
returned by the

getKeySelector

method.
The marshalled

XMLSignature

will be inserted as a child
element of the specified parent node and immediately before the
specified next sibling node.

**Parameters:** signingKey

- the signing key
**Parameters:** parent

- the parent node
**Parameters:** nextSibling

- the next sibling node
**Throws:** NullPointerException

- if

signingKey

,

parent

or

nextSibling

is

null

- DOMSignContext

```java
public DOMSignContext​(
KeySelector
ks,

Node
parent)
```

Creates a

DOMSignContext

with the specified key selector
and parent node. The marshalled

XMLSignature

will be added
as the last child element of the specified parent node unless a next
sibling node is specified by invoking the

setNextSibling

method.

**Parameters:** ks

- the key selector
**Parameters:** parent

- the parent node
**Throws:** NullPointerException

- if

ks

or

parent

is

null

- DOMSignContext

```java
public DOMSignContext​(
KeySelector
ks,

Node
parent,

Node
nextSibling)
```

Creates a

DOMSignContext

with the specified key selector,
parent and next sibling nodes. The marshalled

XMLSignature

will be inserted as a child element of the specified parent node and
immediately before the specified next sibling node.

**Parameters:** ks

- the key selector
**Parameters:** parent

- the parent node
**Parameters:** nextSibling

- the next sibling node
**Throws:** NullPointerException

- if

ks

,

parent

or

nextSibling

is

null

============ METHOD DETAIL ==========

- Method Detail

- setParent

```java
public void setParent​(
Node
parent)
```

Sets the parent node.

**Parameters:** parent

- the parent node. The marshalled

XMLSignature

will be added as a child element of this node.
**Throws:** NullPointerException

- if

parent

is

null
**See Also:** getParent()

- setNextSibling

```java
public void setNextSibling​(
Node
nextSibling)
```

Sets the next sibling node.

**Parameters:** nextSibling

- the next sibling node. The marshalled

XMLSignature

will be inserted immediately before this
node. Specify

null

to remove the current setting.
**See Also:** getNextSibling()

- getParent

```java
public
Node
getParent()
```

Returns the parent node.

**Returns:** the parent node (never

null

)
**See Also:** setParent(Node)

- getNextSibling

```java
public
Node
getNextSibling()
```

Returns the nextSibling node.

**Returns:** the nextSibling node, or

null

if not specified.
**See Also:** setNextSibling(Node)

Constructor Detail

- DOMSignContext

```java
public DOMSignContext​(
Key
signingKey,

Node
parent)
```

Creates a

DOMSignContext

with the specified signing key
and parent node. The signing key is stored in a

singleton KeySelector

that is
returned by the

getKeySelector

method.
The marshalled

XMLSignature

will be added as the last
child element of the specified parent node unless a next sibling node is
specified by invoking the

setNextSibling

method.

**Parameters:** signingKey

- the signing key
**Parameters:** parent

- the parent node
**Throws:** NullPointerException

- if

signingKey

or

parent

is

null

- DOMSignContext

```java
public DOMSignContext​(
Key
signingKey,

Node
parent,

Node
nextSibling)
```

Creates a

DOMSignContext

with the specified signing key,
parent and next sibling nodes. The signing key is stored in a

singleton KeySelector

that is
returned by the

getKeySelector

method.
The marshalled

XMLSignature

will be inserted as a child
element of the specified parent node and immediately before the
specified next sibling node.

**Parameters:** signingKey

- the signing key
**Parameters:** parent

- the parent node
**Parameters:** nextSibling

- the next sibling node
**Throws:** NullPointerException

- if

signingKey

,

parent

or

nextSibling

is

null

- DOMSignContext

```java
public DOMSignContext​(
KeySelector
ks,

Node
parent)
```

Creates a

DOMSignContext

with the specified key selector
and parent node. The marshalled

XMLSignature

will be added
as the last child element of the specified parent node unless a next
sibling node is specified by invoking the

setNextSibling

method.

**Parameters:** ks

- the key selector
**Parameters:** parent

- the parent node
**Throws:** NullPointerException

- if

ks

or

parent

is

null

- DOMSignContext

```java
public DOMSignContext​(
KeySelector
ks,

Node
parent,

Node
nextSibling)
```

Creates a

DOMSignContext

with the specified key selector,
parent and next sibling nodes. The marshalled

XMLSignature

will be inserted as a child element of the specified parent node and
immediately before the specified next sibling node.

**Parameters:** ks

- the key selector
**Parameters:** parent

- the parent node
**Parameters:** nextSibling

- the next sibling node
**Throws:** NullPointerException

- if

ks

,

parent

or

nextSibling

is

null

---

#### Constructor Detail

DOMSignContext

```java
public DOMSignContext​(
Key
signingKey,

Node
parent)
```

Creates a

DOMSignContext

with the specified signing key
and parent node. The signing key is stored in a

singleton KeySelector

that is
returned by the

getKeySelector

method.
The marshalled

XMLSignature

will be added as the last
child element of the specified parent node unless a next sibling node is
specified by invoking the

setNextSibling

method.

**Parameters:** signingKey

- the signing key
**Parameters:** parent

- the parent node
**Throws:** NullPointerException

- if

signingKey

or

parent

is

null

---

#### DOMSignContext

public DOMSignContext​(

Key

signingKey,

Node

parent)

Creates a

DOMSignContext

with the specified signing key
and parent node. The signing key is stored in a

singleton KeySelector

that is
returned by the

getKeySelector

method.
The marshalled

XMLSignature

will be added as the last
child element of the specified parent node unless a next sibling node is
specified by invoking the

setNextSibling

method.

DOMSignContext

```java
public DOMSignContext​(
Key
signingKey,

Node
parent,

Node
nextSibling)
```

Creates a

DOMSignContext

with the specified signing key,
parent and next sibling nodes. The signing key is stored in a

singleton KeySelector

that is
returned by the

getKeySelector

method.
The marshalled

XMLSignature

will be inserted as a child
element of the specified parent node and immediately before the
specified next sibling node.

**Parameters:** signingKey

- the signing key
**Parameters:** parent

- the parent node
**Parameters:** nextSibling

- the next sibling node
**Throws:** NullPointerException

- if

signingKey

,

parent

or

nextSibling

is

null

---

#### DOMSignContext

public DOMSignContext​(

Key

signingKey,

Node

parent,

Node

nextSibling)

Creates a

DOMSignContext

with the specified signing key,
parent and next sibling nodes. The signing key is stored in a

singleton KeySelector

that is
returned by the

getKeySelector

method.
The marshalled

XMLSignature

will be inserted as a child
element of the specified parent node and immediately before the
specified next sibling node.

DOMSignContext

```java
public DOMSignContext​(
KeySelector
ks,

Node
parent)
```

Creates a

DOMSignContext

with the specified key selector
and parent node. The marshalled

XMLSignature

will be added
as the last child element of the specified parent node unless a next
sibling node is specified by invoking the

setNextSibling

method.

**Parameters:** ks

- the key selector
**Parameters:** parent

- the parent node
**Throws:** NullPointerException

- if

ks

or

parent

is

null

---

#### DOMSignContext

public DOMSignContext​(

KeySelector

ks,

Node

parent)

Creates a

DOMSignContext

with the specified key selector
and parent node. The marshalled

XMLSignature

will be added
as the last child element of the specified parent node unless a next
sibling node is specified by invoking the

setNextSibling

method.

DOMSignContext

```java
public DOMSignContext​(
KeySelector
ks,

Node
parent,

Node
nextSibling)
```

Creates a

DOMSignContext

with the specified key selector,
parent and next sibling nodes. The marshalled

XMLSignature

will be inserted as a child element of the specified parent node and
immediately before the specified next sibling node.

**Parameters:** ks

- the key selector
**Parameters:** parent

- the parent node
**Parameters:** nextSibling

- the next sibling node
**Throws:** NullPointerException

- if

ks

,

parent

or

nextSibling

is

null

---

#### DOMSignContext

public DOMSignContext​(

KeySelector

ks,

Node

parent,

Node

nextSibling)

Creates a

DOMSignContext

with the specified key selector,
parent and next sibling nodes. The marshalled

XMLSignature

will be inserted as a child element of the specified parent node and
immediately before the specified next sibling node.

Method Detail

- setParent

```java
public void setParent​(
Node
parent)
```

Sets the parent node.

**Parameters:** parent

- the parent node. The marshalled

XMLSignature

will be added as a child element of this node.
**Throws:** NullPointerException

- if

parent

is

null
**See Also:** getParent()

- setNextSibling

```java
public void setNextSibling​(
Node
nextSibling)
```

Sets the next sibling node.

**Parameters:** nextSibling

- the next sibling node. The marshalled

XMLSignature

will be inserted immediately before this
node. Specify

null

to remove the current setting.
**See Also:** getNextSibling()

- getParent

```java
public
Node
getParent()
```

Returns the parent node.

**Returns:** the parent node (never

null

)
**See Also:** setParent(Node)

- getNextSibling

```java
public
Node
getNextSibling()
```

Returns the nextSibling node.

**Returns:** the nextSibling node, or

null

if not specified.
**See Also:** setNextSibling(Node)

---

#### Method Detail

setParent

```java
public void setParent​(
Node
parent)
```

Sets the parent node.

**Parameters:** parent

- the parent node. The marshalled

XMLSignature

will be added as a child element of this node.
**Throws:** NullPointerException

- if

parent

is

null
**See Also:** getParent()

---

#### setParent

public void setParent​(

Node

parent)

Sets the parent node.

setNextSibling

```java
public void setNextSibling​(
Node
nextSibling)
```

Sets the next sibling node.

**Parameters:** nextSibling

- the next sibling node. The marshalled

XMLSignature

will be inserted immediately before this
node. Specify

null

to remove the current setting.
**See Also:** getNextSibling()

---

#### setNextSibling

public void setNextSibling​(

Node

nextSibling)

Sets the next sibling node.

getParent

```java
public
Node
getParent()
```

Returns the parent node.

**Returns:** the parent node (never

null

)
**See Also:** setParent(Node)

---

#### getParent

public

Node

getParent()

Returns the parent node.

getNextSibling

```java
public
Node
getNextSibling()
```

Returns the nextSibling node.

**Returns:** the nextSibling node, or

null

if not specified.
**See Also:** setNextSibling(Node)

---

#### getNextSibling

public

Node

getNextSibling()

Returns the nextSibling node.

---

