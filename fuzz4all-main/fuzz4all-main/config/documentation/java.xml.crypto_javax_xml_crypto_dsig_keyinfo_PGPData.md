# Interface PGPData

**Source:** `java.xml.crypto\javax\xml\crypto\dsig\keyinfo\PGPData.html`

### Class Description

```java
public interface
PGPData

extends
XMLStructure
```

A representation of the XML

PGPData

element as defined in
the

W3C Recommendation for XML-Signature Syntax and Processing

. A

PGPData

object is used to convey information related to
PGP public key pairs and signatures on such keys. The XML Schema Definition
is defined as:

```java
<element name="PGPData" type="ds:PGPDataType"/>
<complexType name="PGPDataType">
<choice>
<sequence>
<element name="PGPKeyID" type="base64Binary"/>
<element name="PGPKeyPacket" type="base64Binary" minOccurs="0"/>
<any namespace="##other" processContents="lax" minOccurs="0"
maxOccurs="unbounded"/>
</sequence>
<sequence>
<element name="PGPKeyPacket" type="base64Binary"/>
<any namespace="##other" processContents="lax" minOccurs="0"
maxOccurs="unbounded"/>
</sequence>
</choice>
</complexType>
```

A

PGPData

instance may be created by invoking one of the

newPGPData

methods of the

KeyInfoFactory

class, and passing it

byte

arrays representing the contents of the PGP public key
identifier and/or PGP key material packet, and an optional list of
elements from an external namespace.

**All Superinterfaces:** XMLStructure

---

### Field Details

#### static final
String
TYPE

URI identifying the PGPData KeyInfo type:
http://www.w3.org/2000/09/xmldsig#PGPData. This can be specified as the
value of the

type

parameter of the

RetrievalMethod

class to describe a remote

PGPData

structure.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### byte[] getKeyId()

Returns the PGP public key identifier of this

PGPData

as
defined in

RFC 2440

,
section 11.2.

**Returns:**
- the PGP public key identifier (may be

null

if
not specified). Each invocation of this method returns a new clone
to protect against subsequent modification.

---

#### byte[] getKeyPacket()

Returns the PGP key material packet of this

PGPData

as
defined in

RFC 2440

,
section 5.5.

**Returns:**
- the PGP key material packet (may be

null

if not
specified). Each invocation of this method returns a new clone to
protect against subsequent modification.

---

#### List
<
XMLStructure
> getExternalElements()

Returns an

unmodifiable list

of

XMLStructure

s representing elements from an external
namespace.

**Returns:**
- an unmodifiable list of

XMLStructure

s (may be
empty, but never

null

)

---

### Additional Sections

#### Interface PGPData

**All Superinterfaces:** XMLStructure

```java
public interface
PGPData

extends
XMLStructure
```

A representation of the XML

PGPData

element as defined in
the

W3C Recommendation for XML-Signature Syntax and Processing

. A

PGPData

object is used to convey information related to
PGP public key pairs and signatures on such keys. The XML Schema Definition
is defined as:

```java
<element name="PGPData" type="ds:PGPDataType"/>
<complexType name="PGPDataType">
<choice>
<sequence>
<element name="PGPKeyID" type="base64Binary"/>
<element name="PGPKeyPacket" type="base64Binary" minOccurs="0"/>
<any namespace="##other" processContents="lax" minOccurs="0"
maxOccurs="unbounded"/>
</sequence>
<sequence>
<element name="PGPKeyPacket" type="base64Binary"/>
<any namespace="##other" processContents="lax" minOccurs="0"
maxOccurs="unbounded"/>
</sequence>
</choice>
</complexType>
```

A

PGPData

instance may be created by invoking one of the

newPGPData

methods of the

KeyInfoFactory

class, and passing it

byte

arrays representing the contents of the PGP public key
identifier and/or PGP key material packet, and an optional list of
elements from an external namespace.

**Since:** 1.6
**See Also:** KeyInfoFactory.newPGPData(byte[])

,

KeyInfoFactory.newPGPData(byte[], byte[], List)

