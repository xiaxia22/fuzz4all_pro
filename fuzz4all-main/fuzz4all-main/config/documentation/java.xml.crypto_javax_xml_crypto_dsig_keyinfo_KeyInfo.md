# Interface KeyInfo

**Source:** `java.xml.crypto\javax\xml\crypto\dsig\keyinfo\KeyInfo.html`

### Class Description

```java
public interface
KeyInfo

extends
XMLStructure
```

A representation of the XML

KeyInfo

element as defined in
the

W3C Recommendation for XML-Signature Syntax and Processing

.
A

KeyInfo

contains a list of

XMLStructure

s, each of
which contain information that enables the recipient(s) to obtain the key
needed to validate an XML signature. The XML Schema Definition is defined as:

```java
<element name="KeyInfo" type="ds:KeyInfoType"/>
<complexType name="KeyInfoType" mixed="true">
<choice maxOccurs="unbounded">
<element ref="ds:KeyName"/>
<element ref="ds:KeyValue"/>
<element ref="ds:RetrievalMethod"/>
<element ref="ds:X509Data"/>
<element ref="ds:PGPData"/>
<element ref="ds:SPKIData"/>
<element ref="ds:MgmtData"/>
<any processContents="lax" namespace="##other"/>
<!-- (1,1) elements from (0,unbounded) namespaces -->
</choice>
<attribute name="Id" type="ID" use="optional"/>
</complexType>
```

A

KeyInfo

instance may be created by invoking one of the

newKeyInfo

methods of the

KeyInfoFactory

class, and passing it a list of one or more

XMLStructure

s and an optional id parameter;
for example:

```java
KeyInfoFactory factory = KeyInfoFactory.getInstance("DOM");
KeyInfo keyInfo = factory.newKeyInfo
(Collections.singletonList(factory.newKeyName("Alice"), "keyinfo-1"));
```

KeyInfo

objects can also be marshalled to XML by invoking
the

marshal

method.

**All Superinterfaces:** XMLStructure

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### List
<
XMLStructure
> getContent()

Returns an

unmodifiable
list

containing the key information. Each entry of the list is
an

XMLStructure

.

If there is a public subclass representing the type of

XMLStructure

, it is returned as an instance of that
class (ex: an

X509Data

element would be returned as an
instance of

X509Data

).

**Returns:**
- an unmodifiable list of one or more

XMLStructure

s
in this

KeyInfo

. Never returns

null

or an
empty list.

---

#### String
getId()

Return the optional Id attribute of this

KeyInfo

, which
may be useful for referencing this

KeyInfo

from other
XML structures.

**Returns:**
- the Id attribute of this

KeyInfo

(may be

null

if not specified)

---

#### void marshal​(
XMLStructure
parent,

XMLCryptoContext
context)
throws
MarshalException

Marshals the key info to XML.

**Parameters:**
- parent

- a mechanism-specific structure containing the parent node
that the marshalled key info will be appended to
- context

- the

XMLCryptoContext

containing additional
context (may be null if not applicable)

**Throws:**
- ClassCastException

- if the type of

parent

or

context

is not compatible with this key info
- MarshalException

- if the key info cannot be marshalled
- NullPointerException

- if

parent

is

null

---

### Additional Sections

#### Interface KeyInfo

**All Superinterfaces:** XMLStructure

```java
public interface
KeyInfo

extends
XMLStructure
```

A representation of the XML

KeyInfo

element as defined in
the

W3C Recommendation for XML-Signature Syntax and Processing

.
A

KeyInfo

contains a list of

XMLStructure

s, each of
which contain information that enables the recipient(s) to obtain the key
needed to validate an XML signature. The XML Schema Definition is defined as:

```java
<element name="KeyInfo" type="ds:KeyInfoType"/>
<complexType name="KeyInfoType" mixed="true">
<choice maxOccurs="unbounded">
<element ref="ds:KeyName"/>
<element ref="ds:KeyValue"/>
<element ref="ds:RetrievalMethod"/>
<element ref="ds:X509Data"/>
<element ref="ds:PGPData"/>
<element ref="ds:SPKIData"/>
<element ref="ds:MgmtData"/>
<any processContents="lax" namespace="##other"/>
<!-- (1,1) elements from (0,unbounded) namespaces -->
</choice>
<attribute name="Id" type="ID" use="optional"/>
</complexType>
```

A

KeyInfo

instance may be created by invoking one of the

newKeyInfo

methods of the

KeyInfoFactory

class, and passing it a list of one or more

XMLStructure

s and an optional id parameter;
for example:

```java
KeyInfoFactory factory = KeyInfoFactory.getInstance("DOM");
KeyInfo keyInfo = factory.newKeyInfo
(Collections.singletonList(factory.newKeyName("Alice"), "keyinfo-1"));
```

KeyInfo

objects can also be marshalled to XML by invoking
the

marshal

method.

**Since:** 1.6
**See Also:** KeyInfoFactory.newKeyInfo(List)

,

KeyInfoFactory.newKeyInfo(List, String)

public interface

KeyInfo

extends

XMLStructure

A representation of the XML

KeyInfo

element as defined in
the

W3C Recommendation for XML-Signature Syntax and Processing

.
A

KeyInfo

contains a list of

XMLStructure

s, each of
which contain information that enables the recipient(s) to obtain the key
needed to validate an XML signature. The XML Schema Definition is defined as:

```java
<element name="KeyInfo" type="ds:KeyInfoType"/>
<complexType name="KeyInfoType" mixed="true">
<choice maxOccurs="unbounded">
<element ref="ds:KeyName"/>
<element ref="ds:KeyValue"/>
<element ref="ds:RetrievalMethod"/>
<element ref="ds:X509Data"/>
<element ref="ds:PGPData"/>
<element ref="ds:SPKIData"/>
<element ref="ds:MgmtData"/>
<any processContents="lax" namespace="##other"/>
<!-- (1,1) elements from (0,unbounded) namespaces -->
</choice>
<attribute name="Id" type="ID" use="optional"/>
</complexType>
```

A

KeyInfo

instance may be created by invoking one of the

newKeyInfo

methods of the

KeyInfoFactory

class, and passing it a list of one or more

XMLStructure

s and an optional id parameter;
for example:

```java
KeyInfoFactory factory = KeyInfoFactory.getInstance("DOM");
KeyInfo keyInfo = factory.newKeyInfo
(Collections.singletonList(factory.newKeyName("Alice"), "keyinfo-1"));
```

KeyInfo

objects can also be marshalled to XML by invoking
the

marshal

method.

<element name="KeyInfo" type="ds:KeyInfoType"/>
<complexType name="KeyInfoType" mixed="true">
<choice maxOccurs="unbounded">
<element ref="ds:KeyName"/>
<element ref="ds:KeyValue"/>
<element ref="ds:RetrievalMethod"/>
<element ref="ds:X509Data"/>
<element ref="ds:PGPData"/>
<element ref="ds:SPKIData"/>
<element ref="ds:MgmtData"/>
<any processContents="lax" namespace="##other"/>
<!-- (1,1) elements from (0,unbounded) namespaces -->
</choice>
<attribute name="Id" type="ID" use="optional"/>
</complexType>

KeyInfoFactory factory = KeyInfoFactory.getInstance("DOM");
KeyInfo keyInfo = factory.newKeyInfo
(Collections.singletonList(factory.newKeyName("Alice"), "keyinfo-1"));

KeyInfo

objects can also be marshalled to XML by invoking
the

marshal

method.

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

getContent

()

Returns an

unmodifiable
list

containing the key information.

String

getId

()

Return the optional Id attribute of this

KeyInfo

, which
may be useful for referencing this

KeyInfo

from other
XML structures.

void

marshal

​(

XMLStructure

parent,

XMLCryptoContext

context)

Marshals the key info to XML.

- Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

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

getContent

()

Returns an

unmodifiable
list

containing the key information.

String

getId

()

Return the optional Id attribute of this

KeyInfo

, which
may be useful for referencing this

KeyInfo

from other
XML structures.

void

marshal

​(

XMLStructure

parent,

XMLCryptoContext

context)

Marshals the key info to XML.

- Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

---

#### Method Summary

Returns an

unmodifiable
list

containing the key information.

Return the optional Id attribute of this

KeyInfo

, which
may be useful for referencing this

KeyInfo

from other
XML structures.

Marshals the key info to XML.

Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

---

#### Methods declared in interface javax.xml.crypto. XMLStructure

============ METHOD DETAIL ==========

- Method Detail

- getContent

```java
List
<
XMLStructure
> getContent()
```

Returns an

unmodifiable
list

containing the key information. Each entry of the list is
an

XMLStructure

.

If there is a public subclass representing the type of

XMLStructure