,

KeyInfoFactory.newPGPData(byte[], List)

public interface

PGPData

extends

XMLStructure

A representation of the XML

PGPData

element as defined in
the

W3C Recommendation for XML-Signature Syntax and Processing

. A

PGPData

object is used to convey information related to
PGP public key pairs and signatures on such keys. The XML Schema Definition
is defined as:

```java
<element name="PGPData" type="ds:PGPDataType"/>
<complexType name="PGPDataType">
<choice>
<sequence>
<element name="PGPKeyID" type="base64Binary"/>
<element name="PGPKeyPacket" type="base64Binary" minOccurs="0"/>
<any namespace="##other" processContents="lax" minOccurs="0"
maxOccurs="unbounded"/>
</sequence>
<sequence>
<element name="PGPKeyPacket" type="base64Binary"/>
<any namespace="##other" processContents="lax" minOccurs="0"
maxOccurs="unbounded"/>
</sequence>
</choice>
</complexType>
```

A

PGPData

instance may be created by invoking one of the

newPGPData

methods of the

KeyInfoFactory

class, and passing it

byte

arrays representing the contents of the PGP public key
identifier and/or PGP key material packet, and an optional list of
elements from an external namespace.

<element name="PGPData" type="ds:PGPDataType"/>
<complexType name="PGPDataType">
<choice>
<sequence>
<element name="PGPKeyID" type="base64Binary"/>
<element name="PGPKeyPacket" type="base64Binary" minOccurs="0"/>
<any namespace="##other" processContents="lax" minOccurs="0"
maxOccurs="unbounded"/>
</sequence>
<sequence>
<element name="PGPKeyPacket" type="base64Binary"/>
<any namespace="##other" processContents="lax" minOccurs="0"
maxOccurs="unbounded"/>
</sequence>
</choice>
</complexType>

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

TYPE

URI identifying the PGPData KeyInfo type:
http://www.w3.org/2000/09/xmldsig#PGPData.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

List

<

XMLStructure

>

getExternalElements

()

Returns an

unmodifiable list

of

XMLStructure

s representing elements from an external
namespace.

byte[]

getKeyId

()

Returns the PGP public key identifier of this

PGPData

as
defined in

RFC 2440

,
section 11.2.

byte[]

getKeyPacket

()

Returns the PGP key material packet of this

PGPData

as
defined in

RFC 2440

,
section 5.5.

- Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

Field Summary

Fields

Modifier and Type

Field

Description

static

String

TYPE

URI identifying the PGPData KeyInfo type:
http://www.w3.org/2000/09/xmldsig#PGPData.

---

#### Field Summary

URI identifying the PGPData KeyInfo type:
http://www.w3.org/2000/09/xmldsig#PGPData.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

List

<

XMLStructure

>

getExternalElements

()

Returns an

unmodifiable list

of

XMLStructure

s representing elements from an external
namespace.

byte[]

getKeyId

()

Returns the PGP public key identifier of this

PGPData

as
defined in

RFC 2440

,
section 11.2.

byte[]

getKeyPacket

()

Returns the PGP key material packet of this

PGPData

as
defined in

RFC 2440

,
section 5.5.

- Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

---

#### Method Summary

Returns an

unmodifiable list

of

XMLStructure

s representing elements from an external
namespace.

Returns the PGP public key identifier of this

PGPData

as
defined in

RFC 2440

,
section 11.2.

Returns the PGP key material packet of this

PGPData

as
defined in

RFC 2440

,
section 5.5.

Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

---

#### Methods declared in interface javax.xml.crypto. XMLStructure

============ FIELD DETAIL ===========

- Field Detail

- TYPE

```java
static final
String
TYPE
```

URI identifying the PGPData KeyInfo type:
http://www.w3.org/2000/09/xmldsig#PGPData. This can be specified as the
value of the

type

parameter of the

RetrievalMethod

class to describe a remote

PGPData

structure.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getKeyId

```java
byte[] getKeyId()
```

Returns the PGP public key identifier of this