, it is returned as an instance of that
class (ex: an

X509Data

element would be returned as an
instance of

X509Data

).

**Returns:** an unmodifiable list of one or more

XMLStructure

s
in this

KeyInfo

. Never returns

null

or an
empty list.

- getId

```java
String
getId()
```

Return the optional Id attribute of this

KeyInfo

, which
may be useful for referencing this

KeyInfo

from other
XML structures.

**Returns:** the Id attribute of this

KeyInfo

(may be

null

if not specified)

- marshal

```java
void marshal​(
XMLStructure
parent,

XMLCryptoContext
context)
throws
MarshalException
```

Marshals the key info to XML.

**Parameters:** parent

- a mechanism-specific structure containing the parent node
that the marshalled key info will be appended to
**Parameters:** context

- the

XMLCryptoContext

containing additional
context (may be null if not applicable)
**Throws:** ClassCastException

- if the type of

parent

or

context

is not compatible with this key info
**Throws:** MarshalException

- if the key info cannot be marshalled
**Throws:** NullPointerException

- if

parent

is

null

Method Detail

- getContent

```java
List
<
XMLStructure
> getContent()
```

Returns an

unmodifiable
list

containing the key information. Each entry of the list is
an

XMLStructure

.

If there is a public subclass representing the type of

XMLStructure

, it is returned as an instance of that
class (ex: an

X509Data

element would be returned as an
instance of

X509Data

).

**Returns:** an unmodifiable list of one or more

XMLStructure

s
in this

KeyInfo

. Never returns

null

or an
empty list.

- getId

```java
String
getId()
```

Return the optional Id attribute of this

KeyInfo

, which
may be useful for referencing this

KeyInfo

from other
XML structures.

**Returns:** the Id attribute of this

KeyInfo

(may be

null

if not specified)

- marshal

```java
void marshal​(
XMLStructure
parent,

XMLCryptoContext
context)
throws
MarshalException
```

Marshals the key info to XML.

**Parameters:** parent

- a mechanism-specific structure containing the parent node
that the marshalled key info will be appended to
**Parameters:** context

- the

XMLCryptoContext

containing additional
context (may be null if not applicable)
**Throws:** ClassCastException

- if the type of

parent

or

context

is not compatible with this key info
**Throws:** MarshalException

- if the key info cannot be marshalled
**Throws:** NullPointerException

- if

parent

is

null

---

#### Method Detail

getContent

```java
List
<
XMLStructure
> getContent()
```

Returns an

unmodifiable
list

containing the key information. Each entry of the list is
an

XMLStructure

.

If there is a public subclass representing the type of

XMLStructure

, it is returned as an instance of that
class (ex: an

X509Data

element would be returned as an
instance of

X509Data

).

**Returns:** an unmodifiable list of one or more

XMLStructure

s
in this

KeyInfo

. Never returns

null

or an
empty list.

---

#### getContent

List

<

XMLStructure

> getContent()

Returns an

unmodifiable
list

containing the key information. Each entry of the list is
an

XMLStructure

.

If there is a public subclass representing the type of

XMLStructure

, it is returned as an instance of that
class (ex: an

X509Data

element would be returned as an
instance of

X509Data

).

If there is a public subclass representing the type of

XMLStructure

, it is returned as an instance of that
class (ex: an

X509Data

element would be returned as an
instance of

X509Data

).

getId

```java
String
getId()
```

Return the optional Id attribute of this

KeyInfo

, which
may be useful for referencing this

KeyInfo

from other
XML structures.

**Returns:** the Id attribute of this

KeyInfo

(may be

null

if not specified)

---

#### getId

String

getId()

Return the optional Id attribute of this

KeyInfo

, which
may be useful for referencing this

KeyInfo

from other
XML structures.

marshal

```java
void marshal​(
XMLStructure
parent,

XMLCryptoContext
context)
throws
MarshalException
```

Marshals the key info to XML.

**Parameters:** parent

- a mechanism-specific structure containing the parent node
that the marshalled key info will be appended to
**Parameters:** context

- the

XMLCryptoContext

containing additional
context (may be null if not applicable)
**Throws:** ClassCastException

- if the type of

parent

or

context

is not compatible with this key info
**Throws:** MarshalException

- if the key info cannot be marshalled
**Throws:** NullPointerException

- if

parent

is

null

---

#### marshal

void marshal​(

XMLStructure

parent,

XMLCryptoContext

context)
throws

MarshalException

Marshals the key info to XML.

---