PGPData

as
defined in

RFC 2440

,
section 11.2.

**Returns:** the PGP public key identifier (may be

null

if
not specified). Each invocation of this method returns a new clone
to protect against subsequent modification.

- getKeyPacket

```java
byte[] getKeyPacket()
```

Returns the PGP key material packet of this

PGPData

as
defined in

RFC 2440

,
section 5.5.

**Returns:** the PGP key material packet (may be

null

if not
specified). Each invocation of this method returns a new clone to
protect against subsequent modification.

- getExternalElements

```java
List
<
XMLStructure
> getExternalElements()
```

Returns an

unmodifiable list

of

XMLStructure

s representing elements from an external
namespace.

**Returns:** an unmodifiable list of

XMLStructure

s (may be
empty, but never

null

)

Field Detail

- TYPE

```java
static final
String
TYPE
```

URI identifying the PGPData KeyInfo type:
http://www.w3.org/2000/09/xmldsig#PGPData. This can be specified as the
value of the

type

parameter of the

RetrievalMethod

class to describe a remote

PGPData

structure.

**See Also:** Constant Field Values

---

#### Field Detail

TYPE

```java
static final
String
TYPE
```

URI identifying the PGPData KeyInfo type:
http://www.w3.org/2000/09/xmldsig#PGPData. This can be specified as the
value of the

type

parameter of the

RetrievalMethod

class to describe a remote

PGPData

structure.

**See Also:** Constant Field Values

---

#### TYPE

static final

String

TYPE

URI identifying the PGPData KeyInfo type:
http://www.w3.org/2000/09/xmldsig#PGPData. This can be specified as the
value of the

type

parameter of the

RetrievalMethod

class to describe a remote

PGPData

structure.

Method Detail

- getKeyId

```java
byte[] getKeyId()
```

Returns the PGP public key identifier of this

PGPData

as
defined in

RFC 2440

,
section 11.2.

**Returns:** the PGP public key identifier (may be

null

if
not specified). Each invocation of this method returns a new clone
to protect against subsequent modification.

- getKeyPacket

```java
byte[] getKeyPacket()
```

Returns the PGP key material packet of this

PGPData

as
defined in

RFC 2440

,
section 5.5.

**Returns:** the PGP key material packet (may be

null

if not
specified). Each invocation of this method returns a new clone to
protect against subsequent modification.

- getExternalElements

```java
List
<
XMLStructure
> getExternalElements()
```

Returns an

unmodifiable list

of

XMLStructure

s representing elements from an external
namespace.

**Returns:** an unmodifiable list of

XMLStructure

s (may be
empty, but never

null

)

---

#### Method Detail

getKeyId

```java
byte[] getKeyId()
```

Returns the PGP public key identifier of this

PGPData

as
defined in

RFC 2440

,
section 11.2.

**Returns:** the PGP public key identifier (may be

null

if
not specified). Each invocation of this method returns a new clone
to protect against subsequent modification.

---

#### getKeyId

byte[] getKeyId()

Returns the PGP public key identifier of this

PGPData

as
defined in

RFC 2440

,
section 11.2.

getKeyPacket

```java
byte[] getKeyPacket()
```

Returns the PGP key material packet of this

PGPData

as
defined in

RFC 2440

,
section 5.5.

**Returns:** the PGP key material packet (may be

null

if not
specified). Each invocation of this method returns a new clone to
protect against subsequent modification.

---

#### getKeyPacket

byte[] getKeyPacket()

Returns the PGP key material packet of this

PGPData

as
defined in

RFC 2440

,
section 5.5.

getExternalElements

```java
List
<
XMLStructure
> getExternalElements()
```

Returns an

unmodifiable list

of

XMLStructure

s representing elements from an external
namespace.

**Returns:** an unmodifiable list of

XMLStructure

s (may be
empty, but never

null

)

---

#### getExternalElements

List

<

XMLStructure

> getExternalElements()

Returns an

unmodifiable list

of

XMLStructure

s representing elements from an external
namespace.

---

